def multiplicacion(factor1, factor2):
    producto = factor1 * factor2
    return producto

if __name__=="__main__":
    multiplicando = float(input("Multiplicando: "))
    multiplicador = float(input("Multiplicandor: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")