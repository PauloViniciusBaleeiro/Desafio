from django.db import models
from produtos.models import Produto


class Restaurante(models.Model):
    nome_restaurante = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    produtos = models.ManyToManyField(Produto, verbose_name="lista de Produtos")
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome_restaurante

