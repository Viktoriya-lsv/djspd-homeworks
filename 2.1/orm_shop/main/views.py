from django.http import Http404
from django.shortcuts import render

from .models import Car, Client, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    return render(request, 'main/list.html', {
        'cars': cars,
    })  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        car = Car.objects.get(id=car_id)
        template_name = 'main/details.html'
        return render(request, template_name, {'car': car})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404('Car not found')
    
    sales = Sale.objects.filter(car=car)
    template_name = 'main/sales.html'
    return render(request, template_name, {
        'sales': sales,
    })