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
    
def numero_random():
    numero = random.randint(1,10)
    return numero        

def lista_random():
    lista = []
    for i in range(1,11):
        numero = numero_random()
        lista.append(numero)
    return lista
        
## Inicia programa aca

mensaje_inicio()

lista = lista_random()

lista.sort()
    
print(lista)    

mensaje_fin()