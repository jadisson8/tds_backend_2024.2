from rest_framework import serializers
from core import models


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='categoria-detail')

    class Meta:
        model = models.CategoriaModel
        fields = ['url', 'nome']


class FranquiaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='franquia-detail')

    class Meta:
        model = models.FranquiaModel
        fields = ['url', 'nome']


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='produto-detail')
    franquia = serializers.HyperlinkedRelatedField(
        view_name='franquia-detail', read_only=True)
    categoria = serializers.HyperlinkedRelatedField(
        view_name='categoria-detail', read_only=True)

    class Meta:
        model = models.ProdutoModel
        fields = ['url', 'nome', 'descricao', 'preco',
                  'estoque', 'categoria', 'franquia']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cliente-detail')

    class Meta:
        model = models.ClienteModel
        fields = ['url', 'nome', 'sexo', 'telefone', 'email']


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='registro-detail')
    venda = serializers.HyperlinkedRelatedField(
        view_name='venda-detail', read_only=True)
    produto = serializers.HyperlinkedRelatedField(
        view_name='produto-detail', read_only=True)

    class Meta:
        model = models.RegistroModel
        fields = ['url', 'venda', 'produto', 'quantidade',
                  'preco_produto', 'conta_produto', 'estoque_produto']


class VendaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='venda-detail')
    cliente = serializers.HyperlinkedRelatedField(
        view_name='cliente-detail', read_only=True)
    registros = serializers.HyperlinkedRelatedField(
        view_name='registro-detail', read_only=True, many=True)

    class Meta:
        model = models.VendaModel
        fields = ['url', 'cliente', 'data_horario', 'valor', 'registros']
