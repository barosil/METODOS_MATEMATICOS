# Extensões da Integral Gaussiana

## Integral com Termo Linear

Consideremos a integral

```{math}
\int_{-\infty}^{\infty} e^{-a x^2 + bx} dx
```

Completa-se o quadrado:

```{math}
-ax^2 + bx = -a \left( x^2 - \frac{b}{a}x \right) = -a \left( x - \frac{b}{2a} \right)^2 + \frac{b^2}{4a}
```

Logo:

```{math}
\int_{-\infty}^{\infty} e^{-a x^2 + bx} dx = e^{\frac{b^2}{4a}} \int_{-\infty}^{\infty} e^{-a\left(x - \frac{b}{2a}\right)^2} dx = \sqrt{\frac{\pi}{a}} e^{\frac{b^2}{4a}}
```

## Integral com Termo Constante

Para:

```{math}
\int_{-\infty}^{\infty} e^{-a x^2 + bx + c} dx
```

O termo constante $c$ pode ser fatorado:

```{math}
= e^c \int_{-\infty}^{\infty} e^{-a x^2 + bx} dx = e^{c + \frac{b^2}{4a}} \sqrt{\frac{\pi}{a}}
```

## Aplicações

Essas integrais são comuns em:

* Mecânica estatística (funções de partição)
* Teoria quântica de campos (ações quadráticas)
* Processos estocásticos (funções características)

\:::{note}
As extensões da integral gaussiana também servem como base para o método de Laplace e a aproximação de integrandos oscilatórios.
\:::
