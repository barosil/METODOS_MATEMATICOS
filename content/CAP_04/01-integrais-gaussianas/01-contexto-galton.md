# Tópico em Contexto: O Tabuleiro de Galton

+++
Tabuleiro de Galton
+++

```{figure} imgs/content/cap-01/galton_board.png
:width: 60%
:name: galton-board
Tabuleiro de Galton ilustrando a convergência da distribuição binomial para a normal.
```

O tabuleiro de Galton é uma representação visual do Teorema Central do Limite. Bolas caem por uma série de obstáculos, desviando aleatoriamente à esquerda ou à direita. A distribuição das bolas no final se aproxima de uma curva em forma de sino — a distribuição normal.

Esse experimento mecânico ajuda a entender como a distribuição normal emerge da soma de muitas pequenas variações aleatórias.

+++
Demonstração Matemática
+++

A demonstração do Teorema Central do Limite será abordada no final da aula, após a apresentação das principais distribuições de probabilidade e da integral gaussiana. A versão simplificada do enunciado é:

```{math}
\lim_{n \to \infty} P\left( \frac{S_n - n\mu}{\sqrt{n\sigma^2}} \leq z \right) = \Phi(z)
```

:::{admonition} Observação
A função $\Phi(z)$ representa a função de distribuição acumulada da normal padrão. A demonstração completa envolve o uso de funções geradoras ou do método de Laplace.
:::
