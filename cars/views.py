from django.forms.fields import ImageField
from .models import Car, Image
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarAddForm, ImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


@login_required
def AddNewCar(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)

    if request.method == "POST":
        form = CarAddForm(data=request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if form.is_valid() and formset.is_valid():
            form.save()
            form = form.save(commit=False)
            for forms in formset.cleaned_data:
                if forms:
                    image = forms['image_place']
                    photo = Image(car=form, image_place=image)
                    photo.save()
            messages.success(request, 'Car added successfully')
            return redirect('success/')

    else:
        # build form with data provided by the bookmarklet via GET
        form = CarAddForm(request.GET)
        formset = ImageFormSet(queryset=Image.objects.none())

    return render(request, 'submit/add_car.html', {'form': form, 'formset': formset})


def AddNewCarSuccess(request):
    return render(request, 'submit/car_added.html')

def HomeView(request):
    cars = Car.objects.all()
    images = Image.objects.all()
    return render(request, 'home/home.html', {'cars': cars, 'images': images})

def CarDetailView(request, id):
    car = get_object_or_404(Car, id=id)
    images = Image.objects.filter(car_id=id)

    return render(request, 'home/detail.html', {'car': car, 'images': images})
