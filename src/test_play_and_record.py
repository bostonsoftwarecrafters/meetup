import pickle

from action_to_take_class import ActionToTake
from d_and_d_class import DNDGame
from test_directions import NORTH, SOUTH, WEST, EAST


def create_move_actions_to_take(directions, reason):
    ret_val = []
    for direction in directions:
        ret_val.append(ActionToTake(action="move", direction=direction, reason=reason))
    return ret_val


def test_play_moves(safe_game_fixture_setup_teardown):
    game: DNDGame = safe_game_fixture_setup_teardown
    directions = [NORTH,SOUTH,SOUTH,NORTH,WEST,EAST,EAST,WEST]
    actions_to_take = create_move_actions_to_take(directions=directions, reason="Test Play Moves")
    game.do_actions(actions_to_take)
    assert len(game.get_cells_visited())==5
    assert len(game.get_actions()) == len(directions) + 1

def test_record_and_load(safe_game_fixture_setup_teardown):
    game:DNDGame = safe_game_fixture_setup_teardown
    directions = [NORTH,SOUTH,SOUTH,NORTH,WEST,EAST,EAST,WEST]
    actions_to_take = create_move_actions_to_take(directions=directions, reason="Test Play Moves")
    game.do_actions(actions_to_take)
    file = open("test_record_and_load.dmp","wb")
    pickle.dump(game,file)
    file.close()
    file2 = open("test_record_and_load.dmp","rb")
    game: DNDGame = pickle.load(file2)
    file2.close()
    assert len(game.get_cells_visited())==5
    assert len(game.get_actions()) == len(directions) + 1
