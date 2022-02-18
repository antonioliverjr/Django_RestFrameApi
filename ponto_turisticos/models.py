from django.db import models
from eventos.models import Evento
from localizacao.models import Localizacao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    eventos = models.ManyToManyField(Evento)
    endereco = models.ForeignKey(Localizacao, on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return self.nome
