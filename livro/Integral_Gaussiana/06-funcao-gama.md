# A Função Gama

## Histórico e Motivação

A função Gama foi introduzida por **Leonhard Euler** no século XVIII como uma generalização do fatorial para números reais:

```{math}
\Gamma(n) = \int_0^{\infty} x^{n-1} e^{-x} dx
```

Essa fórmula coincide com o fatorial para inteiros positivos:

```{math}
\Gamma(n) = (n-1)! \quad \text{para } n \in \mathbb{N}
```

## Propriedades da Função Gama

### Propriedade Recursiva

```{math}
\Gamma(z+1) = z \Gamma(z)
```

### Valor em 1/2

```{math}
\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}
```

### Continuação Analítica

A função Gama é meromorfa no plano complexo, com polos simples nos inteiros não positivos.

## Relação com a Integral Gaussiana

A integral gaussiana pode ser escrita como:

```{math}
\int_0^{\infty} e^{-x^2} dx = \frac{1}{2} \sqrt{\pi} = \frac{1}{2} \Gamma\left(\frac{1}{2}\right)
```

Mais geralmente:

```{math}
\int_0^{\infty} x^{s-1} e^{-\lambda x^2} dx = \frac{1}{2} \lambda^{-s/2} \Gamma\left(\frac{s}{2}\right)
```

## Aplicações

A função Gama aparece em:

* Estatística (distribuições Gama e Qui-quadrado)
* Física (modelagem de decaimentos, integrais de caminho)
* Cálculo de volumes de hiperesferas (ver próxima seção)

\:::{important}
A função Gama é essencial para estender muitos resultados da análise real para domínios mais amplos.
\:::
