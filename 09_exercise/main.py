#!/usr/bin/env python3
## codigo creado por Christian Portilla Pauca
## Website: https://www.christianportilla.com
## Mail: khrist14n@gmail.com

def mensaje_inicio():
    mensaje = '\nInicio de Programa\n'
    print(mensaje)
    
def mensaje_fin():
    mensaje = '\nFin de Programa\n'
    print(mensaje)
        
def ingrese_texto(mensaje = None):
    texto = ''
    if(mensaje is None):
        mensaje = "Ingrese un texto: "
        
    try:
        texto = raw_input(mensaje + "\t")                    ## esto se usa para string
    except: 
        texto = ingrese_texto(mensaje)
        
    return texto

def ingrese_numero(mensaje = None):
    numero = 0
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero = float(input(mensaje + "\t"))
    except: 
        numero = ingrese_numero(mensaje)
        
    return numero

def factorial(numero):
    if numero == 1:
        return numero
    return numero*factorial(numero-1)

## Inicia programa aca

mensaje_inicio()

numero     =   ingrese_numero("Ingrese un numero: ")

respuesta = factorial(numero)


mensaje_resultado = '\nEl resultado es : \t \n\t'

print(mensaje_resultado)

print(respuesta)

mensaje_fin()    