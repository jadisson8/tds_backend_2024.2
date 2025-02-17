from django.contrib import admin

from core import models


@admin.register(models.CategoriaModel)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(models.FranquiaModel)
class FranquiaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(models.ProdutoModel)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'categoria', 'franquia']
    search_fields = ['nome', 'descricao', 'categoria__nome', 'franquia__nome']
    list_filter = ['nome', 'preco', 'categoria', 'franquia']


class RegistroInline(admin.TabularInline):
    model = models.RegistroModel
    extra = 0
    readonly_fields = ['preco_produto', 'conta_produto', 'estoque_produto']


@admin.register(models.VendaModel)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_horario', 'valor']
    search_fields = ['cliente__nome']
    date_hierarchy = 'data_horario'

    inlines = [RegistroInline]


@admin.register(models.ClienteModel)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sexo', 'telefone', 'email']
    search_fields = ['nome', 'telefone', 'email']
    list_filter = ['sexo']
