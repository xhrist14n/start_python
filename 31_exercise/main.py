#!/usr/bin/env python3
import random 

def mensaje_inicio():
    mensaje = '\nInicio de Programa\n'
    print(mensaje)
    
def mensaje_fin():
    mensaje = '\nFin de Programa\n'
    print(mensaje)
        
def generar_vector(longitud):
    respuesta = []
    for item in range(1,longitud):
        rand = random.randint(0,100)
        respuesta.append(rand)
    return respuesta    

## Inicia programa aca

mensaje_inicio()

vector = generar_vector(100)

print(vector)

mayor = 0
menor = 100000000000000

mayor_posicion = 0
menor_posicion = 0
cont = 0
for item in vector:
    
    if item>mayor:
        mayor = item
        mayor_posicion = cont   
        
    if item<menor:
        menor = item
        menor_posicion = cont
        
    print("Posicion: %s elemento %s\n"%(cont, item))
    
    cont = cont + 1

print("El elemento menor es: %s y su posicion es: %s\n"%(menor, menor_posicion))
print("El elemento mayor es: %s y su posicion es: %s\n"%(mayor, mayor_posicion))

mensaje_fin()    