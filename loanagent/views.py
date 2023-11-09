"""
This is a loan agent API handler
These API endpoints have been invoked from lender in async manner
"""
import json
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from loanagent.tasks import process_consent_status
from ocen.utils import to_json


@csrf_exempt
@require_http_methods(["POST"])
def create_loan_application_response(request):
    print("called: create_loan_application_response")
    data = to_json(request.body) 
    print(data)
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def consent_handle_response(request):
    print("called: create_loan_application_response")
    data = to_json(request.body) 
    print(data)
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def consent_status_request(request):
    print("called: consent_status_request")
    data = request.POST 
    process_consent_status.apply_async(data=data, countdown=3)
    json_response = {"error": "", "trackId": 7843, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)



@csrf_exempt
@require_http_methods(["POST"])
def generate_offer_response(request):
    print("called:generate_offer_response")
    data = to_json(request.body) 
    print(data)
    return JsonResponse(data)
