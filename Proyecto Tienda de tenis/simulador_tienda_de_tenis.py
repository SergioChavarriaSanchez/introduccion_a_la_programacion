catalogo = [
    {
        "marca": "nike",
        "modelos": {
            "Air jordan": {"precio": 100, "stock": 25},
            "Dunk": {"precio": 120, "stock": 30},
            "Air Force One": {"precio": 90, "stock": 30}
        }
    },
    {
        "marca": "adidas",
        "modelos": {
            "Samba": {"precio": 110, "stock": 25},
            "Campus": {"precio": 95, "stock": 15},
            "Yeezy": {"precio": 115, "stock": 20}
        }
        },
    {
        "marca": "puma",
        "modelos": {
            "Suede": {"precio": 80, "stock": 23},
            "Roma": {"precio": 90, "stock": 18},
            "XFerrari": {"precio": 110, "stock": 25}
        }
    },
    {
        "marca":"new balance",
        "modelos": {
            "9060": {"precio": 120, "stock": 25},
            "550": {"precio": 100, "stock": 30},
            "327": {"precio": 105, "stock": 15}
        }
    },
    {
        "marca": "vans",
        "modelos": {
            "Old skool": {"precio": 90, "stock": 27},
            "Knu skool": {"precio": 105, "stock": 20},
            "SK8-HI": {"precio": 85, "stock": 18}
        }
    }
]

carrito = []

def mensaje():
    print("Estos son todos los modelos disponibles! ")

compra=False



#Empieza el programa, pedimos datos para crear la cuenta.
print("Hola, Bienvenido a su tienda de tenis de confianza! \nCree una cuenta.")
nombre_usuario = input("Ingrese un nombre de usuario: ")
contrasena_creada = input("Ingrese una contraseña: ")
direccion = input("Ingrese una direccion: ")
print("\nCuenta creada con exito!")

#Verificamos los datos comparandolos al iniciar sesión. 
print("\nInicie sesión: ")
usuario= input("Usuario: ")
contrasena = input("Contraseña: ")
while usuario != nombre_usuario or contrasena != contrasena_creada:
    print("Usuario y/o contraseña incorrectos! Intente de nuevo: ")
    usuario= input("Usuario: ")
    contrasena = input("Contraseña: ")
print("")

#Mostramos el menú.
print("Hola", usuario, ", bienvenid@ a E&S Store! ")

while (True):
    print("")
    print("Menú: ")
    opcion=input("1. Ver catalogo de tenis. \n2. Ver carrito de compras. \n3. Ver estado del pedido. \n4. Salir. \nIngrese opcion \"1\" , \"2\" , \"3\" o \"4\": ")
    if opcion == "1": #Mostramos el catalogo de marcas.
        print("")
        print("Catalogo: ")
        for marca in catalogo:
            print("-" + marca["marca"].capitalize())
            
        marca_elegida = input("\nIngrese la marca a escoger: ").lower() #Se pregunta por la marca a escoger.
        print("")
        
        for marca in catalogo: #Se muestran los modelos de la marca escogida.
            if marca["marca"] == marca_elegida:
                print(f"Modelos disponibles de {marca_elegida.capitalize()}: ")
                for modelo, datos in marca["modelos"].items():
                    print(f"- {modelo}: ${datos["precio"]} Stock: {datos["stock"]}")
                modelo_elegido = input("\nIngrese el modelo para añadir al carrito: ")
                if modelo_elegido in marca["modelos"]:
                    carrito.append({
                        "marca": marca_elegida,
                        "modelo": modelo_elegido,
                        "precio": marca["modelos"][modelo_elegido]["precio"]
                    })
                    print("\nModelo añadido al carrito! ")
                else:
                    print("\nEl modelo no está disponible. ")
                    break
                
    if opcion == "2": #Mostramos el carrito de compras.
        print("\nCarrito de compras: ")
        if len(carrito) > 0:
            total=0
            for producto_agregado in carrito:
                print(f"- {producto_agregado["modelo"]}: ${producto_agregado["precio"]}")
                total+=producto_agregado["precio"]
            print("Precio total: $", total)
        else:
            print("El carrito está vacio. ")
            
        contador=1
        opcion_carrito=int(input("\n1- Volver a la tienda o 2- Finalizar compra: "))
        if opcion_carrito == 1:
            continue
        elif opcion_carrito == 2:
            print("\nElija un metodo de pago: ")
            metodo_de_pago=int(input("1- Tarjeta de credito o 2- Sinpe movil: "))
            if metodo_de_pago == 1:
                num_tarjeta=input("Ingrese su numero de tarjeta: ")
                while len(num_tarjeta) != 16: 
                    contador+=1
                    if contador > 3:
                        print("\n*** Sistema bloqueado, limite de intentos superados! ***")
                        exit()
                    print("Numero de tarjeta invalido, vuelva a intentarlo: ")
                    num_tarjeta=input("Ingrese su numero de tarjeta: ")
                if len(num_tarjeta) == 16 and contador <= 3:
                    fecha_vencimiento=int(input("Ingrese el año de vencimiento: "))    
                    if fecha_vencimiento < 2025:
                        print("\nSu tarjeta está vencida! ")
                        continue
                        
                    else:
                        contador=1
                        cvv=input("Ingrese el codigo de seguridad: ")
                        while len(cvv) != 3:
                            contador+=1
                            if contador > 3:
                                print("\n*** Sistema bloqueado, limite de intentos superados! ***")
                                exit()
                            print("Codigo de seguridad incorrecto, intente de nuevo: ")
                            cvv=input("Ingrese el codigo de seguridad: ")
                if len(cvv) == 3 and contador <=3:
                    compra=True
                    print("\nFactura: ")
                    for producto_agregado in carrito:
                        print(f"- {producto_agregado["modelo"]}: ${producto_agregado["precio"]}")
                        total+=producto_agregado["precio"]
                    print("Precio total: $", total)
                    print("\nCompra realizada con exito! ")
                    print("\nGracias por comprar en E&S Store! ")
                    carrito.clear()
            elif metodo_de_pago == 2:
                print("Realice el sinpe al siguiente numero: 8439-9902")
                comprobante=input("Ingrese el numero de comprobante: ")
                if len(comprobante) != 25:
                    print("\nNumero de comprobante invalido! ")
                    continue
                else:
                    compra=True
                    print("\nFactura: ")
                    for producto_agregado in carrito:
                        print(f"- {producto_agregado["modelo"]}: ${producto_agregado["precio"]}")
                        total+=producto_agregado["precio"]
                    print("Precio total: $", total)
                    print("\nCompra realizada con exito! ")
                    print("\nGracias por comprar en E&S Store! ")
                    carrito.clear()
    if opcion == "3":
        if compra == True:
            print("\nEl pedido ha sido entregado con exito en:", direccion)
        else:
            print("\nNo hay ninguna entrega pendiente. ")
    if opcion == "4": #Se termina el programa.
        print("\n*** Hasta luego, regrese pronto! ***")
        exit()