from dnd_constants import MAGIC_ARROW_STR, ROPE_STR, PIT_STR, DRAGON_STR, BAT_STR
from game_direction_class import NORTH, SOUTH, EAST, WEST
from mock_game_class import MockGame
from test_basic_play import functest_move_and_move_back

def test_bat(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    mock_game.set_mock_bat(move=2, location="G5", fly_to="C7")
    assert mock_game.get_bat_fly_to(move=2,location="G5") == "C7"
    assert mock_game.get_bat_fly_to(move=2,location="G6") == ""
    assert mock_game.get_bat_fly_to(move=1,location="G5") == ""



def test_bat_danger(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    mock_game.set_mock_bat(move=3, location="G6", fly_to="C7")
    action_1 = mock_game.do_action_move(EAST,"G4 - not near bats")
    assert BAT_STR not in action_1.result.nearby
    action_2 = mock_game.do_action_move(EAST,"G5 - not near bats")
    assert BAT_STR in action_2.result.nearby
    action_3 = mock_game.do_action_move(EAST,"G6 - bat will fly to C7")
    assert action_3.result.location == "C7"



#TODO: Find actual status
def test_pit(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    assert_danger_over(mock_game, PIT_STR)

def test_dragon(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    assert_danger_over(mock_game,DRAGON_STR)

def test_pit_with_rope(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    mock_game.set_mock_object_location(ROPE_STR, "G4")
    mock_game.set_mock_object_location(PIT_STR, "G5")

    action_1 = mock_game.do_action_move(EAST, "G4 - pick up rope")
    assert action_1.result.status == "Alive"

    action_2 = mock_game.do_action_move(EAST, "G5 - pit with rope")
    assert action_2.result.status == "Alive"

    action_3 = mock_game.do_action_move(EAST, "G5 - moves with rope")
    assert action_3.result.status == "Alive"
    assert action_3.result.location == "G6"

    action_4 = mock_game.do_action_move(WEST,"Back to G5 - pit without rope")
    assert action_4.result.status != "Alive"
    assert action_4.result.location == "G5"

    action_5 = mock_game.do_action_move(NORTH,"G5 - cannot move")
    assert action_5.result.status != "Alive"
    assert action_5.result.location == "G5"


def assert_danger_over(mock_game, obj):
    mock_game.set_mock_object_location(obj, "G5")
    action_1 = mock_game.do_action_move(EAST, "G4 - no pit")
    assert action_1.result.status == "Alive"
    action_2 = mock_game.do_action_move(EAST, "G5 - pit")
    assert action_2.result.status != "Alive"
    action_3 = mock_game.do_action_move(EAST, "G5 - cannot move")
    assert action_3.result.status != "Alive"
    assert action_3.result.location == "G5"


def test_inventory(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    mock_game.set_mock_object_location(MAGIC_ARROW_STR,"G5")
    mock_game.set_mock_object_location(ROPE_STR, "G7")

    mock_game.do_action_move(EAST,"G4")
    action = mock_game.get_last_action()
    assert action.result.inventory == []

    mock_game.do_action_move(EAST,"G5, pick up arrow")
    action = mock_game.get_last_action()
    assert action.result.inventory == [MAGIC_ARROW_STR]

    mock_game.do_action_move(EAST,"G6, still have arrow")
    action = mock_game.get_last_action()
    assert action.result.inventory == [MAGIC_ARROW_STR]

    mock_game.do_action_move(EAST,"G7, pick up rope")
    action = mock_game.get_last_action()
    assert action.result.inventory == [MAGIC_ARROW_STR,ROPE_STR]

    mock_game.do_action_move(EAST,"G8, still have rope and arrow")
    action = mock_game.get_last_action()
    assert action.result.inventory == [MAGIC_ARROW_STR,ROPE_STR]

def test_safe_nearby(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    start_cell = mock_game.get_actions()[0].result
    assert start_cell.nearby == ""

def test_object_nearby_functions(safe_mock_game_g3_setup_teardown):
    game = safe_mock_game_g3_setup_teardown
    for dnd_object in (PIT_STR, DRAGON_STR, MAGIC_ARROW_STR, PIT_STR):
        assert_nearby_for_each_adjacent_location(game, dnd_object)

def assert_object_nearby(cell, object_str):
    if object_str == DRAGON_STR:
        return cell.is_dragon_nearby()
    elif object_str == MAGIC_ARROW_STR:
        return cell.is_magic_arrow_nearby()
    elif object_str == PIT_STR:
        return cell.is_pit_nearby()
    elif object_str == ROPE_STR:
        return cell.is_rope_nearby()
    else:
        assert False

def assert_nearby_for_each_adjacent_location(mock_game, dnd_object):
    mock_game.set_mock_object_location(dnd_object, "F3")
    g2_cell = mock_game.make_mock_cell("G2")
    assert g2_cell.nearby == ""
    for location in mock_game.get_adjacent_locations_all("F3"):
        cell = mock_game.make_mock_cell(location)
        assert_object_nearby(cell, dnd_object)


def test_mock_create_game_start_g3():
    mock_game = MockGame("G3")
    action_and_result = mock_game.get_actions()[0]
    cell_visited = mock_game.get_cells_visited()["G3"]
    assert action_and_result.action == "restart"
    assert cell_visited.location == "G3"
    assert action_and_result.result.location == "G3"
    assert cell_visited.inventory == []


def test_mock_move_in_all_directions(safe_mock_game_g3_setup_teardown):
    game = safe_mock_game_g3_setup_teardown
    functest_move_and_move_back(game=game, direction=NORTH)
    functest_move_and_move_back(game=game, direction=SOUTH)
    functest_move_and_move_back(game=game, direction=EAST)
    functest_move_and_move_back(game=game, direction=WEST)