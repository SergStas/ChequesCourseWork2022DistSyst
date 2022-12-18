import json

import requests

WEB_HOSTNAME = 'nginx'
WEB_PORT = '80'
API_ROOT_URL = f'http://{WEB_HOSTNAME}:{WEB_PORT}'


def perform(cheque_id: int):
    response = get_cheque(cheque_id)
    transactions = []
    receiver_name = response["payer"]["name"]
    for tr_json in response["positions"]:
        sender_name = tr_json["owner"]["name"]
        sender_entries = [e for e in transactions if sender_name == e["sender"]["name"]]
        if len(sender_entries) > 0:
            transactions[0]["sum"] += float(tr_json["cost"])
        else:
            transactions.append({
                "sender": {"name": sender_name},
                "receiver": {"name": receiver_name},
                "sum": float(tr_json["cost"]),
            })
    post_result(cheque_id, transactions)


def get_cheque(id: int):
    return requests.get(f'{API_ROOT_URL}/cheques/{id}').json()


def post_result(id: int, transactions: []):
    payload = {'cheque_id': int(id), "transactions": transactions}
    payload_json = json.dumps(payload)
    requests.post(f'{API_ROOT_URL}/results', data=payload_json)
