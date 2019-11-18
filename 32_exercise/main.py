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

## Inicia programa aca

mensaje_inicio()

cantidad = 100

lista = []

suma_pares = 0
suma_impares = 0

elemento = 0

for numero in range(1,cantidad):
    elemento = random.randint(0,1000)
    if numero%2==0:    
        suma_pares = suma_pares + elemento
    else:
        suma_impares = suma_impares + elemento
        
    lista.append(elemento)
    
print("La lista de numeros es :\n")    
print(lista)

print("\n\n")

print("La suma de las posiciones pares es : %s "%(suma_pares))
print("La suma de las posiciones impares es : %s "%(suma_impares))


mensaje_fin()    
