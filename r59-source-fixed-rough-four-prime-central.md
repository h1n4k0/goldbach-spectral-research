# Fixed-power rough squarefree four-prime legs on the actual central sum line

Fix $0<\rho<1/2$ and $0<\kappa<1/4$. For sufficiently large even $N$ put $I_0=[\rho N,(1-\rho)N]$, let $I\subseteq I_0$ be any hard interval, and use the exact retuned thresholds

$$
 L_N=\log N,\quad \theta_N=\frac{20}{\log\log N},\quad
 D=\lfloor\sqrt N e^{-\theta_N L_N}\rfloor,\qquad
 Q=\lfloor N e^{-\theta_N L_N}\rfloor .
$$

Consider two disjoint classes of central legs: the squarefree zero-small legs with at most three prime factors of [R58](r58-source-central-three-factor-first-order.md), and the genuine squarefree four-prime legs whose every prime factor is at least $N^\kappa$. In both classes keep $(n,N)=1$. Define $\mathcal R_{\kappa,\le3\cup4,N}(I)$ to be the signed sum on $n+m=N$, $n\in I$, $m\in I_0$, for pairs in this union with the actual inner mark

$$
 -\sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
       \mu(d)\mu(e)\log(n/d)\log(m/e).
                                                               \tag{1}
$$

The minus is the original central sum-alias sign. The four-prime restriction does not mean that all squarefree four-prime integers are included.

**Theorem (unconditional).** Put $L=\log X$ and $\Delta=\pi^2/12-\log2$. For every fixed $A,b>0$, outside $O_{\rho,\kappa,A,b}(X L^{-b})$ even $N\in[X,2X]$, uniformly and simultaneously for every hard $I$,

$$
 \mathcal R_{\kappa,\le3\cup4,N}(I)
     =-\mathfrak S(N)|I|(\Delta+c_{4,\kappa})^2
      +O_{\rho,\kappa,A,b}\!\left(\mathfrak S(N)
                 \bigl(|I|\theta_N+N L^{-A}\bigr)\right),       \tag{2}
$$

where $\mathfrak S(N)$ is the ordinary even binary singular series and

$$
 c_{4,\kappa}
  =\frac1{24}
     \int_{\substack{x_1+x_2+x_3+x_4=1\\
                    \kappa\le x_i\le1/2\ (1\le i\le4)}}
     \frac{\min(2\min_i x_i,1-2\max_i x_i)}
          {x_1x_2x_3x_4}\,dx_1\,dx_2\,dx_3 \ >0 .             \tag{3}
$$

This is the leading benchmark for this selected sector, not a first-order expansion in $\theta_N$. It excludes the exceptional even targets, any four-prime leg having a factor $<N^\kappa$, higher-factor, repeated-factor, less-rough and exterior sectors. It makes no assertion about the full long--long operator or Hypothesis S. The arithmetic is unconditional; the separate long-divisor reduction for the original operator keeps its own assumptions.

## 1. Genuine positive box counts for a four-prime leg

We first prove the analytic input used for bounding exact masks. Allow optional hard intervals in all four prime slots of a four-prime leg, and in its physical index. Use all labelled ordered prime factors with weight $L/24$, initially allowing repeats. The positive full sum-line count against another such leg, or any old positive marked leg of [R58](r58-source-central-three-factor-first-order.md), admits its exact real local comparator with error $O_{\rho,\kappa,A',b}(\mathfrak S(N)X L^{-A'})$ for arbitrary fixed $A',b>0$, outside one set of size $O_{\rho,\kappa,A',b}(X L^{-b})$, uniformly over all these optional hard intervals and those of the old leg. For a squarefree frequency each complete ordered four-prime collection has total weight $L$; the factor $1/24$ is used even in a single labelled box. The positive old markers used are $\log u$ on type 2, $\log n$ on type 3 and the both-high semiprime, $\log p$ on $H_1$, and either $\log q$ or $L$ on $H_2$. Their exact selector and symmetry factors are those of [R55](r55-source-all-small-triprime-comparator.md)--[R58](r58-source-central-three-factor-first-order.md).

Here are the details of this extension of the [R56](r56-source-high-factor-triprime-mixed-endpoints.md)/[R57](r57-source-triprime-curved-new-new-cutoff.md) prime-axis argument. Use fixed dyad-wide physical envelope $[\rho X/2,2X]$, each four-prime slot in $[X^\kappa,2X^{1-3\kappa}]$, and the classical reduced arcs of denominator $d\le P=L^{6Z}$ and common half-width $P/X$, with $Z=2A'+2b+120$. Their complement $\mathfrak g$ has a reduced Dirichlet approximant with $P<d\ll X/P$ and approximation error $\le d^{-2}$. These arcs are only for a full-circle count. Group the first prime $p$ as primary and the partner integer as the product $m$ of the other three primes. For a primary dyad of scale $U$, the partner scale is $V=X/U$. At fixed levels of the three partner axes, each $m$ has at most six ordered assignments total over their disjoint cell combinations, by unique prime factorization as a multiset. For each combination use Cauchy in $m$, with its bounded multiplicity in the outer factor, giving $O_\rho(VL^2)$ times a nonnegative sum of unmarked primary-prime squares on its actual partner support. Sum over all the partner cells **before** enlarging this nonnegative $m$ sum to all integers of scale $V$. There is at most the factor six just noted, and no loss of a cancellation in the enlarged calculation.

Expand these squares and sum over the disjoint physical cells at each fixed physical level. For $p'=p+h>p$ the exact common-floor factor is

$$
 1-hm/H+\psi((p+h)m/H)-\psi(pm/H),\qquad
       \psi(x)=\{x\}-1/2,\quad hm<H,
$$

with $H$ the physical cell length, just as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md). Positive $h$ are at most $O(H/V)$ and negative differences are conjugate. Now the diagonal is $O(UV^2L^2)$. Group the $h$'s into $O(G)$ intervals of length at most $d/2$, $G=1+U/d$. The grouped sum of truncated reciprocal distances from zero is $O_\rho(G(V+dL))$, including the nearest phase per group. This gives the affine bound $O(UVL^2G(V+dL))$. With $Y_0=X L^{-Z}$ the raw off-diagonal for $H<2Y_0$ is $O(XH L^2)$; for $H\ge2Y_0$ use Fejér degree $K=\lfloor H/Y_0\rfloor$ and the discrete endpoint-inclusive [R56](r56-source-high-factor-triprime-mixed-endpoints.md) error. For fixed $h$, primeness of $p$ and $p+h$ bounds the multiplicity of their grid products by $O(L)$ even after enlarging $m$. Thus that error costs $O(X^2L^{4-Z})$. In the nonzero modes the shift satisfies $k U/H\le U/Y_0=o(1)$. Near the phase zero, spacing gives $O(G(1+dkU/H))$ choices of $h$, with sum over $p$ bounded by $O_\rho(V+(H/k)L)$; outside this range use at least half the former distance from zero. The same bound as [R56](r56-source-high-factor-triprime-mixed-endpoints.md) is consequently

$$
 O_\rho\!\left(VL^2
       \{G(VL+HL+dUVK/H+dU L^2)+UG(V+dL)L\}\right).
$$

The change in the primary exponent upper bound is harmless: $XU\ll X^{2-3\kappa}$, $V\ll X^{1-\kappa}$, $H=O(X)$, $GdUV^2K/H\le(d+U)V L^Z$, and $GdUV=X(d+U)$. All terms are $O_{\rho,\kappa,A',b}(X^2L^{4-Z})$ per ordinary primary dyad. The $O(L)$ dyads add at most $L^2$ by Cauchy. This proves joint cell energy $O(X^2L^{6-Z})$ uniformly on $\mathfrak g$ for each choice of integer levels.

For the other leg the integrated joint energy is $O(XL^2)$ by Parseval using the bounded multiplicity of a prime-factor multiset. This applies to all the old leg types as well, with their additional exact axes such as the $H_1$ partner-product window. At most five integer axes are used per leg. Each factor axis, with optional interval and unit holes, uses $O(L^2)$ aligned cells; the physical and any extra product axis use $O(L)$ cells. Therefore the two-leg expansion uses at most $O(L^{18})$ fixed-cell terms and $O(L^{10})$ choices of levels. Cauchy then Bessel over integer Fourier outputs gives maximal squared sum $O(X^3L^{36-Z})$. The old type 2 last-prime unit can be kept by its own axis or restored by its [R53](r53-source-retuned-exact-local-comparator.md) Cauchy bound. Markov at $XL^{-A'}$ leaves the claimed exceptional set. This gives the actual signed contribution from $\mathfrak g$ even though the full count and its major model are nonnegative.

On the classical major arcs freeze the other three prime coordinates of the four-prime model, writing their product $u$. The last prime lies in its genuine hard interval, intersects the physical interval divided by $u$, and has polynomial size at least $X^\kappa$. Apply reduced-residue [Siegel--Walfisz, Theorem 12.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) at effective denominator $d/(d,u)$ exactly as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md)/[R55](r55-source-all-small-triprime-comparator.md). All prime arguments exceed the major denominator, the phase variation is $O(P)$, and the frozen reciprocal prime weights sum to $O_\kappa(1)$ (a polynomial logarithm would suffice). Thus the substitution of the real profile

$$
  \frac{L}{24\,u\log(t/u)}
       \mathbf1_{\{t/u\ \text{in its chosen last-prime interval}\}}
                                                               \tag{4}
$$

with the frozen factors restricted to their optional exact windows has arbitrary inverse-log uniform error after multiplying and integrating. Here frozen factors are ordered, so there can be at most six labels for a product $u$. The physical interval is in the real integral. A last prime dividing $N$ costs only a power saving pointwise on the arcs: for each such prime $p\ge X^\kappa$ there are $O(X/p)$ possible partner-product indices, at most six ordered assignments and weight $O(L)$, and there are $O_\kappa(1)$ such exclusions. All frozen units are already in the profiles. The old last-prime computations and their harder subpower ranges are unchanged from [R53](r53-source-retuned-exact-local-comparator.md), [R55](r55-source-all-small-triprime-comparator.md), [R56](r56-source-high-factor-triprime-mixed-endpoints.md) and [R58](r58-source-central-three-factor-first-order.md).

For a pair of outer products $u,v$ the signed coefficient after reduced numerators is the [R56](r56-source-high-factor-triprime-mixed-endpoints.md) coefficient
$c_d(N)\mu(d/(d,u))\mu(d/(d,v))/(\varphi(d/(d,u))\varphi(d/(d,v)))$.
It has zero completed sum for any common frozen prime; otherwise the sum is $\mathfrak S(N)\prod_{\ell\mid uv}(\ell-1)/(\ell-2)$. The same argument applies even to temporarily repeated factors of $u,v$: nonsquarefree $d$ is killed by a Möbius zero or a Ramanujan prime-power zero because those frozen primes are exact $N$-units. There are at most six special primes in a pair, so the absolute series is still $O(\mathfrak S(N))$. For clarity the tails are uniform here: for the new real weights take $g_u=C_\kappa L/u$ per frozen ordered triple, larger than their supremum and variation on any chosen hard interval. For squarefree $k$,
$\sum_{k\mid u}g_u\ll_{\rho,\kappa} L^4/k$ on fixed envelopes, by summing the remaining (at most three) prime reciprocals, with at most a bounded ordered multiplicity. The old legs satisfy the same weaker bound. The real Fourier tail is $O(\mathfrak S(N)XL^8/P)$ by bounded variation. In the denominator tail insert $d^{1/2}/P^{1/2}$ and split off the special primes. Common special factors contribute $\prod_{\ell\mid(u,v)}(1+\sqrt\ell)=\sum_{k\mid\operatorname{rad}((u,v))}\sqrt k$, whose weighted sum is $O(L^8\sum_k k^{-3/2})$. Noncommon factors are bounded; the remaining mean over $N$ uses $\sum_{N\le2X}|c_h(N)|\le2X\tau(h)$ and the convergent ordinary half-power series, after fixing the special Ramanujan values by the actual unit masks. This bounds the **average** absolute denominator tail by $O(L^8P^{-1/2})$, so Markov finishes each full-circle comparator uniformly over the hard slots. These exceptional sets do not multiply by the number of slots. As usual the last prime is a real variable only in (4), not in the actual count.

We may remove analytic repetitions from the full count, uniformly: at an integer with a repeated prime $\ell\ge X^\kappa$, the possible frequencies number $O(X\sum_{\ell\ge X^\kappa}\ell^{-2})=O(X^{1-\kappa})$. The opposite integer on the sum line is determined and both marks are $O(L)$. In the real model repeated frozen primes lose at most $O_\kappa(X^{-\kappa}L^C)$ in profile by their reciprocal-square sum, and equality of a frozen prime with the last real argument affects a null set only. Repetitions of any old partner are corrected as in its proof. Consequently the asserted positive box input holds for the actual squarefree four-prime choice.

## 2. Keeping the real divisor product decisions

For a given $N$ partition each labelled four-prime logarithm into hard intervals of length one. These give $O(L^4)$ boxes, with the exact cut at $N^\kappa$ and exact units on each slot. Write $\theta=\theta_N$ temporarily. Use as stable boxes those for which every point satisfies both:
* every singleton log is below $(1/2-2\theta)L_N$;
* every two-element log sum lies outside $[(1/2-2\theta)L_N,(1/2+2\theta)L_N]$.

For true physical products and sufficiently large $N$ all triple divisors in a stable box are $>N^{1/2+\theta}$ (a triple is the complement of a singleton in $\log n=L_N+O_\rho(1)$). Every stable pair divisor is exactly short or long according to its sign relative to $L_N/2$, and any long one exceeds $N^{1/2+\theta}$ as well. All singletons are short. Thus the retained divisor set is precisely the genuine $d>D$ set, not a model truncation. In products against **any** counterpart $e>D$ under consideration, the genuine nonzero stable $d$ always satisfies $de>Q$, using the margins relative to $D$ and $Q$. So on the stable portion it is legal to multiply separately summed long marks.

Away from stable boxes, an actual four-prime leg is either an admissible giant with identically zero curved contribution, or it has a singleton or a pair-subset exponent within $3\theta+O(1/L_N)$ of $1/2$. Indeed any singleton above $1/2+3\theta$ gives $n/p<D$ and $pD>Q$. For such an admissible giant all long divisors are $pf$ with $f\mid n/p$, and $pf e>Q$ for any $e>D$; its complete sum is $-\Lambda(n/p)=0$, since the complement has three distinct prime factors. The remaining failure of the stable labels produces the stated boundary strips because the log boxes have width one. One can outwardly cover the full boundary by all boxes meeting these strips, increasing log widths by $O(1)$ only. This upper cover need not exclude the already zero orbits.

The boundary strip has small **actual** jointly weighted mass on the good moduli. An arbitrary four-prime leg has absolute total long mark $O(L)$; every old leg with a nonzero orbit is covered by the corresponding positive marker from §1, up to a fixed constant, and its total positive real profile is $O_\rho(1)$ by [R55](r55-source-all-small-triprime-comparator.md)--[R58](r58-source-central-three-factor-first-order.md) (use the heavy $L$ marker for $H_2$). The total four-prime positive profile is $O_{\rho,\kappa}(1)$ from (4) and prime reciprocal mass on its polynomial bands. For a fixed real physical $t$, put $x_j=\log p_j/L_N$ for the three frozen prime variables, and substitute $x_4=\log t/L_N-x_1-x_2-x_3$. For any singleton or pair-subset, its log-exponent linear form is nonconstant in at least one frozen $x_j$, with coefficient $1$ or $-1$. If the subset includes the last slot, take any frozen slot outside it; if it does not, take a slot inside it. Therefore under the strip restriction one frozen prime lies in an exponent interval of length $O(\theta+L_N^{-1})$ for each choice of the others. By Chebyshev over ordinary prime dyads, its reciprocal mass is $O_\kappa(\theta+L_N^{-1})$, and the two other frozen reciprocal masses are $O_\kappa(1)$. The factor $L/\log(t/u)$ in (4) is bounded in terms of $\kappa$. Summing the positive models over the disjoint labelled boundary boxes costs only $O_{\rho,\kappa}(\theta)$ for their profile. Shared frozen prime deletion and additional opposite gates can be removed for this upper bound. Thus §1 with $A'$ larger than $A+9$ bounds the contribution of every boundary pairing, with the **original** curved weights, by

$$
 O_{\rho,\kappa,A,b}\bigl(\mathfrak S(N)
                   (|I|\theta+NL^{-A})\bigr).
                                                               \tag{5}
$$

This is an absolute upper bound by larger positive counts on the boundary, not an assertion that the product cutoff is automatic there.

## 3. The stable signed mark and its continuum value

For stable $n$ write $y_i=\log p_i/\log n$ so that the four $y_i$ sum to one. Each complementary pair of two-element divisor indexes has one long member. All four triple divisors have Möbius sign $-1$ and total mark $-\log n$. The long member of a two-element complementary pair contributes the smaller of the two complementary log sums, times $\log n$. Thus the actual separately summed stable mark is $\log n$ times

$$
 -1+\sum_{\text{three complementary pairings}}
             \min(y_i+y_j,1-y_i-y_j)
          =\min(2\min_i y_i,\ 1-2\max_i y_i).                  \tag{6}
$$

To verify the last equality, sort the exponents as $a\le b\le c\le d$. The three smaller sums are $a+b,a+c,\min(a+d,b+c)$. The left side becomes $a-d+\min(a+d,b+c)$, which is the claimed minimum. Stable marks are nonnegative. In unnormalized logs the mark is $\min(2\min_i\log p_i,\ \log n-2\max_i\log p_i)$, a function of the four logs that varies by $O(1)$ within a unit-log box.

Use a constant representative for this mark on each stable box, multiplying the positive weight $L$ in §1 by the representative divided by $L$. Its absolute size is bounded uniformly. The pointwise mark error is $O(1)$; in the actual stable sum line, the error against any other active mark on the other leg is at most $O(1/L)$ times the corresponding positive weighted count. In the real model the same Lipschitz bound holds with the last real prime argument on its box. Thus the total error of this replacement, summed over all relevant stable box pairs, is $O(\mathfrak S(N)(|I|/L+NL^{-A}))$ on the same good sets. The relevant model coefficients are the exact signed local factors of §1; in replacing them by $\mathfrak S(N)$ times the product of the single-leg profiles the $\lambda_\ell$'s all change by $O(1/\log N)$ and there are at most six. A common frozen prime in any such pairing is $\ge X^\kappa$ from the four-prime leg, and its omitted comparator weight is bounded by $O(L^8\sum_{\ell\ge X^\kappa}\ell^{-2})$ using the divisor-mass estimates of §1. This is negligible at the scale of (5).

Let $a_4(t)$ be the resulting signed stable one-leg real profile, using the actual real logs in the marker. Uniformly in $t\in I_0$,

$$
                    a_4(t)=c_{4,\kappa}+O_{\rho,\kappa}(\theta).
                                                               \tag{7}
$$

Indeed use reciprocal prime measure in the three frozen exponents and the real last exponent $x_4=\xi-x_1-x_2-x_3$, $\xi=\log t/L_N=1+O_\rho(L_N^{-1})$. The weight is the exact mark of (6) divided by the last prime logarithm, and the frozen masses are $1/p_i$. For fixed $\kappa$ all relevant exponents lie in a compact interval bounded away from zero. Excluding a prime divisor of $N$ from any frozen slot costs $O_{\rho,\kappa}(X^{-\kappa})$ there, since there are at most $O_\kappa(1)$ such exclusions. Replacing the real stable label region by $x_i\ge\kappa$, $\max x_i\le1/2$, and ignoring the pair-boundary hyperplanes costs $O_{\rho,\kappa}(\theta+L_N^{-1})$ in both discrete and continuous profiles. This is the same strip bound as in §2, and the same argument handles the $O(L_N^{-1})$ perturbation of the real last exponent and lower endpoint when replacing $\xi$ by one. Within the common domain the weights are uniformly bounded and Lipschitz, including the min and max in (6), so the perturbation of the value itself costs $O_{\rho,\kappa}(L_N^{-1})$.

On the fixed limiting domain with compact positive exponent ranges, prime Mertens gives uniform discrepancy $O_\kappa(L_N^{-1})$ for the reciprocal prime mass of a hard exponent interval against $dx/x$. For a quantitative comparison split the three frozen exponent axes into intervals of side $L_N^{-1/10}$. The finitely many boundary hyperplanes have total discrete and continuous mass $O_{\rho,\kappa}(L_N^{-1/10})$ by the one-free-coordinate strip estimate. Elsewhere the weights vary by $O_{\rho,\kappa}(L_N^{-1/10})$ per grid box; the discrepancy summed over all $O(L_N^{3/10})$ boxes is $O_\kappa(L_N^{-7/10})$ even using the crude discrepancy bound per box. These errors are $o(\theta)$ uniformly. At $\xi=1$ the mark factor becomes the numerator of (3), divided by $x_4$ for the last prime density; the other three reciprocal prime measures supply the other denominators and the ordered normalization is $1/24$. This proves (7). Finiteness follows from $x_i\ge\kappa$; strict positivity follows from a neighborhood of $x_1=x_2=x_3=x_4=1/4$, where the integrand is positive, for any fixed $\kappa<1/4$.

## 4. Combining only the selected sectors

The old signed benchmark for pairs of two legs of at most three factors is [R58](r58-source-central-three-factor-first-order.md), and its signed one-leg comparator profile is $\Delta-2\theta+O_\rho(\theta^2\log(1/\theta))$. For paired terms with one stable four-prime leg, product-cutoff automaticity was checked in §2, so this old profile adds with exactly the old signs even for the endpoints $H_1,H_2$ and the both-high semiprime. The old prime and admissible-giant triprime orbits are exactly zero, as in [R58](r58-source-central-three-factor-first-order.md). For two stable four-prime legs use the signed mark (6) on both. All missing four-prime interactions either vanish as a true orbit or are bounded by (5). Therefore the additional four-prime terms have leading coefficient
$-\mathfrak S(N)|I|(2\Delta c_{4,\kappa}+c_{4,\kappa}^2)$, with error $O_{\rho,\kappa,A,b}(\mathfrak S(N)(|I|\theta+NL^{-A}))$. The uniform positive box error used in this assembly can be taken at exponent $A+12$ in §1, since two four-prime label boxes contribute at most $O(L^8)$ finitely many selections; there is no extra union of exceptions for intervals or boxes. Joining the old [R58](r58-source-central-three-factor-first-order.md) good set proves (2). None of the other operator sectors are controlled by this completion.
