from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from comentarios.models  import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer