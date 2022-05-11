from rest_framework import serializers, status
from django.contrib.auth.models import User
from .models import Hipertension


class HipertensionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    resultado = serializers.ReadOnlyField()
    usuario = serializers.CharField()
    presion_s = serializers.CharField()
    edad = serializers.CharField()
    peso = serializers.CharField()
    imc = serializers.CharField()
    

    def create(self, validate_data):
        instance = Hipertension()
        usuariop = validate_data.get('usuario')
        instance.usuario=User.objects.get(username=usuariop)
        instance.presion_s = validate_data.get('presion_s') 
        instance.edad = validate_data.get('edad')
        instance.peso = validate_data.get('peso')
        instance.imc = validate_data.get('imc')
        
        
        instance.save()
        return instance
