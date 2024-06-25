# Convertir grados Celsius a Farenheit
def main():
    celsius = int(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = cel_a_fah(celsius)
    print("\n")
    print("La temperatura en grados Fahrenheit es: ", fahrenheit)
    
def cel_a_fah(temp):
    fahrenheit = (1.8 * temp) + 32
    return fahrenheit

main()

