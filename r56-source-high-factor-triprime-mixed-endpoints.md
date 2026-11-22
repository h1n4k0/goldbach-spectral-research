# One-high and two-high nonadmissible triprimes against the two established partners

Fix $0<\rho<1/2$ and $I_0(N)=[\rho N,(1-\rho)N]$. Let $I\subseteq I_0(N)$ be any hard interval. For sufficiently large even $N$ use exactly

$$
 j_N=\frac{\log N}{\log\log N},\qquad
 D=\lfloor\sqrt N e^{-20j_N}\rfloor,\qquad Q=\lfloor N e^{-20j_N}\rfloor .
$$

On the central sum line $n+m=N$ retain only physical integers that are units modulo $N$. Every prime of a leg below is required to exceed $\log N$ unless it is a high prime $>D$, which exceeds that bound automatically. Retain the two established partners: type 2 is the [R53](r53-source-retuned-exact-local-comparator.md) retuned semiprime $n=up$ with $\log N<u\le D<p$, of positive mark $\log u$; type 3 is the [R55](r55-source-all-small-triprime-comparator.md) squarefree triprime with all three primes $\le D$, of positive mark $\log n$.

Define two new squarefree triprime types:
* Type $H_1$: exactly one high prime. Write $n=qap$ with two distinct low primes $q,a\le D$, one high prime $p>D$, and impose the exact extra gate $qa>D$. The positive mark is $\log p$.
* Type $H_2$: exactly two high primes. Write $n=qrp$ with the low prime $q\le D$ and two distinct high primes $r,p>D$. The positive mark is $\log q$.

The two old types and the two new types are disjoint as arithmetic selections. For $(i,j)$ with one type in $\{H_1,H_2\}$ and the other in $\{2,3\}$, let $C_{ij,N}(I)$ be the true full sum-line count $n\in I,\ m\in I_0(N)$, with the product of their stated positive marks. Both orientations are included separately.

**Divisor labels and signs.** On the central interval a high prime $p$ is admissible precisely if $n/p\le D$: this condition implies $pD\ge n\ge\rho N>Q$, so the other admissibility check is automatic. Thus $H_1,H_2$ are exactly the nonadmissible squarefree zero-small triprimes with at least one high prime. Three high primes are impossible because $D^3>N$ eventually. In $H_1$ every pair of primes is long: the low pair satisfies the imposed gate $qa>D$, and the other two pairs contain $p>D$. In $H_2$ every pair contains a high prime. The three pair-divisor terms together give $+\log n$, and each high prime $v$ contributes the single-divisor term $-\log(n/v)$. The divisor $n$ has zero mark. The true long marks are consequently $+\log p$ on $H_1$ and $-\log q$ on $H_2$. On types 2 and 3 the true long marks remain $-\log u$ and $+\log n$, respectively. Every nonzero long divisor on a type 2 or 3 partner is at least $\rho N/D$, while every long divisor on the new leg is $>D$. Hence the **original** product cutoff on the pair is automatic, since their product exceeds $\rho N>Q$. The only nonzero alias is $n+m=N$, with the negative sum-alias sign; the central equal pair is nonunit. The exact signed arithmetic marks therefore give $+C_{H_1,2}$, $-C_{H_1,3}$, $-C_{H_2,2}$ and $+C_{H_2,3}$, and the corresponding reflections. No pairing of two new legs is included: in that case the original curved cutoff still needs a separate analysis.

For each leg use a squarefree outer cofactor $u$ and the following real profiles on $t\in I_0(N)$, all with the actual cofactor units:
* For types 2 and 3, use the sets and weights $w_{i,u}(t)$ of [R55](r55-source-all-small-triprime-comparator.md) (for type 2, equivalently [R53](r53-source-retuned-exact-local-comparator.md)).
* For $H_1$, $u=qa$ is an unordered product of two distinct low primes in $(\log N,D]$, with $D<u\le N/D$. Set $w_{H_1,u}(t)=u^{-1}\mathbf1_{t/u>D}$. The factor $\log p$ is precisely canceled by the last-prime density denominator.
* For $H_2$, $u=qr$ with one low $q\in(\log N,D]$ and one high $r>D$, $u\le N/D$. Set $w_{H_2,u}(t)=(\log q)(2u\log(t/u))^{-1}\mathbf1_{t/u>D}$. The factor $1/2$ is for the two choices of the last high prime.

