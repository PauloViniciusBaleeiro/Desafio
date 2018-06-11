from django.db import models
import csv


class Pessoa(models.Model):
    SEXO = (('M', 'Masculino'),
            ('F', 'FEMININO'),
            )

    nome_pessoa = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    idade = models.IntegerField()
    cidade = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_pessoa

    class Meta:
        ordering = ['nome_pessoa']
