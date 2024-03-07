#CAPITULO 34: COMO CREAE Y LLAMAR FUNCIONES EN PYTHON
#51.- Crea una función que realice una suma. Para ello, tendrás que añadir dos argumentos(numero1 y numero2). En su interior, especificarás un print() que muestre el resultado de la suma. Deberás hacer tres llamadas que como resultado de la suma den los valores 30, 50 y 57000. Los números que introduzcas en la llamada pueden ser los que quieras siempre que coincidan los resultados en el print().

def suma(num_1, num_2):
    resultado = num_1 + num_2
    print(f"El resultado de la suma es: {resultado}")

suma(15,15)
suma(30,20)
suma(50000,7000)

#CAPITULO 35: ARGUMENTOS ARBITRARIOS

def colores(*args):#<- Ejercicio 52
    print(len(args))

def color_fav(*args): #<-- Ejercicio 53
    print('\nEl color', args[1], 'Es mi favorito.', 'El color', args[0], 'tampoco esta mal.')

def suma(*args): #<-- Ejercicio 54
    resultado = args[0] +args[1] + args[2] + args[3] + args[4]
    print(f"\nEl resultado de la suma es: {resultado}")

#CAPITULO 36 ** KWARGS
def figura(**kwargs): # <-- EJERCICIO PROPUESTO DEL CAPITULO 36
    print("Esta es la figura " + kwargs['figura1'])

print("\nArgumentos de la llamada no 1: ")
colores('rojo','azul','verde','amarillo')

print("Argumentos de la llamada no 2: ")
colores('lila','negro','rojo')

print("Argumentos de la llamada no 3: ")
colores('rosa')

print("Argumentos de la llamada no 2: ")
colores('marron','naranja')

color_fav("rojo", "negro")

suma(20,6,78,10,3)

figura(figura1 = 'Rombo', figura2 = 'Circulo')