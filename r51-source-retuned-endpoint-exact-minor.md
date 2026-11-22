# Exact signed Dirichlet minor averages at the retuned cofactor endpoints

Fix $0<\rho<1/2$. For sufficiently large even $N$ define the two original retuned long-divisor thresholds by

$$
 j_N=\frac{\log N}{\log\log N},\qquad
 D_N=\left\lfloor\sqrt N\,e^{-20j_N}\right\rfloor,\qquad
 Q_{\rm prod}(N)=\left\lfloor N e^{-20j_N}\right\rfloor .
$$

Put $I_0(N)=[\rho N,(1-\rho)N]$, and for any hard interval $I\subseteq I_0(N)$ with either endpoint convention use the genuine weighted prime polynomial

$$
 A_I(N;\alpha)=
    \sum_{\substack{q\ {\rm prime},\ \log N<q\le D_N\\(q,N)=1}}
        (\log q)\!\!\sum_{\substack{p\ {\rm prime},\ (p,N)=1\\qp\in I}}
                     e(\alpha qp),\qquad e(t)=e^{2\pi i t}.
$$

Let $\mathcal A_I^{(4)}$ be the part of $A_I A_{I_0(N)}$ with all four primes distinct. Let $Q_N=\lfloor\sqrt N\rfloor$ and $R_N=\lfloor Q_N(\log N)^{-200}\rfloor$. The exact set $\mathfrak m_N$ is the complement of all reduced arcs with denominator $r\le R_N$ and widths $1/(rQ_N)$, as in [R35](r35-source-square-root-dirichlet-arcs.md). These cutoffs are not interchangeable with $D_N$ or $Q_{\rm prod}(N)$.

**Theorem (unconditional).** For every fixed $C>0$, with $L=\log X$, both $H_I=A_I A_{I_0(N)}$ and $H_I=\mathcal A_I^{(4)}$ satisfy

$$
 \frac1X\sum_{\substack{X\le N\le2X\\N\ {\rm even}}}
 \sup_{I\subseteq I_0(N)}
 \left|\frac1N\int_{\mathfrak m_N}H_I(N;\alpha)e(-N\alpha)\,d\alpha\right|^2
 \ll_{\rho,C} L^{-C}.                                         \tag{1}
$$

The exact contribution of repetitions also satisfies (1). Thus for each fixed $a,b>0$ the signed genuine normalized coefficient is $O_{\rho,a,b}(L^{-a})$ for every hard $I$ on the same dyad, except for $O_{\rho,a,b}(X L^{-b})$ even targets. This reaches the true retuned endpoints $\log N<q\le D_N$ rather than taking a limit of the fixed-power exponents of [R50](r50-source-full-admissible-exact-dirichlet-mean.md).

Here is the connection to the original arithmetic labels. On a central sum line $n+m=N$, if $n=qp$, $q$ is selected above, and $p$ is prime, then $p\ge \rho N/D_N>D_N$ and in fact $pD_N\ge\rho N>Q_{\rm prod}(N)$ for large $N$. The two prime factors are distinct and exceed $\log N$, so this leg has no small prime. The only divisors $d>D_N$ are $p$ and $qp$; the latter has logarithmic mark $\log(n/d)=0$, the former has mark $\mu(p)\log(n/p)=-\log q$. For both legs the positive product cutoff $de>Q_{\rm prod}(N)$ is automatic: each contributing nonzero divisor is at least $\rho N/D_N$, and already $pD_N>Q_{\rm prod}(N)$ and $e>D_N$. Thus the raw zero-small double-giant contribution has coefficient $(\log q)(\log s)$ before the negative sum-alias sign and uses the exact original cutoffs. The raw identification is algebraic. **The bound (1) is for this genuine signed partial-circle integral, not the whole sum-line count.** No centered asymptotic is transferred from [R31](r31-source-double-giant-one-leg-centering.md) or [R35](r35-source-square-root-dirichlet-arcs.md), which require a fixed power gap; this does not address exceptional moduli, proper-power or other rough–rough sectors, or Hypothesis S.

## 1. Auxiliary arcs and the short cofactor range

Take $P=\sqrt X L^{-201}$, put $Q'=\lceil X/P\rceil$, and let $\mathfrak m^*$ be the complement of the fixed reduced auxiliary arcs $r\le P$, $|\beta|\le P/(rX)$. These auxiliary arcs are contained in every exact major set for large $X$, since $P\le R_N$ and $P/X\le1/Q_N$. Use the same fixed physical envelope $[\rho X/2,2X]$ as [R50](r50-source-full-admissible-exact-dirichlet-mean.md), and a fixed dyad-wide cofactor envelope $[2,U_*]$, where

