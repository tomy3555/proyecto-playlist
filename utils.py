import json
from cancion import Cancion

ARCHIVO = "canciones.json"

def guardar_cancion(cancion):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            canciones = json.loads(contenido) if contenido else []
    except FileNotFoundError:
        canciones = []
    except json.JSONDecodeError:
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
    except json.JSONDecodeError:
        return []

def eliminar_cancion(indice):
    canciones = cargar_canciones()
    if 0 <= indice < len(canciones):
        del canciones[indice]
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([c.__dict__ for c in canciones], f, ensure_ascii=False, indent=4)
        return True
    return False

def vaciar_canciones():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)
