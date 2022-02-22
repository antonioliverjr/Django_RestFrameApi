from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao
from ponto_turisticos.api.serializers import PontoTuristicoSerializer

class AvaliacaoSerializer(ModelSerializer):
    ponto_turistico = PontoTuristicoSerializer(read_only=True)
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'avaliacao', 'nota', 'data', 'ponto_turistico')