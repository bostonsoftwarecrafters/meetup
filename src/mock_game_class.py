from cell_result_class import CellResult
from d_and_d_class import DNDGame
from d_and_d_utility import location_in_direction_of, get_adjacent_locations, add_comma

class MockGame(DNDGame):
    def __init__(self, uid, location="G4"):
        self._mock_start_location = location
        self._bat_cells = []
        self._pit_cells = []
        self._arrow_cell = ""
        self._rope_cell = ""
        self._dragon_cell = ""
        super().__init__(uid)


    def get_api_result_cell(
            self,
            action,
            direction="N/A",
            reason=""):
        if action == "restart":
            start_cell = CellResult(location=self._mock_start_location)
            action_and_result = self.add_action_and_result(action=action,direction="N/A",reason=reason,result=start_cell)
            self.catalog_cell_visited(start_cell)
            return action_and_result
        elif action == "move":
            move_list = self.get_actions()
            current_cell = move_list[len(move_list)-1].result
            current_location = current_cell.location
            new_cell_location = location_in_direction_of(current_location,direction)

            new_cell = self.make_mock_cell(new_cell_location)
            move = self.add_action_and_result(action=action,direction=direction,reason=reason,result=new_cell)
            self.catalog_cell_visited(new_cell)
            return move

    def get_nearby(self, adjacent_location):
        adjacent_locations = get_adjacent_locations(adjacent_location)
        ret_val = ""
        for adjacent_location in adjacent_locations:
            if adjacent_location in self._bat_cells:
                ret_val = add_comma(ret_val,"Bats")
            elif adjacent_location in self._pit_cells:
                ret_val = add_comma(ret_val,"Pit")
            elif adjacent_location == self._dragon_cell:
                ret_val = add_comma(ret_val,"Dragon")
            elif adjacent_location == self._rope_cell:
                ret_val = add_comma(ret_val,"Rope")
            elif adjacent_location == self._arrow_cell:
                ret_val = add_comma(ret_val,"Magic Arrow")

        return ret_val

    def add_bat(self, location):
        self._bat_cells.append(location)

    def set_nearby(self, CellResult):
        location = CellResult.location
        CellResult.nearby = self.get_nearby(location)

    def make_mock_cell(self, location):
        ret_val = CellResult(location=location)
        self.set_nearby(ret_val)
        return ret_val

