from django.contrib import admin
from django.urls import path
from .views import detalhar, listar, cadastrar, atualizar, deletar


urlpatterns = [
    path('', listar, name='listar'),
    path('<int:id>', detalhar, name='detalhar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('deletar/<int:id>', deletar, name='deletar')
]