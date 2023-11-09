import requests
import json

from celery import shared_task
from lender.payloads.create_loan_applications_response import payload as payload_loan_request
from lender.payloads.consent_handle_response import payload as payload_consent
from lender.payloads.generate_offer_response import payload as payload_generate

LA_URL = "http://localhost:8000"
HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


def make_request(url, data):
    response = requests.post(url, data=data, headers=HEADERS)
    return response.json()
   

@shared_task(bind=True)
def process_loan_application(data):
    """
    Lender async processing
    """
    print("called: process_loan_application")
    url = f"{LA_URL}/v4.0.0alpha/loanApplications/createLoanResponse"
    make_request(url=url, data=payload_loan_request) 
    print(f"response: {url}")


@shared_task(bind=True)
def process_consent_handle(data):
    """
    Lender async processing
    """
    print("called: process_consent_handle")
    url = f"{LA_URL}/v4.0.0alpha/consent/consentHandleResponse"
    make_request(url=url, data=payload_consent) 
    print(f"response: {url}")


@shared_task(bind=True)
def process_generate_offer(data):
    """
    Lender async processing
    """
    print("called: process_consent_handle")
    url = f"{LA_URL}/v4.0.0alpha/offers/generateoffersResponse"
    make_request(url=url, data=payload_generate) 
    print(f"response: {url}")
