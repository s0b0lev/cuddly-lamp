import dataclasses
import typing
import uuid


@dataclasses.dataclass
class Game:
    uuid: uuid.UUID
    name: str
    board: typing.List[typing.List[int]]
