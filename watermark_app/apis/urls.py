from django.urls import path
from .views import create, get

urlpatterns = [
    path('create/',create.CreateWatermark),
    path('get/',get.GetWatermark),
]