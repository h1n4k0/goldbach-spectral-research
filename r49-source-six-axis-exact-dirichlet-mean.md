# A six-axis maximal bound for the genuine exact Dirichlet minor coefficient

Use the same genuine dense four-prime rectangle and notation as [R47](r47-source-exact-dirichlet-minor-maximal-unconditional.md). For fixed $0<\rho<1/2$ and even $N$, the small prime factors satisfy $N^{.38}\le q\le N^{.42}$ and $N^{.08}\le s\le N^{.12}$, and $p,v$ are the respective genuine prime giants. Use both orders of $qp,sv$, the original unit conditions modulo $N$, marker $(\log q)(\log s)$, and the original windows $I\subseteq I_0(N)=[\rho N,(1-\rho)N]$ and $I_0(N)$. The exact product is $\mathcal P_I(N;\alpha)$. Write $\mathfrak m_N$ for the complement of the full [R35 family](r35-source-square-root-dirichlet-arcs.md) with $Q_N=\lfloor\sqrt N\rfloor$, $R_N=\lfloor Q_N(\log N)^{-200}\rfloor$ and all complete reduced arcs of widths $1/(rQ_N)$ for $r\le R_N$. Put $e(t)=e^{2\pi it}$.

**Theorem (unconditional).** With $L=\log X$,

$$
 \frac1X\sum_{\substack{X\le N\le2X\\N\ {\rm even}}}
 \sup_{I\subseteq I_0(N)}
 \left|\frac1N\int_{\mathfrak m_N}\mathcal P_I(N;\alpha)e(-N\alpha)\,d\alpha\right|^2
 \ll_\rho X^{-19/50}L^{19}.                                    \tag{1}
$$

The supremum is over all exact hard intervals and their original endpoint conventions. Consequently, at any fixed power target $N^{1-\eta}$, $0<\eta<19/100$, the exceptional count is $O_{\rho,\eta}(X^{31/50+2\eta}L^{19})$. In particular $\eta=1/100$ gives $O(X^{16/25}L^{19})$ instead of the R47 $O(X^{17/25}L^{23})$, and one may take $\eta=1/10$ with $O(X^{41/50}L^{19})$ exceptions. No estimate at each individual exceptional target, or for the full weak-S operator, is asserted.

## 1. Auxiliary spacing and physical partition cells

Use fixed auxiliary arcs with denominators $r\le P=\sqrt X\,L^{-201}$, of widths $P/(rX)$, and write $\mathfrak m^*$ for their complement. These auxiliary arcs are contained in every exact $\mathfrak D_N$ for large $X$, since $P\le R_N$ and $P/X\le1/Q_N$; they are not relabeled as the exact arcs. Every $\alpha\in\mathfrak m^*$ has a reduced Dirichlet approximant with $P<r\le\lceil X/P\rceil$ and $|\alpha-a/r|\le r^{-2}$. In particular $r\gg \sqrt X L^{-201}$ and $r\ll \sqrt X L^{201}$.

Use the fixed cofactor envelopes of R47 and a common physical envelope of integers in $[\rho X/2,2X]$. At fixed levels of the two respective dyadic partitions let $E$ run through disjoint cofactor cells of the large cofactor envelope, and $J$ through clipped cells on the physical axis, given by the integer blocks with $\lfloor t/H\rfloor=j$ for a fixed integer dyadic length $H$ and all indices $j$. Such a partition may clip the end blocks to the physical envelope without changing this floor test on the envelope. Define $A_{J,E}(\alpha)$ to be the actual prime-marked transform without any target-dependent unit exclusions. The new estimate is

$$
 \sup_{\alpha\in\mathfrak m^*}\sum_{E,J}|A_{J,E}(\alpha)|^2
       \ll_\rho X^{2-.38}L^5                                  \tag{2}
$$

**simultaneously over both partition cell families**. In contrast, R47 fixes the physical window when using the corresponding cofactor estimate.

Split the large cofactors into ordinary multiplicative dyads $U\le q<2U$ with $V=X/U$. Here $U\gg X^{.38}$, $U\ll X^{.42}$, and $V\asymp_\rho X/U$; the giant lies within a fixed proportional range about $V$. After Cauchy in the giant for each $E,J$, enlarge the remaining giant sum to all integers of that range. Expand the square and sum over **all physical cells at this level before taking absolute values in each off-diagonal pair of cofactors**. For fixed $q,q'=q+h$ in the same cofactor cell and in the ordinary dyad, this gives a sum over an interval of $p\asymp_\rho V$, with both $qp,q'p$ in the physical envelope and the same-block indicator. The diagonal $h=0$ costs $O_\rho(U V^2L^2)$, including the outer Cauchy factor: disjointness of the physical cells means each $p$ is counted only once. For $h>0$ the indicator vanishes unless $hp<H$, so it suffices to sum over $1\le h\ll_\rho H/V$ as well as $h\le U$; negative differences are covered by conjugation. The added strict cut $p<H/h$ keeps the range an interval, and on it the indicator is exactly

