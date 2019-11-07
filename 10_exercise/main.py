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
        
def ingrese_numero(mensaje = None):
    numero = 0
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero = float(input(mensaje + "\t"))
    except: 
        numero = ingrese_numero(mensaje)
        
    return numero

def numero_aleatorio():
    numero = 1
    limit = 100    
    numero = random.randint(1,limit)
    return numero

def es_correcto(numero, numero_adivinado):
    respuesta = False
    if numero == numero_adivinado:
        respuesta = True
        
    return respuesta

def es_mayor(numero, numero_adivinado):
    respuesta = False
    if numero < numero_adivinado:
        respuesta = True
        
    return respuesta

def es_menor(numero, numero_adivinado):
    respuesta = False
    if numero > numero_adivinado:
        respuesta = True
        
    return respuesta

## Inicia programa aca

mensaje_inicio()

numero_intentos = 10

numero = numero_aleatorio()

respuesta_incorrecta    = "\nEl numero ingresado no es el correcto"
respuesta_correcta      = "\nEl numero ingresado es correcto"

respuesta_mayor      = "\nEl numero ingresado es mayor al numero a adivinar\n"
respuesta_menor      = "\nEl numero ingresado es menor al numero a adivinar\n"

respuesta_sin_aciertos = "\nNo hubo ningun acierto\n"

respuesta_numero_aciertos = "\nUsted acerto la respuesta en el intento numero: "

numero_intentos_acierto = 0
for cont in range(1,numero_intentos+1):
    numero_adivinado = ingrese_numero("Ingrese Numero posible : ")
    if es_correcto(numero, numero_adivinado):
        numero_intentos_acierto = cont
        print(respuesta_correcta)
        break
    elif es_mayor(numero, numero_adivinado):
        print(respuesta_mayor)
    elif es_menor(numero, numero_adivinado):
        print(respuesta_menor)
    else:
        print(respuesta_incorrecta)
    
if numero_intentos_acierto == 0:
    print(respuesta_sin_aciertos)
else:
    print("\n%s %s\n\n"%(respuesta_numero_aciertos, numero_intentos_acierto))    
    
mensaje_fin()    