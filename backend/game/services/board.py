import typing

import game.constants as game_constants


class BoardService:
    """
    Game service. Handles game logic.
    Game board is represented as a list of lists.
    """

    def __init__(self, board: typing.List[int] = None) -> None:
        self.board = board or self.initialize()

    def initialize(self) -> typing.List[int]:
        """
        Initialize game board.
        """
        return [[0] * 7] * 7

    def mark(
        self, row_index: int, marker: int, direction: int
    ) -> typing.Tuple[typing.List[int], bool]:
        """
        Mark a row with a marker. Return updated board and if it was updated.
        """
        if row_index not in range(0, len(self.board)):
            raise ValueError("Invalid row index")

        self.board[row_index], updated = self.mark_row(
            self.board[row_index], marker, direction
        )
        return updated

    def mark_row(
        self, row: typing.List[int], marker: int, direction: game_constants.Direction
    ) -> typing.Tuple[typing.List[int], bool]:
        """
        Mark a row with a marker. Return updated row and if it was updated.
        """
        updated = False
        if direction == game_constants.Direction.RIGHT:
            counter = len(row) - 1
            for value in row[::-1]:
                if value == 0:
                    row[counter] = marker
                    updated = True
                    break
                counter -= 1
        elif direction == game_constants.Direction.LEFT:
            for idx, value in enumerate(row):
                if value == 0:
                    row[idx] = marker
                    updated = True
                    break
        return row, updated
