from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from ponto_turisticos.models import PontoTuristico, Evento
from eventos.api.serializers import EventoSerializer
from localizacao.api.serializers import LocalizacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    eventos = EventoSerializer(many=True)
    endereco = LocalizacaoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'descricao_completa', 'endereco', 'eventos',
        'comentarios', 'avaliacoes', 'aprovado', 'foto')
        read_only_fields = ('comentarios', 'avaliacoes')

    def create_evento(self, eventos, ponto):
        for evento in eventos:
            ev = Evento.objects.create(**evento)
            ponto.eventos.add(ev)

    def create(self, validated_data):
        if not 'id' in validated_data['eventos']:
            eventos = validated_data['eventos']
            del validated_data['eventos']
            ponto = PontoTuristico.objects.create(**validated_data)
            self.create_evento(eventos, ponto)
            return ponto
        else:
            return super().create(validated_data)
    
    def get_descricao_completa(self, obj):
        return '%s - %s' %(obj.nome, obj.descricao)