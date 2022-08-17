//Entrada: minutos ingresados
//proceso: dividir cant de minutos entre 60 y calcular el resto a traves del %
//Salida: horas y minutos sobrantes segun la cantidad de minutos ingresada al inicio
Proceso horas_segun_minutos
	Escribir "Ingrese una cantidad de minutos: "
	Leer minutos
	horas<-minutos/60
	horastrun<- TRUNC(horas)
	resto<- minutos% 60
	Si horastrun<>0 Entonces
		Escribir "Usted ingreso: " horastrun " horas con " resto " minutos."
	SiNo
		Escribir "Usted ingreso: " resto " minutos."
	Fin Si
FinProceso

