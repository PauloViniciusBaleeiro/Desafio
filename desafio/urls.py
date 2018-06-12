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
from django.urls import path

from clientes.views import (lista_pessoas, pessoas_dia, pessoas_ano, pessoas_mes)
from pedidos.views import (localiza_pedidos, pedidos_restaurantes, receitas, mktshare_qtd, mktshr_vlr)
from restaurantes.views import lista_restaurante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista/', lista_pessoas),
    path('pdia/<str:dia>', pessoas_dia),
    path('pmes/<int:month>', pessoas_mes),
    path('pano/<int:year>', pessoas_ano),
    path('ped_pessoas/<int:id>', localiza_pedidos),
    path('ped_rest/<int:id>', pedidos_restaurantes),
    path('rest/', lista_restaurante),
    path('receitas/<int:id>', receitas),
    path('mktshrqtd/', mktshare_qtd),
    path('mktshrvlr/', mktshr_vlr),
]
