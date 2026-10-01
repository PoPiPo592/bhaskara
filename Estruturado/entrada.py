import math


def ler_coeficiente(nome):
    while True:
        valor_digitado = input(f"Digite o coeficiente {nome} (diferente de zero): ")
        try:
            valor = float(valor_digitado.strip().replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if not math.isfinite(valor):
            print("Entrada inválida. Digite um número finito.")
            continue
        if valor == 0:
            print("O coeficiente não pode ser zero.")
            continue
        return valor


def ler_coeficientes():
    coeficiente_a = ler_coeficiente("a")
    coeficiente_b = ler_coeficiente("b")
    coeficiente_c = ler_coeficiente("c")
    return coeficiente_a, coeficiente_b, coeficiente_c
