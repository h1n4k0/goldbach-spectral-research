# The moving-cut near-balanced Vaughan Type II slab

Let $N=2^j$, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and

$$
 b_{\mathrm{II}}(v)=\sum_{r\mid v,\,r>N^{.2499}}\Lambda(r).
$$

Assume GRH **only for primitive nonprincipal Dirichlet characters of conductor at most $N^{.05}$** (for the particular $N$ in question). Then, uniformly for $N^{.49999}\le t\le N^{.50001}$ and $N/2\le y\le9N/16$, the following part of the actual signed central Vaughan Type II sum is

$$
 \left|\sum_{\substack{uv+dk=N,\ N/2<uv\le y,\ (uv,N)=1,\ k>t\\
             N^{.49}\le u,v\le N^{.51},\quad N^{.48}\le d\le X L^{10}}}
          \mu(u)\mu(d)b_{\mathrm{II}}(v)\mu^2(dk)\right|
          \ll N L_2^4/L=o(N).                         \tag{1}
$$

Arbitrary additional hard subintervals of the three stated ranges are allowed. All bounds are for sufficiently large $N$. This extends the [fixed R45 box](weak-s-type-ii-balanced-polylog-tags.md); it works directly with the genuine Vaughan weight, not a replacement by a medium-prime statistic. The complement outside the displayed slab, including $d>XL^{10}$ when $t$ is small enough to allow it, is not estimated. There is no claim on weak S. In particular, the upper restriction on $d$ is automatic for the relevant tuples if $t\ge X/L^{10}$; the other slab restrictions are still required.

## 1. Flatten the genuine cut, with one total weighted boundary bound

Write $n=uv,\ m_0=N-n$. For candidate tuples $d\mid m_0$ and $k=m_0/d$; because $N=2^j$, the exact unit condition means $u,v$ odd, hence so are $d,k$. The moving constraints on $v$ are $N/(2u)<v\le y/u$ and $v<(N-td)/u$, where the last inequality is strict. Partition $u,d$ independently into multiplicative intervals of ratio at most $1+\eta$, $\eta=L^{-100}$, with hard endpoints; freeze the denominators $u$ and the cutoff $d$ in these constraints at their respective cell left endpoints $u_0,d_0$. Thus on each cell there is just one hard $v$-interval $J$, possibly empty; do not replace a strict inequality by a weak one. Together with the $u$ and $d$ cells and their imposed hard interval masks, this gives $O(L^{202})$ disjoint rectangles $(I,J,D)$. Any surviving $J$ has scale $\asymp N/u_0$, so a bounded number of dyadic pieces suffice. Write the three scales as $U_0,V_0,D_0$, respectively, with $U_0V_0\asymp N$. Harmless fixed factors in these scale conventions will be absorbed below.

If a tuple changes, then $n\asymp N$ with $N-n\asymp N$, and at least one of

$$
       |n-N/2|,\qquad |n-y|,\qquad |n+td-N|
$$

is $O(\eta N)$. Indeed on either the original or frozen accepted side one has $td=O(N)$, so the $d$-freezing changes $td$ by $O(\eta N)$; the ratio $u/u_0=1+O(\eta)$ gives the other errors. Equality at any strict endpoint is included in these strips. For each fixed $d$, each strip has $O(1+\eta N/d)$ integers $n\equiv N\bmod d$. Thus the union of boundary $(d,n)$ has size $O(\eta N L+X L^{10})$, not this quantity per rectangle. As $|b_{\mathrm{II}}(v)|\le L$, the original weight at a fixed $(d,n)$ is at most $L\tau(n)$, and

$$
 \sum_{d,n:\ d\mid N-n,\ n\asymp N,\ N-n\asymp N}\tau(n)^2
    \le \sum_n\tau(n)^2\tau(N-n)\ll N L^9
$$

by Cauchy and the fourth and second divisor moments. Therefore the total weighted error is $O(N L^6\sqrt\eta+N^{3/4}L^{11})=O(NL^{-40})$ for large $N$. It suffices to bound the signed rectangular sums after this comparison. Their supports stay in fixed $n,N-n\asymp N$ ranges.

