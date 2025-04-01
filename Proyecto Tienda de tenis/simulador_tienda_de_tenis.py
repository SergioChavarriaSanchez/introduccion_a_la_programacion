print("Hola, Bienvenido a su tienda de tenis de confianza! \nCree una cuenta.")
nombre_usuario = input("Ingrese un nombre de usuario: ")
contrasena_creada = input("Ingrese una contraseña: ")
direccion = input("Ingrese una direccion: ")
print("")

print("Inicie sesión: ")
usuario= input("Usuario: ")
contrasena = input("Contraseña: ")
while usuario != nombre_usuario and contrasena != contrasena_creada:
    print("Usuario y/o contraseña incorrectos! Intente de nuevo: ")
    usuario= input("Usuario: ")
    contrasena = input("Contraseña: ")
print("")

def modelos():
    print("Estos son todos los modelos disponibles! ")

print("Hola", usuario, ", bienvenid@ a E&S Store! ")
opcion = "1" or "2" or "3"
while opcion == "1" or opcion == "2" or opcion == "3":
    print("")
    print("Menú: ")
    opcion=input("1. Ver catalogo de tenis. \n2. Ver carrito de compras. \n3. Salir. \nIngrese opcion \"1\" , \"2\" o \"3\": ")
    if opcion == "1":
        print("")
        print("Catalogo: ")
        marca = input("- Nike\n- Adidas\n- Puma\n- New Balance\n- Vans\n Ingrese la marca a escoger: ").lower()
        if marca == "nike":
            print("")
            print("- Air Jordan: $100\nCantidad en stock: 25\n\n- Dunk: $120\nCantidad en stock: 30\n\n- Air Force one: $90\nCantidad en stock: 30\n")
            modelos()
        elif marca == "adidas":
            print("")
            print("- Samba: $110\nCantidad en stock: 25\n\n- Campus: $95\nCantidad en stock: 15\n\n- Yeezy: $115\nCantidad en stock: 20\n")
            modelos()
        elif marca == "puma":
            print("")
            print("- Suede: $80\nCantidad en stock: 23\n\n- Roma: $90\nCantidad en stock: 18\n\n- x Ferrari: $110\nCantidad en stock: 25\n")
            modelos()
        elif marca == "new balance":
            print("")
            print("- 9060: $120\nCantidad en stock: 25\n\n- 550: $100\nCantidad en stock: 30\n\n- 327: $105\nCantidad en stock: 15\n")
            modelos()
        elif marca == "vans":
            print("")
            print("- Old skool: $90\nCantidad em stock: 27\n\n- Knu skool: $105\nCantidad en stock: 20\n\n- SK8-HI: $85\nCantidad en stock: 18\n")
            modelos()
    if opcion == "2":
        print("...")
    if opcion == "3":
        break