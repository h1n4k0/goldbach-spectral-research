# All-small-prime no-giant triprimes and the signed two-class benchmark

Fix $0<\rho<1/2$, $I_0(N)=[\rho N,(1-\rho)N]$, and let $I\subseteq I_0(N)$ be any hard interval. For sufficiently large even $N$ use the original retuned divisor and product cutoffs

$$
 j_N=\frac{\log N}{\log\log N},\qquad
 D=\lfloor\sqrt N e^{-20j_N}\rfloor,\qquad Q=\lfloor N e^{-20j_N}\rfloor .
$$

Keep the exact units modulo $N$ on both legs. Type 2 is the [R53](r53-source-retuned-exact-local-comparator.md) genuine semiprime leg $n=up$, $u,p$ prime, $\log N<u\le D$, marked by $\log u$. The new type 3 in this note is **every squarefree triprime $n$ whose three prime factors are at most $D$**, marked by $\log n$. There are no fixed exponent bands in type 3. For each $n\in I_0(N)$ of type 3, every prime factor is larger than $\log N$ automatically, since it is at least $\rho N/D^2$. Both types are zero-small classes. Type 3 is no-giant; this does not include other nonadmissible forms with a prime exceeding $D$.

Let $C_{ij,N}(I)$ denote their true positive marked count on the ordered sum line $n+m=N$, $n\in I$, $m\in I_0(N)$, of types $i,j$. Define the exact local comparators as follows. Let $\mathcal Q_N=\{q\text{ prime}:\log N<q\le D,\ (q,N)=1\}$, and take $\mathcal U_2=\mathcal Q_N$ and $\mathcal U_3=\{qa:q,a\in\mathcal Q_N,\ q\ne a\}$, viewed as sets of outer cofactors. Put, for $t\in I_0(N)$,

$$
 w_{2,u}(t)=\frac{\log u}{u\log(t/u)},\qquad
 w_{3,u}(t)=\frac{\log t}{3u\log(t/u)}\,\mathbf1_{t/u\le D},\qquad
 \lambda_\ell=\frac{\ell-1}{\ell-2}.
$$

Here $1/3$ counts the three possible choices of last prime in a squarefree triprime. The other two primes are an unordered pair in the outer cofactor $u$, and $t/u>\log N$ is automatic on the support. Let $\mathfrak S(N)$ be the ordinary even binary singular series. For $i,j\in\{2,3\}$ put

$$
 M_{ij,N}(I)=\mathfrak S(N)
      \sum_{\substack{u\in\mathcal U_i,\ v\in\mathcal U_j\\(u,v)=1}}
       \left(\prod_{\ell\mid uv}\lambda_\ell\right)
             \int_I w_{i,u}(t)w_{j,v}(N-t)\,dt .
                                                               \tag{1}
$$

**Theorem (unconditional).** For every fixed $A,b>0$ put $L=\log X$. Outside $O_{\rho,A,b}(XL^{-b})$ even $N\in[X,2X]$, simultaneously for every hard $I$ and the four type pairs,

$$
             C_{ij,N}(I)-M_{ij,N}(I)
           =O_{\rho,A,b}\big(\mathfrak S(N)N L^{-A}\big).        \tag{2}
$$

The deterministic leading factors, uniformly on the central range, are

$$
    M_{ij,N}(I)=\mathfrak S(N)|I|\,(c_i c_j+o_\rho(1)),
       \qquad c_2=\log 2,\quad c_3=\frac{\pi^2}{12}.             \tag{3}
$$

The $(2,2)$ result is [R53](r53-source-retuned-exact-local-comparator.md); the other three use the true entire all-small-prime triprime leg.

For the original long-divisor contribution, the type 2 long mark is $-\log u$ and the type 3 long mark is $+\log n$. In fact for type 3 all three products of two primes are at least $\rho N/D>D$, all single primes are at most $D$, and the divisor $n$ has zero logarithmic weight. Thus the product cutoff $de>Q$ is automatic across these legs, including the mixed terms, because on type 2 the nonzero long divisor is also $\ge\rho N/D$. There are no nonzero difference aliases in $I_0(N)^2$, and the sole sum alias has the original **negative** sign. Consequently the signed contribution of their selected union has signed raw line count

$$
 \begin{split}
 -C_{22,N}(I)+C_{23,N}(I)+C_{32,N}(I)-C_{33,N}(I)
   &=-\mathfrak S(N)|I|\left((\pi^2/12-\log 2)^2+o_\rho(1)\right)\\
   &\quad+O_{\rho,A,b}(\mathfrak S(N)N L^{-A})
 \end{split}                                                    \tag{4}
$$

on the good moduli. This leading sign, for example, is strict for $|I|\ge N L^{-J}$ at any fixed $J$ by taking $A>J$. It is not a sign for all long–long terms, a pointwise estimate on the exceptional targets, or a claim about Hypothesis S. The arithmetic counts themselves are unconditional; using the separate retuned reduction to identify components of the original operator requires its own assumptions.

## 1. Ordered triples, repetitions and fixed envelopes

For the analytic proof first use all ordered prime triples $(q,a,p)$ with each prime in $\mathcal Q_N$, mark $\log(qap)/6$, and allow repeated primes within a triple. For a squarefree $n=qap$ this gives exactly the type 3 polynomial, since the six permutations have total mark $\log n$. On the central sum line a repeated prime $\ell$ in such a triprime has $\ell^2\ge\rho N/D$, because the remaining prime is at most $D$. Consequently the number of possible integers with a repeated prime here is at most

$$
       \sum_{\ell\ge c_\rho N^{1/4},\ \ell\le\sqrt N} \frac N{\ell^2}
               \ll_\rho N^{3/4}.
$$

The other integer on the sum line is then determined. Its total polynomial mark is $O(L)$ in either type, including multiplicities of the ordered triples (at most six). Thus the full sum-line count changes by $O_\rho(X^{3/4}L^2)$ uniformly over hard $I$ when repetitions are removed, including when both slots are ordered triples. This is a full-line deletion, not an estimate on a partial arc set. If the nonsquarefree triprimes with all primes at most $D$ were included with their actual long-divisor marks instead, their total contribution in these same pairings obeys the same bound, since each such mark is $O(L)$.

Throughout use $J_X=L/\log L$, $U_*=\sqrt X e^{-19J_X}$ and $Y_*=\exp(37J_X)$. For large $X$ all $D\le U_*$. On the fixed dyad-wide physical envelope $[\rho X/2,2X]$, any product of three positive primes at most $U_*$ forces each prime to be at least $(\rho X/2)/U_*^2\ge Y_*$ for large $X$. Thus the fixed envelope $[Y_*,U_*]$ for each of the three factors contains the entire genuine type 3 eligibility, including the ordered repetitions. This fact is used both for minor arcs and for the uniform prime scale on the major arcs. No individual prime factor is assumed to have polynomial size.

## 2. Joint minor-cell energy with the two partner axes

Take $Z=2A+2b+100$, $P=L^{6Z}$, and the same classical major arcs as in [R54](r54-source-central-triprime-comparator.md), all reduced fractions of denominator $d\le P$ with common half-width $P/X$. Their complement is a fixed set $\mathfrak g$ on the dyad. On it there is an undilated Dirichlet approximant with $P<d\ll X/P$ and error at most $d^{-2}$. This is the classical decomposition for a full-torus count, not the exact Dirichlet complement of [R51](r51-source-retuned-endpoint-exact-minor.md).

At fixed aligned integer cell levels for $q,a,p$ and physical index $n$, consider the actual ordered triple polynomials on the product cells, before target-dependent unit holes. The same nonnegative Cauchy argument as [R54](r54-source-central-triprime-comparator.md) gives joint summed energy

