import requests
import copy

letters = ["A","B","C","D","E","F","G","H","I","J"]
UUID = 'bee769ac-b6b7-4eb0-b441-1c8ada77adb6'
url = "http://54.85.100.225:8000"
# dd_dict = dict()
# cells_visited = []
# directions_moved = []
# nearby_dragon_cells = []

def get_cell(response):
    json_resp = response.json()
    cell = {"location": json_resp["location"],
              "game": json_resp["game"],
              "status": json_resp["status"],
              "inventory": json_resp["inventory"],
              "actions": json_resp["valid_actions"],
              "nearby": json_resp["nearby"],
              "valid_actions": json_resp["valid_actions"]}
    return cell


def print_cell(cell):
    print(cell)

def get_unknown_adjacent_locations(game,location):
    adjacent_locations = get_adjacent_locations(game,location)
    unknown_adjacent_locations = []
    for adjacent_location in adjacent_locations:
        if not is_location_defined(adjacent_location["location"]):
            unknown_adjacent_locations.append(adjacent_location)
    return unknown_adjacent_locations


def get_adjacent_locations(location):
    letter = location[0]
    letter_index = ord(letter) - ord("A")
    number = int(location[1])
    number_str = location[1]
    previous_letter = letters[(letter_index - 1) % 10]
    next_letter = letters[(letter_index + 1) % 10]
    previous_number_str = str((number - 1) % 10)
    next_number_str = str((number + 1) % 10)
    adjacent_locations = [
        {"location": previous_letter + number_str,
         "direction": NORTH},
        {"location": next_letter + number_str, "direction": SOUTH},
        {"location": letter + previous_number_str,
         "direction": WEST},
        {"location": letter + next_number_str,
         "direction": EAST}
    ]
    return adjacent_locations


def move_warrior(direction, reason):
    r = requests.post(url + "/api/game", json={'account_uuid': UUID, "action": "move",
                                               "direction": direction.value})
    cell = get_cell(r)
    catalog(cell,direction, reason)
    if "Magic Arrow" in cell["inventory"] and "Dragon" in cell["nearby"]:
        dragon_option_cells = get_unknown_adjacent_locations(cell["location"])
        shoot_arrow(dragon_option_cells[0]["direction"])
    return cell


def is_safe(cell):
    nearby = cell["nearby"]
    if "Dragon" in nearby or "Pit" in nearby or "Bats" in nearby:
        return False
    elif cell["game"] != "On":
        return False
    return True


def move_all_adjacent_safe_spaces(start_cell):
    if not is_safe(start_cell):
        print ("Not safe",start_cell["nearby"])
        return start_cell
    unknown_adjacent_locations = get_unknown_adjacent_locations(cell["location"])
    direction_pairs = {NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}
    cell_moved_to = copy.deepcopy(start_cell)
    for adjacent_location in unknown_adjacent_locations:
        direction_to_move = adjacent_location["direction"]
        cell_moved_to = move_warrior(direction_to_move, "safe move")
        cell_moved_to = move_all_adjacent_safe_spaces(cell_moved_to)

        if cell_moved_to["location"] != adjacent_location["location"]:
            print("Failed")
            break

        direction_to_move_back = direction_pairs[direction_to_move]
        cell_moved_to = move_warrior(direction_to_move_back, "moveback")

        if cell_moved_to["location"] != start_cell["location"]:
            print("Failed")
            break
    return cell_moved_to



def get_killed_by(current_cell):
    if current_cell == "":
        return ""
    status = current_cell["status"]
    if status == "Alive":
        killed_by = "";
    elif "Pit" in status:
        killed_by = "Pit";
    elif "dragon" in status:
        killed_by = "dragon"
    else:
        killed_by = "???"
    return killed_by


def alive(cell):
    return cell == "" or cell["status"] == "Alive";


def get_extra_items(current_inventory, previous_inventory):
    extra_item = "???"
    if len(current_inventory) == len (previous_inventory):
        extra_item = ""
    else:
        for item in current_inventory:
            if item not in previous_inventory:
                extra_item = item
                break
    return extra_item


def is_dd_dict_entry_defined(cell):
    return is_location_defined(cell["location"])

def is_location_defined(letter):
    try:
        current_cell = dd_dict[letter]
        return True
    except:
        return False


