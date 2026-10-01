from calculos import (
    calcular_delta,
    calcular_pontos,
    calcular_raizes,
    calcular_vertice,
)
from entrada import ler_coeficientes
from grafico import exibir_grafico
from resultados import exibir_resultados


def main():
    print("Calculadora de Bhaskara")
    a, b, c = ler_coeficientes()

    delta = calcular_delta(a, b, c)
    raizes = calcular_raizes(a, b, delta)
    vertice = calcular_vertice(a, b, delta)
    pontos = calcular_pontos(a, b, c, vertice[0])

    exibir_resultados(delta, raizes, vertice, pontos)
    exibir_grafico(a, b, c, raizes, vertice, pontos)


if __name__ == "__main__":
    main()
