from direction_class import Direction

NORTH,SOUTH,WEST,EAST = (Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST)

def test_enum_direction():
    assert NORTH.value == "north"
    assert SOUTH.value == "south"
    assert WEST.value == "west"
    assert EAST.value == "east"

def test_direction_constants():
    assert Direction.NORTH == NORTH
    assert Direction.SOUTH == SOUTH
    assert Direction.WEST == WEST
    assert Direction.EAST == EAST


def test_opposite_direction():
    assert NORTH.opposite() == SOUTH
    assert SOUTH.opposite() == NORTH
    assert EAST.opposite() == WEST
    assert WEST.opposite() == EAST
