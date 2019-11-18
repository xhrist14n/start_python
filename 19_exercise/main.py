#!/usr/bin/env python3

## codigo creado por Christian Portilla Pauca
## Website: https://www.christianportilla.com
## Mail: khrist14n@gmail.com

import math

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
        numero = ingrese_numero()
        
    return numero

def es_primo(numero):
    limite = int(math.sqrt(numero) + 1)
    respuesta = True
    for item in range(2, limite):
        if numero%item == 0:
            respuesta = False
    return respuesta

## Inicia programa aca

mensaje_inicio()

numero = ingrese_numero()

if es_primo(numero):
    print("\n\tEl numero %i es primo"%numero)
else:
    print("\n\tEl numero %i no es primo"%numero)
       
mensaje_fin()