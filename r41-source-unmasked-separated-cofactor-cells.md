# Signed unmasked macroscopic-gap cofactor cells on the exact Dirichlet complement

Work in the exact setting of the [full Dirichlet arcs](r35-source-square-root-dirichlet-arcs.md) and the [four-distinct-prime reduction](r38-source-four-distinct-prime-minor-reduction.md). Fix $0<\rho<1/2$ and $0<\kappa\le1/2000$, and let $N$ be sufficiently large and even. Write $L=\log N$, $S=\mathfrak S(N)$, $I_0=[\rho N,(1-\rho)N]$. The first window is any moving hard interval $I\subseteq I_0$ with either endpoint convention, and the second stays $I_0$. The eligible small primes are

$$
 \mathcal Q=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\}.
$$

Both large primes are genuine primes coprime to $N$; the weighted summands have the original marker $(\log q)(\log s)$. Put $e(x)=e^{2\pi i x}$, $Q_*=\lfloor\sqrt N\rfloor$, $R=\lfloor Q_*L^{-200}\rfloor$. Let $\mathfrak D$ be the exact disjoint union of complete reduced arcs with $1\le r\le R$ and widths $1/(rQ_*)$, and $\mathfrak m=\mathbb T\setminus\mathfrak D$.

Let $j(q)=\lfloor\log_2 q\rfloor$. Orient the two small primes by $q>s$ for the cell selection only. Choose a set $\mathcal C$ of $K$ distinct pairs of dyadic indices $(j(q),j(s))$ such that, for a fixed $\delta>0$, every occupied cell has $q/s\ge N^\delta$ throughout. Retain both original orders of the physical products $qp,sv$ whenever allowed by the original windows. Let $\mathcal P_{I,\mathcal C}$ be the exact weighted product expansion on those cells, with **no restrictions on the giant primes beyond genuine primality, the original unit masks and the original windows**. For sufficiently large $N$ this is entirely four-distinct: $q\ne s$ by separation, the small and large prime ranges are disjoint, and $p/v=(qp)/(sv)\cdot(s/q)\ll_\rho N^{-\delta}<1$.

**Theorem.** Under global Dirichlet GRH the signed integral is

