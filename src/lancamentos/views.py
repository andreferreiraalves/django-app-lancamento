from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Categoria, Lancamento


class CategoriaList(ListView):
    model = Categoria


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['descricao']           
    success_url = reverse_lazy('categoria_list')


class LancamentoList(ListView):
    model = Lancamento


class LancamentoCreate(CreateView):
    model = Lancamento
    fields = ['descricao', 'valor', 'data', 'categoria']
    success_url = reverse_lazy('admin')