from queues import queue_msg_2
from kombu.mixins import ConsumerMixin

class C(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection
        return
    
    def get_consumers(self, Consumer, channel):
        return [Consumer( queue_msg_2, callbacks = [self.on_message])]
    
    def on_message(self, body, message):
        print ("RECEIVED MSG - body: %r" % (body,))
        print ("RECEIVED MSG - message: %r" % (message,))
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

