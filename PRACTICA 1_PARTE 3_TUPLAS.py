#Ejercicios capitulo 19

#33.- Imprime la segunda posicion de la tupla
#34.- Utiliza los simbolos de suma y resta para hacer operaciones con col elementod de una tupla

#Ejercicios dep capitulo 20

#35.- Convierte una tupla a una lisa, e i9mprime el tipo de variabla


materias = ('Vibraciones', 'Teoria de control 1', 'Electronica','Inteligencia Artificial' )
calificaciones_tc1 = (70,100,80)
calificaciones_vib = (80,90,75)


print("En la materia de " + materias[1] + " El alumno tiene obtivo las siguientes calificaciones d elos tres parciales ")
print(calificaciones_tc1[0] + calificaciones_tc1[1] + calificaciones_tc1[2] )
print("Obteniendo la calificacion final promedio de: ")
calif = calificaciones_tc1[0] + calificaciones_tc1[1] + calificaciones_tc1[2]
calif = round(calif/3,2)
print(calif)
print("Ahora vamos a cambiar la tupla a lista")
print("Actualmente la variable de 'MAterias es del tipo: '")
print(type(materias))
print("Se realiza el cambio de tipo de dato")
materias = list(materias)
print(type(materias))