Write $\mathcal U_i(N)$ for these outer cofactor sets, and $\lambda_\ell=(\ell-1)/(\ell-2)$ at an odd prime $\ell$. Define the exact local model by

$$
 M_{ij,N}(I)=\mathfrak S(N)
   \sum_{\substack{u\in\mathcal U_i(N),\ v\in\mathcal U_j(N)\\(u,v)=1}}
      \left(\prod_{\ell\mid uv}\lambda_\ell\right)
         \int_I w_{i,u}(t)w_{j,v}(N-t)\,dt .                  \tag{1}
$$

Here $\mathfrak S(N)$ is the ordinary even binary singular series.

**Theorem (unconditional).** For every fixed $A,b>0$, with $L=\log X$, outside $O_{\rho,A,b}(XL^{-b})$ even $N\in[X,2X]$, simultaneously for every hard $I$ and all the stated type pairs,

$$
     C_{ij,N}(I)-M_{ij,N}(I)
        =O_{\rho,A,b}\big(\mathfrak S(N)N L^{-A}\big).        \tag{2}
$$

For $\theta=20/\log\log N$, $c_2=\log2$, and $c_3=\pi^2/12$, uniformly in $I$ the respective deterministic main terms are

$$
 \begin{split}
 M_{H_1,j,N}(I),\,M_{j,H_1,N}(I)
   &=\mathfrak S(N)|I|\,(4c_j+o_\rho(1))\,
                         \theta\log(1/\theta),\\
 M_{H_2,j,N}(I),\,M_{j,H_2,N}(I)
   &=\mathfrak S(N)|I|\,(4c_j+o_\rho(1))\,\theta^2,
 \qquad j=2,3 .
 \end{split}                                                   \tag{3}
$$

These are the magnitudes before the four signs stated above. For fixed $J$, on intervals $|I|\ge N L^{-J}$ choose $A>J+1$ in (2) to get the corresponding relative leading terms. These are genuine endpoint additions to [R55](r55-source-all-small-triprime-comparator.md), not estimates for individual exceptional moduli, two high-endpoint legs against each other, the full long–long block, or Hypothesis S. The arithmetic proof is unconditional. Any use of the separate long-divisor reduction of the original operator still requires that reduction's assumptions.

## 1. Exact polynomial roles and symmetry corrections

On the dyad put $J_X=L/\log L$. All high primes on the relevant central support lie in the fixed interval

$$
 [V_-,V_+]=[\sqrt X e^{-21J_X},\,\sqrt X e^{21J_X}].
$$

Indeed $D\ge V_-$ and $N/D\le V_+$ for all sufficiently large $X$ on the dyad. For $H_1$ the upper bound on the high prime follows from $qa>D$; for $H_2$ it follows from the other high prime $>D$. The lower primes are in $[2,U_*]$, $U_*=\sqrt X e^{-19J_X}$, as before. The envelopes may overlap, but the actual $N$-dependent hard windows still have the required strict separation at $D$.

For the analytic polynomial of $H_1$ first use both orders of the low primes, with weight $(\log p)/2$, and admit equality of the low primes. For $H_2$ use both orders of the high primes, with weight $(\log q)/2$, admitting high equality. Each squarefree frequency has the exact original positive mark. A repeated low prime in $H_1$ must satisfy $q^2>D$, so $q\gg X^{.245}$ for large $X$, and a repeated high prime in $H_2$ exceeds $D\gg X^{.49}$. The number of possible repeated integer frequencies of both kinds together is $O_\rho(X^{.76})$ from $\sum_{\ell\ge X^{.245}}2X/\ell^2$. Each frequency has bounded factorization multiplicity even before removal, and weight $O(L)$. On the full sum line the other integer is determined, so the two symmetry corrections cost $O_\rho(X^{.76}L^2)$ uniformly in $I$. For type 3 its ordered polynomial of [R55](r55-source-all-small-triprime-comparator.md) may likewise be used and corrected on the full sum line by the previously bounded repetitions. No assertion about repeats on a partial arc set is used here.

## 2. Minor arcs with the exact extra product gate

