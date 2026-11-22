# Unconditional signed mean on the full fixed-power admissible Dirichlet complement

Fix $0<\rho<1/2$ and $0<\kappa\le1/2000$. For even $N$, let $I_0(N)=[\rho N,(1-\rho)N]$, let $I\subseteq I_0(N)$ be an arbitrary hard interval with either endpoint convention, and put

$$
 \mathcal Q_N=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\},\qquad
 A_I(N;\alpha)=\sum_{q\in\mathcal Q_N}(\log q)
       \sum_{\substack{p\ {\rm prime},\ (p,N)=1\\qp\in I}}e(\alpha qp),
 \qquad e(t)=e^{2\pi i t}.
$$

These are the original genuine prime legs of [R35](r35-source-square-root-dirichlet-arcs.md), [R37](r37-source-synthetic-localization-dirichlet-complement.md) and [R38](r38-source-four-distinct-prime-minor-reduction.md), with no dense-cell or cofactor-separation restriction. Denote the part of $A_I A_{I_0(N)}$ in which the four constituent primes are distinct by $\mathcal A_I^{(4)}(N;\alpha)$. Both polynomials retain the true unit conditions and marks. Write $Q_N=\lfloor\sqrt N\rfloor$, $R_N=\lfloor Q_N(\log N)^{-200}\rfloor$, and write $\mathfrak m_N$ for the exact complement of the full reduced arcs with $r\le R_N$ and widths $1/(rQ_N)$.

**Theorem (unconditional).** For $L=\log X$, both choices $H_I=A_I A_{I_0(N)}$ and $H_I=\mathcal A_I^{(4)}$ satisfy

$$
 \frac1X\sum_{\substack{X\le N\le2X\\N\ {\rm even}}}\!
  \sup_{I\subseteq I_0(N)}
     \left|\frac1N\int_{\mathfrak m_N}H_I(N;\alpha)e(-N\alpha)\,d\alpha\right|^2
  \ll_{\rho,\kappa} X^{-\kappa}L^{19}.                         \tag{1}
$$

In particular, for each $0<\eta<\kappa/2$ there are at most
$O_{\rho,\kappa,\eta}(X^{1-\kappa+2\eta}L^{19})$ even targets where the absolute value of either signed coefficient exceeds $N^{1-\eta}$ for some $I$. The terms with repeated primes are smaller in the same averaged estimate; their normalized squared mean is $O_{\rho,\kappa}(X^{-2\kappa}L^{16})$. This is a signed arithmetic result on the exact arcs, not a bound for termwise absolute energy, and it is unconditional. It does not apply to cofactor exponents tending to $0$ or $1/2$ with $N$ or to individual exceptional moduli. [R49](r49-source-six-axis-exact-dirichlet-mean.md) retains a stronger power on its own smaller dense cell.

## 1. Joint cell energy at all fixed-power cofactor scales

Take $P=\sqrt X L^{-201}$. Let $\mathfrak m^*$ be the complement of the fixed auxiliary reduced rational arcs $r\le P$, $|\beta|\le P/(rX)$. The auxiliary arcs are contained in every exact major set for large $X$, because $P\le R_N$ and $P/X\le 1/Q_N$. On $\mathfrak m^*$ use Dirichlet approximation with integer parameter $\lceil X/P\rceil$. It gives a reduced $a/r$ with

$$
       P<r\le\lceil X/P\rceil,\qquad
       |\alpha-a/r|\le 1/(r\lceil X/P\rceil)\le r^{-2}.
$$

Indeed an approximant with $r\le P$ would be inside the auxiliary set.

Work initially without target-dependent unit holes in the fixed cofactor envelope $[X^\kappa,2X^{1/2-\kappa}]$ and fixed physical envelope $[\rho X/2,2X]$. These contain every target's original intervals. For every aligned cofactor cell $E$ and physical cell $J$ define

$$
 A_{J,E}(\alpha)=\sum_{\substack{q\in E\\q\ {\rm prime}}}\log q
       \sum_{\substack{p\ {\rm prime}\\ qp\in J}}e(\alpha qp),
$$

with both envelopes implicit. At fixed levels, the $E$ partition the cofactor integers and the $J$ partition the physical integers by the floor test $\lfloor t/H\rfloor$ for a dyadic length $H$, including clipped end cells. We prove

$$
        \sup_{\alpha\in\mathfrak m^*}\sum_{E,J}|A_{J,E}(\alpha)|^2
           \ll_{\rho,\kappa}X^{2-\kappa}L^5.                  \tag{2}
$$

