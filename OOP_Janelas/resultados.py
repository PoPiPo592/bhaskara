class Resultados:
    def formatar_numero(self, valor):
        if isinstance(valor, complex):
            parte_real = 0.0 if abs(valor.real) < 1e-12 else valor.real
            parte_imaginaria = 0.0 if abs(valor.imag) < 1e-12 else valor.imag
            if parte_imaginaria == 0:
                return f"{parte_real:.6g}"
            sinal = "+" if parte_imaginaria > 0 else "-"
            return f"{parte_real:.6g} {sinal} {abs(parte_imaginaria):.6g}i"
        return f"{valor:.6g}"

    def formatar_resultados(self, delta, raizes, vertice, pontos):
        linhas = [
            f"Delta: {self.formatar_numero(delta)}",
            f"Raiz 1: {self.formatar_numero(raizes[0])}",
            f"Raiz 2: {self.formatar_numero(raizes[1])}",
            (
                "Vértice: "
                f"({self.formatar_numero(vertice[0])}, "
                f"{self.formatar_numero(vertice[1])})"
            ),
            "",
            "Pontos da parábola:",
        ]
        linhas.extend(
            f"({self.formatar_numero(x)}, {self.formatar_numero(y)})"
            for x, y in pontos
        )
        return "\n".join(linhas)