## 2. The extended dispersion estimate

Use the proof of [R45, §1](weak-s-type-ii-balanced-polylog-tags.md#1-a-centered-dispersion-bound-with-only-logarithmic-loss-in-the-diagonal-terms). In the notation there, it gives the same centered estimate

$$
       \Delta\ll N L^6\sqrt{Q/U}+N^{1-\delta}           \tag{2}
$$

on the enlarged range $MU\asymp N,\ N^{.48}\ll Q\le XL^{O(1)},\ U\le N^{.51+o(1)},\ Q/U=o(1)$. The long coefficient is $1$-bounded, odd squarefree and supported on $n>1$. The only conditional input to (2) is $\left|\sum_n\beta_n\chi(n)\right|\ll\sqrt U\,N^{.03}$ on nonprincipals induced from primitive $f\le N^{.05}$, for all $q\asymp Q$ of the smoothed variance including even ones.

Here are the numerical checks needed to reuse that proof. The large-conductor part of the exact zero energy has bound $O(U(1+U/(QN^{.05})))=O(U)$; the low part is $O(UN^{.11}/Q)=o(U)$. The large-gcd divisor-moment trimming still costs $O(MU L^{10}(1+U/(QN^\kappa)))$, since $mn\ne N$ for every odd $n>1$, and $mn\ll N$ on the smoothed supports. Use the same small-gcd neighboring tiles and Bettin–Chandee fallback: the actual nonzero phases only require $Q\ll U$, $H_f M/Q=N^\kappa$, and $N H_f/(UQ)=O(N^\kappa)$, where $H_f=(Q/M)N^\kappa,\ \kappa=10^{-5}$. When $H_f<1$, there are no retained nonzero frequencies and the smooth tail bound still applies. After multiplying by $MQ$, write $p=\log U/L,\ z_1=\log Q/L$. The two R45 trilinear squared exponents are $1+(15/8)p$ and $23/20+(9/5)p-(3/20)z_1$ before $30\kappa+\epsilon+o(1)$; at $p\le .51+o(1),\ z_1\ge .48+o(1)$ their maxima are $1.95625+o(1)$ and $1.996+o(1)$. The remaining nonzero exponents are bounded by $1+1.5p+2\kappa+\epsilon+o(1)$. All retain fixed power margin. This checks (2), including after the substitution $q=[d,c^2]$ with $c$ polylogarithmic.

All actual transferred long transforms satisfy the low-conductor bound in (2) under only the stated hypothesis. More explicitly, odd Möbius intervals, optionally with a polynomial finite coprime mask, use $1/L(s,\chi)$ and its finite inverse Euler factors. For squarefree $b$ weighted by the genuine $b_{\rm II}$ on squarefree integers, the base series is $L(s,\chi)/L(2s,\chi^2)$, marked by

$$
       \sum_{p>N^{.2499}}(\log p)\,
               \frac{\chi(p)p^{-s}}{1+\chi(p)p^{-s}};
$$

excluded/tag/odd primes are removed by inverse factors $1+\chi(p)p^{-s}$. If tags are excluded below, the band ends at $N^{.001}$, disjoint from the marked primes. It suffices to keep marked primes $p\le N$ in this identity: all interval endpoints are $\le N$. Apply hard Perron at height $N^4$ on $\Re s=.51$. For inducing primitive $f\le N^{.05}$, the [R42 shifted prime bound](weak-s-type-ii-medium-prime-opposite-tags.md#1-the-long-transform-with-the-exact-wide-euler-exclusion) $O(\sqrt Y\,L^3)$ for $\sum_{p\le Y}\chi(p)(\log p)p^{-i\tau}$ follows under GRH for that primitive character and extends to imprimitive $\chi$ by their polynomial-sized modulus Euler correction, including even moduli. It bounds each marked linear sum and the excluded prime Euler logarithm for primes $\ge L^{100000}$ by partial summation, since $L^5(L^{100000})^{-.01}=o(1)$. Higher terms converge absolutely; the factor at 2 is bounded and $1/L(2s,\chi^2)$ is bounded by its absolutely convergent series. The [R40 $L^{\pm1}$ bound](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums) is likewise individual for the same inducing primitive character; it and the shifted prime argument use GRH only for that character, with the remaining factors absolute. The imprimitive correction and any additional polynomial-sized product of coprime masks are at most $\exp(O(\sqrt L))$ on the contour, as there. Thus the hard interval transforms at scale $Y\le N$ are $O(\sqrt Y N^{.02})$ after the fixed shift and logarithmic factors. A single cell-prime transform is $O(\sqrt T L^2)$ for a cell at scale $T$, by subtracting endpoints in the ordinary GRH prime estimate. Products of these bounds give the claimed $\sqrt U N^{.03}$ in all the transfers below. Where principal densities occur, use the actual $\mu(d)$ and the unconditional [R43 reversal](weak-s-type-ii-doubly-untagged-signed-principal.md#1-signed-summation-of-the-principal-density); here $d/g\ge N^{.48-o(1)}$ and the smaller scale in the proof of its masked harmonic estimate is still $\ge N^{.2}$.

## 3. Direct rectangles, or transfer both sorts of tags

Set $B=L^{1000}$, $K_0=20000$. In a rectangle from §1 use the direct argument if $\max(U_0,V_0)\ge D_0 L^{K_0}$, and otherwise use tags. Throughout the proof, a squarefree completion at $c\le B$ with $c^2\mid N-uv$ changes the rectangle sum by $O(NL^{70}B^{-1/2})$ before summing rectangles. Indeed omitted bases affect $O(N/B)$ values of $N-uv$, per value the modulus divisors and omitted square sum cost $\tau(N-uv)^2$, and the factorizations cost $\tau(uv)$; use Hölder $4,4,2$ as in R45. The $L^{70}$ includes up to $O(L)$ later tag multiplicity in addition to $b_{\rm II}\le L$, and applies also after endpoint comparisons. This loss is enough for all rectangle sums, since there are only $O(L^{202})$. Fixed $c$, group squarefree $d$ by $g=(d,c)$, so $q=[d,c^2]=c^2d/g$ is injective in $d$ and odd, and the original divisibilities become $uv\equiv N\bmod q$. The exact principal densities after a transfer use the signed reversal in §2 on any dyadic subinterval of $q$, which gives a hard subinterval in $d$.

**Direct rectangles.** If $u$ is the larger scale, take it as the long odd squarefree Möbius variable and $v$, with $b_{\rm II}(v)/L$, as short. If $v$ is the larger scale write $v=a^2b$ uniquely with $b$ squarefree; discard $a>B$ and take long $b$, short $a^2u$. This last deletion is $O(NL^6 B^{-1/2})$ per rectangle: the number of pairs $(u,v)$ with $v$ admitting such a square is $O(N/B)$, and Cauchy with $\sum_{u,v}\tau(N-uv)^2\ll NL^9$ bounds their true modulus-divisor weight. For $a\le B$ one has $b_{\rm II}(v)=b_{\rm II}(b)$ exactly. Indeed any prime dividing $a$ has full prime-power part in $a^2 b$ at most $B^3<N^{.2499}$; primes outside $a$ have their original exponent in $b$. Thus the long squarefree transform is precisely the marked series in §2. The shifted variables always preserve $uv$ and hence the fixed numerator $N$. The long scale is at least $\max(U_0,V_0)/B^2$, so $Q/U\ll L^{4000-K_0}$. The direct $U$ is at most $N^{.51+o(1)}$.

**Tag rectangles.** If the direct criterion fails, the three dyadic scales satisfy

$$
 X L^{-K_0-12}\ll U_0,V_0\ll X L^{K_0+12},
       \qquad D_0\gg X L^{-K_0-2}.                    \tag{3}
$$

This uses $U_0V_0\asymp N$ and $D_0\le XL^{10}$. Perform the R45 first-cell transfers from the single full band $\mathcal P=[L^{100000},N^{.001}]\cap\mathbb P$, with relative cell ratio $1+\eta'$, $\eta'=L^{-2000}$. First isolate all $v$ with a tag, then among the exact $v$-untagged tuples isolate all $u$ with a tag. No earlier broad/narrow partition is used.

We detail the comparisons when a rectangle has many solutions for fixed $u,d$ or $v,d$, so uniqueness is not invoked. In a cell the excess of summing over the individual prime labels instead of first-cell occupancy is supported on integers with two distinct tags in that cell, and bounded by $O(L)$ per integer. The union of affected pairs $(u,v)$ over all cells in one rectangle has size $O(N(\eta'+L^{-100000})L_2)$, since $\sum_{s\in\mathcal P}1/s=O(L_2)$ and the reciprocal sum in any cell is $O(\eta'+L^{-100000})$ by counting all integers; count multiples of each $st$ below the upper endpoint at the tagged scale. Pairs sharing a tag between both variables, or with a repeated tag $s^2$ in the tagged variable, have respective union sizes $O(N L^{-100000})$, by $\sum_{s\ge L^{100000}}1/s^2$. The true modulus-divisor-weighted cost for any such pair set of size $H$ is $O(L^2\sqrt{H N L^9})$: $\sum_{u,v}\tau(N-uv)^2\ll NL^9$, by $uv$ and the fourth/second moments, and the factor $L^2$ includes the weight and label multiplicity. This same bound applies after enlarging the intervals by the tag cell ratio. When freezing the quotient interval at the tag cell left endpoint $T$, mismatch is supported on the tagged variable within $O(\eta' V_0+1)$, or $O(\eta' U_0+1)$, integers at its two endpoints. This affects $H\ll \eta' N+\max(U_0,V_0)$ pairs in the rectangle, independent of the number of tag cells. All comparisons are made before square completion, and their combined error is $O(NL^{-900})$ per rectangle. If a large square part $a>B$ is discarded in the second transfer, do so before label expansion using the same direct-rectangle bound above.

For the first transfer write $v=s\ell$. On the short coefficient put $b_{\rm II}(\ell)$, the exact earlier-cell mask and oddness, and freeze $\ell\in J/T$ in place of $J/s$. This weight replacement only differs from $b_{\rm II}(v)$ when $s^2\mid v$, since $s\le N^{.001}<N^{.2499}$; the preceding union bound applies and no $s$-dependent short mask is left. The long variable is $n=su$, weighted by the genuine $\mu(u)$ with $(s,u)=1$, hard $I$ support and oddness, summed over $s$ in the cell. Discarding $s\mid u$ cost the shared-tag union counted above. This is odd squarefree. Its transform is the product of the ordinary Möbius interval sum and the cell prime sum, plus a correction $\sum_s \chi(s)^2\sum_{\ell'\in I/s,(\ell',2s)=1}\mu(\ell')\chi(\ell')$, by $\mu(s\ell')=-\mu(\ell')$ on the coprime part; the first product has odd $u$. The first product and this correction separately satisfy the transform in §2 (the correction sums at most $O(T)$ primes and uses scale $U_0/T$). The short coefficient is arbitrary bounded after normalization. The scales satisfy $U\asymp TU_0$, $M\asymp V_0/T$, and the exact product is $uv$.

For the second transfer $v=a^2 b$ with $a\le B$ and squarefree $b$; the full tag exclusion passes exactly to $b$ since $a<B<L^{100000}$, as does $b_{\mathrm{II}}(v)$ by the $B^3$ observation above. Write $u=s\ell$, replace $\mu(s\ell)$ by $-\mu(\ell)$ with a discrepancy only at $s^2\mid u$, and freeze $\ell\in I/T$. Take short $m=a^2\ell$ with the earlier-cell mask, and long $n=sb$ with the full original $v$-interval on $b$, oddness and no tag on $b$. The exact product is $uv$ and $n$ is squarefree because $s\nmid b$. The transform factors into the cell prime sum and the genuine squarefree $b_{\rm II}$-weighted transform of §2. Here $U\asymp TV_0/a^2,\ M\asymp U_0 a^2/T$. In each transfer the actual bounded coefficient normalization costs $O(L^2)$ in total, because each long integer has at most $O(L)$ tag representations and $|b_{\rm II}|\le L$. By (3), both transfers have $U\le N^{.501+o(1)}$ and $Q/U\ll L^{K_0+24+4000-100000}$. None of the short masks is required to have character cancellation.

For direct and tag rectangles sum (2) with the actual signed $\mu(d)\mu(c)$ for the centered part, and use exact principal reversal for the rest. There are $O(L^{202})$ outer rectangles, $O(L)$ dyads of $q$, at most $B^3$ combined $a,c,g$ pieces, and $O(L^{2001})$ tag cells when used. Restoring normalization costs at most $O(L^2)$. The logarithmic loss in (2) is $L^6$. For direct rectangles the product of these factors without tag cells is $O(L^{3211})$, multiplied in its main term by $O(L^{(4000-K_0)/2})$; for tag rectangles it is $O(L^{5212})$, multiplied by $O(L^{(K_0+24+4000-100000)/2})$. These and the fixed power errors are $O(NL^{-10})$. The principal reversal costs $O(Ne^{-c\sqrt L})$ per piece before normalization, so reassembly is harmless. Square tails and all other deletion and endpoint errors above also beat $NL^{-10}$ after summing the outer rectangles. This covers every direct rectangle and all tagged sectors of the remaining rectangles.

## 4. Sum the remaining unsigned term by area, not by the number of rectangles

Now both variables avoid all primes in $\mathcal P$, and only tag rectangles remain. Apply the product of the two [R41 elementary upper sieves](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich) as in R45, §4. Their divisor levels remain $N^{.03}$ each. The one-variable prime product is $\asymp L_2/L$, still uniformly after deleting primes dividing $d$: those removed change its logarithm by $O(L/L^{100000})$. Ignore all squarefree conditions, keeping the original congruence and parity. For fixed $d,r_1,r_2$, a nonunit mask gives no tuples, and otherwise the [rectangular Weil count used in R42](weak-s-type-ii-medium-prime-opposite-tags.md#3-actual-double-untagged-unsigned-scale) has area main $|I||J|\varphi(d)/(4r_1r_2d^2)$. If an interval after dividing by the tag divisor is longer than $d$, split it into $O(1+|I|/d)$ or $O(1+|J|/d)$ periods, respectively; this gives the same main and an error $O_\epsilon(d^{1/2+\epsilon}L^{O(K_0)})$ by (3). Thus the total tuple count error is $O_\epsilon(N^{.81+\epsilon+o(1)})$ over all $d$, both sieve indices, and the polylogarithmic grid.

For the main term no grid-count loss is paid. At each fixed $d$ its original cell is unique, and the $I$'s for that $d$ partition the selected $u$-range (a dyadic $J$-split, if necessary, is disjoint). On tag rectangles $|J|\ll N/u_0$, and $\sum_I |I|/u_0\ll L_2$ by (3) and integration of $1/u$ over the polylogarithmic range of $u$; this includes intervals clipped at either end. Likewise $d\gg X L^{-K_0-2}$ and $d\le XL^{10}$ give $\sum_d 1/d\ll L_2$. Therefore the total ungated volume $\sum_{I,J,d}|I||J|/d$ on these rectangles is $O(NL_2^2)$. Multiplying by the two sieve densities gives $O(N L_2^4/L^2)$ actual potentially occupied tuples, plus the negligible power error. Multiplication by $b_{\rm II}\le L$ proves the remaining absolute bound $O(NL_2^4/L)$. Together with the slanted boundary comparison and the signed estimates above, this proves (1).
