from django.shortcuts import get_object_or_404
from clientes.models import Pessoa
from .models import Pedido
from django.http import HttpResponse



def localiza_pedidos(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)

    if pessoa is not None:

        lista = Pedido.objects.filter(pessoas=id)

        return HttpResponse(pessoa.nome_pessoa + " possui " + str(len(lista)) + " pedidos registrados")

    else:

        return HttpResponse("Id informado inválido, tente novamente")
