#lista de catalogo de tenis, con diccionarios por cada marca. 
catalogo = [ 
    {
        "marca": "nike",
        "modelos": {
            "air jordan": {"precio": 100, "stock": 25},
            "dunk": {"precio": 120, "stock": 30},
            "air force one": {"precio": 90, "stock": 30}
        }
    },
    {
        "marca": "adidas",
        "modelos": {
            "samba": {"precio": 110, "stock": 25},
            "campus": {"precio": 95, "stock": 15},
            "yeezy": {"precio": 115, "stock": 20}
        }
        },
    {
        "marca": "puma",
        "modelos": {
            "suede": {"precio": 80, "stock": 23},
            "roma": {"precio": 90, "stock": 10},
            "xferrari": {"precio": 110, "stock": 25}
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
            "old skool": {"precio": 90, "stock": 27},
            "knu skool": {"precio": 105, "stock": 20},
            "sk8-hi": {"precio": 85, "stock": 18}
        }
    }
]

carrito = []

compra=False
total = 0
clave_admin = "E&S2025"
acceso = False
carrito_vacio = False


#Empieza el programa, pedimos datos para crear la cuenta.
print("\nHola, Bienvenido a su tienda de tenis de confianza! \nCree una cuenta.")
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
    opcion=input("1. Ver catalogo de tenis. \n2. Ver carrito de compras. \n3. Ver estado del pedido. \n4. Menú de Administrador. \n5. Salir. \nIngrese opcion \"1\" , \"2\" , \"3\" , \"4\" o \"5\": ")
    if opcion == "1": #Mostramos el catalogo de marcas.
        print("")
        print("Catalogo: ")
        for marca in catalogo:
            print("-" + marca["marca"].capitalize())
            
        marca_elegida = input("\nIngrese la marca a escoger: ").lower() #Se pregunta por la marca a escoger.
        print("")
        marca_encontrada = False
        for marca in catalogo: #Se valida que la marca exista y se muestran los modelos de la marca escogida.
            if marca["marca"] == marca_elegida:
                marca_encontrada=True
                print(f"Modelos disponibles de {marca_elegida.capitalize()}: ")
                for modelo, datos in marca["modelos"].items():
                    print(f"- {modelo.capitalize()}: ${datos["precio"]} Stock: {datos["stock"]}")
                modelo_elegido = input("\nIngrese el modelo para añadir al carrito: ").lower() #Se pregunta por el modelo que quiere añadir al carrito.
                if modelo_elegido in marca["modelos"]: #Se valida que el modelo escogido exista y se agrega al carrito.
                    if marca["modelos"][modelo_elegido]["stock"]>0:
                        carrito.append({
                            "marca": marca_elegida,
                            "modelo": modelo_elegido,
                            "precio": marca["modelos"][modelo_elegido]["precio"]
                        })
                        print("\nModelo añadido al carrito! ")
                    else:
                        print("\nLo siento, ya no queda stock del modelo, intentelo más tarde! ")
                else:
                    print("\nEl modelo no está disponible. ")
                    continue
        if marca_encontrada == False:
            print("Esta marca no está disponible en nuestro catálogo! ")
            
    elif opcion == "2": #Mostramos el carrito de compras con los modelos agregados y el total del precio.
        print("\nCarrito de compras: ")
        if len(carrito) > 0:
            for producto_agregado in carrito:
                print(f"- {producto_agregado["modelo"].capitalize()}: ${producto_agregado["precio"]}")
                total+=producto_agregado["precio"]
            print("Precio total: $", total)
            carrito_vacio=False
        else:
            print("El carrito está vacio. ") #Si el carrito está vacio.
            carrito_vacio=True
        if carrito_vacio == True:
            opcion_carrito=input("\nIngrese cualquier digito para regresar al menú: ")
            continue
        else:
            contador = 1
            opcion_carrito=input("\n1- Volver a la tienda o 2- Finalizar compra: ") #Se da la opcion de terminar la compra o regresar al menú inicial.
            if opcion_carrito == "1":
                continue
            elif opcion_carrito == "2":
                print("\nElija un metodo de pago: ")
                metodo_de_pago=input("1- Tarjeta de credito/debito o 2- Sinpe movil: ") #Damos a escoger entre 2 metodos de pago (tarjeta o sinpe)
                if metodo_de_pago == "1":
                    while True:
                        try:
                            num_tarjeta = int(input("Ingrese su número de tarjeta: ")) #Validación de la tarjeta.
                            if len(str(num_tarjeta)) == 16:
                                break
                            else:
                                print("El numero debe de tener 16 digitos. ")
                                contador += 1
                        except:
                            print("Solo puede ingresar números! ")
                            contador += 1
                        if contador > 3:
                            print("\nLimite de intentos fallidos alcanzado, regresando al menú principal! ")
                            break
                    if contador <= 3:
                        contador = 1
                        while True:
                            try:
                                fecha_vencimiento=int(input("Ingrese el año de vencimiento: ")) #Validación de la fecha de vencimiento de la tarjeta.   
                                if fecha_vencimiento >= 2025:
                                    break
                                    
                                else:
                                    print("El año no es válido! ")
                                    contador+= 1
                            except:
                                print("Solo puede ingresar números! ")
                                contador+=1
                            if contador > 3:
                                print("\nLimite de intentos fallidos alcanzado, regresando al menú principal! ")
                                break
                        if contador <= 3:
                            contador=1
                            while True:
                                try:
                                    cvv = int(input("Ingrese el código de seguridad (cvv): ")) #Validación del codigo de seguridad de la tarjeta.
                                    if len(str(cvv)) == 3:
                                        break
                                    else:
                                        print("El cvv debe tener solo 3 digitos. ")
                                        contador += 1
                                except:
                                    print("Solo puede ingresar números! ")
                                    contador += 1
                                if contador > 3:
                                    print("\nLimite de intentos fallidos alcanzado, regresando al menú principal! ")
                                    break
                    if contador <=3:
                        compra=True
                        print("\nFactura: ")  #Se muestra la factura y se confirma la compra.
                        for producto_agregado in carrito:
                            print(f"- {producto_agregado["modelo"]}: ${producto_agregado["precio"]}")
                            total+=producto_agregado["precio"]
                        print("Precio total: $", total)
                        print("\nCompra realizada con exito! ")
                        print("\nGracias por comprar en E&S Store! ")
                        for producto_agregado in carrito:
                            for marca in catalogo:
                                if marca["marca"] == producto_agregado["marca"]:
                                    if producto_agregado["modelo"] in marca["modelos"]:
                                        marca["modelos"][producto_agregado["modelo"]]["stock"] -= 1
                        carrito.clear() #Se vacia el carrito cuando la compra se realiza.
                elif metodo_de_pago == "2":
                    print("Realice el sinpe al siguiente numero: 8439-9902")
                    contador=1
                    while True:
                        try:
                            comprobante=int(input("Ingrese el numero de comprobante: ")) #Validacion del numero de comprobante del sinpe.
                            if len(str(comprobante)) == 25:
                                break
                            else:
                                print("El comprobante debe tener 25 digitos! ")
                                contador += 1
                        except:
                            print("Solo puede ingresar números! ")
                            contador += 1
                        if contador > 3:
                            print("\nLimite de intentos fallidos alcanzado, regresando al menú principal! ")
                            break
                    if contador <= 3:  #Se confirma el pago con el metodo sinpe.
                        compra=True 
                        print("\nFactura: ")
                        for producto_agregado in carrito:
                            print(f"- {producto_agregado["modelo"]}: ${producto_agregado["precio"]}")
                            total+=producto_agregado["precio"]
                        print("Precio total: $", total)
                        print("\nCompra realizada con exito! ")
                        print("\nGracias por comprar en E&S Store! ")
                        for producto_agregado in carrito:
                            for marca in catalogo:
                                if marca["marca"] == producto_agregado["marca"]:
                                    if producto_agregado["modelo"] in marca["modelos"]:
                                        marca["modelos"][producto_agregado["modelo"]]["stock"] -= 1
                        carrito.clear()
    elif opcion == "3":  #Se da una actualizacion del estado del pedido.
        if compra == True:
            print("\nEl pedido ha sido enviado con exito a:", direccion)
        else:
            print("\nNo hay ninguna entrega pendiente. ")
    elif opcion == "4":     #opcion para el menú de administrador, opciones para añadir modelos o marcas al catalogo.
        intentos = 0
        while intentos < 3 and acceso == False:
            clave = input("Digite la clave de administrador: ") #Se necesita la clave para poder acceder.
            if clave == clave_admin:
                acceso = True
                break
            else:
                intentos += 1
                print("Clave incorrecta! ")
            
        if acceso == False:
            print("\nAcceso denegado, superó el limite de intentos! ")
        else:
            while True: #Mostramos el menú de administrador.
                print("\nMenú de administrador: \n1- Añadir marcas al catálogo.\n2- Añadir modelos a marcas disponibles.\n3- Salir al menú principal. ")
                opcion_admin = input("\nIngrese una opción del menú: ")
                if opcion_admin == "1":
                    nueva_marca = input("Ingrese el nombre de la marca que desea agregar: ").lower() #Opcion para agregar marcas al catalogo.
                    marca_existe=False
                    for marca in catalogo:
                        if marca["marca"] == nueva_marca: #se verifica que la marca no este agregada ya en el catalogo.
                            print("\nLa marca ya existe en el catálogo! ")
                            marca_existe = True
                            break
                    if marca_existe == False: #Se agrega la marca al catalogo.
                        catalogo.append({
                            "marca": nueva_marca,
                            "modelos": {}
                        })
                        print(f"\nLa marca: {nueva_marca.capitalize()} ha sido agregada al catálogo. ")
                        
                elif opcion_admin == "2": #Opcion para añadir modelos a marcas ya existentes.
                    print("\nMarcas disponibles: ")
                    for marca in catalogo: #Se muestran las marcas ya existentes.
                        print("-" + marca["marca"].capitalize())
                    marca_seleccionada = input("\nIngrese la marca en la que quiere añadir un nuevo modelo: ").lower()
                    marca_encontrada=False
                    for marca in catalogo:
                        if marca["marca"] == marca_seleccionada: #Se verifica que la marca exista dentro del catalogo.
                            nuevo_modelo = input(f"Ingrese el nombre del modelo para añadir a \"{marca_seleccionada.capitalize()}\": ").lower()
                            if nuevo_modelo in marca["modelos"]:
                                print("El modelo ya está disponible en nuestra tienda! ")
                                break
                            else:
                                while True: #Se pregunta por el precio y la cantidad en stock, y se hace la validacion de cada uno.
                                    try:
                                        precio = int(input("Ingrese el precio del modelo: "))
                                        break
                                    except:
                                        print("Digito invalido! ")
                                while True:
                                    try:
                                        stock = int(input("Ingrese la cantidad para stock: "))
                                        break
                                    except:
                                        print("Cantidad invalida! ")
                                
                                marca["modelos"][nuevo_modelo] = { #Se agrega el modelo a la marca.
                                    "precio":precio,
                                    "stock":stock
                                }
                                print(f"\nEl modelo \"{nuevo_modelo}\" se ha agregado con exito en la marca \"{marca_seleccionada}\". ")
                                marca_encontrada = True
                                break
                    if marca_encontrada == False:
                        print("\nLa marca no está disponible en el catálogo. ")
                            
                elif opcion_admin == "3": #Salimos del menú de administrador y volvemos al principal.
                    break
                else:
                    print("Opción invalida. ")
    elif opcion == "5": #Se termina el programa.
        print("\n*** Hasta luego, regrese pronto! ***")
        exit()
    else:
        print("\nOpción invalida! ")