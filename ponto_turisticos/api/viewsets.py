from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication
from ponto_turisticos.models  import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao')

    def get_queryset(self):
        if self.request.query_params is not None:
            id = self.request.query_params.get('id', None)
            nome = self.request.query_params.get('nome', None)
            descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.filter(aprovado=True)

        if id:
            queryset = queryset.filter(id=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

#   Forma de substituir method GET
#    def list(self, request, *args, **kwargs):
#        return super().list(request, *args, **kwargs)

#   Forma de substituir method GET {atributo}
#    def retrieve(self, request, *args, **kwargs):
#        return super().retrieve(request, *args, **kwargs)

#   Forma de substituir method POST
#    def create(self, request, *args, **kwargs):
#        return super().create(request, *args, **kwargs)

#   Forma de substituir method PUT
#    def update(self, request, *args, **kwargs):
#        return super().update(request, *args, **kwargs)

#   Forma de substituir method PATCH
#    def partial_update(self, request, *args, **kwargs):
#        return super().partial_update(request, *args, **kwargs)

#   Forma de substituir method DELETE
#    def destroy(self, request, *args, **kwargs):
#        return super().destroy(request, *args, **kwargs)

    @action(methods=['get','post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass    
