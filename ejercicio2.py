# Ejercicio 2: Calculadora de Propina 
# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.


def calcular_cuenta(consumo):
  propina = consumo * 0.15
  total = consumo + propina
  return total
consumo = float(input("Introduzca el total de la cuenta: "))
total_cuenta = calcular_cuenta(consumo)
print(total_cuenta)