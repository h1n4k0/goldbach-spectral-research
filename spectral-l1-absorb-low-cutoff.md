# Absorbing the first auxiliary cutoffs in a one-sided central test

**Scope.** The fixed low-cutoff correlations inside the [absolute profile](spectral-signed-rectangle-l1-no-jump.md) need not all be estimated to deduce a positive Goldbach lower bound. We absorb the first genuine terms exactly with their signs and then use ordinary squarefree exclusions. The remaining signed rectangle profile is not estimated here. The implication is arithmetic, does not assume GRH, and is not Hypothesis S.

Use $L=\log N$, $S=\mathfrak S(N)$, $a=1/2,b=9/16$, $Q_0=N/\lfloor\sqrt N L^{-C}\rfloor$ and the true central $B^+(t,y)$, $M_1(t)=\int_a^b|B^+(t,Nx)|\,dx$ of the [smooth bridge](spectral-signed-rectangle-smooth-bridge.md) and its addendum. Fix a nonzero $W\ge0$ in $C_c^1((a,b))$. Let
$$
 p_0=\min\{p\text{ prime}:p\nmid N\},\qquad
 T_0=\max(8,p_0+1),\qquad
 g_N=\max\!\left\{\frac{1}{p_0(p_0-1)},\ \frac{1}{L\log L}\right\},
$$
and define the remaining profile
$$
 \mathcal R_N=\int_{T_0}^{7Q_0/32}\frac{M_1(t)}t\,dt
               +\frac{L}{Q_0}\int_{7Q_0/32}^{Q_0/2}M_1(t)\,dt.
$$
For sufficiently large fixed $C$ (as in the smooth bridge), we prove that
$$
 \mathcal R_N=o(NSg_N)\quad\Longrightarrow\quad
 G_W\gg_W Sg_N.
 \tag{1}
$$
This gives $\gg_W NSg_N/L^2$ prime pairs on the support of the test, hence at least $\gg_W SN/(L^3\log L)$ uniformly and $\gg SN/L^2$ if $p_0$ stays bounded (with a constant also depending on that bound). One can replace $\mathcal R_N$ in the input by the shorter $\int_{T_0}^{\sqrt N L^{C_A}} M_1(t)\,dt/t$ using the [unconditional BV upper-tail deletion](spectral-l1-profile-upper-tail.md) with any fixed $A>4$ and $C>C_A+1$ sufficiently large. The input $o(NS/(L\log L))$ on this shorter profile is therefore a simpler sufficient condition for (1). The smaller uniform count guarantee is the tradeoff relative to the prior absolute-profile test.

## 1. Absorb the exact signed integral below $T_0$

Write $m=N-n$, and use the positive linear functional
$$
 \mathbb E_N[f]=\frac1N\sum_{\substack{aN<n\le bN\\(n,N)=1}}
         \Lambda(n)W(n/N)f(N-n).
$$
The model and short terms of the smooth bridge total $S\int W-S\mathbb E_N[\mu]+O_{A,W}(L^{-A})$. Its raw residual before normalizing is $-\sum_{n,q} W(n/N)\Delta_q(n)K(n/N,q)$, where
$$
 \Delta_q(n)=\mu(q)\Lambda(n)\mu(m)
       \left(\mathbf1_{q\mid m}-1/\varphi(q)\right)
 \quad\text{on } (q,N)=(n,N)=1.
$$
For the other pairs set $\Delta_q(n)=0$. Abel summation in $q$ changes this minus sign into the plus integral of $\partial_tK$ times the signed prefix, as $K$ vanishes at the top endpoint. For $t\le T_0=O(L)$ the smooth long multiplier $R$ is identically one and $\partial_tK=-1/t$; here $p_0\ll L$ follows from Chebyshev's lower bound just as in the original criterion. Keeping the exact sign below that cutoff gives
$$
 G_W=S\int W-\mathbb E_N[\mu C_N]
                +O_{A,W}(L^{-A}+\mathcal R_N/N),\qquad
 C_N(m)=S+\sum_{\substack{q<T_0\\(q,N)=1}}\mu(q)\log(T_0/q)
                \left(\mathbf1_{q\mid m}-1/\varphi(q)\right).
 \tag{2}
$$
Indeed a given $q<T_0$ is integrated on $q\le t\le T_0$ with weight $1/t$. No convention at an integer endpoint changes the integral and any term at $q=T_0$ has zero logarithm. The remainder above $T_0$ is bounded by the same second Abel estimate as in the absolute-profile addendum; its two weights remain $1/t$ and $L/Q_0$.

