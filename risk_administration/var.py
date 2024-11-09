# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
def get_closes():
##########
    return closes

def var(datos,titulos,valorportafolio ):
    rendimientos=datos.pctchange()
    matrizcov=rendimientos.cov()
    for i in range(len (datos)):
        precio=pd.DataFrame(columns=)
        precio[i]=datos[-1]
    ponderaciones=titulos*precio/valorportafolio 
    return var
    