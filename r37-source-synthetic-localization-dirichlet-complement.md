# The actual synthetic leg is negligible on the exact Dirichlet complement

Use the exact setup of the [full Dirichlet-width estimate](r35-source-square-root-dirichlet-arcs.md). Fix $0<\rho<1/2$ and $0<\kappa\le1/2000$. Let $N$ be sufficiently large and even, $L=\log N$, $I_0=[\rho N,(1-\rho)N]$, and $I\subseteq I_0$ any moving hard interval with either endpoint convention. Let $\mathcal Q$ be the primes $N^\kappa\le q\le N^{1/2-\kappa}$ that are coprime to $N$, $z=\kappa L/1000$, $W=\prod_{\ell\le z,\ \ell\nmid N}\ell$ over primes, $M=\operatorname{rad}(NW)$, and $K=M/\varphi(M)$. Write $e(x)=e^{2\pi ix}$ and use the actual transforms

$$
\begin{aligned}
 A_I(\alpha)&=\sum_{q\in\mathcal Q}(\log q)
   \sum_{\substack{p\ {\rm prime}\\qp\in I,\ (p,N)=1}}e(\alpha qp),\\
 B_I(\alpha)&=K\sum_{q\in\mathcal Q}(\log q)
   \sum_{\substack{p\ge1\\qp\in I,\ (p,M)=1}}\frac{e(\alpha qp)}{\log p}.
\end{aligned}
$$

The second sum only contains $p>1$ for large $N$. The combined unit condition $(p,M)=1$ is exactly the product of the two original unit masks, so $F_I=A_I-B_I$ is unchanged from R35.

Let $Q_*=\lfloor\sqrt N\rfloor$, $R=\lfloor Q_* L^{-200}\rfloor$, and $\mathfrak D$ be the union of the complete reduced arcs $\|\alpha-a/r\|\le1/(rQ_*)$ on $\mathbb T$ for $1\le r\le R$. Write $\mathfrak m=\mathbb T\setminus\mathfrak D$. Then, **unconditionally**,

$$
 \int_{\mathfrak m}|B_I(\alpha)|^2\,d\alpha
 \ll_{\rho,\kappa} N^{1-\kappa/4},                       \tag{1}
$$

uniformly over the original hard $I$. Consequently the actual signed integral has the unconditional replacement

$$
 \int_{\mathfrak m}F_I F_{I_0}e(-N\alpha)\,d\alpha
 =\int_{\mathfrak m}A_I A_{I_0}e(-N\alpha)\,d\alpha
    +O_{\rho,\kappa}(N^{1-\kappa/10}).                   \tag{2}
$$

No signed bound for the surviving genuine–genuine integral is asserted. If one also assumes the global Dirichlet GRH of R35, its major estimate then gives

$$
 [\xi,\xi]_I
 =\int_{\mathfrak m} A_I A_{I_0}e(-N\alpha)\,d\alpha
     +O_{\rho,\kappa}\!\left(\frac{\mathfrak S(N)N}{L\log L}
                         +N^{1-\kappa/10}\right),       \tag{3}
$$

where $[\xi,\xi]_I=\int_{\mathbb T}F_I F_{I_0}e(-N\alpha)\,d\alpha$ is the unchanged same-target covariance.

## Removing the hard edge and long divisors

Set $H=N^{\kappa/3}$ and $\varepsilon=N^{-\kappa/3}$. Smooth the indicator of $I/N$ by convolution with a nonnegative mass-one bump supported in $[-\varepsilon,\varepsilon]$, giving $w_I(u)\in[0,1]$ with derivative bounds $O_j(\varepsilon^{-j})$. For sufficiently large $N$ its support lies in $[\rho/2,1-\rho/2]$. An allowed singleton endpoint contributes only to the following edge error. Denote by $B_w$ the transform with $w_I(qp/N)$ instead of the hard interval. For each integer $n$ in this support there are at most $1/\kappa$ eligible prime divisors $q$, and $\log q/\log(n/q)=O_\rho(1)$. Thus Parseval on the torus gives

$$
 \|B_I-B_w\|_2^2\ll_{\rho,\kappa} K^2(\varepsilon N+1).   \tag{4}
$$

Use the exact Boolean expansion $\mathbf1_{(p,M)=1}=\sum_{h\mid M,h\mid p}\mu(h)$. Decompose $B_w=B_{w,\le H}+B_{w,>H}$ accordingly, retaining every $p$ of each divisibility class. The latter has squared norm

$$
 \|B_{w,>H}\|_2^2
 \ll_{\rho,\kappa}
 K^2\tau(M)\sum_{q\in\mathcal Q}\sum_{\substack{h\mid M\\h>H}}\frac{N}{qh}
 \ll_{\rho,\kappa} NK^2\tau(M)^2 L/H .                   \tag{5}
