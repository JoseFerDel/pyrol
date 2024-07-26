from prettytable import PrettyTable

# clases = ('Bárbaro', 'Bardo', 'Brujo', 'Clérigo', 'Druida', 'Explorador', 'Guerrero', 'Hechicero', 'Mago', 'Monje', 'Paladín', 'Pícaro')

clasesPj = {
    'Bárbaro' : [
        'Un feroz guerrero de trasfondo primitivo que puede entrar en una furia de batalla.', 
        'd12', 
        ['FUE'], 
        ['FUE', 'CON'],
        [
            'Armadura ligera', 
            'Armadura mediana', 
            'Escudos', 
            'Armas simples', 
            'Armas marciales']], 
    'Bardo' : [
        'Un mago inspirador cuyo poder replica la música de la creación.', 
        'd8', 
        ['CAR'],
        ['DES', 'CAR'],
        [
            'Armadura ligera',
            'Armas simples',
            'Ballestas de mano',
            'Espadas largas', 
            'Estoques', 
            'Espadas cortas']], 
    'Brujo' : [
        'Un practicante de la magia que deriva de un contrato con una entidad extraplanaria.', 
        'd8', 
        ['CAR'],
        ['SAB', 'CAR'],
        [
            'Armadura ligera', 
            'Armas simples']], 
    'Clérigo' : [
        'Un campeón sacerdotal que esgrime magia divina al servicio de un poder mayor.', 
        'd8', 
        ['SAB'],
        ['SAB', 'CAR'],
        [
            'Armadura ligera',
            'Armadura mediana', 
            'Escudos', 
            'Armas simples']], 
    'Druida' : [
        'Un sacerdote de la Antigua Fe que blande los poderes de la naturaleza, la luz de la luna, el crecimiento de las plantas, el fuego, el rayo y que adopta formas animales.', 
        'd8', 
        ['SAB'],
        ['INT', 'SAB'],
        [
            'Armadura ligera',
            'Armadura mediana no metalica',
            'Escudos no metalicos', 
            'Clavas', 
            'Dagas', 
            'Dardos', 
            'Jabalinas', 
            'Mazas', 
            'Bastones', 
            'Cimitarras', 
            'Hoces', 
            'Hondas', 
            'Lanzas']], 
    'Explorador' : [
        'Un guerrero que usa la proeza marcial y la magia de la naturaleza para combatir las amenazas en los límites de la civilización.', 
        'd10', 
        ['DES', 'SAB'],
        ['FUE', 'DES'],
        [
            'Armadura ligera', 
            'Armadura mediana', 
            'Escudos', 
            'Armas simples',
            'Armas marciales']], 
    'Guerrero' : [
        'Un maestro del combate marcial, competente con una gran variedad de armas y armaduras.', 
        'd10', 
        ['FUE', 'DES'], # Fuerza o destreza, una de las dos.
        ['FUE', 'CON'],
        [
            'Todas las armaduras', 
            'Todos los escudos', 
            'Todas las armas simples',
            'Todas las armas marciales']], 
    'Hechicero' : [
        'Un lanzador de conjuros que recurre a la magia inherente de un don o una línea de sangre.', 
        'd6', 
        ['CAR'],
        ['CON', 'CAR'],
        [
            'Dagas', 
            'Dardos', 
            'Hondas', 
            'Bastones', 
            'Ballestas ligeras']], 
    'Mago' : [
        'Un usuario de magia educado capaz de manipular la estructura de la realidad.', 
        'd6', 
        ['INT'],
        ['INT', 'SAB'],
        [
            'Dagas', 
            'Dardos', 
            'Hondas', 
            'Bastones', 
            'Ballestas ligeras']],
    'Monje' : [
        'Un maestro de las artes marciales, que domina el poder del cuerpo en busca de la perfección física y espiritual.', 
        'd8', 
        ['DES', 'SAB'],
        ['FUE', 'DES'],
        [
            'Armas simples', 
            'Espadas cortas']],
    'Paladín' : [
        'Un guerrero santo atado a un juramento sagrado.', 
        'd10', 
        ['FUE', 'CAR'],
        ['SAB', 'CAR'],
        [
            'Todas las armaduras', 
            'Todos los escudos', 
            'Todas las armas simples', 
            'Todas las armas marciales']],
    'Pícaro' : [
        'Un rufián que usa sigilo y astucia para superar obstáculos y enemigos.', 
        'd8', 
        ['DES'],
        ['DES', 'INT'],
        [
            'Armadura ligera', 
            'Armas simples', 
            'Ballestas de mano', 
            'Espadas largas', 
            'Estoques',
            'Espadas cortas']]
}

