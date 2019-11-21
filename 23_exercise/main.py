#!/usr/bin/env python3

## codigo creado por Christian Portilla Pauca
## Website: https://www.christianportilla.com
## Mail: khrist14n@gmail.com

import random

def mensaje_inicio():
    mensaje = '\nInicio de Programa\n'
    print(mensaje)
    
def mensaje_fin():
    mensaje = '\nFin de Programa\n'
    print(mensaje)

def ingrese_numero(mensaje = None):
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero =    float(
                        input("%s \t"%mensaje)
                    )
    except: 
        numero = ingrese_numero(mensaje)
        
    return numero

def ingrese_texto(mensaje = None):
    texto = ''
    if(mensaje is None):
        mensaje = "Ingrese un texto: "
        
    try:
        texto = raw_input(mensaje + "\t")                    ## esto se usa para string
    except: 
        texto = ingrese_texto(mensaje)
        
    return texto

def notas_alumno():
    notas = []
    for item in range(1,11):
        nota = ingrese_numero("Ingrese una nota (1 -10): ")
        while nota<1 or nota>10:
            print("\nNota fuera de rango\n")
            nota = ingrese_numero("Ingrese una nota (1 -10): ")
            
        notas.append(nota)
        
    return notas

def imprimir_notas(notas):
    print("\n\t-- Notas de Alumno --")
    print("\n\t")
    linea = ''
    for nota in notas:
        linea = linea + '\t'
        linea = linea + str(nota)
        linea = linea + ' - '
        
    print(linea)
    
def promedio_notas(notas):
    promedio = 0
    for nota in notas:
        promedio = promedio + nota
    promedio = promedio / len(notas)
    return promedio

## Inicia programa aca

mensaje_inicio()

notas = notas_alumno()

imprimir_notas(notas)

notas.sort(reverse=False)    

promedio = promedio_notas(notas)

primera = notas[0]

ultima = notas[-1]

print("\n\tNota promedio:  %i "%promedio)

print("\n\tPrimera Nota :  %i "%primera)

print("\n\tUltima Nota :  %i "%ultima)

mensaje_fin()