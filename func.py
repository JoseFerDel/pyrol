import random

# Función que realiza una tirada de dados de las caras indicadas como parámetro:
def dadoDe(caras): 
    # Convertir el valor de random en un rango especifico: nuevo_valor = valor_aleatorio × (max−min) + min
    aleatorio = random.random()
    tirada = aleatorio * (caras - 1) + 1
    return round(tirada)

def calcCaracteristicas(): # Función que realiza las tiradas de datos iniciales para los valores de las caracteristicas.
    tiradasD6 = []

    # Se tiran 4 D6 y se guardan los valores en la lista tiradasD6:
    for _ in range(4): # Usamos barra baja como variable de cada iteración cuando el valor del índice no es necesario.
        tiradasD6.append(dadoDe(6))
    
    # Se toman los 3 valores mayores de esas 4 tiradas:
    tiradasD6.sort() # Ordeno la lista de de menor a mayor.
    tiradasD6.pop(0) # Elimino el primer valor, el menor de todos.

    return sum(tiradasD6) # Devuelvo la suma de los 3 valores contenidos en la lista tiradasD6

def eleccionRaza(lista):
    print("Por favor, elija una de las siguientes razas:")
    for i, raza in enumerate(lista, start=1):
        print(f"{i}. {raza}") 

    while True: # Repite para siempre
        try: # Con try controlamos los posibles errores, ValueError en este caso, así podemos hacer algo si falla en lugar de dejar que el programa se detenga.
            razaPj = int(input("Ingrese el número de su elección: ")) # Guarda el número elección del usuario en la variable "razaPj"
            if 1 <= razaPj <= len(lista): # Verificamos que 1 sea menor o igual al número escogido y este a su vez sea menor o igual al número total de razas.
                return lista[razaPj -1] # Si la condición se cumple devuelve la raza seleccionada.
            else:
                print("Por favor, elija un número válido de la lista.") # Si la condición no se cumple se indica al usuario que debe escoger correctamente.
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.") # Si el valor introducido da error "ValueError" informa de que el valor escogido debe ser un número.
    