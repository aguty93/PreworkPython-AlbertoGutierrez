#Ejercicio 7 Calculadora Simple
#Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error matemático"
    else:
        return a / b

def main():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion not in ['1', '2', '3', '4']:
        print("Opción inválida.")
        return

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == '2':
        resultado = resta(num1, num2)
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
        print(f"El producto de {num1} y {num2} es: {resultado}")
    elif opcion == '4':
        resultado = division(num1, num2)
        print(f"La división de {num1} entre {num2} es: {resultado}")
    else:
        resultado = "Operación no válida"
        
if __name__ == "__main__":
    main()