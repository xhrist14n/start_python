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

def ingrese_numero(mensaje = None):
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero =    int(
                        input("%s \t"%mensaje)
                    )
    except: 
        numero = ingrese_numero()
        
    return numero

## Inicia programa aca

mensaje_inicio()

numero   = ingrese_numero("Ingrese un numero : ")

multiplo = 13 ## limite de multiplicacion
    
for item in range(1, multiplo):
    multiplicacion = numero * item
    print("\n\t%i * %i = %i"%(numero, item, multiplicacion))

mensaje_fin()    