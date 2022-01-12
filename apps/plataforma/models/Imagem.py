from apps.plataforma.models import *


class Imagem(models.Model):
    img = models.ImageField(
        upload_to='img',
    )

    def __str__(self) -> str:
        return self.img.url
