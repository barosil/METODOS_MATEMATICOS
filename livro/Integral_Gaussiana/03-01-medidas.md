# Conceitos Fundamentais: Teoria de Conjuntos, Medidas e Integração

::: definition Topologia
Uma **topologia** em um conjunto $X$ é uma coleção $\mathcal{T} \subseteq 2^X$ de subconjuntos de $X$, chamados de abertos, tal que:

1. $\emptyset, X \in \mathcal{T}$;
2. A união arbitrária de conjuntos em $\mathcal{T}$ pertence a $\mathcal{T}$;
3. A interseção finita de conjuntos em $\mathcal{T}$ também pertence a $\mathcal{T}$.
   :::

::: definition $\sigma$-Álgebra
Uma **$\sigma$-álgebra** sobre um conjunto $X$ é uma coleção $\mathcal{F} \subseteq 2^X$ tal que:

1. $X \in \mathcal{F}$;
2. Se $A \in \mathcal{F}$, então $A^c \in \mathcal{F}$;
3. Se $A_1, A_2, \ldots \in \mathcal{F}$, então $\bigcup_{i=1}^\infty A_i \in \mathcal{F}$.
   :::

::: definition Medida
Uma **medida** é uma função $\mu : \mathcal{F} \to [0, \infty]$ definida em uma $\sigma$-álgebra $\mathcal{F}$, tal que:

* $\mu(\emptyset) = 0$;# Conceitos Fundamentais: Probabilidade e Estatística

::: definition Espaço Amostral
O **espaço amostral** $\Omega$ é o conjunto de todos os resultados possíveis de um experimento aleatório.
:::

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

* $\mu$ é $\sigma$-aditiva: se $A_i \in \mathcal{F}$ são disjuntos dois a dois, então
  $\mu\left( \bigcup_i A_i \right) = \sum_i \mu(A_i)$.
  :::

::: definition Função Mensurável
Uma função $f: X \to \mathbb{R} \cup \{\pm\infty\}$ é **mensurável** se, para todo $a \in \mathbb{R}$, o conjunto $\{x \in X : f(x) > a\}$ pertence à $\sigma$-álgebra $\mathcal{F}$.
:::

::: definition Integral de Lebesgue
A **integral de Lebesgue** de uma função mensurável $f$ em relação a uma medida $\mu$ é definida como:

```{math}
\int_X f \, d\mu := \sup\left\{\int_X s \, d\mu : s \leq f, s \text{ simples} \right\}
```

Essa definição permite integrar funções mais gerais do que a integral de Riemann.
:::




