from django.db import models
from clientes.models import Pessoa
from restaurantes.models import Restaurante
from produtos.models import Produto

class Pedido(models.Model):
    numero = models.AutoField(primary_key=True )
    pessoas = models.ForeignKey(Pessoa, verbose_name="Lista de clientes cadastrados", on_delete=models.PROTECT)
    restaurantes = models.ForeignKey(Restaurante, verbose_name="Lista de restautantes cadastrados", on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, verbose_name="Lista de Produtos")
    data = models.DateField()

    def __str__(self):
        return self.numero
