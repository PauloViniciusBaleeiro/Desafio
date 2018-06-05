from django.db import models


class Restaurante(models.Model):
    nome_restaurante = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_restaurante
