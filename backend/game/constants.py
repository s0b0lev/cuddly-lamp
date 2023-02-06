class Direction:
    RIGHT = "R"
    LEFT = "L"

    @classmethod
    def available_directions(cls):
        return [cls.RIGHT, cls.LEFT]

EMPTY_MARKER = 0

# when a player has N consecutive pieces on a diagonal, column, or row
WINNER_SCORE = 4
