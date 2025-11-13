#{}diccionario
#()tuple y van separadas por comas 
#[]lista
#lo que cargas en tuple es inmutable o sea que no lo podes cambiar.
#En diccionario 

#LISTAS
calificaciones = [1,2,3,4,5]
nombres = ["Moises", "Camila", "Fernanda", "Pablo", "Tania"]
lista_variada = [True, 10.5, "abc", [0,1,1]]

print("Estudiante: ", nombres[2])
print("Calificación: ", calificaciones[-2])
print("Lista dentro  de otra: ", lista_variada[3][0])
print("Imprimir un rango o slices: ",nombres[1:2])
print(lista_variada)

#agregar elementos a una lista 
nombres.append("Anibal")
print(nombres)
#remover elementos de una lista 
nombres.remove("Pablo")
print(nombres)

#TUPLE
colores = ("Azul","Verde", "Rojo","Amarillo", "Blanco", "Negro","Gris")
print("Color; ", colores[3])

#DICCIONARIO
productos={"manzana": 5600, "mandarina": 12000, "kiwi": 25000}

print("Precio de la manzana en Gs. ", productos["manzana"])
print("Precios", productos)
                                                