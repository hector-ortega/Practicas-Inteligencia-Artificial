#CAPITULO 31: ¿QUE SON LOS DICCIONARIOS EN PYTHON?
#48.- Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print().
teclado_1 = {
    'Categoria' : 'Teclados',
    'Modelo' : 'HyperX Alloy FPS Pro',
    'Precio' : '89,99'
}
teclado_2 = {
    'Categoria' : 'Teclados',
    'Modelo' : 'Corsair K55 RGB',
    'Precio' : '59,99'
}
print("\nTeclado 2")
print("Modelo: " + teclado_2['Modelo'] + ", " + "Precio: " + teclado_2['Precio'])

#CAPITULO 32: COMO USAR DICCIONARIOS CON EL BUCLE FOR
#49.- Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
print("\n\nTeclado 1")
for x in teclado_1:
    print(x, 'es: ', teclado_1[x] + '.')

#CAPITULO 33: METODOS CON DICCIONARIOS 
#50.- Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.
del teclado_1 #<- Se elimina el teclado 1
del teclado_2['Precio'] #<- Se elimina Precio del teclado 2
del teclado_2['Categoria'] #<- Se elimina categoria del teclado 2
print("\nSe imprime la ultima clave 'Modelo' de teclado 2")
print(teclado_2)