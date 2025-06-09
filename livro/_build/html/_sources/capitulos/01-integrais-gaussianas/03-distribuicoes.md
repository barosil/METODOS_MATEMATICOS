# Distribuições de Probabilidade

# Capítulo 03: Conceitos Fundamentais

Este capítulo apresenta os conceitos essenciais que servem como base matemática para o estudo das distribuições de probabilidade, integrais especiais e métodos estatísticos aplicados à física e outras áreas da ciência.

:::{admonition} Click here!
:class: tip, dropdown
```{include} 03-01-medidas.md
```
:::



## Conceitos Fundamentais

Uma **distribuição de probabilidade** descreve como a probabilidade é distribuída entre os possíveis valores de uma variável aleatória. Entre as propriedades básicas estão:

* Não-negatividade: $P(x) \geq 0$
* Normalização: $\sum_x P(x) = 1$ ou $\int P(x) dx = 1$
* Esperança: $\mathbb{E}[X] = \sum_x x P(x)$
* Variância: $\mathbb{V}[X] = \mathbb{E}[(X - \mu)^2]$

## Distribuições Discretas e Contínuas

### Distribuição Binomial

Modelo para o número de sucessos em $n$ ensaios de Bernoulli:

```{math}
P(k) = \binom{n}{k} p^k (1 - p)^{n - k}
```

### Distribuição de Poisson

Limite da binomial para $n \to \infty$ e $p \to 0$ com $\lambda = np$ fixo:

```{math}
P(k) = \frac{\lambda^k e^{-\lambda}}{k!}
```

### Distribuição Normal (Gaussiana)

Distribuição contínua simétrica em torno da média $\mu$:

```{math}
P(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
```

## O Teorema Central do Limite

\:::{admonition} Teorema Central do Limite
Se $X_i$ são variáveis aleatórias i.i.d. com média $\mu$ e variância $\sigma^2$, então:

```{math}
\frac{1}{\sqrt{n}} \sum_{i=1}^n (X_i - \mu) \xrightarrow{d} \mathcal{N}(0, \sigma^2)
```

\:::

Este teorema explica a ubiquidade da distribuição normal em fenômenos naturais: a soma de muitas pequenas contribuições aleatórias tende a uma distribuição gaussiana.

## Apêndices

### [Medida, Integração e Probabilidades](capitulos/01-integrais-gaussianas/03-01-medidas)

