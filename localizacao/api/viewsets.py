from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from localizacao.models  import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer