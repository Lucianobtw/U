Proceso peri_area
	//Datos y variables de entrada: Base y altura
	//Proceso: Defino y aplico las formulas de perimetro y area del rectangulo
	//Datos de salida: Resultados (perimetro y area)
	espacio <- "     "
	//Datos de entrada 
	Escribir ("            Area y Perimetro del Rectangulo           ")
		Escribir espacio
	Escribir ("Defina la base del rectangulo: ")
		Leer base
	Escribir ("Defina la altura del rectangulo: ")
		Leer altura
	//Proceso
	perimetro <- (base*2)+(altura*2)
	area <- (base*altura)
	//Datos de salida
	Escribir ("                   RESULTADOS           ")
		Escribir espacio
	Escribir ("- El perimetro del rectangulo es: "), perimetro
		Escribir espacio
	Escribir ("- El area del rectangulo es: "), area
		Escribir espacio
FinProceso

