from dnd_constants import MAGIC_ARROW_STR, ROPE_STR, DRAGON_STR, PIT_STR
from game_direction_class import NORTH, EAST, WEST
from mock_game_class import MockGame
from mock_game_utility import derive_mock_game


def test_mock_pick_up_arrow(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, MAGIC_ARROW_STR)

def test_mock_pick_up_rope(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, ROPE_STR)

def test_mock_move_to_dragon(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, DRAGON_STR)

def test_mock_move_to_pit(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    assert_move_to_obj(game_orig, PIT_STR)

def test_adjacent_cells_all_safe(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    action = game_orig.do_action_move(EAST, "Go to G4")
    adjacent_locations_g3 = game_orig.get_adjacent_locations_all("G3")
    adjacent_locations_g4 = game_orig.get_adjacent_locations_all("G4")
    adjacent_locations_g3_g4_set = set(adjacent_locations_g3) | set(adjacent_locations_g4)
    # TODO change derive_mock_game to move to class and not return any value OR don't store at all in game and just use get function
    game_derived: MockGame = derive_mock_game(game_orig)
    for location in adjacent_locations_g3_g4_set:
        assert game_orig.get_derived_content_of_location(location) == []

    assert_play_game_same_results(game_derived, game_orig)


def test_pick_up_rope_go_to_pit(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    action = game_orig.set_mock_object_location(ROPE_STR, "F5")
    action = game_orig.set_mock_object_location(PIT_STR, "F6")
    action = game_orig.do_action_move(EAST, "Go to G4")
    action = game_orig.do_action_move(EAST, "Go to G5")
    action = game_orig.do_action_move(NORTH, "Go to F5 pick up rope")
    action = game_orig.do_action_move(EAST, "Go to F6 to pit")
    action = game_orig.do_action_move(WEST, "Go to F5 with rope")
    assert action.result.location == "F5"
    action = game_orig.do_action_move(EAST, "Go to F6 to pit")
    assert action.result.location == "F6"
    action = game_orig.do_action_move(NORTH,"Fail to climb out of pit")
    assert action.result.location == "F6"
    game_derived: MockGame = derive_mock_game(game_orig)
    assert_play_game_same_results(game_derived, game_orig)

def test_pick_up_rope_and_arrow(safe_mock_game_g3_setup_teardown):
    game_orig = safe_mock_game_g3_setup_teardown
    action = game_orig.set_mock_object_location(ROPE_STR, "F5")
    action = game_orig.set_mock_object_location(MAGIC_ARROW_STR, "F6")
    action = game_orig.do_action_move(EAST, "Go to G4")
    action = game_orig.do_action_move(EAST, "Go to G5")
    action = game_orig.do_action_move(NORTH, "Go to F5 pick up rope")
    action = game_orig.do_action_move(EAST, "Go to F6 to pick up rope")
    action = game_orig.do_action_move(NORTH, "Go to E5")
    assert action.result.inventory == [ROPE_STR,MAGIC_ARROW_STR]
    game_derived: MockGame = derive_mock_game(game_orig)
    assert_play_game_same_results(game_derived, game_orig)

def assert_move_to_obj(game_orig, obj_str):
    game_orig.set_mock_object_location(obj_str, "F5")
    game_orig.do_action_move(EAST, "Go to G4")
    game_orig.do_action_move(EAST, "Go to G5")
    game_orig.do_action_move(NORTH, "Go to F5 pick up "+obj_str)
    game_orig.do_action_move(EAST, "Go to F6")
    game_derived: MockGame = derive_mock_game(game_orig)
    assert game_derived.get_mock_object_location(obj_str) == ["F5"]
    assert_play_game_same_results(game_derived, game_orig)


def assert_play_game_same_results(game_derived, game_orig):
    orig_action_objs = game_orig.get_actions()
    for action_index in range(1, len(orig_action_objs)):
        action = game_orig.get_action(action_index)
        game_derived.do_action_move(action.direction, "Test mock simple game")
    for action_index in range(0, len(orig_action_objs)):
        orig_action_obj = game_orig.get_action(action_index)
        derived_action_obj = game_derived.get_action(action_index)
        assert orig_action_obj.key_field_equals(derived_action_obj)


def test_derive_mock_game_start(safe_mock_game_g3_setup_teardown):
    original_game = safe_mock_game_g3_setup_teardown
    original_action = original_game.get_actions()[0]
    original_location = original_action.result.location
    mock_game = derive_mock_game(original_game)
    mock_action_and_result = mock_game.get_actions()[0]
    cell_visited = mock_game.get_cells_visited()[original_location]
    assert mock_action_and_result.action == "restart"
    assert cell_visited.location == original_location
    assert mock_action_and_result.result.location == original_location