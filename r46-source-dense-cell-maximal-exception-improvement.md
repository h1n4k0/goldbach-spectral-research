# A maximal cofactor estimate sharpens dense-cell exceptional counts

Use the exact genuine dense four-prime rectangle of the [signed major evaluation](r43-source-dense-cell-positive-major-obstruction.md), [density-one count](r44-source-dense-cell-density-one-signed.md) and [power-sparse exceptions](r45-source-dense-cell-power-sparse-exceptions.md): fixed $0<\rho<1/2$, $0<\kappa\le1/2000$, even $N$, cofactors $N^{.38}\le q\le N^{.42}$ and $N^{.08}\le s\le N^{.12}$, genuine prime giants, original unit conditions modulo $N$, and marker $(\log q)(\log s)$. Include both possible orders of $qp,sv$ with any moving hard $I\subseteq I_0(N)=[\rho N,(1-\rho)N]$ in the first position and $I_0(N)$ in the second. All four primes are distinct throughout these windows. Let $C_I(N)$ be the true target coefficient and $\mathcal B_I(N)$ the exact R43 real comparator, including its $\lambda(q)\lambda(s)$ factors and original unit conditions.

**Theorem.** Assume global Dirichlet GRH. Fix $0<\eta\le1/100$. There are at most

$$
 O_{\rho,\kappa,\eta}\!\left(X^{31/50+3\eta}(\log X)^{11}\right)
                                                                    \tag{1}
$$

exceptional even $N\in[X,2X]$, independently of the interval, such that all other even moduli satisfy

$$
 C_I(N)=\mathfrak S(N)\mathcal B_I(N)
           +O_{\rho,\kappa,\eta}\big(\mathfrak S(N)N^{1-\eta}\big)
                                                                    \tag{2}
$$

for every original moving hard $I$, with either endpoint convention. Thus at the R45 accuracy $\eta=1/100$ one can take $O_{\rho,\kappa}(X^{13/20}(\log X)^{11})$ exceptions instead of $O(X^{3/4})$. For any fixed $\epsilon>0$ one can take $O_{\rho,\kappa,\epsilon}(X^{31/50+\epsilon})$ exceptions by reducing the fixed power accuracy $\eta$.

For the [exact Dirichlet complementary arc set](r35-source-square-root-dirichlet-arcs.md) $\mathfrak m(N)$ the genuine signed integral is still $O_{\rho,\kappa,\eta}(\mathfrak S(N)N(\log N)^{-13})$ outside the set (1), by subtracting R43. In particular, for an admissible progression of even integers of spacing $d\le X^{19/50-3\eta-\epsilon}$, the exceptional proportion is $O_{\rho,\kappa,\eta,\epsilon}(X^{-\epsilon}(\log X)^{11})$. These are exceptional-set results, not pointwise estimates for the exceptional moduli.

## 1. Freeze only a single physical prefix endpoint

Write $L=\log X$, $P=X^{2/5}$, and let $\mathfrak D_X^*$ be the auxiliary R45 arcs with reduced denominators $r\le P$ and widths $P/(rX)$. Let $\mathfrak m_X^*$ be their complement. Neither is identified with the exact R35 arcs.

For the **full target coefficient only**, when the first summand $n$ lies in $I\subseteq I_0(N)$, the second summand is necessarily $N-n\in I_0(N)$ by symmetry. Thus replace the second-window support by the fixed ambient interval $K=[\rho X/2,2X]$, which contains every actual $I_0(N)$, without changing the coefficient for that first $I$. The corresponding statement for the real convolution at $N$ is exact as well. This replacement is not made in the integral over the exact R35 complement.

