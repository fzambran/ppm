object_size = int(input('Ingresa el tamaño (m3) del objeto: '))
proximity = int(input('Ingresa la proximidad (km): '))

if object_size > 5 and proximity < 1000:
    print('Se requieren maniobras evasivas')
else:
    print('El objeto no representa amenaza')