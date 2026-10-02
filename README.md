# Calculadora de Bhaskara

Este repositório reúne três versões de uma calculadora para equações do segundo
grau na forma `ax² + bx + c = 0`. As versões calculam o discriminante (delta),
as raízes, o vértice da parábola e pontos para representar a função em um
gráfico. O coeficiente `a` não pode ser zero.

## Requisitos

- Python 3.11
- Matplotlib
- Tkinter para a versão com interface gráfica (normalmente incluído com Python;
  em algumas distribuições Linux, pode ser necessário instalar o pacote do
  sistema `python3-tk`)

Na raiz do repositório, crie e ative um ambiente virtual e instale o Matplotlib:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install matplotlib
```

No Windows, ative o ambiente com `.venv\Scripts\activate` em vez do comando
`source`.

## Versões e execução

Execute os comandos a seguir a partir da raiz do repositório, com o ambiente
virtual ativado.

### Estruturado

Organiza o programa em funções separadas para entrada, cálculos, apresentação
dos resultados e gráfico.

```bash
python Estruturado/main.py
```

### OOP

Usa classes para representar as responsabilidades da aplicação, como cálculos,
entrada, resultados e gráfico. A interação ocorre pelo terminal.

```bash
python OOP/main.py
```

### OOP_Janelas

Combina a organização orientada a objetos com uma interface gráfica Tkinter.
Permite informar os coeficientes em campos, visualizar os resultados na janela
e consultar o gráfico incorporado à interface.

```bash
python OOP_Janelas/main.py
```

## Comparação breve

| Versão | Organização | Interação |
| --- | --- | --- |
| **Estruturado** | Funções agrupadas por responsabilidade; abordagem direta e procedural. | Terminal e janela separada para o gráfico. |
| **OOP** | Classes encapsulam cálculos, entrada, resultados e gráfico; favorece a separação de responsabilidades. | Terminal e janela separada para o gráfico. |
| **OOP_Janelas** | Mantém classes para os cálculos e componentes da aplicação, acrescentando uma interface gráfica. | Janela Tkinter com resultados e gráfico integrados. |