$$
       U_*=\sqrt X\exp(-19L/\log L).
$$

Every $D_N\le U_*$ for large $X$, because $x/\log x$ increases for large $x$ and $\sqrt N\le\sqrt{2X}$. All allowed partner primes on this envelope are $\gg_\rho X/U_*$, hence exceed every cofactor in the envelope and also $\sqrt{2X}$. Unique small/large factorization holds at every physical frequency. At fixed levels, let $E,J$ partition the integer cofactor and physical axes into aligned dyadic cells, clipped only to their fixed envelopes.

Fix any $B>0$, chosen after $C$. For one $q\le L^B$, let
$f_{q,J}(\alpha)=(\log q)\sum_{p\ {\rm prime},\ qp\in J}e(qp\alpha)$.
On $\mathfrak m^*$ apply Dirichlet approximation to the **dilated** phase $q\alpha$, with integer parameter $Q'$, obtaining a reduced $a/d$ with $d\le Q'$ and $|q\alpha-a/d|\le1/(dQ')\le d^{-2}$ in a lift. It must have $qd>P$. In fact if $qd\le P$, on reducing $a/(qd)$ to denominator $r\le qd$ the error for $\alpha$ is at most $1/(qdQ')\le P/(qdX)\le P/(rX)$, contrary to $\alpha\in\mathfrak m^*$. This works even if $q$ divides the numerator, and also for lifts on the torus. Thus

$$
       \sqrt X\,L^{-201-B}<d\ll\sqrt X\,L^{201}.
                                                               \tag{2}
$$

The partner primes for one physical cell lie in a real interval of scale $V=X/q$. The [Vaughan estimate, Montgomery–Vaughan II, Theorem 17.1](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) applies to both prefixes of every such interval, since the approximation error is $\le d^{-2}$. Its bound is
$O((Vd^{-1/2}+V^{4/5}+\sqrt{Vd})(\log(2V))^{5/2})$ for the von Mangoldt weight. Proper powers cost at most $O(\sqrt V\,L^2)$, and partial summation by $1/\log p$ on $p\asymp_\rho V$ gives the prime-only, unweighted partner transform. Restoring $\log q\le L$, (2) implies uniformly for every hard $J$ that

$$
       |f_{q,J}(\alpha)|\ll_{\rho,B}X^{4/5}L^{O_B(1)}
          \qquad(\alpha\in\mathfrak m^*).
                                                               \tag{3}
$$

The two endpoint atoms are allowed; the cut is an integer prefix difference. At one fixed level of physical cells, $\sum_J|f_{q,J}|\ll_\rho (X/q)L$, because the prime supports are disjoint even though the phases are not. Therefore

$$
       \sup_{\alpha\in\mathfrak m^*}\sum_J|f_{q,J}(\alpha)|^2
             \ll_{\rho,B} X^{9/5}L^{O_B(1)} .                   \tag{4}
$$

Cauchy over the at most $L^B$ small cofactors, followed by summation over the disjoint $E$ cells, gives this same power $X^{9/5}$, with possibly more fixed logarithms, for the whole joint cell energy of the portion $q\le L^B$. This step treats the exact short-cofactor primes, not a synthetic approximation.

## 2. The high cofactor range up to the actual subpower edge

On $\mathfrak m^*$ apply the undilated Dirichlet approximation with $Q'$, giving a reduced $a/r$, $P<r\le Q'$, error $\le r^{-2}$. Restrict now to $L^B<q\le U_*$. Partition this range into ordinary multiplicative dyads $U\le q<2U$, put $V=X/U$, and retain the clipped dyad endpoints. Uniformly $U\ll U_*<r/2$, $V\ll X L^{-B}$, and $p\asymp_\rho V\gg_\rho X/U_*$. We repeat the [R50](r50-source-full-admissible-exact-dirichlet-mean.md) joint-cell argument with the non-power cutoff scale

$$
             Y_0=\sqrt X\,L^{203}.
$$

In particular $p/Y_0\to\infty$ uniformly; this is where the true retuned endpoint $D_N$ is used.

For clarity, Cauchy in the partner variable $p$ at each $E,J$ costs $O_\rho(V)$, after which that variable can be enlarged to all integers in its dyad-scale interval. Expanding the square and summing over all physical cells before taking absolute values gives the floor-cell factor

