#clase mascota e instancia
class mascota:
    def __init__(self, nombre: str | None = None,
                  raza: str | None = None,
                    edad: int | None = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        print(f"tu mascota se llama {self.nombre}, tiene {self.edad} años y es su raza es {raza}")

Fideo = mascota("Fideo", "gato", 5)
Luna = mascota("Luna", "perro", 7)

print(Fideo)
print(f"tu mascota se llama {Fideo.nombre} y tiene {Fideo.edad} años")
print(f"tu mascota se llama {Luna.nombre} y su raza es {Luna.raza}")

#mas correcto
###
class animal:
    def __init__(self, nombre: str, edad: int):
        self.nombre = ""
        self.edad = ""

    def datos(self, nombre, edad):
        self.nombre = "fideo"
        self.edad = 5
###
#Combate 
class pelea:
    def __init__(self, nombre: str, tipo: str, ataque: str, vida: int, daño: int):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque_basico = ataque
        self.vida = vida
        self.daño = daño

    def atacar(self, objetivo: object):
        objetivo.vida -= self.daño
        print(f"{self.nombre} ataca a {objetivo.nombre} ")

personaje_1 = pelea("Goku", "luchador", "ataque_basico", 100, 15)
personaje_2 = pelea("Vegeta", "luchador", "ataquebasico", 150, 10)

print(personaje_1.vida, personaje_1.daño)
print(personaje_2.vida, personaje_2.daño)

personaje_1.atacar(personaje_2)
print(personaje_1.daño)
print(personaje_2.vida)
personaje_2.atacar(personaje_1)
print(personaje_2.daño)
print(personaje_1.vida)

###
class Combatientes:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, otro):
        damage = max(0, self.ataque - otro.defensa)
        otro.vida -= damage
        return damage

    def esta_vivo(self):
        return self.vida > 0
    
class Combate:
    def __init__(self, combatiente1, combatiente2):
        self.combatiente1 = combatiente1
        self.combatiente2 = combatiente2

    def iniciar(self):
        print(f"El combate a comenzado entre {self.combatiente1.nombre} y {self.combatiente2.nombre}...")
        while self.combatiente1.esta_vivo() and self.combatiente2.esta_vivo():
            damage1 = self.combatiente1.atacar(self.combatiente2)
            print(f"{self.combatiente1.nombre} ataca a {self.combatiente2.nombre} causando {damage1} de daño.")
            print(f"Vida restante de {self.combatiente2.nombre}: {self.combatiente2.vida}")
            if not self.combatiente2.esta_vivo():
                print(f"{self.combatiente1.nombre} ha salido victorioso.")
                break
            
            damage2 = self.combatiente2.atacar(self.combatiente1)
            print(f"{self.combatiente2.nombre} ataca a {self.combatiente1.nombre} causando {damage2} de daño.")
            print(f"Vida restante de {self.combatiente1.nombre}: {self.combatiente1.vida}")
            if not self.combatiente1.esta_vivo():
                print(f"{self.combatiente2.nombre} ha salido victorioso.")
                break

print ("Bienvenido al combate del siglo!")
boxeador1 = Combatientes("Poli Díaz", 100, 20, 8)
boxeador2 = Combatientes("Pernell Whitaker", 80, 15, 9)
combate = Combate(boxeador1, boxeador2)
combate.iniciar()
###

#una persona que conduce un coche con pasajeros
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def conducir(self, coche, pasajeros):
        print(f"{self.nombre} está conduciendo un {coche.marca}")
        print(f"Los pasajeros son:")
        for pasajero in pasajeros:
            print(pasajero.nombre)

coche1 = Coche("Volkswagen", "negro")      
persona1 = Persona("Alex")
persona2 = Persona("Roberto")
persona3 = Persona("Carlos")
persona4 = Persona("Pedro")
persona1.conducir(coche1, [persona2, persona3, persona4])

#otro
class Coche:
    def __init__(self, marca : str, modelo : str, plazas : int =5, conductor: str =None):
        self.marca=marca
        self.modelo= modelo
        self.plazas= plazas
        self.conductor=conductor

        print(f"Has inscrito el coche {self.marca} {self.modelo} y tiene {self.plazas} plazas")
class Personas:
    def __init__(self, nombre:str, ocupacion : str):

        self.nombre= nombre
        self.ocupacion=ocupacion
        print(f"Has inscrito a {self.nombre} y será {self.ocupacion}")

coche1=Coche("Skoda", "Fabia")
persona1=Personas("David", "Conductor")
persona2=Personas("Laura","Pasajero")

def conducir(persona,coche):
    if coche.conductor == None:
        if persona.ocupacion == "Conductor":
            coche.conductor = persona.nombre
            coche.plazas -=1
            print(f"{persona.nombre} está conduciendo el coche {coche.marca}")
        else:
            print(f"{persona.nombre} no puede conducir porque no es conductor")
    else:
        print("Ya hay un conductor")
conducir(persona1,coche1)

print(f"Ahora hay un total de {coche1.plazas} plazas y lo conduce {coche1.conductor}")

#clase con alumnos, clase es class y alumnos dataclass
import dataclasses

# Clase TajamarAlumno dataclass

@dataclasses.dataclass
class TajamarAlumno:
    nombre: str
    edad: int
    curso: str = "Python"

    def estudiar(self):
        print(f"{self.nombre}, de edad {self.edad} años, está estudiando en el curso {self.curso}.")

# Clase TajamarAlumno sin dataclass
import dataclasses

# Clase TajamarAlumno dataclass

@dataclasses.dataclass
class TajamarAlumno:
    nombre: str
    edad: int
    curso: str = "Python"

    def estudiar(self):
        print(f"{self.nombre}, de edad {self.edad} años, está estudiando en el curso {self.curso}.")

# Clase TajamarAlumno sin dataclass
class TajamarAlumnoNoDataClass:
    def __init__(self, nombre: str, edad: int, curso: str = "Python"):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre}, de edad {self.edad} años,está estudiando en el curso {self.curso}.")



alumno1 = TajamarAlumno(nombre="Pedro", edad=22)
alumno1.estudiar()

alumno2 = TajamarAlumnoNoDataClass(nombre="Belén", edad=25)
alumno2.estudiar()

#otro
import dataclasses

# Dataclass
@dataclasses.dataclass
class Alumno():  # dataclass!
    edad: int
    nombre: str = ""

    def preguntar(self):
        pass

    def entregar_ejerciio(self):
        pass

class Curso:
    def __init__(self,titulo,alumnos:list[Alumno]):
        self.titulo = titulo
        self.alumnos  = alumnos

    def listar_alumnos(self):
        for alumno in alumnos:
            print (alumno)



alejandro = Alumno(23,"Alejandro")
lorenzo = Alumno(43,"Lorenzo Silva")
alumnos = [alejandro, lorenzo]
curso_Tajamar = Curso("Python",alumnos)

curso_Tajamar.listar_alumnos()

 