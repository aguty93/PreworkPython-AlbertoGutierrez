# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def comp_palindromo(palabra):
    palabra_invertida = palabra [::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

palabra = input("Introduzca una palabra: ")

if comp_palindromo(palabra):
  print("Es un palíndromo")
else:
  print("No es un palíndromo")