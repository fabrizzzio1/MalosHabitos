def realizar_calculo(factor1, factor2, factor3):
    return factor1 * factor2 + factor3

def programa_principal():
    try:
        numero1 = float(input("Ingresa el valor del primer número: "))
        numero2 = float(input("Ingresa el valor del segundo número: "))
        numero3 = float(input("Ingresa el valor del tercer número: "))

        resultado = realizar_calculo(numero1, numero2, numero3)
        print(f"{numero1} * {numero2} + {numero3} = {resultado:.2f}")

    except ValueError:
        print("Error: Por favor, ingresa un número válido.")

if __name__ == "__main__":
    programa_principal()
