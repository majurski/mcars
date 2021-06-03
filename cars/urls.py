from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.HomeView, name='cars'),
    path('add/', views.AddNewCar, name='add'),
    path('add/success/', views.AddNewCarSuccess, name='success'),
    path('detail/<int:id>', views.CarDetailView, name='car_detail'),
]
