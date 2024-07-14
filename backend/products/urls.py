from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailsAPIView.as_view()),
]