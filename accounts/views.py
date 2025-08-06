from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, AuthenticationForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('obter_livros')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/login.html', {'form': form})
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


