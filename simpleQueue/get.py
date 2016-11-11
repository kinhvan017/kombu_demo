from kombu import BrokerConnection
from Queue import  Empty

connection = BrokerConnection("amqp://guest:guest@localhost:5672//")

queue = connection.SimpleQueue("logs")

while 1:
    try:
        message = queue.get(block=True, timeout=1)
        print message.payload
        message.ack()
    except Empty:
        pass
    

print message

queue.close()