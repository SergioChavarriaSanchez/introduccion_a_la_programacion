peso=float(input("Indique su peso en kg: "))
estatura=float(input("Indique su estatura en metros: "))

indice_masa_corporal=peso/(estatura**2)
print(f"Tu indice de masa corporal es: {indice_masa_corporal:.2f}")
