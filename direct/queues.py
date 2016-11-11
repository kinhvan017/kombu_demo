from kombu import Exchange, Queue

task_exchange = Exchange("msgs", type="direct")
queue_msg_1 = Queue("messages_1", task_exchange, routing_key = 'message_1')
queue_msg_2 = Queue("messages_2", task_exchange, routing_key = 'message_2')