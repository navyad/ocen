import requests
import json
import copy

from celery import shared_task
from lender.payloads.create_loan_applications_response import payload as payload_loan_request
from lender.payloads.consent_handle_response import payload as payload_consent
from lender.payloads.generate_offer_response import payload as payload_generate
from lender.payloads.document_response import payload as payload_document
from lender.payloads.set_offer_response import payload as payload_set_offer

from ocen.utils import update_request_id, make_request, Constants

LA_URL = Constants.LOAN_AGENT_BASE_URL


@shared_task(bind=True)
def process_loan_application(self, data):
    """
    Lender async processing
    """
    request_id = data['metadata']['requestId']
    url = f"{LA_URL}/v4.0.0alpha/loanApplications/createLoanResponse"
    modified_payload = update_request_id(payload_loan_request, request_id) 
    make_request(url=url, data=modified_payload) 
    print(f"response: {url}")


@shared_task(bind=True)
def process_consent_handle(self, data):
    """
    Lender async processing
    """
    request_id = data['metadata']['requestId']
    url = f"{LA_URL}/v4.0.0alpha/consent/consentHandleResponse"
    modified_payload = update_request_id(payload_consent, request_id) 
    make_request(url=url, data=modified_payload) 
    print(f"response: {url}")


@shared_task(bind=True)
def process_generate_offer(self, data):
    """
    Lender async processing
    """
    request_id = data['metadata']['requestId']
    url = f"{LA_URL}/v4.0.0alpha/offers/generateoffersResponse"
    modified_payload = update_request_id(payload_generate, request_id) 
    make_request(url=url, data=modified_payload) 
    print(f"response: {url}")


@shared_task(bind=True)
def process_document_request(self, data):
    """
    Lender async processing
    """
    request_id = data['metadata']['requestId']
    url = f"{LA_URL}/v4.0.0alpha/offers/sendAdditionalDocumentsResponse"
    modified_payload = update_request_id(payload_document, request_id) 
    make_request(url=url, data=modified_payload) 
    print(f"response: {url}")


@shared_task(bind=True)
def process_set_offer_request(self, data):
    """
    Lender async processing
    """
    request_id = data['metadata']['requestId']
    url = f"{LA_URL}/v4.0.0alpha/offers/setOffersResponse"
    modified_payload = update_request_id(payload_set_offer, request_id) 
    make_request(url=url, data=modified_payload) 
    print(f"response: {url}")
