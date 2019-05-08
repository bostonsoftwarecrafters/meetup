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

    def __eq__(self,obj):
        return self.__dict__ == obj.__dict__

    def __str__(self):
        return "str: "+str(self.__dict__)

    def __repr__(self):
        return "rep: "+str(self.__dict__)

