import math
import tkinter as tk
from tkinter import messagebox, ttk

from calculos import Calculos
from grafico import Grafico
from resultados import Resultados


class InterfaceBhaskara:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora de Bhaskara")
        self.janela.geometry("1050x720")
        self.janela.minsize(820, 600)

        self.campos = {}
        self.resultados = Resultados()
        self._montar_interface()

    def _montar_interface(self):
        conteudo = ttk.Frame(self.janela, padding=18)
        conteudo.pack(fill="both", expand=True)
        conteudo.columnconfigure(0, weight=1)
        conteudo.rowconfigure(2, weight=1)

        ttk.Label(
            conteudo,
            text="Calculadora de Bhaskara",
            font=("TkDefaultFont", 18, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 14))

        quadro_entrada = ttk.LabelFrame(
            conteudo, text="Coeficientes da equação ax² + bx + c = 0", padding=12
        )
        quadro_entrada.grid(row=1, column=0, sticky="ew", pady=(0, 14))
        for coluna, (nome, descricao) in enumerate(
            (("a", "Coeficiente a"), ("b", "Coeficiente b"), ("c", "Coeficiente c"))
        ):
            quadro_entrada.columnconfigure(coluna, weight=1)
            ttk.Label(quadro_entrada, text=descricao).grid(
                row=0, column=coluna, sticky="w", padx=6, pady=(0, 5)
            )
            variavel = tk.StringVar()
            campo = ttk.Entry(quadro_entrada, textvariable=variavel, width=18)
            campo.grid(row=1, column=coluna, sticky="ew", padx=6)
            self.campos[nome] = (variavel, campo)

        self.campos["a"][1].focus_set()
        ttk.Button(
            quadro_entrada,
            text="Calcular",
            command=self.calcular,
        ).grid(row=1, column=3, padx=(12, 6), sticky="ew")

        area_resultados = ttk.Frame(conteudo)
        area_resultados.grid(row=2, column=0, sticky="nsew")
        area_resultados.columnconfigure(0, weight=1, uniform="area")
        area_resultados.columnconfigure(1, weight=2, uniform="area")
        area_resultados.rowconfigure(0, weight=1)

        quadro_resultados = ttk.LabelFrame(
            area_resultados, text="Resultados", padding=12
        )
        quadro_resultados.grid(
            row=0, column=0, sticky="nsew", padx=(0, 10)
        )
        quadro_resultados.columnconfigure(0, weight=1)
        quadro_resultados.rowconfigure(0, weight=1)
        self.texto_resultados = tk.StringVar(
            value="Os resultados aparecerão aqui."
        )
        ttk.Label(
            quadro_resultados,
            textvariable=self.texto_resultados,
            justify="left",
            anchor="nw",
            wraplength=310,
        ).grid(row=0, column=0, sticky="new")

        quadro_grafico = ttk.LabelFrame(
            area_resultados, text="Parábola", padding=8
        )
        quadro_grafico.grid(row=0, column=1, sticky="nsew")
        self.grafico = Grafico(quadro_grafico)

    def _ler_coeficientes(self):
        valores = []
        for nome in ("a", "b", "c"):
            texto = self.campos[nome][0].get().strip().replace(",", ".")
            try:
                valor = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Entrada inválida",
                    f"Digite um número válido para o coeficiente {nome}.",
                    parent=self.janela,
                )
                self.campos[nome][1].focus_set()
                return None

            if not math.isfinite(valor):
                messagebox.showerror(
                    "Entrada inválida",
                    f"O coeficiente {nome} deve ser um número finito.",
                    parent=self.janela,
                )
                self.campos[nome][1].focus_set()
                return None
            if valor == 0:
                messagebox.showerror(
                    "Entrada inválida",
                    f"O coeficiente {nome} não pode ser zero.",
                    parent=self.janela,
                )
                self.campos[nome][1].focus_set()
                return None
            valores.append(valor)
        return valores

    def calcular(self):
        coeficientes = self._ler_coeficientes()
        if coeficientes is None:
            return

        try:
            calculos = Calculos(*coeficientes)
            delta = calculos.calcular_delta()
            raizes = calculos.calcular_raizes(delta)
            vertice = calculos.calcular_vertice(delta)
            pontos = calculos.calcular_pontos(vertice[0])
            texto = self.resultados.formatar_resultados(
                delta, raizes, vertice, pontos
            )
            self.grafico.atualizar(calculos, raizes, vertice, pontos)
        except ValueError as erro:
            messagebox.showerror(
                "Erro de cálculo",
                str(erro),
                parent=self.janela,
            )
            return

        self.texto_resultados.set(texto)

    def executar(self):
        self.janela.mainloop()
