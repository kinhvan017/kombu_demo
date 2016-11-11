from kombu import Exchange, Queue

task_exchange = Exchange("ce", type="fanout")
queue_events_db = Queue("events.db", task_exchange)
queue_events_notify = Queue("events.notify", task_exchange)

