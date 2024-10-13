from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar o usuário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Login do usuário
                return redirect('tela_entrada')  # Redirecionar após login
            else:
                return HttpResponse("Usuário ou senha inválidos")
        else:
            return HttpResponse("Formulário inválido")
    
    form = AuthenticationForm()
    return render(request, 'telas/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após logout


@login_required
# Create your views here.
def tela_entrada(request):
    return render(request, 'telas/tela_entrada.html', {'dado': 'aiin'})


@login_required
def audio_to_text(request):
    return render(request, 'ainnn')


@login_required
def tela_edicao(request):
    return render(request, 'telas/tela_edicao.html', {'dado': 'aiin'})
