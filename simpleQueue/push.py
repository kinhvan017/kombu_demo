from kombu import BrokerConnection

connection = BrokerConnection("amqp://guest:guest@localhost:5672//")

queue = connection.SimpleQueue("logs")

payload = { "severity":"info", "message":"this is just a log", "ts":"2013/09/30T15:10:23" }

queue.put(payload, serializer='pickle')

queue.close()