# LISTA DE RAZAS
razasPj = {
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

# TABLA DE RAZAS:
tablaRazas = PrettyTable()
tablaRazas.title = 'RAZAS'
tablaRazas.field_names = [' ', 'RAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(razasPj.items(), start=1):
    tablaRazas.add_row([i, key, value])
tablaRazas.align['RAZA'] = "l"
tablaRazas.align['BONIFICACIÓN'] = "l"

# TABLA DE SUBRAZAS ENANOS:
tablaSubEnano = PrettyTable()
tablaSubEnano.title = 'SUBRAZAS DE ENANO'
tablaSubEnano.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subEnano.items(), start=1):
    tablaSubEnano.add_row([i, key, value])
tablaSubEnano.align['SUBRAZA'] = "l"
tablaSubEnano.align['BONIFICACIÓN'] = "l"

# TABLA DE SUBRAZAS ELFOS:
tablaSubElfo = PrettyTable()
tablaSubElfo.title = 'SUBRAZAS DE ELFO'
tablaSubElfo.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subElfo.items(), start=1):
    tablaSubElfo.add_row([i, key, value])
tablaSubElfo.align['SUBRAZA'] = "l"
tablaSubElfo.align['BONIFICACIÓN'] = "l"


# TABLA DE SUBRAZAS MEDIANOS:
tablaSubMediano = PrettyTable()
tablaSubMediano.title = 'SUBRAZAS DE MEDIANO'
tablaSubMediano.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subMediano.items(), start=1):
    tablaSubMediano.add_row([i, key, value])
tablaSubMediano.align['SUBRAZA'] = "l"
tablaSubMediano.align['BONIFICACIÓN'] = "l"


# TABLA DE SUBRAZAS GNOMOS:
tablaSubGnomo = PrettyTable()
tablaSubGnomo.title = 'SUBRAZAS DE GNOMO'
tablaSubGnomo.field_names = [' ', 'SUBRAZA', 'BONIFICACIÓN']
for i, (key, value) in enumerate(subGnomo.items(), start=1):
    tablaSubGnomo.add_row([i, key, value])
tablaSubGnomo.align['SUBRAZA'] = "l"
tablaSubGnomo.align['BONIFICACIÓN'] = "l"

# TABLA DE CLASES:
tablaClases = PrettyTable()
tablaClases.title = 'CLASES'
tablaClases.field_names = [' ', 'CLASE', 'DESCRIPCIÓN', 'DADO GOLPE', 'CARAC. PRIMARIA', 'TIRADAS SALVACIÓN', 'ARMAS Y ARMADURAS']
for i, (key, value) in enumerate(clasesPj.items(), start=1):
    tablaClases.add_row([i, key, value[0], value[1], value[2], value[3], value[4]])
    tablaClases.add_row([' ', ' ', ' ', ' ', ' ', ' ', ' ',])
tablaClases.align['CLASE'] = "l"
tablaClases.align['DESCRIPCIÓN'] = "l"
tablaClases.max_width['DESCRIPCIÓN'] = 40
tablaClases.align['DADO GOLPE'] = "c"
tablaClases.align['CARAC. PRIMARIA'] = "l"
tablaClases.align['TIRADAS SALVACIÓN'] = "l"
tablaClases.align['ARMAS Y ARMADURAS'] = "l"
tablaClases.max_width['ARMAS Y ARMADURAS'] = 40





