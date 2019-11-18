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

## Inicia programa aca

mensaje_inicio()

limite_multiplo = 13
   
for numero in range(1,6):
    multiplicacion = 1
    print("\n\n\tTabla del %i \n\t------------\n"%numero)
    for item in range(1,limite_multiplo):
        multiplicacion = numero * item
        print("\n\t%i * %i = %i"%(numero, item, multiplicacion))    
       
mensaje_fin()