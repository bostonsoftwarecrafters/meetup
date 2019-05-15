from d_and_d_class import DNDGame
from d_and_d_utility import print_game, create_move_actions_to_take
from game_direction_class import SOUTH, WEST
from test_basic_play import TEST_ACCOUNT_UID

directions = []
for i in range(0,10):
    directions.append(SOUTH)
    for j in range(0,10):
        directions.append(WEST)
actions_to_take = create_move_actions_to_take(directions,"Example game")
game = DNDGame(TEST_ACCOUNT_UID)
game.do_actions(actions_to_take)
print_game(game)

