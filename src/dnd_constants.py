from enum import Enum

#TODO Revisit whether to use enum or class or string, rename DND_OBJECT


class DNDObjEnum(Enum):
    BAT = "Bats"
    DRAGON = "Dragon"
    MAGIC_ARROW = "Magic Arrow"
    PIT = "Pit"
    ROPE = "Rope"

BAT = DNDObjEnum.BAT
DRAGON = DNDObjEnum.DRAGON
MAGIC_ARROW = DNDObjEnum.MAGIC_ARROW
PIT = DNDObjEnum.PIT
ROPE = DNDObjEnum.ROPE
