import requests
import json

from celery import shared_task
from loanagent.payloads.consent_status_response import payload

HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


def make_request(url, data):
    response = requests.post(url, data=data, headers=HEADERS)
    return response.json()
   

@shared_task(bind=True)
def process_consent_status(data):
    """
    send async call to lender for response
    """
    LENDER_URL = "http://localhost:8001"
    print("called: process_consent_status")
    url = f"{LENDER_URL}/v4.0.0alpha/consent/statusResponse"
    make_request(url=url, data=payload) 
    print(f"response: {url}")
