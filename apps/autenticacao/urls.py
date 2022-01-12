from django.urls import path
from .views import cadastro, logar, sair


urlpatterns = [
    path(
        'cadastro/',
        cadastro.index,
        name='autenticacao-cadastro',
    ),
    path(
        'logar/',
        logar.index,
        name='autenticacao-logar',
    ),
    path(
        'sair/',
        sair.index,
        name='autenticacao-sair',
    ),
]
