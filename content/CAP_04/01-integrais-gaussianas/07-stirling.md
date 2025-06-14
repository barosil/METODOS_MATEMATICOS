# Aproximação de Stirling

A fórmula de Stirling fornece uma estimativa assintótica para o fatorial, útil para grandes valores de $n$:

```{math}
n! \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
```

Em termos da função Gama:

```{math}
\Gamma(n+1) \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
```

## Dedução (esboço)

A aproximação pode ser obtida a partir de métodos do tipo Laplace, aplicando a expansão da função logarítmica:

```{math}
\log n! = \sum_{k=1}^n \log k \approx \int_1^n \log x\,dx = n \log n - n + 1
```

Refinando essa aproximação e aplicando o método de Laplace à integral de Euler para $\Gamma(n+1)$:

```{math}
\Gamma(n+1) = \int_0^{\infty} x^n e^{-x} dx \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
```

## Aplicações

A fórmula de Stirling é amplamente usada para:

* Estimativas de crescimento assintótico
* Cálculo aproximado de probabilidades (ex: binomial, Poisson)
* Entropia e informação (teoria da informação)
* Análise combinatória

\:::{tip}
Versões refinadas incluem termos corretivos como:

```{math}
n! \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \left(1 + \frac{1}{12n} + \cdots \right)
```

\:::
