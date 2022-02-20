from rest_framework.serializers import ModelSerializer
from eventos.models import Evento

class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade_minima')