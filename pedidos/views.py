from django.shortcuts import render
from clientes.models import Pessoa
from .models import Pedido

def localiza_pedidos(request, id):
    lista = Pedido.objetcs.filter()
