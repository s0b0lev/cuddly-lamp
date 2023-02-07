import uuid
import backend.server.models.domain_objects as domain_objects
import backend.server.dal.game as game_dal


class GameService:
    @classmethod
    def create(cls, name: str) -> domain_objects.Game:
        """
        Create a new game. Return game object.
        """
        return game_dal.SQLAlchemyDAL.create(name)
