# Ejercicio 3: Verificación de Edad 
# # Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.

def verificacion_edad(edad):
  if edad >= 18:
      return("Eres mayor de edad")
  else:
      return("Lo siento, eres menor de edad")

edad = int(input("Introduce su edad: "))

mensaje = verificacion_edad(edad)

print(mensaje)