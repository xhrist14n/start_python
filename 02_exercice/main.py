#!/usr/bin/env python3
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

def positivo( numero ):
    respuesta = False
    if(numero>0):
        respuesta = True
    return respuesta

def negativo( numero ):
    respuesta = False
    if(numero<0):
        respuesta = True
    return respuesta

def cero( numero ):
    respuesta = False
    if(numero==0):
        respuesta = True
    return respuesta

## Inicia programa aca

mensaje_inicio()

numero = ingrese_numero()

positivo    = positivo(numero)
negativo    = negativo(numero)
cero        = cero(numero)

mensaje_positivo    = '\nSi es un numero positivo\n'
mensaje_negativo    = '\nNo es un numero negativo\n'
mensaje_cero        = '\nEl numero ingresado es cero\n'
mensaje_cero        = '\nNo se puede determinar\n'

mensaje_numero_ingresado = '\nEl numero ingresado es %s \n'%(numero)

print(mensaje_numero_ingresado)

if      (positivo == True):
    print(mensaje_positivo)
elif    (negativo == True):
    print(mensaje_negativo) 
elif    (cero == True): 
    print(mensaje_cero) 
else:
    print(mensaje_no_determinado)

mensaje_fin()    