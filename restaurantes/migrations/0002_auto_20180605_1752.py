# Generated by Django 2.0.5 on 2018-06-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='produtos',
            field=models.ManyToManyField(to='produtos.Produto', verbose_name='lista de Produtos'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
