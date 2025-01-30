from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UFAdmin(admin.ModelAdmin):
    model = UF
    inlines = [CidadeInline]

class DivulgacaoeInline(admin.TabularInline):
    model = Divulgacao
    extra = 1

class MeioDivulgacaoAdmin(admin.ModelAdmin):
    model = MeioDivulgacao
    inlines = [CidadeInline]


admin.site.register(Categoria)
admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(Divulgacao)
admin.site.register(MeioDivulgacao)
admin.site.register(Publico)
admin.site.register(Local)
admin.site.register(Material)
admin.site.register(Parceria)
admin.site.register(Cobertura)
admin.site.register(TipoCobertura)
admin.site.register(Colaborador)
admin.site.register(TipoParceria)
admin.site.register(Organizador)
admin.site.register(Evento)