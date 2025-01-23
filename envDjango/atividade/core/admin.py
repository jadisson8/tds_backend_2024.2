from django.contrib import admin
from core.models import Projeto, Equipe, Membro, Tarefa


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['dt_final', 'nome', 'equipe', 'dt_inicial', 'orcamento']
    search_fields = ['nome', 'descricao']
    list_filter = ['dt_inicial', 'dt_final']
    date_hierarchy = 'dt_inicial'


class MembroInline(admin.TabularInline):
    model = Membro
    extra = 0


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativa', 'total_membros']
    search_fields = ['nome']

    inlines = [MembroInline]


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['dt_limite', 'nome', 'concluido', 'membro']
    search_fields = ['nome', 'descricao']
    list_filter = ['concluido', 'dt_limite']
