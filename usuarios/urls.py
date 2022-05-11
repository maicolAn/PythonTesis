from django.urls import path, include
from django.conf.urls import  url
from usuarios import views
from .api import UserAPI, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    url(r'^$', views.BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
    path('historial/',views.historial, name="Historial"),
    path('', include(router.urls)),
    path('api/create_user/', UserAPI.as_view(), name = "api_create_user"),
]