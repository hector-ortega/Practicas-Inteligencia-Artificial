#EJERCICIOS CAPITULO 21: coNDICIONAL IF Y OPERADORES DE COMPARACION

#EJERCICIO 36
num_1 = 32
num_2 = 32

if num_1 == num_2: # == hace la comparacin entre los dos numeros y se ejecuta el if si los numeros son iguales
    print('Se ejecuta el if')

#EJERCICIO 37
num_1 = 250
num_2 = 12

if num_2 < num_1: # se ejecuta el if si el num_2 es menor al numero uno
    print('se ejecuta el if')

#EJERCICIO 38
num_1 = 12
num_2 = 32

if num_1 != num_2: #SE EJECUTA EL IF SI EL NUMERO 1 ES DIFERENTE AL NUMERO 2
    print('se ejecuta el if')

#EJERCICIOS CAPITULO 22: EL CONDICIONAL IF ELSE

#Ejercicio 39 CORREGIR EL CONDICIONAL IF ELSE
color ='rojo'
if color == 'rojo':
    print("EL color es rojo")
else:
    print('El color no es rojo')

#EJERCICIOS CAPITULO 23: EL CONDICIONAL IF ELIF ELSE E INPUT, ENTRADA DE DATOS

edad = int(input('introduce tu edad\n'))
if edad <= 0:
    print("jaja todavia no naces o que?\nfavor de introducir tu verdadera edad.\n")
elif edad >= 1 and edad <= 18:
    print('Eres menor de edad')
elif edad >= 18 and edad <= 45:
    print('Eres adulto')
elif edad >= 45 and edad <= 100:
    print("Eres un adulto mayor")
elif edad >100 and edad <=120:
    print("!impresionante que hayas vivido tantos años")
else: 
    print("Edad no valida.")