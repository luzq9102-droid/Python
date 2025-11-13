números = []
for i in range(5):
    num = float(input(f"Ingrese el número {i + 1}"))
    números.append(num)

print("Lista de números: ", números)
print("Suma de los números: ", sum(números))