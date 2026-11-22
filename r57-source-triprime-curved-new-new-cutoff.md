# The actual curved cutoff for two high-endpoint triprime legs

Fix $0<\rho<1/2$, $I_0(N)=[\rho N,(1-\rho)N]$, hard $I\subseteq I_0(N)$, and retain the exact units on $n+m=N$. Use the original cutoffs

$$
 j_N=\frac{\log N}{\log\log N},\qquad
 D=\lfloor\sqrt N e^{-20j_N}\rfloor,\qquad Q=\lfloor N e^{-20j_N}\rfloor,
 \qquad \theta=\frac{20}{\log\log N}.
$$

All the triprimes in this note are squarefree and have all prime factors $>\log N$. Let $H_1,H_2$ be the genuine nonadmissible endpoint types of [R56](r56-source-high-factor-triprime-mixed-endpoints.md): $H_1$ has one high prime $p>D$ and two low primes $q,a\le D$ with $qa>D$; $H_2$ has two high primes $p,r>D$ and one low prime $q\le D$.

For $i,j\in\{H_1,H_2\}$, denote by $\mathcal R_{ij,N}(I)$ the raw sum of the original coefficients on $n\in I,m\in I_0(N)$ of these types:

$$
 \mathcal R_{ij,N}(I)=
  -\!\!\sum_{\substack{n+m=N,\ \text{types }i,j\\n\in I,\ m\in I_0(N)\\
                                            (nm,N)=1}}
    \ \sum_{\substack{d\mid n,\ e\mid m\\ d>D,\ e>D,\ de>Q}}
       \mu(d)\mu(e)\log(n/d)\log(m/e).
                                                               \tag{1}
$$

The minus sign is the actual sum-alias sign. In particular (1) does **not** use the product of the separately summed long marks when both legs are new.

**Theorem (unconditional).** For any fixed $A,b>0$, with $L=\log X$, outside $O_{\rho,A,b}(XL^{-b})$ even $N\in[X,2X]$, uniformly and simultaneously in all hard $I$, the actual curved-cutoff sums satisfy

$$
 \begin{split}
 |\mathcal R_{ij,N}(I)|
 &\ll_{\rho,A,b}\mathfrak S(N)
       \bigl(|I|\theta\log(1/\theta)+N L^{-A}\bigr)
                &&\text{if at least one of }i,j\text{ is }H_1,\\
 |\mathcal R_{H_2,H_2,N}(I)|
 &\ll_{\rho,A,b}\mathfrak S(N)
       \bigl(|I|\theta^2+N L^{-A}\bigr).
 \end{split}                                                    \tag{2}
$$

In the second line the full unsigned weight of two $H_2$ legs is not used to estimate the two large logarithmic differences. Their exact surviving support under $de>Q$ is used.

As a consequence, the selected union of the [R53](r53-source-retuned-exact-local-comparator.md) double-admissible semiprimes and **all** zero-small squarefree triprimes has the signed raw line benchmark

$$
 -\mathfrak S(N)|I|
     \left((\pi^2/12-\log2)^2+o_\rho(1)\right)
       +O_{\rho,A,b}\bigl(\mathfrak S(N)N L^{-A}\bigr)
                                                               \tag{3}
$$

outside the same form of exceptional set, after joining the good sets of [R53](r53-source-retuned-exact-local-comparator.md), [R55](r55-source-all-small-triprime-comparator.md) and [R56](r56-source-high-factor-triprime-mixed-endpoints.md). This includes the actual $de>Q$ decisions throughout that selected union. It is not the whole long–long sector, a bound at each exceptional even integer, or Hypothesis S. The arithmetic theorem needs no GRH; using the separate long-divisor reduction to identify an original-operator component retains that reduction's assumptions.

## 1. Positive rectangle counts with uniformly moving factor intervals

