from django.db import models
from clientes.models import Pessoa
from restaurantes.models import Restaurante
from produtos.models import Produto


class Pedido(models.Model):
    pessoas = models.ForeignKey(Pessoa, verbose_name="Lista de clientes cadastrados", on_delete=models.PROTECT)
    produtos = models.ForeignKey(Produto, verbose_name="Lista de Produtos", default=None, on_delete=models.PROTECT)
    data = models.DateField()

    def __str__(self):
        return str(self.pk + 1)

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "pedidos"
