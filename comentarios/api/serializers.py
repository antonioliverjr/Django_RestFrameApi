from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
from ponto_turisticos.api.serializers import PontoTuristicoSerializer

class ComentarioSerializer(ModelSerializer):
    ponto_turistico = PontoTuristicoSerializer(read_only=True)
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado', 'ponto_turistico')