# Problemas del capitulo 10

# 23.- la siguiente lista, ¿qué color está en la posición 3?
#      materias = ["Matematicas", "Inteligancia Artificial", "Teoria de control", "programacion", "vibraciones"]
# 24.- ¿En qué posición se encuentra el color 'rojo'? ¿y el 'rosa'?
# 25.- Crea una lista que contenga los siguientes valores en las posiciones indicadas.

# Problemas del capitulo 11
# 26.- Utiliza las posiciones negativas para acceder e imprimir los ultimos dos elementos de tu lista.

# Problemas del capitulo 12

# 27.- De esta lista, elimina 2 elementos de tu lista. Debes utilizar al menos una vez las posiciones negativas para eliminar un elemento. Después, imprime la lista para ver los elementos que se han eliminado.

# Problemas del caplitulo 13

# 28.- Elimina de la siguiente lista los elementos 'amarillo' y 'rojo'. Solo puedes eliminarlos utilizando el método remove().

#Problemas del capitulo 14

# 29.- Elimina elementos de tu lista utilizando el metodo pop() y se tendran que guardar estos elementos en una nueva lista 

# Problemas del capitulo 15

# 30.- Añade 2 elementos a tu lista utilizando el metidodo append()

# Problemas del capitulo 16

# 31.- Añadir a tu lista 2 objetos utilizando posiciones de lista negativa con el metodo insert()

# Problemas del capitulo 17 
# 32.- Ordena los elementos de tu lista en orden alfabetico descendente 

#Problema del capitulo 18
# 33.- Contar los elementos de tu lista, guardarlos en una variable y mostrar cuants elementos tiene la lista

materias = ['Matematicas','Inteligencia Artificial','Teoria de Control','Programacion',"vibraciones","Ingles", "Vision Artificial", "Microprocesadores"] #<--- Se crea la lista de "materias"
print("\n")
print(materias) #<--- Se imprime la lista completa
print("\n")
print("En la lista de materias que se muesta arriba tiene el siguiente orden\nQue el alumno Hector Ortega llevará el siguiente semestre de Ing. MEcatronica")

print("en la posicion '0' se encuentra: "+ materias[0])  #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '1' se encuentra: "+ materias[1])  #<--- Se imprime el contenido de la posicion 1 de la lista materias
print("en la posicion '2' se encuentra: "+ materias[2])  #<--- Se imprime el contenido de la posicion 2 de la lista materias
print("en la posicion '3' se encuentra: "+ materias[3])  #<---- Se utiliza posiciones negativas
print("en la posicion '4' se encuentra: "+ materias[4])  #<---- Se utiliza posicion negativa
print("en la posicion '5' se encuentra: "+ materias[-3]) #<---- Se utiliza posicion negativa
print("en la posicion '6' se encuentra: "+ materias[-2]) #<---- Se utiliza posicion negativa
print("en la posicion '7' se encuentra: "+ materias[-1]) #<---- Se utiliza posicion negativa

print("\nPero el alumno, en intersemestral acredito 2 materias, que son: \nVibraciones y Microcontroladores\nEnronces su tira de materias de 6to semestre se vería así;\n")
del materias[-1]
del materias[4]

print("en la posicion '0' se encuentra: "+ materias[0]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '1' se encuentra: "+ materias[1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias
print("en la posicion '2' se encuentra: "+ materias[2]) #<--- Se imprime el contenido de la posicion 2 de la lista materias
print("en la posicion '3' se encuentra: "+ materias[3]) #<---- Se utiliza posiciones negativas
print("en la posicion '4' se encuentra: "+ materias[-2]) #<---- Se utiliza posicion negativa
print("en la posicion '5' se encuentra: "+ materias[-1]) #<---- Se utiliza posicion negativa

print("\nPero por cuestiones de trabajo el alumno debera de desistir en 2 materias mas, ya que su horario no se acomoda\n las materias son: Teoria de control y MAtematicas")
print("Por lo tanto la lista de materias del alumno quedara de la siguiente forma:\n")
materias.remove("Teoria de Control")
materias.remove("Matematicas")

print("en la posicion '0' se encuentra: "+ materias[0]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '1' se encuentra: "+ materias[1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias
print("en la posicion '2' se encuentra: "+ materias[-2]) #<--- Se imprime el contenido de la posicion 2 de la lista materias
print("en la posicion '3' se encuentra: "+ materias[-1]) #<---- Se utiliza posiciones negativas

print("\nAdemas, realizo 2 examenes globales para las materias de:")
materia1 = materias.pop(0) #<-- Al eliminarse el valor en la posicion 0 de la lista, esta se modifica
materia2 = materias.pop(2)
materias_aprobadas = [materia1,materia2] #<--- se guarda en una lista diferente
print(materias_aprobadas[0])
print(materias_aprobadas[1] + "\n")

print("por lo tanto la lista de materias quedaria de la siguiente forma:")
print("en la posicion '0' se encuentra: "+ materias[0]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '1' se encuentra: "+ materias[1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias

print("\nlastimosamente, el alumno debe dos materias que no habia considerado, del semstre pasado que son:\nMecanismos y Termofluidos\n")
materias.append("Termofluidos")
materias.append("Mecanismos")

print("por lo tanto la lista de materias quedaria de la siguiente forma:")
print("en la posicion '0' se encuentra: "+ materias[0]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '1' se encuentra: "+ materias[1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias
print("en la posicion '2' se encuentra: "+ materias[-2]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '3' se encuentra: "+ materias[-1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias

print("\nLo que no recordaba el pobre alumno es que debía de tambíen agregar 2 materias optativas ya que se lo pide la escuela para titularse")
print("por lo tanto, el alumno eligió entre sus materias optativas las siguientes materias")
materias.insert(-4,"Filosofia")
materias.insert(-2,"Dibujo")
print(materias[0])
print(materias[3] + "\n")

print("por lo tanto la lista de materias quedaria de la siguiente forma (Ordenado alfabeticamente de forma descendente):")
materias.sort(reverse = True)
print("en la posicion '0' se encuentra: "+ materias[0]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '1' se encuentra: "+ materias[1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias
print("en la posicion '2' se encuentra: "+ materias[2])
print("en la posicion '3' se encuentra: "+ materias[-3])
print("en la posicion '4' se encuentra: "+ materias[-2]) #<--- Se imprime el contenido de la posicion 0 de la lista materias
print("en la posicion '5' se encuentra: "+ materias[-1]) #<--- Se imprime el contenido de la posicion 1 de la lista materias


cuenta_materias = len(materias)
print(cuenta_materias)
print(f"\nPor lo tanto el alumno estará cursando un total de: {cuenta_materias} materias en el presente semestre")
