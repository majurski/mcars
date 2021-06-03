from django.db import models
from django.db.models import fields
from .models import Car, Image
from django import forms
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'brand_model', 'condition', 'price', 'color', 'miliege']

class ImageForm(forms.ModelForm): 
    class Meta:
        model = Image
        fields = ('image_place', )

    
    