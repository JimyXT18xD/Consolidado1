def suma(a, b):
        return a + b

def resta(a, b):
        return a - b

def multiplicacion(a, b):
        return a * b

def division(a, b):
        return a / b


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("OPERACIONES:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Que operación desea aplicar (1/2/3/4): ")

if opcion == "1":
    resultado = suma(num1, num2)
elif opcion == "2":
    resultado = resta(num1, num2)
elif opcion == "3":
    resultado = multiplicacion(num1, num2)
else:
    resultado = division(num1, num2)

print("Resultado: ", resultado)