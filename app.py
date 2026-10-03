# calculator.py

def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Resta dos números."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b

defUn script completo de Python ideal para alojar en un repositorio de GitHub. Incluye operaciones básicas, manejo de errores y una interfaz interactiva por consola.

### Código de la Calculadora (`calculator.py`)

```python
"""
Calculadora Interactiva en Python
Un proyecto simple e interactivo diseñado para ser compartido en GitHub.
"""

def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Resta el segundo número del primero."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide el primer número entre el segundo."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def get_number(prompt: str) -> float:
    """Solicita un número al usuario y valida la entrada."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Ingrese un número válido.")

def main():
    print("=" * 35)
    print("      CALCULADORA EN PYTHON")
    print("=" * 35)
    
    operations = {
        '1': ('Suma', add, '+'),
        '2': ('Resta', subtract, '-'),
        '3': ('Multiplicación', multiply, '*'),
        '4': ('División', divide, '/')
    }

    while True:
        print("\nSeleccione una operación:")
        for key, (name, _, symbol) in operations.items():
            print(f"  {key}. {name} ({symbol})")
        print("  5. Salir")
        
        choice = input("\nIngrese una opción (1-5): ").strip()

        if choice == '5':
            print("\n¡Gracias por usar la calculadora!")
            break

        if choice in operations:
            name, func, symbol = operations[choice]
            print(f"\n--- Operación: {name} ---")
            
            num1 = get_number("Ingrese el primer número: ")
            num2 = get_number("Ingrese el segundo número: ")

            try:
                result = func(num1, num2)
                print(f"\nResultado: {num1} {symbol} {num2} = {result}")
            except ValueError as error:
                print(f"\nError de cálculo: {error}")
        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
