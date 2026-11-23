# The actual nonsquarefree sharp correction is positive

**Scope.** The [complete sharp product](r63-spectral-full-integer-sharp-product.md) and [its squarefree restriction](r63-spectral-full-squarefree-crt-strip.md) have the same arithmetic prime baseline. We prove that the difference of their cutoff coefficients is strictly positive, with an explicit lower bound. After recording the available extra log precision of those two proofs, this gives a genuine signed asymptotic on the nonsquarefree partners alone. This does not count any extra prime pairs, give a claim on the exceptional moduli, or prove Hypothesis S.

Use the notation and exact cutoff $D_N=\sqrt N(\log N)^{-B}$ of the two proofs. Put $K_N=\varphi(N)/N$, $L=\log N$, and let $r$ be the least prime not dividing the even integer $N$; thus $r\ge3$. Their normalized cutoff coefficients satisfy

$$
       \mathcal D_N^{\rm all}-\mathcal D_N
                     \gg K_N^2\frac{\log r}{r^2}>0.              \tag{1}
$$

On the common good moduli, with the same arbitrary inverse-log exceptional-set order and simultaneously in all original cells,

$$
 \begin{split}
 \sum_{\substack{n\in I\\N-n\ {\rm nonsquarefree}}}
      \lambda(n)G_{D_N}(N-n)
  ={}&2\Sigma(N)(\mathcal D_N^{\rm all}-\mathcal D_N)
       \int_I \frac{\frac12\log(N-u)-\log D_N}{\log(N-u)}\,du\\
     &+O\!\left(\frac{\Sigma(N)H}{L^4}\right).
 \end{split}                                                      \tag{2}
$$

The main term is indeed positive and dominates the error for all sufficiently large good $N$. In particular this sign is for the **genuine signed** high coefficient on composites, not for an unsigned mass or a Goldbach representation count.

## 1. An exact Fourier comparison

Here primes dividing $N$ are inactive. Let $a_p=1/p$ and $s_p=(p-1)/(p^2-2)$ on the active primes. For an array such as $a$ or $s$, write $R_\alpha(t)=\sum_{h\le e^t}\mu(h)\alpha(h)$, extended by zero for $t<0$, with $\alpha(h)=\prod_{p\mid h}\alpha_p$ on squarefree $h$, including $\alpha_p=0$ on inactive primes. Write $R_{\alpha,j}$ for the same cumulative with $(h,j)=1$. Both are in $L^1\cap L^2$ by the reciprocal Mertens kernel bounds of the preceding proofs. Define

$$
 Q_\alpha=\sum_{j\ {\rm squarefree}}\mu(j)\alpha(j)^2
                                      \|R_{\alpha,j}\|_2^2.
$$

Thus $\mathcal D_N^{\rm all}=(K_N/\Sigma(N))Q_a$ and $\mathcal D_N=P_N Q_s$. The ratio of their outside Euler factors is

$$
   \frac{P_N}{K_N/\Sigma(N)}
       =\prod_{p\nmid N}(1-2/p^2).                               \tag{3}
$$

Indeed the local ratio at an inactive prime is one. At an active prime, multiply the squarefree factor $(1-1/p)^2(1+2r_p/p)$, where $r_p=(p-1)/(p-2)$, by $1-1/(p-1)^2$ from $\Sigma(N)K_N$ to obtain $1-2/p^2$ exactly.

For Fourier transform $\widehat R(\xi)=\int e^{-i\xi t}R(t)dt$, excluding a prime $p$ multiplies the transform by $(1-\alpha_p e^{-i\xi\log p})^{-1}$. This is convolution with the positive geometric log kernel of mass $(1-\alpha_p)^{-1}$. Plancherel gives

$$
 Q_\alpha=\frac1{2\pi}\int_{\mathbb R}
    |\widehat R_\alpha(\xi)|^2\,W_\alpha(\xi)\,d\xi,\qquad
 W_\alpha(\xi)=\prod_{p\nmid N}
     \left(1-\frac{\alpha_p^2}{|1-\alpha_p e^{-i\xi\log p}|^2}\right).
                                                                  \tag{4}
$$

