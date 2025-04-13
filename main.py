from cancion import Cancion
import buscador_api

def main():
    termino = input("Escribe una canción o artista para buscar: ")
    resultados = buscador_api.buscar_canciones(termino)

    datos = buscador_api.seleccionar_cancion(resultados)

    if datos:
        nueva_cancion = Cancion(datos["titulo"], datos["artista"], datos["genero"])
        print("\n🎵 Canción añadida:")
        print(nueva_cancion)

if __name__ == "__main__":
    main()
