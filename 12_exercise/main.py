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
    numero = 0
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero = int(input(mensaje + "\t"))
    except: 
        numero = ingrese_numero(mensaje)
        
    return numero

def numero_aleatorio():
    numero = 1
    limit = 100    
    numero = random.randint(1,limit)
    return numero

def es_cero(numero):
    respuesta = False
    if numero == 0:
        respuesta = True
        
    return respuesta


## Inicia programa aca

mensaje_inicio()

cantidad = ingrese_numero("Ingrese la cantidad de numeros a ingresar: ")

cantidad_ceros = 0
cantidad_mayor = 0
cantidad_menor = 0

for cont in range(1,cantidad+1):
    numero = ingrese_numero()
    if numero == 0:
        cantidad_ceros = cantidad_ceros + 1
    elif numero > 0:
        cantidad_mayor = cantidad_mayor + 1
    elif numero < 0:
        cantidad_menor = cantidad_menor + 1        
    else: 
        cantidad_no_determinados = cantidad_no_determinados + 1

mensaje_mayores = "\nLa cantidad de numeros mayores que cero son : %s \n"%cantidad_mayor    

mensaje_menores = "\nLa cantidad de numeros menores que cero son : %s \n"%cantidad_menor

mensaje_ceros = "\nLa cantidad de numeros iguales a cero son : %s \n"%cantidad_ceros


print(mensaje_mayores)

print(mensaje_menores)

print(mensaje_ceros)
    
mensaje_fin()    