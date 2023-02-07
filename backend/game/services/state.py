import typing

import backend.game.constants as game_constants


class StateService:
    """
    Represents current state of the game.
    It can be used to check if game is in progress, if there is a winner, etc.
    """

    def __init__(self, board: typing.List[typing.List[int]] = None) -> None:
        self.board = board

    def in_progress(self) -> bool:
        """
        Check if game is in progress.
        """
        _, winner = self.has_winner()
        return self.has_place() and not winner

    def get_winner(self) -> typing.Optional[int]:
        """
        Get winner.
        """
        if self.in_progress():
            return None

        marker, _ = self.has_winner()
        if marker == game_constants.EMPTY_MARKER:
            return None

        return marker

    def has_place(self) -> bool:
        """
        Check if there is a place to put a marker.
        """
        return any(game_constants.EMPTY_MARKER in row for row in self.board)

    def has_winner(self) -> bool:
        """
        Check if there is a winner.
        """
        return self.has_winner_horizontal() or self.has_winner_vertical()

    def has_winner_horizontal(self) -> bool:
        """
        Check if there is a winner in a horizontal row.
        """
        for row in self.board:
            marker, winner = self.has_winner_row(row)
            if winner:
                return marker, True

        return game_constants.EMPTY_MARKER, False

    def has_winner_vertical(self) -> bool:
        """
        Check if there is a winner in a vertical row.
        """
        for column in zip(*self.board):
            marker, winner = self.has_winner_row(column)
            if winner:
                return marker, True

        return game_constants.EMPTY_MARKER, False

    def has_winner_row(self, row: typing.List[int]) -> bool:
        """
        Check if there is a winner in a row. 
        """
        score = 0
        previous_marker = game_constants.EMPTY_MARKER
        for marker in row:
            if marker == game_constants.EMPTY_MARKER:
                score = 0
                continue

            if marker == previous_marker:
                score += 1

            if marker != previous_marker:
                score = 1
                previous_marker = marker
                continue

            if score == game_constants.WINNER_SCORE:
                return marker, True

        return game_constants.EMPTY_MARKER, False
