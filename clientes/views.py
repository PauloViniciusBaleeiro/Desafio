from django.shortcuts import render
from clientes.models import Pessoa
from pedidos.models import Pedido
from django.http import HttpResponse


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})


def pessoas_dia(request, dia):
    lista = Pedido.objects.filter(data=dia)
    return HttpResponse


def pessoas_dia2(request, year, month, day):
    pesqu_data = str(year)+'-'+str(month)+'-'+str(day)
    listas = Pedido.objects.filter(data=pesqu_data)
    return HttpResponse("neste dia, foram atendidas " + str(len(listas)) + " pessoas!")


def pessoas_mes(request, month):
    lista = Pedido.objects.filter(data__month=month)
    return HttpResponse("Neste mês, foram atendidas "+str(len(lista))+' pessoas!')


def pessoas_ano(request, year):
    lista = Pedido.objects.filter(data__year=year)
    return HttpResponse('Em '+str(year)+' houve '+str(len(lista))+' pessoas atendidas')
