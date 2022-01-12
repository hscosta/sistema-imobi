from apps.plataforma.models import *


class Cidade(models.Model):
    nome = models.CharField(
        max_length=100,
    )

    def __str__(self) -> str:
        return self.nome
