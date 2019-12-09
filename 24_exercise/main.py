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


## Inicia programa aca

mensaje_inicio()

lista = [] 


numero = ingrese_numero()
if numero>=0:
    lista.append(numero)
while numero >= 0 :
    numero = ingrese_numero()
    if numero>=0:
        lista.append(numero)
    
print(lista)    

mensaje_fin()