$$
        \sup_{\alpha\in\mathfrak g}\sum_{\text{four cells}}
                 |A_{3,\text{cell}}(\alpha)|^2
               \ll_{\rho,A,b} X^2 L^{6-Z}.                    \tag{5}
$$

Here are the details needed to transfer the [R54](r54-source-central-triprime-comparator.md) argument without exponent separation or unique partner roles. In an ordinary $q$ dyad of scale $U$, the partner integer $m=ap$ has scale $V=X/U$. For each pair of cells in the $a,p$ axes, group the prime pair by $m$. Its multiplicity $k_m$ is at most two, since $m$ is a product of two primes. Across all pairs of cells at fixed levels, each $m$ has at most two ordered assignments in total. Split the mark $\log(qm)/6$ into a fixed multiple of $\log q+\log m$. For a fixed partner cell pair use Cauchy in $m$ with coefficient $k_m$ in the outer factor, along with $\log m$ if this is the second part of the split. The outer factor is $O_\rho(V)$ or $O_\rho(VL^2)$; the remaining sum of nonnegative inner $q$ squares is over its partner support. Summing those upper bounds over the two partner cell axes therefore costs at most a factor two in the inner $m$-sum. At this stage enlarge $m$ to the interval of all integers on its scale, **once** at the chosen levels, before expanding. Then expanding and summing the physical cells gives the exact same-floor condition for $qm$ and $(q+h)m$, with the same sawtooth and hard endpoints as in [R54](r54-source-central-triprime-comparator.md). The marker-dependent losses are the same $L^2$ inside the bound. This uses no equidistribution of semiprimes.

For the rest of the bound one may now apply the proof of [R54](r54-source-central-triprime-comparator.md) §1 verbatim to this enlarged, nonnegative estimate. The required inequalities are $U\le U_*\ll\sqrt X$, $U\ge Y_*/2\gg L^Z$, $V\ll X L^{-Z}$, $d>L^{6Z}$, and $d\ll X L^{-6Z}$. They hold for every outer dyad, with absolute clipping constants. Partition differences by blocks of length $\le d/2$, take the Fejér scale $X L^{-Z}$, and chop the off-diagonal at $hm<H$ for physical cell length $H$. The discrete error for a fixed $h$ uses only that $q$ or $q+h$ is prime, so the multiplicity of a grid product is $O(L)$ also here after the partner enlargement. The bounds $O(XH L^2)$ for $H<2X L^{-Z}$ and $O(X^2L^{4-Z})$ for the Fejér error in the other case apply as before. The grouped oscillatory, affine and diagonal terms of [R54](r54-source-central-triprime-comparator.md) are $O_\rho(X^2 L^{4-Z})$ per ordinary dyad under the displayed inequalities. The $O(L)$ dyads add at most $L^2$ by Cauchy, proving (5).

On the actual $N$-unit masks each of the three type 3 prime intervals has at most $O(L)$ holes, since the holes are prime divisors of $N$. It uses $O(L^2)$ aligned dyadic cells; the physical interval uses $O(L)$ cells. This also restores the last-prime upper endpoint $p\le D$ as an exact hard integer window, not a physical approximation. Thus one type 3 leg needs at most $O(L^7)$ cells in its expansion and at most $O(L^4)$ choices of levels. The type 2 cofactor uses $O(L^2)$ cells including its unit holes, and its physical interval $O(L)$. Its last-prime unit mask may be restored separately as in [R53](r53-source-retuned-exact-local-comparator.md) at pointwise cost $O(X^{3/4}L^2)$ in the signed integral, by removing at most one partner dividing $N$ and applying Cauchy. For type 3 all three unit masks are already exact in the cell expansion.

