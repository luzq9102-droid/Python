productos = {
    "C": "Celular",
    "L": "Laptop",
    "T": "Televisor"
}
forma_pago = {
    "E": "Efectivo",
    "T": "Tarjeta"
}
license
eleccion_pago = []
eleccion_producto = []

def mostrar_opciones():
    print("\n--------------- Productos disponibles ---------------")
    for i,x in productos.items():
        print(f"Opción {i} / Producto: {x}")
    print("-----------------------------------------------------")
def mostrar_pago():
    print("\n---------------- Pagos Disponibles ----------------")
    for i,x in forma_pago.items():
        print(f"Opción {i} / Forma de pago: {x}")
    print("-----------------------------------------------------")
def pedir_nombre(mensaje):
    print("\n---------------- Nombre del cliente ----------------")
    while True:
        nombre = input(mensaje).strip()
        if nombre.replace(" ", "").isalpha():
            return nombre 
        else:
            print("Error: No se permiten números ni espacios vacios...")
def pedir_producto(mensaje):
    mostrar_opciones()
    while True:
        producto = input(mensaje).upper()
        if producto in productos:
            eleccion_producto.append(productos[producto])
            return producto 
        else:
            print("Error: Ingrese una opción válida....")
def pedir_pago(mensaje):
    mostrar_pago()
    while True:
        pago = input(mensaje).upper()
        if pago in forma_pago:
            eleccion_pago.append(forma_pago[pago])
            return pago 
        else:
            print("Error: Ingrese una opción válida....")
def pedir_precio(mensaje):
    print("\n---------------- Precio unitario ----------------")
    while True:
        try:
            precio = float(input(mensaje))
            if precio > 0 and precio <= 10000000:
                return precio 
            else:
                print("Error: Elija una cantidad válida...")
        except ValueError:
          print("Error: Elija una cantidad válida...")
def pedir_cantidad(mensaje):
    print("\n---------------- Cantidad de productos ----------------")
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad > 0:
                return cantidad 
            else:
                print("Error: Elija una cantidad válida...")
        except ValueError:
            print("Error: Elija una cantidad válida...")

nombre = pedir_nombre("Ingrese su nombre: ")
producto = pedir_producto("Ingrese el tipo de producto: ")
cantidad = pedir_cantidad("Ingrese la cantidad: ")
precio = pedir_precio("Ingrese el precio unitario: ")
pago = pedir_pago("Ingrese la forma de pago: ")

descuento = 0
recargo = 0
precio_base = cantidad * precio 
if producto == "C":
    nombre_producto = "Celular"
    if cantidad >= 3:
        descuento = 3
        precio_base*= (1-0.10)
if producto == "L":
    nombre_producto = "Laptop"
    if pago == "E":
        descuento = 5
        precio_base*= (1-0.05)
if producto == "T":
    nombre_producto = "Televisor"
    if cantidad <= 2:
        recargo = 4
        precio_base*= 1.04
if pago == "E":
    nombre_pago = "Efectivo"
else:
    nombre_pago = "Tarjeta"

print("\n---------------- Factura ----------------")
print(f"Nombre: {nombre}")
print(f"Producto: {nombre_producto}")
print(f"Tipo de pago: {nombre_pago}")
if descuento != 0:
    print(f"Descuento: {descuento}")
elif recargo != 0:
    print(f"Recargo: {recargo}")
else:
    print("Sin ajustes aplicados...")
print(f"Total: {precio_base} Gs.")
print("-----------------------------------------")