$$
 1-\frac{hp}{H}+\psi\!\left(\frac{(q+h)p}{H}\right)
                   -\psi\!\left(\frac{qp}{H}\right),
 \qquad \psi(t)=\{t\}-\tfrac12 .                               \tag{3}
$$

This follows by subtracting the integer parts and applies also at the integer boundary residues. Each difference $h$ has at most $O(U)$ possible $q$ over the whole fixed cofactor partition because the cells are disjoint. The affine term in (3) costs, by Abel summation, $O_\rho(\min(V,\|\alpha h\|^{-1}))$ on each $p$ interval. Since $U<r/2$ for large $X$, the numbers $\alpha h$ for $0\le h\le U$ are pairwise separated modulo one by at least $1/(2r)$; this follows from the reduced approximant and $|\alpha-a/r||h-h'|\le1/(2r)$. In particular the nonzero $h$ are spaced also from zero. Thus their reciprocal distances sum to $O(rL)$, and the affine contribution is at most $O_\rho(U V r L^3)$ after the Cauchy and marker factors.

## 2. Discrete Fejér error and the two-dimensional phases

If $H<2X^{.55}$ there is no off-diagonal term for large $X$, since $p\gg_\rho X^{.58}$. Otherwise let $K=\lfloor H/X^{.55}\rfloor\ge1$, and use the Fejér mean $\psi_K$ of the exact sawtooth in (3), with degree $K$ and Fourier coefficients $O(1/|k|)$ for $0<|k|\le K$, with zero constant term. Its discrete error is

$$
 \sum_{j=0}^{H-1}|\psi(j/H)-\psi_K(j/H)|
       \ll H\frac{\log(2K)}{K}+1.                              \tag{4}
$$

Indeed for $|t|\le1/2$ one has $|\psi(x)-\psi(x-t)|\le |t|+\mathbf1_{\|x\|\le |t|}$. The number of grid points at distance at most $|t|$ from zero is $O(H|t|+1)$, including the asymmetric endpoint at zero. Convolution with the nonnegative mass-one Fejér kernel and its first absolute moment $O(\log(2K)/K)$ prove (4); the latter follows from the usual bound $\ll\min(K+1,((K+1)t^2)^{-1})$.

For each $h$, the multiplicity of an integer product $qp$ or $(q+h)p$ in the enlarged $p,q$ sum is at most its divisor count, $O_\epsilon(X^\epsilon)$. All such products are in the fixed physical envelope; since $H=O(X)$, over it there are $O(X/H)$ periods for (4). Thus the total error for one $h$ and either sawtooth is $O_\epsilon(X^{1+\epsilon}L/K)$, using $K<H$. The number of $h$ is $O_\rho(H/V)$; multiplying by $O_\rho(VL^2)$ from Cauchy and the markers bounds the oscillatory approximation error by

$$
 O_{\rho,\epsilon}(HX^{1+\epsilon}L^3/K)
 =O_{\rho,\epsilon}(X^{1.55+\epsilon}L^3).
$$

No pointwise approximation at a sawtooth jump was dropped.

For each nonzero $k$ with $|k|\le K$, expand the two sawtooths into the phases $\alpha h\pm |k|q/H$ or $\alpha h\pm |k|(q+h)/H$ in $p$. In the latter expression use $q'=q+h$ as the summation variable with $h$ fixed, so it stays in the same ordinary dyad and obeys the identical upper bound. Write $k>0$ below to bound both signs. Since $kU/H\le U X^{-.55}=o(1)$, split $h$ according to $\|\alpha h\|\le4kU/H$ or its complement. On the complement, $\|\alpha h\pm kq/H\|\ge\|\alpha h\|/2$; hence the summed geometric upper bound over $h,q$ is $O(Ur L)$ by the spacing from zero already proved. On the near set there are $O(1+r kU/H)$ possible $h$. For each one, the phases as $q$ ranges over integers of the ordinary dyad are spaced by $k/H$ in an interval of length $O(kU/H)<1/4$ modulo one. Summing their geometric bounds therefore costs $O(V+(H/k)L)$ for one $h$, by isolating the nearest point to zero and summing harmonic distances. The overall bound at $k$ is

