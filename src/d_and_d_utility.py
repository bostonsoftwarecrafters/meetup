from test_directions import NORTH, SOUTH, WEST, EAST
from game_direction_class import GameDirection


def location_in_direction_of(location: str, direction: GameDirection):
    ret_letter = location[0]
    ret_number = location[1]
    if direction == NORTH:
        new_letter_pos = (ord(ret_letter) - ord("A") - 1) % 10
        ret_letter = chr(ord("A") + new_letter_pos)
    elif direction == SOUTH:
        new_letter_pos = (ord(ret_letter) - ord("A") + 1) % 10
        ret_letter = chr(ord("A") + new_letter_pos)
    elif direction == WEST:
        ret_number = str((int(location[1])-1) % 10)
    elif direction == EAST:
        ret_number = str((int(location[1]) + 1) % 10)
    return ret_letter+ret_number

def add_comma(original_val, add_value):
    if add_value in original_val:
        return original_val
    elif original_val != "":
        return original_val + "," + add_value
    else:
        return add_value


def print_game(game):
    for move in game.get_actions():
        print(move.action, move.direction, move.reason, move.result.location, move.result.nearby)