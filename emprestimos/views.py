from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Emprestimo
from .forms import EmprestimoForm

@login_required
def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    return render(request, 'emprestimos/listar_emprestimos.html', {'emprestimos': emprestimos})

@login_required
def detalhar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id, usuario=request.user)
    return render(request, 'emprestimos/detalhar_emprestimo.html', {'emprestimo': emprestimo})

@login_required
def novo_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.usuario = request.user
            emprestimo.data_devolucao = timezone.now().date() + timedelta(days=14)
            emprestimo.save()

            # Atualiza disponibilidade do livro
            emprestimo.livro.disponivel = False
            emprestimo.livro.save()

            return redirect('emprestimos:listar_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimos/novo_emprestimo.html', {'form': form})

@login_required
def devolver_livro(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id, usuario=request.user)
    if request.method == 'POST':
        emprestimo.data_devolucao_real = timezone.now().date()
        emprestimo.status = 'DEVOLVIDO'
        emprestimo.save()

        emprestimo.livro.disponivel = True
        emprestimo.livro.save()

        return redirect('emprestimos:listar_emprestimos')
    return render(request, 'emprestimos/devolver_livro.html', {'emprestimo': emprestimo})
