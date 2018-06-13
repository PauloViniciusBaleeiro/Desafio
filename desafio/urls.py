"""desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from clientes.views import (lista_pessoas, pessoas_dia, pessoas_ano, pessoas_mes)
from pedidos.views import (localiza_pedidos, pedidos_restaurantes, receitas, mktshare_qtd, mktshr_vlr, lista_pedidos)
from restaurantes.views import lista_restaurante
from home import urls as home_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(home_urls)),
    path('login/', auth_views.login, name='login'),
    path('admin/', admin.site.urls),
    path('lista/', lista_pessoas, name='lista_pessoas'),
    path('pdia/<str:dia>', pessoas_dia, name='pedidos_dia'),
    path('pmes/<int:month>', pessoas_mes),
    path('pano/<int:year>', pessoas_ano),
    path('ped_pessoas/<int:id>', localiza_pedidos, name='ped_pessoas'),
    path('ped_rest/<int:id>', pedidos_restaurantes, name='ped_rest'),
    path('rest/', lista_restaurante, name='lista_restaurantes'),
    path('receitas/<int:id>', receitas),
    path('mktshrqtd/', mktshare_qtd, name="mktshrqtd"),
    path('mktshrvlr/', mktshr_vlr, name='mktshrvlr'),
    path('listaped/', lista_pedidos, name='listapedidos'),
]
