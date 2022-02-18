import logging
from datetime import datetime
from typing import Any

import flask

from src.entrypoints.http.router import add_routes


logger = logging.getLogger(__name__)


class CustomJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def unhandled_exceptions_handler(exception):
    return flask.jsonify(error=['Internal Server Error']), 500


def validate_request_content_type():
    if flask.request.content_type != 'application/json':
        return flask.jsonify(error=['Invalid Content-Type. Must be application/json.']), 400


def log_action_request():
    logger.info('Starting request processing')


def create_app():
    app = flask.Flask(__name__)
    add_routes(app)
    app.before_request(log_action_request)
    app.before_request(validate_request_content_type)
    app.register_error_handler(500, unhandled_exceptions_handler)
    app.json_encoder = CustomJSONEncoder
    return app
