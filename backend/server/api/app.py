import os
from pathlib import Path

import connexion

from backend.server.api.extensions import cors, db, migrate


BASE_DIR = Path(__file__).parent
ENV = os.environ.get("FLASK_ENV", "local").lower()


def create_app() -> connexion.FlaskApp:
    options = {"swagger_ui": True}
    connexion_app = connexion.FlaskApp(__name__, specification_dir=".", options=options)
    connexion_app.add_api("openapi.yaml", validate_responses=True)
    return connexion_app.app


def register_extensions(app: connexion.FlaskApp) -> None:
    register_db(app)
    setup_cors(app)


def setup_cors(app: connexion.FlaskApi) -> None:
    cors_origin = "CORS_ORIGIN"
    cors.init_app(
        app,
        supports_credentials=True,
        resources={
            r"/*": {"origins": cors_origin},
        },
    )


def register_db(app: connexion.FlaskApp) -> None:
    app.db = db
    db_url = "DATABASE_URI"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db, directory=BASE_DIR / "migrations")
