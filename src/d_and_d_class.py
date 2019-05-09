import copy
from typing import Optional

import requests
from requests import HTTPError

from cell_result_class import CellResult
from action_class import Action
from d_and_d_utility import location_in_direction_of
from game_direction_class import GameDirection, NORTH, SOUTH, EAST, WEST


class DNDGame(object):

    def __init__(self, uuid: str):
        self._cells_visited = {}
        self._actions = []
        self.uuid = uuid
        self.action_start_game()

    def get_cell(self,location):
        return self._cells_visited[location]

    def make_cell_from_response(self, response):
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

    def get_action(self, index) -> Action:
        return self._actions[index]

    def get_adjacent_locations(self,location):
        return (
            location_in_direction_of(location, NORTH),
            location_in_direction_of(location, SOUTH),
            location_in_direction_of(location, EAST),
            location_in_direction_of(location, WEST)
        )

    def get_adjacent_locations_not_visited(self,location):
        adjacent_locations = self.get_adjacent_locations(location)
        ret_val = []
        for location in adjacent_locations:
            if not self.is_location_visited(location):
                ret_val.append(location)

    def action_start_game(self):
        action = self.get_and_store_action_and_result(action="restart")


    def get_and_store_action_and_result(self, action, direction: Optional[GameDirection] = None, reason="") -> Action:
        json_parameter = {"account_uuid": self.uuid,
                          "action": action}

        if direction is not None:
            json_parameter["direction"] = direction.value
        response = requests.post(BASE_URL + "/api/game", json=json_parameter)
        if response.status_code == 400:
            err_msg = "400 Error - Bad Request\n" + response.request.url + "\n" + response.request.data
            raise HTTPError(err_msg)
        result = self.make_cell_from_response(response)
        self.catalog_cell_visited(result)
        new_action = self.add_action(action=action, direction=direction, reason=reason, result=result)
        return new_action

    def get_cells_visited(self):
        return self._cells_visited

    def catalog_cell_visited(self, cell):
        self._cells_visited[cell.location] = copy.deepcopy(cell)


    def do_action_move(self, direction: GameDirection, reason: str):
        action_and_result_cell = self.get_and_store_action_and_result(action="move", direction=direction, reason=reason)
        return action_and_result_cell

    def get_actions(self) -> list:
        return self._actions

    def add_action(self, action, direction, reason, result):
        action_and_result = Action(
            action=action,
            direction=direction,
            reason=reason,
            result=copy.deepcopy(result)
        )
        self._actions.append(action_and_result)
        return action_and_result

    def is_location_visited(self,location):
        try:
            dummy = self.get_cell(location)
            return True
        except:
            return False


BASE_URL = "http://54.85.100.225:8000"