# Pointwise major arcs for genuine sharp sums and the central Hardy profile

**Scope.** Under the stated Dirichlet GRH inputs, the original sharp central sums, the squarefree removed strip, and the genuine prime-pair count have their explicit main terms on polynomial-denominator major arcs for every modulus and every central prefix. This is not an estimate of the full arithmetic sums at a fixed modulus. It identifies the actual central Hardy compression with one signed minor-arc profile, and shows that a de-biased composite-only sharp profile differs from it by the true signed squarefree strip on those minor arcs. Neither residual minor term, the exterior, nor Hypothesis S is bounded here.

Let even $N$ be large, $L=\log N$, $D=\sqrt N L^{-B}$ with $B>0$ fixed, and $V=[N/3,2N]$. Use $Q=N^{1/1000}$ and let $\mathfrak M$ be the union on the torus of arcs $h/q+\eta$, $(h,q)=1$, $q\le Q$, $|\eta|\le2Q/N$. These arcs are disjoint for large $N$; $\mathfrak m$ denotes their complement. Write $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$, $m=N-n$, $\Sigma(N)$ for the singular series, and $\Delta(x)=\tfrac12\log x-\log D$.

The actual right coefficients, restricted to integer $m\in V$ and zero outside, are $A_{\rm p}=\mathbf1_{m\ {\rm prime}}$, $A_{\rm lo}=F_{0,D}$, $A_{\rm lo,sf}=\mu^2 F_{0,D}$, $A_{\rm hi}=G_D$, $A_{\rm hi,sf}=\mu^2 G_D$, and $A_\Xi=\mu^2\Xi_D$, with the original weak divisor gates $d\le D$, $G_D=F_{0,D}F_{1,D}-F_{0,D}$, and the [squarefree removed strict-midpoint strip](r63-spectral-full-squarefree-crt-strip.md). In particular

$$
 A_{\rm p}=A_{\rm hi,sf}+A_{\rm lo,sf}+A_\Xi
                                                                  \tag{1}
$$

at every positive integer in $V$. Write $\mathcal D_N$ and $\mathcal D_N^{\rm all}$ for the explicit coefficients of the [squarefree CRT](r63-spectral-full-squarefree-crt-strip.md) and [complete integer](r63-spectral-full-integer-sharp-product.md) calculations.

Assume Dirichlet GRH for the needed reciprocal-$L$ and prime progression estimates specified in Section 1. For any real half-open $I\subset(N/2,9N/16]$ and any bounded-variation weight $\omega(u)$ supported there with supremum and variation at most a fixed constant, set $P_{I,\omega}(\theta)=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$ and $\widehat A(\theta)=\sum_m A(m)e(m\theta)$. Then

$$
 \int_{\mathfrak M}P_{I,\omega}(\theta)\widehat A(\theta)e(-N\theta)\,d\theta
  =\int_I\omega(u)\mathcal L_A(N-u)\,du+\mathcal E_A,
                                                                  \tag{2}
$$

where $\mathcal E_{A_{\rm p}}=O(N^{1-10^{-4}})$, and for each of the five other rows $\mathcal E_A=O_{A',B}(NL^{-A'})$ for every fixed $A'>0$, uniformly even in both endpoints of $I$. The densities are

$$
 \begin{array}{c|c}
 A &\mathcal L_A(x)\\ \hline
 A_{\rm p} & \Sigma(N)/\log x\\
 A_{\rm lo},\, A_{\rm lo,sf} & 0\\
 A_{\rm hi} & \Sigma(N)(1+2\mathcal D_N^{\rm all}\Delta(x))/\log x\\
 A_{\rm hi,sf} & \Sigma(N)(1+2\mathcal D_N\Delta(x))/\log x\\
 A_\Xi & -2\Sigma(N)\mathcal D_N\Delta(x)/\log x .
 \end{array}                                                       \tag{3}
$$

The major comparison to the **exact completed real densities** has a power error in every row; reducing those densities to the displayed simple forms uses ordinary reciprocal Mertens bounds, giving the stated superlogarithmic errors on divisor rows.

## 1. The pointwise transfer

For primes, the historical GRH progression error in each reduced class is $O(\sqrt Y(\log N)^2)$ at $Y\le2N$, after the trivial proper-power error. The [GRH reciprocal-$L$ and Perron estimates](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums), equations (2)–(3), give a masked Möbius transform $O_\epsilon(Y^{1/2}N^\epsilon)$ for each nonprincipal character of modulus $q\le Q$, on every scale $N^{\epsilon_0}\le Y\le2N$ with fixed $\epsilon_0>0$. This includes extra coprimality masks of polynomial size. For the principal use [Titchmarsh, Theorem 14.25(C)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), the ordinary RH estimate $\sum_{n\le Y}\mu(n)=O_\epsilon(Y^{1/2+\epsilon})$. The exact coprimality mask is convolution with the indicator of integers supported on the mask's primes. Its weighted reciprocal sum at exponent $1/2+\epsilon$ costs $N^{o(1)}$ for a polynomial-sized mask $w$: $\prod_{p\mid w}(1-p^{-1/2-\epsilon})^{-1}\le\exp(O(\sqrt L))$ by splitting the primes at $L$ and bounding the tail by the number of large prime divisors of $w$. Thus the principal bound with the required $N^\epsilon$ loss follows as well. These inputs hold under global Dirichlet GRH; one must not replace this input by GRH solely for the characters modulo $N$.

