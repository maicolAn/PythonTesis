from django.db import models
from django.conf import settings

# Create your models here.
class Diabetes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    glucosa_plasmatica = models.IntegerField('Glucosa plasmatica')
    presion_arterial = models.IntegerField('Presion Arterial')
    espesor_piel = models.DecimalField('Espesor de la piel', max_digits=5, decimal_places=2)
    insulina = models.DecimalField('insulina', max_digits=5, decimal_places=2)
    imc = models.DecimalField('Indice masa muscular', max_digits=5, decimal_places=2)
    pedigri_diabetes = models.DecimalField('Pedigri diabetes', max_digits=5, decimal_places=2)
    edad = models.IntegerField('Edad')

    def __str__(self):
        return self.glucosa_plasmatica