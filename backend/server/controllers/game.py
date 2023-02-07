import typing

from flask import request

import backend.server.services.game as game_service


def create_game() -> typing.Dict[str, typing.Any]:
    """
    Create a new game. Return game object.
    """
    game = game_service.GameService.create(request.json.get("name"))
    return {
        "uuid": game.uuid,
        "name": game.name,
        "board": game.board,
    }


def join_game(game_uuid: str):
    return "hello"


def move(game_uuid: str):
    # player_uuid: str, direction: str, row_index: int
    name = request.json.get("name")
    return "hello"


def games_list():
    return "hello"
