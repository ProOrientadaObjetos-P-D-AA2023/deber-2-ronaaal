"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Bicicleta:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def frenar(self):
        self.velocidad -= 5

    def acelerar(self):
        self.velocidad += 5


# clase 02

class Dinosaurio:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def rugir(self):
        print("¡GRRRAAAUUU!")

    def envejecer(self):
        self.edad += 1

