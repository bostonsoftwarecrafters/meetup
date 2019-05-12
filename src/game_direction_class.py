from enum import Enum


class GameDirection(Enum):
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

NORTH = GameDirection.NORTH
SOUTH = GameDirection.SOUTH
WEST = GameDirection.WEST
EAST = GameDirection.EAST
