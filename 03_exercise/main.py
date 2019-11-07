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
        
def ingrese_numero():
    try:
        numero =    int(
                        input("Ingrese un numero: \t")
                    )
    except: 
        numero = ingrese_numero()
        
    return numero

def par( numero ):
    respuesta = False
    if(numero%2 == 0):
        respuesta = True
    return respuesta

def impar( numero ):
    respuesta = False
    if(numero%2 == 1):
        respuesta = True
    return respuesta

## Inicia programa aca

mensaje_inicio()

numero = ingrese_numero()

par      = par(numero)
impar    = impar(numero)

mensaje_par                 = '\nSi es un numero Par\n'
mensaje_impar               = '\nNo es un numero Impar\n'
mensaje_no_determinado      = '\nNo se puede determinar\n'

mensaje_numero_ingresado = '\nEl numero ingresado es %s \n'%(numero)

print(mensaje_numero_ingresado)

if      (par == True):
    print(mensaje_par)
elif    (impar == True):
    print(mensaje_impar) 
else:
    print(mensaje_no_determinado)

mensaje_fin()    