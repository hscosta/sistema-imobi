from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'autenticacao/logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR,
                                 'Usuário ou senha inválidos!')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/')

        return HttpResponse(f'Username: {username} - senha: {senha}')
