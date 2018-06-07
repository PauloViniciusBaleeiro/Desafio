from django.shortcuts import render
from clientes.models import Pessoa
from pedidos.models import Pedido
from django.http import HttpResponse


def lista_Pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})


def pessoasDia(request, year, month, day):
    pesqu_data = str(year)+'-'+str(month)+'-'+str(day)
    listas = Pedido.objects.filter(data=pesqu_data)
    return HttpResponse("neste dia, foram atendidas " + str(len(listas)) + " pessoas!")


def pessoasMes(request, month):
    lista = Pedido.objects.filter(data__month=month)
    return HttpResponse("Neste mês, foram atendidas "+str(len(lista))+' pessoas!')


def pessoasAno(request, year):
    lista = Pedido.objects.filter(data__year=year)
    return HttpResponse('Em '+str(year)+' houve '+str(len(lista))+' pessoas atendidas')
