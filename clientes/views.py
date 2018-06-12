from django.shortcuts import render
from clientes.models import Pessoa
from pedidos.models import Pedido
from django.http import HttpResponse

#Função para listagem de pessoas, recebendo uma request via html
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})


#Função para calcular quantas pessoas foram atendiadas em deterinado dia, passado via html
def pessoas_dia(request, dia):
    lista = Pedido.objects.filter(data=dia)
    return HttpResponse("Neste dia houve " + str(len(lista)) + " pedidos!")


def pessoas_mes(request, month):
    lista = Pedido.objects.filter(data__month=month)
    return HttpResponse("Neste mês houve "+str(len(lista))+' pedidos!')


def pessoas_ano(request, year):
    lista = Pedido.objects.filter(data__year=year)
    return HttpResponse('Em '+str(year)+' houve '+str(len(lista))+' pedidos')
