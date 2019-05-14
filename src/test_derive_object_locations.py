from dnd_constants import MAGIC_ARROW, ROPE, DRAGON, PIT
from game_direction_class import EAST, NORTH
from mock_game_class import MockGame
from test_basic_play import TEST_ACCOUNT_UID
from mock_game_utility import derive_mock_game
from d_and_d_utility import create_move_actions_to_take

def test_derive_bat(safe_mock_game_g3_setup_teardown):
    mock_game = safe_mock_game_g3_setup_teardown
    mock_game.set_mock_bat(move=3, location="G6", fly_to="C7")
    action_1 = mock_game.do_action_move(EAST,"G4 - not near bats")
    action_2 = mock_game.do_action_move(EAST,"G5 - not near bats")
    action_3 = mock_game.do_action_move(EAST,"G6 - bat will fly to C7")
    mock_game.derive_contents()
    assert mock_game.get_derived_fly_to(action_index=3, bat_location="G6") == "C7"
    assert len(mock_game.get_derived_fly_tos()) == 1




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

def test_derive_visited_dragon():
    mock_game:MockGame = MockGame("G3")
    mock_game.set_mock_object_location(DRAGON, "G5")
    mock_game.do_action_move(EAST,"G4 - empty cell")
    mock_game.do_action_move(EAST,"G5 - Dragon")
    mock_game.derive_contents()
    assert mock_game.get_derived_contents()["G5"] == [DRAGON.value]

def test_derive_visited_pit():
    mock_game:MockGame = MockGame("G3")
    mock_game.set_mock_object_location(PIT, "G5")
    mock_game.do_action_move(EAST,"G4 - empty cell")
    mock_game.do_action_move(EAST,"G5 - Dragon")
    mock_game.derive_contents()
    assert mock_game.get_derived_contents()["G5"] == [PIT.value]

def test_derive_picked_up_inventory():
    mock_game:MockGame = MockGame("G3")
    mock_game.set_mock_object_location(MAGIC_ARROW, "G5")
    mock_game.set_mock_object_location(ROPE, "G7")
    mock_game.do_action_move(EAST,"G4 - empty cell")
    mock_game.do_action_move(EAST,"G5 - Magic Arrow")
    mock_game.do_action_move(EAST,"G6 - Empty Cell")
    mock_game.do_action_move(EAST,"G7 - Rope")
    mock_game.do_action_move(EAST,"G8 - Empty cell")
    mock_game.derive_contents()
    assert mock_game.get_derived_contents()["G4"] == []
    assert mock_game.get_derived_contents()["G5"] == [MAGIC_ARROW.value]
    assert mock_game.get_derived_contents()["G6"] == []
    assert mock_game.get_derived_contents()["G7"] == [ROPE.value]
    assert mock_game.get_derived_contents()["G8"] == []
