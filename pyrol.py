#!/usr/bin/env python3 

# Pyrol
# File: pyrol.py

from clases import PJ
from func import eleccionRaza


razas = ("Enano", "Elfo", "Mediano", "Humano", "Dracónico", "Gnomo", "Semielfo", "Semiorco", "Tiflin")
clases = ("Bárbaro", "Bardo", "Brujo", "Clérigo", "Druida", "Explorador", "Guerrero", "Hechicero", "Mago", "Monje", "Paladín", "Pícaro")

nombrePj = str(input("Introduce nombre de nuevo personaje: "))
razaPj = eleccionRaza(razas)



Conan = PJ(nombrePj, razaPj)