Let $J_u=[\rho X/2,u]$ be frozen first prefixes up to a fixed grid endpoint $u$, on an evenly spaced grid of step $O_\rho(X^{1-\eta})$. The grid covers $[\rho X,2(1-\rho)X]$ with one step to spare at both ends inside $K$, giving $O_\rho(X^\eta)$ prefixes. Use the ambient cofactor envelopes $E_*,F_*$ of R45, namely fixed integer intervals covering all possible large and small cofactor bands as $N\in[X,2X]$, with the same endpoint exponents up to constant factors. In a Fourier polynomial take any subintervals $E\subseteq E_*$ and $F\subseteq F_*$, and sum true primes with no $N$-dependent unit exclusions; denote the resulting transforms with physical support $J$ by $A_{J,E},A_{J,F}$. The four prime ranges are disjoint at these supports, so at the full coefficient $qp+sv=N$ the target unit constraints automatically hold, including in the outer brackets.

## 2. Dyadic maximal inequality in both cofactor intervals

For each envelope use the standard integer dyadic partitions by scale, clipped to the envelope. Any hard integer interval is a disjoint union of $O(L)$ cells, at most two per level before clipping. This represents the exact prime set even if the real cofactor endpoints are integers. For fixed $J=J_u$ and $K$, set

$$
 b_{J;E,F}(n)=
 \int_{\mathfrak m_X^*} A_{J,E}(\alpha)A_{K,F}(\alpha)e(-n\alpha)\,d\alpha,
 \qquad e(t)=e^{2\pi i t},
$$

for the order with $E$ on the first leg. The opposite order is treated separately. Cofactor additivity and Cauchy–Schwarz applied to at most $O(L^2)$ cell pairs give

$$
 \sup_{E,F}|b_{J;E,F}(n)|^2
 \ll L^2 \sum_{j,k}\ \sum_{\substack{E'\,{\rm level}\ j\\F'\,{\rm level}\ k}}
                   |b_{J;E',F'}(n)|^2 ,                         \tag{3}
$$

where the supremum is over all subintervals, not just dyadic ones.

For fixed partition levels $j,k$, Bessel sums the right-hand cells and targets at once:

$$
 \sum_{n\in\mathbb Z}\sum_{E',F'} |b_{J;E',F'}(n)|^2
 \le \int_{\mathfrak m_X^*}
   \left(\sum_{E'}|A_{J,E'}(\alpha)|^2\right)
   \left(\sum_{F'}|A_{K,F'}(\alpha)|^2\right)d\alpha .             \tag{4}
$$

On the small-cofactor leg, the integrals of the squared transforms sum to $O_\rho(XL^2)$, by the uniquely oriented factorization of each index and disjoint cofactor cells. For the large-cofactor leg we keep the minor saving after summing its cells. First split $q$ into ordinary multiplicative dyads $U\le q<2U$ with $V=X/U$. At one dyad apply Cauchy–Schwarz over the fixed proportional giant range and sum over all integers there. Within one cofactor cell the two admissible hard ranges for $p$ at fixed $q,q'$ intersect in an interval. Its geometric sum is bounded by $O_\rho(\min(V,\|\alpha(q-q')\|^{-1}))$ off the diagonal. For each difference $h=q-q'$ there are $O(U)$ such pairs **over the entire partition level**, because the cells are disjoint. The same argument with $h=0$ costs $O(UV)$ before the outer Cauchy factor. Consequently

$$
 \sum_{E'}|A_{J,E'}^{(U)}(\alpha)|^2
 \ll_\rho V U L^2\left[V+\sum_{1\le h\le2U}\min(V,\|\alpha h\|^{-1})\right].
                                                                    \tag{5}
$$

For $\alpha\in\mathfrak m_X^*$ use the R44 spacing bound with $P<r\le\lceil X/P\rceil$ and $|\alpha-a/r|\le r^{-2}$, so (5) is $O_\rho(X^2L^3(U^{-1}+V^{-1}+r^{-1}+r/X))$. The large cofactor has $U\gg X^{.38}$, $V\gg X^{.58}$. Cauchy across the $O(L)$ multiplicative dyads and summing their bounds shows

$$
 \sup_{\alpha\in\mathfrak m_X^*}\sum_{E'}|A_{J,E'}(\alpha)|^2
 \ll_\rho X^{2-.38}L^5.
$$

