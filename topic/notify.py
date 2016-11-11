from queues import queue_notify
from kombu.mixins import ConsumerMixin

class C(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection
        return
    
    def get_consumers(self, Consumer, channel):
        return [Consumer( queue_notify, callbacks = [self.on_message])]
    
    def on_message(self, body, message):
        print ("notify: RECEIVED MSG - body: %r" % (body,))
        print ("notify: RECEIVED MSG - message: %r" % (message,))
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

