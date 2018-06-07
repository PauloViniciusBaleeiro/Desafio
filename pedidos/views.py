from django.shortcuts import render, get_object_or_404
from clientes.models import Pessoa
from .models import Pedido
from django.http import HttpResponse


def localiza_pedidos(request, id):
    pessoa = Pessoa.objects.get(pk=id)

    if pessoa is not None:

        #pedidos = Pedido.objects.get(pessoas=id)
        lista=[]
        pedidos = Pedido.objects.filter(pessoas=id)
        for pedido in pedidos:
            lista.append(pedido)
        #pedidos = Pedido.objects.all()
        #return HttpResponse(pessoa.nome_pessoa + " possui " + str(len(pedidos)) + " pedidos registrados")
        return render(request, 'pedidos.html', {'lista': lista})
        '''for p in pedidos:
            return HttpResponse (p.numero)'''

    '''else:

        return HttpResponse("Id informado inválido, tente novamente")'''
