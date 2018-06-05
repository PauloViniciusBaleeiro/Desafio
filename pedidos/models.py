from django.db import models
from clientes.models import Pessoa
from restaurantes.models import Restaurante
from produtos.models import Produto


class Pedido(models.Model):
    numero = models.AutoField(primary_key=True, unique=True, default=None)
    pessoas = models.ForeignKey(Pessoa, verbose_name="Lista de clientes cadastrados", on_delete=models.PROTECT)
    restaurantes = models.ForeignKey(Restaurante, verbose_name="Lista de restautantes cadastrados",
                                     on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, verbose_name="Lista de Produtos", default=None)
    data = models.DateField()

    def __str__(self):
        return str(self.numero)

    class Meta:
        ordering = ["numero"]
        verbose_name_plural = "pedidos"