The Möbius bound holds per arbitrary residue by character orthogonality and reduction to a unit class: if $g=(a,q)$ and $n\equiv a\bmod q$, write $n=gv$. The terms vanish unless $g$ is squarefree and $(v,g)=1$, and then are $\mu(g)\mu(v)$ on the reduced class $a/g\bmod q/g$ with an enlarged finite mask. The actual long signed scales below are at least $N^{.1}$ before this division and $g\le N^{.001}$, so no short-scale issue occurs. In the prime polynomials contributing here, no prime dividing $q$ is in the support, since both prime variables have size comparable to $N$. Summing at most $q$ progression errors and partial summation against the slow phase (variation $O(1+Q)$) gives major errors $O_\epsilon(N^{1/2+\epsilon}Q^2)$ for the first prime polynomial and the prime-indicator polynomial. Their real densities are $\mathbf1_I\omega$ and $\mathbf1_V/\log x$, each multiplied by $\mu(q)/\varphi(q)$.

For the sharp sums use the exact $abcd=m$ decompositions of the [complete integer](r63-spectral-full-integer-sharp-product.md) and [squarefree](r63-spectral-full-squarefree-crt-strip.md) proofs. Large signed sectors $b>N^{.1}$, or $c>N^{.1}$ with $b\le N^{.1}$, are pointwise $O_\epsilon(N^{1-1/20+\epsilon}Q^2L^3)$ on every major arc. Indeed the chosen variable has scale $Y\asymp N/s\gg N^{.1}$ for the other-factor product $s$; its actual inequalities form an interval, with the same monotone centered weight and coprimality masks as in those proofs. Apply the GRH bound per residue, sum at most $q$ residues, and pay $O(1+Q)$ variation. Replacing $\sqrt{N/s}$ by $(N/s)N^{-1/20}$ then leaves only the triple harmonic sum $O(L^3)$. These are signed estimates for the actual discarded sectors, not deletions by absolute values.

In the remaining $b,c$ bulk the actual $d$ has scale at least $N^{.39}$. In the unrestricted product, its complete periods cost $O(q(1+Q))$ per triple and retain exactly $q\mid abc$. In the squarefree strip, the original local CRT count for squarefree $d$ coprime to $abc$ has error $\tau(abc)\sqrt Y$ per residue, so costs $O_\epsilon(\sqrt{N/(abc)}N^\epsilon Q^2)$ per triple including variation. Both save a fixed power on summing the triple reciprocals. The additional squarefree $a$-average has $a>N^{.39}$ and Euler convolution moment $O_\epsilon(q^3(bc)^\epsilon)$ in equation (7) of the squarefree proof: each $p\mid q$ factor at exponent $3/4$ is at most $p^3$ by its two explicit coefficients. Its prefactor is at most $q^2$; partial summation costs $O_\epsilon(N^{-.39/4+\epsilon}Q^5 L^{O(1)})$ in the real density. Low terms are easier with $d\gg N^{.49}$, using the same squarefree or unrestricted $d$ count. These calculations produce the exact same right densities as those earlier proofs, with total uniform polynomial error $O(N^{.96})$. The first prime approximation supplies a smaller error. Only squarefree $q$ require a right density since the first main factor vanishes otherwise. The intervals and $D$ already belong to the current $N$; no mesh or averaging over $N$ is used.

For clarity, completion of the rational series is also pointwise. On squarefree $q$, the right densities including their rational factor satisfy the earlier bound $O(L^3 C_1^{\omega(q)}/q)$ in supremum and variation, uniformly over $x\in V$, also for the prime row. Each $p\mid q$ forces occupation and gains $1/p$ in a divisor reciprocal sum, or saves $1/p$ in the corresponding squarefree factor. The Fourier tails after extending the retained convolution integrals to the real line are $O(NQ^{-1} L^3(\log(2Q))^{C_2})$, by the two variations and summing these coefficients. Substitution of the polynomial approximants costs $O(N^{.96} Q^3 L^{O(1)})$, since the total arc measure is $O(Q^3/N)$ and the polynomials have size at most $NL^{O(1)}$.

To estimate the unretained rational tail at **each** $N$, the squarefree inequality $|c_q(N)|\le(q,N)$ gives