The other leg needs only integrated summed energy $O(XL^2)$ by Parseval. The multiplicity of each physical integer in the unrestricted type 3 polynomial is at most six, so its nonnegative coefficient is $O(L)$; the squared cell energies at fixed levels sum to no more than the squared energy with the cells combined. Type 2 has unique small/large roles. At fixed levels apply Bessel to the product integrals over the fixed $\mathfrak g$ and use (5) on a type 3 leg. The squared Cauchy cost of expanding both legs and summing over all level choices is at most $L^{14+8}=L^{22}$. Hence the maximal squared sum over integer targets is $O_{\rho,A,b}(X^3L^{30-Z})$. The optional type 2 partner reinstatement adds $O(X^{5/2}L^4)$, smaller. Markov at $X L^{-A}$ excludes only $O_{\rho,A,b}(X L^{-b})$ even targets. This proof keeps both moving hard physical windows and all exact prime-factor windows.

## 3. Subpower prime scales, local factors and moving weighted tails

For the ordered triple model group the first two primes as an unordered outer product $u$. Temporarily admit $u=q^2$ as well. The weight for a nonsquare outer product is exactly $w_{3,u}$, since there are two orders of the first two primes in the $1/6$ polynomial. For $u=q^2$ give the real model the factor $1/6$ instead of $1/3$. The real variable is the last factor at $p=t/u$, with the actual cutoff $p\le D$ implemented by the single interval endpoint $t\le uD$. The lower bound $p>\log N$ is automatic, even for the repeated outer factor. No extra endpoint needs a smoothing approximation.

On a classical arc about a reduced $a/d$, $d\le P$, apply the same effective-denominator calculation and reduced-residue [Siegel–Walfisz](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) input as in [R54](r54-source-central-triprime-comparator.md) §2, with $d_u=d/(d,u)$. On a nonempty type 3 physical window for fixed $u$, both relevant real prime prefixes have scale $Y=X/u$, with $\log Y\gg L/\log L$ from the fixed factor envelope or the estimate $u\le D^2$. Thus $d\le L^{6Z}\le(\log Y)^{6Z+1}$ eventually (increasing the fixed exponent by a further one would also suffice) and the theorem applies uniformly. Its exponential saving in $\sqrt{\log Y}$ implies arbitrarily strong fixed inverse-log errors in $L$. All relevant last primes exceed $P$. Including the $t\le uD$ endpoint does not increase the number of hard interval pieces. After partial summation and the major phase, the error can be made $O((X/u)L^{-F_1})$ with arbitrarily large fixed $F_1$: the $\log t$ weight costs at most a fixed logarithm, and the variation of the phase $e(\beta t)$ and the number of residue classes cost at most fixed powers of $P$. The total $\sum_u1/u\ll L^2$ suffices on the type 3 outer envelope. Last-prime exclusions dividing $N$ have cost at most $O(X L^2/Y_*)$ in the type 3 major transform: for each fixed prime $p\mid N$ in its band the number of possible ordered outer products is $O(X/p)$, each of weight $O(L)$. This cost absorbs any fixed logarithmic accuracy. The type 2 major treatment is unchanged. The resulting expansion (5) of [R54](r54-source-central-triprime-comparator.md) therefore holds with the new weights on all original hard windows. Total major length $O(P^3/X)$ permits arbitrary log accuracy also after multiplication and integration.

After summing reduced numerators the same signed coefficient $\Gamma_{u,v}(d;N)$ of [R54](r54-source-central-triprime-comparator.md) §2 is obtained. Its local algebra is unchanged even if $u=q^2$: any nonsquarefree $d$ is killed either by a Möbius factor at a prime not dividing $uv$, or by the prime-power Ramanujan zero at a prime of $uv$ because of the exact $N$-units. At squarefree $d$ the multiplicity of the prime in $u$ has no effect. The completed signed sum is precisely $\mathfrak S(N)\prod_{\ell\mid uv}\lambda_\ell$ at coprime pairs and zero at common-prime pairs. The absolute sum is uniformly $O(\mathfrak S(N))$ as before. In particular no positivity bound is substituted for cancellation of the shared-prime model.

