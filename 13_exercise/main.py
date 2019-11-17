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
        
def ingrese_texto(mensaje = None):
    texto = ''
    if(mensaje is None):
        mensaje = "Ingrese un texto: "
        
    try:
        texto = raw_input(mensaje + "\t")                    ## esto se usa para string
    except: 
        texto = ingrese_texto(mensaje)
        
    return texto

def es_vocal( letra ):
    letras_vocales = 'aeiou'
    respuesta = False
    for letra_vocal in letras_vocales:
        if(letra == letra_vocal):
            respuesta = True
    return respuesta

def es_no_vocal( clave ):
    letras_vocales = 'asdasd'
    respuesta = True
    for letra_vocal in letras_vocales:
        if(letra == letra_vocal):
            respuesta = False
    return respuesta

## Inicia programa aca

mensaje_inicio()

usuario     =   ingrese_texto("Ingrese el usuario: ")
clave       =   ingrese_texto("Ingrese la clave: ")

usuario_validado    = es_usuario(usuario)
clave_validada      = es_clave(clave)

mensaje_validado                 = '\nSi es un usuario valido\n'
mensaje_no_validado              = '\nNo es un usuario valido\n'
mensaje_no_determinado           = '\nNo se puede determinar\n'

mensaje_usuario = '\nEl usuario ingresado es %s \n'%(usuario)
mensaje_clave = '\nLa clave ingresada es %s \n'%(clave)

print(mensaje_usuario)
print(mensaje_clave)

mensaje_resultado = 'El resultado de la validacion es : \t '

print(mensaje_resultado)

if      (usuario_validado == True and clave_validada==True):
    print(mensaje_validado)
else:
    print(mensaje_no_validado)

mensaje_fin()    