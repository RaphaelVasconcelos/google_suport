import base64
import json

import flask
import pydantic
from flask.views import View

from src.models.pubsub.pubsub_message import PubSubMessage


THERE_IS_NO_MESSAGE_TO_PROCCESS = 202


class InternalBaseView(View):

    command: pydantic.BaseModel

    def _extract_side_effect_message_data(self, pubsub_message_data: dict):
        message_data_json = base64.b64decode(pubsub_message_data['message']['data']).decode('utf-8')
        return PubSubMessage.extract_side_effect_message_data(self.command, json.loads(message_data_json))

    def dispatch_request(self, *args, **kwargs) -> flask.Response:
        side_effect_message_data = self._extract_side_effect_message_data(flask.request.get_json())
        if not side_effect_message_data:
            return flask.Response(status=THERE_IS_NO_MESSAGE_TO_PROCCESS)
        return self._handle_request(side_effect_message_data=side_effect_message_data, *args, **kwargs)

    def _handle_request(self, side_effect_message_data: dict, *args, **kwargs) -> flask.Response:
        raise NotImplementedError()
