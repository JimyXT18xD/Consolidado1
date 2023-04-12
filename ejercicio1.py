def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Error: Ingrese un numero natural")
    return a / b

def obtener_numero(entrada, mensaje):
        while True:
        try:
            numero = float(input(entrada))
            break
        except ValueError:
            print("Error: Entrada incorrecta, solo se permite numeros")
    return numero

try:
    num1 = obtener_numero("Ingrese el primer número: ", "Error: Entrada incorrecta, solo se permite numeros")
    num2 = obtener_numero("Ingrese el segundo número: ", "Error: Entrada incorrecta, solo se permite numeros")