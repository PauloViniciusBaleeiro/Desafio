from django.shortcuts import render
from restaurantes.models import Restaurante


def lista_restaurante(request):
    restaurantes = Restaurante.objects.all()

    return render(request, 'restaurantes.html', {'restaurantes': restaurantes})
