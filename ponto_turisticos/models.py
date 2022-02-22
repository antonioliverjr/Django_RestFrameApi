import imp
from django.db import models
from eventos.models import Evento
from localizacao.models import Localizacao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    eventos = models.ManyToManyField(Evento)
    endereco = models.ForeignKey(Localizacao, on_delete=models.DO_NOTHING, null=True, blank=True)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    foto = models.ImageField(upload_to='ponto_turisticos', null=True, blank=True)


    def __str__(self) -> str:
        return self.nome
