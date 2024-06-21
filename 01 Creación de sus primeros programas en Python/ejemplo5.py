from functools import reduce

numeros = [3, 2, 6, 8, 4, 6, 2, 9]

pares = list(filter(lambda n : n % 2 == 0, numeros))

print(f'Los números pares de la lista son: {pares}') 

duplicado = list(map(lambda n: n * 2, pares))

print(f'El doble de los valores de la lista anterior es: {duplicado}')

suma =  reduce(lambda a, b : a + b, duplicado)

print(f'La suma de los valores duplicados es: {suma}')