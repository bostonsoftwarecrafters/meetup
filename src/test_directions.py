from game_direction_class import GameDirection, NORTH,SOUTH,WEST,EAST

# NORTH,SOUTH,WEST,EAST = (Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST)

def test_enum_direction():
    assert NORTH.value == "north"
    assert SOUTH.value == "south"
    assert WEST.value == "west"
    assert EAST.value == "east"

def test_direction_constants():
    assert GameDirection.NORTH == NORTH
    assert GameDirection.SOUTH == SOUTH
    assert GameDirection.WEST == WEST
    assert GameDirection.EAST == EAST


def test_opposite_direction():
    assert NORTH.opposite() == SOUTH
    assert SOUTH.opposite() == NORTH
    assert EAST.opposite() == WEST
    assert WEST.opposite() == EAST
