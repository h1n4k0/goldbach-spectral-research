# A macroscopic negative subspace for the signed integer aliases

**Scope.** A strengthened obstruction on the genuine retained coarse means of the long-divisor Gram. It concerns its distinct-*integer* term, not distinct zero copies or the original $T_N$. The integer-equality term is provably large on these same tests, so this does not determine the sign of the sum minus the original benchmark.

Use the notation and fixed parameters of the [exterior integer-diagonal estimate](r39-operator-long-divisor-diagonal-inflation.md): $L=\log N$, $\ell=\log L$, $\alpha=L^{-1}$, $\beta=1/8$, and $r_N(u)=u^{-3/2}((Nu)^{-2\alpha}+(Nu)^{-2\beta})^{1/2}$ on physical $L^2(du)$. Fix $K>0$, $0<\eta<1$, $\mathsf A>2K+5$, $\mathsf B>K+4$, $C_0>K+3$, and take

$$
 (K+3)\ell^2/\log\ell\le H\le L^{1-\eta},\qquad
 Y=e^H,\qquad q_0=N\exp(-C_0\ell^2/\log\ell).
$$

On each physical dyad $I_V=[V,2V)$, $V=2^jY$, use the common cutoff $D_V=\lfloor\min\{VL^{-\mathsf A},\sqrt{q_0}L^{-\mathsf B}\}\rfloor$. Write $\Lambda_{>D_V}(n)=\Lambda(n)-\sum_{d\mid n,d\le D_V}\mu(d)\log(n/d)$. The long-divisor atoms use this coefficient in place of $\Lambda(n)$ in the actual physical Hardy realization.

Under the original local Dirichlet GRH at $N$, there are constants $C>1,\ c>0$ and, for every such $N,H$, a subspace $\mathcal Z$ of the [actual exterior coarse mean profiles](weak-s-exterior-fine.md), with $\dim\mathcal Z\ge cH$, such that

$$
 \langle O_{\rm int}^{>}g,g\rangle\le -c\,\frac{L^2}{H}\,\|g\|_2^2
 \qquad (g\in\mathcal Z).
 \tag{1}
$$

Here the Gram is restricted to the union $W$ of the whole physical dyads contained in $[Y,e^{CH}]$, and $O_{\rm int}^{>}$ is its exact distinct-integer term. The result holds for the **full odd family**, for which the coefficient on units is exactly ${\bf1}_{n\equiv m\ (N)}-{\bf1}_{n\equiv-m\ (N)}$, and separately for the family $q_\chi\ge q_0$ with the total odd-family denominator. The subspace may differ between these two choices. It is supported within a single log strip of length at most $CH=o(L)$; hence (1) holds unchanged for the [log-separation mask](r31-operator-zero-diagonal.md). Every vector in $\mathcal Z$ is assembled from differences of local weighted means, each annihilating the constant Volterra prefix on its own dyad.

## 1. Mean differences and exact integer orthogonality

For each dyad $I_V\subset W$, let $I^-_V$ be the union of whole R30 cells lying within $[V,5V/4)$, and $I^+_V$ the analogous union within $[7V/4,2V)$. The R30 cell lengths are $o(V)$ uniformly on this strip: for any of its fixed parameters the cell-length ratio is at most $O(V^{-1/2+\vartheta/L})$, and $V\ge e^H\to\infty$. Each union therefore has length $\asymp V$. Put

$$
 C_\pm=\|r_N{\bf1}_{I^\pm_V}\|_2,\qquad
 \phi_\pm=r_N{\bf1}_{I^\pm_V}/C_\pm,\qquad
 e_V=\frac{C_-\phi_+ - C_+\phi_-}{(C_-^2+C_+^2)^{1/2}}.
$$

Then $\|e_V\|_2=1$, $e_V$ belongs to the exact coarse mean space, and $\int_{I_V} r_N(u)e_V(u)\,du=0$. Since $CH=o(L)$ for any fixed $C$, $C_\pm\asymp V^{-1}$ uniformly for large $N$. For $n\le NV$ the test annihilates the constant prefix: $\int r_N e_V{\bf1}_{n\le Nu}=0$. For $n\ge2NV$ the same integral vanishes by support. On the entire raw interval $4NV/3<n\le 5NV/3$, the indicator has value one on $I^+_V$ and zero on $I^-_V$, so this integral is $C_-C_+/(C_-^2+C_+^2)^{1/2}\asymp V^{-1}$.

For the actual restricted atom write ${\bf1}_W t_\chi=\sum_{(n,N)=1}\chi(n)a_n$, where on $I_V\subset W$

$$
 a_n(u)=-\frac{\sqrt{2\pi n}}{N}r_N(u){\bf1}_{n\le Nu}\Lambda_{>D_V}(n).
$$

