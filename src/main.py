import re

def suma(a, b):
    return a + b


def multiplicacion(a, b):
    return a * b

def division(a, b):
     return a / b


def calculate(operacion):
    # Usar expresiones regulares para identificar operandos y operadores, incluyendo números negativos
    match = re.match(r'([-+]?\d*\.?\d+)\s*([+\-*/])\s*([-+]?\d*\.?\d+)', operacion)
    if match:
        a, operador, b = match.groups()
        a, b = float(a), float(b)

        if operador == '+':
            resultado = suma(a, b)
        elif operador == '-':
            resultado = resta(a, b)
        elif operador == '*':
            resultado = multiplicacion(a, b)
        elif operador == '/':
            resultado = division(a, b)

        # Verificar si el resultado es un entero
        if resultado == int(resultado):
            return int(resultado)
        else:
            return operacion  # Devolver la operación original si el resultado no es entero

    return "Error: Operación no soportada o formato incorrecto"

def main():
    operacion_actual = ""

    while True:
        entrada = input(f"Operación actual: {operacion_actual}\n> ")

        if entrada.lower() == 'c':
            operacion_actual = ""
        elif entrada.lower() == 'q':
            print("Saliendo de la calculadora.")
            break
        else:
            operacion_actual = entrada
            resultado = calculate(operacion_actual)
            print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
