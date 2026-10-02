import math

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Grafico:
    def __init__(self, frame):
        self.figura, self.eixos = plt.subplots(figsize=(7, 5), dpi=100)
        self.figura.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.figura, master=frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.exibir_instrucoes()

    def exibir_instrucoes(self):
        self.eixos.clear()
        self.eixos.set_title("Gráfico da função quadrática")
        self.eixos.text(
            0.5,
            0.5,
            "Insira os coeficientes e clique em Calcular.",
            ha="center",
            va="center",
            transform=self.eixos.transAxes,
        )
        self.eixos.set_axis_off()
        self.canvas.draw_idle()

    def atualizar(self, calculos, raizes, vertice, pontos):
        x_vertice = vertice[0]
        passo = max(1.0, abs(x_vertice) * 0.25)
        margem = 2.5 * passo
        limite_esquerdo = x_vertice - margem
        limite_direito = x_vertice + margem
        quantidade_pontos = 400
        passo_grafico = (limite_direito - limite_esquerdo) / (
            quantidade_pontos - 1
        )
        valores_x = [
            limite_esquerdo + indice * passo_grafico
            for indice in range(quantidade_pontos)
        ]
        try:
            valores_y = [
                calculos.a * x**2 + calculos.b * x + calculos.c
                for x in valores_x
            ]
        except OverflowError as erro:
            raise ValueError(
                "Não foi possível desenhar o gráfico com esses coeficientes."
            ) from erro
        if not all(math.isfinite(y) for y in valores_y):
            raise ValueError(
                "Não foi possível desenhar o gráfico com esses coeficientes."
            )

        self.eixos.clear()
        self.eixos.axhline(0, color="black", linewidth=0.8)
        self.eixos.axvline(0, color="black", linewidth=0.8)
        self.eixos.plot(
            valores_x,
            valores_y,
            label=(
                f"y = {calculos.a:g}x² + "
                f"{calculos.b:g}x + {calculos.c:g}"
            ),
        )
        self.eixos.scatter(
            [ponto[0] for ponto in pontos],
            [ponto[1] for ponto in pontos],
            color="tab:orange",
            label="Pontos calculados",
            zorder=3,
        )
        self.eixos.scatter(
            [vertice[0]],
            [vertice[1]],
            color="tab:red",
            label="Vértice",
            zorder=4,
        )

        raizes_reais = [
            raiz.real for raiz in raizes if abs(raiz.imag) < 1e-12
        ]
        if raizes_reais:
            self.eixos.scatter(
                raizes_reais,
                [0] * len(raizes_reais),
                color="tab:green",
                label="Raízes reais",
                zorder=4,
            )

        self.eixos.set_title("Gráfico da função quadrática")
        self.eixos.set_xlabel("x")
        self.eixos.set_ylabel("y")
        self.eixos.grid(True, alpha=0.3)
        self.eixos.legend()
        self.figura.tight_layout()
        self.canvas.draw_idle()
