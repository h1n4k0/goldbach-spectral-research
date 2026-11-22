# The dense separated cells have a positive signed major main term

Use the exact genuine four-distinct-prime setting of the [four-distinct-prime reduction](r38-source-four-distinct-prime-minor-reduction.md) and the [separated cofactor cells](r41-source-unmasked-separated-cofactor-cells.md). Fix $0<\rho<1/2$, $0<\kappa\le1/2000$, and $L=\log N$ for sufficiently large even $N$. Let $S=\mathfrak S(N)$, $I_0=[\rho N,(1-\rho)N]$, and let $I\subseteq I_0$ be an arbitrary moving hard interval with either endpoint convention. Both small primes are eligible modulo $N$, in $[N^\kappa,N^{1/2-\kappa}]$; both large primes are genuine and coprime to $N$. Orient by the small prime ordering $q>s$ for mask selection only. Select $K=O(L^2)$ distinct dyadic cells as in R41 with $q/s\ge N^\delta$ for a fixed $\delta>0$ uniformly over the occupied cells, and retain both original ordered products when allowed by $I,I_0$. Optionally allow fixed hard truncations of the cofactor ranges in either leg of each cell. Denote this exact collection of oriented cofactor pairs by $\mathcal U$ and its genuine weighted product by $\mathcal P_{I,\mathcal U}(\alpha)$ (marker $\log q\log s$). Its full-torus coefficient at the target $N$ is denoted by $C_I(N)$. The four primes are distinct throughout, by scale separation and the central windows.

Put $Q_*=\lfloor\sqrt N\rfloor$ and $R=\lfloor Q_*L^{-200}\rfloor$. The [exact Dirichlet major set](r35-source-square-root-dirichlet-arcs.md) $\mathfrak D$ consists of all complete reduced arcs with $r\le R$, each of width $1/(rQ_*)$, and $\mathfrak m=\mathbb T\setminus\mathfrak D$. Write $e(t)=e^{2\pi it}$. Define
$$
 g_q(t)=\frac{\log q}{q\log(t/q)},\qquad \lambda(q)=\frac{q-1}{q-2}.
$$

**Theorem (global Dirichlet GRH).** Uniformly over the same hard intervals and selected cells,
$$
 \int_{\mathfrak D}\mathcal P_{I,\mathcal U}(\alpha)e(-N\alpha)\,d\alpha
   =S\,\mathcal B_I(N)+O_{\rho,\kappa}(NL^{-13}),                    \tag{1}
$$
where the explicit nonnegative real quantity is
$$
 \mathcal B_I(N)=\int_I\sum_{(q,s)\in\mathcal U}\lambda(q)\lambda(s)
       \bigl[g_q(t)g_s(N-t)+g_s(t)g_q(N-t)\bigr]\,dt .
                                                                    \tag{2}
$$
Consequently the exact signed minor coefficient is $C_I(N)-S\mathcal B_I(N)+O_{\rho,\kappa}(NL^{-13})$. For the entire dense rectangle $N^{.38}\le q\le N^{.42}$ and $N^{.08}\le s\le N^{.12}$ one has, uniformly in $I$,
$$
 \mathcal B_I(N)=
 \left[2\log\frac{.62}{.58}\log\frac{.92}{.88}+o_{\rho,\kappa}(1)\right]|I|.  \tag{3}
$$
In particular the signed major coefficient is bounded below by a positive constant times $SN$ for each macroscopic $I$. Unconditionally, $C_{I_0}(N)\asymp_{\rho,\kappa} SN$ holds on a positive lower density of even $N$ in the sense that, for every sufficiently large $X$, it holds for $\gg_{\rho,\kappa}X$ such $N\in[X,2X]$. This is a scale obstruction to bounding the two terms separately by $o(SN)$, not a lower bound for their difference.

## 1. Exact numerator factors and extension of the real major integral

The genuine prime-leg approximation of R35 applies to an arbitrary subset of a single dyad and to the exact hard intervals used here, as in R41; restricting the cofactor coefficients changes neither the unit-class energy upper bound nor the exceptional $q\mid r$ multiplicity. For fixed $q$, put $r_q=r/(r,q)$ and
$$
 V_{J,q}(\beta)=\int_Jg_q(t)e(\beta t)\,dt,\qquad J\in\{I,I_0\}.
