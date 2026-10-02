from calculos import Calculos
from entrada import Entrada
from grafico import Grafico
from resultados import Resultados


class AplicacaoBhaskara:
    def __init__(self):
        self.entrada = Entrada()
        self.resultados = Resultados()
        self.grafico = Grafico()

    def executar(self):
        print("Calculadora de Bhaskara")
        a, b, c = self.entrada.ler_coeficientes()

        calculos = Calculos(a, b, c)
        delta = calculos.calcular_delta()
        raizes = calculos.calcular_raizes(delta)
        vertice = calculos.calcular_vertice(delta)
        pontos = calculos.calcular_pontos(vertice[0])

        self.resultados.exibir_resultados(delta, raizes, vertice, pontos)
        self.grafico.exibir_grafico(calculos, raizes, vertice, pontos)


if __name__ == "__main__":
    AplicacaoBhaskara().executar()
