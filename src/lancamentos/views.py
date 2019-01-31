from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Categoria, Lancamentos

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['descricao']
    success_url = reverse_lazy('admin')

class LancamentoCreate(CreateView):
    model = Lancamentos
    fields = ['descricao', 'valor', 'categoria']
    success_url = reverse_lazy('admin')