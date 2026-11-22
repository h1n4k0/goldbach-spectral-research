# A signed four-prime giant-gap slice on the exact Dirichlet complement

Use the exact setup of the [full Dirichlet-width estimate](r35-source-square-root-dirichlet-arcs.md) and the [four-distinct-prime reduction](r38-source-four-distinct-prime-minor-reduction.md). Fix $0<\rho<1/2$, $0<\kappa\le1/2000$ and a sufficiently large even $N$, and set $L=\log N$, $I_0=[\rho N,(1-\rho)N]$. The first interval $I\subseteq I_0$ is any moving hard interval with either endpoint convention; the second remains $I_0$. Let

$$
 \mathcal Q=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\},
 \qquad Q_*=\lfloor\sqrt N\rfloor,\quad R=\lfloor Q_*L^{-200}\rfloor.
$$

The exact R35 set $\mathfrak D$ consists of the disjoint complete reduced arcs $\|\alpha-a/r\|\le1/(rQ_*)$ on $\mathbb T$ for $1\le r\le R$; put $\mathfrak m=\mathbb T\setminus\mathfrak D$ and $e(x)=e^{2\pi i x}$.

Consider the actual four-distinct-prime part of the product of genuine transforms $A_I A_{I_0}$ from R38. Both small constituents are in $\mathcal Q$, and both large constituents are primes coprime to $N$, with the original physical products in $I$ and $I_0$ respectively. For the *mask only*, orient by the two small primes: write $q>s$ for the larger and smaller small prime, $p$ for the large prime attached to $q$, and $v$ for the large prime attached to $s$. Thus the oriented products are $qp,sv$ and the signed gap is $h=v-p\ne0$. This orientation does not reassign the original two hard intervals.

For each possible smaller small prime $s$, prescribe any finite set $\mathcal H_s\subset\mathbb Z\setminus\{0\}$ of allowable signed gaps. These sets can depend on $N$ and need not be intervals, but are fixed as $I$ varies. Let $\mathcal P_I(\alpha)$ be the exact four-distinct-prime product expansion with only terms satisfying $h\in\mathcal H_s$, with the original marker $(\log q)(\log s)$. Both original product orderings are retained when allowed by $I,I_0$. Write $B=\sum_{s\in\mathcal Q}|\mathcal H_s|$.

**Theorem (unconditional).** Uniformly over the hard $I$,

$$
 \left|\int_{\mathfrak m}\mathcal P_I(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll B R L^4 .                                                   \tag{1}
$$

In particular the natural mask $\min(q,s)|p-v|\le H$ has signed contribution

$$
 O_{\rho,\kappa}(H\sqrt N\,L^{-196}) .                            \tag{2}
$$

Thus all four-distinct terms in this mask with $H=\sqrt N$ cost $O_{\rho,\kappa}(NL^{-196})$ on the exact complement. This controls that mask only, after the [synthetic-leg removal](r37-source-synthetic-localization-dirichlet-complement.md) and the repeated-prime reduction to the genuine four-prime term; it does not estimate the entire four-distinct contribution or a restricted product with a synthetic leg.

## 1. Multiplicity at every output integer

Before integration, expand $\mathcal P_I=\sum_M a_I(M)e(M\alpha)$. For fixed $M,s,h$ any actual tuple satisfies

$$
 M-sh=p(q+s).
$$

The right side is positive and at most $2qp\le2(1-\rho)N$ because $s<q$. Every physical constituent $p$ on the larger-small-prime side satisfies $p\ge\rho N^{1/2+\kappa}>\sqrt{2N}$ for large $N$. Thus the integer $M-sh$ has at most one possible prime divisor $p$ of the required size. If that prime exists then $q=(M-sh)/p-s$ and $v=p+h$ are uniquely determined. Primality, exact unit conditions, the four-distinct condition, and both hard cutoffs can only reduce the count. The two possible original orderings of these oriented products cost at most a factor of two. In particular every output obeys

$$
 0\le a_I(M)\le 2 B L^2 .                                       \tag{3}
$$

All four primes are odd for sufficiently large $N$, so only even $M$ arise; no bound requires ignoring or strengthening this parity restriction. Both physical products are in $I_0$, so the target displacement $k=M-N$ satisfies $|k|\le(1-2\rho)N$.

## 2. The exact R35 cutoff kernel has small truncated Fourier mass

For the disjoint complete arcs one has, for $k\ne0$,

$$
 \int_{\mathfrak D}e(k\alpha)\,d\alpha
  =\sum_{r\le R} c_r(k)\frac{\sin(2\pi k/(rQ_*))}{\pi k},
$$

where $c_r(k)=\sum_{a\bmod r}^{*}e(ka/r)$. Additivity here is for the exact $\mathfrak D$ itself; no higher-denominator arcs and no R34 union are used. At $k=0$ the integral is $|\mathfrak D|\le2R/Q_*$. From $c_r(k)=\sum_{d\mid(r,k)}d\mu(r/d)$, finite divisor switching yields

$$
 \sum_{1\le k\le N}\frac{|c_r(k)|}{k}
 \le\sum_{d\mid r}\sum_{1\le j\le N/d}\frac1j
 \ll L\,\tau(r).
$$

The same bound holds at negative $k$, and $\sum_{r\le R}\tau(r)\ll R(1+\log R)$. Therefore

$$
 \sum_{|k|\le N}
 \left|\int_{\mathfrak D}e(k\alpha)\,d\alpha\right|
 \ll R L^2 .                                                   \tag{4}
$$

Equations (3)–(4) bound the actual signed integral of $\mathcal P_I e(-N\alpha)$ on $\mathfrak D$ by $O(BRL^4)$. Its full-torus coefficient is $a_I(N)=O(BL^2)$. Subtracting the major integral gives (1) on the exact $\mathfrak m$. The argument requires no prime equidistribution or GRH, no smoothing of either hard interval, and no assumption on the sign of the minor integral.

For the geometric mask set $\mathcal H_s=\{h\in\mathbb Z:0<|h|\le H/s\}$. Then $B\le 2H\sum_{s\in\mathcal Q}1/s=O_\kappa(H)$ by the ordinary prime harmonic estimate over the polynomial range $[N^\kappa,N^{1/2-\kappa}]$. With $R\le\sqrt N L^{-200}$ this gives (2). As the masks and second leg are fixed, the moving first interval may also be integrated against the usual bounded-variation physical weight.

The geometric mask is not confined to repetitions or to bounded gaps. For example, using an auxiliary $X\to\infty$, choose $q>s$ among distinct primes in $[X^{1/4},(1+\epsilon)X^{1/4}]$ with fixed sufficiently small $\epsilon$ in terms of $\rho$. Split $[X^{3/4},(1+\epsilon)X^{3/4}]$ into intervals of length at most $X^{1/4}/4$. The ordinary prime number theorem and pigeonholing give a cell with $\gg_\epsilon X^{1/4}/\log X$ primes; its first and last provide $p,v$ whose gap lies between $\gg_\epsilon X^{1/4}/\log X$ and $X^{1/4}/4$. Now $N=qp+sv$ is even and comparable to $X$; all four primes are distinct and coprime to $N$, since each would otherwise divide the product on the other side. Both products are central for that choice of $\epsilon$, and $s|p-v|\le\sqrt N$. This shows the scope includes genuinely growing gaps on true eligible target tuples; it is not a signed lower bound and says nothing about the rest of the four-prime terms.
