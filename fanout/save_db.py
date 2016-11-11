from queues import queue_events_db
from kombu.mixins import ConsumerMixin

class C(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection
        return
    
    def get_consumers(self, Consumer, channel):
        return [Consumer( queue_events_db, callbacks = [self.on_message])]
    
    def on_message(self, body, message):
        print ("save_db: RECEIVED MSG - body: %r" % (body,))
        print ("save_db: RECEIVED MSG - message: %r" % (message,))
        message.ack()
        return


if __name__ == "__main__":
    from kombu import BrokerConnection
    from kombu.utils.debug import setup_logging
    
    setup_logging(loglevel="DEBUG")

    with BrokerConnection("amqp://guest:guest@localhost:5672//") as connection:
        try:
            C(connection).run()
        except KeyboardInterrupt:
            print("bye bye")

