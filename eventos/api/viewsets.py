from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from eventos.models  import Evento
from .serializers import EventoSerializer

class EventoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filterset_fields = ('nome', 'descricao')