# Calculadora con historial - HU-2
# Versión mejorada: suma, resta, multiplicación, división y mejor historial

from datetime import datetime

historial = []

def registrar_operacion(operacion):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historial.append(f"[{timestamp}] {operacion}")

def sumar(a, b):
    resultado = a + b
    registrar_operacion(f"{a} + {b} = {resultado}")
    return resultado

def restar(a, b):
    resultado = a - b
    registrar_operacion(f"{a} - {b} = {resultado}")
    return resultado

def multiplicar(a, b):
    resultado = a * b
    registrar_operacion(f"{a} * {b} = {resultado}")
    return resultado

def dividir(a, b):
    if b == 0:
        registrar_operacion(f"{a} / {b} = Error (División por cero)")
        return "Error: División por cero"
    resultado = a / b
    registrar_operacion(f"{a} / {b} = {resultado}")
    return resultado

# Ejemplo de uso
print("Suma:", sumar(5, 3))
print("Resta:", restar(10, 4))
print("Multiplicación:", multiplicar(6, 2))
print("División:", dividir(8, 0))

print("\nHistorial de operaciones:")
for operacion in historial:
    print(operacion)
