from action_to_take_class import ActionToTake
from dnd_constants import DRAGON_STR, PIT_STR
from action_class import Action
from cell_result_class import CellResult
from d_and_d_utility import location_in_direction_of
from game_direction_class import GameDirection, NORTH, SOUTH, EAST, WEST
import copy
import requests
from requests import HTTPError
BASE_URL = "http://54.85.100.225:8000"

from typing import Optional

class DNDGame(object):


    def __init__(self, uuid: str):
        self._derived_bats = {}
        self._derived_contents = {}
        self._cells_visited = {}
        self._actions = []
        self.uuid = uuid

        self.do_action_start()

    def catalog_action(self, action, direction, reason, result):
        action_and_result = Action(
            action=action,
            direction=direction,
            reason=reason,
            result=copy.deepcopy(result)
        )
        self._actions.append(action_and_result)
        return action_and_result

    def catalog_cell_visited(self, cell):
        self._cells_visited[cell.location] = copy.deepcopy(cell)

    def do_action_and_store(self, action, direction: Optional[GameDirection] = None, reason="") -> Action:
        json_parameter = {"account_uuid": self.uuid,
                          "action": action}

        if direction is not None:
            json_parameter["direction"] = direction.value
        response = requests.post(BASE_URL + "/api/game", json=json_parameter)
        if response.status_code == 400:
            err_msg = "400 Error - Bad Request\n" + response.request.url + "\n" + response.request.data
            raise HTTPError(err_msg)
        result = self.make_and_catalog_cell_from_response(response)
        self.catalog_cell_visited(result)
        new_action = self.catalog_action(action=action, direction=direction, reason=reason, result=result)
        return new_action

    def do_action_move(self, direction: GameDirection, reason: str):
        action_and_result_cell = self.do_action_and_store(action="move", direction=direction, reason=reason)
        return action_and_result_cell

    def do_action_start(self):
        action = self.do_action_and_store(action="restart")

    def get_action(self, index) -> Action:
        return self._actions[index]


    def do_actions(self, actions_to_take):
        action_to_take : ActionToTake
        for action_to_take in actions_to_take:
            action = self.do_action_and_store(
                action=action_to_take.action,
                direction=action_to_take.direction,
                reason=action_to_take.reason
            )
            if action.result.status != "Alive":
                break


    def get_actions(self) -> list:
        return self._actions

    def get_adjacent_locations_all(self, location):
        return (
            location_in_direction_of(location, NORTH),
            location_in_direction_of(location, SOUTH),
            location_in_direction_of(location, EAST),
            location_in_direction_of(location, WEST)
        )


    def get_adjacent_locations_not_visited(self,location):
        adjacent_locations = self.get_adjacent_locations_all(location)
        ret_val = []
        for location in adjacent_locations:
            if not self.is_location_visited(location):
                ret_val.append(location)
        return ret_val

    def get_adjacent_locations_visited(self,location):
        adjacent_locations = self.get_adjacent_locations_all(location)
        ret_val = []
        for location in adjacent_locations:
            if self.is_location_visited(location):
                ret_val.append(location)
        return ret_val

    def get_cell(self,location):
        return self._cells_visited[location]

    def get_cells_visited(self):
        return self._cells_visited

    def is_location_visited(self,location):
        try:
            dummy = self.get_cell(location)
            return True
        except:
            return False

    def make_and_catalog_cell_from_response(self, response):
        json_resp = response.json()
        result_cell = CellResult(location=json_resp["location"],
                          game=json_resp["game"],
                          status=json_resp["status"],
                          inventory=json_resp["inventory"],
                          valid_actions=json_resp["valid_actions"],
                          nearby=json_resp["nearby"]
                          )
        self.catalog_cell_visited(result_cell)
        return result_cell

    def derive_visited_objects(self):
        actions = self.get_actions()
        self.derive_content_start_cell()
        for action_index in range(1, len(actions)):
            curr_action: Action = actions[action_index]
            curr_location = curr_action.result.location
            prev_action = actions[action_index-1]

            inventory_content = self.derive_content_visited_inventory(action_index)
            self.add_location_derived_content(curr_location, inventory_content)

            danger_content = self.derive_content_danger_visited(action_index)
            self.add_location_derived_content(curr_location,danger_content)

            predicted_location = location_in_direction_of(prev_action.result.location, curr_action.direction)
            if predicted_location != curr_location:
                self.derive_bat(action_index, predicted_location, curr_location)

    def derive_contents(self):

        self.derive_visited_objects()
        self.derive_contents_of_unknown_adjacent_cells()

    def derive_content_danger_visited(self, action_index):
        curr_action = self.get_action(action_index)
        upper_status = curr_action.result.status.upper()
        if DRAGON_STR.upper() in upper_status:
            ret_val = [DRAGON_STR]
        elif PIT_STR.upper() in upper_status:
            ret_val = [PIT_STR]
        else:
            ret_val = []
        return ret_val

    def derive_content_visited_inventory(self, curr_action_index):
        actions = self.get_actions()
        curr_action = actions[curr_action_index]
        curr_result = curr_action.result
        curr_location = curr_result.location
        curr_inventory = curr_result.inventory
        prev_action: Action = actions[curr_action_index - 1]
        prev_inventory = prev_action.result.inventory
        new_inventory_set = set(curr_inventory) - set(prev_inventory)
        return list(new_inventory_set)

    def get_derived_content_of_location(self,location):
        return self._derived_contents[location]

    def add_location_derived_content(self, location, objects):
        derived_dict = self._derived_contents
        self.init_derived_location(target_dictionary=derived_dict,
                                   location=location, value=[])
        for obj in objects:
            self._derived_contents[location] = objects

    def init_derived_location(self, target_dictionary, location, value):
        try:
            dummy = target_dictionary[location]
        except:
            target_dictionary[location] = value

    def derive_bat(self, action_index, bat_location, fly_to):
        self._derived_bats[action_index, bat_location] = fly_to

    def get_derived_fly_to(self, action_index, bat_location):
        try:
            ret_val = self._derived_bats[action_index, bat_location]
        except:
            ret_val = ""
        return ret_val

    def get_derived_fly_tos(self):
        return copy.deepcopy(self._derived_bats)

    def derive_contents_of_unknown_adjacent_cells(self):

        visited_cells = self.get_cells_visited()
        for (location,visited_cell) in visited_cells.items():
            adjacent_locations = self.get_adjacent_locations_all(location)
            unknown_adjacent_locations = self.get_adjacent_locations_not_visited(location)
            if len(unknown_adjacent_locations) == 0:
                pass
            elif visited_cell.nearby == "":
                for unknown_adjacent_location in unknown_adjacent_locations:
                    self.add_location_derived_content(unknown_adjacent_location,[])


    def get_derived_contents(self):
        return copy.deepcopy(self._derived_contents)

    # TODO Write test just for this function
    def derive_content_start_cell(self):
        location = self.get_action(0).result.location
        inventory = self.get_action(0).result.inventory
        self.add_location_derived_content(location,inventory)





