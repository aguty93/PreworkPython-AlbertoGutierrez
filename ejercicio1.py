# Ejercicio 1: Conversor de Temperatura 
# Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

# F = C * (9/5) + 32
def convertidor(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit
  
temperatura_celsius = float (input("Introduzca la temperatura en Celsius: "))
temperatura_fahrenheit = convertidor(temperatura_celsius)
print(temperatura_fahrenheit)