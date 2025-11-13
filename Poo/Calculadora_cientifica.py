class Calculadora:
    # Constructor
    def __init__(self):
        self.n1 = 0
        self.n2 = 0 

    # Método para cargar números
    def cargarNumeros(self, x, y):
        self.n1 = x
        self.n2 = y

    # Método para sumar
    def sumar(self):
        return self.n1 + self.n2


# Clase hija
class CalculadoraCientifica(Calculadora):
    def __init__(self):
        super().__init__()  # llama al constructor de la clase base

    # Método factorial
    def factorial(self):
        ac = 1
        for x in range(1, self.n1 + 1):
            ac *= x
        return ac

    # Método potencia (usa los números cargados)
    def calcularPotencia(self):
        return self.n1 ** self.n2

    # Método raíz cuadrada (solo del primer número)
    def calcularRaizCuadrada(self):
        return self.n1 ** 0.5


# Bloque principal
if __name__ == "__main__":
    casio = Calculadora()
    casio.cargarNumeros(15, 9)
    print(f"La suma es {casio.sumar()}")

    print("\nCalculadora Científica")
    casioFX = CalculadoraCientifica()
    casioFX.cargarNumeros(5, 4)
    print(f"La suma es {casioFX.sumar()}")
    print(f"El factorial de {casioFX.n1} es: {casioFX.factorial()}")
    print(f"La potencia de {casioFX.n1} elevado a {casioFX.n2} es: {casioFX.calcularPotencia()}")
    print(f"La raíz cuadrada de {casioFX.n1} es: {casioFX.calcularRaizCuadrada()}")
