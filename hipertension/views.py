from django.shortcuts import render
from .models import Hipertension
from django.contrib.auth.models import User
from joblib import load
import numpy as np

# Create your views here.
def modelo(request):
    return render(request, "hipertension/modelo.html")

def buscar(request):

    
    if (request.POST ["edad"] and request.POST ["presions"] and request.POST ["imc"] and request.POST [ "peso"]):
        
        usuariop=User.objects.get(username=request.user)
        
        presions=request.POST ['presions']
        genero=request.POST ['select']
        edad=request.POST ['edad']
        imc=request.POST ['imc']
        peso=request.POST ['peso']
        #usuario=User.objects.username()
        if(genero=="1"):
            sexo="Masculino"
        elif(genero=="2"):
            sexo="Femenino"

        modelo= load('hipertension/modelo/modelo_entrenado_hipertension.pkl')
        pca= load("hipertension/modelo/modelo_pca_hipertension.pkl")
        presionsp=int(presions)
        pesop=int(peso)
        edadp=int(edad)
        imcp=int(imc)
        
        #X=np.array([[-90.4469,	-14.529,	1.09817,	-1.40543,	-4.05994]])
        X=np.array([[edadp, pesop, presionsp ,imcp]])
        X_pca=pca.transform(X)
        y = modelo.predict(X_pca)
        if (y == 0):
            Resultado="Normal"
        elif(y==1):
            Resultado="Prehipertenso"
        elif(y==2):
            Resultado="Hipertension en estado 1"
        elif(y==3):
            Resultado="Hipertension en estado 2"
            

        datos=Hipertension(usuario=usuariop,presion_s=presions, edad=edad,  imc=imc, peso=pesop, resultado=Resultado)
        datos.save()
        consulta=Hipertension.objects.filter(usuario=usuariop).order_by("-id")
        #mensaje= "Tus datos : %r" %request.POST ["nombre"]
        #mensaje=usuario
        

    else:

        Resultado="Error, llena todas las lineas"
        datos=0
        sexo=0
        usuariop=User.objects.get(username=request.user)
        consulta=Hipertension.objects.filter(usuario=usuariop).order_by("-id")


    return render(request, "hipertension/resultado.html", {"resultados":Resultado, "datos":datos, "sexo":sexo, "consultas":consulta})