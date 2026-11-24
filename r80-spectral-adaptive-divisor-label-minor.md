# Actual moving minors with independently moving divisor labels and target gcd tests

**Scope.** This is an unconditional almost-all bound for actual above-BV squarefree mixed minors. Unlike the [original moving-cut estimate](r79-spectral-original-minor-power-exception.md), it allows arbitrary target-dependent intervals in the true divisor and prime labels and arbitrary bounded functions of their gcds with the target. It does not allow arbitrary unrelated right coefficients on each target. No major estimate, fixed-target bound, or implication for weak S is claimed.

Fix real constants $0<\delta\le\kappa<1/3$ and an ambient scale $Y$. Write $e(t)=e^{2\pi i t}$ and $\lambda(n)=(\log n)\mathbf1_{n\text{ prime}}$. For each even $N\in[Y,2Y]$ choose two parameters $Q_N,B_N\in[Y^\delta/2,3Y^\kappa]$ with no regularity requirement. Let $\mathfrak m_N$ be the complement on the torus of the disjoint arcs

$$
 (a,q)=1,\qquad q\le Q_N,\qquad |\theta-a/q|\le B_N/N .
$$

The original $Q_N=N^{1/1000}$ and $B_N=2Q_N$ are included by taking $\delta=\kappa=1/1000$.

For each squarefree $m\in[Y/4,5Y]$, take all ordered positive decompositions $abcd=m$ with $\min(ab,ac)<\sqrt m$. The factors are automatically pairwise coprime. Give a tuple the same weight as in the [genuine mixed strip](r66-spectral-above-bv-strip-deletions.md):

$$
 w(a,b,c,d)=\mu(b)\mu(c)\left(1-\frac{2\log(ac)}{\log m}\right).
$$

Let $\rho_m$ be a fixed common multiplier with $|\rho_m|\le1$. At each $N$ permit independently chosen, arbitrary hard intervals in $m$ and the five true labels

$$
 {\bf t}=(ab,\ ac,\ abc,\ P^+(m),\ m/P^+(m)).
$$

An empty interval may be chosen. In addition multiply each selected tuple by any function $F_N((t_1,N),\ldots,(t_5,N))$ with $|F_N|\le1$; the function and the intervals may all vary with $N$. Let $A_N(m)$ be the sum of these weighted selected tuples times $\rho_m$, zero elsewhere. This includes the original hard gates $ab,ac>D_N$, $abc>H_N$ and $m\in V_N$, either total parity through $\rho_m$, any actual largest-prime and cofactor bands, and targets with actual right unit tests. Here and below gcd notation applies separately to each coordinate.

Write $\widehat A(\theta)=\sum_m A(m)e(m\theta)$, and $P_{I,\omega}(\theta)=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$. Uniformly for every $\epsilon>0$,

$$
 \sum_{\substack{Y\le N\le2Y\\2\mid N}}
 \sup\left|\int_{\mathfrak m_N}P_{I,\omega}(\theta)
             \widehat A_N(\theta)e(-N\theta)\,d\theta\right|^2
 \ll_{\delta,\kappa,\epsilon}Y^{3-\delta/2+\epsilon}.
 \tag{1}
$$

The supremum is over all the choices at $N$ just described, including $Q_N,B_N$, every hard left interval $I\subset(N/2,9N/16]$, and weights with fixed bounded supremum plus variation. It is for the fixed common $\rho$, and the bound is independent of that common multiplier. In particular the bound $Y^{1-\sigma}$ holds outside $O_\epsilon(Y^{1-\delta/2+2\sigma+\epsilon})$ even targets for any fixed $0<\sigma<\delta/4$ and sufficiently small $\epsilon$.

## 1. Arithmetic axes rather than threshold freezing

First fix a common vector of positive integers {\bf h}=(h_1,\ldots,h_5)$, and impose only the fixed divisibility tests $h_i\mid t_i$ on the underlying tuples. Partition $m$ and the five labels into dyadic integer cells, using a fixed ambient power-of-two integer box containing $[1,5Y]$. At any fixed levels the cells $C$ form a disjoint partition in the six coordinates. Denote the resulting right coefficients by $A_{{\bf h},C}$. They are computed with $\rho_m$ and the original tuple weight, including the same fixed strict upper gate $\min(ab,ac)<\sqrt m$.

At each $m$ put $n_{{\bf h},C}(m)$ for the positive number of underlying tuples in this cell satisfying the divisibility tests. Then $|A_{{\bf h},C}(m)|\le n_{{\bf h},C}(m)$. Their total over cells for fixed {\bf h}$ is at most $\tau_4(m)$, since every tuple is assigned once. In particular

$$
 \sum_{{\bf h},C}\|\widehat A_{{\bf h},C}\|_2^2
 \le \sum_{\substack{m\le5Y\\m\ {\rm squarefree}}}
                \tau(m)^5\tau_4(m)^2
 \ll Y(1+\log Y)^{511}.
 \tag{2}
$$

Indeed every label divides $m$, so only $\tau(m)^5$ choices of {\bf h}$ can occur at this $m$. The last summand is $\tau_{512}(m)$ on squarefree integers. Its unrestricted sum has the displayed bound by counting ordered tuples and summing the reciprocals of the first 511 positive factors. Thus no cancellation of two tuples or smoothness of any numeric threshold is used in the summed squared norm.

For the true gcd weights use the finite divisor-lattice identity

$$
 F_N({\bf g})=\sum_{{\bf h}\mid{\bf g}} c_N({\bf h}),\qquad
 c_N({\bf h})=\sum_{{\bf v}\mid{\bf h}}
   F_N({\bf v})\prod_{i=1}^5\mu(h_i/v_i).
 \tag{3}
