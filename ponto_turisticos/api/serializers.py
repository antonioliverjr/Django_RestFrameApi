from rest_framework.serializers import ModelSerializer
from ponto_turisticos.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto')