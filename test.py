nombre = "miguel"
print(nombre)

n1 = 10
n2 = 40
print(n1+n2)

n1 = 10
n2 = 40
print(n1//n2) #devuelve el resultado sin decimales

n1 = 10
n2 = 40
print(n1%n2) #devuelve el modulo (para ver si es par o impar)

n1 = int(input("Dame un numero "))
n2 = int(input("Dame otro numero "))
print("La suma es ", n1+n2)

#ejercicio 1 filtro de palabrotas
import random
mensaje = input("Introduce un mensaje ").lower()
palabras = mensaje.split(" ")
mapa_palabrotas = {
    "idiota": ["#", "$"],
    "tonto": ["#", "$"],  
    "imbecil": ["#", "$"]
}
for palabrota in palabras:
    if palabrota in mapa_palabrotas.keys():
        mensaje = mensaje.replace(palabrota, random.choice((mapa_palabrotas[palabrota])))

print(mensaje)

#ejercicio2 - calculadora de nota media 
import statistics
notas = (3, 8, 6, 2, 5)
media = statistics.mean(notas)
print(media)

#todos los nombres a minusculas
nombres = ["Miguel", "JavIER", "AnA"]
names = []
for palabra in nombres:
    names.append(palabra.lower())
print(names)
