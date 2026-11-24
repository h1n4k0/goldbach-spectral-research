# All aliases in selected critical-prime residue rows, with saddle masks

Keep the actual central prime polynomial $P$, full complementary polynomial $D$, and shell

$$
 \mathcal Q=\{q\ {\rm prime}:.8X\le q\le .9X\},\qquad
 \mathcal B=[-1/(10N),1/(10N)],
 \qquad X=\sqrt N,\quad L=\log N
$$

from [the boundary reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). In particular $N$ is even, the disjoint prime boxes are $[.740X,.745X]$ and $[.715X,.720X]$, and the first leg has any original independent hard cuts, true product gate and $N$-unit mask, and fixed arbitrary $-E(u,v)\log v$ with $|E|\le1$. The exact signed coefficients of $D$ have $d\in I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le dk<N/2$, $y\le9N/16$, both $N$-units and $(d,k)=1$, with weight $\mu(d)\mu^2(k)$. Write $e(z)=e^{2\pi iz}$.

Write $F_m=\rho_m D_m$, $F(\alpha)=\sum_m F_m e(m\alpha)$, for any true product mask $|\rho_m|\le1$ fixed independently of $q,\beta$. Optionally require the mask to be supported on the true count saddle of [the signed-count proof](weak-s-type-ii-critical-prime-signed-count-saddle.md). Precisely, take fixed $0<\delta<1$, $Z_1=\exp(L^\delta)$ and either $Z_0=2$ or $Z_0=\exp(L^\gamma)$ with fixed $0<\gamma<\delta$. Put $R=\log Z_1/\log Z_0$, and assume

$$
 \omega_{[Z_0,Z_1)}(m)\ge 2\log R-10\sqrt{\log R\,(1+\log\log\log N)}
 \tag{1}
$$

on the mask. Only the lower side of the saddle corridor is needed. Write $\mathcal V=1$ for an arbitrary mask, and $\mathcal V=R^{-(2\log 2-1)/2+\epsilon}$ in the saddle case for any fixed $\epsilon>0$.

At each $q,\beta$ write $p_q(r)$ and $f_q(r)$ for the actual $\beta$-modulated residue masses of $P,F$. The unit-centered masses $p_q^*,f_q^*$ are zero at residue zero, and subtract the mean over the nonzero residues elsewhere. For any fixed list $\mathcal M\subset[.90N,1.05N]\cap\mathbb Z$ of size $K$, at each $q,\beta$ select any subset $A_{q,\beta}\subseteq\{M\bmod q:M\in\mathcal M\}$, measurably in $\beta$. Unconditionally,

$$
 \int_{\mathcal B}\sum_{q\in\mathcal Q}
 \left|q\sum_{r\in A_{q,\beta}}p_q^*(N-r)f_q^*(r)\right|d\beta
 \ll K N\left(L^{-3/2}\mathcal V+L^{-2}\right).
 \tag{2}
$$

The omitted phase $e(-N\beta)$ has modulus one. This is a statement about selected rows of the *genuine double-centered covariance*, including all actual aliases represented in each row. It is not a selection of a few alias offsets or Jacobi-product characters. In the one-scale saddle $Z_0=2$, for example any $K\le L^{\,3/2+\delta(2\log2-1)/2-\eta}$ with fixed $\eta>0$ is allowed for an $o(N)$ error. It remains sparse in the globally specified rows; the all-row covariance is not estimated.

There is also a bookkeeping consequence for the full pairing, with no restriction to selected rows. For this same arbitrary $F$ (in particular a saddle mask), summing the *absolute difference of the two signed numerator sums* over the entire shell gives

$$
 \int_{\mathcal B}\sum_{q\in\mathcal Q}
 \left|
  \sum_{a=1}^{q-1} P(a/q+\beta)F(a/q+\beta)e(-N(a/q+\beta))
  -e(-N\beta)q\sum_{r\bmod q}p_q^*(N-r)f_q^*(r)
 \right|\,d\beta
 \ll N\left(L^{-3/2}\mathcal V+L^{-2}\right).
 \tag{3}
$$

Separately deleting the exact nonunit terms $q\mid m$ from the *full* numerator sum, with the same absolute-modulus and integrated convention, costs $O(N/L^2)$ even without (1). The nonunit terms are already absent in $f_q^*$. The comparison (3) for arbitrary product masks does not invoke a principal asymptotic for that masked polynomial.

## 1. Uniform genuine row bounds

