def info(usuarios):
    while True:
        print("""
        -----------------------------
            REGISTRO DE USUARIO     
        -----------------------------
        """)
        usuario = {
            'nombre': [],
            'nickname': []
            }
        
        usuarios.append(usuario)
        nickname_registrado = {}
        
        nombre_delusuario = input("Ingresa tu nombre completo -> ")
        nickname_delusuario = input ("Ingresa tu nickname -> ")

        if nickname_delusuario in nickname_registrado:
            print("Este nickname YA ESTA REGISTRADO, Ingresa uno diferente")
            w= input("Preciona ENTER para continuar -> ")
            continue
        usuario['nombre'].append(nombre_delusuario)
        usuario['nickname'].append(nickname_delusuario)
        ingresar_otro =input("Te gustaria ingresar otro Usuario? SI(1) NO(2) -> ")
        if ingresar_otro != '1':
            w=input("Presiona ENTER para continuar -> ")
            break