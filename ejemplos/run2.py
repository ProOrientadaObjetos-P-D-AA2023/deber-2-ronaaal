"""

"""
# Crear dos objetos de la clase 02

class Dinosaurio:
    def __init__(self, nombre, especie, altura):
        self.nombre = nombre
        self.especie = especie
        self.altura = altura

# objeto 01

# crear

dino = Dinosaurio("T-Rex", "Tyrannosaurus rex", 6)

# Presentar objeto; usar el método __st__

print("Mi dinosaurio es un",dino.nombre, ", su especie es", dino.especie, "y mide", dino.altura ,"metros.")

# objeto 02

# crear ingresando valores por teclado

nombre = input("Ingresa el nombre del dinosaurio: ")
especie = input("Ingresa la especie del dinosaurio: ")
altura = float(input("Ingresa la altura del dinosaurio (en metros): "))
dino_2 = Dinosaurio(nombre, especie, altura)

# Presentar objeto; usar el método __st__

print("Mi segundo dinosaurio es un",dino_2.nombre, ", su especie es", dino_2.especie, "y mide", dino_2.altura ,"metros.")


