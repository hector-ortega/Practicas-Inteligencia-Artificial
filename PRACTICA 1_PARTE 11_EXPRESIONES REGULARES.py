import re

Nombre = "Hector Alejandro "
buscar = re.search('e',Nombre) #<-- Utilizamos la funcion search() (Capitulo 47)
print(buscar)


texto = "pablito clavo un clavito en la calva de un calvito"
busqueda = re.findall("cl",texto) #<-- Se utiliza findal para devolver la lista de lo que estamos buscando (Capitulo 48)
busqueda_2 = re.split("to",texto) #<-- se usa el metodod split() (Capitulo 49)
busqueda_3 = re.sub(" ", "-",texto) #<-- se usa el metodod sub() (Capitulo 49)
busqueda_4 = re.findall("ca{1}lva",texto) #<--se busca un numero determinado con el caracter{} (Capitulo 50)
print(busqueda)
print(busqueda_2)
print(busqueda_3)

if busqueda_4:
    print("\nHay almenos una coincidencia.\n")
else: 
    print("no hay coincidencia")


variable = "'variable' Esta declarado" #<-- Se realiza un manejo de eexcepciones (Capitulo 51)
try:
    print(variable)
except:
    print("La variable no esta declarada")
