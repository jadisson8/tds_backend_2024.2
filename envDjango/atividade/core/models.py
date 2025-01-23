import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Equipe(models.Model):
    nome = models.CharField(max_length=100, null=False)
    ativa = models.BooleanField(verbose_name='Ativa?', default=True)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome', 'ativa']

    def __str__(self):
        return self.nome

    def total_membros(self):
        return self.membros.count()


class Projeto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField(
        verbose_name='Descrição', max_length=1000, null=False)
    dt_inicial = models.DateField(verbose_name='Data inicial', null=False)
    dt_final = models.DateField(verbose_name='Data final', null=False)
    orcamento = models.DecimalField(
        verbose_name='Orçamento', max_digits=10, decimal_places=2, null=True, blank=True)

    equipe = models.ForeignKey(
        Equipe, on_delete=models.RESTRICT, related_name='projetos', null=True, blank=True)

    def clean(self):
        if self.dt_final < self.dt_inicial:
            raise ValidationError(
                'Data de fim deve ser após data de início ou igual')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['dt_final', 'nome']

    def __str__(self):
        return f'{self.nome} - {self.dt_final}'


SEXO = (
    ('M', 'Mulher'),
    ('H', 'Homem'),
)


class Membro(models.Model):
    nome = models.CharField(max_length=100, null=False)
    sexo = models.CharField(choices=SEXO, max_length=1, null=True, blank=True)
    email = models.EmailField(max_length=100, null=False)
    telefone = models.CharField(null=True, blank=True, max_length=15, help_text='(99) 99999-9999',
                                validators=[RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$',
                                                           message='Telefone deve estar no formato (99) 99999-9999')]
                                )

    equipe = models.ForeignKey(
        Equipe, on_delete=models.RESTRICT, related_name='membros', null=True, blank=True)

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['nome', 'equipe']

    def __str__(self):
        return f'{self.nome} ({self.equipe})'


class Tarefa(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField(
        verbose_name='Descrição', max_length=1000, null=False)
    concluido = models.BooleanField(verbose_name='Concluído?', default=False)
    dt_limite = models.DateField(null=False, verbose_name='Data limite')
    horas_estimadas = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    proejto = models.ForeignKey(
        Projeto, on_delete=models.CASCADE, related_name='tarefas', null=True, blank=True)
    membro = models.ForeignKey(
        Membro, on_delete=models.SET_NULL, related_name='tarefas', null=True, blank=True)

    def clean(self):
        if self.dt_limite < datetime.date.today():
            raise ValidationError(
                'Data limite deve ser após ou igual a de hoje')

    def clean_horas_estimadas(self):
        if self.horas_estimadas <= 0:
            raise ValidationError('Horas estimadas deve ser maior que zero')

    def clean_membro(self):
        if self.membro.equipe != self.projeto.equipe:
            raise ValidationError('Membro deve pertencer à equipe do projeto')

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['dt_limite', 'concluido', 'nome']

    def __str__(self):
        return f'{self.nome} - {self.dt_limite}'
