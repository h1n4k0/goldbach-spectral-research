# A genuine no-giant triprime block and its mixed full sum-line comparator

Fix $0<\rho<1/2$, $I_0(N)=[\rho N,(1-\rho)N]$, and a hard interval $I\subseteq I_0(N)$ with either endpoint convention. Use sufficiently large even $N$, the original retuned labels

$$
 j_N=\frac{\log N}{\log\log N},\qquad
 D=\lfloor\sqrt N e^{-20j_N}\rfloor,\qquad Q=\lfloor N e^{-20j_N}\rfloor,
$$

and actual units for both physical coordinates. There are two types of genuine legs.

* **Type 2** is the complete [R53](r53-source-retuned-exact-local-comparator.md) retuned semiprime leg $n=up$ with $u,p$ prime, $\log N<u\le D$, $(up,N)=1$, marked by $\log u$.
* **Type 3** is $n=qap$ with $q,a,p$ prime, $(qap,N)=1$,

$$
             N^{29/100}\le q\le N^{30/100},\qquad
             N^{32/100}\le a\le N^{33/100},
$$

marked by $\log n$. Its outer cofactor is $u=qa$. On the central interval the last prime $p$ has size between $\rho N^{37/100}$ and $(1-\rho)N^{39/100}$. In particular the three prime slots are disjoint for sufficiently large $N$, so this is a unique factorization with these prescribed roles, not a weighted multiplicity.

For $(i,j)=(3,3),(3,2),(2,3)$, let $C_{ij,N}(I)$ be the genuine sum-line count of ordered pairs $n+m=N$, $n\in I$, $m\in I_0(N)$, of types $i,j$ with their displayed **positive** marks. Write $\mathcal U_i(N)$ for the permitted outer cofactors of type $i$, including the actual unit mask $(u,N)=1$. These are squarefree, with at most two primes. For $t\in I_0(N)$ set

$$
 w_{2,u}(t)=\frac{\log u}{u\log(t/u)},\qquad
 w_{3,u}(t)=\frac{\log t}{u\log(t/u)},\qquad
 \lambda_\ell=\frac{\ell-1}{\ell-2}\quad(\ell>2\text{ prime}),
$$

and let $\mathfrak S(N)$ be the ordinary even binary singular series as in [R52](r52-source-retuned-full-count-comparator.md). The comparator is

$$
 M_{ij,N}(I)=\mathfrak S(N)
       \sum_{\substack{u\in\mathcal U_i(N),\ v\in\mathcal U_j(N)\\(u,v)=1}}
       \left(\prod_{\ell\mid uv}\lambda_\ell\right)
       \int_I w_{i,u}(t)w_{j,v}(N-t)\,dt.                      \tag{1}
$$

**Theorem (unconditional).** For each fixed $A,b>0$, with $L=\log X$, outside $O_{\rho,A,b}(X L^{-b})$ even $N\in[X,2X]$, simultaneously for every hard $I$ and the three type pairs above,

$$
  C_{ij,N}(I)-M_{ij,N}(I)
       =O_{\rho,A,b}\big(\mathfrak S(N)N L^{-A}\big).           \tag{2}
$$

The comparator coefficients on the same central interval satisfy, uniformly in $I$,

$$
 \begin{split}
 M_{33,N}(I)&=\mathfrak S(N)|I|\,(c_3^2+o_\rho(1)),\\
 M_{32,N}(I),\,M_{23,N}(I)&=\mathfrak S(N)|I|\,(c_3\log2+o_\rho(1)),\\
 c_3&=\int_{29/100}^{30/100}\int_{32/100}^{33/100}
              \frac{d\beta\,d\alpha}{\alpha\beta(1-\alpha-\beta)}>0 .
 \end{split}                                                   \tag{3}
$$

**Exact connection to the original long divisors.** Type 3 is a genuine zero-small **no-giant** class: all its prime factors exceed $\log N$ but lie below $D$. Every two-prime product is at least a fixed constant times $N^{61/100}$, hence exceeds $D$; the divisor equal to $n$ has zero logarithmic mark. Thus the complete long-divisor factor is $+\log n$ on type 3, whereas it is $-\log u$ on type 2. Any contributing two-leg product of long divisors exceeds $Q$, even in the mixed case (the type 2 giant is $\ge\rho N/D$). Therefore no moving product-cutoff terms have been suppressed: on this central box the only nonzero alias is $n+m=N$, with the original negative sum-alias sign, so the actual marked coefficient is negative for $(3,3)$ and positive for $(3,2),(2,3)$. The arithmetic identification and theorem are unconditional. Using the separate long-divisor reduction for the original operator still requires that reduction’s own assumptions. The theorem treats these typed triprimes and their stated partners, not all no-giant integers, exceptional targets, or Hypothesis S. In particular this is not an estimate for the pair of two Type 2 legs.

