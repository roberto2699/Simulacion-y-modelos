import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(['cara', 'cruz'])

def simular_tiradas(num_tiradas):
    ganadas = 0
    perdidas = 0
    
    for _ in range(num_tiradas):
        resultado_dado = lanzar_dado()
        resultado_moneda = lanzar_moneda()
        
        if resultado_dado % 2 == 0 and resultado_moneda == 'cara':
            ganadas += 1
        else:
            perdidas += 1
    
    return ganadas, perdidas

def main():
    num_tiradas = 1000
    ganadas, perdidas = simular_tiradas(num_tiradas)
    
    print(f"Resultados después de {num_tiradas} tiradas:")
    print(f"Veces ganadas: {ganadas} ({ganadas/num_tiradas * 100:.2f}%)")
    print(f"Veces perdidas: {perdidas} ({perdidas/num_tiradas * 100:.2f}%)")

if __name__ == "__main__":
    main()