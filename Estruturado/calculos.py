import cmath


def calcular_delta(a, b, c):
    return b**2 - 4 * a * c


def calcular_raizes(a, b, delta):
    raiz_delta = cmath.sqrt(delta)
    raiz_1 = (-b + raiz_delta) / (2 * a)
    raiz_2 = (-b - raiz_delta) / (2 * a)
    return raiz_1, raiz_2


def calcular_vertice(a, b, delta):
    x_vertice = -b / (2 * a)
    y_vertice = -delta / (4 * a)
    return x_vertice, y_vertice


def calcular_pontos(a, b, c, x_vertice):
    passo = max(1.0, abs(x_vertice) * 0.25)
    deslocamentos = (-2, -1, 0, 1, 2)
    pontos = []
    for deslocamento in deslocamentos:
        x = x_vertice + deslocamento * passo
        y = a * x**2 + b * x + c
        pontos.append((x, y))
    return pontos
