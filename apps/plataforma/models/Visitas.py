from apps.plataforma.models import *


class Visitas(models.Model):
    choices_visitas_status = (
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado'),
    )

    choices_visitas_status = (
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado'),
    )

    imovel = models.ForeignKey(
        Imovel, on_delete=models.DO_NOTHING,
    )
    usuario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING,
    )
    dia = models.CharField(
        max_length=30,
    )
    horario = models.TimeField()
    status = models.CharField(
        max_length=1, choices=choices_visitas_status,
    )

    def __str__(self) -> str:
        return self.usuario.username
