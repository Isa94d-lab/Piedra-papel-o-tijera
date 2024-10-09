#Importamos todo lo necesario
import modules.Ingresar_usuario as Ingresar_usuario
import modules.Jugar_multijugador as Jugar_multijugador
import modules.Jugar_ia as Jugar_ia 
import modules.puntuaciones as puntuaciones
from modules.puntuaciones import cargar_usuarios_desde_json
usuarios = puntuaciones.cargar_puntajes()
partidas = []
usuarios = cargar_usuarios_desde_json()

while True:
    print("""
        -------------------
           THE CHACHIPUN  
        -------------------
    """)

    print("BIENVENID@! Que te gustaría hacer?")
    print("1. Ingresar usuario")
    print("2. Jugar multijugador")
    print("3. Jugar contra IA")
    print("4. Puntajes obtenidos")
    print("5. Salir")

    opcion = input("Ingresa una opcion -> ")
    #Dependiendo de lo que ingrese el usuario lo enviaremos a diferentes modulos
    if opcion == "1":
        Ingresar_usuario.info(usuarios)
    elif opcion == "2":
        Jugar_multijugador.MostrarUsuarios(usuarios)
    elif opcion == "3":
        Jugar_ia.info(usuarios)
    elif opcion == "4":
        print("Estadisticas de juego:")
        print("Mejores jugadores:")
        mejores_jugadores = puntuaciones.listar_mejores_jugadores()
        for jugador in mejores_jugadores:
            print(f"Nickname: {jugador['nickname']}, Puntos: {jugador['puntos']}")
        
        ultimo_jugador = puntuaciones.listar_ultimo_jugador()
        if ultimo_jugador:
            print(f"Ultimo jugador: {ultimo_jugador['nickname']} con {ultimo_jugador['puntos']} puntos")
    elif opcion == "5":
        break
    else: 
        print("Ingresaste una respuesta INCORRECTA, Intenta de nuevo")
        input("Presiona ENTER para continuar -> ")