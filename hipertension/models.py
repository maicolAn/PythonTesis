from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hipertension(models.Model):
    usuario= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    presion_s = models.DecimalField(max_digits=5, decimal_places=2)
    edad= models.IntegerField(null= True)
    peso= models.IntegerField(null= True)
    imc= models.DecimalField(max_digits=5, decimal_places=2, null= True)
    resultado = models.CharField(max_length=24, null = True)