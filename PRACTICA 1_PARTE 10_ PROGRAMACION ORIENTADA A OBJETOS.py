#En este es un ejercicio propouesto que comprende los capitulos del 37 al 46
import math
import datetime

def area_circulo(radio):
    area = math.pi * radio * radio # <-- Se crea la funcion lambda y se importa el modulo math (Capitulo 44)
    return area


global Escuela #<-- Se declara la variable global del nombre de la escuela de los alumnos (Capitulo 43)
Escuela = 'CETI Colomos'

class Alumno: # <--- Se crea una superclase (capitulo 37)

    def __init__(self, nombre, registro, semestre_grupo, numero_lista): #<--- se agrega el metodo init (capitulo 38)
        self.nombre = nombre
        self.registro = registro
        self.semestre_grupo = semestre_grupo
        self.numero_lista = numero_lista

    def imprime_datos_alumno(self):
        print('\nNombre: ', self.nombre, '\nRegistro: ', self.registro , '\nSemstre y grupo: ', self.semestre_grupo, '\nNumero de lista: ', self.numero_lista, "\nUniversidad: ", Escuela)

class Tipo_Alumno(Alumno): #<--- Se crea una subclase que hereda de la superclase (capitulo 41)
    def __init__(self,nombre, registro, semestre_grupo, numero_lista ,tipo): # <--- Se heredan los atributos de la suberclase en el metodo init (capitulo 42)
        self.tipo = tipo
        self.nombre = nombre
        self.registro = registro
        self.semestre_grupo = semestre_grupo
        self.numero_lista = numero_lista

    def imprime_datos_tipo(self):
        print('\nNombre: ', self.nombre, '\nRegistro: ', self.registro , '\nSemstre y grupo: ', self.semestre_grupo, '\nNumero de lista: ', self.numero_lista, '\nTipo de Alumno: ', self.tipo, "\nUniversidad: ", Escuela)

alumno_1 = Alumno('', 0 , '' , 0 )
# Se modifican los atributos del objeto alumno_1 (capitulo 39)
fecha = datetime.datetime.now()
print("Hoy estamos a la fecha de:")     
print(fecha.strftime("%c")) #<-- Se muestre la fecha actual (Capitulo 45 y 46)

alumno_1.nombre = input("\nCual es tu nombre: ")
alumno_1.registro = int(input("Cual es tu registro: "))
alumno_1.semestre_grupo = input("Cual es tu semestre y grupo: ")
alumno_1.numero_lista = 27

alumno_1.imprime_datos_alumno()

alumno_2 =Alumno('Augusto Ortiz', 123586 , '5A', 37 )
alumno_2.imprime_datos_alumno()
del alumno_2 #<--- se elimina el alumno 2 (Capitulo 40)

alumno_t1 = Tipo_Alumno('Carlos Ortega', 154235, '9h', 33,"Tecnologo")
alumno_t1.imprime_datos_tipo()


print("\nVamos a calcular el area de un circulo: ")
radio_cir = int(input("Dame el radio del circulo:"))
area_cir = area_circulo(radio_cir)
print(f"El Area del circulo es {area_cir}")

