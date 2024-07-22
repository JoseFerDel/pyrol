from func import calcCaracteristica

class PJ: 
    def __init__(self, name0, race0, class0):
        self.nombre = name0
        self.raza = race0
        self.clase = class0

        self.fue = calcCaracteristica() # Fuerza
        self.des = calcCaracteristica() # Destreza
        self.con = calcCaracteristica() # Constitución
        self.int = calcCaracteristica() # Inteligencia
        self.sab = calcCaracteristica() # Sabiduría
        self.car = calcCaracteristica() # Carisma
        print(' ')
        print(f'Se ha creado un nuevo personaje jugador')
        print(' ')
        print(f'NOMBRE: {self.nombre}')
        print(f'RAZA: {self.raza}')
        print(f'CLASE: {self.clase}')
        print(' ')
        print(f'FUERZA: {self.fue}')
        print(f'DESTREZA: {self.des}')
        print(f'CONSTITUCIÓN: {self.con}')
        print(f'INTELIGENCIA: {self.int}')
        print(f'SABIDURÍA: {self.sab}')
        print(f'CARISMA: {self.car}')