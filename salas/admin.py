from django.contrib import admin
from .models import Sala, Recurso, Reserva, Recorrencia


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade')
    search_fields = ('nome',)


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'sala')
    list_filter = ('tipo',)


@admin.register(Recorrencia)
class RecorrenciaAdmin(admin.ModelAdmin):
    list_display = ('frequencia',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'responsavel', 'data_inicio', 'status', 'tem_conflito')
    list_filter = ('status', 'sala', 'data_inicio')
    search_fields = ('responsavel', 'sala__nome')
    date_hierarchy = 'data_inicio'
    fieldsets = (
        ('Informações Básicas', {'fields': ('sala', 'responsavel', 'descricao')}),
        ('Datas e Horários', {'fields': ('data_inicio', 'data_fim')}),
        ('Recorrência e Status', {'fields': ('recorrencia', 'status')}),
    )
    
    def save_model(self, request, obj, form, change):
        if obj.tem_conflito():
            raise ValueError('Existe conflito com outra reserva neste horário!')
        super().save_model(request, obj, form, change)