For the type 3 real weight use a fixed dyad majorant $g_{3,u}=L/u$: its supremum and total variation on any hard central interval after zero extension are $O_\rho(g_{3,u})$, including the additional step at $uD$. Indeed $\log(t/u)\gg L/\log L$ on the support, and the ratio $\log t/\log(t/u)$ is monotone there. For type 2 keep $g_{2,u}=(\log u)/(uL)$. Uniformly for squarefree $k$,

$$
       \sum_{k\mid u} g_{i,u}\ll_\rho L^3/k
                                                               \tag{6}
$$

on the fixed cofactor envelopes for either type. For a single prime $k$, type 3 uses at most the reciprocal sum of the remaining prime times $L/k$; for a squarefree product of two primes there is at most one outer product. For larger squarefree $k$ there are none, and at $k=1$ the trivial harmonic bound $O(L^3)$ is sufficient. Prime squares in $u$ pose no change in (6), since $k$ here is squarefree. Thus the real Fourier tail extending from $|\beta|\le P/X$ to the real line costs $O_\rho(\mathfrak S(N)X L^6/P)$ by bounded variation and the absolute Euler factors. Full Fourier inversion gives the real integral of the local pair weights on $I$ exactly, because $N-I\subseteq I_0(N)$.

For the separate denominator tail use the absolute Rankin calculation of [R54](r54-source-central-triprime-comparator.md) §3 with (6). Noncommon special factors $1+\sqrt\ell/(\ell-1)$ are uniformly bounded over at most four primes. The common-prime factor is $\prod_{\ell\mid(u,v)}(1+\sqrt\ell)=\sum_{k\mid \operatorname{rad}((u,v))}\sqrt k$. By (6) its pair-weighted sum is $O(L^6\sum_k k^{-3/2})$. The rest of the Ramanujan absolute series, averaged over $N$, is handled by $\sum_{N\le2X}|c_h(N)|\le2X\tau(h)$ and the convergent half-power series exactly as before. The special Ramanujan values are fixed by the true units before dropping the moving masks in this average. It follows that the average weighted tail over the dyad is $O(L^6P^{-1/2})$, so the restored integral has error $O(X L^{-A})$ outside $O_{\rho,A,b}(X L^{-b})$ targets by Markov. These statements are uniform over all hard $I$.

The completed model with $u=q^2$ included differs from (1) by a genuinely negligible endpoint term: $\sum_{q\ge Y_*}g_{3,q^2}\ll L/Y_*$, so by the absolute local-factor bound its paired model mass is at most $O_\rho(\mathfrak S(N)X L^4/Y_*)$, smaller than every fixed inverse-log scale. Last-factor equality with an outer prime only affects the actual repeated triprimes already removed in §1; in a real profile it consists of finitely many points for each fixed outer product and does not change the integral. The exact full-torus count now has (2) for each pairing with type 3 by §§1–3. The $(2,2)$ pairing follows from [R53](r53-source-retuned-exact-local-comparator.md) on joining its exceptional set. No conclusions at individual exceptional moduli are required.

## 4. The moving-simplex limit and the signed residual

Write $L_N=\log N$, $r_N=(\log D)/L_N=\tfrac12-20/\log L_N+o(1/L_N)$ and $\xi=(\log t)/L_N=1+O_\rho(1/L_N)$ on $I_0(N)$. For the two ordered outer prime coordinates let $\alpha=(\log q)/L_N$, $\beta=(\log a)/L_N$, and define $\gamma=\xi-\alpha-\beta$ for the last prime's real scale. The actual profile condition is $\alpha,\beta,\gamma\le r_N$. Every coordinate is then at least $\delta_N=\xi-2r_N\gg_\rho1/\log L_N$, and tends into the simplex with all three coordinates at most $1/2$. The real mark factor is $\xi/\gamma$. Thus the prime reciprocal measures on any fixed compact exponent interval imply convergence of the clipped profiles on $\alpha,\beta,\gamma\ge\eta>0$ by Mertens and the absence of limiting mass on the finitely many boundary lines. The convergence is uniform in $t\in I_0(N)$ because all perturbations of these lines tend uniformly to zero.