$$
     1-hp/H+\psi((q+h)p/H)-\psi(qp/H),\qquad
         \psi(t)=\{t\}-\tfrac12,
                                                               \tag{5}
$$

for $q'=q+h>q$ on the interval cut by $hp<H$ and the two physical-envelope bounds, where $H$ is the physical cell length. On the remaining range its value is zero. The floored identity and hard integer endpoints are unchanged from [R50](r50-source-full-admissible-exact-dirichlet-mean.md). Negative differences are conjugate. The diagonal costs $O(UV^2L^2)$. Since $\alpha h$ for $0\le h\le U$ are $1/(2r)$-separated, summing the affine part costs $O_\rho(U V r L^3)$ by the same geometric-sum and Abel bounds, including the marks and the outer $O(V)$.

If $H<2Y_0$, there is no positive $h$ for large $X$. Otherwise use the Fejér approximation with degree $K=\lfloor H/Y_0\rfloor$. The discrete error in [R50](r50-source-full-admissible-exact-dirichlet-mean.md), $\sum_{j=0}^{H-1}|\psi(j/H)-\psi_K(j/H)|\ll H\log(2K)/K+1$, includes the jump. For a fixed $h$ each integer product in (5) has at most $O(L)$ possible divisor primes $q$ or $q+h$, even though $p$ has been enlarged to all integers. The physical envelope has $O(X/H)$ grid periods. Accordingly the total error for one $h$ in the unmarked expansion is $O(X L^2/K)$. Summing at most $O_\rho(H/V)$ values of $h$, then multiplying by the outer $O_\rho(VL^2)$ with the marks, costs $O_\rho(XY_0 L^4)$, since $H/K\ll Y_0$. This is $O(X^{3/2}L^{207})$, with no power-sized divisor bound.

For a nonzero Fourier frequency $1\le k\le K$, the two phases are $\alpha h\pm kq/H$ and $\alpha h\pm k(q+h)/H$. In the second case change the summation variable to $q+h$ at fixed $h$. Here $kU/H\le U/Y_0=o(1)$ uniformly. For $\|\alpha h\|>4kU/H$ the shifted phase stays at least $\|\alpha h\|/2$ from zero, for total bound $O(UrL)$ before the outer factor. Otherwise the number of possible $h$ is $O(1+rkU/H)$, since the phase centers are spaced. For each such $h$, the $q$ phases have step $k/H$ in a span $<1/4$, and the sum of truncated reciprocals is $O_\rho(V+(H/k)L)$, by isolating the nearest phase and summing harmonic distances. The Fourier coefficients are $O(1/k)$. Consequently after summation over $k$ the amount is

$$
 O_\rho\!\left(VL^2(VL+HL+rUVK/H+rU L^2)\right).
                                                               \tag{6}
$$

The two terms involving $r$ satisfy $r\,U V L^4\ll X^{3/2}L^{205}$ and
$rUV^2(K/H)L^2\ll X V$ since $r/Y_0\ll L^{-2}$. The other terms are bounded by $O_\rho(X^2 L^{3-B})$ using $VH\ll X^2 L^{-B}$ and $V\ll X L^{-B}$. For fixed $B$, the diagonal, affine, and Fejér errors also fit this bound for large $X$. Cauchy in the $O(L)$ ordinary dyads costs at most $L^2$ in the joint energy upper bound. Combining this high portion with (4), which is smaller by a fixed power, yields for the true joint cells without target units

$$
 \sup_{\alpha\in\mathfrak m^*}\sum_{E,J}|A_{J,E}(\alpha)|^2
                \ll_{\rho,B} X^2 L^{5-B}.
                                                               \tag{7}
$$

## 3. Signed coefficient and target-dependent holes

Use exactly the wide disjoint arcs and two rank-prefix coordinates from [R50](r50-source-full-admissible-exact-dirichlet-mean.md): denominators $r\le\lceil\sqrt{2X}L^{-200}\rceil$, widths $1/(r\lfloor\sqrt X\rfloor)$, and offsets ranked by $r|\beta|$ between the possible thresholds $1/Q_N$. On their intersection with $\mathfrak m^*$, the exact major set outside the auxiliary arcs is the rectangle $r\le R_N,\ r|\beta|\le1/Q_N$. Both rank axes have $O(L)$ levels. Subtract the Fourier coefficient on this rectangle from the one on all of $\mathfrak m^*$, without any replacement of $\mathfrak m_N$.

