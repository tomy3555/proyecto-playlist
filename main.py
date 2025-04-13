from cancion import Cancion
from utils import guardar_cancion, cargar_canciones, eliminar_cancion, vaciar_canciones
import requests

def buscar_canciones(query):
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=5"
    headers = {
        "Authorization": "Bearer TU_TOKEN_DE_ACCESO"  # Asegúrate de agregar tu token de acceso de Spotify
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        canciones = []
        for item in data['tracks']['items']:
            titulo = item['name']
            artista = item['artists'][0]['name']
            genero = "Desconocido"  # Puedes modificar esto si tienes más información sobre el género
            canciones.append({"titulo": titulo, "artista": artista, "genero": genero})
        return canciones
    else:
        print("Error al buscar canciones.")
        return []

def main():
    while True:
        print("\n🌟 Menú de opciones:")
        print("1. Buscar y agregar canción")
        print("2. Mostrar canciones guardadas")
        print("3. Eliminar canción")
        print("4. Vaciar todas las canciones")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Buscar y agregar canción
            busqueda = input("Escribe una canción o artista para buscar: ")
            resultados = buscar_canciones(busqueda)

            print("\n🎶 Canciones encontradas:")
            for idx, cancion in enumerate(resultados, start=1):
                print(f"{idx}. {cancion['titulo']} - {cancion['artista']} ({cancion['genero']})")

            seleccion = input("Número de canción a agregar (o enter para cancelar): ")

            if seleccion:
                try:
                    seleccion = int(seleccion) - 1
                    datos = resultados[seleccion]
                    nueva_cancion = Cancion(datos["titulo"], datos["artista"], datos["genero"])
                    guardar_cancion(nueva_cancion)
                    print("\n✅ Canción guardada en canciones.json")
                except (ValueError, IndexError):
                    print("Selección inválida, por favor elige un número entre 1 y 5.")
        
        elif opcion == "2":
            # Mostrar canciones guardadas
            print("\n🎶 Tus canciones guardadas:")
            for idx, c in enumerate(cargar_canciones(), start=1):
                print(f"{idx}. {c}")
        
        elif opcion == "3":
            # Eliminar canción
            print("\n🎶 Canciones guardadas para eliminar:")
            canciones = cargar_canciones()
            for idx, c in enumerate(canciones, start=1):
                print(f"{idx}. {c}")
            
            seleccion = input("Número de canción a eliminar (o enter para cancelar): ")
            
            if seleccion:
                try:
                    seleccion = int(seleccion) - 1
                    if eliminar_cancion(seleccion):
                        print("\n✅ Canción eliminada")
                    else:
                        print("\n❌ No se pudo eliminar la canción.")
                except (ValueError, IndexError):
                    print("Selección inválida.")
        
        elif opcion == "4":
            # Vaciar todas las canciones
            confirmacion = input("¿Estás seguro de que deseas vaciar todas las canciones? (y/n): ")
            if confirmacion.lower() == "y":
                vaciar_canciones()
                print("\n✅ Todas las canciones han sido eliminadas.")
        
        elif opcion == "5":
            # Salir
            print("👋 ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")
            
# Ejecutar el programa
if __name__ == "__main__":
    main()
