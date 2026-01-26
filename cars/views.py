from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    # consulta todos os campos e colunas da tabela Car
    cars = Car.objects.all()

    return render(
        request, 
        'cars.html', 
        {'cars': cars }
    )

