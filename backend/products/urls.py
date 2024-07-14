from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailsAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
]