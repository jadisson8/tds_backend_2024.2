from django.contrib import admin
from django.db import models
from datetime import date


class Montadora(models.Model):
    nome = models.CharField(verbose_name='Nome',
                            blank=False, null=False, max_length=128)
    pais = models.CharField(verbose_name='País',
                            blank=False, null=False, max_length=128)
    ano_fundacao = models.PositiveIntegerField(
        verbose_name='Ano de Fundação', blank=False, null=False)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'
        ordering = ['-ano_fundacao']

    def __str__(self):
        return f'{self.nome} - {self.pais}'

    @admin.display(description='Anos de Operação')
    def idade(self):
        return date.today().year - self.ano_fundacao

    @admin.display(description='Quantidade de Veículos')
    def count_veiculos(self):
        return self.veiculos.count()


MOTOR_CHOICES = (
    ('1.0', 'Motor 1.0'),
    ('1.3', 'Motor 1.3'),
    ('1.4', 'Motor 1.4'),
    ('1.6', 'Motor 1.6'),
    ('2.0', 'Motor 2.0'),
)


class ModeloVeiculo(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    motorizacao = models.CharField(
        choices=MOTOR_CHOICES, null=False, blank=False, max_length=5)
    em_producao = models.BooleanField(default=False, blank=False, null=False)

    montadora = models.ForeignKey(
        Montadora, on_delete=models.RESTRICT, related_name='veiculos')

    class Meta:
        verbose_name = 'Modelo de Veículo'
        verbose_name_plural = 'Modelos de Veículos'
        ordering = ['montadora__nome', 'nome']

    def __str__(self):
        return f'{self.montadora} - {self.nome}'


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, null=False, blank=False)
    cor = models.CharField(max_length=32, null=False, blank=False)
    ano = models.PositiveIntegerField(null=False, blank=False)
    km_rodados = models.PositiveIntegerField(null=False, blank=False)
    modelo = models.ForeignKey(
        ModeloVeiculo, on_delete=models.RESTRICT, related_name='veiculos')

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['modelo__montadora__nome', 'modelo__nome']

    def __str__(self):
        return f'{self.modelo} - {self.placa}'
