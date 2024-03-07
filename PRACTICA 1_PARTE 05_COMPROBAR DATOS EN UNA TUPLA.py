#EJERCICIIOS CAPITULO 24: COMPROBAR DATOS EN UNA TUPLA

#EJERCICIO 41: COMPROBAR QUE EL ELEMENTO QUE INTRODUZCA EL USUARIO SE ENCUENTRE DENTRO DE LA TUPLA

#EJERCICIOS CAPITULO 25: MULTIPLES IF

#EJERCICIO PROPUESTO: IMPLEMENTAR VARIOS IF PARA QUE EL PROGRAMA DEVUELVA LA POSICION EN LA QUE ESTA EL COLOR ELEGIDO POR EL USUARIO

colores = ('Azul', 'Rojo','Verde','Amarillo')
eleccion = input("Escribe el color que buscas\nLa primera letra del nombre del color de tu eleccion debe de ser mayuscula\n")
if eleccion in colores:
    print("El color " + eleccion + " esta admitido :)")
    if eleccion == "Azul":
        print("El color "+ eleccion + " esta en la posicion 0")
    if eleccion == "Rojo":
        print("El color "+ eleccion + " Esta en la posicion 1")
    if eleccion == "Verde":
        print("El color " + eleccion + " Esta en la posicion 2")
    if eleccion == "Amarillo":
        print("El color "+ eleccion + " Esta en la posicion 3")
else:
    print("El color " + eleccion + " no esta admitido :(")
