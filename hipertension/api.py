from rest_framework.response import Response
from .serializers import HipertensionSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from joblib import load
import numpy as np

class HipertensionAPI(APIView):

    
    def post(self,request):
        serializer = HipertensionSerializer(data = request.data)
        if serializer.is_valid():
            hipertension = serializer.save()
            presionsp = hipertension.presion_s
            edadp = hipertension.edad
            pesop = hipertension.peso
            imcp = hipertension.imc
            presionsp=int(presionsp)
            edadp=int(edadp)
            pesop=int(pesop)
            imcp=int(imcp)
            modelo= load('hipertension/modelo/modelo_entrenado_hipertension.pkl')
            pca=load('hipertension/modelo/modelo_pca_hipertension.pkl')
            X=np.array([[ edadp, pesop, presionsp ,imcp]])
            X_pca=pca.transform(X)
            y = modelo.predict(X_pca)
            if (y == 0):
                Resultado="Normal"
            elif(y==1):
                Resultado="Prehipertenso"
            elif(y==2):
                Resultado="Hipertension estado 1"
            elif(y==3):
                Resultado="Hipertension estado 2"
            
            hipertension.resultado=Resultado
            hipertension.save()
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)