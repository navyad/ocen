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
                return JsonResponse(response_data, status=400)
            
            from ocen.utils import Constansts
            if product_id != Constansts.PRODUCT_ID or product_network_id != Constansts.PRODUCT_NETWORK_ID:
                error_message = 'Invalid values for productId or productNetworkId.'
                return JsonResponse({'error': error_message}, status=400)
            
            request_id = post_data.get("requestId")
            if not request_id:
                return JsonResponse({'error': "requestId is required"}, status=400)


        response = self.get_response(request)
        return response

