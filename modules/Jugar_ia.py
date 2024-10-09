import random
def info(usuarios):
    while True:
        num = 0
        print("""
        ----------------------------
            JUGAR CONTRA MAQUINA     
        ----------------------------
        """)
        #Lo mismo que en multijugador pero contra una maquina, la maquina sera la que escoja sus propios valores 
        print("Jugadores Disponibles:")
        for usuario in usuarios:
            for i in range(len(usuario['nickname'])):
                print(f"{num+1}. {usuario['nickname'][num]}") 
                num += 1
            print("Segun los numeros de la tabla, ingresa el nickname del jugador que se enfrentara a la maquina: ") 
            primer_jugador = int(input("-> ")) -1

            partidas = {
                'ganadores': []
            }



            print(f"""
            ---------------------
                EFRENTAMIENTO     
            ---------------------
            """)
            print(f"    /\/\ {usuario['nickname'][primer_jugador]} /\/\  V.R  /\/\ MAQUINA /\/\ ")
            # w=input("    Preciona ENTER para continuar -> ")

            escudo_jugador1 = False
            escudo_maquina = False

            # rondas_consecutivas_jugador1= 0
            # rondas_consecutivas_jugador2= 0
            partidas_ganadas_jugador1 = 0 
            partidas_ganadas_maquina = 0


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


                print(f"Se ingresa la opcion de la maquina")
                print("1. Piedra / 2. Papel / 3. Tijera")
                x=[1, 2, 3]
                jugada_maquina = int(random.choice(x))
                print(f"La opcion escogida por la maquina fue -> {jugada_maquina}")
                if jugada_maquina == '1':
                    escogio = 'Piedra'
                elif jugada_maquina == '2':
                    escogio = 'Papel'
                elif jugada_maquina == '3':
                    escogio = 'Tijera'

                if primera_jugada_jugador1 == jugada_maquina:
                    print("EMPATE")
                    
                elif (primera_jugada_jugador1 == '2' and jugada_maquina == '1') or \
                     (primera_jugada_jugador1 == '1' and jugada_maquina == '3') or \
                     (primera_jugada_jugador1 == '3' and jugada_maquina == '2'):
                        print(f"EL GANADOR DE ESTA RONDA ES -> {usuario['nickname'][primer_jugador]}")
                        ganador = {usuario['nickname'][primer_jugador]} 
                else:
                    print(f"EL GANADOR DE ESTA RONDA FUE -> LA MAQUINA ")
                    ganador = 'LA MAQUINA'



                if ganador == {usuario['nickname'][primer_jugador]}:
                    partidas_ganadas_jugador1 += 1
            
                    if escudo_maquina == False and partidas_ganadas_maquina >= 1: 
                        partidas_ganadas_maquina =0
                    
                    partidas['ganadores'].append(ganador)

#/////////////////////////////////////////////////////////////////////////////////

                elif ganador == 'LA MAQUINA':
                    partidas_ganadas_maquina += 1

                    if escudo_jugador1 == False and partidas_ganadas_jugador1 >= 1: 
                        partidas_ganadas_jugador1 =0
                    
                    partidas['ganadores'].append(ganador)



                if partidas_ganadas_jugador1 == 2 and not escudo_jugador1:
                    escudo_jugador1 = True
                    print(f"{usuario['nickname'][primer_jugador]} CONSIGUIO UN ESCUDO!")

                if partidas_ganadas_maquina == 2 and not escudo_maquina: 
                    escudo_maquina = True
                    print(f"LA MAQUINA CONSIGUIO UN ESCUDO!")

        
                if escudo_jugador1 and ganador == 'LA MAQUINA':
                    escudo_jugador1 = False
                    print(f"EL ESCUDO DE {usuario['nickname'][primer_jugador]} HA SIDO DESTRUIDO!")

                if escudo_maquina and ganador == {usuario['nickname'][primer_jugador]}:
                    escudo_maquina = False
                    print(f"EL ESCUDO DE LA MAQUINA HA SIDO DESTRUIDO!")

                if partidas_ganadas_jugador1 == 3:
                    print(f"EL JUGADOR DEFINITIVO ES {usuario['nickname'][primer_jugador]}")
                    w=input("Pulsa ENTER para continuar -> ")
                    break 
                elif partidas_ganadas_maquina == 3:
                    print(f"EL JUGADOR DEFINITIVO ES LA MAQUINA")
                    w=input("Pulsa ENTER para continuar -> ")
                    break
        break 