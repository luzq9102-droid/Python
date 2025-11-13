#va guardar nombre y nro de telefono
#usar diccionaro: clave: valor, nomnre: telefono
agenda = {}
def guardarRegistro(nombre, telefono):
    agenda[nombre] = telefono
def imprimirAgenda():
    print (agenda)

#vrear un menu
while True:
    print("1. Guardar contacto\n2.Imprimir\n3.Salir")
    opción = input("opcion: ")
    if opción == "1":
        nombre = input("Nombre: ")
        telefono =input("Telefono: ")
        guardarRegistro(nombre, telefono)
    elif opción == "2":
        imprimirAgenda()
    elif opción == "0":
        break
    else:
        print("Opcion invalida")
