# -*- coding: utf-8 -*-
"""
Módulo 5 -Manejo de archivos
@Diego Avalos
11-Ene-2020

Enumerar las filas
"""
import csv

#Abrimos el archivo
leer=open('texto2.csv','r')
leer_csv=csv.reader(leer)

#Impresión
for nombre, nota in leer_csv:
    print ('El alumno ',nombre, ' obtuvo ',nota)
#Cerrar el archivo
leer.close()

#Escribir en archivo
escribir=open('texto3.csv','w')
escribir_csv=csv.write(escribir)

