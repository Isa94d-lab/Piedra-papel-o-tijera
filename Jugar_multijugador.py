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
            primer_jugador = int(input("-> ")) -1
            print("Ingresa el segundo jugador: ")
            segundo_jugador = int(input("-> ")) -1

            partidas = {
                'Opciones_seleccionadas_jugador1': [],
                'Opciones_seleccionadas_jugador2': []
            }



            print(f"""
            ---------------------
                EFRENTAMIENTO     
            ---------------------
            """)
            print(f"    /\/\ {usuario['nickname'][primer_jugador]} /\/\  V.R  /\/\ {usuario['nickname'][segundo_jugador]} /\/\ ")
            # w=input("    Preciona ENTER para continuar -> ")
            rondas_consecutivas_jugador1= 0
            rondas_consecutivas_jugador2= 0
            while rondas_consecutivas_jugador1 <= 3 or rondas_consecutivas_jugador2 <= 3: 
                print("""
                ----------
                    GO!     
                ----------
                """)
                print(f"Ingresa la opcion de {usuario['nickname'][primer_jugador]}")
                print("1. Piedra / 2. Papel / 3. Tijera")
                primera_jugada_jugador1 = input("-> ")
                if primera_jugada_jugador1 == '1':
                    escogio = 'Piedra'
                    partidas['Opciones_seleccionadas_jugador1'].append(escogio)
                elif primera_jugada_jugador1 == '2':
                    escogio = 'Papel'
                    partidas['Opciones_seleccionadas_jugador1'].append(escogio)
                elif primera_jugada_jugador1 == '3':
                    escogio = 'Tijera'
                    partidas['Opciones_seleccionadas_jugador1'].append(escogio)

                print(f"Ingresa la opcion de {usuario['nickname'][segundo_jugador]}")
                print("1. Piedra / 2. Papel / 3. Tijera")
                primera_jugada_jugador2 = input("-> ")
                if primera_jugada_jugador2 == '1':
                    escogio = 'Piedra'
                    partidas['Opciones_seleccionadas_jugador2'].append(escogio)
                elif primera_jugada_jugador2 == '2':
                    escogio = 'Papel'
                    partidas['Opciones_seleccionadas_jugador2'].append(escogio)
                elif primera_jugada_jugador2 == '3':
                    escogio = 'Tijera'
                    partidas['Opciones_seleccionadas_jugador2'].append(escogio)
                print(partidas)

                if primera_jugada_jugador1 == '1' and primera_jugada_jugador2 == '1' or primera_jugada_jugador1 == '2' and primera_jugada_jugador2 == '2' or primera_jugada_jugador1 == '3' and primera_jugada_jugador2 == '3':
                    print("EMPATE")
                elif primera_jugada_jugador1 == '2' and primera_jugada_jugador2 == '1' or primera_jugada_jugador1 == '1' and primera_jugada_jugador2== '3' or primera_jugada_jugador1 == '3' and primera_jugada_jugador2== '2':
                    print(f"EL GANADOR DE ESTA RONDA ES -> {usuario['nickname'][primer_jugador]}")
                    rondas_consecutivas_jugador1 += 1
                else:
                    print(f"EL GANADOR DE ESTA RONDA ES -> {usuario['nickname'][segundo_jugador]}")
                    rondas_consecutivas_jugador2 += 1
                
                if rondas_consecutivas_jugador1 == 2: 
                    print(f"{usuario['nickname'][primer_jugador]} CONSIGUIO UN ESCUDO!")
                    w=input("Preciona ENTER para continuar -> ")                
                
            

