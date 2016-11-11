from __future__ import with_statement
from queues import task_exchange

from kombu.common import maybe_declare
from kombu.pools import producers


if __name__ == "__main__":
    from kombu import BrokerConnection

    connection = BrokerConnection("amqp://guest:guest@localhost:5672//")

    with producers[connection].acquire(block=True) as producer:
        maybe_declare(task_exchange, producer.channel)
        
        payload = {"operation": "create", "content": "the object"}
        producer.publish(payload, exchange = 'user', serializer="pickle", routing_key = 'user.write')

        payload = {"operation": "update", "content": "updated fields", "id": "id of the object"}
        producer.publish(payload, exchange = 'user', serializer="pickle", routing_key = 'user.write')

        payload = {"operation": "delete", "id": "id of the object"}
        producer.publish(payload, exchange = 'user', serializer="pickle", routing_key = 'user.write')

        payload = {"operation": "read", "id": "id of the object"}
        producer.publish(payload, exchange = 'user', serializer="pickle", routing_key = 'user.read')
