email = input("Introduce tu email: ").lower()
valido = True
caracteres_aceptables = "qwertyuiopasdfghjklzxcvbnmñ.1234567890"

if email.count("@") != 1:
    valido = False
else:
    email_dividido = email.split("@")
    nombre = email_dividido[0]
    dominio = email_dividido[1]
    if len(nombre) == 0:
        valido = False
        if dominio.count(".") != 1:
            valido = False
        else:
            dominio = dominio.split(".")
            if len(dominio) != 2 or len(dominio[0]) == 0 or len(dominio[1]) == 0:
                valido = False
            else:
                for parte in [nombre, dominio[0], dominio[1]]:
                    for caracter in parte:
                        if caracter not in caracteres_aceptables:
                            valido = False
                            break

print("¿Email válido?", valido)

#Quiero que se pregunten notas una a una (tendreis que usar un bucle) y que se vayan guardando, hasta que se introduzca un -1, entonces, quiero que me mostreis las notas, la primera, las tres ultimas, y las que van desde la segunda nota hasta la penultima
notas = []
nota = float(input("Introduce una nota "))

while nota != -1:
    notas.append(nota)
    nota = float(input("Introduce una nota "))

#todas las notas
print(notas)

#primera nota
print(notas[0])

#tres ultimas
if len(notas) >= 3:
    print(notas[-3:])
else:
    print("no hay suficientes notas")

#de la 2 a penultima
print(notas[1:-1])



#Hacer un sistema de base de datos de alumnos, con nombre, edad y cursos en los que estan apuntados

from pprint import pprint
base_datos = {}  # Diccionario principal
id_actual = 1     # Para dar IDs únicos a cada entrada

while True:
    nombre = input("Nombre del alumno (o escribe 'salir' para finalizar la ejecucion): ")
    if nombre.lower() == "salir":
        break

    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    curso = input("Curso: ")
    
    # Recoger notas
    notas = []
    while True:
        nota = input("Introduce una nota (-1 para finalizar la recogida de notas): ")
        if nota == "-1":
            break
        try:
            notas.append(float(nota))
        except ValueError:
            print("Eso no es una nota válida.")

    base_datos[id_actual] = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Curso": curso,
        "Notas": notas
    }
    id_actual += 1

# Mostrar toda la base de datos
pprint("Base de datos completa: ")
for id, datos in base_datos.items():
    print(f"ID {id}: {datos}")


