from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    search  = request.GET.get('search')

    if search:
    # filtra de acordo com a pesquisa do usuário com a variável search
        cars = cars.filter(model__contains=search)

    return render(
        request, 
        'cars.html', 
        {'cars': cars }
    )

