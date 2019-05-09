from d_and_d_class import DNDGame
from d_and_d_game_helper import make_moves
from mock_game_class import MockGame
from test_directions import NORTH, SOUTH, WEST, EAST
from test_mock import safe_mock_game_setup_teardown

def derive_mock_game(game: DNDGame):
    mock_game = MockGame(game.get_action(0).result.location)
    mock_game.calculate_adjacent_notvisited_cells()
    return mock_game

def play_mock_game(game: DNDGame):
    mock_game = MockGame(game.get_action(0).result.location)
    original_game_actions = game.get_actions()
    for index in range (1,len(original_game_actions)):
        action = original_game_actions[index]
        new_action = mock_game.get_and_store_action_and_result(
            action=action.action,
            direction=action.direction,
            reason="Mock "+action.reason
        )


    return mock_game

def test_generate_mock_board(safe_mock_game_setup_teardown):
    moves = [NORTH]
    game = safe_mock_game_setup_teardown
    game = make_moves(game, moves,"Test Generate Mock Board")
    mock_board = derive_mock_game(game)
    assert game.get_actions() == game.get_actions()
    # mock_game = make_mock_game(mock_board)
    # assert mock_game.get_moves() == game.get_moves()

