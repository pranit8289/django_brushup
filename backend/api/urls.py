from .views import apihome
from django.urls import path

urlpatterns = [
    path('', apihome),
]