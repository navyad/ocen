import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

"""
This is a loan agent API handler
These API endpoints have been invoked from lender in async manner
"""


def to_json(byte_data):
    json_string = byte_data.decode('utf-8')
    return json.loads(json_string)
   

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