In (2), $q=1$ gives zero. If $T_0=8$, the contributing $q$ can only be $3,5,7$, since $2\mid N$ and $\mu$ rejects nonsquarefree integers. If $p_0>7$, only $q=p_0$ can occur: any other prime is either below $p_0$ (then it divides $N$) or at least $p_0+2$, and every nontrivial admissible composite is at least $p_0^2$. All surviving $q$ are primes, giving
$$
 C_N(m)=S-\sum_{\substack{p<T_0\\p\nmid N\\p\ {\rm prime}}}
           \log(T_0/p)\big(\mathbf1_{p\mid m}-1/(p-1)\big).
$$
When $T_0=8$ the most this can subtract from $S$ is
$$
 \tfrac12\log(8/3)+\tfrac34\log(8/5)+\tfrac56\log(8/7)
 < \tfrac12+\tfrac38+\tfrac5{42}=\tfrac{167}{168}<1.
$$
Here $e>8/3$, $e^{1/2}>8/5$ follow from the initial terms of their power series, and $\log(1+1/7)<1/7$. When $p_0>7$ even the unscaled $\log(1+1/p_0)$ is less than one. Since
$$
 S\ge 2\prod_{p\ge3}(1-1/(p-1)^2)
     \ge 2(1-\pi^2/24)>7/6 ,
$$
using $\sum_{p\ge3}(p-1)^{-2}\le\sum_{j\ge1}(2j)^{-2}=\pi^2/24$, we conclude $C_N(m)\ge S/7$ pointwise. This argument uses the original singular-series normalization and no boundedness of $S$.

## 2. Obtain a gap without any correlation estimate at these cutoffs

By the [ordinary Siegel–Walfisz theorem](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) (Montgomery–Vaughan, Corollary 11.19), and Abel summation against fixed $W$, the normalized unit mass of $m\equiv0\bmod h$ is
$$
 \mathbb E_N[\mathbf1_{h\mid m}]=\frac{\int W}{\varphi(h)}
                                  +O_{A,W}(L^{-A})
 \tag{3}
$$
for the coprime moduli $h=1,p,p_0^2,r^2,r^2s^2$ used here, all $O(L^4)$. In (3) the $n$-residue is $N\bmod h$, hence reduced. Imposing $(n,N)=1$ only removes prime powers supported on primes dividing $N$, of raw weight $O(L^2)$. In particular (3) applied to the finitely many primes $p<T_0$ actually present in (2) gives $\mathbb E_N[C_N]=S\int W+O_{A,W}(S L^{-A})$.

Let $E$ be any event implying that $m$ is divisible by a prime square. Since $\mu(m)\le1-\mathbf1_E$ and $C_N\ge S/7$, positivity of $\mathbb E_N$ gives
$$
 \mathbb E_N[\mu C_N]\le\mathbb E_N[C_N]-(S/7)\mathbb E_N[\mathbf1_E].
$$
Taking $E=\{p_0^2\mid m\}$, formula (3) gives $\mathbb E_N[\mathbf1_E]\gg_W1/[p_0(p_0-1)]$. Alternatively take $E=\{\exists r\in\mathcal P:r^2\mid m\}$ with $\mathcal P=\{r\text{ prime}:4L\le r\le8L,\ r\nmid N\}$. The PNT yields $\#\mathcal P\asymp L/\log L$, since at most $L/\log(4L)$ of the primes in this interval divide $N$. By the two-term Bonferroni inequality and (3),
$$
 \mathbb E_N[\mathbf1_E]\ \ge\
 (\int W)\!\left(h_N-\tfrac12 h_N^2\right) - O_{A,W}(L^{2-A}),
 \qquad
 h_N=\sum_{r\in\mathcal P}\frac1{r(r-1)}\asymp\frac1{L\log L}.
$$
The bound on the pair term uses the coprimality of distinct prime powers, and the errors cost at most $O(L^2)$ terms. Both choices of $E$ are legitimate, so one obtains a gap $\gg_W Sg_N$ from (2), with errors $O_{A,W}(S L^{-A}+\mathcal R_N/N)$ by choosing the Siegel–Walfisz saving large enough. This proves (1). Proper prime powers on either leg cost $O_W(N^{-1/2}L^2)$ in $G_W$, negligible relative to $Sg_N$; dividing by the maximum raw pair weight $O_W(L^2)$ gives the claimed count.

## 3. What this does and does not remove

In particular, when $3\nmid N$ the absolute profile through $t=3$ does control an actual fixed-$N$ $\Lambda(n)\mu(N-n)\chi_3(n)$ correlation, as described in the upper-tail note. Formula (2) instead bypasses that condition: it absorbs the signed contribution on $[3,4)$ as part of the coefficient $C_N$, without claiming the correlation is small. It also absorbs through $t=8$ and past the first nontrivial $q$ on every modulus. It neither supplies a bound on the remaining profile between $T_0$ and the square-root transition, nor establishes any Goldbach asymptotic or operator bound.