The [two-prime residue bound](weak-s-type-ii-critical-prime-double-centered.md#2-the-exact-remaining-numerator-on-the-prime-side) gives $|p_q(r)|\ll X/L$ in every nonzero residue. The cited proof, with the same two independent Selberg squares, uses the hyperbola $uv=c\bmod q$ with nonzero $c$: its incomplete Kloosterman error is uniform in that unit residue, so one can replace $N\bmod q$ by any $r\ne0$. The boxes are strictly below $q$, so $p_q(0)=0$. The total $P_0=P(\beta)$ has $|P_0|\ll N/L$ by counting primes in the fixed boxes. In particular $|p_q^*(r)|\ll X/L$ for all $r$. The [sharp ordinary complementary estimate](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy) gives $\sum |D_m|^2\ll N$, hence

$$
 \sum_m |F_m|^2\ll N,\qquad
 \sum_m |F_m|\ll N. \tag{4}
$$

Masks are only dropped after taking the absolute value or square of the true Fourier coefficient.

Fix $M=0$ or $M\in[.90N,1.05N]\cap\mathbb Z$. The exact physical $F$ support is contained in $[7N/16,N/2)$, so $0<|M-m|<.64N$ for every $m$ on it. Distinct critical primes have product at least $.64N$. Thus for each $m$ there is at most one $q\in\mathcal Q$ for which $m\equiv M\bmod q$.

For an arbitrary mask at most $O(X)$ integers in the physical interval occupy one class modulo $q$. In case (1) we improve this to $O(X\mathcal V^2)$. Indeed put $B=\lfloor2\log R-10\sqrt{\log R(1+\log\log\log N)}\rfloor$. For large $N$ this is nonnegative and any admissible $m$ has at least $B$ distinct band primes. As in [the shifted saddle count](weak-s-type-ii-critical-prime-saddle-sparse-alias-gain.md), its indicator is bounded by $2^{-B}$ times the number of squarefree divisors $h$ of $m$ supported on the band and having at most $B$ factors. Every such $h$ is at most $Z_1^B=N^{o(1)}$ and is coprime to $q$. By CRT, the count in the class is $O(N/(qh)+1)=O(X/h)$ uniformly in $M$, since $Z_1^B=o(X)$. Summing $1/h$ is bounded by $\prod_{Z_0\le p<Z_1}(1+1/p)\ll R$ by prime Mertens. Together with $2^{-B}=R^{-2\log 2+o(1)}$, this proves the stated uniform bound, with effective constants and $N$ sufficiently large for the fixed parameters.

By prime counting, there are $O(X/L)$ critical primes. Using (4), uniqueness of $q$ at each $m$, and the class count just proved, ordinary Cauchy–Schwarz yields, uniformly in $\beta$,

$$
 \sum_{q\in\mathcal Q}|f_q(M)|\ll
 \left(\frac{N}{L}\mathcal V^2\right)^{1/2}
 \left(\sum_m|F_m|^2\right)^{1/2}
 \ll N L^{-1/2}\mathcal V .
 \tag{5}
$$

Here and below $f_q(M)$ means the residue $M\bmod q$. In a selected nonzero row, $|f_q^*(M)|\le |f_q(M)|+O(X)$ by (4) and $q\asymp X$. At $M\equiv0\bmod q$ it is exactly zero. Representatives of duplicate selected rows can be discarded or bounded by summing absolute values over the full list. Now use $q\ll X$, $|p_q^*|\ll X/L$, (5), and $|\mathcal B|=1/(5N)$, proving (2). This uses a sum over the moduli after evaluating the genuine signed row, and permits the stated adaptive row selection.

## 2. Full numerator and nonunit terms

Let $F^u_0=\sum_{r\ne0}f_q(r)=F(\beta)-f_q(0)$, $\bar p=P_0/(q-1)$ and $\bar f=F^u_0/(q-1)$. Finite Fourier summation writes the true full numerator without $e(-N\beta)$ as $q\sum_r p_q(N-r)f_q(r)-P_0F(\beta)$. For $q\nmid N$, expand the centered expression over $r\ne0,N\bmod q$. Their exact difference equals

$$
 (q p_q(N)-P_0)f_q(0)-q\bar p f_q(N)
 -q\bar f\,p_q(N)+P_0F^u_0\left(\frac{q^2}{(q-1)^2}-1\right).
 \tag{6}
$$

If $q\mid N$, $f_q(0)=0$ by the original $N$-unit mask and the difference is $P_0F^u_0/(q-1)$ by direct expansion over the $q-1$ nonzero residues. In (6) the first two factors outside $f_q(0)$ and $f_q(N)$ are $O(N/L)$, while the last two terms are $O(X|F^u_0|/L)$. Use (5) at $M=0,N$, $|F^u_0|\ll N$, and the integration width to obtain (3). These are exact signed numerator identities; (3) is not an absolute estimate on individual numerator coordinates.

The first term of (6) is the contribution of the exact $q\mid m$ slice of the full numerator. It has the following sharper unmasked bound, which also applies to any $|\rho_m|\le1$. Always $k<X/2<q$, so $q\mid m$ implies $d=qr$, and then $r\le B_0:=N^{.50001}/(2q)\ll N^{.00001}$ and $m'=m/q= rk$. The original squarefree support implies $q\nmid r,k$ and weight $-\mu(r)$ on each original admissible splitting. For this coefficient square the unit and squarefree product masks may be dropped, as may $\rho_{qm'}$. At fixed pair of short divisors $r,s\le B_0$, count $m'$ in the actual common hard interval and divisible by $[r,s]$, with floor error $O(1)$. The total floor error is $O(B_0^2)$. The continuous main is an integral over a physical $m'$ interval of length $O(X)$ of the quadratic form $\sum_{r,s\in J(m')}\mu(r)\mu(s)/[r,s]$. Here $J(m')$ is an interval of integers by the exact $qr\in I_d\cap[X,\infty)$ and $r<m'/t$ tests; the bounds at a single endpoint are covered by the same floor errors. The uniform signed gcd quadratic estimate for hard intervals used in the sharp ordinary complementary estimate §1 gives $O(1)$ for this inner form. Thus

$$
 \sum_{q\mid m}|F_m|^2\ll X+B_0^2\ll X,\qquad |f_q(0)|\ll X
$$

uniformly in $q,\beta$. The second inequality uses the $O(X)$ possible integers in that residue. Since $|q p_q(N)-P_0|\ll N/L$ also when $q\mid N$, summing the exact nonunit numerator over $q$ and integrating proves the stated $O(N/L^2)$ deletion. This removes every alias carried by those nonunit products, but gives no estimate for the remaining unit nonprincipal covariance across all rows.
