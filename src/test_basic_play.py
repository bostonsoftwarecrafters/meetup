import pytest

from d_and_d_utility import print_game
from d_and_d_game_helper import get_game_with_no_dangers_near_start
from cell_result_class import CellResult
from d_and_d_class import DNDGame
from d_and_d_utility import location_in_direction_of
from action_class import Action
from test_directions import SOUTH, NORTH, WEST, EAST

TEST_ACCOUNT_UID: str = 'bee769ac-b6b7-4eb0-b441-1c8ada77adb6'

def test_CellResult_Equality():
    print("A")
    result1 = CellResult(location="A6",
                        game="On",
                        status="Alive",
                        inventory=["", "X"],
                        valid_actions=["Move"],
                        nearby="Pit"
                        )
    result2 =     result = CellResult(location="A6",
                        game="On",
                        status="Alive",
                        inventory=["", "X"],
                        valid_actions=["Move"],
                        nearby="Pit"
                        )
    assert result1 == result2

def test_CellResult():
    result = CellResult(location="A6",
                        game="On",
                        status="Alive",
                        inventory=["", "X"],
                        valid_actions=["Move"],
                        nearby="Pit"
                        )
    assert isinstance(result, CellResult)


def test_WarriorMove():
    action_and_result = Action(
        action="Move",
        direction=SOUTH._value_,
        reason="safe move",
        result=CellResult(
            location="A6",
            game="On",
            status="Alive",
            inventory=[],
            valid_actions=["Move"],
            nearby="Pit"
        )
    )
    assert isinstance(action_and_result, Action)


# TODO can you start one move from death?


def test_move_back_to_same_cell(safe_game_setup_teardown):
    game = safe_game_setup_teardown
    start_action = game.get_action(0)
    print("Start",start_action)
    first_move = game.do_action_move(direction=NORTH, reason="test")
    move_back = game.do_action_move(direction=SOUTH, reason="test")
    print("Move",move_back)
    assert move_back.result.location == start_action.result.location


# TODO use record (and history?) instead of catalog
def test_record_actions_and_cells(safe_game_fixture_setup_teardown):
    game = safe_game_fixture_setup_teardown
    start_cell = game.get_action(0).result
    move_cell = game.do_action_move(NORTH, "test")
    assert len(game.get_cells_visited()) == 2
    assert len(game.get_actions()) == 2

@pytest.fixture()
def safe_game_setup_teardown(request):
    game = get_game_with_no_dangers_near_start(TEST_ACCOUNT_UID)
    tests_failed_before_module = request.session.testsfailed
    yield game
    if request.session.testsfailed > tests_failed_before_module:
        print("**************************************")
        print("*** MOVES EXECUTED AS PART OF TEST ***")
        print("**************************************")
        print_game(game)


def test_location_in_direction_of():
    assert location_in_direction_of("F4", SOUTH) == "G4"
    assert location_in_direction_of("F4", NORTH) == "E4"
    assert location_in_direction_of("F4", EAST) == "F5"
    assert location_in_direction_of("F4", WEST) == "F3"
    assert location_in_direction_of("J9", SOUTH) == "A9"
    assert location_in_direction_of("A9", NORTH) == "J9"
    assert location_in_direction_of("J9", EAST) == "J0"
    assert location_in_direction_of("J0", WEST) == "J9"

def test_move_in_all_directions(safe_game_setup_teardown):
    game = safe_game_setup_teardown
    functest_move_and_move_back(game=game, direction=NORTH)
    functest_move_and_move_back(game=game, direction=SOUTH)
    functest_move_and_move_back(game=game, direction=EAST)
    functest_move_and_move_back(game=game, direction=WEST)

def test_game_restart(safe_game_setup_teardown):
    game = safe_game_setup_teardown
    assert isinstance(game, DNDGame)
    assert game.uuid == TEST_ACCOUNT_UID
    assert isinstance(game.get_action(0), Action)
    assert len(game.get_cells_visited()) == 1
    assert len(game.get_actions()) == 1


def functest_move_and_move_back(direction, game):
    start_cell = game.get_action(0).result
    cell = game.do_action_move(direction, "test " + direction.value).result
    cell_back = game.do_action_move(direction.opposite(), "test back " + direction.opposite().value).result
    assert start_cell.location == cell_back.location
    assert location_in_direction_of(start_cell.location, direction) == cell.location