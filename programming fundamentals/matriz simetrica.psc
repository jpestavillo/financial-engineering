	Proceso matrizSimetrica
		definir a, i, j, n Como Entero;
		definir bandera como logico;
		leer n; //tama?o de filas y columnas, filas = calumnas
		dimension a(100, 100); //funciona para matrices menores a 100 filas y colmnas
		
		//Capturadno datos de la matriz
		Para i<-0 hasta n-1 Hacer
			para j<-0 hasta n-1 Hacer
				leer a(i, j);
			FinPara
		FinPara
		
		bandera <- verdadero;
		Para i <- 1 hasta n-1 Hacer
			Para j <- 0 hasta i-1 Hacer
				si a(i,j) <> a(j,i) Entonces
					bandera <- falso;
				FinSi
			FinPara
		FinPara
		
		si bandera=verdadero Entonces
			escribir "Simetrica";
		Sino
			escribir "No simetrica";
		FinSi
FinProceso
