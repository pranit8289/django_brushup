# from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.models import Products

# def apihome(request, *args, **kwargs):

#     # body = request.body
#     # data = {}
#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass

#     # data["params"] = dict(request.GET)
#     # data["content_type"] = request.content_type
#     # data["headers"] = dict(request.headers)
#     model_data = Products.objects.all().order_by("?").first()
#     data = {}
#     # if model_data:
#     #     data["id"] = model_data.id
#     #     data["title"] = model_data.title
#     #     data["content"] = model_data.content
#     #     data["price"] = model_data.price
#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title", "content", "price"])
#     return JsonResponse(data)
@api_view(["GET"])
def apihome(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Products.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "content", "price"])
    return Response(data)