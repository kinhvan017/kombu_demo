from __future__ import with_statement
from queues import task_exchange

from kombu.common import maybe_declare
from kombu.pools import producers


if __name__ == "__main__":
    from kombu import BrokerConnection

    connection = BrokerConnection("amqp://guest:guest@localhost:5672//")

    with producers[connection].acquire(block=True) as producer:
        maybe_declare(task_exchange, producer.channel)
        
        payload = {"type": "handshake", "content": "hello #1"}
        producer.publish(payload, exchange = 'msgs', serializer="pickle", routing_key = 'message_1')
        
        payload = {"type": "handshake", "content": "hello #2"}
        producer.publish(payload, exchange = 'msgs', serializer="pickle", routing_key = 'message_2')

