from django.db import models

class Pessoas(models.Model):
    SEXO = (('M', 'Masculino'),
            ('F', 'FEMININO'),
            )

    nome_pessoa = models.CharField(max_length=100)
    altura = models.DecimalField(max_digits=1, decimal_places=2)
#    nascimento = models.DateField(blank=True, null=True)
    idade = models.IntegerField(max_length=3)
#   endereço = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
#   sexo = models.CharField(max_length=1, choices=SEXO, blank=True, null=True)

    def __str__(self):
        return self.nome_pessoa


class Restaurante(models.Model):
    nome_restaurante = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_restaurante


class Produto(models.Model):
    nome_produto = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_produto


'''class Produto_Restaurante(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT())
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=3, decimal_places=2)'''

