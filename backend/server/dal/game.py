from sqlalchemy.dialects.postgresql import insert

import backend.server.api.extensions as api_extension
import backend.server.models.game as game_models
import backend.server.models.domain_objects as domain_objects


class SQLAlchemyDAL:
    @classmethod
    def create(self, name: str) -> game_models.Game:
        statement = (
            insert(game_models.Game)
            .values(name=name)
            .returning(
                game_models.Game.c.uuid,
                game_models.Game.c.name,
                game_models.Game.c.board,
            )
        )
        api_extension.db.session.execute(statement)
        api_extension.db.session.commit()
        result = api_extension.db.session.query()
        return domain_objects.Game(
            uuid=result.uuid,
            name=result.name,
            board=result.board,
        )
