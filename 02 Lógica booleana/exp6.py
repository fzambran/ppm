a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))

if a > b:
    if b > c:
        print(f'{a} es mayor que {b} y {b} es mayor que {c}')
    elif b == c:
            print(f'{a} es mayor que {b} y {b} es igual a {c}')
    else:
        if a > c:
            print(f'{a} es mayor que {b} y {c}, y {b} es menor que {c}')
        else:
            print(f'{a} es mayor que {b} y menor que {c}')
elif a == b:
    if b > c:
        print(f'{a} es igual a {b} y {b} es mayor que {c}')
    elif b == c:
        print(f'{a} es igual a {b} y {b} es igual a {c}')
    else:
        print(f'{a} es igual a {b} y {b} es menor que {c}')
else:
    if a > c:
        print (f'{a} es menor que {b}, pero mayor que {c}')
    elif a == c:
        print (f'{a} es menor que {b} e igual a {c}')
    else:
        if b > c:
            print(f'{a} es menor que {b} y {b} es mayor que {c}')
        else:
            print(f'{a} es menor que {b} y {b} es igual a {c}')