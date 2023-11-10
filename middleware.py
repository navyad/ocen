import json

from django.http import JsonResponse


class CheckRequiredAttributesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            post_data = json.loads(request.body.decode('utf-8'))
            product_data = post_data.get("productData")
            product_id = product_data.get("productId")
            product_network_id = product_data.get("productNetworkId")

            if not product_id or not product_network_id:
                response_data = {'error': 'productId and productNetworkId are required'}
                print(response_data)
                return JsonResponse(response_data, status=400)
            
            from ocen.utils import Constants
            if product_id != Constants.PRODUCT_ID or product_network_id != Constants.PRODUCT_NETWORK_ID:
                error_message = 'Invalid values for productId or productNetworkId.'
                print(error_message)
                return JsonResponse({'error': error_message}, status=400)
            
            request_id = post_data.get("metadata").get("requestId")
            if not request_id:
                error_message = {'error': "requestId is required"}
                print(error_message)
                return JsonResponse(error_message, status=400)


        response = self.get_response(request)
        return response

