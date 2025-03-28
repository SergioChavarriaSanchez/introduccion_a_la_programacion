cantidad_invertir=float(input("Ingrese la cantidad que quiere invertir: \n"))
tasa_interes_anual=float(input("Ingrese la tasa de interes anual (%): \n"))/100
numero_años=int(input("Ingrese la cantidad de años: \n"))

capital=cantidad_invertir*(1+tasa_interes_anual)**numero_años
print(f"El capital obtenido en la inversion es de: {capital:.2f} Colones. ")