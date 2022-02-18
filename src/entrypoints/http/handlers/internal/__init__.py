from flask.blueprints import Blueprint

from src.entrypoints.http.handlers.internal.operation_log import CreateOperationLogView


internal_api = Blueprint('InternalAPI', __name__, url_prefix='/internal')


internal_api.add_url_rule(
    '/operation-log/',
    view_func=CreateOperationLogView.as_view(name='create_operation_log'),
    methods=['POST'],
)
