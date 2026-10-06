import math
import re


def ler_coeficiente(nome):
    while True:
        valor_digitado = input(
            f"Digite o coeficiente {nome} (diferente de zero): "
        ).strip()
        if re.fullmatch(r"[0-9]+(?:[.,][0-9]+)?", valor_digitado) is None:
            print("Entrada inválida. Digite um número inteiro ou decimal usando ponto ou vírgula.")
            continue

        valor = float(valor_digitado.replace(",", "."))
        if not math.isfinite(valor):
            print("Entrada inválida. Digite um número finito.")
            continue
        if valor == 0:
            print(f"Entrada inválida. O coeficiente {nome} não pode ser zero.")
            continue
        return valor


def ler_coeficientes():
    coeficiente_a = ler_coeficiente("a")
    coeficiente_b = ler_coeficiente("b")
    coeficiente_c = ler_coeficiente("c")
    return coeficiente_a, coeficiente_b, coeficiente_c
