from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacao = models.TextField(null=True, blank=True)
    nota = models.DecimalField(decimal_places=2, max_digits=4)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.usuario.first_name if self.usuario.first_name != '' else self.usuario.username
