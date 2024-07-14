from rest_framework import generics, mixins

from .models import Products
from .serializers import ProductsSerializer


# These Classbased Generics view
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer


# class ProductDetailsAPIView(generics.RetrieveAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     lookup_field = 'pk'

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if not instance.content:
    #         instance.content = instance.title


# class ProductDeleteAPIView(generics.DestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     lookup_field = 'pk'

#     def perform_destoy(self, instance):
#         super().perform_destroy()
#         if not instance.content:
#             instance.content = instance.title


# These are mixins and class based genericsAPIViews

class ProductMixinView(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_fields = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = "This is default title added by cool singleview in createView"
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.destroy(request, *args, **kwargs)

    def perform_destoy(self, instance):
        super().perform_destroy()
        if not instance.content:
            instance.content = instance.title
