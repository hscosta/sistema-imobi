from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.plataforma.models import Imovel, Cidade


# home.index
@login_required(login_url='/auth/logar')
def index(request):
    imoveis = Imovel.objects.all()
    cidades = Cidade.objects.all()

    context = {
        'imoveis': imoveis,
        'cidades': cidades,
    }

    return render(request, 'plataforma/home.html', context)
