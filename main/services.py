from main.models import Artista, Album, Grupo, ArtistaGrupo

def crear_artista(nombre, apellido, cantante, instrumento):
    artista = Artista(nombre = nombre, apellido = apellido, cantante = cantante, instrumento= instrumento)
    artista.save()
    #return artista

def crear_grupo(nombre, fecha_creacion):
    grupo = Grupo(nombre = nombre, fecha_creacion = fecha_creacion)
    grupo.save()
    #return grupo

def relacion_artista_grupo(artista, grupo, fecha_ingreso=None, agregado_por=None):
    artista_grupo = ArtistaGrupo(artista = artista, grupo = grupo, fecha_ingreso = fecha_ingreso, agregado_por= agregado_por)
    artista_grupo.save()

def agregar_album(titulo, year, grupo):
    album = Album(titulo = titulo, year =year, grupo = grupo)

def obtiene_artista():
    pass

def obtiene_grupo():
    pass

def artista_pertenece_a_grupos():
    pass

def artista_participa_albumes():
    pass

def grupo_albumes():
    pass