Take $Z=2A+2b+100$, $P=L^{6Z}$, and use the fixed classical major arcs about reduced fractions $d\le P$, of common half-width $P/X$, with complement $\mathfrak g$. This is a full-circle analysis, not a change to the exact square-root arc family in [R51](r51-source-retuned-endpoint-exact-minor.md). On $\mathfrak g$ Dirichlet approximation gives a reduced $a/d$ with $P<d\ll X/P$ and error $\le d^{-2}$. Use the fixed physical envelope $[\rho X/2,2X]$.

For either new leg, take a **high** prime $p$ as the primary variable and let the partner integer be $m=qa$ or $m=qr$. In $H_1$ the hard inequality $m>D$ (and optionally $m\le N/D$, which is automatic for true physical products when $p>D$) is an integer dyadic axis of its own. Thus this moving, nonlinear gate on the two low primes is not smoothed or treated as a product of independent cutoffs on $q,a$. In $H_2$ the partner has a high factor, so its product already exceeds $D$; no extra axis is required.

We show the uniform joint energy bound at any fixed set of aligned dyadic levels of the prime-factor axes, the physical axis, and, for $H_1$, this partner-product axis:

$$
 \sup_{\alpha\in\mathfrak g}\ 
      \sum_{\text{cells}} |A_{i,\text{cell}}(\alpha)|^2
             \ll_{\rho,A,b} X^2 L^{6-Z},\qquad i=H_1,H_2 .   \tag{4}
$$

Initially use the fixed envelopes; actual $N$-masks are restored through their dyadic unions below. In a primary-prime dyad $U\le p<2U$, put $V=X/U$; the partner integers have scale $V$. For a fixed pair of factor cells for the partner and fixed partner-product cell when present, group by the integer $m$. Its multiplicity is at most two for ordered prime factors, even when the fixed envelopes overlap. For the $H_1$ mark use Cauchy in $m$ with an outer factor $O(V)$ and inner prime weights $\log p$; for $H_2$ the weights $\log q$ are on the partner and their squared Cauchy factor is $O(VL^2)$. Sum these **nonnegative** estimates over both partner-factor axes and the partner-product axis before enlarging $m$: a fixed $m$ has at most two ordered prime decompositions over all those cells and belongs to exactly one partner-product cell at the given level. This permits a single enlargement to all integers of scale $V$. The product gate was exact in the actual polynomials and in their decomposition; this enlargement happens only after Cauchy.

Once expanded and summed over the physical cells, the bound is the floor-cell calculation of [R54](r54-source-central-triprime-comparator.md) and [R55](r55-source-all-small-triprime-comparator.md), with prime primary variable $p$. For $p'=p+h>p$, the interval cut $hm<H$ at physical cell length $H$ leaves the exact common-cell indicator $1-hm/H+\psi((p+h)m/H)-\psi(pm/H)$, with $\psi(t)=\{t\}-1/2$. Every ordinary dyad here satisfies $X^{.4}\ll U\ll X^{.6}$, $UV=X$. In particular $U/(X L^{-Z})=o(1)$ and $V\ll X L^{-Z}$. Use the Fejér scale $Y_0=X L^{-Z}$ and group the $h$'s into $O(G)$ intervals of length at most $d/2$, $G=1+U/d$. On short cells $H<2Y_0$ the raw off-diagonal is $O(XH L^2)$. Otherwise the degree $K=\lfloor H/Y_0\rfloor$ has the same inclusive discrete jump bound, with total error $O(X^2L^{4-Z})$, since the number of possible prime divisors $p$ of a grid product is $O(L)$. The grouped affine bound is $O(UV L^2G(V+dL))$. The oscillatory bound, deriving as in [R54](r54-source-central-triprime-comparator.md) §1 by near/far spacing of $\alpha h$ in each block and by summing shifted $p$ phases of step $k/H$, is

$$
 O_\rho\!\left(VL^2\{G(VL+HL+dUVK/H+dU L^2)+UG(V+dL)L\}\right).
$$

