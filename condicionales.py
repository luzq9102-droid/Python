lluvia  = False
finde = True   

if not (lluvia and finde):
    print("salir")
elif lluvia or finde:
    print("me quedo en casa")

else:
    print("voy a clases")

#Ejercicio condicionales 
num1 = int(input("Ingrese el primer nro: "))
num2 = int(input("Ingrese el segundo nro: "))
if num1 > num2:
    mayor = num1
else:
    mayor = num2
if mayor % 2 == 0 :
    print(f"El nro mayor es {mayor} and par.")
else:
    print(f"El nro mayor es {mayor} and impar.")

   
