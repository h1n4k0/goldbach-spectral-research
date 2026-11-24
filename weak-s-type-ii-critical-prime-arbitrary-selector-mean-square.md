# The dense critical shell for arbitrary target-dependent prime selectors

Let $Y$ be large, $L=\log Y$, and first restrict the even targets to $Y\le N\le1.01Y$. For each $N$, use the exact fixed proportional prime boxes, any independent hard prime subintervals, optional product gate and $N$-unit mask of [the critical-prime setup](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Allow every selector $|E_N(u,v)|\le1$, chosen separately for each target but fixed independently of the rational point. Its true prime weight is $-E_N(u,v)\log v$. The complementary polynomial has every original hard $I_d$, $d\ge\sqrt N$, $k>t\ge N^{.49999}$, $N-y\le dk<N/2$ with $N/2\le y\le9N/16$, exact $(dk,N)=1$, and weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. The hard cuts may vary arbitrarily with the target. One may also keep a fixed common product multiplier $\rho_m$, $|\rho_m|\le1$, on the complementary coefficients across the ambient target interval (in particular, use $\rho=1$ for the unmasked leg). No bound is claimed for arbitrary $N$-dependent complementary multiplier.

Use the exact signed $\mathcal I_N,\mathcal C_N$ on all critical primes $.8\sqrt N\le q\le.9\sqrt N$ and all $a\ne0$ there, with $|\beta|\le1/(10N)$. The latter pairing centers both numerator transforms separately as in the cited setup. The exact signed sums/integrals are taken before absolute values. Unconditionally,

$$
 \sum_{\substack{Y\le N\le1.01Y\\N\ {\rm even}}}
 \sup_{\substack{E_N,\ {\rm all\ the\ above}\\{\rm hard\ cuts}}}
 \left(|\mathcal I_N|^2+|\mathcal C_N|^2\right)
 \ll \frac{Y^3(1+\log L)^{14}}{L^{1/2}} .
 \tag{1}
$$

The bound extends to $[Y,2Y]$ by a fixed finite cover of such intervals. For every fixed $0<\nu<1/4$, both quantities are at most $Y/L^\nu$ outside $O_\nu(YL^{-1/2+2\nu}(1+\log L)^{14})$ targets, uniformly over all the indicated choices. This is a logarithmic almost-all result; it does not give pointwise cancellation at a prescribed target. Unlike [the earlier power-saving almost-all bound](weak-s-type-ii-critical-prime-signed-almost-all-boundaries.md), it does not assume that the first-leg selector is fixed across targets or separated.

## 1. Relative signed complementary energies

Temporarily omit the $N$-unit condition and confine $m=dk$ to any interval in $[.4Y,.6Y]$. Let $D_h$ keep the true signed coefficient at each $h\mid m$, and otherwise zero, for squarefree $h$. Then, uniformly for any fixed hard intervals on $d,k,m$ in the physical ranges,

$$
 \|D_h\|_2^2\ll 4^{\omega(h)}Y/h .
 \tag{2}
$$

We use ordinary $\mathbb R/\mathbb Z$ norms. Either omit the common multiplier or note that it contracts this squared norm. This follows from the same [signed hard-interval least-common-multiple quadratic bound](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy), namely

$$
 Q(J)=\sum_{a,b\in J}\frac{\mu(a)\mu(b)}{[a,b]}\ll1
 \tag{3}
$$

for every interval of positive integers $J$. We give the divisor dependence and the partition estimate below.

On actual support $m$ is squarefree, and the signed coefficient is $\mu(m)\sum_{k\mid m}\mu(k)$ with the genuine hard divisor cuts retained. Write $m=hv$ with $v$ squarefree and coprime to $h$. Every splitting has $k=rs$ with $r\mid h$, $s\mid v$. For each $r$ separate $s\le\sqrt v$ from $s>\sqrt v$. The first orientation uses short divisor $a=s$, $k=ra$, $d=hv/(ra)$; the second uses $a=v/s<\sqrt v$, $k=rv/a$, $d=ha/r$, with $\mu(s)=\mu(v)\mu(a)$. The signs outside the short-divisor sum have modulus one on true support. Cauchy–Schwarz over the two orientations and $r\mid h$ costs $2\cdot2^{\omega(h)}$ before summing their squared short-divisor sums. Only now may the squarefree, coprime and common product masks be dropped for the upper bound.

In the square expansion, for fixed short divisors $a,b=O(\sqrt{Y/h})$, common admissibility is one real interval for $v$ and divisibility by $[a,b]$. In the first orientation the $k$ tests are fixed and the $d$ tests give intervals in $v$; in the second the $d$ tests are fixed and the $k$ tests give intervals in $v$. The short-divisor tests add $v\ge a^2,b^2$ (strict in the second orientation). Counting multiples gives the length divided by $[a,b]$ with an absolute $O(1)$ error, including arbitrary endpoint conventions. The total error is $O(Y/h)$. The main term, after integrating over $v$, is $Q(J(v))$ with $J(v)$ a hard interval of short divisors, and is $O(Y/h)$ by (3). This proves (2).

We also need a sum of these energies over fixed partition levels. Partition the possible long and short variables into equal cells in $\log d$ and $\log k$ and pass to any dyadic coarsenings of these partitions. The total logarithmic ranges are $O(L)$ and the number of cells in each coordinate is bounded by a fixed power of $L$. Partition $m$ arbitrarily into consecutive hard intervals. Write $D_{h,\mathbf c}$ for the complementary coefficient polynomial belonging to a single triple $\mathbf c=(I_d',I_k',I_m')$ at these fixed levels, still before the $N$-unit mask. Uniformly for $h\le Y^{.01}$,

$$
 \sum_{\mathbf c}\|D_{h,\mathbf c}\|_2^2
 \ll 4^{\omega(h)}(Y/h)L^{3/2}.
 \tag{4}
$$

The $m$-cell partition can be summed away at once in this squared norm, since it cuts disjoint integer coefficients for each fixed $d,k$ cell. Then use the same genuine short-divisor expansion above, for each $r$ and orientation. At a fixed real $v$, the short-divisor intervals $J(v)$ corresponding to different pairs of cells are disjoint. The ones with integer endpoints $A_0\le B_0$ and width $H=B_0-A_0\le A_0/\sqrt L$ have

$$
 Q(J)\ll \sum_{a\in J}\frac1a+\frac{H^2}{A_0^2}(1+\log(2H)).
 \tag{5}
$$

For $H=0$ the second term is zero. For distinct $a,b$ their gcd is $\le H$; expand $(a,b)=\sum_{\ell\mid(a,b)}\varphi(\ell)$ and use at most $O(H/\ell)$ multiples of $\ell$ in the interval for $\ell\le H$, proving (5). For these short cells, $H/A_0\ll\sum_{a\in J}1/a$, so summing (5) over the disjoint $J$ gives $O(L^{3/2})$. Each of the other intervals has harmonic sum $\gg1/\sqrt L$, so there are at most $O(L^{3/2})$, since $a\ll\sqrt Y$. Bound each by (3). This proves the integrated main term bound in (4).

For the accumulated floor errors, in the direct orientation $k=ra$ fixes at most one $k$-cell for each $a$; only the $d$-cell can change as $v$ varies. If there are $G$ cells in that coordinate with logarithmic width $\Delta\ll L/G$, the requirement that both $a,b$ use the same varying cell forces $|\log(a/b)|\le\Delta$. There are $O((Y/h)\min(1,\Delta)+\sqrt{Y/h})$ such ordered pairs. Each occurs in at most $G$ such cell counts. The error is therefore $O((Y/h)L+G\sqrt{Y/h})=O((Y/h)L)$, since $G$ is polylogarithmic and $h\le Y^{.01}$. In the complemented orientation $d=ha/r$ fixes that cell and the identical argument uses the varying $k$-cell. The multiplier cost from Cauchy over orientations and allocations and then summing them is $O(4^{\omega(h)})$. This proves (4); floor errors were controlled for the actual cell geometry, not assumed orthogonal across divisor choices.

## 2. Exact large-prime part of the target unit mask

Take $Z=L^4$, and put $H_N=\prod_{p\le Z,\ p\mid N}p$. Use (2) at $h=p$ and a union bound on the coefficient square. Restoring the true unit condition from the low-prime unit mask $(m,H_N)=1$ changes the ordinary squared complementary norm by at most $O(Y\sum_{p\mid N,p>Z}1/p)$, where “changes” here means the squared norm of the difference. This is uniform in the true hard cuts. The ordinary prime energy is $O(Y)$, by prime counts and uniqueness of products between the two disjoint ambient boxes. Cauchy on the disjoint arcs thus gives an error in the squared pairing, summed over targets and maximized over allowable choices, of

$$
 \ll Y^2\sum_{Y\le N\le1.01Y}\sum_{\substack{p\mid N\\p>Z}}\frac1p
 \ll Y^3\sum_{p>Z}\frac1{p^2}
 \ll Y^3/Z.
 \tag{6}
$$

All target residue classes remain exact; the divisor moments only bound the losses.

We may discard the targets $H_N>Y^{.01}$ for a negligible squared total. Indeed at $\theta=1/\log Z$, the positive divisor expansion and $\lfloor 2Y/h\rfloor\le 2Y/h$ bound their number by

$$
 2Y\,e^{-.01L/\log Z}\prod_{p\le Z}
 \left(1+\frac{p^\theta-1}{p}\right)
 \ll Y\,e^{-.01L/\log Z}(1+\log Z)^{e-1}.
$$

Here the $e$ in the exponent is Euler's number. This follows since $p^\theta\le e$, and by the prime harmonic estimate. The uniform ordinary squared energies $O(Y)$ on both true legs, hence pairing squared $O(Y^2)$, cover these rare $N$. For all other targets the low-prime unit mask is exactly $\sum_{h\mid H_N,\ h\mid m}\mu(h)$, with all $h\le Y^{.01}$.

## 3. Common coarse cells and their boundary errors

Take a power of two $M\asymp L^{12}$. For each of the $d,k$ coordinates use $M$ equal logarithmic cells in fixed common ranges $[\sqrt Y,Y^{.50002}]$ and $[Y^{.49998},.6\sqrt Y]$ respectively. These contain all possible original $d,k$ for the given dyad, by $m<N/2$ and $k>t\ge N^{.49999}$. For $m$ use $M$ equal linear cells in $[.4Y,.6Y]$. Take half-open partitions, making the final endpoint convention consistent; a coordinate cut need not align with any cell. Approximate each of the three true hard coordinate intervals from inside by consecutive complete cells. The original sum minus this approximation can be telescoped in the three coordinates into a sum of a bounded number of strips (with exact original unit and product masks). If a hard interval lies in one cell, it is itself a strip.

For a discarded $d$ or $k$ strip its logarithmic width is $O(L/M)$. Use the original direct short divisor $k<X_N/2\ll\sqrt Y$ for the signed square, where $X_N=\sqrt N$. For each real $m$, the short divisor interval $J(m)$ has relative width $O(L/M)$ and lower endpoint at least $Y^{.49999}$ if nonempty. Its main term (5) is $O(L/M+Y^{-.49999}+(L/M)^2L)$. The floor error pairs must have $|\log(k/k')|\ll L/M$, so the total floor cost is $O(YL/M+\sqrt Y)$. Thus these strips have ordinary squared energy $O(YL/M)$ for large $Y$. This argument uses the actual signs, and not monotonicity of the squared norm under dropping divisor terms.

For a discarded $m$ strip, the interval length is $O(Y/M)$. On the true squarefree support $|D_m|^2\le \tau(m)^2=\tau_4(m)$, where $\tau_4$ is the four-fold divisor function. For an interval of length $U$ at scale $Y$,

$$
 \sum_{m\ {\rm in\ interval}}\tau_4(m)\ll U L^3+Y^{3/4}L^2.
$$

To see this, choose the largest of the four factors (at most four choices), so the product of the other three is $O(Y^{3/4})$; count the remaining factor by $U$ divided by that product plus one, and sum over the triples. This gives squared energy $O(YL^3/M)$ for such strips. Consequently the total squared pairing error over all targets from rounding the physical cuts is $O(Y^3 L^3/M)$ by ordinary Cauchy. These bounds may be applied after keeping the low-prime unit mask: it remains only a product restriction.

For the arc coordinates use $M$ equal real $q$-cells in the ambient interval $[.8\sqrt Y,.9\sqrt{1.01Y}]$, and $M$ equal $\beta$-cells in $[-1/(10Y),1/(10Y)]$. Every cell contains all nonzero numerators for its prime denominators. All ambient arcs are disjoint since distinct reduced centers are separated by $\gg1/Y$ (indeed $1/(qq')$ is greater than the combined radius), and cell interiors are disjoint. Round each exact arc coordinate interval inward to the union of complete cells. Omitted arcs lie in the wall cells of $q=.8\sqrt N,.9\sqrt N$ or $\beta=\pm1/(10N)$. For any one wall and any one grid cell, the targets for which the wall lies in that cell belong to an interval of length $O(Y/M)$ by the respective derivative bounds on this dyad. Among $h\mid N$ their number is $O(Y/(Mh)+1)=O(Y/(Mh))$ for $h\le Y^{.01}$. A wall lying exactly on a grid endpoint may be included in either adjacent wall cell for this error bound.

Fix such an $h$. For each omitted arc strip $T$ and target, ordinary Cauchy bounds the squared pairing contribution by $O(Y)\|\mathbf1_TD_{h,\mathbf R}\|_2^2$, where $\mathbf R$ is its (target-dependent) rectangle of complete physical cells. Decompose any such three-coordinate rectangle into $O((1+\log M)^3)$ canonical dyadic cell triples, and Cauchy–Schwarz across that decomposition. Sum the resulting bounds over all levels and all cells, retaining the strip factor. For each wall, the strips at that coordinate are disjoint, and the target multiplicity just established is $O(Y/(Mh))$. Thus, using (4), the squared sum of these errors for fixed $h$, even after maximizing all choices, is

$$
 \ll \frac{Y^2}{Mh}(1+\log M)^6\,
        4^{\omega(h)}(Y/h)L^{3/2}.
 \tag{7}
$$

The six logs account for Cauchy over the decomposition and for the number of level triples. This handles arbitrary moving physical cuts without substituting a fixed polynomial in the arc-wall estimate.

## 4. Dense signed maximal Bessel and prime-product multiplicity

For fixed $h\le Y^{.01}$, now consider the main rounded pairing, before multiplying by $\mu(h)$. It uses only targets with $h\mid N$. For each fixed complete rectangle of physical and arc cells $\mathbf R$, let $G_{h,\mathbf R}(\alpha)$ be the corresponding true rounded complementary polynomial multiplied by its arc indicator. By summing the absolute-square Fourier coefficients over integer frequencies after a five-coordinate canonical dyadic decomposition, one has

$$
 \sum_{b\in\mathbb Z}\ \sup_{\mathbf R}
          |\widehat G_{h,\mathbf R}(b)|^2
 \ll (1+\log M)^{10}\,4^{\omega(h)}(Y/h)L^{3/2}.
 \tag{8}
$$

Here Fourier coefficients use $\widehat G(b)=\int_0^1G(\alpha)e(-b\alpha)\,d\alpha$. Indeed each rectangle is a union of $O((1+\log M)^5)$ canonical cells and Cauchy pays that factor. Sum over all cell choices at all five levels. At each fixed set of levels, Plancherel and disjointness of the two arc-coordinate cells leave the sum of the ordinary coefficient-cell energies, bounded by (4). The remaining number of level choices contributes the second factor $(1+\log M)^5$. No complementary choices depend on Fourier frequency inside a single cell.

The two ambient prime intervals are disjoint and of lengths $O(\sqrt Y)$. Each possible product $n=uv$ is uniquely represented, has weight bounded by $O(L)$, and there are $O(Y/L^2)$ different possible products. At a given $N$, Cauchy over these products gives the squared pairing bound

$$
 \ll Y\sum_{n\ {\rm ambient\ products}}
               |\widehat G_{h,\mathbf R}(N-n)|^2 .
$$

It is uniform in every $E_N$, in its hard prime cuts and in its actual $N$-unit mask. Now sum over $N$ divisible by $h$ and put $b=N-n$. All prime factors in the ambient prime boxes exceed $h$, so the multiplicity of any fixed $b$ is at most $O(Y/(\varphi(h)L^2))$: for each ambient prime $u$, require $v\equiv-b\bar u\bmod h$. There are no pairs for a nonunit class. For a unit class apply [Montgomery–Vaughan, Theorem 2, equation (1.10)](https://backend.production.deepblue-documents.lib.umich.edu/server/api/core/bitstreams/5adbb05b-05d0-4779-b1fd-304ec1ec257a/content#page=3) on an ambient interval of length $\asymp\sqrt Y$ containing the $v$ support, where $h\le Y^{.01}$ gives $\log(\sqrt Y/h)\gg L$. Sum over $O(\sqrt Y/L)$ primes $u$. The case $h=1$ is the elementary prime count. This multiplicity estimate also permits dropping the $N$ gate temporarily inside the nonnegative upper bound.

Combining with (8), the squared sum for this piece is

$$
 \ll \frac{Y^3 L^{3/2}}{L^2}(1+\log M)^{10}
               \frac{4^{\omega(h)}}{h\varphi(h)} .
$$

Use the exact inclusion-exclusion from §2 and Minkowski on these squared sums after taking square roots (the same inequalities bound the suprema). For all squarefree $h$ with primes $\le Z$,

$$
 \sum_h\frac{2^{\omega(h)}}{\sqrt{h\varphi(h)}}
  =\prod_{p\le Z}\left(1+\frac2{\sqrt{p(p-1)}}\right)
  \ll (1+\log Z)^2.
$$

The finite product estimate follows from the prime harmonic estimate and $1/\sqrt{p(p-1)}=1/p+O(p^{-2})$. Truncating to $h\le Y^{.01}$ only decreases this positive sum. Likewise summing the square roots of (7) uses $\sum_h2^{\omega(h)}/h\ll(1+\log Z)^2$. Both resulting errors, the physical rounding error and (6) are smaller than the bound in (1) with $M\asymp L^{12},Z=L^4$. This proves the full signed assertion.

Finally, [the exact full-vs-centered comparison](weak-s-type-ii-critical-prime-global-shift-rows.md) gives $|\mathcal I_N-\mathcal C_N|\ll N/(\log N)^{3/2}$ uniformly for the genuine unrounded arbitrary hard cuts, actual $N$-units and the common multiplier. Its squared sum is smaller than (1), proving the centered assertion. No individual modulus, numerator or alias has been removed in the claimed result.
