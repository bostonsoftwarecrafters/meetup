#TODO Decide on whether to use enum or str
from dnd_constants import BAT_STR, DRAGON_STR, MAGIC_ARROW_STR, PIT_STR, ROPE_STR

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


    def key_fields_equal(self,obj):
        print("debug")
        print(self.location,"n",self.nearby,"i",self.inventory,self.status)
        print(obj.location,"n",obj.nearby,"i",obj.inventory,obj.status)
        try:
            ret_val = self.nearby == obj.nearby \
                      and self.inventory == obj.inventory \
                      and self.status == obj.status \
                      and self.location == obj.location
        except:
            ret_val = False
        return ret_val


    def is_bat_nearby(self):
        return self.is_object_nearby(BAT_STR)

    def is_magic_arrow_nearby(self):
        return self.is_object_nearby(MAGIC_ARROW_STR)

    def is_pit_nearby(self):
        return self.is_object_nearby(PIT_STR)

    def is_dragon_nearby(self):
        return self.is_object_nearby(DRAGON_STR)

    def is_rope_nearby(self):
        return self.is_object_nearby(ROPE_STR)

    def is_object_nearby(self,object_str):
        return object_str in self.nearby



