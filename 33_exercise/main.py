#!/usr/bin/env python3
def mensaje_inicio():
    mensaje = '\nInicio de Programa\n'
    print(mensaje)
    
def mensaje_fin():
    mensaje = '\nFin de Programa\n'
    print(mensaje)
        
def ingrese_texto(mensaje = None):
    texto = ''
    if(mensaje is None):
        mensaje = "Ingrese un texto: "
        
    try:
        texto = raw_input(mensaje + "\t")                    ## esto se usa para string
    except: 
        texto = ingrese_texto(mensaje)
        
    return texto

def ingrese_numero(mensaje = None):
    numero = 0
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero = float(input(mensaje + "\t"))
    except: 
        numero = ingrese_numero(mensaje)
        
    return numero

def es_nota_valida( nota ):
    respuesta = False
    if(nota >= 5):
        respuesta = True
    return respuesta

def es_edad_valida( edad ):
    respuesta = False
    if(edad >= 18):
        respuesta = True
    return respuesta

def es_femenino( sexo ):
    respuesta = False
    if(sexo == 'F'):
        respuesta = True
    return respuesta

def es_masculino( sexo ):
    respuesta = False
    if(sexo == 'M'):
        respuesta = True
    return respuesta

## Inicia programa aca

mensaje_inicio()

nota     =   ingrese_numero("Ingrese la nota: ")
edad       =   ingrese_numero("Ingrese la edad: ")
sexo       =   ingrese_texto("Ingrese su sexo(M/F): ")


nota_valida = es_nota_valida(nota)
edad_valida = es_edad_valida(edad)
femenino = es_femenino(sexo)
masculino = es_masculino(sexo)

mensaje_validado                 = '\nACEPTADA\n'
mensaje_no_validado              = '\nNO ACEPTADA\n'
mensaje_posible                  = '\nPOSIBLE\n'
mensaje_no_determinado           = '\nNo se puede determinar\n'

mensaje_resultado = '\nEl resultado es : \t '

print(mensaje_resultado)

if      nota_valida == True and edad_valida==True:
    if femenino == True:
        print(mensaje_validado)
    elif masculino == True:
        print(mensaje_posible)
    else:
        print(mensaje_no_determinado)            
else:
    print(mensaje_no_validado)

mensaje_fin()    