The physical axes are the actual hard $I$ and actual hard $I_0(N)$, representable as unions of $O(L)$ aligned integer cells. Each cofactor axis uses the exact target interval $(\log N,D_N]$ minus the primes dividing $N$. There are at most $O(L)$ such holes and the resulting union of integer intervals can be decomposed into $O(L^2)$ cells. Thus at most $O(L^8)$ fixed-cell coefficients occur in each expansion (two cofactor axes, two physical axes, two rank axes). The number of level choices is still $O(L^6)$, giving combined maximal loss $O(L^{14})$ after Cauchy. For fixed levels apply Bessel over integer output targets; disjoint rank cells leave the integral over a subset of $\mathfrak m^*$ of the product of the two summed joint cell energies. Use (7) for one, and $O(XL^2)$ integrated energy for the other by Parseval and unique small/large factorization. With the $L^{14}$ cost the squared sum is $O_{\rho,B}(X^3L^{21-B})$. The entire auxiliary complement term needs only four axes and has no greater cost.

Every actual excluded giant dividing $N$ exceeds $\sqrt{2X}$, so there is at most one. Its removed polynomial has squared energy $O(U_* L^2)\ll X^{1/2}L^2$, since only its cofactor varies. Cauchy against the other leg with energy $O(XL^2)$ changes the signed coefficient by at most $O_\rho(X^{3/4}L^2)$ pointwise, uniformly in all hard intervals. Its squared sum $O(X^{5/2}L^4)$ is absorbed. This reinstates the true $N$-unit condition also on the large prime, after it was already exact on the cofactor. No change of either physical window was needed.

## 4. Four distinct primes and the repeated fibers

As the cofactor and partner ranges are disjoint, repetitions come from a shared cofactor or shared partner. Fix the integer cell levels and the corresponding repetition polynomial, and write it as $\sum_t f_t(t\alpha)g_t(t\alpha)$, where $t$ is one of those shared primes. These fibers have nonnegative coefficients and indices $m=t(u+v)\le4X$.

For $t>L^B$ use the whole-circle energy: each $m$ has at most $O(L)$ possible prime divisors $t$, and each fiber has squared energy $O((X/t)^3L^4)$ by counting ordered partner pairs at each sum. At fixed levels each ordered pair is in one combination of cells, so positivity means summing squared cell energies only decreases the unrestricted bound. After summing over $t>L^B$ the bound is $O(X^3L^{5-2B})$. This handles both types at high $t$, and all shared large partners.

For shared cofactors $t\le L^B$, use instead the bound on $\mathfrak m^*$ from (4). At fixed four integer cell levels, Cauchy over the at most $L^B$ possible $t$ reduces the summed integral to at most $L^B$ times the sum, over $t$, of

$$
   \int_{\mathfrak m^*}
        \left(\sum_J |f_{t,J}(\alpha)|^2\right)
        \left(\sum_K |f_{t,K}(\alpha)|^2\right)d\alpha .
$$

At each fixed $t$ the shared cofactor lies in only one cell per cofactor axis. One parenthesis has supremum $O_{\rho,B}(X^{9/5}L^{O_B(1)})$ by (4), the other integrated energy $O((X/t)L^2)$ by disjoint physical prime supports and Parseval. Hence this low shared part has energy $O_{\rho,B}(X^{14/5}L^{O_B(1)})$ before the maximal losses. Here the integration cannot be enlarged to all of $\mathbb T$ before applying (4); the exact rank cells and also the unsubtracted term lie inside $\mathfrak m^*$, which is sufficient for Bessel. The intersection of the two repetition classes is the identical constituent pair, with frequencies $2qp$ and squared energy $O(XL^4)$ by uniqueness. It is added back once.

Reassemble these estimates with the same $O(L^{14})$ maximal loss. On putting back the giant units the removed one-leg fiber energy totals $O(U_*L^2)$, whether a whole shared-giant fiber or individual shared-cofactor partners are removed. The other summed fiber energy totals $O(XL^2)$, so direct-sum Cauchy over the shared prime and $\alpha$ gives the same absorbed $O(X^{3/4}L^2)$ change per target. The identical pair removal has still smaller absolute cost by counting its $O(U_*)$ weights. Thus the repetitions obey (1) as well. Take $B>C+22$ and divide all squared sums by the equivalent dyadic normalization $X^3$. This proves (1). Markov's inequality with $C>b+2a$ gives the displayed exceptional count. Neither a fixed-power centered estimate at varying parameters nor a pointwise error for those exceptions is asserted.
