from flask import Flask
from .config import CONFIG_MAP
from .extensions import db, migrate


def create_app(config_name="development"):
    app = Flask(__name__)

    if config_name not in CONFIG_MAP:
        raise ValueError(f"Unknown config_name: {config_name}")

    app.config.from_object(CONFIG_MAP[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
