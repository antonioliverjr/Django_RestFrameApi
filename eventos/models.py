from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='evento', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