$$
 \left|\int_{\mathfrak m}\mathcal P_{I,\mathcal C}(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll_{\rho,\kappa} S N K/L^2.                                   \tag{1}
$$

The constants are uniform in the original hard interval and the choice of cells; the sufficiently large $N$ threshold also depends on $\delta$. In particular, a strip of $O(L^{1/2})$ dyadic differences at a fixed positive proportional separation has $K=O(L^{3/2})$ and contributes $O_{\rho,\kappa}(SN/\sqrt L)$. The bounds do not estimate the whole four-prime term. A concrete full strip of this kind lies wholly outside the [small giant-gap mask](r39-source-four-prime-small-giant-gap.md) and the [rational-slope mask](r40-source-four-prime-rational-giant-slopes.md); see below.

## 1. Full-torus target coefficient: unconditional uniform two-form sieve

Fix $q>s$ as above. The equation $qp+sv=N$ has the integral parametrization $p=p_0+s k$, $v=v_0-qk$ for any integral solution $(p_0,v_0)$, and the physical cuts confine $k$ to an interval of length $O(N/(qs))$. Indeed $qp$ varies by $qs$ per step; bounding the entire central interval is sufficient for any endpoint convention. Write $X=N/(qs)\ge N^{2\kappa}$.

For each prime $\ell$, let $\nu(\ell)$ count the roots of the product of the two linear forms in $k$ modulo $\ell$. For $\ell\mid q s$ exactly one form is a nonzero constant by $(q s,N)=1$, so there is one root. For $\ell\nmid q s$ both linear coefficients are units and the two roots coincide exactly when $\ell\mid N$, since the determinant is $qp_0+sv_0=N$. In particular $\nu(2)=1$ because $2\mid N$ and $q,s$ are odd. No $\nu(\ell)$ equals $\ell$.

For completeness, choose $Z=N^{\kappa/10}$ and $z=Z^\eta$ with a sufficiently small absolute $\eta>0$. All occurring $p,v$ exceed $z$. Let $\mathcal D_z$ be the squarefree divisors of $\prod_{\ell\le z}\ell$ up to $Z$, a divisor-closed set. Set $g(d)=\prod_{\ell\mid d}\nu(\ell)/\ell$, $h(d)=\prod_{\ell\mid d}g(\ell)/(1-g(\ell))$, and $G=\sum_{d\in\mathcal D_z}h(d)$. In the standard quadratic upper-bound sieve, use $\lambda_1=1$, weights $\lambda_d$ supported on $\mathcal D_z$, and majorize the unsieved count by the sum of $\big(\sum_{d\mid(p_0+sk)(v_0-qk)}\lambda_d\big)^2$. The residue count for each least common multiple is its expected $g([d,e])$ times interval length, with absolute error at most $\nu([d,e])$. To see the relevant weights explicitly, write $y_l=\sum_{l\mid d,\ d\in\mathcal D_z}\lambda_d g(d)$; the main quadratic form equals $\sum_{l\in\mathcal D_z}y_l^2/h(l)$, since $1/g((d,e))=\sum_{l\mid(d,e)}1/h(l)$. Choose $y_l=\mu(l)h(l)/G$. Divisor inversion gives $\lambda_1=1$, main quadratic form $1/G$, and

$$
 |\lambda_d|\le h(d)/g(d)=\prod_{\ell\mid d}(1-g(\ell))^{-1}\le d.
$$

The last inequality uses $\nu(\ell)\le\ell-1$. With $\nu([d,e])\le[d,e]\le Z^2$ the full lattice error is $O(Z^6)$.

In the Euler product of all $h(d)$ over $d\mid\prod_{\ell\le z}\ell$, the probability weight of including $\ell$ is $g(\ell)$. Its mean of $\log d$ is $\sum_{\ell\le z}g(\ell)\log\ell\ll\log z$ by elementary Chebyshev, uniformly in the forms. Choosing $\eta$ small, Markov's inequality leaves at least half this weight at $d\le Z$. Thus

$$
 G^{-1}\ll\prod_{\ell\le z}\left(1-\frac{\nu(\ell)}{\ell}\right)
          \ll_\kappa \frac{S}{L^2}.
$$

For the last inequality factor out $\prod_{\ell\le z}(1-1/\ell)^2$, which is $O(1/\log^2 z)$ by Mertens. The remaining factor at $\ell=2$ is $2$; at $\nu(\ell)=2$ it is at most one; each odd prime dividing $N$ contributes at most $(\ell-1)/(\ell-2)$, and the at most two extra primes dividing $qs$ contribute a bounded factor. These are bounded by a constant multiple of the usual even Goldbach singular series $S$.

Since $Z^6=N^{3\kappa/5}=o(X/L^2)$, the actual two-prime count is $O_\kappa(SN/(qsL^2))$ in the hard central window, and equally for the reflected original order. Weighting by $\log q\log s$ and summing one chosen dyad on each side gives $O_\kappa(SN/L^2)$, since $\sum_{U\le q<2U}(\log q)/q\ll1$ by Chebyshev. This is the signed full-torus coefficient bound at the actual target $N$, independent of GRH.

## 2. Exact major coefficient and subtraction

For an eligible dyad $E$, denote the actual prime transform in a hard interval $J$ by $A_{J,E}$. On a reduced arc $a/r+\beta$ its uncentered real model is the integral over $J$ of $e(\beta t)$ times

$$
 G_E(t;r)=\sum_{q\in E}g_q(t)\frac{\mu(r_q)}{\varphi(r_q)},
 \qquad
 g_q(t)=\frac{\log q}{q\log(t/q)},\quad r_q=\frac{r}{(r,q)}.
$$

Only the **prime leg of R35, §2** is used. Its squared approximation error on $\mathfrak D$ is $O_{\rho,\kappa}(NL^{-32})$ also for one arbitrary cofactor dyad $E$: the unit cofactor character energy estimate uses $\sum_{q\in E}|\log q|^2$ and the same interval length $U$, the shared $q\mid r$ bound uses at most the original number of choices, and the smoothed hard-edge error uses the same bound on the number of eligible divisors of an integer. The missing primes dividing $N$ are already part of that uniform GRH error. The real hard-edge model estimate is unchanged since $|G_E(t;r)|\ll_\rho1/\varphi(r)$ by the same $\sum_{q\mid r}\log q\le\log r$ argument. No model or estimate for a synthetic leg is used here. By Parseval and the bounded number of eligible $q\mid n$, $\|A_{J,E}\|_2^2\ll_\kappa NL^2$, so replacing the actual two prime factors in their signed major integral costs $O_{\rho,\kappa}(NL^{-15})$.

The real model is independent of the reduced numerator. Thus the target phase sums to $c_r(N)$ before taking absolute values. On expansion in a fixed pair $q\ne s$, any nonsquarefree $r$ is killed: a prime square other than $q^2,s^2$ leaves a zero Möbius factor, while $q^2$ or $s^2$ in $r$ kills $c_r(N)$ because those primes are units modulo $N$. For squarefree $r$ the denominator-factor sum is bounded by

$$
 \sum_r
 \frac{|c_r(N)|\,\mu(r_q)^2\mu(r_s)^2}{\varphi(r_q)\varphi(r_s)}
 \ll S.
$$

Indeed at the special prime $q$ the nontrivial local factor is $1/(q-1)$ (exactly one denominator loses $q$ and $|c_q(N)|=1$), likewise for $s$. Other local factors are the usual absolute Euler factors $|c_\ell(N)|/\varphi(\ell)^2$ of R32, with product after adjoining the trivial factors $O(S)$. Equivalently that product has $(1+1/(\ell-1))$ at primes dividing $N$, a uniformly convergent product at other odd primes, and a fixed factor at $2$.

Now $g_q(t)\ll_\rho(\log q)/(qL)$ on the original central range. Real Plancherel and Cauchy–Schwarz bound each integrated pair of real profiles in absolute value by $O_\rho(N(\log q)(\log s)/(qs L^2))$ times the indicated denominator weights. Summation over two dyads as in §1 gives $O_{\rho,\kappa}(SN/L^2)$ for the signed major contribution including the approximation error. Subtracting from the actual full-torus coefficient proves (1) for each cell, both original orders, and summing $K$ proves the result. Dyadic masks are fixed with respect to the moving first window, so its usual bounded-variation physical transfer is preserved.

## 3. A whole strip with unrestricted giant gaps, disjoint from the older geometric masks

For instance, select every occupied ordered cell with

$$
 .38\log_2 N\le j(q)\le .42\log_2 N,\qquad
 \big|j(q)-j(s)-.30\log_2 N\big|\le\sqrt L .
$$

There are $K=O(L^{3/2})$ cells; throughout them $q/s\ge N^{.29}$ and $q^2/s\gg N^{.66}$ for sufficiently large $N$. Thus $s|p-v|=sv-sp\ge \rho N-O(N^{1-.29})$, wholly outside R39's $\sqrt N$ threshold.

This entire strip is also outside the geometric R40 mask at $H=\sqrt N$. A reduced positive slope $a/b$ in that mask would require $b\le\sqrt N/q$ from the nonzero integer $bp-av$, and

$$
 \frac1b\le\frac ab
 \le\frac p v+\frac{\sqrt N}{qb^2v}
 \le\frac p v\left(1+\frac1{\rho\sqrt N}\right)
 \ll_\rho s/q.
$$

This forces $b\gg_\rho q/s$, incompatible with $q^2/s\gg N^{.66}$. No assumption about which giant primes occur is needed for either exclusion. Genuine actual target tuples occur for arbitrarily large $N$ in this strip: use the ordinary PNT to choose $q,s,p,v$ in fixed sufficiently narrow proportional windows around $X^{2/5},X^{1/10},X^{3/5},X^{9/10}$, and set $N=qp+sv\asymp X$. The summands are central for the chosen windows, all four primes are distinct odd units modulo even $N$, and the dyadic-index separation is $.30\log_2 N+O(1)$. This witness is not a signed lower bound. General macroscopic-gap cells away from any logarithmically thin collection, including $K\asymp L^2$, are not resolved by (1).
