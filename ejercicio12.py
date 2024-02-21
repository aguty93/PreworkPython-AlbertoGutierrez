# Ejercicio 12: Calculadora de Área de un Rectángulo
# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.

def calcular_area(longitud, anchura):
  area = longitud * anchura
  return area

longitud = float(input("Introduce la longitud: "))
anchura = float(input("Introduce la anchura: "))

area = calcular_area(longitud, anchura)
print(area)