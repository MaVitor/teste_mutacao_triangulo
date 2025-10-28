def classificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Os lados devem ser positivos."
    if a + b <= c or a + c <= b or b + c <= a:
        return "Os lados não formam um triângulo."

    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

if __name__ == "__main__":
    a = float(input("Lado A: "))
    b = float(input("Lado B: "))
    c = float(input("Lado C: "))
    print(classificar_triangulo(a, b, c))