Split the cofactors into ordinary multiplicative dyads $U\le q<2U$, write $V=X/U$, and then aggregate these dyads by Cauchy. In one such dyad, $X^\kappa\ll U\ll X^{1/2-\kappa}$ and $X^{1/2+\kappa}\ll V\ll X^{1-\kappa}$, with constants for clipping. The primes $p$ lie in a fixed proportional range about $V$, depending on $\rho$. Cauchy in $p$ on each $E,J$ costs $O_\rho(V)$, after which the squared sum over $p$ can be enlarged to all integers in this range. Expand the square and sum over $J$ before taking absolute values per ordered pair $q,q'$. For $q=q'$ the disjoint cells cost only $O_\rho(UV^2 L^2)$. For $q'=q+h>q$, same-cell membership requires $hp<H$, and for fixed $h$ at most $O(U)$ choices of $q$ are in the same cofactor cell as $q+h$. Both physical conditions, the $p$ range, and $p<H/h$ cut one real interval in $p$. On its integers the same-cell indicator is exactly

$$
 1-\frac{hp}{H}+\psi((q+h)p/H)-\psi(qp/H),\qquad
 \psi(t)=\{t\}-\tfrac12 ,
                                                               \tag{3}
$$

from subtraction of the two floors. This formula retains the original integer endpoints. Negative differences are conjugate.

Here $U<r/2$ for large $X$ at fixed $\kappa$. The phases $\alpha h$ for $0\le h\le U$ are separated by at least $1/(2r)$ modulo one, using the rational approximation and the distance $1/r$ between distinct residue fractions. The affine term of (3) on each $p$ interval is bounded by $O_\rho(\min(V,\|\alpha h\|^{-1}))$ by Abel summation. Summing the distances from zero and then $q$ bounds the total affine contribution by $O_\rho(U V r L^3)$ including markers and Cauchy.

Put $\delta=\tfrac12+\tfrac\kappa2$. If $H<2 X^\delta$, there is no positive $h$ for large $X$, since $p\gg_\rho X^{1/2+\kappa}$. Otherwise use $K=\lfloor H/X^\delta\rfloor\ge1$ and the mass-one Fejér convolution $\psi_K$ of degree $K$. Its nonzero Fourier coefficients are $O(1/|k|)$ and its zero coefficient vanishes. The endpoint-inclusive discrete error is

$$
   \sum_{j=0}^{H-1}|\psi(j/H)-\psi_K(j/H)|
          \ll H\log(2K)/K+1 .                                \tag{4}
$$

For $|t|\le1/2$, the difference $|\psi(x)-\psi(x-t)|$ is at most $|t|+\mathbf1_{\|x\|\le|t|}$. The grid has at most $O(H|t|+1)$ points near zero. Integrate against the Fejér kernel, whose first absolute moment is $O(\log(2K)/K)$ by its bound $O(\min(K+1,((K+1)t^2)^{-1}))$. This proves (4), also at the jump itself.

For fixed $h$, an integer product $qp$ or $(q+h)p$ in the physical envelope has only $O_\kappa(1)$ eligible cofactor primes at least $X^\kappa$, even after enlarging $p$ to all integers. This follows by multiplying the distinct prime divisors of the product, which is at most $2X$. There are $O(X/H)$ grid periods in the envelope, since $H=O(X)$. Thus the error in (4) over $p,q$ for a fixed $h$ is $O_\kappa(XL/K)$. The number of $h$ is $O_\rho(H/V)$, the outer square cost including the marks is $O_\rho(VL^2)$, and $H/K=O(X^\delta)$. The total error is $O_{\rho,\kappa}(X^{1+\delta}L^3)$, with exponent $1+\delta<2-\kappa$.

For a Fourier mode $1\le k\le K$ the two sawtooths have geometric phase $\alpha h\pm kq/H$ or $\alpha h\pm k(q+h)/H$. In the latter use $q'=q+h$ as summation variable; it belongs to the same dyad and there are no extra multiplicities. Since $kU/H\ll_\kappa X^{-3\kappa/2}$, split the $h$ at $\|\alpha h\|\le4kU/H$. Outside this set the phase has norm at least $\|\alpha h\|/2$, costing $O(UrL)$ summed over $q,h$. Inside it, spacing gives $O(1+rkU/H)$ possible $h$. For one $h$, the integer $q$ phases have spacing $k/H$ in a span $<1/4$ on the circle. Isolate the closest to zero, with bound $O_\rho(V)$, and sum reciprocals for the rest. The cost is $O_\rho(V+(H/k)L)$ irrespective of the endpoints of the geometric interval or any prime restrictions. Thus the entire oscillatory contribution is

$$
  O_\rho\!\left(V L^2\big(VL+HL+rUVK/H+rU L^2\big)\right).
                                                               \tag{5}
$$

In deriving (5), the $O(1/k)$ Fourier coefficients give a summable $k^{-2}$ term and the remaining harmonic sums are $O(L)$. Now $VH\ll X^{2-\kappa}$, $V^2\ll X^{2-2\kappa}$, and
$rUV^2 K/H\ll_{\rho,\kappa}X^{2-\kappa-\kappa/2}L^{201}$ by $UV=X$. Also $V r U\ll X^{3/2}L^{201}$. This makes (5), as well as the affine, diagonal and approximation estimates, $O_{\rho,\kappa}(X^{2-\kappa}L^3)$ per ordinary cofactor dyad. Combining $O(L)$ dyads by Cauchy adds at most $L^2$, proving (2).

## 2. All six moving coordinates, including the exact mask

Use the wide disjoint arcs with $r\le R^*=\lceil\sqrt{2X}L^{-200}\rceil$ and widths $1/(rQ_*)$, $Q_*=\lfloor\sqrt X\rfloor$. They contain every exact major set and are disjoint because the ratio of the sum of two widths to the least distance between their centers is at most $2R^*/Q_*<1$. On their intersection with $\mathfrak m^*$ a point has a unique pair $(r,\beta)$, with $\beta$ the lift around its reduced rational. Partition $r|\beta|$ at all possible values of $1/Q_N$ in the dyad. For each $N$, its exact major set minus the auxiliary arcs is precisely the two-coordinate prefix rectangle $r\le R_N,\ r|\beta|\le1/Q_N$ on this fixed domain, modulo null boundary choices. No part of the exact complement is exchanged for a larger one.

On the two legs there are four integer axes (cofactor and physical index on each). Add the two arc-rank axes. Each hard integer interval or rank prefix is an exact union of $O(L)$ aligned dyadic cells, as is any bounded union of hard intervals. The product coefficient for the selected rectangle expands into $O(L^6)$ fixed-cell Fourier coefficients. The square of its value is at most $O(L^6)$ times the sum of squares over all cell choices and level choices, irrespective of the moving intervals. The term on the entire $\mathfrak m^*$ needs only four axes. At fixed levels, Bessel for the integer Fourier coefficients and disjointness of the rank cells bound the sum over targets and all six cells by

$$
 \int_{\mathfrak m^*}
       \left(\sum_{E,J}|A_{J,E}(\alpha)|^2\right)
       \left(\sum_{F,K}|A_{K,F}(\alpha)|^2\right)d\alpha
 \ll_{\rho,\kappa} X^{3-\kappa}L^7 .                           \tag{6}
$$

Indeed either leg has (2), and the other has integrated summed energy $O(XL^2)$ by Parseval: every physical integer has at most one small-prime/large-prime factorization here, since the prime ranges are disjoint separated by a factor $\gg_\rho X^{2\kappa}$. At fixed levels its unique pair is assigned to one cell. Summing over $O(L^6)$ level choices and the above Cauchy cost gives the maximal squared sum $O(X^{3-\kappa}L^{19})$. The four-axis contribution on the whole auxiliary complement has a smaller log loss. Subtraction restores the true $\mathfrak m_N$ exactly.

All cofactor primes dividing $N$ can be removed as $O_\kappa(1)$ singleton holes, since they are at least $X^\kappa$. This keeps each cofactor selection a bounded union of hard integer intervals. For the original $p$ mask, every possible giant $p\gg_\rho X^{1/2+\kappa}$ exceeds $\sqrt{2X}$ for large $X$, so at most one divides $N$. Fixing this giant leaves $O(X^{1/2-\kappa})$ cofactor indices. The removed transform has squared norm $O(X^{1/2-\kappa}L^2)$ and the other leg has squared norm $O(XL^2)$. Cauchy on the exact complement bounds the pointwise signed change by $O(X^{3/4-\kappa/2}L^2)$. Its squared sum over the dyad is $O(X^{5/2-\kappa}L^4)$, subordinate to (6) with the maximal losses. This proves (1) for the full product. In particular no full-torus substitution of the second hard window was used on this partial-circle coefficient.

## 3. Repeated constituents on the same averaging scale

Because the two prime ranges are disjoint, shared constituents are either the same cofactor or the same giant. For each type and each fixed set of integer cells, write that product polynomial as $\sum_t f_t(t\alpha)g_t(t\alpha)$, where $t$ is the shared prime and the two polynomials sum the original marked partners at their own scales, with the prescribed cells. The indices of the expanded polynomial are $m=t(u+v)$ with $0<m\le4X$. For any such $m$ there are $O_\kappa(1)$ possible $t\mid m$; all eligible shared primes in either type are at least $X^\kappa$. Therefore whole-circle Parseval and the bounded multiplicity over $t$ bound its squared energy by $O_\kappa(1)$ times the sum of the individual fiber energies.

