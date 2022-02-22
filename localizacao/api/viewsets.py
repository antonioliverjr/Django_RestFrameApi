from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from localizacao.models  import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer