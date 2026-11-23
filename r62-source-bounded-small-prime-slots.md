# Bounded small-prime slots: exact curved cancellation on the central sum line

Fix $0<\rho<1/2$, a fixed $0<\kappa<1/4$, and a fixed integer $M\ge1$. Write $L_N=\log N$, $I_0=[\rho N,(1-\rho)N]$, and use the [R60](r60-source-fixed-rough-all-arities-dickman.md) thresholds

$$
 \theta_N=20/\log\log N,\qquad
 D=\lfloor \sqrt N e^{-\theta_N L_N}\rfloor,\qquad
 Q=\lfloor N e^{-\theta_N L_N}\rfloor.
$$

For even $N$, let $\mathcal T_{\kappa,M}(N)$ consist of squarefree central units $n=su$ where $s$ has $1\le j\le M$ distinct prime factors, all $\le\log N$, and $u$ has $r\ge1$ distinct prime factors, all $\ge N^\kappa$. These prime ranges are disjoint for sufficiently large $N$; no intermediate factors are allowed. The [R60](r60-source-fixed-rough-all-arities-dickman.md) selections $\mathcal F_\kappa,\mathcal B,\mathcal H_\kappa,\mathcal U_\kappa$ contain no small primes, so each is disjoint from $\mathcal T_{\kappa,M}$.

For hard $I\subset I_0$ use the exact negative sum alias

$$
 R_N(\mathcal D,\mathcal E;I)=
 -\!\sum_{\substack{n+m=N,\ n\in I\cap\mathcal D,\ m\in I_0\cap\mathcal E\\(nm,N)=1}}
 \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
       \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

All three cutoff inequalities are strict. No difference alias can occur on the two central coordinates.

**Theorem (unconditional).** Put $H_N=1+\log(1+\log\log N)$ and

$$
 \varepsilon_N=\frac{1+\log\log N}{\log N}\,H_N^{2M-1}.
$$

For every fixed $A,b>0$, writing $L=\log X$, outside $O_{\rho,\kappa,M,A,b}(XL^{-b})$ even targets $N\in[X,2X]$, simultaneously for every hard $I$ and every ordered pair with at least one $\mathcal T_{\kappa,M}$ leg and the other in $\{\mathcal T_{\kappa,M},\mathcal F_\kappa,\mathcal B,\mathcal H_\kappa,\mathcal U_\kappa\}$,

$$
 |R_N(\mathcal D,\mathcal E;I)|
   \ll_{\rho,\kappa,M,A,b}\mathfrak S(N)(|I|\varepsilon_N+NL^{-A}).
 \tag{2}
$$

Here $\mathfrak S(N)$ is the ordinary even binary singular series. Either added leg may be restricted to specified values of $j$ and $r$. Adjoining $\mathcal T_{\kappa,M}$ disjointly to any [R60](r60-source-fixed-rough-all-arities-dickman.md) selection does not change its leading coefficient in the [R60](r60-source-fixed-rough-all-arities-dickman.md) pairings. The small factors are present in the actual sequences, and the curved cutoff is not replaced by a rectangular one. Neither growing $M$ or varying $\kappa$, nor intermediate prime factors, nonsquarefree legs, exceptional targets, or Hypothesis S are covered.

## 1. Complete and partial small-divisor orbits

Let $n=su$ be an added leg. Fix an actual opposite $e\mid m$, $e>D$, and put $T_e=\max(D,Q/e)$. The exact test on $d$ is $d>T_e$. Since $e\ge D+1>\sqrt N e^{-\theta_N L_N}$ and $Q\le N e^{-\theta_N L_N}$, we have $D\le T_e\le\sqrt N$. Write $d=af$ uniquely with $a\mid s$, $f\mid u$. The $f=1$ orbit is empty since $s\le L_N^M<D$; the $f=u$ orbit is full since $u\ge\rho N/L_N^M>\sqrt N$. A partially included orbit therefore has a nonempty proper rough subset $f$, and can occur only when

$$
      f\le T_e<sf,\qquad
      \log f\in(\log T_e-\log s,\log T_e].
 \tag{3}
$$

The endpoint convention follows from the strict original tests. A full orbit has its signed mark

$$
 \mu(f)\sum_{a\mid s}\mu(a)\log(su/(af))=\mu(f)\Lambda(s).
 \tag{4}
$$

Indeed $\sum_{a\mid s}\mu(a)=0$ and $\sum_{a\mid s}\mu(a)\log(s/a)=\Lambda(s)$. This is zero at $j\ge2$, and is $\mu(f)\log q$ at $j=1$, $s=q$. A partial orbit is bounded by $O_M(L)$ on its support (3). When $u$ is one prime there are no proper rough subsets, so such a marked leg vanishes identically at $j\ge2$ against *every* opposite divisor. At $j=1$ its exact mark is $-\log q$, independently of $e>D$.

The [R58](r58-source-central-three-factor-first-order.md) prime and admissible-giant-with-composite-cofactor legs can also be deleted against every opposite divisor. A prime only has complementary log zero. If $m=ps'$ with $p$ its giant, $s'\le D$ squarefree composite, then $p\ge\rho N/D>\sqrt N$ eventually. All $pa$ with $a\mid s'$ pass both cutoffs against any $d>D$, and all other $m$-divisors are $\le D$. The signed sum is $-\Lambda(s')=0$. On the five other old classes $2,3,H_1,H_2,B$ of [R58](r58-source-central-three-factor-first-order.md), absolute long marks are bounded by a constant times their standard positive marks (use the heavy $L$ mark at $H_2$). The real profiles of those marks have uniformly bounded total on $I_0$ by [R58](r58-source-central-three-factor-first-order.md) §§1–3 and its [R56](r56-source-high-factor-triprime-mixed-endpoints.md)/[R57](r57-source-triprime-curved-new-new-cutoff.md) inputs. In particular old type 2 uses $\log q$, not $L$, at its possibly small positive cofactor $q>\log N$.

## 2. Positive hard-box comparison after adding the small slots

We use the [R60](r60-source-fixed-rough-all-arities-dickman.md) §1 positive full-sum-line comparison with its per-slot hard windows and both physical windows. The comparison itself has **no** divisor cutoff. We show that the added families with $r\ge2$, and $r=j=1$, can each serve on either side of this comparison, with a fixed common exceptional set and any fixed inverse-logarithmic error exponent. Other added arities already vanish in (1) by (4), so no positive estimate for them is required. On an added family use marker $L$ or, for $j=1$, marker $\log q$; include all ordered tuples with coefficient $1/(j!r!)$. An individual labelled configuration is bounded by a fixed multiple of this normalization. **Exact distinctness among the small slots on each side is imposed from the start**, not as a rare prime-square correction.

The comparison is, for arbitrary hard windows $I_1,I_2$, the positive real expression

$$
 \mathfrak S(N)
 \sum_{\substack{u_0,v_0\ {\rm frozen\ tuples}\\(u_0v_0,N)=1,\ (u_0,v_0)=1}}
 \prod_{\ell\mid u_0v_0}\frac{\ell-1}{\ell-2}
 \int_{I_1\cap(N-I_2)} w_{u_0}(t)w_{v_0}(N-t)\,dt
 \tag{5}
$$

up to $O_{\rho,\kappa,M,A',b}(\mathfrak S(N)NL^{-A'})$ for every fixed $A',b>0$, outside one $O_{\rho,\kappa,M,A',b}(XL^{-b})$ set for all boxes. Coprimality and Euler factors on the frozen tuples refer to their integer products. On an added leg freeze every factor except a rough last one. Its profile is

$$
 w_{u_0}(t)=\frac{\text{positive marker}}{j!r!\,u_0\log(t/u_0)}
     \mathbf1_{t/u_0\ {\rm in\ its\ last\ prime\ window}},
 \tag{6}
$$

with the tuple retained only when each frozen window, small-slot distinctness and unit condition holds. Old profiles have their usual weights and indicators. We use the upper bound of these positive profiles with bounded local factors, not any replacement of the factors by one.

**Minor arcs.** Use the fixed dyadic physical envelope $[\rho X/2,2X]$ and the classical major arcs of denominators $\le P=L^{6Z}$ and common half-width $P/X$. The fixed $Z$ may be arbitrarily large. In an added leg with $r\ge2$ designate one rough prime on scale $U$, grouping its complementary integer on scale $V=X/U$. Since at least one other factor is rough, $U,V\ll_\rho X^{1-\kappa}$. At fixed aligned dyadic levels for the other prime axes each complementary integer has at most $(j+r-1)!$ assignments across all their disjoint cells. Exact distinct-small-slot predicates can only reduce this multiplicity and do not constrain the primary prime; the marker (including $\log q$ when used) depends only on the complementary tuple. Use [R60](r60-source-fixed-rough-all-arities-dickman.md) §1 Cauchy in that integer before expanding squares, sum its disjoint partner cells, and then enlarge nonnegatively to the whole complementary integer interval. One obtains precisely the same primary-prime same-physical-cell sums as in [R60](r60-source-fixed-rough-all-arities-dickman.md). Its numerical bounds apply since $U,V\ll X^{1-\kappa}$ and $U/(XL^{-Z})=o(1)$, yielding joint cell energy $O(X^2 L^{6-Z})$. Repeats involving rough primes may provisionally be allowed just as in [R60](r60-source-fixed-rough-all-arities-dickman.md); this does not remove small-slot distinctness.

For $r=j=1$, use the low cofactor argument of [R53](r53-source-retuned-exact-local-comparator.md) §1 over $q\le\log(2X)$ (with an additional interval on the last-prime axis). Given minor $\alpha$, approximate $q\alpha$ by reduced $a/d$ with $d\le \lceil X/P\rceil$ and error $\le1/(d\lceil X/P\rceil)$. If $qd\le P$, the lift $a/(qd)$, reduced if necessary, puts $\alpha$ on the major arcs. Thus $d>P/q\gg L^{6Z-1}$. The last-prime scale is $Y\asymp_\rho X/q$. Apply Vaughan's estimate [Montgomery–Vaughan, Theorem 17.1](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) at the two hard endpoints, subtract prime powers and partially sum to unweighted primes, including the outer marker bounded by $L$. The single-cell bound is $O_\rho(X L^{-(6Z-1)/2+5}+X^{4/5}L^5)$. At fixed $q$, the sum of absolute cell counts is $O_\rho((X/q)L)$: each $qp$ belongs to only one pair of physical and last-prime cells at fixed levels. Multiply the supremum by this sum to bound the squared cell sum. Cauchy over $O(L)$ choices of $q$ and disjointness of cofactor cells give again $O(X^2L^{6-Z})$. The last-prime hard window is a single further axis. This handles the case with two such legs as well, without requiring a pointwise prime-pair theorem.

The partner joint energy integrated over the circle is $O(XL^2)$ by Parseval and bounded multiplicity, including the [R58](r58-source-central-three-factor-first-order.md) active families. Restore the hard intervals and target-unit holes by the [R60](r60-source-fixed-rough-all-arities-dickman.md) aligned-cell and Bessel argument. An axis with unit deletions has at most $O(L)$ missing indices (only prime divisors of $N$) and uses $O(L^2)$ dyadic cells; physical intervals use $O(L)$. Keep also the old $H_1$ product axis of [R56](r56-source-high-factor-triprime-mixed-endpoints.md). There are $O_{\kappa,M}(1)$ axes and a fixed power of $L$ cost for all cells of a given moving window and all level choices. Distinctness of small slots is fixed in the complementary coefficients, not a moving relationship between independent cell indices. The minor maximal squared sum at target frequency $N$ is $O(X^3L^{8-Z+O_{\kappa,M}(1)})$ by Bessel and the two joint energy estimates. Choose $Z$ sufficiently large and use Markov, uniformly over both physical windows, all factor windows and their hard endpoints.

**Major arcs.** Freeze the indicated tuple. The actual phase on the last prime at reduced $a/d$ has denominator $d/(d,u_0)$. Use [Siegel–Walfisz](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) at this reduced denominator as in [R60](r60-source-fixed-rough-all-arities-dickman.md) §1 and [R53](r53-source-retuned-exact-local-comparator.md) §2. All added last primes are $\ge X^\kappa$; old last primes obey the already-used lower bound $\log(t/u_0)\gg_\rho L/\log L$. Thus a fixed power of $L$ is bounded by a fixed power of the last prime logarithm. One can demand any fixed inverse-log accuracy before the polylog losses from residue sums, hard partial summation, the arc phase and the fixed number of outer harmonic sums. Omission of a last prime dividing $N$ costs $O(X^{1-\kappa}L^{O_{\kappa,M}(1)})$ for new families, since it determines the complementary product at $O(X/p)$ possible integer indices, and each has bounded tuple multiplicity. The old deletion at its subpower lower bound costs $O(XL^{-C})$ for every fixed $C$. Frozen unit holes in the small slots remain exact.

If repeats among rough factors were provisionally admitted, their actual integers have $p^2\mid n$ for some $p\ge X^\kappa$; there are $O(X^{1-\kappa})$ of them, each with bounded tuple count and only one opposite integer on the full sum line. Correct these on the full coefficient, not by pretending their Fourier transforms have no minor part. In the real model repeated frozen rough slots lose a power by reciprocal-square mass, and equality with the last rough slot is null for fixed frozen tuple. For old repeats use [R58](r58-source-central-three-factor-first-order.md)/[R60](r60-source-fixed-rough-all-arities-dickman.md). No small-slot repetition was ever admitted in the new families.

Summation over reduced numerators gives

$$
 c_d(N)\frac{\mu(d/(d,u_0))\mu(d/(d,v_0))}
                   {\varphi(d/(d,u_0))\varphi(d/(d,v_0))}.
$$

Nonsquarefree denominators give zero by a Möbius factor or a Ramanujan prime-power zero at an $N$-unit special prime. At a squarefree common special prime the complete local multiplier $1+c_\ell(N)$ is zero. At a singly frozen prime it is $1+1/(\ell-1)$, so division by the ordinary factor gives $(\ell-1)/(\ell-2)$. No frozen prime is 2 since $N$ is even and the exact units are kept. All remaining factors are positive and bounded by $2^{O_{\kappa,M}(1)}$.

For the tails put $g_{u_0}\ll L/u_0$ per frozen tuple, so $\sum_{h\mid u_0}g_{u_0}\ll L^{O_{\kappa,M}(1)}/h$ for squarefree $h$, assigning prescribed primes to the bounded number of slots and summing remaining reciprocal weights by harmonic sums. The real Fourier tail past $P/X$ is $O(XL^{O_{\kappa,M}(1)}/P)$ by bounded variation, including the hard steps. For the denominator tail use the half-power Rankin factor of [R60](r60-source-fixed-rough-all-arities-dickman.md). The ordinary part has finite mean by $\sum_{N\le2X}|c_d(N)|\le2X\tau(d)$ and convergence of $\sum_d d^{1/2}\tau(d)/\varphi(d)^2$. The noncommon special factors are bounded, and the common ones are $\prod_{\ell\mid(u_0,v_0)}(1+\sqrt\ell)=\sum_{h\mid\operatorname{rad}((u_0,v_0))}\sqrt h$. The double prescribed-divisor bound makes their weighted contribution converge with $\sum_h h^{-3/2}$. In taking the positive upper average envelope, drop the moving masks only *after* using the unit conditions to fix the special Ramanujan factors. The averaged normalized tail is $O(L^{O_{\kappa,M}(1)}P^{-1/2})$, independent of any box choice. Markov gives the uniform denominator error after increasing $Z$. There are only fixed finitely many families of arities and markers, and the two tails, minor bound, and major real approximation give (5) on their joined good set.

## 3. Outward bound on the exact thin partial-orbit support

For a heavy added profile with $j$ small slots and $r\ge2$, its total real weight at any $t\in I_0$ is $O_{\rho,\kappa,M}(H_N^j)$ using (6), the fixed-$\kappa$ lower bound on the last denominator, bounded reciprocal mass on the rough axes, and

$$
 \sum_{q\le L_N}\frac1q\ll H_N,\qquad
 \sum_{q\le L_N}\frac{\log q}{q}\ll 1+\log L_N
 \tag{7}
$$

