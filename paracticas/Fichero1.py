texto = input('Introduce sus datos: ')
nombre_fichero = 'agenda.txt'
f=open(nombre_fichero, 'w') #apertura w= write, a = append
f.write(f'{texto}\n')
f.close()

print("contenido de agenda.txt")
leerFichero = open(nombre_fichero, 'r')
print(leerFichero.read())
leerFichero.close()
