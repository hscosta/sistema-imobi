from django.db import models
from django.contrib.auth.models import User

# 1 Imagem
# 2 Cidade
# 3 DiasVisita
# 4 Horario
# 5 Imovel
# 6 Visitas
from .Imagem import Imagem
from .Cidade import Cidade
from .DiasVisita import DiasVisita
from .Horario import Horario
from .Imovel import Imovel
from .Visitas import Visitas


# choices = (
#     ('V', 'Venda'),
#     ('A', 'Aluguel')
# )

# choices_imovel = (
#     ('A', 'Apartamento'),
#     ('C', 'Casa')
# )

# choices_visitas = (
#     ('S', 'Segunda'),
#     ('T', 'Terça'),
#     ('Q', 'Quarta'),
#     ('QI', 'Quinta'),
#     ('SE', 'Sexta'),
#     ('SA', 'Sábado'),
#     ('D', 'Domingo'),
# )

# choices_visitas_status = (
#     ('A', 'Agendado'),
#     ('F', 'Finalizado'),
#     ('C', 'Cancelado'),
# )
