from apps.plataforma.models import *


class Horario(models.Model):
    horario = models.TimeField()

    def __str__(self) -> str:
        return str(self.horario)
