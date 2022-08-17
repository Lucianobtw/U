Proceso operaciones_mat
	espacio <- "     "
	//Datos y variables de entrada(Defino numeros como real para trabajar con todo tipo de numeros reales)
	//Proceso (Defino las formulas de las 4 operaciones)
	//Datos de salida (Se muestran los resultados finales de cada operacion)
	Escribir ("o---o---o---o---o---o---o")
	Definir digito_1 Como Real
	Definir digito_2 Como Real
	//Datos de entrada
	Escribir ("Ingrese el primer digito:")
	Leer digito_1
	Escribir ("Ingrese el segundo digito:")
	Leer digito_2
	//Proceso 
	suma <- digito_1 + digito_2
	resta <- digito_1 - digito_2
	multipli <- digito_1*digito_2 
	
	Escribir ("o---o---o---o---o---o---o")
	//Datos de salida
	Escribir ("- La suma de ambos digitos resulta: "), suma 
	Escribir ("- La resta de ambos digitos resulta: "), resta 
	Escribir ("- La multiplicacion de ambos digitos resulta: "), multipli
	Si digito_2=0 Entonces
		Escribir "- No se puede dividir por 0"
	SiNo
		division <- digito_1/digito_2
		Escribir ("- La division de ambos digitos resulta: "), division 
	FinSi
	Escribir ("Fin del Programa")
FinProceso
