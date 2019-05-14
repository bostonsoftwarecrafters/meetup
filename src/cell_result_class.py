#TODO Decide on whether to use enum or str
from dnd_constants import BAT, DRAGON, MAGIC_ARROW, PIT, ROPE, DNDObjEnum

#TODO: Change nearby to use list
#TODO: Make immutable
class CellResult(object):
    def __init__(self,
                 location: str,
                 game: str = "On",
                 status: str = "Alive",
                 inventory: list=None,
                 valid_actions: list=None,
                 nearby: str = ""):
        if inventory is None:
            inventory = list()
        elif valid_actions is None:
            valid_actions = list()
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

    # TODO: Complete this function
    # def get_nearby_dnd_objects(self):
    #     ret_val = []
    #     for dnd_object in :
    #         if self.is_object_nearby(dnd_object):
    #             ret_val.append(dnd_object)
    #     return ret_val

    def is_bat_nearby(self):
        return self.is_object_nearby(BAT)

    def is_magic_arrow_nearby(self):
        return self.is_object_nearby(MAGIC_ARROW)

    def is_pit_nearby(self):
        return self.is_object_nearby(PIT)

    def is_dragon_nearby(self):
        return self.is_object_nearby(DRAGON)

    def is_rope_nearby(self):
        return self.is_object_nearby(ROPE)

    def is_object_nearby(self,objectEnum:DNDObjEnum):
        return objectEnum.value in self.nearby



