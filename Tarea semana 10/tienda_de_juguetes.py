PESO_PAYASOS = 112
PESO_MUÑECAS = 75

cantidad_payasos=int(input("Ingrese la cantidad de payasos: "))
cantidad_muñecas=int(input("ingrese la cantidad de muñecas: "))

peso_total=PESO_PAYASOS*cantidad_payasos+PESO_MUÑECAS*cantidad_muñecas
print("El peso total del paquete con", cantidad_payasos, "payasos y", cantidad_muñecas, "muñecas, es de:", peso_total, "g")