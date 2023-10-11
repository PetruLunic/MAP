import math

def calcEcGrad2(a, b, c):
    delta = pow(b, 2) - (4 * a * c)

    if delta < 0: return "Multime vida"

    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    return {
        x1,
        x2
    }

print(calcEcGrad2(1, -5, 4))