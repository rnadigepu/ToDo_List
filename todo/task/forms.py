from django import forms
from django.forms import ModelForm
from .models import task_list

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new Task...' }))
    class Meta:
        model = task_list
        fields = '__all__'


