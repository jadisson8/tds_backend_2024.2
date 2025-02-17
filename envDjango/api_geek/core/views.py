from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core import models, serializers, filters, pagination


class ProdutoCRUD(viewsets.ModelViewSet):
    queryset = models.ProdutoModel.objects.all()
    serializer_class = serializers.ProdutoSerializer
    pagination_class = pagination.CustomPagination
    filterset_class = filters.ProdutoFilter
    search_fields = ['nome']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        produto = self.get_object()
        if produto.estoque > 0:
            raise ValidationError(
                'Produtos só podem ser excluídos se estiverem fora de estoque.')
        else:
            return super().destroy(request, *args, **kwargs)


class CategoriaCRUD(viewsets.ModelViewSet):
    queryset = models.CategoriaModel.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FranquiaCRUD(viewsets.ModelViewSet):
    queryset = models.FranquiaModel.objects.all()
    serializer_class = serializers.FranquiaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClienteCRUD(viewsets.ModelViewSet):
    queryset = models.ClienteModel.objects.all()
    serializer_class = serializers.ClienteSerializer
    pagination_class = pagination.CustomPagination


class VendaCRUD(viewsets.ModelViewSet):
    queryset = models.VendaModel.objects.all()
    serializer_class = serializers.VendaSerializer
    pagination_class = pagination.CustomPagination


class RegistroCRUD(viewsets.ModelViewSet):
    queryset = models.RegistroModel.objects.all()
    serializer_class = serializers.RegistroSerializer
