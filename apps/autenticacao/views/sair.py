from django.shortcuts import redirect
from django.contrib import auth


# sair.index
def index(request):
    auth.logout(request)
    return redirect('/auth/logar')
