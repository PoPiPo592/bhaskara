import cmath


class Calculos:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_delta(self):
        return self.b**2 - 4 * self.a * self.c

    def calcular_raizes(self, delta):
        raiz_delta = cmath.sqrt(delta)
        raiz_1 = (-self.b + raiz_delta) / (2 * self.a)
        raiz_2 = (-self.b - raiz_delta) / (2 * self.a)
        return raiz_1, raiz_2

    def calcular_vertice(self, delta):
        x_vertice = -self.b / (2 * self.a)
        y_vertice = -delta / (4 * self.a)
        return x_vertice, y_vertice

    def calcular_pontos(self, x_vertice):
        passo = max(1.0, abs(x_vertice) * 0.25)
        deslocamentos = (-2, -1, 0, 1, 2)
        pontos = []
        for deslocamento in deslocamentos:
            x = x_vertice + deslocamento * passo
            y = self.a * x**2 + self.b * x + self.c
            pontos.append((x, y))
        return pontos
