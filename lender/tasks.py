import requests
import json

from celery import shared_task
from lender.payloads.create_loan_applications_response import payload as payload_1

BASE_URL = "http://localhost:8001"
HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


@shared_task(bind=True)
def create_loan_application_response(data):
    print("called: create_lon_application_response")
    url = BASE_URL+"/v4.0.0alpha/loanApplications/createLoanResponse"
    response = requests.post(url, data=payload_1, headers=HEADERS)
    json_response = response.json()
    print(f"response: {json_response}")



