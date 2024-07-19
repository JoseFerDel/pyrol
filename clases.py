from func import calcCaracteristicas

class PJ: 
    def __init__(self, name, race):
        self.nombre = name
        self.raza = race

        self.fue = calcCaracteristicas() # Fuerza
        self.des = calcCaracteristicas() # Destreza
        self.con = calcCaracteristicas() # Constitución
        self.int = calcCaracteristicas() # Inteligencia
        self.sab = calcCaracteristicas() # Sabiduría
        self.car = calcCaracteristicas() # Carisma
        print(" ")
        print(f"Se ha creado un nuevo personaje jugador")
        print(" ")
        print(f"NOMBRE: {self.nombre}")
        print(f"RAZA: {self.raza}")
        print(f"CLASE: ??????")
        print(" ")
        print(f"FUERZA: {self.fue}")
        print(f"DESTREZA: {self.des}")
        print(f"CONSTITUCIÓN: {self.con}")
        print(f"INTELIGENCIA: {self.int}")
        print(f"SABIDURÍA: {self.sab}")
        print(f"CARISMA: {self.car}")
