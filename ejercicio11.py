# Ejercicio 11: Calculadora de Edad
# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

def calc_edad(año_nacimiento):
  año_actual = 2023
  edad = año_actual - año_nacimiento
  return edad
año_nacimiento = int(input("Introduzca su año de nacimiento: "))
edad = calc_edad(año_nacimiento)
print(edad)