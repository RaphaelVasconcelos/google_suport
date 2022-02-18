import json
from typing import Sequence

from src.models.pubsub.side_effect_messages import SideEffectMessage


class PubSubMessage:

    def __init__(self, side_effect_messages: Sequence[SideEffectMessage]):
        self.side_effect_messages = side_effect_messages

    def json(self) -> str:
        side_effect_messages_data = [side_effect_message.dict() for side_effect_message in self.side_effect_messages]
        return json.dumps({'side_effect_messages': side_effect_messages_data})

    @staticmethod
    def extract_side_effect_message_data(command_class, message_data: dict) -> dict:
        command_class_fields = sorted(list(command_class.__fields__.keys()))
        for side_effect_message_data in message_data['side_effect_messages']:
            side_effect_message_data_keys = sorted(list(side_effect_message_data.keys()))
            if side_effect_message_data_keys == command_class_fields:
                return side_effect_message_data
        return {}
