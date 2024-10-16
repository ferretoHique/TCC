from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import speech_recognition as sr
from django.conf import settings
from django.http import JsonResponse
from pydub import AudioSegment


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
    if request.method == 'POST' and 'audio' in request.FILES:
        # Receber o arquivo de áudio enviado
        audio_file = request.FILES['audio']
        audio_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
        
        with open(audio_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        AudioSegment.from_file(audio_path).export(audio_path, format='wav')
        # Usar SpeechRecognition para converter o áudio em texto
        recognizer = sr.Recognizer()

        try:
            # Abrir o arquivo de áudio salvo
            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source)  # Lê o conteúdo do áudio
                # Converter o áudio em texto usando a Google Web Speech API
                text = recognizer.recognize_google(audio_data, language='pt-BR')  # Para português
                return JsonResponse({'message': 'Áudio transcrito com sucesso!', 'text': text})

        except sr.UnknownValueError:
            return JsonResponse({'error': 'Não foi possível entender o áudio.'}, status=400)
        except sr.RequestError as e:
            return JsonResponse({'error': f'Erro ao conectar ao serviço de reconhecimento: {e}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'Erro ao processar o áudio: {e}'}, status=500)

    return JsonResponse({'error': 'Nenhum arquivo de áudio foi enviado.'}, status=400)


@login_required
def tela_edicao(request):
    return render(request, 'telas/tela_edicao.html', {'dado': 'aiin'})
