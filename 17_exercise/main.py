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
        numero =    float(
                        input("%s \t"%mensaje)
                    )
    except: 
        numero = ingrese_numero()
        
    return numero

def exponencial(base, exponente):
    multiplicacion = 1
    for item in range(0, int(exponente)):
        multiplicacion = multiplicacion * base
    return multiplicacion
## Inicia programa aca

mensaje_inicio()

base        = ingrese_numero("Ingrese la base: ")
exponente   = ingrese_numero("Ingrese exponente : ")

exponenciacion = exponencial(base, exponente)

print("\n\t %f ^ %f = %f "%(base, exponente, exponenciacion))
       
mensaje_fin()