import pickle

from d_and_d_class import DNDGame
from d_and_d_utility import make_moves
from test_basic_play import TEST_ACCOUNT_UID, safe_game_setup_teardown
from test_directions import NORTH, SOUTH, WEST, EAST


class PlayGame(object):
    def __init__(self, moves, uid):
        self._game = DNDGame(uuid = uid)
        for move in moves:
            self._game.do_action_move(move, reason="play")

    def get_game(self):
        return self._game


def test_play_moves(safe_game_setup_teardown):
    game = safe_game_setup_teardown
    directions = [NORTH,SOUTH,SOUTH,NORTH,WEST,EAST,EAST,WEST]
    game = make_moves(game=game, directions=directions, reason="MOVE TEST PLAY")
    assert len(game.get_cells_visited())==5
    assert len(game.get_actions()) == len(directions) + 1

def test_record_and_load():
    moves = [NORTH,SOUTH,SOUTH,NORTH,WEST,EAST,EAST,WEST]
    play_game: PlayGame = PlayGame(uid=TEST_ACCOUNT_UID, moves=moves)
    file = open("test_record_and_load.dmp","wb")
    pickle.dump(play_game,file)
    file.close()
    file2 = open("test_record_and_load.dmp","rb")
    load_play_game: PlayGame = pickle.load(file2)
    file2.close()
    for move in load_play_game.get_game().get_actions():
        print(move.action,move.direction,move.reason,move.result.location,move.result.nearby)
    assert len(load_play_game.get_game().get_cells_visited())==5
    assert len(load_play_game.get_game().get_actions()) == len(moves) + 1
