from enum import Enum

class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    WEST = "west"
    EAST = "east"

    def opposite(self):
        opposites = {
            self.NORTH: self.SOUTH,
            self.SOUTH: self.NORTH,
            self.EAST: self.WEST,
            self.WEST: self.EAST
        }
        return opposites[self]

NORTH,SOUTH,WEST,EAST = Direction

def test_enum_direction():
    assert Direction.NORTH.value == "north"
    assert Direction.SOUTH.value == "south"
    assert Direction.WEST.value == "west"
    assert Direction.EAST.value == "east"

def test_direction_constants():
    assert Direction.NORTH == NORTH
    assert Direction.SOUTH == SOUTH
    assert Direction.WEST == WEST
    assert Direction.EAST == EAST


def test_opposite_direction():
    assert Direction.NORTH.opposite() == Direction.SOUTH
    assert Direction.SOUTH.opposite() == Direction.NORTH
    assert Direction.EAST.opposite() == Direction.WEST
    assert Direction.WEST.opposite() == Direction.EAST
