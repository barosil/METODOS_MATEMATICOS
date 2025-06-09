# Conceitos Fundamentais: Probabilidade e Estatística

::::md

```{prf:definition}
:label: espaco-amostral

O **espaço amostral** $\Omega$ é o conjunto de todos os resultados possíveis de um experimento aleatório.
```

::::


::: definition Variável Aleatória
Uma **variável aleatória** é uma função mensurável $X : \Omega \to \mathbb{R}$, que associa um número real a cada resultado $\omega \in \Omega$.
:::

::: definition Medida de Probabilidade
Uma **medida de probabilidade** $P$ é uma medida definida sobre uma $\sigma$-álgebra $\mathcal{F}$ tal que $P(\Omega) = 1$.
:::

::: definition Distribuição de Probabilidade Discreta
Uma **distribuição de probabilidade discreta** é uma função $p: \mathbb{N} \to [0,1]$ tal que $\sum_i p(i) = 1$.
:::

::: definition Função de Distribuição de Probabilidade
A **função de distribuição de probabilidade** $f_X(x)$ descreve a probabilidade de uma variável aleatória $X$ assumir um valor específico $x$: $P(X = x) = f_X(x)$.
:::

::: definition Distribuição de Probabilidade Cumulativa
A **função de distribuição acumulada** $F_X(x)$ é dada por $F_X(x) = P(X \leq x)$.
:::

::: definition Axiomas de Kolmogorov
Os três axiomas fundamentais da probabilidade são:

1. $P(A) \geq 0$;
2. $P(\Omega) = 1$;
3. Para eventos disjuntos $A_i$, $P\left(\bigcup_i A_i\right) = \sum_i P(A_i)$.
   :::

::: definition Lei dos Grandes Números
A **Lei dos Grandes Números** afirma que a média amostral converge para a média esperada quando o número de observações tende ao infinito.
:::

::: definition Teorema Central do Limite
O **Teorema Central do Limite** estabelece que, sob certas condições, a soma de variáveis aleatórias independentes e identicamente distribuídas converge para uma distribuição normal.
:::

::: definition Momentos
Os **momentos** de uma variável aleatória $X$ são valores esperados de potências de $X$: $E[X^n]$.
:::

::: definition Função Geradora de Momentos
A **função geradora de momentos** $M_X(t)$ é definida como:

```{math}
M_X(t) = E[e^{tX}]
```

:::

::: definition Função Característica
A **função característica** $\varphi_X(t)$ é definida como:

```{math}
\varphi_X(t) = E[e^{itX}]
```

:::

::: definition Paradoxo de Bertrand
O **Paradoxo de Bertrand** mostra que diferentes métodos de escolher aleatoriamente uma corda em um círculo levam a diferentes probabilidades — destacando ambiguidades na definição de "aleatoriedade".
:::
