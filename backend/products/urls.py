from . import views
from django.urls import path

# # This we have used it for Generics views
# urlpatterns = [
#     path('', views.ProductListCreateAPIView.as_view()),
#     path('<int:pk>/', views.ProductDetailsAPIView.as_view()),
#     path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
#     path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
# ]

# This we have used it for Mixins and Generics views.
urlpatterns = [
    path('', views.ProductMixinView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('<int:pk>/update/', views.ProductMixinView.as_view()),
    path('<int:pk>/delete/', views.ProductMixinView.as_view()),
]