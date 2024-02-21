# Ejercicio 17: Conversor de Millas a Kilómetros
# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.

def convertir_millas_kilometros(millas):
  kilometros = millas * 1.60934
  return kilometros
millas = float(input("Introduce la distancia en millas: "))
kilometros = convertir_millas_kilometros(millas)
print(f"La distancia en km es: {kilometros}")