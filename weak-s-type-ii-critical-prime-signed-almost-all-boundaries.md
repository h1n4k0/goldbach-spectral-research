# Signed critical-shell bounds for almost all even targets, with the true three boundary bands

Use the actual prime boxes and full complementary polynomial of the [critical-prime shell](weak-s-type-ii-critical-prime-double-centered.md). For each even $N$, the prime factors $u,v$ lie in arbitrary hard subintervals of $[.740\sqrt N,.745\sqrt N]$ and $[.715\sqrt N,.720\sqrt N]$, with $N/2<uv\le y\le9N/16$, $(uv,N)=1$, and weight $-\log v$. The selector is the unselected true box $E=1$. The proof also allows a fixed bounded separated multiplier $E(u,v)=E_1(u)E_2(v)$, with each function independent of the target and cutoff choices; it does not cover an arbitrary target-dependent selector.

The complementary leg has its original arbitrary hard $I_d$, $I_0=I_d\cap[\sqrt N,\infty)$, strict $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. Either use the full complementary polynomial, or use its exact three surviving signed terms for $P^-(m)\le Z$ from the [least-prime reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). The latter includes the [polylogarithmic choice $Z=(\log N)^A$](weak-s-type-ii-critical-prime-polylog-boundary-width.md) for every fixed $A>0$; here even the least-prime cutoff $Z$ may vary arbitrarily with the target. An individual boundary type is also allowed.

Let $\mathcal I_N$ and $\mathcal C_N$ denote the full and separately double-centered signed pairings with outside phase $e(-N\alpha)$, where $e(z)=e^{2\pi iz}$. They are over all $q$ prime in $[.8\sqrt N,.9\sqrt N]$, $a=1,\ldots,q-1$, and $\alpha=a/q+\beta$ with $|\beta|\le1/(10N)$. The double-centering means subtraction of the separate $a\ne0$ averages of the two true transforms at each $q,\beta$. The theorem is unconditional. For $Y\le N\le2Y$, $N$ even, and any fixed $\epsilon>0$,

$$
\sum_N\sup_{\text{permitted hard cuts}}
 (|\mathcal I_N|^2+|\mathcal C_N|^2)
\ll_\epsilon
\begin{cases}
Y^{5/2+\epsilon},&y=9N/16,\\
Y^{11/4+\epsilon},&N/2\le y\le9N/16\text{ also in the supremum}.
\end{cases}
\tag{1}
$$

In the first line the prime product gate is automatic. Consequently, in that line, both signed shell quantities are at most $N^{1-\delta}$, uniformly over all the indicated cuts, outside $O_\epsilon(Y^{1/2+2\delta+\epsilon})$ even targets in the dyad for any fixed $0<\delta<1/4$. In the second line the exception bound is $O_\epsilon(Y^{3/4+2\delta+\epsilon})$ for $0<\delta<1/8$. These estimates concern the actual signed sum over the dense shell, not unsigned mass, a selected set of aliases, or a pointwise estimate at an exceptional target.

## 1. Ambient arcs and harmless prime-unit terms

