from flask import Flask
from .views.common import common_views


def create_app():
    app = Flask(__name__)
    app.register_blueprint(common_views)

    return app
