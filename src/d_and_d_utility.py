from action_to_take_class import ActionToTake
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

# move print game to class
def print_game(game):
    for move in game.get_actions():
        print(move.result.status, move.action, move.direction, move.reason, "location",move.result.location, "nearby", move.result.nearby, "inventory",move.result.inventory)

# TODO: Maybe get rid of this
def create_move_actions_to_take(directions, reason):
    ret_val = []
    for direction in directions:
        ret_val.append(ActionToTake(action="move", direction=direction, reason=reason))
    return ret_val