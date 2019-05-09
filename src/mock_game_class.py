from cell_result_class import CellResult
from d_and_d_class import DNDGame
from d_and_d_utility import add_comma, location_in_direction_of
from dnd_constants import DND_OBJECT



class MockGame(DNDGame):
    def __init__(self, uid, location="G4"):
        self._mock_start_location = location
        self._object_locations = {}
        for object_enum in DND_OBJECT:
            self._object_locations[object_enum] = []

        super().__init__(uid)


    def get_and_store_action_and_result(
            self,
            action,
            direction="N/A",
            reason=""):
        if action == "restart":
            start_cell = CellResult(location=self._mock_start_location)
            action_and_result = self.add_action(action=action, direction="N/A", reason=reason, result=start_cell)
            self.catalog_cell_visited(start_cell)
            return action_and_result
        elif action == "move":
            move_list = self.get_actions()
            current_cell = move_list[len(move_list)-1].result
            current_location = current_cell.location
            new_cell_location = location_in_direction_of(current_location,direction)

            new_cell = self.make_mock_cell(new_cell_location)
            move = self.add_action(action=action, direction=direction, reason=reason, result=new_cell)
            self.catalog_cell_visited(new_cell)
            return move

    def get_nearby(self, adjacent_location):
        adjacent_locations = self.get_adjacent_locations(adjacent_location)
        ret_val = ''
        for adjacent_location in adjacent_locations:
            for dnd_object in DND_OBJECT:
                if adjacent_location in self._object_locations[dnd_object]:
                    ret_val = add_comma(ret_val,dnd_object.value)

        return ret_val

    def add_object_location(self, dnd_object, location):
        self._object_locations[dnd_object].append(location)

    def set_nearby(self, CellResult):
        location = CellResult.location
        CellResult.nearby = self.get_nearby(location)

    def make_mock_cell(self, location) -> CellResult:
        ret_val = CellResult(location=location)
        self.set_nearby(ret_val)
        return ret_val

    def calculate_adjacent_notvisited_cells(self):
        for cell_location in self.get_cells_visited():
            cell_visited: CellResult = self.get_cells_visited()[cell_location]
            print("Visited",cell_visited)
            location = cell_visited.location
            unknown_adjacent_locations = self.get_adjacent_locations_not_visited(location)
            for dnd_object in cell_visited.get_nearby_dnd_objects():
                pass

