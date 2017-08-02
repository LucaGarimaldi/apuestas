# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Preguntas, RespuestasValidas

def add_simbol_text(modeladmin,request,queryset):
    for q in queryset:
        q.text = q.text + '?'
        q.save()
add_simbol_text.short_description = 'Agregar simbolo ?'

class RespuestasValidasHeadInLine(admin.TabularInline):
    model = RespuestasValidas
    extra = 1

class PreguntasAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'create_user')
    search_fields = ('text','create_user__username')
    list_filter = ('create_user__username',)
    inlines = [RespuestasValidasHeadInLine, ]
    actions = [add_simbol_text,]

admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(RespuestasValidas)
