from django import forms

from . import models

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = models.Organizacion
        fields = '__all__'

        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class TransitoForm(forms.ModelForm):
    class Meta:
        model = models.Transito
        fields = '__all__'