For the somewhat higher possible $U$, the estimates still apply: $GV^2=V^2+XV/d$, $GVH=VH+XH/d$,
$GdUV^2K/H\le(d+U)V L^Z$, and $GdUV=X(d+U)$. The $XU$ term costs only $O(X^{1.6})$ up to fixed logarithms, while $d\gg L^{6Z}$, $d\ll X L^{-6Z}$ and $V\ll X L^{-Z}$ give the same savings in all terms involving $d$. Including the diagonal, the bound per ordinary dyad is $O_{\rho,A,b}(X^2L^{4-Z})$. The $O(L)$ ordinary dyads and Cauchy cost at most $L^2$, proving (4).

Each prime-axis selector, including its true $N$-unit holes, is a union of $O(L)$ hard integer intervals and hence of $O(L^2)$ aligned cells. The physical axis and the extra product axis each cost $O(L)$ cells. Thus the five axes of $H_1$ give at most $O(L^8)$ terms per leg, and the four of $H_2$ at most $O(L^7)$. The largest old partner cost is $O(L^7)$ terms and four axes (type 3) as in [R55](r55-source-all-small-triprime-comparator.md). At fixed levels the other leg needs only integrated joint energy $O(XL^2)$ by Parseval and bounded prime-factorization multiplicity. Cauchy and Bessel over integer outputs give total squared sum at most
$O(X^3 L^{8-Z+15+9})=O(X^3 L^{32-Z})$ after at most $O(L^{15})$ expansion terms and $O(L^9)$ level choices. If paired against type 2 its last-prime unit is restored as in [R53](r53-source-retuned-exact-local-comparator.md), at squared-sum cost $O(X^{5/2}L^4)$. All new prime units, both moving physical windows, and the $H_1$ product cut are already exact in their axes. Markov at $X L^{-A}$ yields a simultaneous minor bound except for $O_{\rho,A,b}(X L^{-b})$ targets. Only pairs with a new leg and an old partner are used.

## 3. Major arcs: exact weights and local tails

For the major analysis freeze the two outer primes and use the last high prime as the prime variable for either new type. The analytic symmetry model of §1 gives weight $w_{H_1,u}$ exactly for a nonsquare outer $u$, and half that weight if $u=q^2$ is temporarily included. For $H_2$ the symmetry factor is $1/2$ from the two high orders; coincidence of the last prime with the frozen high does not change a real integral, and was removed on the actual full sum line in §1. The actual $p>D$ is the hard real step $t/u>D$. In $H_1$ the mask $D<u\le N/D$ is already on the outer cofactor. In $H_2$ the same upper bound is automatic wherever the profile is nonzero.

Apply the [Siegel–Walfisz theorem, Theorem 12.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) and the effective denominator $d_u=d/(d,u)$ as in [R54](r54-source-central-triprime-comparator.md) §2 or [R55](r55-source-all-small-triprime-comparator.md) §3. Both new last primes have polynomial scale at least $D\gg X^{.49}$, and the true phase is $a u/(d,u)$ reduced modulo $d_u$. For the two old types the previous SW scale estimates still apply. Partial summation on the actual last-prime hard interval adds only fixed logarithms and the $O(P)$ phase variation; another polynomial in $P$ for summing residues is allowed. The logarithmic marker $\log p$ of $H_1$ divides out of the unweighted prime density, and the marker $\log q$ of $H_2$ is constant at fixed outer cofactor. The upper and lower hard boundaries are handled by the two real prefixes with their actual endpoint convention. Divisor exclusions from the last prime cost at most $O(XL^2/V_-)$ for the new types: for each $p\mid N$ in the fixed high interval, there are at most $O(X/p)$ possible ordered outer products by their at-most-two factorization multiplicity. The total $\sum_u1/u\ll L^2$ suffices in summing errors. In consequence each genuine polynomial is approximated by $\sum_u(\mu(d_u)/\varphi(d_u))\int_J w_{i,u}(t)e(\beta t)\,dt$ to $O(X L^{-F})$ for any fixed $F$, on the arc at reduced $a/d+\beta$ with $|\beta|\le P/X$. The bounded measure $O(P^3/X)$ of the arcs permits arbitrary log accuracy in the signed integrated product.

Summing numerators gives the exact signed coefficients

$$
 \Gamma_{u,v}(d;N)
      =c_d(N)\frac{\mu(d_u)\mu(d_v)}{\varphi(d_u)\varphi(d_v)}.
$$

