from django import forms
from certamen3App.models import Auto
from certamen3App.models import Marca

class FormAuto(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'

class FormMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'