Here is the necessary uniform integrability at all three moving edges. Chebyshev over ordinary prime dyads gives a reciprocal prime bound $O(w+L_N^{-1})$ on an exponent strip of width $w$ contained in a fixed positive exponent range. If $\alpha\le\eta$ for sufficiently small fixed $\eta$, then $\beta,\gamma> .3$ and the permitted $\beta$ interval has length at most $\alpha$, since its endpoints are $\xi-\alpha-r_N$ and $r_N$. The edge is bounded by

$$
  O\!\left(\sum_{\alpha\le\eta}\frac{\alpha}{q}
              +\frac1{L_N}\sum_{\alpha\le\eta}\frac1q\right)
          = O(\eta)+o(1),
$$

using $\sum_{q\le N^\eta}(\log q)/q\ll 1+\eta L_N$ and the prime reciprocal upper bound. The same holds for $\beta\le\eta$. For $\gamma\le\eta$ partition its range into dyads $\gamma\asymp w$ with $w\gg 1/\log L_N$. Both $\alpha,\beta$ must lie in strips of width $O(w)$ immediately below $r_N$. The two reciprocal masses and the real factor $O(1/w)$ give $O((w+L_N^{-1})^2/w)=O(w)$ per dyad; summing costs $O(\eta)$. All these bounds hold on the unconditioned prime envelopes, so also on the exact masks. Conversely omitting any prime divisor of $N$ from the two sampled axes has a uniformly negligible loss, by $q,a\ge Y_*$ and the inverse-exponential envelope, even using $L$ as the real ratio bound and $O(L)$ such exclusions. Omitting $q=a$ is negligible by the same repeated-outer estimate used after (6). This proves the uniform full profile limit, with no regularity at the three simplex corners assumed.

The limiting profile for the ordered $1/6$ model is therefore

$$
 \begin{split}
 c_3 &=\frac16 \int_0^{1/2}\int_{1/2-\alpha}^{1/2}
                    \frac{d\beta\,d\alpha}{\alpha\beta(1-\alpha-\beta)}\\
     &=\frac13\int_0^1-\log(1-x)
                           \left(\frac1x+\frac1{2-x}\right)dx
       =\frac13\left(\frac{\pi^2}{6}+\frac{\pi^2}{12}\right)
       =\frac{\pi^2}{12}.
 \end{split}                                                    \tag{7}
$$

For the first step after integrating $\beta$, set $x=2\alpha$; the two integrals then give the ordinary and alternating reciprocal-square sums, in the second using $1-x$ as variable. The unordered pair factor $1/3$ in (1) is exactly the two possible orders divided by six, not an additional normalization.

The type 2 profile tends uniformly to $c_2=\log2$ by [R52](r52-source-retuned-full-count-comparator.md) §4. All special local factors differ from one by $O(L_N^{-1})$ because there are at most four special primes and they exceed $\log N$. Common outer prime pairs cost $o(1)$ in the normalized model: at least one leg in the new pairings is type 3, so any such prime is $\ge Y_*$ and (6) bounds their summed profile weight by $O(L^6\sum_{\ell\ge Y_*}\ell^{-2})=o(1)$. For $(2,2)$ the analogous conclusion is already [R52](r52-source-retuned-full-count-comparator.md). These estimates yield (3) uniformly over hard $I$, and the actual alias signs stated above give (4). The constant $(\pi^2/12-\log2)^2$ is strictly positive. The untouched long–long sectors can still compensate this selected negative benchmark.
