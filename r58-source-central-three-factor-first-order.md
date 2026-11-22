# The first-order signed benchmark for every squarefree zero-small leg with at most three prime factors

Fix $0<\rho<1/2$, $I_0(N)=[\rho N,(1-\rho)N]$ and any hard $I\subseteq I_0(N)$. On the sum line retain only pairs whose two integers are coprime to the modulus. Use the original retuned labels

$$
 j_N=\frac{\log N}{\log\log N},\qquad
 D=\lfloor\sqrt N e^{-20j_N}\rfloor,\qquad
 Q=\lfloor N e^{-20j_N}\rfloor,\qquad
 \theta=\frac{20}{\log\log N}.
$$

Let $\mathcal R_{\le3,N}(I)$ be the negative sum-alias contribution on $n+m=N$, $n\in I$, $m\in I_0(N)$, restricted to squarefree $n,m$ with at most three prime factors each, all primes $>\log N$. Thus its actual divisor summand is

$$
 -\!\sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
                 \mu(d)\mu(e)\log(n/d)\log(m/e).
                                                               \tag{1}
$$

**Theorem (unconditional).** Put $\Delta=\pi^2/12-\log 2>0$ and $L=\log X$. For every fixed $A,b>0$, outside $O_{\rho,A,b}(XL^{-b})$ even integers $N\in[X,2X]$, uniformly over all hard $I$,

$$
 \begin{split}
 \mathcal R_{\le3,N}(I)
   &=-\mathfrak S(N)|I|\,(\Delta^2-4\Delta\theta)\\
   &\quad
     +O_{\rho,A,b}\!\left(\mathfrak S(N)
            \bigl(|I|\theta^2\log^2(1/\theta)+NL^{-A}\bigr)\right).
 \end{split}                                                    \tag{2}
$$

All terms with higher factor count, repeated prime factors, prime factors at most $\log N$, and coordinates outside the central range remain outside this statement. In particular this is not the full long--long block, a pointwise assertion about exceptions, or Hypothesis S. Identifying this with a component of the original operator via the separate long-divisor reduction still requires that reduction's own assumptions.

## 1. The additional squarefree semiprime type

A central prime has zero long mark, since its only possible long divisor is the integer itself. For a squarefree semiprime at least one prime factor exceeds $D$, because $D^2<\rho N$. If there is exactly one such high prime, this is type 2 of [R53](r53-source-retuned-exact-local-comparator.md), with true long mark $-\log u$ and long divisor at least $\rho N/D$. The new semiprime type $B$ has **both** factors $u,p>D$. Its long divisors with nonzero marks are $u,p$, with summed mark $-\log n$. Their actual product cutoff is automatic only against types 2 and 3 of [R55](r55-source-all-small-triprime-comparator.md), each of whose nonzero long divisors on either leg is $\ge\rho N/D$.

Use the positive mark $\log n$ for type $B$ in counts; allow both orders with factor $1/2$. Its frozen prime is the high prime $u$, and the real profile for it is

$$
      w_{B,u}(t)=\frac{\log t}{2u\log(t/u)}
                   \mathbf1_{t/u>D},\qquad u>D,\quad (u,N)=1.
                                                               \tag{3}
$$

At nonempty support the frozen and last primes both lie in the same fixed high band of [R56](r56-source-high-factor-triprime-mixed-endpoints.md) on the dyad. On this symmetric ordered count omit $u=p$ on the actual full line: the difference involves at most $O(X^{1/2})$ frequencies, each with weight $O(L)$ and exactly one possible opposite integer. The error against any selected leg is $O(X^{1/2} L^2)$. Real equality changes only a single point per fixed $u$. The analytic ordered normalization is unchanged.

