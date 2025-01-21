from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    #inlines = [DisciplinaInline]

class TipoDivulgacaoAdmin(admin.ModelAdmin):
    model = TipoDivulgacao
    #inlines = [DisciplinaInline]

class MeioDivulgacaoAdmin(admin.ModelAdmin):
    model = MeioDivulgacao
    #inlines = [DisciplinaInline]

class PublicoAdmin(admin.ModelAdmin):
    model = Publico
    #inlines = [DisciplinaInline]

class LocalAdmin(admin.ModelAdmin):
    model = Local
    #inlines = [DisciplinaInline]

class MaterialAdmin(admin.ModelAdmin):
    model = Material
    #inlines = [DisciplinaInline]

class ParceriaAdmin(admin.ModelAdmin):
    model = Parceria
    #inlines = [DisciplinaInline]

class CoberturaAdmin(admin.ModelAdmin):
    model = Cobertura
    #inlines = [DisciplinaInline]

class OrganizadorAdmin(admin.ModelAdmin):
    model = Organizador
    #inlines = [DisciplinaInline]

class EventoAdmin(admin.ModelAdmin):
    model = Evento
    #inlines = [DisciplinaInline]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(TipoDivulgacao, TipoDivulgacaoAdmin)
admin.site.register(MeioDivulgacao, MeioDivulgacaoAdmin)
admin.site.register(Publico, PublicoAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Parceria, ParceriaAdmin)
admin.site.register(Cobertura, CoberturaAdmin)
admin.site.register(Organizador, OrganizadorAdmin)
admin.site.register(Evento, EventoAdmin)