The interchange follows from
$\sum_j|\mu(j)|\alpha(j)^2\prod_{p\mid j}(1-\alpha_p)^{-2}<\infty$. The product $W_\alpha$ converges uniformly and is bounded below by an absolute positive constant, since $\alpha_p\le1/p$, $p\ge3$, and $\prod_{p\ge3}(1-(p-1)^{-2})>0$.

Also $R_s$ is $R_a$ convolved with the uniformly bounded positive log kernel whose Fourier transform is
$\prod_{p\nmid N}(1-s_p e^{-i\xi\log p})/(1-a_p e^{-i\xi\log p})$. Local equality follows by dividing the two Möbius factors; the kernel is finite because $\sum_{p\nmid N}(a_p-s_p)<\infty$ and each local denominator has geometric mass at most $3/2$. In terms of the integrand $|\widehat R_a|^2W_a$, the combined effect of this transform and (3)–(4) is a product of the local ratios

$$
 \frac{(1-2/p^2)(1-2s_p\cos\theta)}{1-2a_p\cos\theta}
      =1-\frac{2(1-\cos\theta)}{p^2(1-2\cos\theta/p)},
                  \qquad \theta=\xi\log p .
                                                                  \tag{5}
$$

This identity follows by cancelling $|1-\alpha_p e^{-i\theta}|^2$ in (4); the denominator is positive. All factors are positive and at most one, and the product converges uniformly by $O(p^{-2})$ deviations. Use just the factor at $r$ to lower-bound the loss between one and that product. By (4) and the bound on $W_a$, the difference in (1) is at least an absolute positive multiple of

$$
 \frac{K_N}{\Sigma(N) r^2}\frac{1}{2\pi}
          \int_{\mathbb R}|\widehat R_a(\xi)|^2(1-\cos(\xi\log r))d\xi
       =\frac{K_N}{2\Sigma(N)r^2}
                \|R_a(\cdot)-R_a(\cdot-\log r)\|_2^2 .
$$

The norm square is at least $\log r$ since $R_a=1$ on $0\le t<\log r$ and the shifted function is zero there. Because $\Sigma(N)\asymp K_N^{-1}$ for even $N$, this proves (1).

## 2. Error precision and the genuine sign

In both preceding arithmetic proofs use the Bessel threshold $X\ell^{-J-4}$ instead of $X\ell^{-J-2}$ and the mean Ramanujan-tail threshold $\ell^{-4}$ instead of $\ell^{-2}$, where $\ell=\log X$ and $N\in[X,2X]$. This increases the exceptional-set upper bounds by factors $\ell^4$ and $\ell^2$, respectively. The displayed choices $E=A_0+4J+40$ and $C_0=10(E+1)$ already have more than this margin. The real Fourier-tail errors at retained $q$ and the superlogarithmic major errors likewise beat $H/L^4$. The original mesh width $X\ell^{-J-12}$ need not change: the original endpoint costs $O(X\ell^{-J-8}+X^{3/4}\ell^3)$ and $D$-change costs $O(X\ell^{-J-9}+X^{3/4}\ell^{B/2+2})$ beat $H/L^4$ by the direct-cut estimates. No moving roughness condition remains. On the model side the density and the frozen-$D$ variation are bounded by the explicit formulas and the uniform $O(1)$ cutoff coefficients, so the mesh changes are smaller still. This proves both earlier arithmetic equations with errors $O(\Sigma(N)H/L^4)$, after which their subtraction proves (2).

For the domination in (2), $K_N\gg1/\log L$ by Mertens' product splitting at $p=L$, and $r\ll L$ by the prime number theorem for $\sum_{p\le x}\log p$ (otherwise the product of the first $O(L)$-bounded primes dividing $N$ would exceed $N$). The gap (1) is therefore $\gg L^{-2}(\log L)^{-2}$. The central integral in (2) is $\asymp_B H(\log L)/L$, since $\frac12\log(N-u)-\log D_N=B\log L+O(1)$. Its main term is $\gg_B\Sigma(N)H/(L^3\log L)$, greater than the $O(\Sigma(N)H/L^4)$ error for all sufficiently large good $N$. There is no assertion for the exceptional moduli, for the absolute signed coefficient, or for any pointwise spectral condition.
