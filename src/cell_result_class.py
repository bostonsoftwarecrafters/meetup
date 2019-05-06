class CellResult(object):
    def __init__(self,
                 location: str,
                 game: str = "On",
                 status: str = "Alive",
                 inventory: list = (""),
                 valid_actions: list = (""),
                 nearby: str = ""):
        self.location = location
        self.game = game
        self.status = status
        self.inventory = inventory
        self.valid_actions = valid_actions
        self.nearby = nearby