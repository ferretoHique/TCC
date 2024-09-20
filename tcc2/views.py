from django.shortcuts import render
from .models import Post

# Create your views here.
def tela_entrada(request):
    return render(request, 'telas/tela_entrada.html', {'dado': 'aiin'})


def tela_edicao(request):
    return render(request, 'telas/tela_edicao.html', {'dado': 'aiin'})