$$
 \sum_{\substack{q>Q\\q\ {\rm squarefree}}}
      \frac{C_1^{\omega(q)}|c_q(N)|}{q\varphi(q)}
  \ll_\epsilon Q^{-1/4}
       \prod_{p\mid N}(1+O(p^{-3/4}))
       \prod_{p\nmid N}(1+O(p^{-7/4}))
  \ll_\epsilon Q^{-1/4}N^\epsilon .
                                                                  \tag{4}
$$

The second product converges, and all sufficiently large prime factors of the first are at most $p^\epsilon$. With $\epsilon=1/20000$ this is enough even after multiplying by $NL^3$. The other Fourier errors above beat $N^{1-10^{-4}}$ as well. The completely summed densities are exactly the deterministic CRT and harmonic evaluations of the cited proofs: the prime baseline $\Sigma(N)/\log x$ is exact; the divisor rows differ from (3) by arbitrary inverse powers of $L$ uniformly in $x$. The high squarefree row also follows from (1). This proves (2)–(3) without using their earlier good-modulus conclusions.

## 2. The genuine Hardy link

Write $a=1/2$, $b=9/16$, $w(v)=\sqrt{v(1-v)}$, $M(x)=\int_a^xw(v)\,dv$. For $x\in[a,b]$ choose the exact $I_x=(aN,xN]$ and $\omega_N(u)=w(u/N)\log(N-u)/L$, of uniformly bounded variation. Define

$$
 \mathcal C_{A,N}(x)=\frac L N\int_{\mathfrak m}
      P_{I_x,\omega_N}(\theta)\widehat A(\theta)e(-N\theta)\,d\theta,
 \qquad
 E_N(x)=\int_a^x w(v)\Delta(N(1-v))\,dv.
                                                                  \tag{5}
$$

The original strict upper-half Hardy arithmetic profile is

$$
 F_N(x)=\frac1N\sum_{\substack{aN<n\le xN\\(n,N)=1}}
    \Lambda(n)\Lambda(N-n)w(n/N)-\Sigma(N)M(x).
$$

Proper prime powers cost $O(L^2/\sqrt N)$ uniformly; on the remaining prime-prime pairs the unit condition is automatic in this strict half-window. Thus the prime row alone gives $F_N(x)=\mathcal C_{A_{\rm p},N}(x)+O(N^{-1/20000})$ uniformly in $x$. The [exact symmetric central kernel comparison](spectral-weak-s-central-threshold.md#3-a-smaller-target-one-strict-central-half-and-a-one-sided-real-probe), with local GRH(N) for its spectral interpretation, is $\|T_N^{\rm central}\|\asymp\|F_N\|_{L^2[a,b]}$. In particular this compares the original central compression to the norm of the actual signed minor profile, with the displayed vanishing additive arithmetic error. There is no implication for the full operator.

For $*={\rm sf},{\rm all}$ let $A_{\rm hi,*}$ be the corresponding row, with $\mathcal D_N^*=\mathcal D_N,\mathcal D_N^{\rm all}$, and define the corrected genuine sharp profile

$$
 \mathcal H_{*,N}(x)=
      \frac L N\sum_{n\in I_x}\lambda(n)\omega_N(n)A_{\rm hi,*}(N-n)
        -\Sigma(N)M(x)-2\Sigma(N)\mathcal D_N^*E_N(x).
                                                                  \tag{6}
$$

Formula (2) gives $\mathcal H_{*,N}(x)=\mathcal C_{A_{\rm hi,*},N}(x)+O_{A',B}(L^{-A'})$ for every fixed $A'>0$. This is a composite-only surrogate: $G_D=0$ on primes in $V$, since each linear divisor sum is one there. The exact genuine identity (1) now implies

$$
 F_N(x)-\mathcal H_{{\rm sf},N}(x)
     =\mathcal C_{A_\Xi,N}(x)+\mathcal C_{A_{\rm lo,sf},N}(x)
                      +O_{A',B}(L^{-A'}).                         \tag{7}
$$

For any fixed requested accuracy choose $B$ sufficiently large as in the [pointwise BV low-block theorem](spectral-midpoint-complete-low-squarefree-bv.md). Partial summation in the true $\omega_N$ and the low major formula show $\mathcal C_{A_{\rm lo,sf},N}(x)=O(L^{-A'})$ for every even $N$ at this fixed cutoff (increase the exponent in that theorem before choosing $B$). Equation (7) therefore leaves exactly the **signed removed-strip minor term** as the gap between the corrected sharp profile and the original Hardy one. Its major term has a definite sign, but this gives no sign or bound on its individual-modulus minor term. The corrected composite profile's own minor term likewise remains uncontrolled on each modulus. These are two genuine arithmetic targets, not consequences of the previously obtained density-one main terms.
