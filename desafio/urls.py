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
from clientes.views import lista_Pessoas
from clientes.views import pessoasDia
from clientes.views import pessoasMes
from clientes.views import pessoasAno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista/', lista_Pessoas),
    path('pdias/<int:year>/<int:month>/<int:day>', pessoasDia),
    path('pmes/<int:month>', pessoasMes),
    path('pano/<int:year>', pessoasAno),
]
