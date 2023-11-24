from django import forms
from certamen3App.models import Auto

class FormAuto(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'