
usuario_correcto = "Estudiantes"#Este será el usuario dado por el administrador.
contrasena_correcta = "inscripciones2025"#Esta será la contraseña.

#Funcion de inicio de sesion.
def iniciar_sesion():
    #Mostramos el mensaje de saludo inicial y las credenciales que se deben utilizar.
    print(f"\nHola, ingrese a nuestros servicios iniciando sesión con los siguientes datos:\nUsuario: {usuario_correcto}\nContraseña: {contrasena_correcta} ")
    
    #Hacemos la comparación del usuario ingresado con el correcto (sin limite de intentos)
    while True:
        usuario = str(input("\nIngrese el usuario: "))
        if usuario == usuario_correcto:
            break
        else:
            print("El usuario no es correcto, vuelve a intentarlo: ")
    
    #Hacemos la comparación de las contraseñas (3 intentos permitidos)
    intentos = 0
    while intentos < 3:
        contrasena = str(input("Ingrese la contraseña: "))
        if contrasena == contrasena_correcta:
            print("\nEl inicio de sesión fue un exito! Bienvenido.")
            break
        else:
            intentos+=1
            if intentos == 3:
                print("\n*** Ha superado el limite de intentos, programa bloqueado ***")
                exit()
            else:
                print("\nContraseña incorrecta, intentelo nuevamente! ")
                continue

#Funcion para inscribir estudiantes.
def inscripcion():
    while True:
        seccion = input("\nIngrese la sección en la que desea inscribir al estudiante (7, 8 o 9): ")
        if seccion in secciones:
            break
        else:
            print("Sección no encontrada dentro de las opciones! Intentalo nuevamente: ")
    
    #Definimos las variables de los datos del estudiante y nos aseguramos de que se completen los campos.
    while True:
        nombre= input("Ingresa el nombre del estudiante: ")
        if len(nombre) < 3:
            print("\nIngrese el nombre del estudiante por favor! ")
        else:
            break
    while True:
        apellido= input("Ahora su apellido: ")
        if len(apellido) < 2:
            print("\nIngrese un apellido por favor! ")
        else:
            break
    while True:
        try: #Validamos que se escriban solo numeros y no letras.
            cedula= int(input("Ingresa su numero de cedula: "))
            if len(str(cedula)) < 8:
                print("\nCantidad de digitos invalidos para una cedula! ")
            else:
                break
        except:
            print("\nIngrese un numero de cedula valido por favor! ")
    
    #Creamos un diccionario que guarde los datos del estudiante inscrito.
    estudiante= {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula 
    }
    #Añadimos el diccionario con el estudiante a la sección escogida.
    secciones[seccion].append(estudiante)
    
    print("\nFelicidades, has inscrito un nuevo estudiante! ")

#Funcion para consultar las secciones.
def consultar():
    print("\nSecciones: ")
    for seccion, estudiantes_inscritos in secciones.items():
        print(f"\nSección \"{seccion}\":")
        
        if len(estudiantes_inscritos) == 0:#Si no hay estudiantes muestra que no los hay.
            print("No hay estudiantes inscritos. ")
        else:
            for estudiante in estudiantes_inscritos:
                print(f"- {estudiante["nombre"]} {estudiante["apellido"]} -> Cedula: {estudiante["cedula"]}")

#Definimos el diccionario principal con las secciones.
secciones = {
    "7": [],
    "8": [],
    "9": []
}





# *** Inicia el programa: ***

iniciar_sesion()

#Mostramos el menu principal del sistema.
while True:
    print("\nMenú:\n1. Inscribir un estudiante.\n2. Consultar las secciones.\n3. Salir del sistema. ")
    opcion = input("\nIngrese una opción del menú: ")#Solicitamos una opcion del menu
    
    #Agregamos la funcion segun su opcion correspondiente.
    if opcion == "1":
        inscripcion()
    elif opcion =="2":
        consultar()
    elif opcion == "3": #Opcion de salir y finalizar el programa.
        print("\nGracias por su tiempo! Adios.")
        exit()
    else:
        print("\nOpción invalida, por favor vuelva a intentarlo: ")#En caso de no ingresar una opcion valida.