import json

def to_json(byte_data):
    json_string = byte_data.decode('utf-8')
    return json.loads(json_string)
