from django import forms
from django.forms import ModelForm
from TASKLIST.models import *
class tasklistform(ModelForm):
    heading = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Что необходимо приобрести?'}))
    class Meta:
        model = tasklist
        fields = '__all__'
