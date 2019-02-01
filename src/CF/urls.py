from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from lancamentos.views import (
    CategoriaList,
    CategoriaCreate,
    CategoriaDelete,

    LancamentoList, 
    LancamentoCreate, 
    LancamentoDelete)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('', login_required(LancamentoList.as_view()), name='index'),
    
    path('categoria/', login_required(CategoriaList.as_view()), name='categoria_list'),
    path('categoria/create/', login_required(CategoriaCreate.as_view()), name='categoria_form'),
    path('categoria/delete/<int:pk>/', login_required(CategoriaDelete.as_view()), name='categoria_delete'),

    path('lancamento/', login_required(LancamentoList.as_view()), name='lancamento_list'),
    path('lancamento/create/', login_required(LancamentoCreate.as_view()), name='lancamento_form'),
    path('lancamento/delete/<int:pk>/', login_required(LancamentoDelete.as_view()), name='lancamento_delete'),

    path('login/', LoginView.as_view(template_name="usuario-login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="usuario-login.html"), name='logout')
]
