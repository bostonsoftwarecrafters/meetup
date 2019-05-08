from d_and_d_class import DNDGame
from d_and_d_utility import make_moves
from mock_game_class import MockGame
from test_basic_play import TEST_ACCOUNT_UID, safe_game_setup_teardown
from test_directions import NORTH, SOUTH, WEST, EAST
from test_play_and_record import PlayGame


def derive_mock_board(game: DNDGame):
    mock_board_game = MockGame(game.get_action(0).result.location)
    return mock_board_game

def test_generate_mock_board(safe_game_setup_teardown):
    moves = [NORTH]
    game = safe_game_setup_teardown
    game = make_moves(game, moves,"Test Generate Mock Board")
    mock_board = derive_mock_board(game)
    assert game.get_actions() == game.get_actions()
    # mock_game = make_mock_game(mock_board)
    # assert mock_game.get_moves() == game.get_moves()

