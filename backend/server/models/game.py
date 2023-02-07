import uuid

import sqlalchemy as sa

import backend.server.api.extensions as api_extension


class Game(api_extension.db.Model):
    uuid = sa.Column(sa.String(100), primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.String(100), nullable=False)
    game = sa.Column(sa.JSON, nullable=False)
    aciton_log = sa.Column(sa.JSON, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False, default=False)
    created_at = sa.Column(sa.DateTime, nullable=False, default=sa.func.now)

    __tablename__ = "game"

    def __repr__(self) -> str:
        return f"<Game {self.uuid} {self.name}>"
