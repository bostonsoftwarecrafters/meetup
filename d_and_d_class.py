import requests
from requests import HTTPError

from cell_result_class import CellResult
from move_class import WarriorMoveAndResult

class DandDGame(object):

    def __init__(self, uuid: str):
        self._cells_visited = {}
        self._moves = []
        self.uuid = uuid
        self.action_start_game()

    def get_cell(self,location):
        return self._cells_visited[location]

    def make_cell_from_response(self, response):
        print("response", response)
        json_resp = response.json()
        result_cell = CellResult(location=json_resp["location"],
                          game=json_resp["game"],
                          status=json_resp["status"],
                          inventory=json_resp["inventory"],
                          valid_actions=json_resp["valid_actions"],
                          nearby=json_resp["nearby"]
                          )
        ret_val = self.catalog_cell_visited(result_cell)
        return ret_val

    def get_move(self, index):
        return self._moves[index]

    def action_start_game(self):
        result_cell = self.get_api_result_cell(action="restart")
        print(result_cell)

    def get_api_result_cell(self, action, direction="N/A",reason=""):
        json_parameter = {"account_uuid": self.uuid,
                          "action": action}

        if direction != "N/A":
            json_parameter["direction"] = direction
        response = requests.post(BASE_URL + "/api/game", json=json_parameter)
        if response.status_code == 400:
            err_msg = "400 Error - Bad Request\n" + response.request.url + "\n" + response.request.data
            raise HTTPError(err_msg)
        result = self.make_cell_from_response(response)
        self.catalog_cell_visited(result)
        move = self.add_move(action=action,direction=direction,reason=reason,result=result)
        return move

    def get_cells_visited(self):
        return self._cells_visited

    def catalog_cell_visited(self, cell):
        try:
            ret_val = self._cells_visited[cell.location]
            return ret_val
        except:
            self._cells_visited[cell.location] = cell
            return cell


    def action_move(self, direction, reason):
        move_cell = self.get_api_result_cell(action="move",direction=direction,reason=reason)
        return move_cell

    def get_moves(self):
        return self._moves

    def add_move(self, action, direction, reason, result):
        move = WarriorMoveAndResult(
            action=action,
            direction=direction,
            reason=reason,
            result=result
        )
        self._moves.append(move)
        return move


BASE_URL = "http://54.85.100.225:8000"