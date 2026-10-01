def formatar_numero(valor):
    if isinstance(valor, complex):
        parte_real = 0.0 if abs(valor.real) < 1e-12 else valor.real
        parte_imaginaria = 0.0 if abs(valor.imag) < 1e-12 else valor.imag
        if parte_imaginaria == 0:
            return f"{parte_real:.6g}"
        sinal = "+" if parte_imaginaria > 0 else "-"
        return f"{parte_real:.6g} {sinal} {abs(parte_imaginaria):.6g}i"
    return f"{valor:.6g}"


def exibir_resultados(delta, raizes, vertice, pontos):
    print("\n=== Resultados da equação ===")
    print(f"Delta: {formatar_numero(delta)}")
    print(f"Raiz 1: {formatar_numero(raizes[0])}")
    print(f"Raiz 2: {formatar_numero(raizes[1])}")
    print(
        "Vértice: "
        f"({formatar_numero(vertice[0])}, {formatar_numero(vertice[1])})"
    )
    print("Pontos da parábola:")
    for x, y in pontos:
        print(f"  ({formatar_numero(x)}, {formatar_numero(y)})")
