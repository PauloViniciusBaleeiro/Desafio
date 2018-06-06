from django.shortcuts import render
from clientes.models import Pessoa

def lista_Pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'person.html', {'pessoas': pessoas})

