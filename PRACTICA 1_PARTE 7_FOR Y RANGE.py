#CAPITULO 29: BUCLE FOR
#46.-Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'.

print("\n\n----Bucle colores----")
colores = ('rojo','azul','verde','amarillo')
for x in colores:
    print(f"el color es: {x}.")

#CAPITULO 30: LA FUNCION RANGE () EN BUCLES
#47.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.

print("\n\n----Bucle con Range()----")
for x in range (7,700,100):
    print(x)