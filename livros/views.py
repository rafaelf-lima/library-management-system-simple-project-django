from django.shortcuts import redirect, render, get_object_or_404
from .models import Livro
from django.contrib.auth.decorators import login_required
from .forms import LivroForm

# Create your views here.
@login_required
def obter_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/obter_livros.html', {'livros': livros})

@login_required
def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'livros/detalhes_livro.html', {'livro': livro})

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros:obter_livros')
    else:
        form = LivroForm()    
    return render(request, 'livros/adicionar_livro.html', {'form': form})
        

@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livros:obter_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/editar_livro.html', {'form': form, 'livro': livro})


@login_required
def remover_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        livro.delete()
        return redirect('livros:obter_livros')
    return render(request, 'livros/remover_livro.html', {'livro': livro})


