#EJERCICIOS CAPITULO 27: BUCLE WHILE
#42.- CREA UN BUCLE WHILE QUE SE EJECUTE HASTA QUE X VAGA 15 CON INCREMENTOS DE 5
#43.- CREA UN BUCLE WHILE QUE SE EJECUTE HASTA QUE X VALGA -100 CON INCREMENTOS DE 20
#44.- CREA IN BUCLE WHILE QUE SE EJECUTE HASTA QUE X VALGA  CON DECTREMENTOS DE 1

print("\n----------Bucle de 0 a  15----------")
x = 0
while x<=15:
     print(f"El valor de x en el bucle es: {x}")
     x+=1

print("\n----------Bucle de 0 a -100----------")
x = 0
while x >= -100:
    print(f"El valor de x en el bucle es: {x}")
    x -= 20

print("\n----------Bucle de 10 a 0----------")
x = 10
while x >= 0:
    print(f"El valor de x en el bucle es: {x}")
    x -= 1

#EJERCICIO CAPITULO 28 EL BUCLE WHILE CON CONDICIONAL IF
# 45.- Crea un bucle while con las siguientes características:
# El valor inicial de la variable x será de 0.
# El valor de incremento será 1.
# La condición de salida del bucle será mayor o igual a 30.
# La ejecución se deberá romper cuando x valga 15.
# Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
# Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
# En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
# Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.

print("\n\n\n----------Bucle de 0 a 30 con saltos----------")
x = 0
while x <= 30:
    x += 1
    if x == 4 or x == 6 or x ==10:
        print(f"----Se salto el valor de {x}----")
        continue
    elif x == 15:
        print(f"Se rompio la ejecucion del bucle cuando x valia: {x}")
        break
    else:
        print(f"El valor de x en el bucle es: {x}")
  