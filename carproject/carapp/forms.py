from django import forms
from carapp.models import Car
app_name = 'carapp'

class Carform(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name','desc','year','img']