# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

from .models import Pregunta, RespuestaValidas
from datetime import datetime
from django.contrib.auth.models import User

class abm_apuestas(TestCase):

    def setUp(self):
        self.user = User(username='lgarimaldi')
        self.user.set_password('1234')
        self.user.save()

        self.pregunta = Pregunta(
            text = 'Llovera?',
            due_date = datetime.now(),
            create_user = self.user,
            update_user = self.user,
        )
        self.pregunta.save()

    def test_alta_pregunta(self):
        #user = User.objects.get(username = 'lgarimaldi')
        pregunta = Pregunta(
            text = 'Llueve hoy?',
            due_date = datetime.now(),
            create_user = self.user,
            update_user = self.user,
        )
        pregunta.save()

    def test_alta_respuestas(self):
        respuesta = RespuestaValidas(
            pregunta = self.pregunta,
            text = 'Si',
            create_user = self.user,
            update_user = self.user,
        )
        respuesta.save()

    def test_home():
        client = Client()
        response = client.get('/')
        print response

    def test_login_post_password_error(self):
        client = Client()
        response = client.post(
            '/accounts/login/',
            {
                'username': 'lgarimaldi',
                'password': ''
            }
        )
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_login_post_password_ok(self):
        client = Client()
        response = client.post(
            '/accounts/login/',
            {
                'username': 'lgarimaldi',
                'password': '1234'
            }
        )
        validator = True
        if response.status_code == '302':
            validator = False
        self.assertTrue(validator)
