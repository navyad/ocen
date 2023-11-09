
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from lender.tasks import (
    process_loan_application, process_consent_handle
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






