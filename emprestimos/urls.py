from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('', views.listar_emprestimos, name='listar_emprestimos'),
    path('novo/', views.novo_emprestimo, name='novo_emprestimo'),
    path('devolver/<int:id>/', views.devolver_livro, name='devolver_livro'),
    path('<int:id>/', views.detalhar_emprestimo, name='detalhar_emprestimo'),
]
