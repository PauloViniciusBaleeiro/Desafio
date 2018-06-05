from django.db import models


class Pessoa(models.Model):
    SEXO = (('M', 'Masculino'),
            ('F', 'FEMININO'),
            )

    nome_pessoa = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
#    nascimento = models.DateField(blank=True, null=True)
    idade = models.IntegerField()
#   endereço = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
#   sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)

    def __str__(self):
        return self.nome_pessoa
