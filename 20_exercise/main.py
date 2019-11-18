#!/usr/bin/env python3

## codigo creado por Christian Portilla Pauca
## Website: https://www.christianportilla.com
## Mail: khrist14n@gmail.com

import math

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
        numero =    float(
                        input("%s \t"%mensaje)
                    )
    except: 
        numero = ingrese_numero(mensaje)
        
    return numero


## Inicia programa aca

mensaje_inicio()

interes = float(5)
monto = 0
ahorro = 0

for item in range(1,13):
    monto = ingrese_numero("Ingrese monto ahorrado el mes %i :"%item)
    ahorro = ahorro + monto 
    ahorro = ahorro + ahorro*interes/100

print("\n\t Interes de ahorro en el periodo anual : %f %% "%interes)               
print("\n\t Monto ahorrado en el periodo anual : %f "%ahorro)           

mensaje_fin()