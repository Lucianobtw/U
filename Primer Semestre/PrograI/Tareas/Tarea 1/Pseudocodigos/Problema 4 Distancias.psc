Proceso Diferencias
	//Datos y variables de entrada: Digito1 y Digito1_2
	//Proceso: Ingreso los parametros para calcular la distancia entre abos numeros)
	//Datos de salida: Resultados (Distancia entre ambos numeros)
	Escribir ("Ingrese el primer digito: ")
		Leer digito1
	Escribir ("Ingrese el segundo digito: ")
	Leer Digito2
	//Proceso(ingreso los parametros para calcular la distancia entre abos numeros)
		Si Digito1 > Digito2 Entonces
			dist<- Digito1-Digito2
		FinSi
		Si Digito1<Digito2 Entonces
			dist<- Digito2-Digito1
		Fin Si
		//Datos de salida y resultados
		Escribir ("La distancia entre los dos numeros es de: "), dist

FinProceso
