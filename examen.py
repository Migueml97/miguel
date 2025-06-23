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






