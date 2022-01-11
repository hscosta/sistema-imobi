from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


# cadastro.index
def index(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'autenticacao/cadastro.html')

    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']

        if len(username.strip()) == 0 or \
                len(email.strip()) == 0 or \
                len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                 'Preencha todos os campos para cadastrar!')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR,
                                 'Já existe um usuário com este username!')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            user.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso!')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR,
                                 'Erro interno do sistema!')
            return redirect('/auth/cadastro')
