from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# home.index
@login_required(login_url='/auth/logar')
def index(request):
    return HttpResponse('Estamos na página Plataforma/Home')
