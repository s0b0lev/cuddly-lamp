from enum import Enum


class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"

    @classmethod
    def available_directions(cls):
        return [cls.RIGHT, cls.LEFT]


EMPTY_MARKER = 0

# when a player has N consecutive pieces on a diagonal, column, or row
WINNER_SCORE = 4
