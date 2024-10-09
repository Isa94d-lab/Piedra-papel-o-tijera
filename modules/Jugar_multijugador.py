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
                'ganadores': []
            }



            print(f"""
            ---------------------
                EFRENTAMIENTO     
            ---------------------
            """)
            print(f"    /\/\ {usuario['nickname'][primer_jugador]} /\/\  V.R  /\/\ {usuario['nickname'][segundo_jugador]} /\/\ ")
            # w=input("    Preciona ENTER para continuar -> ")

            escudo_jugador1 = False
            escudo_jugador2 = False

            # rondas_consecutivas_jugador1= 0
            # rondas_consecutivas_jugador2= 0
            partidas_ganadas_jugador1 = 0 
            partidas_ganadas_jugador2 = 0

            victoria_jugador1 = 0
            victoria_jugador2 = 0


            while True: 
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
                elif primera_jugada_jugador1 == '2':
                    escogio = 'Papel'
                elif primera_jugada_jugador1 == '3':
                    escogio = 'Tijera'


                print(f"Ingresa la opcion de {usuario['nickname'][segundo_jugador]}")
                print("1. Piedra / 2. Papel / 3. Tijera")
                primera_jugada_jugador2 = input("-> ")
                if primera_jugada_jugador2 == '1':
                    escogio = 'Piedra'
                elif primera_jugada_jugador2 == '2':
                    escogio = 'Papel'
                elif primera_jugada_jugador2 == '3':
                    escogio = 'Tijera'

                if primera_jugada_jugador1 == primera_jugada_jugador2:
                    print("EMPATE")
                    
                elif (primera_jugada_jugador1 == '2' and primera_jugada_jugador2 == '1') or \
                     (primera_jugada_jugador1 == '1' and primera_jugada_jugador2== '3') or \
                     (primera_jugada_jugador1 == '3' and primera_jugada_jugador2== '2'):
                        print(f"EL GANADOR DE ESTA RONDA ES -> {usuario['nickname'][primer_jugador]}")
                        ganador = {usuario['nickname'][primer_jugador]} 
                else:
                    print(f"EL GANADOR DE ESTA RONDA ES -> {usuario['nickname'][segundo_jugador]}")
                    ganador = {usuario['nickname'][segundo_jugador]}



                if ganador == {usuario['nickname'][primer_jugador]}:
                    partidas_ganadas_jugador1 += 1
            
                    if escudo_jugador2 == False and partidas_ganadas_jugador2 >= 1: 
                        partidas_ganadas_jugador2 =0
                    
                    partidas['ganadores'].append(ganador)

#/////////////////////////////////////////////////////////////////////////////////

                elif ganador == {usuario['nickname'][segundo_jugador]}:
                    partidas_ganadas_jugador2 += 1

                    if escudo_jugador1 == False and partidas_ganadas_jugador1 >= 1: 
                        partidas_ganadas_jugador1 =0
                    
                    partidas['ganadores'].append(ganador)



                if partidas_ganadas_jugador1 == 2 and not escudo_jugador1:
                    escudo_jugador1 = True
                    print(f"{usuario['nickname'][primer_jugador]} CONSIGUIO UN ESCUDO!")

                if partidas_ganadas_jugador2 == 2 and not escudo_jugador2: 
                    escudo_jugador2 = True
                    print(f"{usuario['nickname'][segundo_jugador]} CONSIGUIO UN ESCUDO!")

                # Destruir escudo si el oponente gana una ronda después de que el escudo fue otorgado
                if escudo_jugador1 and ganador == {usuario['nickname'][segundo_jugador]}:
                    escudo_jugador1 = False
                    print(f"EL ESCUDO DE {usuario['nickname'][primer_jugador]} HA SIDO DESTRUIDO!")

                if escudo_jugador2 and ganador == {usuario['nickname'][primer_jugador]}:
                    escudo_jugador2 = False
                    print(f"EL ESCUDO DE {usuario['nickname'][segundo_jugador]} HA SIDO DESTRUIDO!")

                if partidas_ganadas_jugador1 == 3:
                    print(f"EL JUGADOR DEFINITIVO ES {usuario['nickname'][primer_jugador]}")
                    w=input("Pulsa ENTER para continuar -> ")
                    break 
                elif partidas_ganadas_jugador2 == 3:
                    print(f"EL JUGADOR DEFINITIVO ES {usuario['nickname'][segundo_jugador]}")
                    w=input("Pulsa ENTER para continuar -> ")
                    break
        break 