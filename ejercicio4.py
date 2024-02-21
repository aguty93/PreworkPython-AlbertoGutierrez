# Ejercicio 4: Contador de Vocales 
# # Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario

def contar_vocales(palabra):
    vocales = "AEIOUaeiou"
    contador = 0
    for letra in palabra:
      if letra in vocales:
        contador = contador + 1
    return contador
palabra = input("Introduzca una palabra: ")
numero_vocales= contar_vocales(palabra)
print (numero_vocales)