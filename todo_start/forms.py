from dataclasses import field
from django import forms
from .models import Todo

class Listform(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["title","status"]