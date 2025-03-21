Algoritmo Examen_BancoSimulador
	definir usuarioycontrasena, usuarioycontrasenaIngresado, num, arregloMenosMas Como Caracter
	Definir intentos, celda, dineroRetirado, contadorDeIndice Como Entero
	Definir saldo, deposito, cargo, arregloHistoralMonto Como Real
	definir acceso Como Logico
	intentos=0
	acceso=Falso
	saldo=3000
	contadorDeIndice=0
	dimension arregloMenosMas[999]
	Dimension arregloHistoralMonto[999]
	Dimension usuarioycontrasena[2], usuarioycontrasenaIngresado[2]
	usuarioycontrasena[0]="Sergio" //Usuario
	usuarioycontrasena[1]="S3rg10"//Contraseña
	
	Escribir "Bienvenido al banco! "
	Mientras intentos<=5 y acceso=Falso Hacer
		Escribir "Ingrese su usuario: "
		leer usuarioycontrasenaIngresado[0]
		Escribir "Ingrese su contraseña"
		leer usuarioycontrasenaIngresado[1]
		si Minusculas(usuarioycontrasena[0]) = Minusculas(usuarioycontrasenaIngresado[0]) y usuarioycontrasena[1] = usuarioycontrasenaIngresado[1] Entonces
			Escribir "*** Acceso completado, Bienvenido! *** "
			acceso=Verdadero
		SiNo
			intentos=intentos+1
			si intentos<= 5 Entonces
				Escribir "*** Usuario o contraseña incorrectos, intentelo de nuevo *** "
			FinSi
		FinSi
	Fin Mientras
	si acceso=Falso Entonces
		Escribir "*** Acceso denegado, superó el limite de intentos. *** "
	FinSi
	si acceso=Verdadero Entonces
		Repetir
			Escribir "***** Menú: ***** "
			Escribir "1. Depositar dinero en la cuenta "
			Escribir "2. Sacar dinero de la cuenta "
			Escribir "3. Ver saldo "
			Escribir "4. Salir "
			leer num
			
			Mientras num <> "1" y num <>"2" y num <>"3" y num <>"4" Hacer
				Escribir ""
				Escribir "*** Opcion no valida, intente de nuevo *** "
				Escribir "Digite la opcion 1, 2, 3 o 4 del menú: "
				leer num
			Fin Mientras
			
			si num= "1" Entonces
				Escribir "Digite cantidad de dinero a depositar: "
				leer deposito
				si deposito >= 1000 Entonces
					cargo=deposito*0.05
					deposito=deposito-cargo
				FinSi
				saldo=saldo+deposito
				arregloMenosMas[contadorDeIndice]=" +"
				arregloHistoralMonto[contadorDeIndice]=deposito
				contadorDeIndice=contadorDeIndice+1
				Escribir ""
				Escribir "Ha depositado una cantidad final de: ", deposito, " Colones, ahora tiene un total de: ", saldo, " Colones en su cuenta. "
			FinSi
			si num = "2" Entonces
				Escribir "Digite cantidad de dinero a sacar: "
				leer dineroRetirado
				si dineroRetirado > saldo Entonces
					Escribir ""
					Escribir "*** La transaccion no pudo ser realizada, saldo insuficiente *** "
				SiNo
					si dineroRetirado MOD 1000 = 0 Entonces
						saldo=saldo-dineroRetirado
						arregloMenosMas[contadorDeIndice]=" -"
						arregloHistoralMonto[contadorDeIndice]=dineroRetirado
						contadorDeIndice=contadorDeIndice+1
						Escribir ""
						Escribir "Ha retirado: ", dineroRetirado, " Colones, su saldo actual es de: ", saldo, " Colones. "
						Escribir ""
					SiNo
						Escribir ""
						Escribir "*** Cantidad invalida para retirar *** "
					FinSi
				FinSi
			FinSi
			si num = "3" Entonces
				Escribir ""
				Escribir "El saldo actual es de: ", saldo, " Colones. "
				si contadorDeIndice=0 Entonces
					Escribir "*** Aun no hay transacciones para mostrar *** "
					Escribir ""
				SiNo
					Escribir "Historial de transacciones: "
					para celda=0 Hasta contadorDeIndice-1 Hacer
						Escribir arregloMenosMas[celda], arregloHistoralMonto[celda], " Colones. "
					FinPara
					Escribir ""
				FinSi
			FinSi
			
		Hasta Que num="4"
	FinSi
	
	
	
	
FinAlgoritmo
