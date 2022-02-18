from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from ponto_turisticos.models import PontoTuristico

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    ponto_tur = models.ForeignKey(PontoTuristico, on_delete=models.DO_NOTHING, null=True, blank=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.usuario.username
