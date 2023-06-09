def suma(a, b):
    """Operacion de suma"""
    return a + b

def resta(a, b):
    """Operacion de resta"""
    return a - b

def multiplicacion(a, b):
    """Operacion de multiplicación"""
    return a * b

def division(a, b):
    """Operacion de división"""
    if b == 0:
        raise ValueError("Error: Ingrese un numero natural")
    return a / b

def obtener_numero(entrada, mensaje):
    """Funciona para verificar el digito ingresado"""
    while True:
        try:
            numero = float(input(entrada))
            break
        except ValueError:
            print("Error: Entrada incorrecta, solo se permite numeros")
    return numero

try:
    # Seccion donde se ingresa los numeros
    num1 = obtener_numero("Ingrese el primer número: ", "Error: Entrada incorrecta, solo se permite numeros")
    num2 = obtener_numero("Ingrese el segundo número: ", "Error: Entrada incorrecta, solo se permite numeros")
    
    # Seccion donde se muestra el menu de operaciones
    print("OPERACIONES:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    # Seccion donde se elije la operacion
    while True:
        opcion = input("Que operación desea aplicar (1/2/3/4): ")
        if opcion in ["1", "2", "3", "4"]:
            break
        else:
            print("Error: Entrada incorrecta, solo se permite numeros")
            
    # Seccion donde se opera los numeros
    if opcion == "1":
        resultado = suma(num1, num2)
    elif opcion == "2":
        resultado = resta(num1, num2)
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
    else:
        resultado = division(num1, num2)

    # Mostrar la respuesta
    print("Resultado: ", resultado)

except ValueError as e:
    print(str(e))
except Exception as e:
    print("Error: ", str(e))