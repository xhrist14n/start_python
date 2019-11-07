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
        numero = float(input(mensaje + "\t"))
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

numero = ingrese_numero()

cont = 1

suma = numero

while numero!=0 :
    numero = ingrese_numero()
    suma = suma + numero
    cont = cont+1
    
promedio = suma/cont

mensaje_suma = "\nLa suma de los numeros ingresados es : %s \n"%suma    

mensaje_promedio = "\nEl promedio de los numeros ingresados es : %s \n"%promedio    

print(mensaje_suma)

print(mensaje_promedio)
    
mensaje_fin()    