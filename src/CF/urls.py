"""CF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from lancamentos.views import CategoriaCreate, LancamentoCreate, CategoriaList, LancamentoList

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    
    path('categoria/create', CategoriaCreate.as_view(), name='categoria_form'),
    path('categoria/', CategoriaList.as_view(), name='categoria_list'),

    path('lancamento/', LancamentoList.as_view(), name='lancamento_list'),
    path('lancamento/create', LancamentoCreate.as_view(), name='lancamento_form'),
]
