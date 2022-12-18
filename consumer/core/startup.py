from os import getenv

import pika
import calculator.worker as calc

USER = getenv("RABBITMQ_DEFAULT_USER")
PASSWORD = getenv("RABBITMQ_DEFAULT_PASS")
BROKER_HOSTNAME = 'rabbit'
CONNECTION_URL = f'amqp://{USER}:{PASSWORD}@{BROKER_HOSTNAME}:5672/%2F'
QUEUE_NAME = getenv("RABBIT_QUEUE_NAME")


def handle_message(ch, method, properties, body):
    cheque_id = body.decode('utf-8')
    calc.perform(cheque_id)


def run():
    connection = pika.BlockingConnection(pika.URLParameters(CONNECTION_URL))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=handle_message)
    channel.start_consuming()
