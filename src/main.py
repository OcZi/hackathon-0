import re
import operator
import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: División por cero")
    return a / b

def evaluate_expression(expression):
    """Evaluar expresiones matemáticas utilizando una gramática simple"""
    # Reemplazar potencias y raíces por operaciones básicas
    expression = expression.replace('^', '**')

    # Evaluar la expresión de forma segura usando eval y un diccionario de operaciones permitidas
    allowed_operators = {
        '+': suma,
        '-': resta,
        '*': multiplicacion,
        '/': division
    }

    # Analizar la expresión y asegurarse de que solo contiene números y operadores permitidos
    pattern = re.compile(r'^[-+/*\d\s().]+$')
    if not pattern.match(expression):
        raise ValueError("Error: Caracteres no permitidos en la expresión")

    try:
        # Evaluar la expresión utilizando eval, permitiendo solo operadores seguros
        result = eval(expression, {"__builtins__": None}, allowed_operators)
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: División por cero")
    except Exception as e:
        raise ValueError(f"Error: {e}")

    # Verificar si el resultado es un número entero
    if isinstance(result, (int, float)):
        if result == int(result):
            return int(result)
        else:
            return result
    else:
        return "Error: Resultado no válido"

def calculate(operacion):
    """Función principal para calcular operaciones"""
    try:
        return evaluate_expression(operacion)
    except Exception as e:
        return str(e)

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
            try:
                resultado = calculate(operacion_actual)
                print(f"Resultado: {resultado}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