The complete signed series, by the [R54](r54-source-central-triprime-comparator.md)/[R55](r55-source-all-small-triprime-comparator.md) local calculation, vanishes for a common prime (both effective factors lose it and its local factor is $1+c_\ell(N)=0$) and otherwise equals $\mathfrak S(N)\prod_{\ell\mid uv}\lambda_\ell$. Every nonsquarefree $d$ is killed by a Möbius factor or by a Ramanujan prime-power zero at one of the special $N$-unit primes. This also holds for a temporarily repeated outer prime in $u=q^2$. The absolute series is uniformly $O(\mathfrak S(N))$.

For clarity the same tail calculation really applies with the new mixed low/high envelopes. Take dyad majorant $g_{i,u}=L/u$ for the new legs, and the [R55](r55-source-all-small-triprime-comparator.md) majorants for the old ones. Both sup norm and variation of the real weights, extended by zero beyond their hard windows, are $O_\rho(g_{i,u})$, including the jump at $uD$. For any squarefree $k$ each type satisfies $\sum_{u:k\mid u}g_{i,u}\ll_\rho L^3/k$ on its fixed envelope: an outer product has at most two primes, and at a single prescribed prime the remaining factor has harmonic mass at most $O(L)$. The total real Fourier tail beyond $P/X$ therefore costs $O_\rho(\mathfrak S(N)X L^6/P)$ by bounded variation and the absolute series estimate. After Fourier inversion $N-I\subseteq I_0(N)$, giving precisely the real pair integral in (1).

The absolute denominator tail averaged on the dyad is $O(L^6P^{-1/2})$ after normalizing out the real $X$ length bound. Indeed split the squarefree denominator into its special primes and the remaining $h$. Rankin's factor $d^{1/2}$ at noncommon primes costs only $1+\sqrt\ell/(\ell-1)$ individually; the common factors are handled by

$$
       \prod_{\ell\mid (u,v)}(1+\sqrt\ell)
          =\sum_{k\mid\operatorname{rad}((u,v))}\sqrt k
\quad\Longrightarrow\quad
 \sum_{u,v}g_{i,u}g_{j,v}\prod_{\ell\mid(u,v)}(1+\sqrt\ell)
        \ll L^6\sum_{k\ge1}k^{-3/2}.
$$

The remaining half-power series converges after using $\sum_{N\le2X}|c_h(N)|\le 2X\tau(h)$. Before dropping the moving cofactor masks in this average, the special primes have their Ramanujan values fixed by the actual $N$-units. Markov gives the restored major coefficient with error $O_{\rho,A,b}(\mathfrak S(N)N L^{-A})$ outside $O(XL^{-b})$ moduli, uniformly over $I$. For $H_1$ the temporary repeated cofactor has $q^2>D$, hence $\sum_{q^2>D}g_{i,q^2}\ll L/\sqrt D$; its model contribution is negligible even paired with the other totalling $O(L^3)$ weights. The old type 3 correction is as in [R55](r55-source-all-small-triprime-comparator.md). Combining this major computation with §2 and the actual repetition correction proves (2), with no change to a genuine unit, interval or cutoff.

## 4. The two endpoint constants

Put $L_N=\log N$, $d=(\log D)/L_N=\tfrac12-\theta+o(L_N^{-1})$, $\xi=(\log t)/L_N=1+O_\rho(L_N^{-1})$, and $w=\xi-2d=2\theta+O_\rho(L_N^{-1})$. These definitions in this section are real exponent variables. On both new legs $w\to0$ uniformly.