For a given $t$, both ranges for $u,v$ lie in $[1,2X/t]$, with markers of size at most $O(L)$. The convolution has $O(X/t)$ possible integer output indices and for each index at most $O(X/t)$ ordered pairs. Thus its energy is $O((X/t)^3 L^4)$. This bound survives summation over all four integer cells at fixed levels: the coefficients are nonnegative, and each ordered pair with this $t$ is in exactly one product of cells, so summing the squares can only decrease the unpartitioned square. Summing over $t\ge X^\kappa$, even allowing integers rather than primes in this last upper bound, gives $O(X^{3-2\kappa}L^4)$. For the intersection of the two repetition classes, both pairs are the same semiprime. The index is $2qp$, with unique small/large factorization and coefficient of size $O(L^2)$, hence its energy in the same cell sum is $O(XL^4)$.

Apply the exact same six-axis Fourier coefficient estimate as in §2 to each repetition polynomial and their intersection. At fixed levels the rank sets are disjoint; after Bessel one can enlarge their union to the whole circle for the nonnegative squared energy bound just proved. Cofactor unit holes are still exact. On reinstating the excluded giant, the shared-cofactor family loses fibers with one partner fixed as that giant, and the shared-giant family loses at most its entire fiber. In either case the summed squared norm of the removed one-leg fiber polynomials is $O(X^{1/2-\kappa}L^2)$ (the only possible original pairs are indexed by the small prime). The summed squared norm on the other leg is $O(XL^2)$ by disjointness of the factorization. Cauchy over $(t,\alpha)$, using that dilation by $t$ preserves the whole torus norm, gives again an $O(X^{3/4-\kappa/2}L^2)$ pointwise cost. The identical-pair correction for the removed giant has this bound as well, or can be estimated by trivially summing its $O(X^{1/2-\kappa})$ weights. Since $\kappa\le1/2000$, their squared sum $O(X^{5/2-\kappa}L^4)$ is below $X^{3-2\kappa}L^{16}$.

The sum over targets of the squared exact signed repeated contribution is thus $O(X^{3-2\kappa}L^{16})$ using the same twelve logarithmic factors for the maximal argument. In subtracting repetitions, add back the identical-pair class once. This is the exact inclusion–exclusion for four distinct primes and proves the second assertion of (1). Division by $X^3$, equivalent to averaging and taking $N^{-2}$ on the dyad, gives the stated normalization for both products.

## 4. A separate centered consequence assuming global Dirichlet GRH

The genuine coefficient in (1) uses no GRH. Under the separate global Dirichlet GRH assumptions of [R31](r31-source-double-giant-one-leg-centering.md) and [R35](r35-source-square-root-dirichlet-arcs.md), let $M_\kappa(I;N)$ be the [R31](r31-source-double-giant-one-leg-centering.md) local-density comparator for these original fixed-power admissible prime legs and let $A_\kappa(I;N)$ be their genuine sum-line count. The centered covariance in [R31](r31-source-double-giant-one-leg-centering.md) and the full-torus coefficient of the [R35](r35-source-square-root-dirichlet-arcs.md) transforms agree: the terms with equal cofactors have full-torus coefficient zero, including in the synthetic expansion, since the common cofactor is a unit modulo $N$ and all its frequencies are multiples of it. Likewise no shared giant can occur in an actual sum-line representation. By [R37](r37-source-synthetic-localization-dirichlet-complement.md)'s unconditional synthetic removal and the [R35](r35-source-square-root-dirichlet-arcs.md) major bound under GRH, the full-circle centered covariance equals the signed genuine–genuine integral on this exact $\mathfrak m_N$ up to

$$
 O_{\rho,\kappa}\left(N^{1-\kappa/10}+\frac{\mathfrak S(N)N}{(\log N)\log\log N}\right).
$$

Take $\eta=\kappa/4$ in (1) and apply the [R31](r31-source-double-giant-one-leg-centering.md) centering identity. For all but $O_{\rho,\kappa}(X^{1-\kappa/2}L^{19})$ even $N\in[X,2X]$, uniformly for all the hard $I$, this gives

$$
 A_\kappa(I;N)-M_\kappa(I;N)
 =O_{\rho,\kappa}\left(N^{1-\kappa/10}+
                 \frac{\mathfrak S(N)N}{(\log N)\log\log N}\right).
$$

Here global Dirichlet GRH is used only in the imported pointwise major and centering inputs, not the new signed minor estimate. This is an almost-all result for the original fixed-power double-admissible central count, not for exponents approaching the retuned endpoints, the no-giant sector, individual exceptional even integers, or the full weak-S operator.