We will use a consequence of the [R56](r56-source-high-factor-triprime-mixed-endpoints.md) polynomial proof that does not involve the cross-leg divisor cutoff. For each endpoint leg, retain its own exact arithmetic prime, unit, physical and one-high partner-product cuts from [R56](r56-source-high-factor-triprime-mixed-endpoints.md). Also allow arbitrary hard subintervals for each of its three prime slots, including the last prime; optionally distinguish the two high-prime labels on $H_2$. Allow the three possible positive weights $\log p$ on $H_1$ (its high prime), or $\log q$ or $L$ on $H_2$ (its low prime). The number $L=\log X$ is constant on the dyad. For unlabelled counts use the symmetric two-order polynomial with division by two. For prime-axis selections referring to an individual high label $p$ in $H_2$, use the ordered count of admissible choices without division by two. At most two choices occur for a fixed squarefree frequency. For the product of any two such endpoint legs, the **positive** full sum-line count, with no cross-leg $de$ mask, equals its explicit local comparator up to $O_{\rho,A',b}(\mathfrak S(N)X L^{-A'})$ for any fixed $A',b>0$, on one set outside $O_{\rho,A',b}(XL^{-b})$ targets, simultaneously over all the optional intervals. In the comparator each frozen pair product $u$ has real weight equal to its positive marker divided by $u\log(t/u)$, times its actual admissibility indicator and symmetry factor, and the same local factors and common frozen prime deletion as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md).

Here is why this further uniformity and the new pairing follow with no new prime distribution assumption. For a chosen partition level the extra prime intervals are on the three already existing prime axes of [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §2. They do not change the exact fourth/fifth axis for physical position and the one-high product cut. Cauchy in the partner integer, followed by summing over its ordered-factor and product cells (multiplicity at most two), gives the same joint energy bound $X^2L^{6-Z}$ on the fixed classical minor set; a constant dyad marker $L$ simply occupies the partner squared Cauchy factor. Take $Z=2A'+2b+110$ and the same $P=L^{6Z}$. The second leg, now also an endpoint leg, has integrated cell energy $O(XL^2)$ by bounded factorization multiplicity. Two endpoint legs have at most ten levels and at most $O(L^{16})$ expanded fixed-cell terms, so Cauchy then Bessel gives a total maximal squared sum $O(X^3L^{34-Z})$. Markov at $XL^{-A'}$ has the asserted exception bound. All prime argument cutoffs and units are still literal integer selectors. At most a bounded number of label conventions are used, and no dependence on an upper bound for the number of hard interval choices enters the maximal estimate.

