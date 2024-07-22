from random import random
from time import sleep
import listasYtablas


# Función que realiza una tirada de dados de las caras indicadas como parámetro:
def dadoDe(caras): 
    # Convertir el valor de random en un rango especifico: nuevo_valor = valor_aleatorio × (max−min) + min
    aleatorio = random()
    tirada = (aleatorio * (caras - 1)) + 1
    return round(tirada)

def pausa():
    print()
    for i in range(3):
        print('.', end='', flush=True)  # end='' evita el salto de línea, flush=True fuerza la salida inmediata
        sleep(0.5)  # Pausa de medio segundo entre cada punto.
    print()
    print()

def calcCaracteristica(): # Función que realiza las tiradas de datos iniciales para los valores de las caracteristicas.
    tiradasD6 = []

    # Se tiran 4 D6 y se guardan los valores en la lista tiradasD6:
    for _ in range(4): # Usamos barra baja como variable de cada iteración cuando el valor del índice no es necesario.
        tiradasD6.append(dadoDe(6))
    
    # Se toman los 3 valores mayores de esas 4 tiradas:
    tiradasD6.sort() # Ordeno la lista de de menor a mayor.
    tiradasD6.pop(0) # Elimino el primer valor, el menor de todos.

    return sum(tiradasD6) # Devuelvo la suma de los 3 valores contenidos en la lista tiradasD6

def eleccionRaza(): # Seleccionamos una lista de elementos y un mensaje para informar al usuario de que escoja una opción.
    print('Indica el nombre de la raza deseada (Algunas razas tienen subrazas):')
    print('vvv')

    print(listasYtablas.tablaRazas) # Muestro tabla en pantalla.
    print(' ')
    # Pedimos al usuario que escoja hasta que seleccione un número de elección valido:
    while True: # Repite indefinidamente, hasta que se escoja una opción correcta.
        try: # Con try controlamos los posibles errores, ValueError en este caso, así podemos hacer algo si falla en lugar de dejar que el programa se detenga.
            numRaza = (int(input('Ingrese el número de su elección: '))) # Guarda el número elección del usuario en la variable 'elecPj'
            if 1 <= numRaza <= len(listasYtablas.razas): # Verificamos que 1 sea menor o igual al número escogido y este a su vez sea menor o igual al número total de razas.
                contador = 1
                for key in listasYtablas.razas:
                    if contador == numRaza:
                        razaSelec = key
                        print(f'Raza seleccionada: {razaSelec}.')
                        print(' ')
                        break
                    contador += 1
                
                if razaSelec == 'Enano':
                    print('Los enanos tienen dos subrazas:')
                    print('vvv')
                    print(listasYtablas.tablaSubEnano) # Muestro tabla de subraza de enanos en pantalla
                    print(' ')

                    while True:
                        try:
                            numSubraza = int(input('Ingrese el número de su elección: '))
                            if 1 <= numSubraza <= len(listasYtablas.subEnano): 
                                contador = 1
                                for key in listasYtablas.subEnano:
                                    if contador == numSubraza:
                                        SubRazaSelec = key
                                        print(f'Subraza seleccionada: {SubRazaSelec}.')
                                        print(' ')
                                        return SubRazaSelec
                                    contador += 1
                        except ValueError:
                            print('Entrada no válida. Por favor, ingrese un número.')

                if razaSelec == 'Elfo':
                    print('Los elfos tienen tres subrazas:')
                    print('vvv')
                    print(listasYtablas.tablaSubElfo) # Muestro tabla de subraza de elfos en pantalla
                    print(' ')

                    while True:
                        try:
                            numSubraza = int(input('Ingrese el número de su elección: '))
                            if 1 <= numSubraza <= len(listasYtablas.subElfo): 
                                contador = 1
                                for key in listasYtablas.subElfo:
                                    if contador == numSubraza:
                                        SubRazaSelec = key
                                        print(f'Subraza seleccionada: {SubRazaSelec}.')
                                        print(' ')
                                        return SubRazaSelec
                                    contador += 1
                        except ValueError:
                            print('Entrada no válida. Por favor, ingrese un número.')


                if razaSelec == 'Mediano':
                    print('Los medianos tienen dos subrazas:')
                    print('vvv')
                    print(listasYtablas.tablaSubMediano) # Muestro tabla de subraza de medianos en pantalla
                    print(' ')

                    while True:
                        try:
                            numSubraza = int(input('Ingrese el número de su elección: '))
                            if 1 <= numSubraza <= len(listasYtablas.subMediano): 
                                contador = 1
                                for key in listasYtablas.subMediano:
                                    if contador == numSubraza:
                                        SubRazaSelec = key
                                        print(f'Subraza seleccionada: {SubRazaSelec}.')
                                        print(' ')
                                        return SubRazaSelec
                                    contador += 1
                        except ValueError:
                            print('Entrada no válida. Por favor, ingrese un número.')

                if razaSelec == 'Gnomo':
                    print('Los gnomos tienen dos subrazas:')
                    print('vvv')
                    print(listasYtablas.tablaSubGnomo) # Muestro tabla de subraza de gnomos en pantalla
                    print(' ')

                    while True:
                        try:
                            numSubraza = int(input('Ingrese el número de su elección: '))
                            if 1 <= numSubraza <= len(listasYtablas.subGnomo): 
                                contador = 1
                                for key in listasYtablas.subGnomo:
                                    if contador == numSubraza:
                                        SubRazaSelec = key
                                        print(f'Subraza seleccionada: {SubRazaSelec}.')
                                        print(' ')
                                        return SubRazaSelec
                                    contador += 1
                        except ValueError:
                            print('Entrada no válida. Por favor, ingrese un número.')

                else:
                    return razaSelec # Si la condición se cumple retorna la raza seleccionada y finaliza el bucle while.
            else:
                print('Por favor, elija un número válido de la lista.') # Si la condición no se cumple se indica al usuario que debe escoger correctamente.
        
        except ValueError:
            print('Entrada no válida. Por favor, ingrese un número.') # Si el valor introducido da error "ValueError" informa al usuario de que el valor escogido debe ser un número.
    
