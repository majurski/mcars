from cars import models
from django.contrib import admin
from .models import Car, Image

class ImageInline(admin.StackedInline):
    model = Image

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ['brand', 'brand_model', 'price', 'condition', 'color', 'miliege']
