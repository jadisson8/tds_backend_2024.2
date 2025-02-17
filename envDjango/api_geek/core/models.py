from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator

from core.validations import validar_preco, validar_estoque, validar_quantidade


class CategoriaModel(models.Model):
    nome = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class FranquiaModel(models.Model):
    nome = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Franquia'
        verbose_name_plural = 'Franquias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class ProdutoModel(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField('Descrição', blank=True, null=True)
    preco = models.DecimalField('Preço(R$)', max_digits=8, decimal_places=2)
    estoque = models.PositiveSmallIntegerField(default=1)
    categoria = models.ForeignKey(
        CategoriaModel, on_delete=models.RESTRICT, related_name='produtos_categorias')
    franquia = models.ForeignKey(
        FranquiaModel, on_delete=models.CASCADE, related_name='produtos_franquias')

    def clean(self):
        validar_preco(self.preco)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome', 'preco']

    def __str__(self):
        return self.nome


SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros'),
]


class ClienteModel(models.Model):
    nome = models.CharField(max_length=128)
    sexo = models.CharField(default='O', max_length=1, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=15, blank=True, null=True, help_text='(99) 91234-5678', validators=[
                                RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$', message='Telefone deve estar no formato (99) 91234-5678')])
    email = models.EmailField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class VendaModel(models.Model):
    cliente = models.ForeignKey(
        ClienteModel, on_delete=models.RESTRICT, related_name='vendas_clientes')
    data_horario = models.DateTimeField('Data/Horário', auto_now_add=True)

    @admin.display(description='Valor')
    def valor(self):
        total = 0
        for registro in self.registros_vendas.all():
            total += registro.conta_produto()
        return total

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        ordering = ['cliente', 'data_horario']

    def __str__(self):
        return f'Cliente: {self.cliente.nome}'


class RegistroModel(models.Model):
    venda = models.ForeignKey(
        VendaModel, on_delete=models.RESTRICT, related_name='registros_vendas')
    produto = models.ForeignKey(
        ProdutoModel, on_delete=models.RESTRICT, related_name='registros_produtos')
    quantidade = models.PositiveSmallIntegerField(default=1)

    @admin.display(description='Preço(R$) da un.')
    def preco_produto(self):
        return self.produto.preco

    @admin.display(description='Estoque')
    def estoque_produto(self):
        return self.produto.estoque

    @admin.display(description='Conta')
    def conta_produto(self):
        return self.quantidade * self.produto.preco

    def clean(self):
        validar_estoque(self.produto.estoque, self.quantidade)
        validar_quantidade(self.quantidade)

    def save(self, *args, **kwargs):
        self.full_clean()
        self.produto.estoque -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return self.produto.nome
