def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def programa_principal():
    try:
        base_rectangulo = float(input("Ingresa la base del rectángulo: "))
        altura_rectangulo = float(input("Ingresa la altura del rectángulo: "))
        resultado_r = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
        print(f"Área del rectángulo: {resultado_r:.2f}")

        base_triangulo = float(input("Ingresa la base del triángulo: "))
        altura_triangulo = float(input("Ingresa la altura del triángulo: "))
        resultado_t = calcular_area_triangulo(base_triangulo, altura_triangulo)
        print(f"Área del triángulo: {resultado_t:.2f}")

    except ValueError:
        print("Error: Por favor, ingresa un número válido.")

if __name__ == "__main__":
    programa_principal()