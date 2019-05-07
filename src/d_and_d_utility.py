from d_and_d_class import DNDGame
from test_directions import Direction, NORTH, SOUTH, WEST, EAST


def location_in_direction_of(location: str, direction: Direction):
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


def get_adjacent_locations(location):
    return (
        location_in_direction_of(location,NORTH),
        location_in_direction_of(location,SOUTH),
        location_in_direction_of(location,EAST),
        location_in_direction_of(location,WEST)
    )


def add_comma(original_val, add_value):
    if add_value in original_val:
        return original_val
    elif original_val != "":
        return original_val + "," + add_value
    else:
        return add_value


def get_safe_game(uid) -> DNDGame:
    game: DNDGame = DNDGame(uid)
    while True:
        nearby = game.get_action(0).result.nearby
        if "Pit" not in nearby and "Bat" not in nearby and "Dragon" not in nearby:
            break
        game = DNDGame(uid)
    return game


