# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
  
peso = float(input("Introduzca su peso: "))
altura = float(input("Introduzca su altura: "))

imc = calcular_imc(peso,altura)

print(imc)