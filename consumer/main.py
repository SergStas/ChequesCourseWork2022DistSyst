import sys
import pika
import requests
import json
from typing import Optional
from os import getenv
import redis


USER = getenv("RABBITMQ_DEFAULT_USER")
PASSWORD = getenv("RABBITMQ_DEFAULT_PASS")
BROKER_HOSTNAME = 'rabbit'
WEB_HOSTNAME = 'nginx'
WEB_PORT = '80'


CONNECTION_URL = f'amqp://{USER}:{PASSWORD}@{BROKER_HOSTNAME}:5672/%2F'

QUEUE_NAME = 'links'
redis_cache = redis.Redis(host="cache", port=6379, db=0)


def get_link_status(link: str) -> str:
    status = get_status_from_cache(link)
    if status is None:
        status = fetch_status_from_inet(link)
        update_status_in_cache(link, status)
    return status


def get_status_from_cache(link: str) -> Optional[str]:
    key = f"url-{link}"
    value = redis_cache.get(key)
    return None if value is None else value.decode("utf-8")


def update_status_in_cache(link: str, status_code: str) -> None:
    key = f"url-{link}"
    redis_cache.set(name=key, value=status_code)


def fetch_status_from_inet(link: str) -> str:
    response = requests.get(link, timeout=10)
    status = str(response.status_code)
    return status


def handle_message(ch, method, properties, body):
    try:
        pass
        # body_str = body.decode('utf-8')
        # link_json = json.loads(body_str)
        # status = get_link_status(link_json['url'])
        # payload = {'id': int(link_json['id']), 'status': str(status)}
        # payload_json = json.dumps(payload)
        # result = requests.put(f'http://{WEB_HOSTNAME}:{WEB_PORT}/links/', data=payload_json)
        # print(result.content)
    except Exception as e:
        print(e)


def main():
    connection = pika.BlockingConnection(pika.URLParameters(CONNECTION_URL))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=handle_message)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
