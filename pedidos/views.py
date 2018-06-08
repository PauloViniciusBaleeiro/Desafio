from django.shortcuts import render, get_object_or_404
from clientes.models import Pessoa
from .models import Pedido
from django.http import HttpResponse


def localiza_pedidos(request, id):
    try:
        pessoa = Pessoa.objects.get(pk=id)
    except:
        pass

    if pessoa:


        lista=[]
        pedidos = Pedido.objects.filter(pessoas=id)
        for pedido in pedidos:
            lista.append(pedido)
        
        return render(request, 'pedidos.html', {'lista': lista, 'pessoa': pessoa})
    else:
        return render(request, 'pedidos.html', {'lista': None, 'pessoa': 'nenhuma pessoa encontrada'})


