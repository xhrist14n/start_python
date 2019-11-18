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

def ingrese_numero(mensaje = None):
    if(mensaje is None):
        mensaje = "Ingrese un numero: "
        
    try:
        numero =    int(
                        input("%s \t"%mensaje)
                    )
    except: 
        numero = ingrese_numero()
        
    return numero    
        


def es_par( numero ):
    respuesta = False    
    if numero%2==0 :
        respuesta = True
    return respuesta


## Inicia programa aca

mensaje_inicio()

numero_inicio   = ingrese_numero("Ingrese un numero : ")
numero_fin      = ingrese_numero("Ingrese un numero : ")

intercambio = 0

if numero_inicio>numero_fin:
    intercambio = numero_fin
    numero_fin = numero_inicio
    numero_inicio = intercambio 

numero_fin = numero_fin + 1     
    
for item in range(numero_inicio, numero_fin):
    if es_par(item) == True:
        print("\n\t %i "%item)


mensaje_fin()    