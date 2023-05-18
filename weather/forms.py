from weather.models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class':'form-control', 'name':'city', 'id':'city', 'placeholder':'Введите город'})}
        # widget = {'name':TextInput(attrs={'type':"text", 'id':"city", 'name':"city", 'class':"form-control", 'placeholder':"Введите город"})}