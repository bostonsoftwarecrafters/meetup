from src.cell_result_class import CellResult
from src.d_and_d_class import DandDGame
from src.d_and_d_utility import location_in_direction_of
from src.move_class import WarriorMoveAndResult

TEST_ACCOUNT_UID: str = 'bee769ac-b6b7-4eb0-b441-1c8ada77adb6'


def test_CellResult():
    result = CellResult(location="A6",
                        game="On",
                        status="Alive",
                        inventory=["", "X"],
                        valid_actions=["Move"],
                        nearby="pit"
                        )
    assert isinstance(result, CellResult)


def test_WarriorMove():
    move = WarriorMoveAndResult(action="Move",
                                direction="south",
                                reason="safemove",
                                result=CellResult(location="A6",
                                                  game="On",
                                                  status="Alive",
                                                  inventory=[],
                                                  valid_actions=["Move"],
                                                  nearby="pit"
                                                  )
                                )
    assert isinstance(move, WarriorMoveAndResult)

def test_move_back_to_same_cell():
   game = DandDGame(TEST_ACCOUNT_UID)
   start_move = game.get_move(0)
   first_move = game.action_move("north","test")
   move_back = game.action_move("south","test")
   assert move_back.result.location == start_move.result.location

def test_move_catalog_cells_and_moves():
    game = DandDGame(TEST_ACCOUNT_UID)
    start_cell = game.get_move(0).result
    move_cell = game.action_move("north","test")
    assert len(game.get_cells_visited() )==2
    assert len(game.get_moves())==2


def test_location_in_direction_of():
    assert location_in_direction_of("F4", "south") == "G4"
    assert location_in_direction_of("F4", "north") == "E4"
    assert location_in_direction_of("F4", "east") == "F5"
    assert location_in_direction_of("F4", "west") == "F3"
    assert location_in_direction_of("J9", "south") == "A9"
    assert location_in_direction_of("A9", "north") == "J9"
    assert location_in_direction_of("J9", "east") == "J0"
    assert location_in_direction_of("J0", "west") == "J9"


def test_move_in_all_directions():
    game = DandDGame(TEST_ACCOUNT_UID)
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
    assert start_cell.location == north_cell_back.location == \
           south_cell_back.location == west_cell_back.location == \
           east_cell_back.location
    assert location_in_direction_of(start_cell.location, "north") == north_cell.location
    assert location_in_direction_of(start_cell.location, "south") == south_cell.location
    assert location_in_direction_of(start_cell.location, "west") == west_cell.location
    assert location_in_direction_of(start_cell.location, "east") == east_cell.location




def test_game_restart():
    game = DandDGame(TEST_ACCOUNT_UID)
    assert isinstance(game, DandDGame)
    assert game.uuid == TEST_ACCOUNT_UID
    assert isinstance(game.get_move(0), WarriorMoveAndResult)
    # assert game.get_move(0).result.location == game.get_cell(0).location
