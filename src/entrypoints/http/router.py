from flask import Flask

from src.entrypoints.http.handlers.internal import internal_api


def add_routes(app: Flask):
    app.register_blueprint(internal_api)
