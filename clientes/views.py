from django.shortcuts import render
from clientes.models import Pessoa
from pedidos.models import Pedido
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#Função para listagem de pessoas, recebendo uma request via html
@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})


#Função para calcular quantas pessoas foram atendiadas em deterinado dia, passado via html
@login_required
def pessoas_dia(request, dia):
    lista = Pedido.objects.filter(data=dia)
    return HttpResponse("Neste dia houve " + str(len(lista)) + " pedidos!")

#Função para que retorna a quantidade de pedidos filtrado por mês
@login_required
def pessoas_mes(request, month):
    lista = Pedido.objects.filter(data__month=month)
    return HttpResponse("Neste mês houve "+str(len(lista))+' pedidos!')

#Função que retorna a quantidade de pedidos filtrado por ano
@login_required
def pessoas_ano(request, year):
    lista = Pedido.objects.filter(data__year=year)
    return HttpResponse('Em '+str(year)+' houve '+str(len(lista))+' pedidos')