$$
 O_\rho\left((1+r kU/H)(V+(H/k)L)+UrL\right).
$$

Summing with coefficients $O(1/k)$ up to $K$ and multiplying by $O_\rho(VL^2)$ gives

$$
 \ll_\rho V L^2\bigl(VL+HL+rUVK/H+rU L^2\bigr).
$$

The possibly largest terms are $V H L^3\ll X^{1.62}L^3$, and $rUV^2 K/H\ll X^{.5}L^{201}X V X^{-.55}\ll X^{1.57}L^{201}$. The others, the affine bound, and the Fejér error with a fixed small $\epsilon$ are all $\ll X^{1.62}L^3$ for large $X$. The diagonal $UV^2L^2$ is bounded likewise. Thus the bound per ordinary cofactor dyad is $O_\rho(X^{1.62}L^3)$ uniformly in both partition levels. Cauchy over the $O(L)$ ordinary cofactor dyads and then summation adds at most $L^2$, proving (2).

## 3. Six dyadic axes and exact restoration

Use the wide disjoint arc union of [R47 §1](r47-source-exact-dirichlet-minor-maximal-unconditional.md#1-encode-the-moving-exact-arcs-as-two-prefix-coordinates) with $r\le R^*=\lceil\sqrt{2X}L^{-200}\rceil$ and widths $1/(r\lfloor\sqrt X\rfloor)$. On its intersection with $\mathfrak m^*$ use the same two rank coordinates: the unique arc denominator and $v=r|\beta|$, with $v$ partitioned at every threshold $1/Q_N$ for integer $Q_N$ in the dyad range. Boundaries are harmless null sets. For any $N$, $\mathfrak D_N$ outside the auxiliary arcs is the intersection of two prefixes in these coordinates. Thus $\mathfrak m_N$ is the fixed $\mathfrak m^*$ minus one of those rank rectangles. All rank cells are disjoint at fixed pairs of levels and lie inside the fixed $\mathfrak m^*$.

Represent each of the two physical hard windows and each of the two cofactor intervals by $O(L)$ dyadic cells on its integer axis. Fixed unions of $O(1)$ intervals have the same bound. Represent both rank prefixes by $O(L)$ dyadic cells each. Cofactor and physical truncation are independent restrictions on a polynomial coefficient and hence additive over their product cells. At a target $n$, the square of the supremum over these choices is bounded by $O(L^6)$ times the sum of squared coefficients over all six level indices and cells, by Cauchy applied to each expansion into $O(L^6)$ terms. For fixed levels, Bessel in $n$ and disjointness of the arc pieces leave the integral on $\mathfrak m^*$ of the product of the two joint cell-energy sums. The large-leg sum has supremum (2), while the small-leg sum has integrated energy $O_\rho(XL^2)$ by Parseval: each index has a unique small/giant prime factorization in its envelope, and both integer partitions are disjoint. The roles may be assigned in either order. Multiplying by the $O(L^6)$ level choices proves that the summed square of the maximal coefficient for the rank rectangle contribution is $O_\rho(X^{3-.38}L^{19})$. The coefficient on the entire $\mathfrak m^*$ needs only four axes, hence has a smaller log loss. Subtracting these two terms gives the same bound on the exact moving $\mathfrak m_N$ for all selected windows and cofactor sets simultaneously.

For target $N$ choose the exact cofactor bounds, excluding the $O(1)$ cofactors that divide $N$; since eligible primes are $\gg X^{.08}$, this is a fixed bounded number of interval holes, handled by the same dyadic expansions. Both exact physical intervals are subsets of the integer envelope, including their original endpoint atoms, so there is no grid or positivity bracketing. The only excluded giants are primes dividing $N$. There is at most one since they exceed $\sqrt{2X}$, and fixing it leaves $O_\rho(X^{.42})$ eligible small cofactor indices. Its removed factor has squared torus norm $O_\rho(X^{.42}L^2)$, so by Cauchy against the other true-prime factor it contributes $O_\rho(X^{.71}L^2)$ on the exact complementary arcs, uniformly in all hard intervals. The squared sum of these errors is $O_\rho(X^{2.42}L^4)$, smaller than $X^{3-.38}L^{19}$. Summing the two orientations and dividing by $X^3$ (equivalent to the normalization in (1) on this dyad) finishes the proof. This is a direct signed bound; it uses neither GRH, a replacement of the exact arc mask by the auxiliary one, nor any full-torus second-window substitution.
