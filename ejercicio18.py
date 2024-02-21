# Ejercicio 18: Contador de Palabras
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

def contar_palabras(oracion):
    palabras = oracion.split()
    cantidad_palabras= len(palabras)
    print(cantidad_palabras)
    return cantidad_palabras

frase = input("Introduce una oración: ")
numero_palabras = contar_palabras(frase)
print(f"La oración tiene {numero_palabras} palabras")