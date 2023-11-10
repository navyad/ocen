import json

def to_json(byte_data):
    json_string = byte_data.decode('utf-8')
    return json.loads(json_string)


class Constansts:
    LOAN_AGENT_BASE_URL = "http://localhost:8000"
    LENDER_A_BASE_URL = "http://localhost:8001"
    LENDER_B_BASE_URL = "http://localhost:8002"
    PRODUCT_ID = "BNPL23"
    PRODUCT_NETWORK_ID = "NTX_BPNL" 


def update_requst_id(payload, request_id):
    payload_dict = json.loads(payload)
    payload_dict["metadata"]["requestId"] = request_id 
    return json.dumps(payload_dict)