over primes. A single small slot with light $\log q$ marker has profile $O_{\rho,\kappa}((1+\log L_N)/L)$, also at $r=1$. The [R60](r60-source-fixed-rough-all-arities-dickman.md) rough partners have bounded heavy profiles; the old partners were discussed in §1. If the partner is also added, delete its $r'=1,j'\ge2$ case by (4) applied to it first. Use its heavy $L$ marker at $r'\ge2$ and its exact light mark at $r'=j'=1$. In the latter case only the giant divisor has a nonzero individual long term. Together these bound the absolute opposite-divisor weights by a constant times the corresponding positive marker, with real total $O(H_N^{j'})$ when the partner has $j'$ small slots. Use $j'=0$ otherwise.

Full-orbit terms in (4) vanish for $j\ge2$. For $j=1$ bound their absolute value by the positive count (5) with light $\log q$ on the designated added side and the just-described partner marker. The cutoff is still kept in (4) before this upper bound. The estimate is $O(\mathfrak S(N)(|I|(1+\log L_N)H_N^{j'}/L+NL^{-A}))$.

For partial terms fix a nonempty proper rough subset label $f$ and an opposite divisor label $e$. There are only boundedly many labels. Partition the prime logs into half-open unit bins on both sides. In any fixed opposite box $\log e$ varies by $O_{\kappa,M}(1)$. The threshold log $z\mapsto\max(\log D,\log Q-z)$ is $1$-Lipschitz. For fixed opposite bins and own small-slot bins, (3) therefore puts $\log f$ in one outward interval of width at most $\log s+O_{\kappa,M}(1)$: take upper ends of the own small bins and account for the opposite threshold variation. Include every own rough unit box meeting this interval. Such inclusion enlarges its effect on $\log f$ by at most a further bounded constant. This is an outward **majorization**, not an identification of the actual curved indicators with those boxes.

For fixed real physical $t$ in (6), substitute $\log p_r=\log t-\log s-\sum_{i<r}\log p_i$ for the last rough log. If this last slot is absent from $f$, some frozen rough coordinate in $f$ has coefficient $+1$ in $\log f$. If it is present, some frozen rough coordinate outside $f$ has coefficient $-1$. Hence conditional on all other frozen factors the chosen rough log lies in a single interval of length $\log s+O_{\kappa,M}(1)$. At polynomial scales a unit log interval has reciprocal prime mass $O_\kappa(1/L)$ from Chebyshev on the enclosing fixed-ratio interval. Partition longer logs into unit lengths for the uniform bound $O_\kappa((1+\log s)/L)$. Last-prime support and all residual window restrictions can only reduce this positive upper bound.

Summing over the included own bins does not duplicate real factors, since a real last argument and each frozen prime lie in unique half-open bins. By (7) the small-slot reciprocal sum with the width factor is bounded by

$$
 \sum_{q_1,\ldots,q_j\le L_N}
       \frac{1+\sum_i\log q_i}{q_1\cdots q_j}
   \ll_M (1+\log L_N)H_N^{j-1},
$$

where disregarding distinctness only enlarges this bound. The remaining rough reciprocal masses and the marker-to-last-log ratio in the heavy profile are bounded. Sum the partner real profiles over their unit bins; the sum restores their unsplit profile, preserving in particular the old $H_1$ product flag and the true type-2 marker. Bounding the positive local factors of (5) by a constant now gives total partial main upper bound

$$
 O_{\rho,\kappa,M}\!\left(
    \mathfrak S(N)|I|\frac{1+\log L_N}{L}H_N^{j-1+j'}\right).
$$

The number of all labelled box pairs is $L^{O_{\kappa,M}(1)}$, and $A'$ can be increased by a fixed amount to absorb their comparison errors. Every selected partial orbit was bounded using its actual exact support, and not by discarding the signs of complete orbits.

This proves (2) when the added leg is first since $j-1+j'\le2M-1$, and the exponent for full terms uses $j=1$. For the reflected orientation, use the exact equality $R_N(\mathcal D,\mathcal E;I)=R_N(\mathcal E,\mathcal D;N-I)$; the hard reflected interval remains central with the same length. The two-added-leg block is included by the single designated orbit, with no separability assumption on the curved boundary. Expand the disjoint unions on the joined [R60](r60-source-fixed-rough-all-arities-dickman.md) and present good sets. The original external minus sign in (1) never changes. The result is a central density-one estimate for the stated classes; identification with a component of the original operator still uses that separate reduction's own assumptions.
