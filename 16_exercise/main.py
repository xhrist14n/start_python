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

## Inicia programa aca

mensaje_inicio()

limite_inferior  = ingrese_numero("Ingrese limite inferior : ")
limite_superior  = ingrese_numero("Ingrese limite superior : ")

while limite_inferior>limite_superior:
    limite_inferior  = ingrese_numero("Ingrese limite inferior : ")

numero = ingrese_numero("ingrese numero: ")
lista = [ numero ]
while numero != 0:
    numero = ingrese_numero("ingrese numero: ")
    lista.append( numero )

suma = 0    
cont = 0 

mensaje = ""

for item in lista:
    if item >= limite_inferior and item <= limite_superior :
        suma = suma + item
        if item == limite_inferior:
            mensaje = mensaje + "\n\t El numero "+str(item)+" es igual al limite del intervalo inferior"
        if item == limite_superior:
            mensaje = mensaje + "\n\t El numero "+str(item)+" es igual al limite del intervalo superior"
    else:
       cont = cont + 1 
       
print( "\n\t La suma de los numeros que estan dentro del intervalo es : %i "%(suma) )       

print( "\n\t Los numeros que estan fuera del intervalo son : %i "%(cont) )       

print(mensaje)
       
mensaje_fin()