from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.obter_livros, name='obter_livros'),
    path('detalhes/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('remover/<int:livro_id>/', views.remover_livro, name='remover_livro')
]
