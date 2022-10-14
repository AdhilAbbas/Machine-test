from dataclasses import fields
from pyexpat import model
from django import forms
from django import forms
from .models import Upload

class ImageForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('picture')
        