$$
The model at $a/r+\beta$ for a single cofactor set is the sum over that set of $V_{J,q}(\beta)\mu(r_q)/\varphi(r_q)$, independent of the reduced numerator. The squared error for a dyad on $\mathfrak D$ is $O_{\rho,\kappa}(NL^{-32})$; true squared energy is $O_\kappa(NL^2)$ by Parseval. Thus both orders of one cell have signed product replacement error $O_{\rho,\kappa}(NL^{-15})$, and summing $K=O(L^2)$ such errors costs $O_{\rho,\kappa}(NL^{-13})$. This uses only the genuine prime estimate, not a model for a synthetic leg.

Summing the target phase over the full reduced numerators gives $c_r(N)$. Let
$$
 H_{q,s}(r)=
 c_r(N)\frac{\mu(r_q)\mu(r_s)}{\varphi(r_q)\varphi(r_s)} .
$$
The coefficient is multiplicative in $r$ and supported on squarefree $r$: any other prime square gives a zero Möbius factor, while a square of $q$ or $s$ gives zero Ramanujan factor because $q,s$ are units modulo $N$. At a prime $\ell\notin\{q,s\}$ the factor is $c_\ell(N)/(\ell-1)^2$. At $\ell=q$, the $q$ leg has removed $\ell$, the $s$ leg gives $-1/(\ell-1)$, and $c_\ell(N)=-1$, so the factor is $+1/(\ell-1)$; similarly for $s$. Therefore
$$
 \sum_{r\ge1}H_{q,s}(r)=S\,\lambda(q)\lambda(s),\qquad
 \sum_{r\ge1}|H_{q,s}(r)|\ll S.                                  \tag{4}
$$
In the signed product, the usual unmodified factor at $\ell=q$ is $1-1/(q-1)^2$ and the new one is $1+1/(q-1)$; their ratio is precisely $\lambda(q)$. The absolute product is $O(S)$ since the local factors at primes dividing $N$ are $1+1/(\ell-1)$ and the other ordinary factors form a convergent product. The truncated denominator tail is
$$
 \sum_{r>R}|H_{q,s}(r)|\ll R^{-1/2}
                 \prod_\ell(1+\ell^{1/2}|H_{q,s}(\ell)|)
            = N^{-1/4+o(1)}.                                  \tag{5}
$$
The factors for primes not dividing $Nqs$ have bounded product. For primes dividing $Nqs$, the log of the product is $o(L)$ uniformly: for any fixed $\epsilon>0$ all sufficiently large such primes have $\log(1+\sqrt{\ell}/(\ell-1))\le\epsilon\log\ell$, and the exceptional bounded primes cost only a fixed factor. The remaining logs sum to at most $\log(Nqs)\le2L$. This proves (5) for every $q,s$ in the range.

Put $w_q=(\log q)/(qL)$. On the fixed central range $g_q(t)\ll_\rho w_q$ and $g'_q(t)\ll_\rho w_q/(NL)$ in absolute value. Hence direct integration by parts at the original interval edges gives
$$
 |V_{J,q}(\beta)|\ll_\rho w_q\min(N,|\beta|^{-1}).
$$
For $r\le R$, extending the $\beta$ integral from $|\beta|\le1/(rQ_*)$ to the whole real line thus costs $O_\rho(w_q w_s\,rQ_*)$ per $q,s,r$ profile product; $R Q_*/N\ll L^{-200}$. Sum using (4), and use (5) to restore $r>R$ at cost $O_\rho(N^{3/4+o(1)} w_q w_s)$ per pair. Summing all pairs costs the same bounds up to constants, since $\sum_{q\in\mathcal Q} w_q\ll1$ by Chebyshev; $S\ll L^2$ is more than enough to absorb the $L^{-200}$ tail into the error in (1). The whole real integral is exact Fourier inversion of two compact profiles:
$$
 \int_{\mathbb R}V_{I,q}(\beta)V_{I_0,s}(\beta)e(-N\beta)\,d\beta
   =\int_I g_q(t)g_s(N-t)\,dt ,
