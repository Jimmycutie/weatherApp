from django.urls import path
from .views import index
from .views import get_weather

urlpatterns = [
    path('', index, name='index'),
    path('api/weather', get_weather, name='get_weather'),
]
