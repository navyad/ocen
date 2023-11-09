from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from lender.tasks import create_loan_application_response 

@csrf_exempt
@require_http_methods(["POST"])
def create_loan_application(request):
    data = request.POST 
    print("called: create_loan_application")
    create_loan_application_response.apply_async(data=data, countdown=3)
    print("complete: create_loan_application")
    return JsonResponse({"error": "", "trackId": 2343})

