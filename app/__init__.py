from flask import Flask
import os
from datetime import timedelta

from .db import init_driver
from .views.common import common_views


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        NEO4J_URI=os.getenv('NEO4J_URI'),
        NEO4J_USERNAME=os.getenv('NEO4J_USERNAME'),
        NEO4J_PASSWORD=os.getenv('NEO4J_PASSWORD'),
        NEO4J_DATABASE=os.getenv('NEO4J_DATABASE'),

        JWT_SECRET=os.getenv('JWT_SECRET'),
        JWT_AUTH_HEADER_PREFIX="Bearer",
        JWT_VERIFY_CLAIMS="signature",
        JWT_EXPIRATION_DELTA=timedelta(360)
    )

    with app.app_context():
        uri = app.config.get("NEO4J_URI")
        username = app.config.get("NEO4J_USERNAME")
        password = app.config.get("NEO4J_PASSWORD")

        init_driver(uri, username, password)

    app.register_blueprint(common_views)

    return app
