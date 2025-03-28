PRECIO_REGULAR_PAN=3000
DESCUENTO=0.60
pan_vendido_no_fresco=int(input("Digite la cantidad de barras de pan no frescas vendidas: "))

costo=pan_vendido_no_fresco*PRECIO_REGULAR_PAN
descuento_aplicado=costo*DESCUENTO
costo_final=costo-descuento_aplicado

print("El precio regular de una barra de pan es", PRECIO_REGULAR_PAN, "Colones")
print(f"Pero al ser pan no fresco se le hace un descuento del 60%, restandole una cantidad de {descuento_aplicado:.2f} Colones")
print(f"El costo total pasa de ser {costo:.2f} Colones, a ser {costo_final:.2f} Colones.")