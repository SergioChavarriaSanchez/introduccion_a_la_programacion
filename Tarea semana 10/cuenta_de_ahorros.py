deposito_inicial=float(input("Ingrese su deposito inicial: "))

TASA_INTERES=0.04

primer_año=deposito_inicial*(1+TASA_INTERES)
segundo_año=primer_año*(1+TASA_INTERES)
tercer_año=segundo_año*(1+TASA_INTERES)

print(f"Ahorros el primer año: {primer_año:.2f} \nAhorros el segundo año: {segundo_año:.2f} \nAhorros el tercer año: {tercer_año:.2f}")