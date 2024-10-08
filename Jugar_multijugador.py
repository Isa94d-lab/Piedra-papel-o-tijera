def MostrarUsuarios(usuarios):
    while True:
        num = 0
        print("""
        --------------------------
            JUGAR MULTIJUGADOR     
        --------------------------
        """)
        print("Jugadores Disponibles:")
        for usuario in usuarios:
            for i in range(len(usuario['nickname'])):
                print(f"{num+1}. {usuario['nickname'][num]}") 
                num += 1
            print("Segun los numeros de la tabla ingresa el nickname del primer jugador: ") 
            primer_jugador = int(input(" -> ")) -1
            print("Ingresa el segundo jugador: ")
            segundo_jugador = int(input(" -> ")) -1

            print(f"El primer jugador es -> {usuario['nickname'][primer_jugador]}")
            print(f"El segundo jugador es -> {usuario['nickname'][segundo_jugador]}")

            print(f"""
            -----------------------
                EFRENTAMIENTO     
            -----------------------
            """)