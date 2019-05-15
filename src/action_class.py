import copy

from cell_result_class import CellResult


class Action(object):
    def __init__(self,
                 action: str,
                 direction: str,
                 reason: str,
                 result: CellResult
                 ):
        self.action = action
        self.direction = direction
        self.reason = reason
        self.result = copy.deepcopy(result)

    def key_field_equals(self,obj):
        try:
            ret_val = self.action == obj.action \
                and self.direction == obj.direction \
                and self.result.key_fields_equal(obj.result)
        except:
            ret_val = False
        return ret_val