from apps.plataforma.models import *


class DiasVisita(models.Model):
    dia = models.CharField(
        max_length=30,
    )

    def __str__(self) -> str:
        return self.dia
