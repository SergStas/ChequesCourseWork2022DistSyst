from os import getenv

import pika

CONNECTION_URL = 'amqp://rabbituser:password@rabbit:5672/%2F'
QUEUE_NAME = getenv("RABBIT_QUEUE_NAME")
connection = pika.BlockingConnection(pika.URLParameters(CONNECTION_URL))


def publish_task(task: str):
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=task.encode('utf-8'))
