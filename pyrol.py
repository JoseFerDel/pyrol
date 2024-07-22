#!/usr/bin/env python3 

# Pyrol
# File: pyrol.py

from clases import PJ
from func import eleccionRaza
from func import pausa

atrib = []

### CREACIÓN DE PERSONAJE ###
#############################
nombrePj = str(input('Introduce nombre de nuevo personaje: '))
pausa()
razaPj = eleccionRaza()
pausa()
# clasePj = eleccion(clases, 'Escoge tu clase de la lista:')
pausa()
print()

print('Generando valores aleatorios para los atributos:')
pausa()
print(atrib)