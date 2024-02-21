# Ejercicio 20: Suma de Números en una Lista
# Crea un programa que sume todos los números en una lista ingresada por el usuario.

def sumar_lista(lista):
  suma = 0
  for num in lista:
      suma += num
      return suma
numeros = list(map(int, input("Introduce una lista de números: ").split()))
resultado = sumar_lista(numeros)
print(f"La suma de los números es: {resultado}")