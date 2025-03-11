import random

def simulacion_exploracion():
    costo_exploracion = 1_000_000  # 1M$
    barriles = 300_000
    precio_barril = 150
    ingresos_potenciales = barriles * precio_barril  # 45M$
    
    # Probabilidad de éxito en la exploración
    if random.random() < 0.4:
        # Éxito: 40% estado, 60% empresa
        ganancia_empresa = ingresos_potenciales * 0.6 - costo_exploracion
        return ganancia_empresa
    else:
        # Fracaso: pierde la inversión
        return -costo_exploracion

def analizar_estrategia(num_simulaciones=10000):
    resultados = []
    ganancia_total = 0
    
    for _ in range(num_simulaciones):
        resultado = simulacion_exploracion()
        resultados.append(resultado)
        ganancia_total += resultado
    
    promedio_ganancia = ganancia_total / num_simulaciones
    positivos = sum(1 for r in resultados if r > 0)
    negativos = num_simulaciones - positivos
    
    # Cálculo del umbral de éxito
    ingreso_neto_exito = (300_000 * 150 * 0.6) - 1_000_000
    perdida_fracaso = -1_000_000
    umbral = 1_000_000 / (ingreso_neto_exito - perdida_fracaso)
    
    print("Resultados de la simulación:")
    print(f"Ganancia promedio por exploración: ${promedio_ganancia/1e6:.2f}M")
    print(f"Probabilidad de éxito empírica: {positivos/num_simulaciones:.1%}")
    print(f"\n1. Estrategia recomendada: {'Realizar exploración' if promedio_ganancia > 0 else 'No explorar'}")
    print(f"2. Umbral de éxito mínimo: {umbral:.2%}")
    print("3. Análisis financiero:")
    print(f"   - Inversión requerida: $1M por exploración")
    print(f"   - Ganancia potencial en éxito: ${ingreso_neto_exito/1e6:.1f}M")
    print(f"   - Pérdida en fracaso: $1M")

analizar_estrategia()