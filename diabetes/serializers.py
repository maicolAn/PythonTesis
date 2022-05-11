from rest_framework import serializers, status
from django.contrib.auth.models import User
from .models import Diabetes


class DiabetesSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    resultado = serializers.ReadOnlyField()
    user = serializers.CharField()
    glucosa_plasmatica = serializers.CharField()
    presion_arterial = serializers.CharField()
    espesor_piel = serializers.CharField()
    insulina = serializers.CharField()
    imc = serializers.CharField()
    pedigri_diabetes = serializers.CharField()
    edad= serializers.CharField()
    

    def create(self, validate_data):
        instance = Diabetes()
        usuariop = validate_data.get('user')
        instance.user=User.objects.get(username=usuariop)
        instance.glucosa_plasmatica = validate_data.get('glucosa_plasmatica')
        instance.presion_arterial = validate_data.get('presion_arterial')
        instance.espesor_piel = validate_data.get('espesor_piel') 
        instance.insulina = validate_data.get('insulina')
        instance.imc = validate_data.get('imc')
        instance.pedigri_diabetes = validate_data.get('pedigri_diabetes')
        instance.edad = validate_data.get('edad')
        
        instance.save()
        return instance
