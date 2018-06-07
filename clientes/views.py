from django.shortcuts import render
from clientes.models import Pessoa
from pedidos.models import Pedido
from django.http import HttpResponse


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})


def pessoas_dia(request, dia):
    lista = Pedido.objects.filter(data=dia)
    return HttpResponse("Neste dia foram atendidos " + str(len(lista)) + " pessoas!")


def pessoas_mes(request, month):
    lista = Pedido.objects.filter(data__month=month)
    return HttpResponse("Neste mês, foram atendidas "+str(len(lista))+' pessoas!')


def pessoas_ano(request, year):
    lista = Pedido.objects.filter(data__year=year)
    return HttpResponse('Em '+str(year)+' houve '+str(len(lista))+' pessoas atendidas')
