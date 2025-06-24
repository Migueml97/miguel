#funciones
def mi_nombre():
    print("Miguel")

mi_nombre()

#funcion no muda
def nombre():
    mi_nombre = input("Introduce tu nombre").upper()
    return mi_nombre

yo = nombre()
print(yo)

#Haced una funcion que le de dos colores de la escala cromatica (rojo, verde o azul) y me devuelva su mexcla
 
color_1 = input("Introduce un color(rojo, azul o verde)")
color_2 = input ("Introduce otro color(rojo, azul o verde)")

def mezcla(color_1, color_2):
    valido = True
    if color_1 == "rojo" and color_2 == "azul":
        mezcla_1 = "Magenta"
    elif color_1 == "rojo" and color_2 == "verde":
        mezcla_1 = "Amarillo"
    elif color_1 == "azul" and color_2 == "verde":
        mezcla_1 = "Cian"
    if color_2 == "rojo" and color_1 == "azul":
        mezcla_1 = "Magenta"
    elif color_2 == "rojo" and color_1 == "verde":
        mezcla_1 = "Amarillo"
    elif color_2 == "azul" and color_1 == "verde":
        mezcla_1 = "Cian"
    else:
        valido = False
    if valido == True:
        return mezcla_1
    else:
        return valido == False

color = mezcla(color_1, color_2) 
if mezcla(color_1, color_2) == False:
    print("No has introducido colores correcto")
else:
    print(f"Tu mezcla es: {color}")
    


#copiado
def mezclar_colores(color1, color2):
    colores_primarios = {'rojo', 'verde', 'azul'}
    
    if color1 not in colores_primarios or color2 not in colores_primarios:
        return "Colores no válidos. Deben ser rojo, verde o azul."
    
    if color1 == color2:
        return f"El color resultante es {color1}."
    
    mezclas = {
        ('rojo', 'verde'): 'amarillo',
        ('rojo', 'azul'): 'morado',
        ('verde', 'azul'): 'cian',
        ('verde', 'rojo'): 'amarillo',
        ('azul', 'rojo'): 'morado',
        ('azul', 'verde'): 'cian'
    }

    return mezclas.get((color1, color2), mezclas.get((color2, color1), "Mezcla no definida."))
    
    

if __name__ == "__main__":

    # Ejemplo de uso
    print(mezclar_colores('rojo', 'verde'))  # Debería devolver 'amarillo'
    print(mezclar_colores('rojo', 'azul'))    # Debería devolver 'morado'
    print(mezclar_colores('verde', 'azul'))   # Debería devolver 'cian'
    print(mezclar_colores('rojo', 'rojo'))    # Debería devolver 'El color resultante es rojo.'
    print(mezclar_colores('amarillo', 'azul'))  # Debería devolver 'Colores no válidos. Deben ser rojo, verde o azul.'

#calculadora
from functools import reduce
import operator
def suma(numeros):
    return sum(numeros)

def resta(numeros):
    return reduce(operator.sub, numeros)

def multiplicacion(numeros):
    return reduce(operator.mul, numeros)

def division(numeros):
    try:
        return reduce(operator.truediv, numeros)
    except ZeroDivisionError:
        return "Error"

tipo = input("Introduce el tipo de cuenta que quieres(suma, resta, multiplicacion, division)")
numeros = []
valido = True

print("Introduce números uno por uno. Escribe -1 para terminar:")

while True:
    entrada = int(input("Introduce numeros "))
    if entrada == -1:
        break
    numeros.append(entrada)

def calculadora(tipo, numeros):
    if tipo == "suma":
        return suma(numeros)
    elif tipo == "resta":
        return resta(numeros)
    elif tipo == "multiplicacion":
        return multiplicacion(numeros)
    elif tipo == "division":
        return division(numeros)
    else:
        valido = False
        return valido

resultado = calculadora(tipo, numeros)
print(f"la cuenta de los numeros es: {resultado}")
