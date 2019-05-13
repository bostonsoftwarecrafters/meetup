import pytest

from d_and_d_game_helper import get_game_with_no_dangers_near_start
from d_and_d_utility import print_game
from mock_game_class import MockGame
from test_basic_play import TEST_ACCOUNT_UID


@pytest.fixture
def safe_game_fixture_setup_teardown(request):
    game = get_game_with_no_dangers_near_start(TEST_ACCOUNT_UID)
    tests_failed_before_module = request.session.testsfailed
    yield game
    if request.session.testsfailed > tests_failed_before_module:
        print("**************************************")
        print("*** MOVES EXECUTED AS PART OF TEST ***")
        print("**************************************")
        print_game(game)


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