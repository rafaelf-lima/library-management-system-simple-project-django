from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# Create your views here.
def login_view(request):
    pass

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


