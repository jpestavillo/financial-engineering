Proceso sin_titulo
	definir ventas, r, c, suma Como Entero;
	Dimension ventas[2, 3]; //2 renglones, 3 columnas
	Para r <- 0 hasta 1 Hacer
		para c <- 0 hasta 2 Hacer
			escribir "Ingresa las unidades vendidas ", r,", ", c;
			leer ventas[r, c];
		FinPara
	FinPara
	
	escribir "Promedio por modelo";
	para r <- 0 hasta 1 hacer
		suma <- 0;
		para c <- 0 hasta 2 Hacer
			suma <- suma + ventas[r, c];
		FinPara
		escribir "El promedio de ventas de ", r, " es ", suma/3;
	FinPara
	
	escribir "Promedio por mes";
	para c <- 0 hasta 2 hacer
		suma <- 0;
		para r <- 0 hasta 1 Hacer
			suma <- suma + ventas[r, c];
		FinPara
		escribir "El promedio de ventas de ", c, " es ", suma/2;
	FinPara
FinProceso
