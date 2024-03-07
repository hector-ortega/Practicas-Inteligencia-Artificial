#Problema del capidulo dos

# 1.- Escribe un mensaje en una variable que ´puedes llamar como quieras.
# 2.- Crea dos variables y almacena en ellas un numero.
# 3.- Sumar las dos variables del ejercicio anterior y guarda el resultado de esta suma en una tercera variable.
# 4.- Imprimir el valor de la variable del resultado.

#Problemas del capitulo 3

# 5.- Escribe dos variables con strings. Uno con comillas simples '' y otro con comillas dobles ""
# 6.- Almacena literalmente  esta frase en una variable e imprimela "print()" se utiliza para imprimir valores en la consola

#Problemas capitulo 4

# 7.- Concatena dos strings en una variable. Puedes comprobar el resultado con un print()
# 8.- Concatena dos variables con strings en una tercera variable.
# 9.- Concatena una variable con string directamente en un print()
# 10.- Escribe tu nombre y apellidos separados en variables. Despues concatena estas variables dentro de otra e imprime el resultado.
# 11.- Concatena dos numeros, no los sumes.

#Problemas capitulo 5

# 12.- Pon en mayusculas la primera letra de cada palabra de este nombre utilizando uno de los metodos del capitulo
# 13.- Deja esta frase totalmente en letras minusculas utilizando uno de los metodos del capitulo
# 14.- Deja esta frase totalmente en letras maysculas. 

#Problemas Capitulo 6

# 15.- Escribe contenido en un solo string, se deben utilizar saltos de linea y al final añade dos lenguajes mas. ademas añadir un quin al principio de cada fula y punto final

# Ejercicios capitulo 7

# 16.- Almacena en una variable una suma que de como resultado el número 87. Es obligatorio incluir en dicha suma los números 20 y 23.
# 17.- Almacena en una variable una resta que de como resultado el número negativo -87. Es obligatorio incluir en dicha resta los números positivos 20 y 23.
# 18.- Almacena en una variable una multiplicación que de como resultado el número 870. Es obligatorio incluir en dicha multiplicación los números 20 y 23.
# 19.- Almacena en una variable una división que de como resultado el número 10 (no hace falta que sea 10 exacto, puede tener decimales). Es obligatorio incluir en dicha división los números 5000 y 230.
# 20.- A la siguiente operación añade los símbolos aritméticos básicos (+, -, *, /). Debes utilizar los cuatro sin repertirlos. Uno para cada espacio:
# operacion = 10 __ 5 __ 15 __ 17

# Ejercicios capitulo 8

# 21.- Utilizando solo el numero 2  y sin utilizar exponentes, debes de obtener el resultado 1024

#Ejercicios capidulo 9

# 22.- Redondea a cinco decilares un numero float

titulo = "-----esta es la primer practica del curso de IA-----\n".title()
nombre = "Nombre: Hector"
nombre_dos = " Alejandro"
apellido_uno = " Ortega"
apellido_dos = " Garcia\n"

msj_bienvenida = "Hola mundo!!! \n".upper() #<-- mensaje hecho con doble ""

msj_dos = '"print()" se utiliza para imprimir valores en la consola, pore ejemplo: el mensaje que estas leyendo\n'#<-- mensaje hecho con '' simple
msj_expl = "En este programa veremos las operaciones aritmeeticas basicas con Python:\n\tSuma\n\tResta\n\tMultiplicacion\n\tDivision\n"

msj_concat_sum = "1.-se van a sumar " + "Los numeros: 20, 23, 44"
msj_res = "\n2.-Se van a restar" + "Los numeros: 20, 23, 44"
msj_mult = "\n3.-Se van a multiplicar" + " Los numeros: 147 * 5"
msj_div = "\n4.-Se va a realizar la siquiente division: 5000 / 230 / 2 y redondearlo a 5 decimales"
op_esp = "\n5.-Se ralizara una operacion especial, la cual deberemos de utilizar 4 numero y 3 operadores diferentes y el resultado debe de ser 0\n  La operacion sera la siguiente\n  2 X 5 + 30 - 40"
msj_exp ="\n6.-Obtener el resultado de 1024 utilizando solo el numero 2 multiplixandose por si mismo, las veces que sea necesarias\n"

nombre_completo = nombre + apellido_uno + apellido_dos

num_uno = 20
num_dos = 23

res_sum = num_uno + num_dos + 44
res_res = 23 - 20 -90
res_mult = 147 * 5
res_div = 5000 / 230 /2
res_div_red = round(res_div,5)
res_op_esp = 2 * 5 + 30 - 40
res_milveinticuatro = 2*2*2*2*2*2*2*2*2*2

print(titulo)
print(nombre_completo)

print(msj_bienvenida)
print(msj_dos + msj_expl)
print(msj_concat_sum + msj_res + msj_mult + msj_div + op_esp + msj_exp)

print("---------los resultados de las operaciones son:---------")
print("El rESuLTAdo de La SUMa Es:".lower())
print(res_sum)
print("El resultado de la resta es: ")
print(res_res)
print("El resultado de la multiplicacion es: ")
print(res_mult)
print("El resultado de la division es: ")
print(res_div)
print("El resultado de la division redondeada a 5 decimales es:")
print(res_div_red)
print("El resultaado de la operacion especial es:")
print(res_op_esp)
print("para obtener el numero 1024 debemos de multiplicas al 2 recursibamente 10 veces")
print(res_milveinticuatro)


