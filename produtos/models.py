from django.db import models
from restaurantes.models import Restaurante


class Produto(models.Model):
    nome_produto = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)
    restaurante = models.ForeignKey(Restaurante, verbose_name="Lista de Restaurantes Cadastrados", on_delete=models.PROTECT, default=None)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome_produto


    class Meta:
        ordering = ['nome_produto']
