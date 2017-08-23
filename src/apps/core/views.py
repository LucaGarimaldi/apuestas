# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def register_user(request):
    template = loader.get_template('registration/register.html')
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            grupo_jugador = Groups.objects.get(name='Jugador')
            user.save()
            user.group.add(grupo_jugador)
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))
