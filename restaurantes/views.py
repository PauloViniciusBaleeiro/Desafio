from django.shortcuts import render
from restaurantes.models import Restaurante
from django.contrib.auth.decorators import login_required


@login_required
def lista_restaurante(request):
    restaurantes = Restaurante.objects.all()

    return render(request, 'restaurantes.html', {'restaurantes': restaurantes})
