from django.forms import ModelForm
from .models import Restaurante


class RestForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nome_restaurante', 'endereco']