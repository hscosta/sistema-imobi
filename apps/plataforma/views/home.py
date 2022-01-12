from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.plataforma.models import Imovel


# home.index
@login_required(login_url='/auth/logar')
def index(request):
    imoveis = Imovel.objects.all()
    context = {
        'imoveis': imoveis,
    }

    return render(request, 'plataforma/home.html', context)