## 1. Classical minor arcs for a genuine two-prime partner

Write $Z=2A+2b+64$, $P=L^{6Z}$, and use the fixed classical major set $\mathfrak G$ of all reduced centers $d\le P$ with common half-width $P/X$. Its arcs are disjoint for large $X$; write $\mathfrak g=\mathbb T\setminus\mathfrak G$. It is not the [R51](r51-source-retuned-endpoint-exact-minor.md) exact square-root Dirichlet family. On $\mathfrak g$, ordinary Dirichlet approximation with parameter $\lceil X/P\rceil$ gives a reduced $a/d$ with $P<d\ll X/P$ and error $\le d^{-2}$. In fact any approximant with $d\le P$ and error $\le1/(d\lceil X/P\rceil)$ is inside $\mathfrak G$.

Use fixed envelopes $[\rho X/2,2X]$ for integer physical indices, $[X^{.29},2X^{.30}]$ for $q$, and $[X^{.32},2X^{.33}]$ for the second small prime $a$. The last prime of type 3 can be restricted to a fixed envelope $[c_\rho X^{.37},C_\rho X^{.39}]$, implied by the physical envelope and the two smaller envelopes. Choose the constants to include every such centrally contributing last factor. At fixed aligned dyadic levels let $J,E,F$ be cells of the physical, $q$, and $a$ axes. Initially omit the target-dependent unit holes. At fixed levels we claim for the genuine type 3 polynomials

$$
        \sup_{\alpha\in\mathfrak g}
          \sum_{J,E,F}|A_{3;J,E,F}(\alpha)|^2
           \ll_{\rho,A,b}X^2 L^{6-Z}.                         \tag{4}
$$

Here is why the extra prime-cofactor axis does not lose the floor-cell cancellation. In a $q$ dyad $U\le q<2U$ put $V=X/U$ and group the other two primes as $m=ap$, so $m\asymp_\rho V$ for central products. Each such $m$ has at most one admissible factorization into an $a$ from its fixed band and a $p$ from the separated last-prime band. For fixed $F$, let $\mathcal G_F$ denote the resulting partner integers $m$ with $a\in F$. The sets $\mathcal G_F$ are disjoint at the chosen $F$ level. Split the true mark $\log(qm)=\log q+\log m$. For the first term use Cauchy in $m\in\mathcal G_F$, with outer factor $O_\rho(V)$ and the $\log q$ weight in the inner $q$ sum. For the second term put $\log m$ in the Cauchy factor $O_\rho(VL^2)$ and leave the inner $q$ sum unmarked. Sum these nonnegative Cauchy bounds over $F$ **before** expanding the inner squares. Disjointness lets us enlarge the remaining $m$ sum once, not once per $F$, to the whole integer interval of scale $V$. After expanding and summing over all physical cells $J$ the only condition in the $m$ sum, besides interval bounds, is the same-cell factor of [R50](r50-source-full-admissible-exact-dirichlet-mean.md)/[R52](r52-source-retuned-full-count-comparator.md): for $q'=q+h>q$ and $hm<H$, with $H$ the physical cell length, it is

$$
             1-hm/H+\psi((q+h)m/H)-\psi(qm/H),\qquad
                 \psi(t)=\{t\}-1/2.
$$

Negative differences are conjugate. Both $qm,q'm$ lie in the same fixed physical envelope, so those restrictions and $hm<H$ cut one interval for the integer $m$. The floor identity works at integer endpoints. When removed, the partner prime constraints were used only as disjoint supports in the nonnegative squared upper bound, not as an additive approximation of an actual coefficient.

