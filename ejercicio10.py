# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

def determinar_dia(numero):
    dias_semana = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    if numero >= 1 and numero <=7:
        return dias_semana[numero-1]

numero = int(input("Introduce un número del 1 al 7: "))
nombre_dia = determinar_dia(numero)
print(nombre_dia)