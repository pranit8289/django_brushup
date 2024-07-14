# from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.models import Products
from products.serializers import ProcustSerializer

# @api_view(["GET"])
# def apihome(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     model_data = Products.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = ProcustSerializer(model_data).data
#     return Response(data)


@api_view(["POST"])
def apihome(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProcustSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(f"[INFO] instance - {instance}")
        return Response(serializer.data)
    else:
        return Response({"status_code": 400, "message": "BAD DATA"})