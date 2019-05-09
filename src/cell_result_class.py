from dnd_constants import DND_OBJECT


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

    def is_bat_nearby(self):
        return self.is_object_nearby(DND_OBJECT.BAT)

    def is_magic_arrow_nearby(self):
        return self.is_object_nearby(DND_OBJECT.MAGIC_ARROW)

    def is_pit_nearby(self):
        return self.is_object_nearby(DND_OBJECT.PIT)

    def is_dragon_nearby(self):
        return self.is_object_nearby(DND_OBJECT.DRAGON)

    def is_rope_nearby(self):
        return self.is_object_nearby(DND_OBJECT.ROPE)

    def is_object_nearby(self,dnd_object):
        return dnd_object.value in self.nearby

    def get_nearby_dnd_objects(self):
        ret_val = []
        for dnd_object in DND_OBJECT:
            if self.is_object_nearby(dnd_object):
                ret_val.append(dnd_object)
        return ret_val



