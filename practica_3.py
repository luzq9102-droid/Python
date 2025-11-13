print("La suma de 10 + 4 :",3 + 4)
print("La resta :", 10-4)
print("La multplicacion: ", 10*4)
print("La division: ", 10/4)
print("El resto: ", 10%4)
print("este no se que es pero bueeeno: ", 10//4)
print("Elevado: ", 10**4)


#ecuacion cuadratica 2x**2-7+3=0
a=2
b=-7
c=3
x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
print("x1: ", x1)
print("x2: ", x2)

#cadenas de texto 
print("SNPP"+" CTFPPJ"+" PROGRAMACION PYTON")
print("AULA" + " 2102")


#peradores mixtas
print("Tun chi "* 5)
print("Ja "* (2**3))

#operador de comparación
print(3>4)
print(3<4)
print(3>=4)
print(4<=4)
print(3==4)
print(3!=4)

#operaciones cadenas de texto 
print("python" > "PYTHON")
print("aaaa" >= "abaa")#ordenación alfabetica por ASCII
print(len("aaaa")>=len("abaa"))#Cuenta caracteres

print("python" != "PYTHON")

#Operadores logicos 
print(10>4 and "Z" > "A")
print(10>4 or "Z" > "A")
print(not(10>4) and "Z" > "A")

#strings o cadenas de texto 
nombre = "Tu nombre "
apellido = "Apellido"

print(nombre + "" + apellido)

texto = "Este texto \n tiene saldo de linea y \t tabulacion"
print(texto)