For $H_1$, let $\alpha=(\log q)/L_N$ and $\beta=(\log a)/L_N$. Its actual real profile is one half of the ordered reciprocal prime sum in the strip
$d<\alpha+\beta<d+w$, $\alpha,\beta\le d$, with the lower prime cutoff and unit masks. To replace the prime sum by its integral with an adequate error at the moving edges, first remove $\min(\alpha,\beta)\le \epsilon=\theta^2$. At fixed such $\alpha$, the permitted $\beta$ interval is of width at most $\alpha$ and lies in a fixed positive range near $d$; a dyadic Chebyshev bound gives reciprocal prime mass $O(\alpha+L_N^{-1})$. Hence the removed mass on either edge is $O(\epsilon+(\log L_N)/L_N)=o(w)$, using $\sum_{q\le N^\epsilon}\log q/q\ll 1+\epsilon L_N$. On the remaining exponent range each reciprocal prime interval differs from its integral $dt/t$ by $O(1/(\epsilon L_N))$, uniformly, by the prime reciprocal Mertens bound. This bound follows by partial summation from $\sum_{p\le x}(\log p)/p=\log x+O(1)$. For the second summation the integrated first-span length in reciprocal measure is
$\bigl[\log(\min(d,d+w-\alpha)/\max(\epsilon,d-\alpha))\bigr]_+$.
Its supremum and total variation are $O(\log(1/\epsilon))$: it is piecewise monotone, with changes only at the two switches between the constant/linear endpoints. Thus the two successive prime-measure errors cost $O(\log(1/\epsilon)/(\epsilon L_N))=o(w)$. The cofactor prime divisors of $N$ above $N^\epsilon$ are negligible even against the unrestricted reciprocal weight; smaller exclusions lie in the removed edge. The repeated outer pair is negligible as in §3. The integral of the edge strips has the same $O(\epsilon)$ upper bound.

We are left with

$$
 \frac12\int_0^d\frac{1}{\alpha}
         \log\!\left(\frac{\min(d,d+w-\alpha)}{d-\alpha}\right)d\alpha .
$$

The ends $\alpha<w$ and $\alpha>d-w$ cost $O(w)$: at the first the width is $\alpha$, and at the second the integral in $s=d-\alpha$ is bounded by a constant times $\int_0^w\log(1+w/s)\,ds$. On the middle range expand $\log(1+w/(d-\alpha))=w/(d-\alpha)+O(w^2/(d-\alpha)^2)$; the integrated error is $O(w)$. The main integral there is $(w/d)\log(1/w)+O(w)$. Since $d\to1/2$, $w\sim2\theta$, this proves the uniform profile $4\theta\log(1/\theta)(1+o_\rho(1))$.

For $H_2$ the low exponent must be $0<\alpha<w$, and the frozen high exponent $\beta=(\log r)/L_N$ belongs to $(d,d+w-\alpha)$. The real last exponent $\gamma=\xi-\alpha-\beta$ is $1/2+O(\theta)$, as is $\beta$. At fixed $\alpha$ the reciprocal prime mass for $r$ is $\log((d+w-\alpha)/d)+O(L_N^{-1})=(2+O(\theta))(w-\alpha)+O(L_N^{-1})$. The mark ratio and symmetry factor are $(\log q)/(2\log(t/(qr)))=\alpha(1+O(\theta))$. Hence the profile is $(2+O(\theta))\sum_q ((\log q)/(qL_N))(w-\alpha)$ over $\log N<q<N^w$, with error $O(w/L_N)$. Partial summation from the same prime Mertens estimate makes this sum $w^2/2+O(w\log L_N/L_N)$, accounting for the cutoff $q>\log N$ and unit deletions: $\sum_{q\mid N,\ q>\log N}(\log q)/q\le1$, while high prime divisors are negligible by their scale. Thus the uniform profile is $w^2(1+o_\rho(1))=4\theta^2(1+o_\rho(1))$.

Finally the partner profiles tend to $c_j$ by [R52](r52-source-retuned-full-count-comparator.md) and [R55](r55-source-all-small-triprime-comparator.md). All special factors $\lambda_\ell$ differ from one by $O(1/L_N)$ on the true outer cofactors. The model loss from a common frozen prime with a type 3 partner is negligible at every log power by the lower bound $\exp(37J_X)$ for that partner's contributing factors and the divisor mass bound of §3. For a type 2 partner, a prescribed common prime $\ell>\log N$ has new-leg summed real weight $O(L/\ell)$ (both new weights are $O(1/u)$), and the type 2 profile at that prime is $O((\log\ell)/(\ell L_N))$. Thus the total shared loss is $O(\sum_{\ell>\log N}(\log\ell)/\ell^2)=O((\log L_N)/L_N)=o(\theta^2)$ even summing integers. These estimates give (3) with the exact pair model. The four signs refer only to the stated mixed sectors; in an original new–new pair one must still retain $de>Q$.
