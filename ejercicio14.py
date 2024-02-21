# Ejercicio 14: Calculadora de Descuento
# .

def calcular_precio_final(precio_original):
    descuento = 0.20  # 20% de descuento
    precio_final = precio_original * (1 - descuento)
    return precio_final

precio_original = float(input("Ingrese el precio original del artículo: "))

precio_final = calcular_precio_final(precio_original)

print(f"El precio final después de aplicar un descuento del 20% es: {precio_final:.2f}")