#Quiero hacer un algoritmo que me convierta un valor de temperatura en una unidad, a otra.
#Es decir, pasar de C° a F° o K.

#PASOS
#1. Indicar la unidad de la temperatura que quiero convertir (En qué unidad entra)
#2. Indicar la unidad de la temperatura a la que quiero convertir (En que unidad sale)
#3. Introducir el valor de mi temperatura. (Entra)
#4. Convertir la temperatura
#5. Imprimirla en pantalla.

import math

#PASO 1: Puse todo junto para que se haga en una sola linea...
itemp_unit = 0
ftemp_unit = 0
while itemp_unit not in ("1","2", "3") or ftemp_unit not in ("1","2", "3"):
    itemp_unit = input("En qué unidad quieres está la temperatura que quieres convertir? (1. C°/2. F°/3. K)\n1. C°\n2. F°\n3. K\n")
    ftemp_unit = input("A qué unidad quieres convertir? (1/2/3)\n1. C°\n2. F°\n3. K\n")
    try:
        temp = float(input("Introduce el valor de tu temperatura sin unidades\n"))
        break
    except ValueError:
        print("Error: solo se aceptan valores reales")
        

    

#PASO 4: voy a utilizar funciones para practicarlas...
def convert_temp():
    if itemp_unit == "1" and ftemp_unit == "2":
        new_temp = (temp*9/5) + 32
        return f"{new_temp}F°"
    elif itemp_unit == "1" and ftemp_unit == "3":
        new_temp = temp + 273.15
        return f"{new_temp}K°"
    elif itemp_unit == "2" and ftemp_unit == "1":
        new_temp = (temp-32)*5/9
        return f"{new_temp}C°"
    elif itemp_unit == "2" and ftemp_unit == "3":
        new_temp = (temp-32)*5/9 + 273.15
        return f"{new_temp}K°"
    elif itemp_unit == "3" and ftemp_unit == "1":
        new_temp = temp - 273.15
        return f"{new_temp}C°"
    elif itemp_unit == "3" and ftemp_unit == "2":
        new_temp = ((temp - 273.15)*9/5)+32
        return f"{new_temp}F°"
    else:
        print("No puedes convertir a la misma unidad...")

print("Tu temperatura es", convert_temp())