import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
@require_http_methods(["POST"])
def create_loan_application_response(request):
    print("called: create_loan_application_response")
    byte_data = request.body 
    json_string = byte_data.decode('utf-8')
    data = json.loads(json_string)
    print(data)
    return JsonResponse(data)

