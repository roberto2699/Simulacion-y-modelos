import random

# Definición de las opciones
OPCIONES = ["Cooperar", "Traicionar"]

# Matriz de pagos: (Prisionero 1, Prisionero 2)
PAGOS = {
    ('Cooperar', 'Cooperar'): (3, 3),      # Ambos cooperan
    ('Cooperar', 'Traicionar'): (0, 5),    # Prisionero 1 coopera, Prisionero 2 traiciona
    ('Traicionar', 'Cooperar'): (5, 0),    # Prisionero 1 traiciona, Prisionero 2 coopera
    ('Traicionar', 'Traicionar'): (1, 1)   # Ambos traicionan
}

def tomar_decision():
    """Simula la decisión de un prisionero."""
    return random.choice(OPCIONES)

def main():
    print("=== Dilema del Prisionero ===")
    print("Opciones: Cooperar o Traicionar\n")

    # Obtener las decisiones de los prisioneros
    decision1 = tomar_decision()
    decision2 = tomar_decision()

    print(f"Prisionero 1 ha decidido: {decision1}")
    print(f"Prisionero 2 ha decidido: {decision2}")

    # Determinar el resultado basado en las decisiones
    resultado1, resultado2 = PAGOS[(decision1, decision2)]

    print("\nResultados:")
    print(f"Prisionero 1 obtiene: {resultado1} puntos")
    print(f"Prisionero 2 obtiene: {resultado2} puntos")

# Ejecutar el programa
if __name__ == "__main__":
    main()