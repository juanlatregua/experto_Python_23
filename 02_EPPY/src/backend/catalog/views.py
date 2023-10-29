from django.shortcuts import render
from catalog.models import Car

# Create your views here.

def car_index(request):
    cars = Car.objects.all()
    context = {
        'cars' : cars
    }

    return render(request, 'car_index.html', context)

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car' : car
    }

    return render(request, 'car_detail.html', context)
