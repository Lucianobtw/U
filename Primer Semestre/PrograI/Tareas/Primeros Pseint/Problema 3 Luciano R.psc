Proceso Edad_Cliente
	//Este programa tiene como objetivo encontrar el costo en $ que debera pagar una persona segun su edad//
	Escribir "Ingrese su edad para continuar"
	Leer edad 
	Si edad < 8 
		Escribir " Entrada: sin costo"
		
	FinSi
	//Se debe asignar el simbolo "menor o igual y menor o igual" para evitar incongruencias//
	Si edad >= 8 y edad <= 12
		Escribir "Entrada: $800"
	FinSi
	
	Si edad > 12
		Escribir "Entrada: $1500"
	FinSi
FinProceso
