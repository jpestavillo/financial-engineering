Proceso sin_titulo
	definir nombre,nombre2,apellidopaterno,apellidomaterno,pregunta1 Como Caracter;
	Escribir  "cual es tu primer nombre jovenazo?" ;
	leer nombre ;
	Escribir "tienes un segundo nombre, si lo tienes escribelo?" ;
	leer pregunta1  ;
	Si pregunta1<>"no"  Entonces
		nombre2<- pregunta1 ;
	Sino
		nombre2<- "" ;
	FinSi
	escribir "cual es el apellido de tu jefe?" ;
	leer apellidopaterno ;
	escribir "cual es el apellido de tu sexy madre?" ;
	leer apellidomaterno ;
	escribir subcadena(nombre,0,0), subcadena(nombre2,0,0), subcadena(apellidopaterno,0,0), subcadena(apellidomaterno,0,0);

FinProceso
