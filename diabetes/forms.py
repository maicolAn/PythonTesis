from django import forms

from .models import Diabetes

class DiabetesForm(forms.ModelForm):
    """Formulario de diabetes"""

    class Meta:
        model = Diabetes
        fields = (
            'user',
            'glucosa_plasmatica',
            'presion_arterial',
            'espesor_piel',
            'insulina',
            'imc',
            'pedigri_diabetes',
            'edad',
            
             )

        widgets = {
            'glucosa_plasmatica': forms.NumberInput(
                attrs={
                    'placeholder': 'Glucosa plasmatica ',
                }
            ),
            'presion_arterial': forms.NumberInput(
                attrs={
                    'placeholder': 'Presion arterial ',
                }
            ),
            'espesor_piel': forms.NumberInput(
                attrs={
                    'placeholder': 'Gruesor de la piel ',
                }
            ),
            'insulina': forms.NumberInput(
                attrs={
                    'placeholder': 'Insulina ',
                }
            ),
            'imc': forms.NumberInput(
                attrs={
                    'placeholder': 'Indice de masa muscular ',
                }
            ),
            'pedigri_diabetes': forms.NumberInput(
                attrs={
                    'placeholder': 'Pedigri de diabetes',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'placeholder': 'Edad',
                }
            ),
        }

