from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from avaliacoes.models  import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer