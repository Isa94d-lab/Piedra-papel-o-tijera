import Ingresar_usuario
import Jugar_multijugador

usuarios= []
partidas = []

while True:
    print ("""
        -------------------
           THE CHACHIPUN  
        -------------------
    """)

    print("BIENVENID@! Que te gustaria hacer?")
    print("1. Ingresar usuario")
    print("2. Jugar multijugador")
    print("3. Jugar contra IA")
    print("4. Puntajes obtenidos")
    print("5. Salir")

    opcion = input("Ingresa una opcion -> ")

    if opcion == "1":
        Ingresar_usuario.info(usuarios)
    elif opcion == "2":
        Jugar_multijugador.MostrarUsuarios(usuarios)
    elif opcion == "3":
        pass 
    elif opcion == "4":
        pass
    elif opcion == "5":
        break
    else: 
        print("Ingresaste una respuesta INCORRECTA, Intenta de nuevo")
        input("Presiona ENTER para continuar -> ")