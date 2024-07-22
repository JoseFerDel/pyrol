from prettytable import PrettyTable

# LISTA DE RAZAS
razas = {
    'Enano' : 'Enano de las Colinas (+2CON, +1SAB) -- Enano de la Montaña (+2CON, +1FUE)', 
    'Elfo' : 'Elfo Alto (+2DES, +1INT) -- Elfo Silvano (+2DES, +1SAB) -- Elfo Drow (+2DES, +1CAR)', 
    'Mediano' : 'Mediano de la Colina (+2DES, +1CON) -- Mediano de la Selva (+2DES, +1CAR)', 
    'Humano' : '+1TODOS', 
    'Dracónico' : '+2FUE. +1CAR', 
    'Gnomo' : 'Gnomo de la Roca (+2INT, +1CON) -- Gnomo de la Selva (+2INT, +1DES)', 
    'Semielfo' : '+2CAR, +1 a dos atributos de tu elección', 
    'Semiorco' : '+2FUE, +1CON', 
    'Tiflin' : '+2CAR, +1INT'
}

subEnano = {
    'Enano de las Colinas' : '+2CON, +1SAB',
    'Enano de la Montaña' : '+2CON, +1FUE'
}

subElfo = {
    'Elfo Alto' : '+2DES, +1INT',
    'Elfo Silvano' : '+2DES, +1SAB',
    'Elfo Drow' : '+2DES, +1CAR'
}

subMediano = {
    'Mediano de la Colina' : '+2DES, +1CON',
    'Mediano de la Selva' : '+2DES, +1CAR'
}

subGnomo = {
    'Gnomo de la Roca' : '+2INT, +1CON',
    'Gnomo de la Selva' : '+2INT, +1DES'
}

clases = ('Bárbaro', 'Bardo', 'Brujo', 'Clérigo', 'Druida', 'Explorador', 'Guerrero', 'Hechicero', 'Mago', 'Monje', 'Paladín', 'Pícaro')

# TABLA DE RAZAS:
tablaRazas = PrettyTable()
tablaRazas.title = "RAZAS"
tablaRazas.field_names = [' ', 'RAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(razas.items(), start=1):
    tablaRazas.add_row([i, key, value])
tablaRazas.align['RAZA'] = "l"
tablaRazas.align['BONIFICACIÓN'] = "l"

# TABLA DE SUBRAZAS ENANOS:
tablaSubEnano = PrettyTable()
tablaSubEnano.title = "SUBRAZAS DE ENANO"
tablaSubEnano.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subEnano.items(), start=1):
    tablaSubEnano.add_row([i, key, value])
tablaSubEnano.align['SUBRAZA'] = "l"
tablaSubEnano.align['BONIFICACIÓN'] = "l"

# TABLA DE SUBRAZAS ELFOS:
tablaSubElfo = PrettyTable()
tablaSubElfo.title = "SUBRAZAS DE ELFO"
tablaSubElfo.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subElfo.items(), start=1):
    tablaSubElfo.add_row([i, key, value])
tablaSubElfo.align['SUBRAZA'] = "l"
tablaSubElfo.align['BONIFICACIÓN'] = "l"


# TABLA DE SUBRAZAS MEDIANOS:
tablaSubMediano = PrettyTable()
tablaSubMediano.title = "SUBRAZAS DE MEDIANO"
tablaSubMediano.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subMediano.items(), start=1):
    tablaSubMediano.add_row([i, key, value])
tablaSubMediano.align['SUBRAZA'] = "l"
tablaSubMediano.align['BONIFICACIÓN'] = "l"


# TABLA DE SUBRAZAS GNOMOS:
tablaSubGnomo = PrettyTable()
tablaSubGnomo.title = "SUBRAZAS DE GNOMO"
tablaSubGnomo.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subGnomo.items(), start=1):
    tablaSubGnomo.add_row([i, key, value])
tablaSubGnomo.align['SUBRAZA'] = "l"
tablaSubGnomo.align['BONIFICACIÓN'] = "l"