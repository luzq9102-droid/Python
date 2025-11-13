import os
claves = {"admin": "12345", "luz":"abc"}
user = input("Ingrese usuario:")
password =input("Ingrese contraseña")
intento = 0

if user in claves :
    print("Usuario existente")
    while True:
        if claves [user] == password:
            print("Acceso correcto")
            break
        else:
            intento += 1

            if intento > 3:
              print("Demasiados intentos :( ")
              break

            os.system("cls")
            print("Error de contraseña")
            password = input(f"Intento {intento} de 3. Ing. cont:")


else:
    print("Usuario inexistente")