For completeness the [R52](r52-source-retuned-full-count-comparator.md)/[R53](r53-source-retuned-exact-local-comparator.md) numerical parameters still give (4). Partition $h\le U$ into $O(G)$ groups of length at most $d/2$, $G=1+U/d$. Within each group $\alpha h$ are $1/(2d)$-separated and their truncated sum of reciprocal distances from zero is $O_\rho(V+dL)$ (the nearest term costs at most $O_\rho(V)$). Use $Y_0=X L^{-Z}$. If $H<2Y_0$ there are $O_\rho(H/V)$ positive $h$ and the crude off-diagonal is $O(XH L^2)$. Otherwise take the Fejér degree $K=\lfloor H/Y_0\rfloor$. The discrete grid error of [R50](r50-source-full-admissible-exact-dirichlet-mean.md), including the jump, costs $O(XY_0L^4)$ after summation: for each $h$, an integer $qm$ or $(q+h)m$ has at most $O(L)$ eligible prime divisors, there are $O(X/H)$ residue periods, and the mark and outer Cauchy contribute $O(VL^2)$. The diagonal costs $O(UV^2L^2)$, and the affine part costs $O(UV L^2 G(V+dL))$. For a nonzero mode $k\le K$, $kU/H\le U/Y_0=o(1)$. The near set $\|\alpha h\|\le4kU/H$ has $O(G(1+dkU/H))$ indices, and then the shifted $q$ phases have step $k/H$ in a span $<1/4$, costing $O_\rho(V+(H/k)L)$ for each $h$. On the far set use half the old norm of $\alpha h$ and the grouped reciprocal bound. Summing the $1/k$ coefficients gives the oscillatory bound

$$
 O_\rho\!\left(VL^2\{G(VL+HL+dUVK/H+dU L^2)+UG(V+dL)L\}\right).
$$

In this expression $GV^2=V^2+XV/d$, $GVH=VH+XH/d$, $GdUV^2 K/H\le(d+U)V L^Z$, $GdUV=X(d+U)$, and $G(V+dL)\ll V+X/d+(d+U)L$. Here $U\ll\sqrt X$, $V\ll X L^{-Z}$, $d>L^{6Z}$, and $d\ll X L^{-6Z}$. Every contribution is $O_{\rho,A,b}(X^2 L^{4-Z})$ on one $q$ dyad. Cauchy over the $O(L)$ ordinary dyads adds at most $L^2$, giving (4) at the chosen three levels, uniformly in them.

The other leg needs only integrated cell energy $O_\rho(XL^2)$ by Parseval and unique factorization of each physical frequency. This applies also to the type 2 leg on the fixed [R53](r53-source-retuned-exact-local-comparator.md) envelopes: its genuine $u$ is at most $U_*=\sqrt X e^{-19L/\log L}$ and its $p$ exceeds $\sqrt{2X}$. We do not need a minor-arc bound on that leg itself. The cofactor and physical windows of type 3, including the units on $q,a$, each use $O(L)$ aligned dyadic cells; there are only $O(1)$ possible forbidden prime divisors of $N$ in their polynomial bands. For type 2, the cofactor window including its at most $O(L)$ unit holes uses $O(L^2)$ cells and the physical window $O(L)$. In both pairings at most $O(L^6)$ fixed-cell terms occur in the product expansion. The number of level choices is $O(L^6)$ (indeed one fewer in the mixed case). At fixed levels Bessel over the output integers gives the integral of the product of the two joint cell energies on $\mathfrak g$. Use (4) and Parseval; Cauchy for the expansion and the level sum then give a total maximal squared sum $O_{\rho,A,b}(X^3 L^{20-Z})$.

The missing last-prime units can be reinstated without affecting this bound. There are only $O(1)$ forbidden partners dividing $N$ on the type 3 polynomial band. Fixing any one leaves $O(X^{.63})$ possible products $qa$, distinct by their separated roles, each mark $O(L)$. Its removed transform has squared energy $O_\rho(X^{.63}L^2)$. For type 2 the corresponding bound is $O(X^{1/2}L^2)$ as in [R53](r53-source-retuned-exact-local-comparator.md). Cauchy on the same minor arcs against the unaffected leg with energy $O(XL^2)$ bounds the change by $O_\rho(X^{.815}L^2)$ per target; a product of two removed pieces is no larger and can also be included in a telescoping replacement. The squared sum $O(X^{2.63}L^4)$ fits the estimate. All moving physical endpoints and cofactor cutoffs were exact. Markov at $XL^{-A}$ with the stated $Z$ proves the required signed bound on $\mathfrak g$ on one common good set for all three pairs.

## 2. Classical major arcs and exact common-factor deletion

