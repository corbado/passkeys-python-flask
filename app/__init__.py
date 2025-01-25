# app/__init__.py

from flask import Flask, g
from flask_migrate import Migrate

from .config import Config
from .db import db
from .utils.authentication import (
    get_authenticated_user_from_cookie,
    get_authenticated_user_from_authorization_header,
    init_corbado_sdk
)

migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    # Load configuration
    app.config.from_object(Config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    # Initialize Corbado SDK
    init_corbado_sdk(app)

    @app.before_request
    def attach_user():
        """
        Middleware to retrieve the authenticated user from cookies or Authorization header
        and attach it to Flask's `g` object.
        """
        corbado_user = get_authenticated_user_from_cookie() or get_authenticated_user_from_authorization_header()
        g.corbado_user = corbado_user


    @app.context_processor
    def inject_base_info():
        """
        Injects base information into all templates.
        """
        return {
            'CORBADO_PROJECT_ID': app.config['CORBADO_PROJECT_ID'],
            'CORBADO_FRONTEND_API': app.config['CORBADO_FRONTEND_API'],
            'corbado_user': g.corbado_user
        }

    # Register routes
    with app.app_context():
        from . import routes

    return app
