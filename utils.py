import json
from cancion import Cancion

ARCHIVO = "canciones.json"

def guardar_cancion(cancion):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            canciones = json.load(f)
    except FileNotFoundError:
        canciones = []

    canciones.append({
        "titulo": cancion.titulo,
        "artista": cancion.artista,
        "genero": cancion.genero,
        "estado_animo": cancion.estado_animo
    })

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(canciones, f, ensure_ascii=False, indent=4)

def cargar_canciones():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return [Cancion(**d) for d in datos]
    except FileNotFoundError:
        return []