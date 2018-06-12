from django.shortcuts import render, get_object_or_404
from clientes.models import Pessoa
from .models import Pedido
from restaurantes.models import Restaurante
from django.db.models import Sum


def localiza_pedidos(request, id):
    try:
        pessoa = Pessoa.objects.get(pk=id)
    except:
        pass

    if pessoa:

        lista = []
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

        lista = []
        pedidos = Pedido.objects.filter(produtos__restaurante=id)

        for pedido in pedidos:
            lista.append(pedido)

        return render(request, 'ped_rest.html', {'lista': lista, 'restaurante': restaurante})

    else:

        return render(request, 'ped_rest.html', {'lista': None, 'restaurante': "Nenhum restaurante encontrado, "
                                                                               "tente novamente"})


def receitas(request, id):
    restaurante = Restaurante.objects.get(id=id)

    if restaurante:

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


def mktshare_qtd(request):
    restaurantes = Restaurante.objects.all()
    pedidos = Pedido.objects.count()

    pn = Pedido.objects.filter(produtos__restaurante=3).count()
    hb = Pedido.objects.filter(produtos__restaurante=4).count()
    pc = Pedido.objects.filter(produtos__restaurante=5).count()
    nm = Pedido.objects.filter(produtos__restaurante=6).count()

    if pedidos <= 0:
        pedidos = 1
        pn_per = (pn / pedidos) * 100
        hb_per = (hb / pedidos) * 100
        pc_per = (pc / pedidos) * 100
        nm_per = (nm / pedidos) * 100

    else:

        pn_per = (pn / pedidos) * 100
        hb_per = (hb / pedidos) * 100
        pc_per = (pc / pedidos) * 100
        nm_per = (nm / pedidos) * 100

    lista_perc = [pn_per, hb_per, pc_per, nm_per]
    lista_rest = []

    for r in restaurantes:
        lista_rest.append(r.nome_restaurante)

    return render(request, 'mktshr.html', {'lista_rest': lista_rest, 'pedidos': pedidos,
                                           'restaurantes': restaurantes, 'lista_perc': lista_perc,
                                           'lista_geral': zip(lista_rest, lista_perc)})


def mktshr_vlr(request):
    restaurantes = Restaurante.objects.all()
    pedidos = Pedido.objects.aggregate(total=Sum('produtos__valor'))
    soma_total = pedidos['total']

    pn = Pedido.objects.filter(produtos__restaurante=3).aggregate(soma=Sum('produtos__valor'))
    pn_soma = pn['soma']
    hb = Pedido.objects.filter(produtos__restaurante=4).aggregate(soma=Sum('produtos__valor'))
    hb_soma = hb['soma']
    pc = Pedido.objects.filter(produtos__restaurante=5).aggregate(soma=Sum('produtos__valor'))
    pc_soma = pc['soma']
    nm = Pedido.objects.filter(produtos__restaurante=6).aggregate(soma=Sum('produtos__valor'))
    nm_soma = nm['soma']

    lista_vlr = [pn_soma, hb_soma, pc_soma, nm_soma]

    pn_per = (pn_soma / soma_total) * 100
    hb_per = (hb_soma / soma_total) * 100
    pc_per = (pc_soma / soma_total) * 100
    nm_per = (nm_soma / soma_total) * 100

    lista_perc = [pn_per, hb_per, pc_per, nm_per]
    lista_rest = []

    for r in restaurantes:
        lista_rest.append(r.nome_restaurante)

    return render(request, 'mktshrvlr.html', {'lista_rest': lista_rest, 'valor': soma_total,
                                              'restaurantes': restaurantes, 'lista_perc': lista_perc,
                                              'lista_geral': zip(lista_rest, lista_perc, lista_vlr),
                                              'lista_valor': lista_vlr})