$$

The order on vectors is coordinatewise divisibility. With $g_i=(t_i,N)$ this is an exact sum over {\bf h}\mid(N,\ldots,N)$ of the fixed tests $h_i\mid t_i$. Each $|c_N({\bf h})|\le\tau(N)^5$ and there are at most $\tau(N)^5$ such vectors. By Cauchy, for any values $Z_{\bf h}$,

$$
 \left|\sum_{{\bf h}\mid(N,\ldots,N)}c_N({\bf h})Z_{\bf h}\right|^2
   \le \tau(N)^{15}
            \sum_{{\bf h}\mid(N,\ldots,N)}|Z_{\bf h}|^2.
 \tag{4}
$$

The elementary divisor bound makes the prefactor $O_\epsilon(Y^\epsilon)$ for arbitrarily small $\epsilon$. In a nonnegative sum over $N$ the condition {\bf h}\mid(N,\ldots,N)$ on the right may be dropped; the additional sum over all fixed {\bf h}$ is already budgeted by (2).

## 2. A fixed enclosing minor and genuine moving rectangles

Use the fixed common minor $\mathcal U$ obtained by removing denominators $q\le Y^\delta/4$ up to distance $Y^{-1+\delta}/8$ from all reduced centers. Every actual major set contains the removed common arcs. On $\mathcal U$, Dirichlet approximation with bound $\lceil 16Y^{1-\delta}\rceil$ gives a reduced $a/q$ with $Y^\delta/4<q\ll Y^{1-\delta}$ and $|\theta-a/q|\le q^{-2}$: a smaller denominator would put $\theta$ in a removed common arc. The [Vaughan bound, Montgomery–Vaughan Theorem 17.1](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf#page=79) then gives

$$
 \sup_{\theta\in\mathcal U}\sup_{J\subset[1,5Y]}
       |P_J(\theta)| \ll_\delta Y^{1-\delta/2}(1+\log Y)^4
 \tag{5}
$$

for unweighted hard integer intervals $J$. The middle term $Y^{4/5}$ is smaller since $\delta<1/3$; prime powers and interval differences cost no change of exponent. Short prefixes with $q>x$ use the trivial bound since $\sqrt{xq}\ge x$.

Take the fixed ambient arc family of denominators $q\le 3Y^\kappa$ and slow coordinate $|\beta|\le 3Y^{-1+\kappa}$. It is pairwise disjoint on the torus, since centers are separated by $\gg Y^{-2\kappa}$. On the whole torus the true minor is exactly $\mathcal U$ minus its intersection with the single moving rectangle $q\le Q_N$, $|\beta|\le B_N/N$ in this family. Every $q,\beta$ cell retains all reduced numerators. Leave the discrete $q$ cutoff exact; round each actual $\beta$ interval inward to a union of cells in a fixed power-of-two grid of mesh at most $Y^{-4}$ and polynomial size. Only two cells at each center may differ. The omitted measure is $O(Y^{2\kappa-4})$. Before any divisor-lattice expansion, the true right sup norm is $O(Y(1+\log Y)^3)$ by positive domination with $\tau_4$, and the left sup norm is $O(Y)$ by Chebyshev. Thus the integral rounding error, uniformly even with all true gcd weights, is $O(Y^{-2+2\kappa}(1+\log Y)^3)$. This contributes negligibly to (1).

## 3. Maximal Bessel with the divisibility budget

For a fixed {\bf h}$ the rounded minor integral is the difference of the integrals on $\mathcal U$ and on the rectangle just described intersected with $\mathcal U$. There are nine dyadic axes for the latter: the left integer coordinate, the six right coordinates, $q$, and the slow grid. The integral on $\mathcal U$ alone uses the same argument without the last two axes. A hard rectangle on these axes decomposes into $O((1+\log Y)^9)$ dyadic boxes. Their positions may depend on $N$. For one canonical tuple of cells $(J,C,R)$ the Fourier coefficient at $N$ is taken of the fixed torus function

$$
 \mathbf1_{\mathcal U\cap R}P_J\,\widehat A_{{\bf h},C}.
$$

Cauchy across the decomposition controls the squared supremum by a fixed log power times the sum of squared coefficients over all canonical choices. Sum nonnegatively over integer Fourier indices and use Parseval for these fixed functions. At any set of levels the arc cells are mutually disjoint by the original geometry. Also the left integer intervals are disjoint, so on $\mathcal U$

$$
 \sum_J|P_J|^2\le(\sup_J |P_J|)\sum_J|P_J|
            \ll_\delta Y^{2-\delta/2}(1+\log Y)^4.
$$

Consequently the total torus energy summed over the cells and over all {\bf h}$ is at most this bound times (2). There are only fixed powers of $\log Y$ possible level choices. At each $N$ variation of the left weight is handled by partial summation over its actual interval, uniformly by the supremum over its hard prefixes times the fixed variation-plus-supremum bound. Apply (4) for the true gcd weight before taking the supremum, and enlarge the positive sum over {\bf h}$ as above. Thus the summed maximal squared integral is $Y^{3-\delta/2}$ times a fixed log power and the removable divisor factor $Y^{o(1)}$. The negligible unrounded error completes (1).

In particular the numerical thresholds never had to be frozen. The result controls the actual strict or weak endpoints of all integer labels and the genuine moving original minor, but gives no uniform signed major or full-value estimate. The fixed common multiplier on $m$ is essential to the argument: the gcd masks can be represented through (3), not through arbitrary target-dependent modulation.
