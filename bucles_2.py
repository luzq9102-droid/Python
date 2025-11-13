#suma de valores
v = -1
suma = 0
while v != 0:
    v = int(input("Ingrese un n° Z+"))
    if v > 0 :
      suma += v
print(f"La suma es: {suma}")


#ejemplo 2
v = -1 
suma = 0
while True:
  v = int(input("Ingrese un n° Z+"))
  if v > 0 :
    suma += v
  elif v == 0:
    break
  print(f"La suma es: {suma}")