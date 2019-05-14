import copy
from tokenize import String

from action_class import Action
from cell_result_class import CellResult
from d_and_d_class import DNDGame
from d_and_d_utility import add_comma,  location_in_direction_of
from dnd_constants import DNDObjEnum, MAGIC_ARROW, ROPE, PIT, DRAGON, BAT
from game_direction_class import GameDirection


MOCK_UID = "MOCK.1234"
class MockGame(DNDGame):
    def __init__(self, start_location):
        self._derived_bats = {}
        self._bat_fly_to_on_move_location = {}
        self._derived_contents = {}
        self._mock_start_location = start_location
        self._object_locations = {}
        for object_enum in DNDObjEnum:
            self._object_locations[object_enum] = []
        super().__init__(MOCK_UID)

    def do_action_and_store(
            self,
            action,
            direction="N/A",
            reason=""):
        if action == "restart":
            start_cell = CellResult(location=self._mock_start_location)
            action = self.catalog_action(action=action, direction="N/A", reason=reason, result=start_cell)
            self.catalog_cell_visited(start_cell)
            return action
        elif action == "move":
            move_list = self.get_actions()
            source_cell = move_list[len(move_list)-1].result
            source_location = source_cell.location
            source_move_index = len(move_list)-1
            new_move_index = source_move_index + 1
            if source_cell.status == "Alive":
                new_cell_location = location_in_direction_of(source_location,direction)
                bat_fly_to = self.get_bat_fly_to(new_move_index, new_cell_location)
                if bat_fly_to != "":
                    new_cell_location = bat_fly_to
            else:
                new_cell_location = source_location
            new_cell = self.make_mock_cell(new_cell_location)
            self.update_mock_inventory(new_cell, source_cell.inventory)
            self.update_danger(new_cell)
            self.remove_rope_if_pit(new_cell,source_cell)
            move = self.catalog_action(action=action, direction=direction, reason=reason, result=new_cell)
            self.update_bats_nearby(move.result, new_move_index)
            self.catalog_cell_visited(move.result)
            return move

    #TODO: Make inventory non-mutable
    def update_mock_inventory(self, new_cell:CellResult, previous_inventory):
        new_cell.inventory = copy.deepcopy(previous_inventory)
        for obj in (MAGIC_ARROW, ROPE):
            if new_cell.location in self.get_object_locations(obj):
                if obj.value not in new_cell.inventory:
                    new_cell.inventory.append (obj.value)


    def get_mock_nearby(self, adjacent_location):
        adjacent_locations = self.get_adjacent_locations_all(adjacent_location)
        ret_val = ''
        for adjacent_location in adjacent_locations:
            for dnd_object in (DRAGON,ROPE,MAGIC_ARROW,PIT):
                if adjacent_location in self._object_locations[dnd_object]:
                    ret_val = add_comma(ret_val,dnd_object.value)

        return ret_val

    def make_mock_cell(self, location) -> CellResult:
        ret_val = CellResult(location=location)
        self.set_mock_nearby(ret_val)
        return ret_val

    def set_mock_nearby(self, CellResult):
        location = CellResult.location
        CellResult.nearby = self.get_mock_nearby(location)

    def set_mock_object_location(self, dnd_object, location):
        #TODO: See if can shorten
        record: list
        # try:
        record = self._object_locations[dnd_object]
        # except:
        #     record = self._object_locations[dnd_object] = []
        record.append(location)

    def do_action_start(self):
        action = self.do_action_and_store(action="restart")

    def do_action_move(self, direction: GameDirection, reason: str) -> Action:
        action = self.do_action_and_store(action="move", direction=direction, reason=reason)
        return action

    def derive_contents(self):
        actions = self.get_actions()
        for action_index in range (1, len(actions)):
            curr_action:Action = actions[action_index]
            curr_location = curr_action.result.location

            curr_inventory = curr_action.result.inventory
            prev_action:Action = actions[action_index-1]
            prev_inventory = prev_action.result.inventory
            new_inventory_set = set(curr_inventory) - set(prev_inventory)
            self.set_location_derived_content(curr_location,list(new_inventory_set))

            upper_status = curr_action.result.status.upper()
            if DRAGON.value.upper() in upper_status:
                self.set_location_derived_content(curr_location,[DRAGON.value])
            elif PIT.value.upper() in upper_status:
                self.set_location_derived_content(curr_location,[PIT.value])

            predicted_location = location_in_direction_of(prev_action.result.location, curr_action.direction)
            if predicted_location != curr_location:
                self.derive_bat(action_index,predicted_location,curr_location)


    def get_derived_content_of_location(self,location):
        return self._derived_contents[location]

    def set_location_derived_content(self, location, objects):
        self._derived_contents[location] = objects

    def get_derived_contents(self):
        return self._derived_contents

    def get_last_action(self) -> Action:
        actions = self.get_actions()
        action = actions[len(actions)-1]
        return action

    #TODO Add add_object_location
    def get_object_locations(self, obj):
        return self._object_locations[obj]

    def update_danger(self, new_cell):
        location = new_cell.location
        if location in self.get_object_locations(PIT) and ROPE.value not in new_cell.inventory:
            new_cell.status = "(Trapped in a dark pit until dead)"
        elif location in self.get_object_locations(DRAGON):
            new_cell.status = "(Killed by the Dragon)"

    def remove_rope_if_pit(self, new_cell, source_cell):
        if source_cell.location in self.get_object_locations(PIT):
            rope_list = [ROPE.value]
            inventory_set = set(new_cell.inventory) - set(rope_list)
            new_cell.inventory = list (inventory_set)

    def set_mock_bat(self, move, location, fly_to):
        self._bat_fly_to_on_move_location[(move,location)] = fly_to

    def get_bat_fly_to(self, move, location):
        try:
            ret_val = self._bat_fly_to_on_move_location[(move, location)]
        except:
            ret_val = ""
        return ret_val

    def update_bats_nearby(self, result:CellResult, move_number):
        if BAT.value in result.nearby:
            return
        for adjacent_location in self.get_adjacent_locations_all(result.location):
            dummy = self.get_bat_fly_to(move_number+1,adjacent_location)
            if dummy != "":
                result.nearby = add_comma(result.nearby,BAT.value)
                break

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








