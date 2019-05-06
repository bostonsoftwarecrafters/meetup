from src.cell_result_class import CellResult
from src.d_and_d_class import DNDGame
from src.d_and_d_utility import location_in_direction_of
from src.action_class import Action
from test_directions import SOUTH, NORTH, WEST, EAST

TEST_ACCOUNT_UID: str = 'bee769ac-b6b7-4eb0-b441-1c8ada77adb6'


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
        direction=SOUTH,
        reason="safemove",
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
def test_move_back_to_same_cell():
    game = DNDGame(TEST_ACCOUNT_UID)
    start_action = game.get_action(0)
    first_move = game.do_action_move(direction=NORTH, reason="test")
    move_back = game.do_action_move(direction=SOUTH, reason="test")
    assert move_back.result.location == start_action.result.location


# TODO use record (and history?) instead of catalog
def test_record_actions_and_cells():
    game = DNDGame(TEST_ACCOUNT_UID)
    start_cell = game.get_action(0).result
    move_cell = game.do_action_move(NORTH, "test")
    assert len(game.get_cells_visited()) == 2
    assert len(game.get_action_history()) == 2


def test_location_in_direction_of():
    assert location_in_direction_of("F4", SOUTH) == "G4"
    assert location_in_direction_of("F4", NORTH) == "E4"
    assert location_in_direction_of("F4", EAST) == "F5"
    assert location_in_direction_of("F4", WEST) == "F3"
    assert location_in_direction_of("J9", SOUTH) == "A9"
    assert location_in_direction_of("A9", NORTH) == "J9"
    assert location_in_direction_of("J9", EAST) == "J0"
    assert location_in_direction_of("J0", WEST) == "J9"


def test_move_in_all_directions():
    game = DNDGame(TEST_ACCOUNT_UID)
    start_cell = game.get_action(0).result

    # TODO turn these into function
    north_cell = game.do_action_move(NORTH, "test north").result
    north_cell_back = game.do_action_move(SOUTH, "test back south").result
    assert start_cell.location == north_cell_back.location
    assert location_in_direction_of(start_cell.location, NORTH) == north_cell.location

    south_cell = game.do_action_move(SOUTH, "test south").result
    south_cell_back = game.do_action_move(NORTH, "test back north").result
    assert start_cell.location == south_cell_back.location
    assert location_in_direction_of(start_cell.location, SOUTH) == south_cell.location

    west_cell = game.do_action_move(WEST, "test west").result
    west_cell_back = game.do_action_move(EAST, "test back east").result
    assert start_cell.location == west_cell_back.location
    assert location_in_direction_of(start_cell.location, WEST) == west_cell.location

    east_cell = game.do_action_move(EAST, "test east").result
    east_cell_back = game.do_action_move(WEST, "test back west").result
    assert start_cell.location == east_cell_back.location
    assert location_in_direction_of(start_cell.location, EAST) == east_cell.location


def test_game_restart():
    game = DNDGame(TEST_ACCOUNT_UID)
    assert isinstance(game, DNDGame)
    assert game.uuid == TEST_ACCOUNT_UID
    assert isinstance(game.get_action(0), Action)
    # assert game.get_move(0).result.location == game.get_cell(0).location