For a squarefree outer cofactor $u$ of either type put $d_u=d/(d,u)$ at a reduced center $a/d$ of $\mathfrak G$. The prime variable's effective rational phase has denominator $d_u$, including when one or two primes of $u$ divide $d$. Every genuine last prime exceeds $P$. Applying [Siegel–Walfisz, Theorem 12.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) at the polynomial scale of that last prime, summing its reduced residue classes and changing variable $t=up$ gives the real model

$$
 A_{i,J}(N;a/d+\beta)=
     \sum_{u\in\mathcal U_i(N)}
          \frac{\mu(d_u)}{\varphi(d_u)} W_{i,u,J}(\beta)
       +O_{\rho,A,b,F_1}(X L^{-F_1}),\quad
 W_{i,u,J}(\beta)=\int_J w_{i,u}(t)e(\beta t)\,dt,               \tag{5}
$$

for any fixed $F_1>0$, uniformly for both types and all original hard $J$. The principal reduced-residue average is independent of the numerator because $a u/(d,u)$ is a unit modulo $d_u$. To see the uniform error, use two prime prefixes at scale $X/u$, remove the proper powers in the logarithmic prime theorem, and apply partial summation with the reciprocals of the last-prime logarithms. The real endpoints or singleton prime atoms are accounted for by the prefix conventions. The phase has $O(P)$ variation over the physical interval at $|\beta|\le P/X$. The mark is either $\log u$ or $\log t$, both bounded by $O(L)$ including variation. Summing the errors over $u$ costs at most $O(L)$ in the reciprocal sum $\sum_u 1/u$ for type 2, and $O(1)$ for type 3 by the two prime harmonic sums on its fixed exponent bands. The target-dependent last units can be omitted in the prime-theorem application then reinstated at cost $O(X^{.63}L)$ or smaller by the previous count of possible indices. These losses fit any specified inverse-log error in (5) by increasing the prime theorem accuracy. No prime estimate at a polynomial-size modulus is being used.

The total major measure is $O(P^3/X)$, and actual polynomials and the real approximants are $O_\rho(XL)$, so choosing $F_1$ large after $A,b$ makes the integrated transform replacement error $O_{\rho,A,b}(XL^{-A})$. The exact coefficient after summing reduced numerators is

$$
 \Gamma_{u,v}(d;N)=c_d(N)
         \frac{\mu(d_u)\mu(d_v)}{\varphi(d_u)\varphi(d_v)} .
                                                               \tag{6}
$$

It multiplies the real product integral with target phase $e(-N\beta)$ over $[-P/X,P/X]$, the same interval for each denominator.

The signed complete series in (6) is zero if $(u,v)>1$, and otherwise equals $\mathfrak S(N)\prod_{\ell\mid uv}\lambda_\ell$. Indeed a nonsquarefree $d$ is killed by a Möbius factor at a prime not dividing $uv$, or by $c_{\ell^j}(N)=0$ at a special prime $\ell\mid uv$ (all such primes are units modulo $N$). At an ordinary prime the Euler factor is $1+c_\ell(N)/(\ell-1)^2$. At a prime dividing exactly one cofactor, one effective denominator loses that prime and the remaining Möbius factor has sign $-1$. As $c_\ell(N)=-1$ this gives the factor $1+1/(\ell-1)$, of ratio $\lambda_\ell$ to the ordinary one. At a common prime both effective denominators lose it, and the factor is $1+c_\ell(N)=0$. The corresponding absolute series is $O(\mathfrak S(N))$ uniformly: outside at most four special primes the ordinary absolute Euler factors have a bounded ratio to the singular series, and each special absolute factor is at most two. In particular this keeps, then cancels, any shared frozen primes of the major model, even for the mixed type pair.

## 3. Uniform tails and the size of the comparator

Use fixed positive dyad weights $g_{2,u}=(\log u)/(uL)$ for type 2 and $g_{3,u}=1/u$ for type 3. A type 2 cofactor is prime, and a type 3 cofactor is the product of its two prescribed primes. The magnitude and variation of $w_{i,u}\mathbf1_J$ are both $O_\rho(g_{i,u})$ uniformly on the central interval. Also $\sum_u g_{i,u}\ll1$ on each fixed cofactor envelope. The real Fourier product tail for a pair, outside $[-P/X,P/X]$, is $O_\rho(X g_{i,u} g_{j,v}/P)$ by bounded variation, so the absolute coefficient sums make this $O_\rho(\mathfrak S(N)X/P)$ pointwise after summing pairs. Upon real inversion the product for each pair is exactly $\int_I w_{i,u}(t)w_{j,v}(N-t)\,dt$ using $N-I\subseteq I_0(N)$, and is bounded by $O_\rho(Xg_{i,u}g_{j,v})$.

