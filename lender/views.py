
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from ocen.utils import to_json
from lender.tasks import (
    process_loan_application, process_consent_handle,
    process_generate_offer, process_document_request,
    process_set_offer_request,
)


@csrf_exempt
@require_http_methods(["POST"])
def create_loan_application(request):
    """
    Lender handling loan request
    """
    data = request.POST 
    print("called: create_loan_application")
    process_loan_application.apply_async(data=data, countdown=3)
    json_response = {"error": "", "trackId": 2343, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)


@csrf_exempt
@require_http_methods(["POST"])
def consent_handle_request(request):
    """
    Lender handling consent request 
    """
    data = request.POST 
    print("called: consent_handle_request")
    process_consent_handle.apply_async(data=data, countdown=3)
    json_response = {"error": "", "trackId": 7843, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)



@csrf_exempt
@require_http_methods(["POST"])
def consent_journey_notify(request):
    """
    Lender handling journey notify 
    """
    data = request.POST 
    print("called: consent_journey_notify")
    json_response = {"error": "", "trackId": 7843, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)


@csrf_exempt
@require_http_methods(["POST"])
def consent_status_response(request):
    """
    Invoked by loanagent in async manner 
    """
    print("called: consent_status_response")
    data = to_json(request.body)
    print(data)
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def generate_offer_request(request):
    """
    Lender handling generate offer request 
    """
    data = request.POST 
    print("called: generate_offer_request")
    process_generate_offer.apply_async(data=data, countdown=3)
    json_response = {"error": "", "trackId": 7843, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)


@csrf_exempt
@require_http_methods(["POST"])
def document_request(request):
    """
    Lender handling document_request 
    """
    data = request.POST
    print("called: document_request")
    process_document_request.apply_async(data=data, countdown=3)
    json_response = {"error": "", "trackId": 7843, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)


@csrf_exempt
@require_http_methods(["POST"])
def set_offer_request(request):
    """
    Lender handling set offer request 
    """
    data = request.POST
    print("called: set_offer_request")
    process_set_offer_request.apply_async(data=data, countdown=3)
    json_response = {"error": "", "trackId": 7843, "datetime": datetime.now()}
    print(f"response: {json_response}")
    return JsonResponse(json_response)

