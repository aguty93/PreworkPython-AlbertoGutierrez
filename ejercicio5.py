# Ejercicio 5:  Suma de Números Pares 
# # Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

suma = 0
for numero in range (2, 101, 2):
    suma += numero
print(suma)