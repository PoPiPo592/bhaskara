import cmath
import math


class Calculos:
    def __init__(self, a, b, c):
        coeficientes = (a, b, c)
        if any(not math.isfinite(valor) for valor in coeficientes):
            raise ValueError("Os coeficientes devem ser números finitos.")
        if any(valor == 0 for valor in coeficientes):
            raise ValueError("Os coeficientes não podem ser zero.")

        self.a = a
        self.b = b
        self.c = c

    def _validar_resultado(self, valores):
        if any(
            not math.isfinite(parte)
            for valor in valores
            for parte in (
                (valor.real, valor.imag)
                if isinstance(valor, complex)
                else (valor,)
            )
        ):
            raise ValueError(
                "Os coeficientes são grandes demais para calcular "
                "resultados finitos."
            )

    def calcular_delta(self):
        try:
            delta = self.b**2 - 4 * self.a * self.c
        except OverflowError as erro:
            raise ValueError(
                "Os coeficientes são grandes demais para calcular delta."
            ) from erro
        self._validar_resultado((delta,))
        return delta

    def calcular_raizes(self, delta):
        try:
            raiz_delta = cmath.sqrt(delta)
            raizes = (
                (-self.b + raiz_delta) / (2 * self.a),
                (-self.b - raiz_delta) / (2 * self.a),
            )
        except (OverflowError, ZeroDivisionError) as erro:
            raise ValueError(
                "Não foi possível calcular raízes finitas "
                "com esses coeficientes."
            ) from erro
        self._validar_resultado(raizes)
        return raizes

    def calcular_vertice(self, delta):
        try:
            vertice = (-self.b / (2 * self.a), -delta / (4 * self.a))
        except (OverflowError, ZeroDivisionError) as erro:
            raise ValueError(
                "Não foi possível calcular um vértice finito "
                "com esses coeficientes."
            ) from erro
        self._validar_resultado(vertice)
        return vertice

    def calcular_pontos(self, x_vertice):
        passo = max(1.0, abs(x_vertice) * 0.25)
        pontos = []
        try:
            for deslocamento in (-2, -1, 0, 1, 2):
                x = x_vertice + deslocamento * passo
                y = self.a * x**2 + self.b * x + self.c
                pontos.append((x, y))
        except OverflowError as erro:
            raise ValueError(
                "Não foi possível calcular pontos finitos "
                "com esses coeficientes."
            ) from erro
        self._validar_resultado(
            valor for ponto in pontos for valor in ponto
        )
        return pontos
