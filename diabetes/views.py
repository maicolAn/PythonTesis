
import diabetes
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy, reverse
from joblib import load
import numpy as np



# importar los VIEW
from django.views.generic import (
    ListView
)

from .forms import DiabetesForm


from django.views.generic.edit import (
    View,
    FormView
)

# importamos modelos
from .models import Diabetes
from django.contrib.auth.models import User

def ListDiabetes(request):
    
    return render(request, "diabetes/list_diabetes.html")
    #success_url = reverse_lazy('home_app:inicio')

def PresionArterial(request):
    glucosap = request.POST ['glucosa-plasmatica']
   
    return render(request, "diabetes/presion.html", {'glucosa':glucosap})
    
def Espesorpiel(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    return render(request, "diabetes/espesor.html", {'glucosa':glucosap, 'presion':presionp})
    
def Insulina(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    espesorp = request.POST ['espesor-piel']
    return render(request, "diabetes/insulina.html", {'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp})
    
def Imc(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    espesorp = request.POST ['espesor-piel']
    insulinap= request.POST ['insulina']
    return render(request, "diabetes/imc.html", {'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap})
    
def pedigree1(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    espesorp = request.POST ['espesor-piel']
    insulinap= request.POST ['insulina']
    imcp= request.POST ['imc']

    return render(request, "diabetes/pedigree1.html", {'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap, 'imc':imcp})
    
def pedigree2(request):
    if (request.POST ["select"]):
        glucosap = request.POST ['glucosa-plasmatica']
        presionp = request.POST ['presion-arterial']
        espesorp = request.POST ['espesor-piel']
        insulinap= request.POST ['insulina']
        imcp= request.POST ['imc']
        diabetes_familia=request.POST ['select']
        num_familia=request.POST ['familia']
        diabetes_familia=int(diabetes_familia)
        num_familia1=int(num_familia)
        num_familia = range(0,num_familia1)
        if (diabetes_familia == 1):
            return render(request, "diabetes/pedigree2.html", {'familia':num_familia1, 'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap, 'imc':imcp})

        elif (diabetes_familia == 2):
            return render(request, "diabetes/pedigree4.html", {"familia":num_familia, "familiano":num_familia, 'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap, 'imc':imcp})

    
def pedigree3(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    espesorp = request.POST ['espesor-piel']
    insulinap= request.POST ['insulina']
    imcp= request.POST ['imc']
    num_familia=request.POST ['familia']
    num_familia_dia=request.POST ['diabeticos']
    num_familia1=int(num_familia)
    num_familia_dia1=int(num_familia_dia)
    res=num_familia1-num_familia_dia1
    num_familia_dia = range(0,num_familia_dia1)
    return render(request, "diabetes/pedigree3.html", {"familiadia":num_familia_dia, "familiano":res, "familiadia2":num_familia_dia1, 'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap, 'imc':imcp})
    
    
def pedigree4(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    espesorp = request.POST ['espesor-piel']
    insulinap= request.POST ['insulina']
    imcp= request.POST ['imc']
    edad_familiar=[]
    parentesco_familiar=[]
    num_familia=request.POST ['familiano']
    num_familia_dia=int(request.POST ['familiadia'])
    sumatoria=0

    for i in range(0, num_familia_dia):
        sa='select'+str(i)
        ss= 'edad-familiar'+str(i)
        edad_familiar.append(int(request.POST[ss]))
        parentesco_familiar.append(float(request.POST[sa]))
    
    for e in range(1,num_familia_dia+1):
        sumatoria= (parentesco_familiar[e-1]*(88-edad_familiar[e-1])) + sumatoria

    numerador= sumatoria + 20
    num_familia=int(num_familia)
    num_familia1 = range(0,num_familia)
    return render(request,"diabetes/pedigree4.html", {"familia":num_familia1, "numerador":numerador, "familiano":num_familia, 'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap, 'imc':imcp})
    
def pedigree5(FormView):
    template_name = 'diabetes/pedigree5.html'
    form_class = DiabetesForm
    
def edad(request):
    glucosap = request.POST ['glucosa-plasmatica']
    presionp = request.POST ['presion-arterial']
    espesorp = request.POST ['espesor-piel']
    insulinap= request.POST ['insulina']
    imcp= request.POST ['imc']
    edad_familiar=[]
    parentesco_familiar=[]
    num_familia=int(request.POST ['familiano'])
    numerador = float(request.POST ['numerador'])
    sumatoria=0
    for i in range(0, num_familia):
        sa='select'+str(i)
        ss= 'edad-familiar'+str(i)
        edad_familiar.append(int(request.POST [ss]))
        parentesco_familiar.append(float(request.POST[sa]))

    for e in range(1,num_familia+1):
        sumatoria= (parentesco_familiar[e-1]*(edad_familiar[e-1]-14)) + sumatoria
    
    denominador= sumatoria + 50
    dpf=numerador/denominador
    
    return render(request, "diabetes/edad.html",{'glucosa':glucosap, 'presion':presionp, 'espesor':espesorp, 'insulina':insulinap, 'imc':imcp, 'pedigree':dpf})


def resultado(request):

    if (request.POST ["glucosa-plasmatica"] and request.POST ['presion-arterial'] and request.POST ['espesor-piel'] and request.POST ['insulina'] and request.POST ["imc"]):
        glucosap = request.POST ['glucosa-plasmatica']
        presionp = request.POST ['presion-arterial']
        espesorp = request.POST ['espesor-piel']
        insulinap = request.POST ['insulina']
        imcp = request.POST ['imc']
        pedigrep = request.POST ['pedigree']
        edadp = request.POST ['edad']
        #usuariop=User.objects.get(email=request.user)
        usuariop=User.objects.get(username=request.user)
        datos=Diabetes(user=usuariop, glucosa_plasmatica=glucosap, presion_arterial=presionp,espesor_piel=espesorp, insulina=insulinap, imc=imcp, pedigri_diabetes=pedigrep, edad=edadp)
        datos.save()
    
        glucosap = int(glucosap)
        presionp = int(presionp)
        espesorp = int(espesorp)
        insulinap = int(insulinap)
        imcp = float(imcp)
        pedigrep = float(pedigrep)
        edadp = int(edadp)
        modelo= load("usuarios/static/ProyectoTesisApp/modelo/entreno_diabetes.pkl")
        pca= load("usuarios/static/ProyectoTesisApp/modelo/pca_diabetes.pkl")
        X=np.array([[0, glucosap, presionp, espesorp, insulinap,imcp, pedigrep, edadp ]])
        X_pca=pca.transform(X)
        y = modelo.predict(X_pca)
        if (y == 0):
            Resultado="No diabetico"
        elif(y==1):
            Resultado="Diabetico"

        consulta=Diabetes.objects.filter(user=usuariop).order_by("-id")

    else:
        Resultado="Error, llena todas las lineas"
        datos=0
        usuariop=User.objects.get(username=request.user)
        consulta=Diabetes.objects.filter(user=usuariop).order_by("-id")


    return render(request, "diabetes/resultado_diabetes.html", {"resultados":Resultado, "datos":datos, "consultas":consulta})
    
    

