from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from common.variables import CARS_LIST, ENGINE_TYPES, COLOR_CHOICES
from datetime import datetime

class Car(models.Model):
    brand = models.CharField(max_length=20, choices=CARS_LIST)
    brand_model = models.CharField(max_length=20)
    condition = models.BooleanField(blank=True)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True)
    miliege = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return reverse('cars:car_detail', args=[self.id])

    class Meta:
        ordering = ('-added',)

def get_image_filename(instance, filename):
    id = instance.car.id
    title = instance.car.brand
    slug = slugify(title)
    return "img/%s/%s-%s" % (id, slug, filename)  


class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image_place = models.ImageField(upload_to=get_image_filename, verbose_name='Image')