$$
since $N-t\in I_0$ whenever $t\in I$. The pointwise convolution identity is valid despite hard interval endpoints; the Fourier product is integrable by the preceding bounds. Adding the other original order proves (1) and (2).

In the displayed dense rectangle, uniformly over $t\in I_0$, one has $g_q(t)=\bigl(\log q/[q(L-\log q)]\bigr)(1+O_\rho(L^{-1}))$, and $\lambda(q)=1+O(N^{-\kappa})$. Ordinary prime Mertens by partial summation yields, for fixed $a,b$ inside the eligible range, $\sum_{N^a\le q\le N^b}(\log q)/(q(L-\log q))\to \int_a^b(1-u)^{-1}du$. The prime factors of $N$ excluded in that range are at most $1/\kappa$ and cost $o(1)$. This proves (3). The dense rectangle is strictly outside the [small giant-gap](r39-source-four-prime-small-giant-gap.md) and [rational-slope](r40-source-four-prime-rational-giant-slopes.md) masks: $q/s\ge N^{.26}$ forces $s|p-v|\asymp_\rho N$, and $q^2/s\ge N^{.64}$ conflicts with the necessary R40 conditions $b\le\sqrt N/q$ and $b\gg_\rho q/s$ for any positive slope. These hold throughout the indicated hard windows, without restricting the actual giant primes.

## 2. The true full coefficient can also be macroscopic

This part is unconditional. Use an auxiliary $X\to\infty$, choose $q$ in $[X^{.39},X^{.41}]$ and $s$ in $[X^{.09},X^{.11}]$, and impose both $qp,sv\in[2X/3,2(1+\epsilon)X/3]$ with a fixed $\epsilon>0$ small in terms of $\rho$. Then $N=qp+sv$ is even and lies in $[X,2X]$, both summands are central, and the narrower cofactor bands lie inside the stated dense rectangle for this $N$. The exponent ranges of $q,s,p,v$ are pairwise disjoint, hence all four primes are distinct and each is a unit modulo $N$ automatically. For each chosen $q$, the ordinary prime number theorem uniformly gives $\gg_\rho X/(q\log X)$ possible $p$, and similarly for $s$ and $v$. Summing with the markers $\log q,\log s$ and using the ordinary prime harmonic mass over the fixed polynomial bands shows that the two side masses are each $\gg_\rho X$. They may be selected independently before assigning their target, so
$$
 \sum_{\substack{N\in[X,2X]\\N\ {\rm even}}} C_{I_0}(N)\gg_\rho X^2 .
$$
The unconditional full-target sieve in R41, summed over $K=O(L^2)$ cells, gives $0\le C_{I_0}(N)\ll_{\rho,\kappa} S N$. The singular series has bounded second moment $\sum_{N\le2X,\,2\mid N}\mathfrak S(N)^2\ll X$: expand $\prod_{\ell\mid N,\ell>2}(1+O(1/\ell))$ over squarefree divisors and average with $\sum_{N\le 2X,\,d\mid N}1\le2X/d$; the product of the resulting $1+O(\ell^{-2})$ factors converges. Thus $\sum C_{I_0}(N)^2\ll_{\rho,\kappa}X^3$. A threshold $c_\rho X$ with small fixed $c_\rho>0$ and Cauchy–Schwarz show $C_{I_0}(N)\ge c_\rho X$ for $\gg_{\rho,\kappa}X$ even $N$ in the dyad. Discard the moduli with $S$ above a sufficiently large fixed bound; the same second moment leaves $\gg_{\rho,\kappa}X$ such moduli. On the surviving family $C_{I_0}(N)\asymp_{\rho,\kappa} SN$ as asserted.

Equations (1)–(3) quantify why a separate-bound argument on the exact dense residual does not suffice. A pointwise estimate for the signed minor integral there must use cancellation between the genuine weighted four-prime coefficient and the explicit positive major main term. No such pointwise cancellation, no bound for the full four-prime residual, and no lower bound for a signed remainder are claimed.
