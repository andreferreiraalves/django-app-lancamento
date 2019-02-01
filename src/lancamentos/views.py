from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView
from .models import Categoria, Lancamento


class CategoriaList(ListView):
    model = Categoria


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['descricao']           
    success_url = reverse_lazy('categoria_form')


class CategoriaDelete(DeleteView)    :
    model = Categoria
    success_url = reverse_lazy('categoria_list')


class LancamentoList(ListView):
    model = Lancamento


class LancamentoCreate(CreateView):
    model = Lancamento
    fields = ['descricao', 'valor', 'data', 'categoria']
    success_url = reverse_lazy('lancamento_form')


class LancamentoDelete(DeleteView):
    model = Lancamento
    success_url = reverse_lazy('lancamento_list')
