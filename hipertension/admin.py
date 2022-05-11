from django.contrib import admin

# Register your models here.
from .models import Hipertension

@admin.register(Hipertension)
class HipertensionAdmin(admin.ModelAdmin):
    list_display = ('presion_s', 'edad', 'peso', 'imc')