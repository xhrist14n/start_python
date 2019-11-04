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

def es_mayuscula( letra ):
    respuesta = False
    if(letra.isupper() == True):
        respuesta = True
    return respuesta

## Inicia programa aca

mensaje_inicio()

texto     =   ingrese_texto("Ingrese el texto: ")

letra_mayuscula = False
for letra in texto:
    if(es_mayuscula(letra)==True):
        letra_mayuscula = True

mensaje_mayuscula                 = '\nSi hay una letra mayuscula\n'
mensaje_no_mayuscula              = '\nNo hay una letra mayuscula\n'
mensaje_no_determinado            = '\nNo se puede determinar\n'

mensaje_texto = '\nEl texto ingresado es :  %s \n'%(texto)

print(mensaje_texto)

mensaje_resultado = 'El resultado de la validacion es : \t '

print(mensaje_resultado)

if      (letra_mayuscula == True):
    print(mensaje_mayuscula)
else:
    print(mensaje_no_mayuscula)

mensaje_fin()    