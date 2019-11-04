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

def es_cero( numero ):
    respuesta = False
    if(numero == 0):
        respuesta = True
    return respuesta

def dividir(numero_uno, numero_dos):
    resultado = 0
    evaluacion = es_cero(numero_dos)
    if(evaluacion == False):
        resultado = numero_uno/numero_dos
    return resultado

## Inicia programa aca

mensaje_inicio()

numero_uno = ingrese_numero()
numero_dos = ingrese_numero()

cero      = es_cero(numero_dos)

mensaje_cero                 = '\nSi es cero\n'
mensaje_no_cero              = '\nNo es cero\n'
mensaje_no_determinado       = '\nNo se puede determinar\n'

mensaje_numero_ingresado_uno = '\nEl primer numero ingresado es %s \n'%(numero_uno)
mensaje_numero_ingresado_dos = '\nEl segundo numero ingresado es %s \n'%(numero_dos)

print(mensaje_numero_ingresado_uno)
print(mensaje_numero_ingresado_dos)

mensaje_resultado = 'El resultado de la division es : \t '

if      (cero == True):
    print(mensaje_cero)
elif    (cero == False):
    print(mensaje_no_cero) 
    resultado = dividir(numero_uno, numero_dos)
    mensaje_resultado = '\n %s %s \n'%(mensaje_resultado,resultado)
    print(mensaje_resultado)
else:
    print(mensaje_no_determinado)

mensaje_fin()    