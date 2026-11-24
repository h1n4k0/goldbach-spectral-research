# The genuine ordinary-energy obstruction survives the count-saddle cut

Use the exact fixed box and hard endpoints of the [ordinary-energy obstruction](weak-s-type-ii-fixed-prime-box-minor-l2.md): $N=2^j$, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and

$$
I_u=[.740X,.745X],\quad I_v=[.715X,.720X],\quad
I_d=[X,.100N^{.50001}],\quad y=9N/16,\quad t=N^{.49999}.
$$

Let $P,D$ be the true polynomials there. Fix $A>0$ and set $W=L^A$. Choose any fixed finite list of count bands with $Z_{1,i}=\exp(L^{\delta_i})$, $0<\delta_i<1$, and either $Z_{0,i}=2$ or $Z_{0,i}=\exp(L^{\gamma_i})$ for $0<\gamma_i<\delta_i$. Write $R_i=\log Z_{1,i}/\log Z_{0,i}$ and $b_{1,i}(m)$ for the exact product of the primes of the squarefree integer $m$ in $[Z_{0,i},Z_{1,i})$. Let $D_{\rm sad}$ consist of the **complete true coefficient** at each such $m$ for which

$$
P^-(m)\le W,\qquad
|\omega(b_{1,i}(m))-2\log R_i|
 \le 10\sqrt{\log R_i(1+\log L_2)}
 \quad\hbox{for every band }i,
$$

and zero elsewhere. This is a restriction on the actual product $m$, not a selection of Möbius summands within its coefficient.

Then unconditionally $\|D_{\rm sad}\|_{L^2(\mathbb R/\mathbb Z)}^2\asymp N$. Its squared energy remains $\gg N$ even when restricted to the exact **integer coefficient carrier** used in the original lower bound, described below. Also $\|D_{\rm sad}\|_{L^2(\mathfrak m)}^2\gg N$ on the original broad stretched minor union $\mathfrak m$ of that proof. The latter conclusion for $D_{\rm sad}$ alone uses the unconditional stretched-major estimate for $D$ there; the simultaneous lower for the left prime norm on that same stretched minor retains the stated historical Dirichlet GRH. Neither assertion is a lower on the much narrower critical-prime shell or on any signed pairing.

## 1. Only true product masks are removed

The [least-prime exchange](weak-s-type-ii-critical-prime-least-prime-boundaries.md) gives the whole original coefficient as the sum of the three signed true branches at every squarefree $m$. In the example the prime product gate is active only to define the existing hard support; the stated prime boxes already fit it. The [polylogarithmic least-prime tail](weak-s-type-ii-critical-prime-polylog-boundary-width.md) removes $P^-(m)>W$ with squared ordinary cost $o(N)$. At $P^-(m)\le W$, the [signed count-saddle theorem](weak-s-type-ii-critical-prime-signed-count-saddle.md) gives squared ordinary cost $o(N)$ for each of the two tails outside the displayed window for any fixed band. In particular it applies to the full true coefficient, not just to a term of one branch. Since the union of discarded products lies in the union of these finitely many sets, Parseval and the nonnegativity of squared coefficients give

$$
\|D-D_{\rm sad}\|_{L^2(\mathbb R/\mathbb Z)}^2=o(N).
$$

There is no loss from overlapping count conditions or from the sharp endpoints. This applies to any fixed finite list; no assertion of uniformity in an increasing family of bands is needed.

## 2. The surviving energy and its exact scope

The original ordinary lower is already proved on the disjoint integer carrier $m=P_* k$, where $P_*$ is a prime in $[N^{.500002},N^{.500006}]$ and $k$ is odd squarefree in $[.450N/P_*,.490N/P_*]$. There the whole original coefficient is $-\sum_{b\mid k,\ b\le .100N^{.50001}/P_*}\mu(b)$, with $P_*$ unique. The original variance calculation gives total squared mass $\gg N$ on this carrier. Within it the same product mask can remove at most the $o(N)$ mass just proved, so its retained mass is still $\gg N$. On the full circle the ordinary universal upper $O(N)$ for the exact $D$ follows from the [sharp complementary energy](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy), and a product mask contracts squared ordinary energy.

On the broad stretched minors, the original proof bounds the **unfiltered** $D$ energy on the stretched majors by $o(N)$ unconditionally; therefore the unfiltered minor energy is $\gg N$ unconditionally. Restricting the difference to the minor union cannot increase its $o(N)$ squared cost, hence triangle leaves $\|D_{\rm sad}\|_{L^2(\mathfrak m)}\gg\sqrt N$. This argument does not assert a stretched-minor lower after first taking the narrower carrier projection in coefficient space. For the original prime $P$, the broad stretched-minor lower still uses global Dirichlet GRH (including ordinary RH) as in the original proof. With that input both norms in the separate Cauchy quantity remain $\gg\sqrt N$ on this broad union. The corresponding classical smaller-major removal for $P$ is unconditional by the original Siegel–Walfisz argument, with ineffective constants.

This locates the existing whole-circle and broad-minor method obstruction inside simultaneous true count saddles. It says nothing about the sign of that covariance, the local norm on the near-square-root prime arcs, or weak S.
