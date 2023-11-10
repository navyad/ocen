import requests
import json

from celery import shared_task
from loanagent.payloads.consent_status_response import payload


from ocen.utils import update_request_id, make_request, Constants


@shared_task(bind=True)
def process_consent_status(self, data):
    """
    send async call to lender for response
    """
    request_id = data['metadata']['requestId']
    LENDER_URL = Constants.LENDER_A_BASE_URL 
    print("called: process_consent_status")
    url = f"{LENDER_URL}/v4.0.0alpha/consent/statusResponse"
    modified_payload = update_request_id(payload, request_id)
    make_request(url=url, data=modified_payload)
    print(f"response: {url}")
