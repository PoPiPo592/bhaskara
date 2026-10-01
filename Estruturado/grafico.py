import matplotlib.pyplot as plt


def exibir_grafico(a, b, c, raizes, vertice, pontos):
    x_vertice = vertice[0]
    passo = max(1.0, abs(x_vertice) * 0.25)
    margem = 2.5 * passo
    limite_esquerdo = x_vertice - margem
    limite_direito = x_vertice + margem
    quantidade_pontos = 400
    passo_grafico = (limite_direito - limite_esquerdo) / (quantidade_pontos - 1)

    valores_x = [
        limite_esquerdo + indice * passo_grafico
        for indice in range(quantidade_pontos)
    ]
    valores_y = [a * x**2 + b * x + c for x in valores_x]

    plt.figure(figsize=(9, 6))
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.plot(valores_x, valores_y, label=f"y = {a:g}x² + {b:g}x + {c:g}")
    plt.scatter(
        [ponto[0] for ponto in pontos],
        [ponto[1] for ponto in pontos],
        color="tab:orange",
        label="Pontos calculados",
        zorder=3,
    )
    plt.scatter(
        [vertice[0]],
        [vertice[1]],
        color="tab:red",
        label="Vértice",
        zorder=4,
    )

    raizes_reais = [raiz.real for raiz in raizes if abs(raiz.imag) < 1e-12]
    if raizes_reais:
        plt.scatter(
            raizes_reais,
            [0] * len(raizes_reais),
            color="tab:green",
            label="Raízes reais",
            zorder=4,
        )

    plt.title("Gráfico da função quadrática")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
