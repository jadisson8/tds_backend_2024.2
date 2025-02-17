from django_filters import rest_framework as filter
from core import models


class ProdutoFilter(filter.FilterSet):
    nome = filter.CharFilter(field_name='nome', lookup_expr='icontains')
    descricao = filter.CharFilter(
        field_name='descricao', lookup_expr='icontains')
    categoria = filter.CharFilter(
        field_name='categoria__nome', lookup_expr='icontains')
    franquia = filter.CharFilter(
        field_name='franquia__nome', lookup_expr='icontains')

    class Meta:
        model = models.ProdutoModel
        fields = ['nome', 'descricao', 'categoria', 'franquia']
