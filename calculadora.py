def sumar(x,y):
    return x + y
def restar(x,y):
    return x - y
def multiplicar(x,y):
    pass
def dividir(x,y):
    if y != 0:
        return x/y
    else:
        return "Error. Division por cero"
    
while True:
    opcion = input("1.sumar\n2.restar\nElige: ")
    if opcion == "1":
        n1 = float(input("Valor 1: "))
        n2 = float(input("Valor 2: "))
        print(f"{n1}+{n2}={sumar(n1,n2)}")
    else:
        print("Bye")
        break