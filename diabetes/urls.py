from django.urls import path
from django.conf.urls import  url
from . import views
from .api import DiabetesAPI


urlpatterns = [
    path('listar-diabetes/',views.ListDiabetes,name='diabetes'),
    path('presionarterial/',views.PresionArterial, name="presion"),
    path('espesorpiel/',views.Espesorpiel, name="espesor"),
    path('insulina/',views.Insulina, name="insulina"),
    path('imc/',views.Imc, name="imc"),
    path('pedigree1/',views.pedigree1, name="pedigre1"),
    path('pedigree2/',views.pedigree2, name="pedigree2"),
    path('pedigree3/',views.pedigree3, name="pedigre3"),
    path('pedigree4/',views.pedigree4, name="pedigre4"),
    path('pedigree5/',views.pedigree5, name="pedigree5"),
    path('edad/',views.edad, name="edad"),
    path('resultado/',views.resultado, name="Resultado"),
    path('api/create_diabe/', DiabetesAPI.as_view(), name = "api_create_diabe"),
]