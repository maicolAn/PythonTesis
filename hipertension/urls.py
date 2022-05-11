from django.urls import path, include

from . import views
from .api import HipertensionAPI

urlpatterns = [
    path('modelo/', views.modelo, name='Modelo'),
    path('buscar/',views.buscar, name="Buscar"),
    path('api/create_hipe/', HipertensionAPI.as_view(), name = "api_create_hipe"),
]