$$

Indeed the Fourier coefficient at $n$ is a sum of at most $O_\kappa(\tau(M))$ terms, each bounded by $O_\rho(K)$; after Cauchy–Schwarz the number of $n\le N$ with $qh\mid n$ is at most $N/(qh)$. The elementary $\sum_{q\le N}q^{-1}\ll L$ here does not require a prime estimate. Chebyshev's elementary $\sum_{p\le z}\log p\le10z$ for large $z$ and $\tau(\operatorname{rad}N)=N^{o(1)}$ give

$$
 K\le\tau(M)\le \tau(\operatorname{rad}N)\,W
             \le N^{\kappa/100+o(1)}.
$$

In particular both (4) and (5) are $O_{\rho,\kappa}(N^{1-\kappa/4})$ at fixed $\kappa$; even the loss $K^2\tau(M)^2L$ only costs $N^{.04\kappa+o(1)}$ in (5).

## On every complementary approximant the short sum has no zero frequency

For any $\alpha\in\mathfrak m$, Dirichlet approximation gives a reduced $a/r$ with $R<r\le Q_*$ and a lift $\alpha=a/r+\beta$ with $|\beta|\le1/(rQ_*)$. No decomposition into nonoverlapping arcs is needed. Fix any $q\in\mathcal Q$, $h\mid M$, $h\le H$; put $P=N/q$ and $d=r/(r,q)$. Uniformly in these choices,

$$
 d\ge r/q\gg N^\kappa L^{-200}>H,\qquad
 N|\beta|\ll L^{200},\qquad
 P/(hd)\ge N^{2\kappa/3}.                                \tag{6}
$$

In the $h$ term the oscillation at the rational center on $p=hm$ is $e(a q h m/r)$. Since $a$ is reduced and the reduced denominator of $q/r$ is exactly $d$, its frequency has distance at least $1/d$ from $\mathbb Z$: it cannot be an integer because $d\nmid h$.

Write

$$
 v_{q,\beta}(u)=\frac{w_I(u)}{\log(Pu)}e(\beta Nu)
$$

on its compact support. The endpoint derivative bound and (6), with Fourier convention $\widehat v(s)=\int v(u)e(-su)\,du$, give for each fixed $j\ge2$

$$
 |\widehat v_{q,\beta}(s)|
 \ll_{\rho,j} L^{-1} N^{j\kappa/3}(1+|s|)^{-j}.          \tag{7}
$$

Direct Poisson summation on $p=hm$ is

$$
 \sum_{m\in\mathbb Z} v_{q,\beta}(hm/P)e(a q h m/r)
   =\frac{P}{h}\sum_{k\in\mathbb Z}
       \widehat v_{q,\beta}\!\left(\frac P h (k-a q h/r)\right).
$$

Because $\sum_{k\in\mathbb Z}|k-a q h/r|^{-j}\ll_j d^j$ by the distance bound and summability away from the nearest integer, (6)–(7) bound this by

$$
 \ll_{\rho,j} \frac{P}{hL}\,N^{-j\kappa/3}.             \tag{8}
$$

The strictly positive central support means the formal sum over all $m\in\mathbb Z$ contributes exactly the original positive $p$. Summing (8) with the original factors $K\log q\,\mu(h)$ incurs only a polynomial loss in $N$; choose fixed $j$ sufficiently large in terms of $\kappa$ to make $B_{w,\le H}(\alpha)=O_{\rho,\kappa}(N^{-100})$ on the entire exact $\mathfrak m$. This calculation uses any admissible approximant at a given $\alpha$ and does not multiply-count overlapping high-denominator arcs.

Now (4), (5), and the pointwise bound give (1). The genuine prime transform has $\|A_I\|_{L^2(\mathbb T)}^2\ll_\kappa NL^2$ by counting eligible divisors of each Fourier index and Parseval. Combining this with (1) by Cauchy–Schwarz bounds each mixed term by $O_{\rho,\kappa}(N^{1-\kappa/8}L)$ and the synthetic product by $O_{\rho,\kappa}(N^{1-\kappa/4})$, proving (2). Add the signed R35 estimate to obtain (3). All errors are uniform in $I$; the second factor remains fixed for the original bounded-variation cumulative transfer.

Under global Dirichlet GRH and for macroscopic $I$, the [unsigned energy lower bound](r36-source-minor-energy-after-dirichlet.md) transfers to the genuine prime transform on the same complement, since (1) makes $\|F_I-A_I\|_{L^2(\mathfrak m)}$ negligible compared with $(|I|L)^{1/2}$. This replacement neither contradicts that energy obstruction nor estimates the remaining genuine signed product. No assertion is made for a union with the separate R34 arcs.
