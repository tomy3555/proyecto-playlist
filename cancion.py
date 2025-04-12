class Cancion:
    def __init__(self, titulo, artista, genero, estado_animo):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.estado_animo = estado_animo

    def __str__(self):
        return f'"{self.titulo}" de {self.artista} - {self.genero}, {self.estado_animo}'