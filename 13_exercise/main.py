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

def es_no_vocal( letra ):
    letras_vocales = 'aeiou'
    respuesta = True
    for letra_vocal in letras_vocales:
        if(letra == letra_vocal):
            respuesta = False
    return respuesta

def ingreso_letra():
    letra = ingrese_texto('Ingrese Un Caracter')
    while len(letra)>1:
        letra = ingrese_texto('Ingrese Un Caracter')
    
    vocal = es_vocal(letra)
    if vocal == True:
        print('Es Vocal')
    else:
        print('No es Vocal')
    return letra    

## Inicia programa aca

mensaje_inicio()

letra = ingreso_letra()

while letra == ' ':
    letra = ingreso_letra()

mensaje_fin()    