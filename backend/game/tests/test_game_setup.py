import typing
import pytest

import game.constants as game_constants
import game.services.board as board_service


def test_game_init() -> None:
    """
    Test if game is initialized.
    """
    game = board_service.BoardService()
    assert game.initialize() == [[0] * 7] * 7


def test_game_mark() -> None:
    """
    Test if marker is placed in the row.
    """
    game = board_service.BoardService()
    game.mark(row_index=2, marker=1, direction=game_constants.Direction.LEFT)
    assert game.board[2][0] == 1


@pytest.mark.parametrize(
    "row_state, marker, direction, expected_state, should_update",
    [
        (
            [0, 0, 0, 0, 0, 0, 0],
            1,
            game_constants.Direction.LEFT,
            [1, 0, 0, 0, 0, 0, 0],
            True,
        ),
        (
            [1, 0, 0, 0, 0, 0, 0],
            1,
            game_constants.Direction.LEFT,
            [1, 1, 0, 0, 0, 0, 0],
            True,
        ),
        (
            [1, 1, 0, 0, 0, 0, 0],
            1,
            game_constants.Direction.LEFT,
            [1, 1, 1, 0, 0, 0, 0],
            True,
        ),
        (
            [1, 1, 1, 0, 0, 0, 0],
            1,
            game_constants.Direction.LEFT,
            [1, 1, 1, 1, 0, 0, 0],
            True,
        ),
        (
            [1, 1, 1, 1, 0, 0, 0],
            1,
            game_constants.Direction.LEFT,
            [1, 1, 1, 1, 1, 0, 0],
            True,
        ),
        (
            [1, 1, 1, 1, 1, 1, 0],
            1,
            game_constants.Direction.LEFT,
            [1, 1, 1, 1, 1, 1, 1],
            True,
        ),
        (
            [1, 1, 1, 1, 1, 1, 1],
            1,
            game_constants.Direction.LEFT,
            [1, 1, 1, 1, 1, 1, 1],
            False,
        ),
        (
            [0, 0, 0, 0, 0, 0, 0],
            1,
            game_constants.Direction.RIGHT,
            [0, 0, 0, 0, 0, 0, 1],
            True,
        ),
        (
            [0, 0, 0, 0, 0, 0, 1],
            1,
            game_constants.Direction.RIGHT,
            [0, 0, 0, 0, 0, 1, 1],
            True,
        ),
        (
            [0, 0, 0, 0, 0, 1, 1],
            1,
            game_constants.Direction.RIGHT,
            [0, 0, 0, 0, 1, 1, 1],
            True,
        ),
        (
            [0, 0, 0, 0, 1, 1, 1],
            1,
            game_constants.Direction.RIGHT,
            [0, 0, 0, 1, 1, 1, 1],
            True,
        ),
        (
            [0, 0, 0, 1, 1, 1, 1],
            1,
            game_constants.Direction.RIGHT,
            [0, 0, 1, 1, 1, 1, 1],
            True,
        ),
        (
            [0, 0, 1, 1, 1, 1, 1],
            1,
            game_constants.Direction.RIGHT,
            [0, 1, 1, 1, 1, 1, 1],
            True,
        ),
        (
            [0, 1, 1, 1, 1, 1, 1],
            1,
            game_constants.Direction.RIGHT,
            [1, 1, 1, 1, 1, 1, 1],
            True,
        ),
        (
            [1, 1, 1, 1, 1, 1, 1],
            1,
            game_constants.Direction.RIGHT,
            [1, 1, 1, 1, 1, 1, 1],
            False,
        ),
    ],
)
def test_game_mark_direction_left(
    row_state: typing.List[int],
    marker: int,
    direction: int,
    expected_state: typing.List[int],
    should_update: bool,
) -> None:
    """
    Test marking a row in a given direction with a given marker.
    This test is parametrized to test all possible directions.
    """
    game = board_service.BoardService()
    updated_row, updated = game.mark_row(row_state, marker, direction)
    assert updated_row == expected_state
    assert updated == should_update


def test_game_mark_direction_invalid() -> None:
    """
    Test marking a row by invalid index.
    """
    game = board_service.BoardService()
    with pytest.raises(ValueError):
        game.mark(row_index=7, marker=2, direction=game_constants.Direction.LEFT)
