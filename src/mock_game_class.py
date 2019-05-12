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

    # TODO: Implement functionality for below
    # def find_stationary_objects(self):
    #     self.find_pit()
    #     self.find_dragon()
    #     self.find_magic_arrow()
    #     self.find_rope()
    #
    # def find_stationary_object(self,object_name):
    #     for cell_location in self.get_cells_visited():
    #         cell_visited: CellResult = self.get_cells_visited()[cell_location]
    #         location = cell_visited.location
    #         adjacent_locations = self.get_adjacent_locations_all(location)
    #         if object_name not in cell_visited.get_nearby_dnd_objects():
    #             self.set_not_nearby(adjacent_locations,object_name)




    def catalog_object_location(self, dnd_object, location):
        self._object_locations[dnd_object].append(location)

    def do_action_and_store(
            self,
            action,
            direction="N/A",
            reason=""):
        if action == "restart":
            start_cell = CellResult(location=self._mock_start_location)
            action_and_result = self.catalog_action(action=action, direction="N/A", reason=reason, result=start_cell)
            self.catalog_cell_visited(start_cell)
            return action_and_result
        elif action == "move":
            move_list = self.get_actions()
            current_cell = move_list[len(move_list)-1].result
            current_location = current_cell.location
            new_cell_location = location_in_direction_of(current_location,direction)

            new_cell = self.make_mock_cell(new_cell_location)
            move = self.catalog_action(action=action, direction=direction, reason=reason, result=new_cell)
            self.catalog_cell_visited(new_cell)
            return move

    def get_nearby(self, adjacent_location):
        adjacent_locations = self.get_adjacent_locations_all(adjacent_location)
        ret_val = ''
        for adjacent_location in adjacent_locations:
            for dnd_object in DND_OBJECT:
                if adjacent_location in self._object_locations[dnd_object]:
                    ret_val = add_comma(ret_val,dnd_object.value)

        return ret_val

    def make_mock_cell(self, location) -> CellResult:
        ret_val = CellResult(location=location)
        self.set_nearby(ret_val)
        return ret_val

    def set_nearby(self, CellResult):
        location = CellResult.location
        CellResult.nearby = self.get_nearby(location)

