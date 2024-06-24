a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))

if a > b:
    if b > c:
        print(f'{a} es mayor que {b} y {b} es mayor que {c}')
    else:
        print(f'{a} es mayor que {b} y menor que {c}')
elif a == b:
    print(f'{a} es igual a {b}')
else:
    print (f'{a} es menor que {b}')