We use the following positive-count version of (3): for a type $B$ leg against any of types $2,3,H_1,H_2,B$, the uncut positive full count has the exact local comparator with arbitrary fixed inverse-log error and exception exponent as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md), uniformly in optional hard prime-slot windows and both original hard physical windows. For $H_2$ one may use positive marker $L$ or $\log q$ and labelled high slots, as in [R57](r57-source-triprime-curved-new-new-cutoff.md). To check this extension, group either of the two high primes of $B$ as the primary variable and the other prime as its integer partner, and split $\log n/2$ into two separate logarithmic marks. Cauchy in the partner and summation over its disjoint hard cells precedes enlargement to all partner integers. There are now only two prime axes and one physical axis for this leg. The floor-cell minor proof of [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §2 applies at every primary scale $X^{.4}\ll U\ll X^{.6}$ with $V=X/U$, giving its $O(X^2 L^{6-Z})$ joint energy. The other leg needs only the $O(XL^2)$ integrated Parseval bound by bounded multiplicity, including the older [R55](r55-source-all-small-triprime-comparator.md) ordered triple count and optional prime cuts. If a type 2 last-prime subinterval is specified, add a hard integer axis for that prime. Its partner-factor uniqueness gives the same integrated bound; even with this axis there are no more levels or expansion terms than in [R57](r57-source-triprime-curved-new-new-cutoff.md) §1. Exactly as there, this gives the signed classical minor error outside the desired common exceptional set. The actual selector on each prime axis includes its own $N$-unit deletions; the type 2 last-prime exception may be restored by its separate [R53](r53-source-retuned-exact-local-comparator.md) Cauchy estimate.

On the classical major set use Siegel–Walfisz on the true last high prime $p$ at the effective denominator $d/(d,u)$ as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §3. The optional last-prime cut is just one further hard interval restriction, and the new profile (3) has bounded variation $O_\rho(1/u)$, including its hard steps, since $\log p\gg L$. Its special prime factors in the exact Ramanujan model obey the same signed common-prime zero and the same weighted absolute Rankin bound: for squarefree $k$ the fixed weights satisfy $\sum_{k\mid u}g_{B,u}\ll L^3/k$, even with the coarse $g_{B,u}=L/u$. The other factors, real Fourier tail, signed Euler factors and uniformity are precisely the argument of [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §3 and [R57](r57-source-triprime-curved-new-new-cutoff.md) §1. Thus the new positive comparator is (1) of [R56](r56-source-high-factor-triprime-mixed-endpoints.md) with the additional weight (3), and variable prime-slot intervals are kept exactly. Summed repeated integers, including repetitions on an ordered old leg, cost only the earlier power-saving full-line corrections.

Its total profile, uniformly in $t\in I_0(N)$, satisfies

$$
        a_B(t):=\sum_{u}w_{B,u}(t)=4\theta+O_\rho(\theta^2).
                                                               \tag{4}
$$

Indeed write $L_N=\log N$, $d=(\log D)/L_N=1/2-\theta+o(L_N^{-1})$, $\xi=(\log t)/L_N=1+O_\rho(L_N^{-1})$. On nonempty support the exponent of $u$ lies in $(d,\xi-d)$. The factor $\log t/(2\log(t/u))$ is $1+O_\rho(\theta)$ uniformly, and the reciprocal prime mass of this interval is $\log((\xi-d)/d)+O(L_N^{-1})=4\theta+O_\rho(\theta^2)$ by prime Mertens. Prime divisors of $N$ in this high band have negligible reciprocal mass (at most $O(L_N/D)$); endpoints are also covered by the same uniform error. This proves (4).

## 2. Sharpening the actual curved endpoint pairs to second order

The three endpoint types are $B,H_1,H_2$. Their positive profile magnitudes at their usual signed-mark sizes are respectively $O(\theta)$, $O(\theta\log(1/\theta))$, and $O(\theta^2)$ by (4) and [R56](r56-source-high-factor-triprime-mixed-endpoints.md). The crude heavy profile of $H_2$ with constant marker $L$ is only $O(1)$, not $o(1)$, as in [R57](r57-source-triprime-curved-new-new-cutoff.md). We show that the actual coefficient (1) from **all pairs of endpoint types** is

$$
 O_{\rho,A,b}\!\left(\mathfrak S(N)
        \bigl(|I|\theta^2\log^2(1/\theta)+NL^{-A}\bigr)\right).
                                                               \tag{5}
$$

Except for pairs with $H_2$, simple positive products suffice, because the absolute sum of long marks on $B$ is exactly $\log n$ and on $H_1$ is $O(\log p)$ (its high prime $p$). Thus $B$--$B$, $B$--$H_1$ and $H_1$--$H_1$ are bounded by their positive uncut counts with profile products $O(\theta^2)$, $O(\theta^2\log(1/\theta))$ and $O(\theta^2\log^2(1/\theta))$, respectively. Here the true $de>Q$ is upper-bounded by a larger positive count; it is not assumed automatic. The actual $H_2$--$H_2$ term is $O(\theta^2)$ at profile scale by the double-toggle argument of [R57](r57-source-triprime-curved-new-new-cutoff.md).

For $T$--$H_2$ with $T=B$ or $H_1$, use the actual vector of [R57](r57-source-triprime-curved-new-new-cutoff.md) §2 on $H_2$, writing its low prime as $s$ and high primes as $v,w$. The part with factor $\log s$ is bounded in absolute value by the positive light count, with profile at most $O_\rho(\theta^2 a_T(t))$ when $T$ is at physical position $t$. It remains to keep the cancellations in the two differences $\delta_{sv}-\delta_v$ and $\delta_{sw}-\delta_w$, whose scalar weights are $O(L)$. Fix one such high label $v$ and a long divisor label $d_0$ on the $T$ leg. The actual curved difference is nonzero only when

$$
     \mathbf1_{d_0sv>Q}-\mathbf1_{d_0v>Q}\ne0
       \quad\Longleftrightarrow\quad
       \log v\in(\log Q-\log d_0-\log s,\ \log Q-\log d_0].
                                                               \tag{6}
$$

This follows directly from the strict inequality in (1) and keeps the included boundary.

For a chosen $T$-divisor label partition all its prime factor logarithms into unit-length half-open bins, as well as $\log s$. There are $O(L^4)$ combinations. Since $\log d_0$ is the sum of the logs of a fixed subset of the prime labels, its variation in a bin is at most three. The possible interval in (6) for $\log v$ therefore admits one outward covering interval of length at most $\log s+O(1)$ uniformly in the bin, intersected with the genuine high range. Its location is allowed to depend on $N$ and the bins. In $H_2$ choose the switched high prime $v$ as the frozen high label; the other high prime is genuinely prime and is still restricted to be high. Keep all cuts in each positive rectangle other than the outward enlargement of (6). The genuine optional factor windows are covered by the preceding positive-count statements ([R57](r57-source-triprime-curved-new-new-cutoff.md) for $H_1$--$H_2$, §1 here for $B$--$H_2$). Use the positive marker of $T$ and the marker $L$ for the $H_2$ leg to bound the absolute logarithmic multipliers.

In each box the latter leg's positive real weight is at most a constant times

$$
 \sum_{s\ {\rm in\ its\ bin}}\frac1s
   \sum_{v\ {\rm in\ the\ covering\ window}}\frac1v
       \ \ll_\rho\
 \sum_{s\ {\rm in\ its\ bin}}\frac{\log s+1}{s L}.
                                                               \tag{7}
$$

The inequality uses the high scale $v\gg X^{.49}$ and a dyadic Chebyshev bound on its hard interval. As $s\le N/D^2=\exp(O(L/\log L))$, summing (7) gives $O(1/\log L)=O(\theta)$, by $\sum_{p\le z}\log p/p\ll\log z$. On the $T$ leg the sum of positive real profiles over its factor bins is exactly its undivided profile (or at most a fixed multiple with labelled orders), for each real $t$: both frozen factors and the real last-prime argument lie in one bin each. In particular the bin sum keeps the intrinsic $qa>D$ in $H_1$ and does not lose its smaller profile. The ordinary local factors are bounded by a constant times $\mathfrak S(N)$ for every box. Thus the total main upper bound over boxes is

$$
 O_\rho(\mathfrak S(N)|I|\theta \sup_{t\in I_0(N)} a_T(t)),
$$

also in the reflected orientation. This is $O_\rho(\mathfrak S(N)|I|\theta^2\log(1/\theta))$ or smaller. Use the uniform positive estimate at error exponent $A+6$ so $O(L^4)$ outward boxes cost only $O(\mathfrak S(N)NL^{-A})$ on the same good moduli. Summing over the boundedly many divisor and high labels proves (5). No distinction of the two large curved indicators has been discarded without the exact support (6).

## 3. Quantitative cancellation of the two triprime profiles

Write $a_i(t)=\sum_u w_{i,u}(t)$ for the exact positive one-leg real profiles of [R53](r53-source-retuned-exact-local-comparator.md)/[R55](r55-source-all-small-triprime-comparator.md)/[R56](r56-source-high-factor-triprime-mixed-endpoints.md) and §1. Uniformly on the central range, the type 2 prime cofactor profile from [R52](r52-source-retuned-full-count-comparator.md) §4 satisfies the sharper expansion

$$
       a_2(t)=\log 2-2\theta+O_\rho(\theta^2),
                                                               \tag{8}
$$

by inserting $\log D=(1/2-\theta)L_N+o(1)$ in its explicit formula and using $\log t=L_N+O_\rho(1)$. For $H_2$ we need only the $O_\rho(\theta^2)$ bound established in [R56](r56-source-high-factor-triprime-mixed-endpoints.md).

For the all-small-prime triprime (type 3), define its continuum profile at cap $d$ by

$$
 F(d)=\frac16\int_{\substack{\alpha+\beta+\gamma=1\\
                       0<\alpha,\beta,\gamma\le d}}
                   \frac{d\alpha\,d\beta}{\alpha\beta\gamma}.
                                                               \tag{9}
$$

The real parameter cap in $a_3(t)$ is $d/\xi$ after rescaling all three exponents by $\xi=(\log t)/L_N$; the mark factor $\xi/\gamma$ and the reciprocal measures make this an exact rescaling of the continuum. The cap is $1/2-\theta+O_\rho(L_N^{-1})$. The discrete profile is $F(d/\xi)+o_\rho(\theta^2)$, as can be verified quantitatively without an unproved asymptotic at a moving prime endpoint. Indeed all allowed exponents before rescaling have minimum $\xi-2d\gg\theta$. On any such exponent interval the prime reciprocal measure differs from its integral $d\alpha/\alpha$ by $O(1/(\theta L_N))$, uniformly, by prime Mertens. For a fixed first prime exponent $\alpha$, the last reciprocal factor $\xi/(\xi-\alpha-\beta)$ as a function of $\beta$ is monotone and has supremum and variation $O_\rho(1/\theta)$. The first prime-measure replacement costs $O_\rho(1/(\theta^2 L_N))$ for each $\alpha$. Its sum costs $O_\rho(\log(1/\theta)/(\theta^2 L_N))$ since the first prime reciprocal mass is $O(\log(1/\theta))$. After this inner integration the function of $\alpha$ is

$$
 \frac{2\xi}{\xi-\alpha}
            \log\frac{d}{\xi-\alpha-d}
         \quad\text{on }[\xi-2d,d].
$$

It is monotone increasing and has supremum/variation $O_\rho(\log(1/\theta))$, so the second measure replacement is also negligible. As in [R55](r55-source-all-small-triprime-comparator.md), unit deletions and identical outer primes cost inverse-exponentially in $L/\log L$ because all contributing individual exponents are $\gg\theta$. Thus the errors are $o_\rho(\theta^2)$ even after all hard edges are included.

For $1/3<d<1/2$ the derivative in (9) is the equal contribution of three moving faces. Their equality uses that switching a coordinate with $\gamma$ has Jacobian of absolute value one. At $\alpha=d$ the face interval is $1-2d\le\beta\le d$. Therefore, writing $d_s=1/2-s$,

$$
 \frac{d}{ds}F(d_s)
       =-\frac{1}{d_s(1-d_s)}\log\frac{d_s}{2s}.
$$

For instance this follows directly by differentiating each face cut for $d<1/2$, where every coordinate is bounded away from zero. By the [R55](r55-source-all-small-triprime-comparator.md) integral $F(1/2)=\pi^2/12$; the derivative is integrable at $s=0$. Using $[d_s(1-d_s)]^{-1}=4+O(s^2)$ and $\log(d_s/(2s))=\log(1/(4s))+O(s)$ gives

$$
   a_3(t)=\frac{\pi^2}{12}
             -4\theta\bigl(\log(1/(4\theta))+1\bigr)
             +O_\rho(\theta^2).
                                                               \tag{10}
$$

The $O(1/L_N)$ perturbation in the cap contributes only $O_\rho(\log(1/\theta)/L_N)$ by the same derivative.

For $H_1$, refine [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §4 by removing exponent edges $\min(\alpha,\beta)\le\theta^3$ before replacing the two prime measures. The same Chebyshev bound there costs $O_\rho(\theta^3+\log L_N/L_N)$; the two Mertens errors cost $O_\rho(\log(1/\theta)/(\theta^3 L_N))$, and unit exclusions on the retained exponents and repeated outer factors are negligible. Thus this profile differs by $o_\rho(\theta^2)$ from its continuum. Its ordered-pair $1/2$ normalization and exponent strip $d<\alpha+\beta<d+w$, $w=\xi-2d$, give the exact continuous formula

$$
     \int_0^w \frac{\log(d/y)}{d+y}\,dy .
$$

Indeed first put $y=\alpha+\beta-d$ and integrate over $y\le\alpha\le d$. Replace $w$ by $2\theta$ since the derivative at $w\asymp\theta$ costs only $O_\rho(\log(1/\theta))$ times the $O(L_N^{-1})$ displacement. Then replacing $(d+y)^{-1}$ by $d^{-1}$ and integrating explicitly gives

$$
 a_{H_1}(t)
     =4\theta\bigl(\log(1/(4\theta))+1\bigr)
                 +O_\rho\!\bigl(\theta^2\log(1/\theta)\bigr).
                                                               \tag{11}
$$

Thus both the $\theta\log(1/\theta)$ and linear $\theta$ losses in (10) are restored by the actual $H_1$ marker. Including the signed $H_2$ magnitude $O(\theta^2)$ proves

$$
       a_3(t)+a_{H_1}(t)-a_{H_2}(t)
       =\frac{\pi^2}{12}+O_\rho\!\bigl(\theta^2\log(1/\theta)\bigr).
                                                               \tag{12}
$$

## 4. Signed assembly

The full classification on the stated squarefree support is exact. The two semiprime types are 2 and $B$, and a prime leg contributes zero. For triprimes the all-small-prime class, $H_1$, and $H_2$ exhaust the nonadmissible possibilities. The remaining admissible giant $p$ has squarefree cofactor $qa\le D$ with two primes; its entire long orbit $p f$ ($f\mid qa$) satisfies $p f e>Q$ against every counterpart long $e>D$, and sums to $-\Lambda(qa)=0$ by [R57](r57-source-triprime-curved-new-new-cutoff.md) §4. Its possible mark at the divisor equal to the integer is zero. No other eligible squarefree factor-count class is removed by this cancellation.

For the paired terms with at least one type 2 or type 3, the product cutoff is automatic by the lower bound $\rho N/D$ for that side's nonzero long divisors. Use the exact local comparators of [R53](r53-source-retuned-exact-local-comparator.md), [R55](r55-source-all-small-triprime-comparator.md), [R56](r56-source-high-factor-triprime-mixed-endpoints.md) and §1 for these pairings. In replacing them by $\mathfrak S(N)$ times the product of the single profiles, the factors $\lambda_\ell$ all differ from one by $O(1/L_N)$ and there are at most four per pair. The excluded common cofactor primes contribute $o(\theta^2)$ uniformly in this real model: if a type 3 cofactor is present, its support primes are at least $\exp(37L/\log L)$ and the divisor-mass bound $\sum_{\ell\mid u}g_{i,u}\ll L^3/\ell$ suffices after summing $\ell^{-2}$. For type 2 against another type 2 the same loss is $O(L_N^{-1})$ by direct diagonal summation. For type 2 against $H_1$ or $H_2$ it is $O((\log L_N)/L_N)$, exactly as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md) (the other real weight traces are $O(L/\ell)$ at a prescribed prime, while $w_{2,\ell}=O((\log\ell)/(\ell L_N))$). Type 2 and $B$ outer primes cannot coincide because the cutoff separates them. Thus all errors in these real product comparisons are $o(\mathfrak S(N)|I|\theta^2)$ uniformly.

All remaining endpoint products are already bounded, with their exact cutoff, by (5). Also the product of any two of their **ordinary** signed profiles is $O_\rho(\theta^2\log^2(1/\theta))$, since the signed-profile magnitudes are $a_B,a_{H_1},a_{H_2}$. It follows that the entire coefficient is

$$
 -\mathfrak S(N)\int_I f_N(t) f_N(N-t)\,dt
  +O_{\rho,A,b}\bigl(\mathfrak S(N)(|I|\theta^2\log^2(1/\theta)+NL^{-A})\bigr),
\qquad
 f_N=a_3+a_{H_1}-a_{H_2}-a_2-a_B .
$$

The signs inside $f_N$ are the actual long-mark signs; the external minus is the actual sum alias. Substituting (4), (8) and (12) gives $f_N(t)=\Delta-2\theta+O_\rho(\theta^2\log(1/\theta))$ uniformly on $I_0(N)$, proving (2) on the union of the required good sets. The untouched higher-factor and other operator contributions are not controlled by this sign computation.
