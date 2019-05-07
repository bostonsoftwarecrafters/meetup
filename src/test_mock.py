from d_and_d_class import DNDGame
from d_and_d_utility import location_in_direction_of
from mock_game_class import MockGame
from test_basic_play import TEST_ACCOUNT_UID
from test_directions import NORTH, SOUTH, WEST, EAST


def test_mock_create_game():
    # game = DandDGame(TEST_ACCOUNT_UID)
    mock_game = MockGame(TEST_ACCOUNT_UID)
    assert isinstance(mock_game, DNDGame)
    assert len(mock_game.get_action_history()) == 1
    assert len(mock_game.get_cells_visited()) == 1

def test_define_init_cell():
    mock_game = MockGame(TEST_ACCOUNT_UID, location="G3")
    action_and_result = mock_game.get_action_history()[0]
    cell_visited = mock_game.get_cells_visited()["G3"]
    assert action_and_result.action == "restart"
    assert cell_visited.location == "G3"
    assert action_and_result.result.location == "G3"

def test_mock_all_directions():
    game = MockGame(TEST_ACCOUNT_UID)
    start_cell = game.get_action(0).result
    north_cell = game.do_action_move(NORTH, "test north").result
    north_cell_back = game.do_action_move(SOUTH, "test back south").result
    south_cell = game.do_action_move(SOUTH, "test south").result
    south_cell_back = game.do_action_move(NORTH, "test back north").result
    west_cell = game.do_action_move(WEST, "test west").result
    west_cell_back = game.do_action_move(EAST, "test back east").result
    east_cell = game.do_action_move(EAST, "test east").result
    east_cell_back = game.do_action_move(WEST, "test back west").result
    # TODO: create assert, action_and_result in different directions
    assert start_cell.location == \
           north_cell_back.location == \
           south_cell_back.location == \
           west_cell_back.location == \
           east_cell_back.location
    assert location_in_direction_of(start_cell.location, NORTH) == north_cell.location
    assert location_in_direction_of(start_cell.location, SOUTH) == south_cell.location
    assert location_in_direction_of(start_cell.location, WEST) == west_cell.location
    assert location_in_direction_of(start_cell.location, EAST) == east_cell.location
