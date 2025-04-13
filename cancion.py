import json

class Cancion:
    lista_canciones = []
    
    def __init__(self, titulo, artista, genero, estado_animo=None):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.estado_animo = estado_animo

    def __str__(self):
        return f'"{self.titulo}" de {self.artista} - {self.genero}, {self.estado_animo}'
    
    @classmethod
    def agregar_cancion(cls, cancion): 
        cls.lista_canciones.append(cancion)
        cls.guardar_canciones()

    @classmethod
    def guardar_canciones(cls):
        with open('canciones.json', 'w') as archivo:
            canciones_dict = [
                {"titulo": cancion.titulo, "artista": cancion.artista, 
                 "genero": cancion.genero, "estado_animo": cancion.estado_animo}
                for cancion in cls.lista_canciones
            ]
            json.dump(canciones_dict, archivo)

    @classmethod
    def cargar_canciones(cls):
        try:
            with open('canciones.json', 'r') as archivo:
                canciones_dict = json.load(archivo)
                cls.lista_canciones = [Cancion(**cancion) for cancion in canciones_dict]
        except FileNotFoundError:
            cls.lista_canciones = []