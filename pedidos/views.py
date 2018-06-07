from django.shortcuts import render
from clientes.models import Pessoa
from .models import Pedido
from django.http import HttpResponse

def localiza_pedidos(request, id):
    lista = Pedido.objetcs.filter(pessoas=id)
    return HttpResponse()
