from src.d_and_d_class import DandDGame
from src.d_and_d_utility import location_in_direction_of
from src.mock_game_class import MockGame
from src.test_basic_play import TEST_ACCOUNT_UID


def test_mock_create_game():
    # game = DandDGame(TEST_ACCOUNT_UID)
    mock_game = MockGame(TEST_ACCOUNT_UID)
    assert isinstance(mock_game,DandDGame)
    assert len(mock_game.get_moves()) == 1
    assert len(mock_game.get_cells_visited()) == 1

def test_define_init_cell():
    mock_game = MockGame(TEST_ACCOUNT_UID, location="G3")
    move = mock_game.get_moves()[0]
    cell_visited = mock_game.get_cells_visited()["G3"]
    assert move.action == "restart"
    assert cell_visited.location == "G3"
    assert move.result.location == "G3"

def test_mock_all_directions():
    game = MockGame(TEST_ACCOUNT_UID)
    start_cell = game.get_move(0).result
    north_cell = game.action_move("north","test north").result
    north_cell_back = game.action_move("south","test back south").result
    south_cell = game.action_move("south","test south").result
    south_cell_back = game.action_move("north","test back north").result
    west_cell = game.action_move("west","test west").result
    west_cell_back = game.action_move("east","test back east").result
    east_cell = game.action_move("east","test east").result
    east_cell_back = game.action_move("west","test back west").result
    # TODO: create assert, move in different directions
    assert start_cell.location == \
           north_cell_back.location == \
           south_cell_back.location == \
           west_cell_back.location == \
           east_cell_back.location
    assert location_in_direction_of(start_cell.location, "north") == north_cell.location
    assert location_in_direction_of(start_cell.location, "south") == south_cell.location
    assert location_in_direction_of(start_cell.location, "west") == west_cell.location
    assert location_in_direction_of(start_cell.location, "east") == east_cell.location
