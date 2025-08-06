from django.urls import path
from . import views

urlpatterns = [
    path('obter/', views.obter_emprestimos, name='obter_emprestimos'),
    path('detalhes/<int:emprestimo_id>/', views.detalhes_emprestimo, name='detalhes_emprestimo'),
    path('adicionar/', views.adicionar_emprestimo, name='adicionar_emprestimo'),
    path('editar/<int:emprestimo_id>/', views.editar_emprestimo, name='editar_emprestimo'),
    path('remover/<int:emprestimo_id>/', views.remover_emprestimo, name='remover_emprestimo')
]