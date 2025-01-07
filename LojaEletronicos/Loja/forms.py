from django import forms
from .models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria', 'marca', 'imagem']