from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from ponto_turisticos.models import PontoTuristico
from eventos.api.serializers import EventoSerializer
from localizacao.api.serializers import LocalizacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    eventos = EventoSerializer(many=True)
    endereco = LocalizacaoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'descricao_completa', 'aprovado'
        , 'endereco', 'eventos', 'foto')
    
    def get_descricao_completa(self, obj):
        return '%s - %s' %(obj.nome, obj.descricao)