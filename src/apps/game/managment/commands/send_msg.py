from django.core.management.base import BaseCommand

from django.template import loader


class Command(BaseCommand):

    def handle(self, *args, **options):

        usuario = "luca123"
        pregunta = "Llueve hoy?"
        respuesta = "si"
        mails = ['pruebascursodjango@gmail.com']

        subject = 'Ganaste'
        from_email = 'pruebascursodjango@gmail.com'
        to = mails
        text_content = 'Ganaste!!!. Nombre: ' + usuario + 'Pregunta:' + pregunta + 'Su Respuesta:' + respuesta

        template = loader.get_template('mails/hola_mundo.html')
        html_content = template.render({'nombre_usuario': usuario, 'texto_pregunta': pregunta, 'texto_respuesta': respuesta}, None)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")

        msg.send()