Fix $Y$. Use the ambient torus arcs with $q$ prime in $[.8\sqrt Y,.9\sqrt{2Y}]$, all $a\ne0$, and $|\beta|\le1/(10Y)$. They are disjoint, since the combined radii are at most $1/(5Y)$, below $1/(qq')$ for distinct reduced centers. Every actual shell is a subset obtained by restricting the $q$ and $\beta$ intervals, always keeping all nonzero numerators at each remaining $q,\beta$. For a polynomial $F$, on an ambient arc we can therefore define the fixed linear operation

$$
F^*(a/q+\beta)=F(a/q+\beta)
 -\frac1{q-1}\sum_{a'=1}^{q-1}F(a'/q+\beta).
\tag{2}
$$

It contracts $L^2$ on any $q,\beta$ subregion including all $a\ne0$. It is independent of $N$ once $F$ is fixed. We use it on the polynomial cells below, not as a target-dependent approximation.

Temporarily ignore $(uv,N)=1$ on the prime side. Only $O(1)$ primes in either ambient prime interval can divide any one $N$, since these primes are $\gg\sqrt Y$. The offending products have $O(\sqrt Y)$ representations, with bounded multiplicity by unique factorization, and weights $O(\log Y)$. Their polynomial has ordinary squared energy $O(\sqrt Y(\log Y)^2)$. Each true complementary polynomial has squared energy $O_\epsilon(Y^{1+\epsilon})$ even by the crude coefficient bound $\tau(m)$. Thus the prime-unit error for either pairing is $O_\epsilon(Y^{3/4+\epsilon})$ by Cauchy–Schwarz, also after (2). Its squared sum over $N$ fits the first line of (1), after reducing the auxiliary $\epsilon$ as needed. The prime-unit requirement is restored at the end. The complementary $N$-unit condition will be kept exactly.

## 2. Moving windows as shared finite cells

Use standard binary partitions of each relevant ambient integer coordinate, padding its range to a power of two. All these coordinate ranges have polynomial size in $Y$, so a hard interval is a union of $O(\log Y)$ disjoint dyadic cells and there are $O(\log Y)$ levels. A different interval may be chosen at every $N$. Within each fixed tuple of levels the cells are disjoint and partition the common coordinate universe.

For $P$, the two coordinates are $u,v$. In the second line of (1) add the coordinate $uv$ to impose the exact active product gate. The ambient prime variables are $O(\sqrt Y)$, restricting each to the corresponding union of its possible true boxes, and $uv=O(Y)$. The base weights and the two primality masks do not vary with $N$.

For the full complementary polynomial the coordinates are $d,k,m=dk$. Use its fixed sign weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$, and temporarily leave the mask $(m,N)=1$ to the divisor expansion below. To represent an exact boundary polynomial, impose the fixed structural condition $p=P^-(m)\mid d$ for type 1, or $p\mid k$ for types 2 and 3, and use the additional coordinate $p$ for the moving cutoff. The other coordinates for the exact type tests are as follows.
- Type 1 adds $d/p$, whose failed membership $d/p\notin I_0$ is exactly the original lower-endpoint failure, because $d\in I_0$ and $d/p<d$.
- Type 2 adds $pd$, whose failed membership $pd\notin I_0$ is exactly the original upper-endpoint failure, because $d\in I_0$ and $pd>d$.
- Type 3 adds $pd,k/p$, with $pd\in I_0$, $k/p\le t$.
All conditions are hard intervals in their displayed coordinates. Strictness and inclusion at a coincident endpoint are retained on the integer coordinate; empty cases contribute zero. The coordinates such as $d/p,k/p$ are integers precisely in their stated structural types. The ambient bounds $m\ll Y$, $d,k,p\ll Y$ suffice, with $pd\ll Y^2$. Each type uses its own cell universe, and the finite sum of types is harmless. No replacement of a signed boundary by its containing band is made.

For the complementary $N$-unit mask use the exact identity

$$
\mathbf1_{(m,N)=1}=\sum_{\substack{h\mid N\\h\mid m}}\mu(h).
\tag{3}
$$

For each fixed $h$ the condition $h\mid m$ is included in the common complementary cell polynomial; the expansion for a particular $N$ chooses $h\mid N$. This does not modify any other sign or mask.

For arc selection use a dyadic tree for the integer $q$. Partition $[-1/(10Y),1/(10Y)]$ by equal cells on a binary grid of mesh at most $Y^{-6}$, using $O(\log Y)$ levels. Round the two true $\beta$ endpoints inwards to the grid. The resulting interval has a dyadic decomposition of length $O(\log Y)$. An arc cell consists of its chosen $q$ and $\beta$ cells and every $a\ne0$ on those arcs. At fixed levels these arc sets are disjoint. The rounding error is negligible uniformly: there are $O(Y)$ ambient centers, the omitted length at each is $O(Y^{-6})$, and the crude supremum of each true polynomial is $O_\epsilon(Y^{1+\epsilon})$, also after (2). The resulting pairing error is $O_\epsilon(Y^{-3+2\epsilon})$. In particular the theorem concerns the original exact $\beta$ endpoints.

## 3. Pointwise square sum for prime cells

Throughout an ambient arc, the complete matrix with entries $e(aij/q)$, $i,j\bmod q$, has $\ell^2$ operator norm $\sqrt q$. The multiplication by $e(\beta uv)$ can be separated by its Taylor series in $(u/\sqrt Y)^j(v/\sqrt Y)^j$, because $|\beta|Y\le1/10$ and both normalized variables are bounded by fixed constants. Sum the resulting absolute coefficient norms (including the fixed bounds for the two monomials) to get $O(1)$. Each residue contains only $O(1)$ integers in either prime variable's ambient support, so the same bilinear norm, up to an absolute factor, applies to vectors supported on arbitrary subsets of the two integer intervals.

For fixed levels of the $u,v$ cells, let $P_{U,V}$ be the common prime polynomials before the $N$-unit mask. The matrix inequality gives

$$
\sum_{U,V}|P_{U,V}(a/q+\beta)|^2
\ll q\left(\sum_u1\right)\left(\sum_v(\log v)^2\right)
\ll Y^{3/2}(\log Y)^2.
\tag{4}
$$

The last estimate only needs the crude integer counts $O(\sqrt Y)$. The same square sum is bounded by a constant times (4) for the centered cells, by Jensen over $a\ne0$ in (2) and uniformity of (4).

For the active gate, include one fixed dyadic level of the $uv$ coordinate, with cell length $H$. Each integer $uv$ has at most two ordered prime representations across the ambient supports, even if those two ambient intervals overlap. Thus the raw number of prime pairs in any $U,V,J$ cell is $O(H)$ and their total over all cells is $O(Y)$. It follows that the summed squared polynomial values are $O(YH(\log Y)^2)$.

For the other bound first fix one product cell $J$. In each $U,V$ tile, for each $u$ the allowed integer $v\in V$ with $uv\in J$ form an interval. Decompose it into canonical dyadic blocks $W$. At a fixed internal level there are at most two selected blocks per $u$; let $U_W$ be the set of rows selecting $W$. The contribution at that level is a sum over $W$ of the rectangular bilinear forms on $U_W,W$. Cauchy–Schwarz over blocks and the complete matrix bound give

$$
\ll \sqrt q
 \left(\sum_W\sum_{u\in U_W}1\right)^{1/2}
 \left(\sum_W\sum_{v\in W}(\log v)^2\right)^{1/2}
\ll\sqrt q\,(\#U)^{1/2}
             \left(\sum_{v\in V}(\log v)^2\right)^{1/2},
$$

where prime weights are used and the $O(1)$ residue multiplicity and $\beta$ Taylor series are included. There are $O(\log Y)$ internal levels. Sum the resulting squares over $U,V$, and over $O(Y/H)$ product cells. This gives $O(Y^{5/2}H^{-1}(\log Y)^4)$. Combining the two bounds, for every fixed tuple of levels we obtain

$$
\sup_{\alpha\ {\rm on\ ambient\ arcs}}\ \sum_{U,V,J}|P_{U,V,J}(\alpha)|^2
\ll Y^{7/4}(\log Y)^4.
\tag{5}
$$

Indeed $\min(YH,Y^{5/2}/H)\le Y^{7/4}$. Jensen again gives the same order for the centered cells. The argument does not use factorization of an arbitrary nonseparable pair selector.

## 4. Complementary square sums and Bessel over the original targets

For fixed levels of all complementary coordinates, write $D_{B,h}$ for the corresponding common cell polynomials with $h\mid m$ as in (3), for one specified type or for the full complementary polynomial. For each $m$, the cells partition the actual available tuples $(d,k)$; their absolute weights sum to at most $\tau(m)$. Thus the sum over cells of the squares of the coefficients at $m$ is at most $\tau(m)^2$, even before using Möbius cancellation. Summing over $h\mid m$ gives, by ordinary Parseval,

$$
\sum_{B,h}\int_0^1|D_{B,h}(\alpha)|^2d\alpha
 \le\sum_{m\ll Y}\tau(m)^3\ll_\epsilon Y^{1+\epsilon}.
\tag{6}
$$

The final bound follows from the elementary divisor bound with an arbitrarily small positive exponent. It is also an upper bound on the integrated squared sum after restriction to ambient arcs and after (2).

For each target and any hard cuts, the rounded pairing is the sum of at most $(\log Y)^{O(1)}\tau(N)$ terms, each with multiplier $\mu(h)$, of the form

$$
\int_{\mathbb T}\mathbf1_\Omega(\alpha)\,
    P_A^{\dagger}(\alpha)D_{B,h}^{\dagger}(\alpha)e(-N\alpha)\,d\alpha.
\tag{7}
$$

Here $A,B,\Omega$ are fixed prime, complementary and arc cells; both daggers mean either the identity or the common centering (2). The chosen cells and $h$ may depend on the target, but the function inside (7) before $e(-N\alpha)$ does not. Cauchy–Schwarz and $\tau(N)\ll_\epsilon Y^\epsilon$ bound the square of the sum by $Y^\epsilon(\log Y)^{O(1)}$ times the sum of squared (7) over all possibly selected cells and $h$. This inequality holds for every cut, so also for its supremum. Sum over the actual even $N$ and apply Bessel on all integer $N$ separately for each fixed cell and $h$; the restriction $h\mid N$ may now be dropped because all these summands are nonnegative. The resulting sum, for fixed tuples of all levels, is at most

$$
\begin{split}
\sum_{A,B,h,\Omega}\int_\Omega |P_A^\dagger(\alpha)D_{B,h}^\dagger(\alpha)|^2\,d\alpha
&\le \left(\sup_{\alpha\ {\rm on\ ambient\ arcs}}\sum_A|P_A^\dagger(\alpha)|^2\right)
  \sum_{B,h}\int_{\rm ambient\ arcs}|D_{B,h}^\dagger(\alpha)|^2d\alpha .
\end{split}
$$

This uses the disjointness of the arc cells at fixed levels. Equations (4) or (5), and (6), bound it by $Y^{5/2+\epsilon}$ or $Y^{11/4+\epsilon}$ times powers of $\log Y$. Summing the finitely many tuples of levels costs only another power of $\log Y$; choose all initial auxiliary divisor exponents sufficiently small in terms of the final $\epsilon$. Restore the prime-unit and rounding errors from §§1–2, and add the at-most-three boundary polynomials if requested. This proves (1). The exception counts follow immediately by summing the squared lower threshold on the exceptional targets.

The argument uses signed orthogonality of the target phase with genuinely common polynomials across targets. It retains the exact coefficient signs and the entire critical shell. It gives no bound for every sufficiently large even $N$, for other unestimated arc ranges, the full Type II operator, or weak S.
