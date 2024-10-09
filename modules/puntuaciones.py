import json
import os

archivo_json = 'puntuaciones.json'

#Con esto cargamos los puntajes desde el archivo JSON
def cargar_puntajes():
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as f:
            return json.load(f)
    return []

#Con esto guardamos los puntajes en el archivo JSON
def guardar_puntajes(puntajes):
    with open(archivo_json, 'w') as f:
        json.dump(puntajes, f, indent=4)

#Con esto agrefamos el puntaje de un jugador al archivo JSON 
def agregar_puntuacion(nickname, puntos):
    puntajes = cargar_puntajes()

    #Ahora verificamos si el jugador ya existe y contiene su nickname y puntos
    for jugador in puntajes:
        if jugador['nickname'] == nickname:
            jugador['puntos'] += puntos
            break
    else:
        #Si no, los creamos 
        puntajes.append({'nickname': nickname, 'puntos': puntos})

    guardar_puntajes(puntajes)

#Agregamos un nuevo usuario a JSON segun lo anterior
def agregar_usuario(nickname):
    puntajes = cargar_puntajes()
    
    #Confirmamos que el nickname no este repetido 
    if any(jugador['nickname'] == nickname for jugador in puntajes):
        print("Este nickname ya esta registrado")
        return

    #Añadimos los nickname y inicialisamos los puntos en 0
    puntajes.append({'nickname': nickname, 'puntos': 0}) 
    guardar_puntajes(puntajes)

#Con esta funcion enlistaremos a los mejores jugadores
def listar_mejores_jugadores():
    """Listar los tres mejores jugadores."""
    puntajes = cargar_puntajes()
    mejores_jugadores = sorted(puntajes, key=lambda x: x['puntos'], reverse=True)[:3]
    return mejores_jugadores

#Mostraremos el ultimo puesto en la lista 
def listar_ultimo_jugador():
    """Listar el jugador en el ultimo puesto"""
    puntajes = cargar_puntajes()
    if puntajes:
        return sorted(puntajes, key=lambda x: x['puntos'])[0]

    return None



def guardar_usuarios_en_json(usuarios):
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f, indent=4)
        


def cargar_usuarios_desde_json():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    return []