This proof would not follow by separately bounding every cell by one unrestricted norm; the disjoint pair count in (5) avoids a power loss. If the large-cofactor leg is instead on the second side, apply the same proof with its fixed window $K$; the integrated small-leg bound still holds with window $J$.

Combining (3)–(5) with the $O(L^2)$ pairs of levels gives

$$
 \sum_{n\in\mathbb Z}\sup_{E,F}|b_{J;E,F}(n)|^2
 \ll_\rho X^{3-.38}L^{11}
$$

for each prefix and each orientation. At threshold $X^{1-\eta}$ this leaves $O_\rho(X^{.62+2\eta}L^{11})$ exceptional targets per prefix. Union over the $O_\rho(X^\eta)$ prefixes, not over any cofactor cut choices, yields (1) for the signed auxiliary minor term.

## 3. Major completion and exact interval restoration

The R45 prime-leg model approximation on $\mathfrak D_X^*$ is uniform over these arbitrary cofactor subintervals and all the fixed-scale physical windows. Its proof uses only their ambient support and the upper estimates on actual cofactor character energies, not the number of possible endpoints. Thus the hard squared approximation remains $O_\rho(X^{.96}L^{O(1)})$ per leg, and signed prime-model replacement costs $O_\rho(X^{.98}L^{O(1)})=o(X^{1-\eta})$. The completed signed Euler factor for the frozen $q,s$ pair is exactly $\mathfrak S(N)\lambda(q)\lambda(s)\mathbf1_{(qs,N)=1}$ as in R45: if a cofactor divides $N$, its special Euler factor is zero. The initial frozen transforms do not have a moving unit mask; the model restores it.

To sharpen the common exceptional estimate for real and denominator completion, keep the positive $Z_X(N)$ of R45 and use Rankin exponent $\sigma=19/20$, instead of $3/4$. The ordinary local terms $1+2\ell^\sigma/(\ell-1)^2$ form a convergent product, and the two exceptional local terms $1+2q^\sigma/(q-1)$ and $1+2s^\sigma/(s-1)$ are uniformly bounded. The same divisor bound on the averaged Ramanujan sums and the ambient cofactor weight sums $O(1)$ therefore give

$$
 X^{-1}\sum_{n\in[X,2X]}Z_X(n)\ll P^{-\sigma}=X^{-.38}.
$$

By Markov, except for $O(X^{.62+\eta})$ targets one has $Z_X(N)\le X^{-\eta}$. This is common to all physical prefixes and cofactor selections. The real and denominator completion error is $O_\rho(XZ_X(N))$ and the completed real integral is the hard convolution at $N$ for the prefix and the fixed ambient second window. Thus on the good even moduli the actual full count for every grid prefix, both orders, and all cofactor subintervals differs from its exact model by $O_{\rho,\eta}(X^{1-\eta})$.

For any interior real prefix endpoint $u$ not on the grid, bracket the exact hard prefix above and below by nearby grid prefixes, with an extra step if needed to include or exclude an atom. True counts are nonnegative with marker $\log q\log s$, and the real profiles and factors $\lambda$ are uniformly bounded as in R45. Hence changing the physical endpoint by one grid step changes the real integral by $O_\rho(X^{1-\eta})$, independently of the exact cofactor cuts and unit conditions. Positivity brackets the genuine count with the same error after multiplication by $\mathfrak S(N)$. Subtract two exact prefixes, taking the appropriate strict or non-strict convention at each end, to restore any hard $I$ including singletons. At that point the second summand really lies in $I_0(N)$, so the first-step replacement of the ambient window is reversed exactly, for the full count and the real model. This proves (2).

Finally, no polynomial-mask identity is claimed when the ambient second leg replaces $I_0(N)$ on just a portion of the circle. The signed bound in the theorem is obtained only by subtracting the R43 major evaluation for the **original** product and its **original** exact R35 cutoff from the now-restored full coefficient (2). The exceptional count is absolute and does not establish an estimate for any one target in the exceptional set.
