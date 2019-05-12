import pytest

from d_and_d_class import DNDGame
from d_and_d_utility import print_game
from mock_game_class import MockGame
from test_basic_play import TEST_ACCOUNT_UID, functest_move_and_move_back
from game_direction_class import NORTH, SOUTH, EAST, WEST


#TODO: Move to conftest.py
@pytest.fixture()
def safe_mock_game_setup_teardown(request):
    mock_game = MockGame(TEST_ACCOUNT_UID)
    tests_failed_before_module = request.session.testsfailed
    yield mock_game
    if request.session.testsfailed > tests_failed_before_module:
        print("*******************************************")
        print("*** MOCK MOVES EXECUTED AS PART OF TEST ***")
        print("******************************************")
        print_game(mock_game)



def test_mock_create_game(safe_mock_game_setup_teardown):
    mock_game = safe_mock_game_setup_teardown
    assert isinstance(mock_game, DNDGame)
    assert len(mock_game.get_actions()) == 1
    assert len(mock_game.get_cells_visited()) == 1

def test_mock_create_game_start_g3():
    mock_game = MockGame(TEST_ACCOUNT_UID,"G3")
    action_and_result = mock_game.get_actions()[0]
    cell_visited = mock_game.get_cells_visited()["G3"]
    assert action_and_result.action == "restart"
    assert cell_visited.location == "G3"
    assert action_and_result.result.location == "G3"

def test_mock_move_in_all_directions(safe_mock_game_setup_teardown):
    game = safe_mock_game_setup_teardown
    functest_move_and_move_back(game=game, direction=NORTH)
    functest_move_and_move_back(game=game, direction=SOUTH)
    functest_move_and_move_back(game=game, direction=EAST)
    functest_move_and_move_back(game=game, direction=WEST)

