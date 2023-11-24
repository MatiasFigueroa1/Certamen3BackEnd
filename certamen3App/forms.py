from django import forms
from certamen3App.models import Auto
from certamen3App.models import Marca

class FormAuto(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
    
    '''
    images = MultiFileField()

    def save(self, commit=True):
        instance = super(ArticleForm, self).save(commit)
        for each in self.cleaned_data['images']:
            Image.objects.create(image=each, article=instance)
        return instance
    '''

class FormMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'