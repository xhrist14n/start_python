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

def aleatorio():
    numero = random.randint(1,10)
    return numero

def lista_aleatorios():
    lista = []
    for item in range(1,11):
        lista.append(aleatorio())
    return lista

def cuadrado(numero):
    return numero**2

def cubo(numero):
    return numero**3



## Inicia programa aca

mensaje_inicio()

aleatorios = lista_aleatorios()

for aleatorio in aleatorios:
    print("\n\t>> Numero: %i Cuadrado: %i Cubo: %i"%(aleatorio, cuadrado(aleatorio), cubo(aleatorio)))           

mensaje_fin()