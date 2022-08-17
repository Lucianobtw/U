Proceso c_hipotenusa
	//Defino el tipo de dato de las variables
	//Datos de entrada: Cateto1 y Cateto2
	//Proceso (defino y aplico la formula para calcular la hipotenusa)
	//Datos de Salida: Resultado (Valor de la hipotenusa)
	Definir Cateto1 Como Real
	Definir Cateto2 Como Real
	Definir Hipotenusa Como Real
//Datos de entrada
	Escribir ("Ingrese la medida del primer cateto")
		Leer Cateto1
	Escribir ("Ingrese la medida del segundo cateto")
		Leer Cateto2
//Proceso 
		Hipotenusa<- raiz(Cateto1^2+Cateto2^2)
//Datos de Salida 
	Escribir  ("La medida de esta hipotenusa es de "), Hipotenusa 
FinProceso
