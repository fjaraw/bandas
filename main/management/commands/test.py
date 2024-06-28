from django.core.management.base import BaseCommand
from main.services import *
# se ejecuta: python manage.py test_client
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #probar que se pueda agregar un nuevo Cliente
        print('Testeo de programa')
        #crear_artista('Peter','Gabriel','True','Guitarra')
        #crear_grupo('Genesis','1970-01-01')
        relacion_artista_grupo(1, 1, '1970', 'Phil Collins')
        #crear_artista('Peter','Capusotto','True','Voz')
        obtiene_artistas('Peter')
        print('Operación realizada.')