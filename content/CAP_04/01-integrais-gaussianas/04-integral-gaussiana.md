# A Integral Gaussiana

## Cálculo da Integral

A integral da função gaussiana é um resultado fundamental:

```{math}
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
```

Como a primitiva de $e^{-x^2}$ não é elementar, o método de resolução envolve a transformação em coordenadas polares.

## Método da Integral Dupla

Considere:

```{math}
I = \left( \int_{-\infty}^{\infty} e^{-x^2} dx \right)^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2 + y^2)} dx\,dy
```

Em coordenadas polares:

```{math}
I = \int_0^{2\pi} d\theta \int_0^{\infty} e^{-r^2} r\,dr
```

A substituição $u = r^2 \Rightarrow du = 2r\,dr$ leva a:

```{math}
I = 2\pi \cdot \frac{1}{2} \int_0^{\infty} e^{-u} du = \pi
```

Portanto:

```{math}
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
```

## Elemento de Volume e Métrica

Em coordenadas cartesianas:

```{math}
dA = dx\,dy
```

Em coordenadas polares, o elemento de área envolve o determinante da métrica:

```{math}
dA = \sqrt{g}\,dr\,d\theta = r\,dr\,d\theta
```

Aqui, $g = \det \begin{pmatrix}1 & 0 \\ 0 & r^2\end{pmatrix} = r^2$, então $\sqrt{g} = r$.

\:::{note}
Esse método será estendido mais adiante para o caso de $n$ dimensões.
\:::
