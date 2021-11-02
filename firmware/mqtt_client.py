import logging
import uuid

from paho.mqtt import client as mqtt_client

from settings import settings

logger = logging.getLogger()


class Client:
    _client = None

    @property
    def client_id(self):
        return f'client-{uuid.uuid4()}'

    def __init__(self):
        client = mqtt_client.Client(self.client_id)
        client.on_publish = Client.on_publish
        client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
        self._client = client

    def publish(self, topic, payload):
        return self._client.publish(topic, payload)

    @staticmethod
    def on_publish(client, userdata, result):
        logger.debug(f'{userdata} published with {result} result')
