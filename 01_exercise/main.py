#!/usr/bin/env python3
def mensaje_inicio():
    mensaje = '\nInicio de Programa\n'
    print(mensaje)
    
def mensaje_fin():
    mensaje = '\nFin de Programa\n'
    print(mensaje)
        
def ingrese_numero():
    numero =    int(
                    input("Ingrese un numero: \t")
                )
    return numero

def mayor(primero,segundo):
    respuesta = False
    if(primero>segundo):
        respuesta = True
    return respuesta

## Inicia programa aca

mensaje_inicio()

numero_uno = ingrese_numero()
numero_dos = ingrese_numero()

mayor_primero = mayor(numero_uno,numero_dos)

mensaje_positivo = '\nSi es mayor el primer numero ingresado\n'
mensaje_negativo = '\nNo es mayor el primer numero ingresado\n'

mensaje_numero_ingresado_uno = '\nEl primer numero ingresado es %s \n'%(numero_uno)
mensaje_numero_ingresado_dos = '\nEl segundo numero ingresado es %s \n'%(numero_dos)

print(mensaje_numero_ingresado_uno)
print(mensaje_numero_ingresado_dos)

if(mayor_primero == True):
    print(mensaje_positivo)
else:
    print(mensaje_negativo)
    
    
mensaje_fin()    