All sums are finite on $W$. Its integer-equality diagonal is $D_{\rm int}^{>}=\rho\sum_n a_n\otimes a_n$, with $\rho=1$ for the full odd family and $\rho=1-o(1)$ for the high-conductor family by the [conductor-defect count](r33-operator-conductor-defect.md). The coefficient $\Lambda_{>D_V}(n)$ is constant in $u$ on a dyad. Thus $\langle a_n,e_V\rangle$ vanishes unless $NV<n<2NV$. These raw intervals for different dyads are disjoint, so $\langle D_{\rm int}^{>}e_V,e_{V'}\rangle=0$ exactly when $V\ne V'$.

Moreover,

$$
 \langle D_{\rm int}^{>}e_V,e_V\rangle\ge c_0\,\frac{L^2}{\log V}.
 \tag{2}
$$

In fact the R39 Bonferroni lower sieve applies unchanged on $(4NV/3,5NV/3]$: the interval still has length a fixed positive fraction of $NV$, and each divisor congruence count has an $O(1)$ floor error. With $D_V=\lfloor VL^{-\mathsf A}\rfloor$ on this strip and $k\asymp\ell$ as in R39, $D_V^k=\exp(o(L))$ uniformly. The removal of nonunits, primes and proper powers has the same negligible bound as in R39. Therefore $\gg NV/\log V$ integers in the new interval are units, have all prime factors $>D_V$ and are not prime powers. Each satisfies $\Lambda_{>D_V}(n)=-\log n$, and its squared coefficient on $e_V$ is $\gg L^2/(NV)$ by the preceding test computation. This proves (2) unconditionally. No cross-congruence estimate is used for it.

## 2. A trace budget yields many negative directions

Write $P^{>}$ for the true long-divisor Gram, so $O_{\rm int}^{>}=P^{>}-D_{\rm int}^{>}$. For either character family, the R39 trace argument gives $\operatorname{tr}P^{>}\le C_1 L^2$ for any fixed $C$, with an absolute $C_1$ for all sufficiently large $N$. Explicitly, for the high family the [deleted-atom energy](r38-operator-exterior-linear-type-i.md) is $o(1)$, while for the full family the same holds on any such finite $W$ by the R39 auxiliary conductor $q_c=e^{3CH}$ argument. It uses R38 above $q_c$, the $N^{-1+o(1)}$ fraction below $q_c$, and the [per-character dyad bound](r34-operator-exterior-type-i.md) of $N^{o(1)}$ squared energy on $W$. Thus the positive Gram trace is bounded by twice the original full-family atom trace plus $o(1)$. Local GRH is used only for the genuine embedding and the original trace bound; no global Dirichlet GRH is used.

Choose $C=2^M$ with $M$ a sufficiently large fixed integer. For each $s=0,\ldots,M-1$, form $\mathcal H_s$ by spanning those $e_V$ for which the whole $\log I_V$ is contained in $[U_s,2U_s]$, $U_s=2^sH$. Different spaces are orthogonal, and their dimensions $r_s$ satisfy $r_s\ge c_1 U_s$ for some absolute $c_1>0$, since the dyadic logarithmic step is $\log2$ and at most two cells are lost at each band boundary. Let $P_s,D_s$ be the orthogonal compressions of $P^{>},D_{\rm int}^{>}$. By (2) and its exact cross-dyad vanishing,

$$
 D_s\ge d_s I_{\mathcal H_s},\qquad d_s=\frac{c_0 L^2}{2U_s}.
$$

The PSD trace budget implies $\sum_s \operatorname{tr}P_s\le C_1L^2$. Some $s$ has $\operatorname{tr}P_s\le C_1L^2/M$. The number of eigenvalues of $P_s$ larger than $d_s/2$ is at most $4 C_1 U_s/(M c_0)$. Choose $M$ so this is at most $r_s/2$. On the subspace $\mathcal Z\subset\mathcal H_s$ belonging to eigenvalues of $P_s$ at most $d_s/2$, the quadratic form of $P_s-D_s$ is at most $-d_s/2$ times the identity. Its dimension is at least $r_s/2\gg H$, and $d_s/2\gg L^2/H$ with a constant depending only on the fixed $C$. This proves (1).

All supports entering this single compression satisfy $|x-z|\le U_s\le CH=o(L)$ in log coordinates. The exact R31 mask is one throughout this support for large $N$, not just on each dyad separately. Thus the nonpositive comparison does not rely on dropping a mask, on translating the midpoint, or on using a null vector of the unregularized covariance.

The semidefinite conclusion is only about the distinct integers of the signed convolution Gram. The large positive artificial $n=m$ term remains present and can compensate this negative subspace. Neither the sign nor the size of $P^{>}$ minus the original $D_N+K_N$ on $\mathcal Z$ follows, and there is no assertion of weak S or of negative distinct-zero-copy covariance.
