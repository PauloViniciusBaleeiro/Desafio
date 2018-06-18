from django.shortcuts import render, get_object_or_404, redirect
from restaurantes.models import Restaurante
from django.contrib.auth.decorators import login_required
from .forms import RestForm

# Função para listar os restaurantes cadastrados
@login_required
def lista_restaurante(request):
    restaurantes = Restaurante.objects.all()

    return render(request, 'restaurantes.html', {'restaurantes': restaurantes})


@login_required
def atualiza_restaurante(request, id):
    restaurante = get_object_or_404(Restaurante, pk=id)
    form = RestForm(request.POST or None, instance=restaurante)

    if form.is_valid():
        form.save()
        return redirect('lista_restaurantes')
    return render(request, 'rest_form.html', {'form': form, 'rest': restaurante})
