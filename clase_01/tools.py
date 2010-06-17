'''Herramientas para PythonCabal

Rutinas para todo el grupo
'''

def ponComa( numero ):
    '''Regresa numero como cadena con comas.

    numero es un entero
    no maneja signo'''
    particion = str( numero ).partition('.')
    cadena = particion[0]
    indice = len( cadena )

    while indice > 3:
        '''Restar 3 al indice'''
        indice = indice - 3
        
        '''Agregar coma'''
        cadena = cadena[ :indice ] +  ',' + cadena[ indice: ]
        
    
    '''Regresar resultado con todo y parte decimal'''
    return cadena + particion[1] + particion[2]

if __name__ == '__main__':
    for datoDePrueba in [ 0, 12, 123, 1234, 12345, 123456, 1234567, 1234.5678 ]:
        print ( datoDePrueba , ponComa( datoDePrueba ) )
