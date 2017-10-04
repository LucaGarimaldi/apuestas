# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from django.template import loader

from django.core import mail


class Command(BaseCommand):

    def handle(self, *args, **options):

        connection = mail.get_connection()
        import ipdb; ipdb.set_trace()
        connection.open()

        mail0 = mail.EmailMessage(
            'Asunto 0',
            'Cuerpo del email 0',
            'pruebacursodjango@gmail.com',
            ['pruebacursodjango@gmail.com'],
            connection=connection
        )
        print mail0.send()

        mail1 = mail.EmailMessage(
            'Asunto 1',
            'Cuerpo del email 1',
            'pruebacursodjango@gmail.com',
            ['pruebacursodjango@gmail.com'],
            connection=connection
        )
        print mail1.send()

        mail2 = mail.EmailMessage(
            'Asunto 2',
            'Cuerpo del email 2',
            'pruebacursodjango@gmail.com',
            ['pruebacursodjango@gmail.com'],
        )

        mail3 = mail.EmailMessage(
            'Asunto 3',
            'Cuerpo del email 3',
            'pruebacursodjango@gmail.com',
            ['pruebacursodjango@gmail.com'],
        )

        print connection.send_messages([mail2, mail3])
        connection.close()
