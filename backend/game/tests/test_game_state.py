import typing
import pytest
import game.constants as game_constants
import game.services.board as board_service
import game.services.state as state_service


def test_game_state_has_place() -> None:
    """
    Test if there is a place to put a marker.
    """
    game = board_service.BoardService()
    game_state = state_service.StateService(board=game.board)
    assert game_state.has_place() is True


def test_game_state_doesnt_have_place() -> None:
    """
    Test if there is no place to put a marker.
    """
    game_state = state_service.StateService([[1] * 7] * 7)
    assert game_state.has_place() is False


def test_game_state_has_place_left() -> None:
    """
    Test if there is no place to put a marker.
    """
    board = [[1] * 7] * 7
    board[0][0] = 0
    game_state = state_service.StateService(board)
    assert game_state.has_place() is True

    game = board_service.BoardService(board=board)
    updated = game.mark(0, 1, game_constants.Direction.LEFT)
    assert updated is True
    assert game_state.has_place() is False


@pytest.mark.parametrize(
    "state, expected_winner, winner_exists",
    [
        (
            [1, 1, 1, 1, 0, 0, 0],
            1,
            True,
        ),
        (
            [1, 1, 1, 2, 0, 0, 0],
            0,
            False,
        ),
        (
            [1, 1, 1, 2, 2, 2, 2],
            2,
            True,
        ),
        (
            [1, 1, 1, 0, 2, 2, 2],
            0,
            False,
        ),
        (
            [1, 1, 1, 3, 2, 2, 2],
            0,
            False,
        ),
    ],
)
def test_has_winner_row(
    state: typing.List[int], expected_winner: int, winner_exists: bool
) -> None:
    """
    Test if there is a winner in a row.
    """
    game_state = state_service.StateService(None)
    marker, winner = game_state.has_winner_row(state)
    assert marker == expected_winner
    assert winner == winner_exists


def test_has_winner_row_right() -> None:
    """
    Test if there is a winner in a row.
    """
    game_state = state_service.StateService(None)
    marker, winner = game_state.has_winner_row([0, 0, 0, 1, 1, 1, 1])
    assert marker == 1
    assert winner is True
