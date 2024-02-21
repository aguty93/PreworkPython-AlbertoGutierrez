# Ejercicio 9: Conversor de Divisas
# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

def conv_divisas(dolares):
  euros = dolares * 0.85
  return euros

cantidad_dolares = float(input("Introduce la cantidad de dolares a convertir: "))
cantidad_euros = conv_divisas(cantidad_dolares)

print(cantidad_euros)
