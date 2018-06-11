from django.shortcuts import render, get_object_or_404
from clientes.models import Pessoa
from .models import Pedido
from restaurantes.models import Restaurante


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


def pedidos_restaurantes(request, id):
    try:
        restaurante = Restaurante.objects.get(id=id)

    except:
        pass

    if restaurante:

        lista=[]
        pedidos = Pedido.objects.filter(produtos__restaurante=id)

        for pedido in pedidos:
            lista.append(pedido)

        return render(request, 'ped_rest.html', {'lista' : lista, 'restaurante' : restaurante})

    else:

        return render(request, 'ped_rest.html', {'lista' : None, 'restaurante': "Nenhum restaurante encontrado, "
                                                                                 "tente novamente"})

def receitas(request, id):
    restaurante = Restaurante.objects.get(id=id)


    if restaurante is not None:

        lista = []
        pedidos = Pedido.objects.filter(produtos__restaurante=id)
        valor = 0

        for pedido in pedidos:
            valor += pedido.produtos.valor

        for pedido in pedidos:
            lista.append(pedido)

        return render(request, 'receitas.html', {'lista': lista, 'restaurante': restaurante, 'valor': valor})

    else:
        return render(request, 'receitas.html', {'lista': None, 'restaurante': 'Nenhum restaurante encontrado'})
