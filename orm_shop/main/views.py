from django.shortcuts import render, get_object_or_404
from .models import Car, Sale

def cars_list_view(request):
    cars = Car.objects.all().order_by('-year')
    return render(request, 'main/list.html', {'cars': cars})

def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'main/details.html', {'car': car})

def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    sales = Sale.objects.filter(car=car).select_related('client')
    return render(request, 'main/sales.html', {'car': car, 'sales': sales})