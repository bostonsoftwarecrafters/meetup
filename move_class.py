from cell_result_class import CellResult


class WarriorMoveAndResult(object):
    def __init__(self,
                 action: str,
                 direction: str,
                 reason: str,
                 result: CellResult
                 ):
        self.action = action
        self.direction = direction
        self.reason = reason
        self.result = result