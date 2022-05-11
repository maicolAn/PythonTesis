from rest_framework.response import Response
from .serializers import DiabetesSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from joblib import load
import numpy as np

class DiabetesAPI(APIView):

    
    def post(self,request):
        serializer = DiabetesSerializer(data = request.data)
        if serializer.is_valid():
            diabetes = serializer.save()

            glucosap = diabetes.glucosa_plasmatica
            presionp = diabetes.presion_arterial
            espesorp = diabetes.espesor_piel
            insulinap = diabetes.insulina
            imcp = diabetes.imc
            pedigrep = diabetes.pedigri_diabetes
            edadp = diabetes.edad
            glucosap = int(glucosap)
            presionp = int(presionp)
            espesorp = int(espesorp)
            insulinap = int(insulinap)
            imcp = float(imcp)
            pedigrep = float(pedigrep)
            edadp = int(edadp)
            modelo= load("diabetes/modelo/entreno_diabetes.pkl")
            pca= load("diabetes/modelo/pca_diabetes.pkl")
            X=np.array([[0, glucosap, presionp, espesorp, insulinap,imcp, pedigrep, edadp ]])
            X_pca=pca.transform(X)
            y = modelo.predict(X_pca)
            if (y == 0):
                Resultado="No diabetico"
            elif(y==1):
                Resultado="Diabetico"
            
            diabetes.resultado=Resultado
            
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)