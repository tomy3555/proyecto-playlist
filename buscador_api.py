import requests

def buscar_canciones(termino):
    url = "https://itunes.apple.com/search"
    params = {
        "term": termino,
        "media": "music",
        "limit": 5,
        "lang": "es_es"
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    resultados = datos.get("results", [])

    if not resultados:
        print("No se encontraron canciones.")
        return []

    for i, cancion in enumerate(resultados, start=1):
        nombre = cancion.get("trackName", "Desconocido")
        artista = cancion.get("artistName", "Desconocido")
        genero = cancion.get("primaryGenreName", "Desconocido")
        print(f"{i}. {nombre} - {artista} ({genero})")

    return resultados

def seleccionar_cancion(resultados):
    opcion = input("Número de canción a agregar (o enter para cancelar): ")
    if not opcion.isdigit():
        print("Cancelado.")
        return None

    indice = int(opcion) - 1
    if 0 <= indice < len(resultados):
        seleccion = resultados[indice]
        return {
            "titulo": seleccion.get("trackName", "Desconocido"),
            "artista": seleccion.get("artistName", "Desconocido"),
            "genero": seleccion.get("primaryGenreName", "Desconocido")
        }
    else:
        print("Número inválido.")
        return None
