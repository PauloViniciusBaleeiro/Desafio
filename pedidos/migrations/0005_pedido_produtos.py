# Generated by Django 2.0.5 on 2018-06-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('pedidos', '0004_remove_pedido_produtos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(default=None, to='produtos.Produto', verbose_name='Lista de Produtos'),
        ),
    ]