For the separate denominator tail, average

$$
 \mathcal E_N=\sum_{u\in\mathcal U_i(N),\,v\in\mathcal U_j(N)}
          g_{i,u}g_{j,v}\sum_{d>P}|\Gamma_{u,v}(d;N)|.
$$

Insert the Rankin factor $d^{1/2}/P^{1/2}$ and split the squarefree $d$ into its special primes dividing $uv$ and its other part $h$ coprime to $uv$. Since the special $c_\ell$ values are already fixed by the exact units, the $h$ part can be averaged over the whole dyad even though the cofactor selections are target dependent. The divisor formula gives $\sum_{N\le2X}|c_h(N)|\le2X\tau(h)$, and $\sum_h \mu(h)^2 h^{1/2}\tau(h)/\varphi(h)^2<\infty$. A prime dividing exactly one cofactor contributes the bounded factor $1+\sqrt\ell/(\ell-1)$ in the Rankin moment, with at most four such primes. For a common prime the factor is $1+\sqrt\ell$, possibly large. Crucially

$$
 \prod_{\ell\mid (u,v)}(1+\sqrt\ell)=\sum_{k\mid(u,v)}\sqrt k,
 \qquad
       \sum_{u:k\mid u}g_{i,u}\ll 1/k
                                                               \tag{7}
$$

on the fixed dyad envelopes for either type. For a prime $k$ this latter bound is immediate for type 2; for type 3 one sums the reciprocal prime mass of the remaining factor on its separated band. For a product of two primes $k$, there is at most the single type 3 cofactor $u=k$; for all other $k>1$ there is no term, and $k=1$ is the bounded weight total. Hence the weighted special common-prime sum is at most a constant times $\sum_{k\ge1} k^{-3/2}<\infty$ by (7). This proves $\sum_{N\in[X,2X],\,2\mid N}\mathcal E_N\ll XP^{-1/2}$. Markov makes $\mathcal E_N\le L^{-A}$ outside $O(X L^A P^{-1/2})=O_{A,b}(XL^{-b})$ targets, on one set independent of $I$. The signed complete major model now equals (1) with error $O_{\rho,A,b}(\mathfrak S(N)N L^{-A})$. The classical minor estimate and integer Fourier orthogonality finish (2). For clarity, an actual shared constituent, not just a frozen cofactor prime, is impossible on the sum line because it would divide $N$ in violation of the actual units.

Finally, uniformly for $t\in I_0(N)$, the type 3 raw real profile is

$$
 \sum_{u\in\mathcal U_3(N)}w_{3,u}(t)=c_3+o_\rho(1).
$$

Indeed $\log t=\log N+O_\rho(1)$, and reciprocal prime measure on each fixed exponent interval tends to $d\alpha/\alpha$ by the prime Mertens formula. The integrand $\log t/\log(t/(qa))$ tends uniformly to $(1-\alpha-\beta)^{-1}$ on the two exponent bands. Removing $q,a\mid N$ loses $O_\rho(N^{-.29})$ by bounded reciprocal mass on each band and the bounded number of such divisors. The corresponding type 2 profile tends uniformly to $\log2$ by [R52](r52-source-retuned-full-count-comparator.md) §4. All factors $\lambda_\ell$ differ from one by $O(1/\log N)$ uniformly for these cofactor primes. Excluding the common frozen factors costs at most a constant times $\sum_{\ell>\log N}\ell^{-2}$ in the summed model weight, by the prime case of (7), so this error also tends to zero. This proves (3).

If used in the central logarithmic physical kernel, the uniform moving-interval discrepancy (2) transfers to an $O_{\rho,A,b}(\mathfrak S(N)L^{-A})$ Hilbert–Schmidt discrepancy after normalization by $N$: insert the bounded-variation weight $\sqrt{(n/N)(1-n/N)}$ by Abel summation on the sole central alias line. The physical cumulative and logarithmic area are bounded in terms of $\rho$ on this compact central support. This transfer is only for the stated arithmetic components and their own comparators; it does not claim compensation with the remaining central or exterior terms.
