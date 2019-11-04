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

def es_positivo( numero ):
    respuesta = False
    if(numero>0):
        respuesta = True
    return respuesta

def es_negativo( numero ):
    respuesta = False
    if(numero<0):
        respuesta = True
    return respuesta

def es_cero( numero ):
    respuesta = False
    if(numero == 0):
        respuesta = True
    return respuesta

## Inicia programa aca

mensaje_inicio()

base            =   ingrese_numero("Ingrese la base: ")
exponente       =   ingrese_numero("Ingrese el exponente: ")

positivo = es_positivo(exponente)
negativo = es_negativo(exponente)
cero = es_cero(exponente)


mensaje_resultado = 'El resultado de la exponenciacion es : \t '

print(mensaje_resultado)

mensaje_resultado_no_conocido = 'No se puede llegar a un resultado determinado'

if      positivo == True:
    potencia = pow(base, exponente)
elif    negativo == True:
    exponente = (-1)*exponente
    potencia = pow( (1/base), exponente)
elif    cero == True:
    potencia = 1
else:
    potencia = mensaje_resultado_no_conocido
    
print( "Potencia :  %06.10f "%(potencia))

mensaje_fin()    