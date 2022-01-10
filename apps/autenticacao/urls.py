from django.urls import path
from .views import cadastro, logar


urlpatterns = [
    path(
        'cadastro/',
        cadastro.index,
        name='autenticacao-cadastro'
    ),
    path(
        'logar/',
        logar.index,
        name='autenticacao-logar'
    ),
]