For the major estimate, the optional last-prime interval intersects its usual interval with one hard subinterval, so the prime prefixes in Siegel–Walfisz and the bounded-variation real models of [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §3 are uniform in it. Added restrictions on either outer prime just remove some positive outer summands. The same effective denominator, local Ramanujan factors, uniform real tail and averaged denominator tails therefore apply. The heavy marker $L$ on $H_2$ has real weight at most $O(1/u)$, because the last prime is high and $\log(t/u)\gg L$. The temporary repeated-frequency removal costs at most $O(X^{.76}L^2)$ on the full line as before, uniformly even for labelled slots. This proves the stated positive rectangle estimate, including the common exceptional set. Its comparator is nonnegative and each local factor at most two; upper bounds may ignore common-factor exclusions and any omitted factor gates. Applying this result to a polylogarithmic number of rectangles below adds their error magnitudes, not their exceptional sets.

## 2. Pieces not requiring a double-toggle estimate

Every possible high factor in either type lies in the dyad-wide interval $[\sqrt X e^{-21J_X},\sqrt X e^{21J_X}]$, $J_X=L/\log L$, and on $H_2$ the low prime is at most $N/D^2\le \exp(CJ_X)$ for an absolute constant $C$. The reciprocal prime mass of the entire high interval is $O(J_X/L)$ by Chebyshev over ordinary dyads. The reciprocal mass of the low range is $O(\log L)$ by the prime harmonic bound. Thus the total real profile of an $H_2$ leg with heavy marker $L$ is $O(1)$ uniformly on the central interval: the real weights are $O(1/(qp))$ for an allowed low/high outer pair. The positive profile with marker $\log q$ is $O(\theta^2)$ by [R56](r56-source-high-factor-triprime-mixed-endpoints.md) §4. For $H_1$ the positive profile with marker $\log p$ is $O(\theta\log(1/\theta))$ by that same theorem. The absolute sum of the finitely many actual long-divisor marks on an $H_1$ leg is $O(\log p)$ because $p\gg X^{.49}$; on an $H_2$ leg it is $O(L)$. Hence whenever at least one leg is $H_1$, the absolute value in (1) is bounded by a constant times a positive uncut rectangle count with these marks. Section 1 and the profile bounds give the first line of (2). This is an upper bound on a larger positive count, not removal of a condition inside a signed identity.

For $H_2$--$H_2$ write the actual uncut one-leg long-mark vector, indexed by long divisors, as

$$
 -(\log q)(\delta_p+\delta_r-\delta_{pr})
       +(\log r)(\delta_{qp}-\delta_p)
       +(\log p)(\delta_{qr}-\delta_r).
                                                               \tag{4}
$$

Indeed the only nonzero positions are the two high primes, their product, and their products with $q$; the coefficients at $p,r$ are $-\log(qr),-\log(qp)$ and the three pair marks are their complementary logarithms. The full integer itself has logarithmic mark zero. Insert (4) on each side of the exact kernel $\mathbf1_{de>Q}$. Whenever at least one factor in the expansion comes from the first parenthesis in (4), its absolute contribution in the kernel is at most a fixed positive combination of weights $(\log q)L$ or its reflection on the actual pairs, including the low-low term. Thus §1 with the light and heavy profiles already bounds all such terms by $O(\mathfrak S(N)(|I|\theta^2+XL^{-A'}))$. No sign was used within those small-logged terms.

## 3. The remaining four double-toggle terms on the actual curved cutoff

Let $q,s$ be the low primes on the two $H_2$ legs. Choose one of the two high primes $p$ on the first leg and one $v$ on the second; there are four possible choices in the expansion (4). Their corresponding discrete differences are $(\delta_{qp}-\delta_p)$ and $(\delta_{sv}-\delta_v)$, with logarithmic multipliers $O(L)$ each. At $x=pv$ the kernel coefficient is exactly

$$
 T(x;q,s)=\mathbf1_{xqs>Q}-\mathbf1_{xq>Q}
                     -\mathbf1_{xs>Q}+\mathbf1_{x>Q}.
                                                               \tag{5}
$$

Set $a_0=\min(q,s)$ and $b_0=\max(q,s)$. Looking at $Q/x$ in the ranges below $1$, in $[1,a_0)$, in $[a_0,b_0)$, in $[b_0,a_0b_0)$ and above, (5) is respectively $0,-1,0,+1,0$. The convention at the rightmost boundary is that equality at $a_0b_0$ has value zero, as the inequalities are strict. Equivalently its exact support is the union of

$$
  \log x\in(\log Q-\log a_0,\log Q]
         \quad\text{or}\quad
  \log x\in(\log Q-\log(a_0b_0),\log Q-\log b_0].
                                                               \tag{6}
$$

Neither strip is replaced by the entire region $x>Q$ or the entire region $x<Q$. For an upper bound on each surviving absolute contribution, it is now permissible to cover these strips by hard rectangles in prime coordinates.

Partition the possible $\log q,\log s,\log p$ into half-open intervals of length one (last endpoints can be independently closed when needed), applying their genuine prime and unit ranges as well. Each axis has $O(J_X)$ boxes: the low bounds follow from the two high primes, and the high range is of logarithmic length $O(J_X)$. Fix three of these bins, say indices $i,j,k$. In the first range in (6), $\log v=\log x-\log p$ lies in one interval of length $O(1+\min(i,j))$, by taking the extreme endpoints for $q,s,p$ in their bins. In the second range both $\log(qs)$ and $\log b_0$ vary by at most two, and $\log p$ by at most one, so the same length bound holds there as well. Use both covering intervals, each intersected with the actual high range $v>D$ and its fixed envelope. They may depend on $N$ through $\log Q$, which is permitted in §1. This is an outward cover of the *exact* kernel (6), including its possibly included endpoints. It uses $O(J_X^3)$ products of hard prime-slot intervals. The frozen high label for each leg can be its selected $p$ or $v$ in the double toggle; the other high prime remains genuine and comes from the last-prime variable of the comparator. All masks $n\in I,\ m\in I_0$, true units, and high/low eligibility are retained in every count.

Apply §1 with the positive weight $L$ on both legs. Its main on a fixed box is at most

$$
 O_\rho(\mathfrak S(N)|I|)
     \left(\sum_{q\ {\rm in}\ i}\frac1q
           \sum_{p\ {\rm in}\ k}\frac1p\right)
     \left(\sum_{s\ {\rm in}\ j}\frac1s
           \sum_{v\ {\rm in\ its\ covering\ interval}}\frac1v\right),
                                                               \tag{7}
$$

since each relevant last prime is high; disregarding its cut in this comparator only increases (7). The possible labels count exactly an ordered high choice or overcount by at most a fixed factor, which is sufficient for the bound. The high reciprocal sum in the covering interval is $O((1+\min(i,j))/L)$ by Chebyshev across ordinary dyads at high prime scales. Summing the first high weight over $k$ costs $O(J_X/L)$. Thus the overall main is

$$
 \ll_\rho \mathfrak S(N)|I|\,\frac{J_X}{L^2}
       \sum_{\substack{q,s\ {\rm prime}\\q,s\le \exp(CJ_X)}}
              \frac{1+\min(\log q,\log s)}{q s}
 \ll_\rho \mathfrak S(N)|I|\,\frac{J_X^2}{L^2}.
                                                               \tag{8}
$$

For the last step, in $q\le s$ the inner sum $\sum_{q\le s}(\log q)/q\ll\log s$, and $\sum_{s\le\exp(CJ_X)}(\log s)/s\ll J_X$. The part from $1$ is $O((\log L)^2)=O(J_X)$, and the reflected order gives the same. The omitted original smaller/larger restrictions in this last positive harmonic upper bound do not affect its validity.

Sum the uniform error in §1 over the $O(J_X^3)$ covers for each of the four possible high-label pairings, taking $A'=A+5$. The total error is $O_{\rho,A,b}(\mathfrak S(N)X L^{-A})$ on the same good moduli. Since $J_X^2/L^2\asymp\theta^2$ on the dyad, (8), (5), and the small-log pieces in §2 give the second line of (2). The product cutoff throughout this deduction was kept in (5); only the support of its exact discrete difference was covered from outside by positive rectangles. No claim is made that either sign of (5) separately contributes its uncut mark.

## 4. What this completes among squarefree zero-small triprimes

A central squarefree triprime with an admissible giant has the form $n=pqa$ with $p>D$, $qa\le D$, and all three primes distinct. Its long divisors are exactly $p f$ for $f\mid qa$ (with the full-divisor term allowed and marked zero), since every divisor not containing $p$ is $\le D$. For every counterpart long divisor $e>D$, all of these $p f e$ exceed $pD\ge n\ge \rho N>Q$. Thus the actual curved-cutoff coefficient of this entire leg against **any** central counterpart is zero:

$$
         \sum_{f\mid qa}\mu(pf)\log(qa/f)=-\Lambda(qa)=0.
$$

This cancellation uses squarefreeness and two distinct cofactor primes; it does not assert zero for a prime-power cofactor. Every remaining central squarefree triprime is either the [R55](r55-source-all-small-triprime-comparator.md) all-small-prime class, or one of the two nonadmissible endpoint types $H_1,H_2$ with at least one high prime, by the actual admissibility classification in [R56](r56-source-high-factor-triprime-mixed-endpoints.md). Three high primes cannot occur. The mixed terms with [R53](r53-source-retuned-exact-local-comparator.md)/[R55](r55-source-all-small-triprime-comparator.md) are estimated in [R56](r56-source-high-factor-triprime-mixed-endpoints.md) and have total size $O(\mathfrak S(N)(|I|\theta\log(1/\theta)+NL^{-A}))$ on their good moduli; the new--new terms are now bounded by (2). Adding these $o(\mathfrak S(N)|I|)$ bounds and their uniform inverse-log remainders to the [R55](r55-source-all-small-triprime-comparator.md) signed two-class benchmark proves (3). The only selected semiprimes here are the [R53](r53-source-retuned-exact-local-comparator.md) type 2 legs; this does not classify all semiprimes or include higher-factor, repeated-cofactor, less-rough, or exterior terms.
