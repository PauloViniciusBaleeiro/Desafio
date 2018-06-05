from django.db import models


class Produto(models.Model):
    nome_produto = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_produto
