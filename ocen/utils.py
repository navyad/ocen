import json
import requests
import copy


HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


def to_json(byte_data):
    json_string = byte_data.decode('utf-8')
    return json.loads(json_string)


class Constants:
    LOAN_AGENT_BASE_URL = "http://localhost:8000"
    LENDER_A_BASE_URL = "http://localhost:8001"
    LENDER_B_BASE_URL = "http://localhost:8002"
    PRODUCT_ID = "BNPL23"
    PRODUCT_NETWORK_ID = "NTX_BPNL" 


def update_request_id(payload, request_id):
    modified_payload = copy.deepcopy(payload)
    modified_payload['metadata']['requestId'] = request_id
    return json.dumps(modified_payload)


def make_request(url, data):
    response = requests.post(url, data=data, headers=HEADERS)
    return response.json()
