def location_in_direction_of(location, direction):
    ret_letter = location[0]
    ret_number = location[1]
    if direction == "north":
        new_letter_pos = (ord(ret_letter) - ord("A") - 1) % 10
        ret_letter = chr(ord("A") + new_letter_pos)
    elif direction == "south":
        new_letter_pos = (ord(ret_letter) - ord("A") + 1) % 10
        ret_letter = chr(ord("A") + new_letter_pos)
    elif direction == "west":
        ret_number = str((int(location[1])-1) % 10)
    elif direction == "east":
        ret_number = str((int(location[1]) + 1) % 10)
    return ret_letter+ret_number


def get_adjacent_locations(location):
    return (
        location_in_direction_of(location,"north"),
        location_in_direction_of(location,"south"),
        location_in_direction_of(location,"east"),
        location_in_direction_of(location,"west")
    )


def add_comma(original_val, add_value):
    if add_value in original_val:
        return original_val
    elif original_val != "":
        return original_val + "," + add_value
    else:
        return add_value