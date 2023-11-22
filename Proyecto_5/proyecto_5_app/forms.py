from django import forms 
from . import models

class FormProyecto(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields ='__all__'