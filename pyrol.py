#!/usr/bin/env python3 

# Pyrol
# File: pyrol.py

from clases import PJ
from func import eleccionRaza
from func import eleccionClase
from func import pausa

atrib = []

### CREACIÓN DE PERSONAJE ###
#############################
nombrePj = str(input('Introduce nombre de nuevo personaje: '))
pausa()
clasePj = eleccionClase()
pausa()
razaPj = eleccionRaza()
pausa()
print('FICHA DE PERSONAJE:')
print('-------------------')
print(f'Nombre: {nombrePj}')
print(f'Clase: {clasePj}')
print(f'Raza: {razaPj}')
print()
# print('Generando valores aleatorios para los atributos:')