def shoot_arrow(direction):
    print ("=> => => Shooting ",direction)
    r = requests.post(url + "/api/game", json={'account_uuid': UUID, "action": "attack",
                                               "direction": direction})
    cell = get_cell(r);
    print_cell(cell)
    catalog(cell,direction, "shoot")
    return cell

def catalog(cell,direction,reason):
    # define current_cell and catalog dd_dict
    current_location = cell["location"]
    cell_visited = {"location": current_location,"cell":cell,"direction":direction,"reason":reason}
    cells_visited.append(cell_visited)
    print(cell)
    # directions_moved.append({"direction":direction)
    if is_dd_dict_entry_defined(cell):
        print("Aleady catalogued")
        return
    if "Dragon" in cell["nearby"] and current_location not in nearby_dragon_cells:
        nearby_dragon_cells.append(current_location)
    current_index = len(cells_visited)-1
    dd_dict[current_location] = copy.deepcopy(cell)
    current_dd_dict_rec = dd_dict[current_location]
    current_dd_dict_rec["contents"] = ""
    current_killed_by = get_killed_by(current_dd_dict_rec)
    current_inventory = current_dd_dict_rec["inventory"]
    # define previous cell
    # print("B")

    if current_index == 0:
        previous_location = ""
        previous_dd_dict_rec = ""
        previous_killed_by = ""
        previous_inventory = ""
    else:
        previous_location = cells_visited[current_index-1]["location"]
        previous_dd_dict_rec = dd_dict[previous_location]
        previous_killed_by =  get_killed_by(previous_dd_dict_rec);
        previous_inventory = previous_dd_dict_rec["inventory"]
    # print("C")

    # previous_killed_by = get_killed_by(previous_dd_dict_rec)
    print("killed by",current_killed_by,":",previous_killed_by)

    if previous_killed_by == "" and current_killed_by != "":
        current_dd_dict_rec["contents"] = current_killed_by;
    else:
        new_item = get_extra_items(current_inventory,previous_inventory)
        if new_item not in ("","???"):
            current_dd_dict_rec["contents"] = new_item
    print("Set contents to: ",current_dd_dict_rec["contents"])
    # cells_visited.append({"location": current_location,"response":cell,"direction":"N/A","action": "catalog"})

    # print("Adjacent",adjacent_cells(current_location))



def restartGame():
    r = requests.post(url + "/api/game", json={'account_uuid': UUID,"action": "restart"})
    cell = get_cell(r)
    catalog(cell,"start","start")
    return cell



cell =  restartGame();

inventory = cell["inventory"]

print(inventory);

nearby = dict()
dir = 'north'


def move_to_next_unexplored_cell(cell):
    x = 0
    do_loop = True
    cell_moved_to = copy.deepcopy(cell)
    while x < 10 and do_loop and cell_moved_to["game"]=="On":
        y = 0
        while y < 10 and do_loop and cell_moved_to["game"]=="On":
            unknown_adjacent_locations = get_unknown_adjacent_locations(cell["location"])
            if len(unknown_adjacent_locations) > 0:
                direction = unknown_adjacent_locations[0]["direction"]
                cell_moved_to = move_warrior(get_unknown_adjacent_locations(direction,"unsafe move"))
                return cell_moved_to
            cell_moved_to = move_warrior(NORTH,"explore")
        cell_moved_to = move_warrior(EAST,"explore")
    return cell_moved_to



for x in range(50):
    cell = move_all_adjacent_safe_spaces(cell)
    cell = move_to_next_unexplored_cell(cell)


for cell in cells_visited:
    print("**",cell)

# for x in range(100)
#     result = moveWarrior(dir)
#     print(result["inventory"])
#     if result["game"] == "Over":
#         break
#
#     nearhere = result["nearby"]
#     nearby[result["location"]] = nearhere
#
#     if "Pit" in nearhere:
#         dir = getrandomdir()
#     elif "Rope" in nearhere or "Magic Arrow" in nearhere:
#         result = moveWarrior(NORTH).json()
#         result = moveWarrior(SOUTH).json()
#         result = moveWarrior(EAST).json()
#         result = moveWarrior(WEST).json()
#         result = moveWarrior(WEST).json()
#         result = moveWarrior(EAST).json()
#         result = moveWarrior(SOUTH).json()
#         result = moveWarrior(NORTH).json()
#         print("**********" + str(result["inventory"]))
#
#     print(nearby)

