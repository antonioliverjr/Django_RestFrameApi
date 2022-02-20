from rest_framework.viewsets import ModelViewSet
from eventos.models  import Evento
from .serializers import EventoSerializer

class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer