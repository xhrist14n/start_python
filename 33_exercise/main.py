#!/usr/bin/env python3
import random
def mensaje_inicio():
    mensaje = '\nInicio de Programa\n'
    print(mensaje)
    
def mensaje_fin():
    mensaje = '\nFin de Programa\n'
    print(mensaje)
        
def generar_codigo():
    letras = 'abcdefghijklmnopqrstuvwxyz'
    codigo = ''
    for item in range(1,8):
        posicion = random.randint(1,len(letras))
        try:
            letra = letras[posicion]
        except:
            posicion = posicion%(len(letras)-1)
            letra = letras[posicion]
            
        codigo = '%s%s'%(codigo, letra)
    return codigo



## Inicia programa aca

mensaje_inicio()

cantidad = 200;

numero_estudiantes_computadoras = random.randint(0, cantidad)

numero_estudiantes_algoritmos = cantidad - numero_estudiantes_computadoras

codigos = []

codigos_computadoras = []
for item in range(1, numero_estudiantes_computadoras):
    codigo = generar_codigo()
    codigos_computadoras.append(codigo)

codigos_algoritmos = []
for item in range(1, numero_estudiantes_algoritmos):
    codigo = generar_codigo()
    codigos_algoritmos.append(codigo)

codigos = codigos_computadoras + codigos_algoritmos

print("\n\tCodigos Computadoras\n")
print(codigos_computadoras)

print("\n\tCodigos Algoritmos\n")
print(codigos_algoritmos)

print("\n\tCodigos\n")
print(codigos)
    
mensaje_fin()    