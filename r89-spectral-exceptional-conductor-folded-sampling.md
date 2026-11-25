# The actual exceptional left term has a divisibility-sampled second moment

**Scope.** This is an unconditional estimate for the genuine exceptional correction of [the all-scale reduction](r87-spectral-all-scale-exceptional-left-reduction.md#2-treat-only-the-left-arithmetic-on-the-excluded-arcs). No external zero-gap input is used. On a progression of **multiples** of an integer $K$, the saving is in the part of the actual exceptional conductor outside $K$. It removes the term on an ambient density-one family of even targets on every dyad, and, in contrast to ambient log-density estimates, gives a sufficient test relative to sparse planted families. It does not give a bound at prescribed targets, and it need not save when the exceptional conductor is supported almost entirely on the planting integer. The result concerns the signed mixed-composite strip, not prime-pair counts or Hypothesis S.

Keep the true $M_\pm$, $I,\omega$, and all parameters of that reduction: $Y\le N\le2Y$, $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $\Delta=2Q_0/Y$, $D=\sqrt N(\log N)^{-B}$, $H_0=\sqrt N(\log N)^{-B_0}$, with fixed admissible $B>B_0>0$. We take $\|\omega\|_\infty+\mathrm{Var}_I(\omega)\le1$ without loss by homogeneity. Write $e(t)=e^{2\pi it}$. If the Page zero exists, its primitive real character has conductor $r\le Q_0$, zero $\beta>1-4a_0/\sqrt G$, and real gap $b=1-\beta$. As in R87, put $\mathfrak E_\pm=0$ when it does not exist. In the case it does exist, for induced characters $\chi_q$ and Gauss sums $\tau_q(\chi_q)$, write the actual correction as

$$
 \mathfrak E_\pm(N;I,\omega)=
 \int_{\mathbb R/\mathbb Z}
       A(\theta)V_{I,\omega,\beta}(\eta(\theta))
              \widehat M_{\pm,N}(\theta)e(-N\theta)\,d\theta ,
 \quad
 V_{I,\omega,\beta}(\eta)=\int_I\omega(u)u^{\beta-1}e(\eta u)\,du .
 \tag{1}
$$

Here $A(\theta)=-\tau_q(\chi_q)\chi_q(a)/\varphi(q)$ on the auxiliary arcs $\theta=a/q+\eta$, $q\le Q_0,\ r\mid q,\ (a,q)=1,\ |\eta|\le\Delta$, and is zero outside them. The arcs are disjoint for large $Y$; their zero-weight arcs may be omitted. Thus (1) is exactly R87 (2), not the hard replacement of R88, and not a surrogate in which the right arithmetic is modeled.

**Theorem.** Uniformly over positive integers $K$ with $4KQ_0^3<Y$, for some fixed $C$ and in the case the zero exists,

$$
 \sum_{\substack{Y\le N\le2Y\\K\mid N,\ 2\mid N}}
       \ \sup_{I,\omega,\pm}|\mathfrak E_\pm(N;I,\omega)|^2
 \ \ll\ \frac{Y^{2\beta+1}}{K}\,G^C\,\frac{(r,K)}r .
 \tag{2}
$$

In particular, writing $g=(r,K)$, for each fixed $A>0$ the number of these actual targets where some correction exceeds $YG^{-A}$ is at most

$$
 \ll \frac YK\,G^{C+2A}e^{-2bG}\frac{g}{r}.
 \tag{3}
$$

All these statements are about the exact moving cutoffs and the supremum is over the actual tests. No assumption on the support of the character in a prescribed planting set is made in (2).

## 1. Fold the exceptional arcs over sampled frequencies

Write $t=q/(q,K)$. The image of the center $a/q$ under multiplication by $K$ is a reduced fraction $a'/t$; this includes $t=1$. Distinct reduced image centers on the torus, all of denominators at most $Q_0$, have distance at least $Q_0^{-2}$. Each image arc has radius $K\Delta$, so the images from distinct centers are disjoint by $4KQ_0^3<Y$. At a fixed output point in an image arc, the nonzero preimages $\theta$ from the exceptional arcs come only from this one image center. For a particular $q$, the map on reduced numerators is reduction to $t$ followed by multiplication by the unit $K/(K,q)$ modulo $t$. This reduction is surjective by the CRT and each fiber has precisely $\varphi(q)/\varphi(t)$ lifts. From each original arc there is just one possible point above the output point, since multiplication by $K$ is injective on that arc. Boundary overlaps of measure zero are irrelevant.

The Gauss induction identity used in R87 gives $|\tau_q(\chi_q)|\le\sqrt r$ (it vanishes unless $q=rv$ with squarefree $v$ coprime to $r$). Consequently at every output point the total squared left multiplier of its nonzero preimages is bounded by

$$
 \begin{split}
 \sum_{\theta:\,K\theta=\psi}|A(\theta)|^2
 &\le \frac{r}{\varphi(t)}
                     \sum_{\substack{q\le Q_0\\ r\mid q}}\frac1{\varphi(q)}
 \ \ll\ \frac{r\log(2Q_0)}{\varphi(r)\varphi(t)}
 \ \ll\ G^{C_0}\frac{g}{r}.
 \end{split}
 \tag{4}
$$

For the middle inequality use $\varphi(rv)\ge\varphi(r)\varphi(v)$ and $\sum_{v\le X}1/\varphi(v)\ll\log(2X)$, as in R87. For the last inequality, $r/g\mid t$ follows prime by prime from $r\mid q$; in particular $t\ge r/g$. The bounds $u/\varphi(u)\ll\log(2u)$ for $u=r,t\le Q_0$ suffice. There is no need for $K$ to be squarefree.

For any $F\in L^2(\mathbb R/\mathbb Z)$, its sampled coefficients $\int F(\theta)e(-kK\theta)d\theta$ are the ordinary coefficients of the push-forward density $K^{-1}\sum_{\theta:\,K\theta=\psi}F(\theta)$. The following specializes Parseval to $F=A H$, with $H\in L^2$. Apply Cauchy at each $\psi$ using (4), then change variables on the $K$ inverse branches; the latter contributes exactly one factor $K$:

$$
 \begin{split}
 \sum_{k\in\mathbb Z}
       \left|\int A(\theta)H(\theta)e(-kK\theta)d\theta\right|^2
 &=
   \frac{1}{K^2}\int
     \left|\sum_{\theta:\,K\theta=\psi}A(\theta)H(\theta)\right|^2d\psi\\
 &\ll \frac{G^{C_0}}K\frac{g}{r}
                   \int_{\{A\ne0\}}|H(\theta)|^2d\theta .
 \end{split}
 \tag{5}
$$

In particular this estimate does not pay the index $K$ after normalization by the number of sampled targets. Counting preimages without the squared Gauss weights would not yield (4).

## 2. Use the actual moving coefficient and all hard tests

For the right polynomial use the same canonical dyadic decomposition as [the common-complement proof](r85-spectral-unconditional-planted-ap-good-dyads.md#3-the-two-actual-arc-complements). Each true squarefree tuple $m=abcd$ has arithmetic labels $m,ab,ac,abc$, all positive integers at most $4Y$. Retain the exact fixed square-root gate, pairwise coprimality, its weight $\mu(b)\mu(c)(1-2\log(ac)/\log m)$, and the true parity. Then the moving physical interval, lower gates at $D$, and upper-strip gate at $H_0$ select unions of canonical rectangles over these four axes. The term “upper strip” here imposes $abc>H_0$. The integer interval for each axis is decomposed into $O(G)$ canonical intervals, preserving its exact strict or weak endpoints. At fixed right dyadic levels the rectangles $C$ partition the underlying tuples, so for their fixed right polynomials $\widehat M_C$,

$$
 \sum_C\|\widehat M_C\|_{L^2(\mathbb R/\mathbb Z)}^2
 \ \le\ \sum_{m\le4Y}\tau_4(m)^2\mathbf1_{m\ {\rm sf}}
 \ \ll\ YG^{15}.
 \tag{6}
$$

At a given $m$, to see the inequality take the sum of squares of the absolute-weight counts in disjoint rectangles, then bound by the square of the total count, since all individual weights have absolute value at most one. On squarefree integers $\tau_4^2=\tau_{16}$. The procedure applies to either parity, and all polynomials at their fixed cells are independent of the sampled $N$.

For the left first take $\omega=1$ and intervals with integer endpoints within a fixed integer range enclosing $[Y/2,9Y/8]$, and contained in $[Y/3,2Y]$ for large $Y$. Use canonical dyadic subintervals $J$ of this range. At each fixed left level these are disjoint, and since $u\asymp Y$ and $\beta\in(0,1)$,

$$
 \sum_J |V_{J,1,\beta}(\eta)|^2
 \ \le\left(\sum_J\int_J u^{\beta-1}\,du\right)^2
 \ \ll Y^{2\beta}
 \qquad(\eta\in\mathbb R).
 \tag{7}
$$

Apply (5) separately to each $H(\theta)=V_{J,1,\beta}(\eta(\theta))\widehat M_C(\theta)$, extending by zero off the arcs. Sum the resulting energies across both cell sets at each choice of left and right levels, using (6)–(7). At each $N$ an actual product of the hard windows is a sum of at most $O(G^5)$ such products with coefficient one, so Cauchy controls its squared modulus by this number times the sum of all fixed-cell squares. Sum over the $O(G^5)$ choices of levels and both parities, and restrict the sampled target range in (5) to $[Y,2Y]$ and the even targets. This proves (2) for integer-endpoint intervals with unit weight.

For real endpoints, round to integers with each change at most one. The induced difference in $V$ is $O(Y^{\beta-1})$ uniformly in $\eta$, and $\|\widehat M_{\pm,N}\|_\infty\ll YG^3$ by the same squarefree tuple count. Also $\int |A|\ll\Delta Q_0/\sqrt r$, because the sum of amplitudes at a fixed permitted $q$ is at most $\sqrt r$, and there are at most $Q_0/r$ such $q$. The error in (1) due to rounding is therefore $O(Y^{\beta-1}Q_0^2G^3/\sqrt r)$. There are $O(Y/K)$ target integers under the stated cap on $K$. The sum of squared rounding errors is absorbed in (2), since $Q_0=Y^{o(1)}$, $g\ge1$. The integer-endpoint argument is over the entire fixed enclosing range, so rounding need not preserve the central bounds.

Finally for any actual $\omega$, partial summation of the continuous integral defining $V$ bounds (1) by a constant times the supremum over its left (real) subintervals at unit weight. This can be seen by integrating the pointwise left prefix against the Stieltjes variation measure. The finitely many arcs and finite right polynomial cause no convergence issue; on a compact real interval the exceptional left density is integrable, so the BV identity applies also to complex weights by taking real and imaginary parts. Changing the endpoint representative of a BV function does not change $V$. This last step is for (1); it does not replace the original pointwise weight in the genuine prime sum. This completes (2), and Markov gives (3).

## 3. Consequences for the genuine full and original-major sums

First consider the prescribed planted family of R87, $K=K_z$ with $G^\epsilon\le z\le Z$. Its $K_z\le e^{2Z}$ satisfies the fold restriction. On **every** dyad, one can now replace the explicit exceptional term in its (3) by $O(YG^{-A})$ at a cost of at most (3) further targets, with no extra losses on either parity or the original hard tests. Thus one can drop the term off relative density zero on any sequence of dyads for which $e^{-2bG}(g/r)$ is smaller than each fixed inverse power of $G$ whenever the zero exists. For a fixed desired power $A$, a concrete sufficient condition for the additional count to be $O((Y/K_z)G^{-A})$ is

$$
       \log (r/g)+2bG\ \ge\ (C+3A)\log G .
 \tag{8}
$$

This is strictly a sufficient test; no conclusion for an ultra-close zero with $r/g$ small is proved. In particular the added estimate is independent of the earlier pointwise $Ye^{-bG}G^{O(1)}$ bound. Equation (2) can give a saving even when $bG$ is bounded.

For completeness, the same fold gives a direct all-dyad transfer for the **exact completed finite-cut bracket**, with no planted profile limit. The ambient log-exception conclusion also follows from the earlier common polylogarithmic methods of R80; the new point here is the actual exceptional correction and its dependence on the sampled subgroup, which can be sparse. Define $\mathcal B_\pm(N;I,\omega)$ to be [the real completed bracket (2)](r80-spectral-whole-mixed-parity-density.md#1-unconditional-parity-calculation-on-common-polylogarithmic-arcs), retaining $Q_N,Q_{N,U},J_{N,U},C_N,T(x)$ exactly. Then on every sufficiently large dyad, for each fixed $A>0$, off $O_A(YG^{-A})$ even targets both the genuine full sum and the actual original moving polynomial-major integral are

$$
                \mathcal B_\pm(N;I,\omega) + O_A(YG^{-A}),
 \tag{9}
$$

uniformly for both parities and all usual tests. The same absolute error and relative exceptional count $O_A((Y/K)G^{-A})$ hold on multiples of any $K\le G^M$, for any fixed $M$, with constants also depending on $M$. More generally the proof gives (9) for a prescribed $K\le e^{2Z}$ when (8) holds, with $O_A((Y/K)G^{-A})$ exceptions. If necessary take the exponent of the absolute error and the exponent in the count to be the same by slightly increasing the fixed $A$ in the inherited estimates.

Here is the verification that no moment hypotheses are needed for (9). In the [nonmultiple rational completion of R87](r87-spectral-all-scale-exceptional-left-reduction.md#1-remove-only-multiples-of-the-exceptional-conductor-in-the-auxiliary-calculation) and the [pointwise rational-tail estimate](r81-spectral-radical-criterion-and-log-exceptions.md#1-complete-the-auxiliary-major-at-each-such-target) use the elementary uniform bound

$$
 \log\mathcal A(N)
 \ll\sum_{\substack{p\mid N\\p>2}}p^{-3/4}
 \ \ll\ G^{1/4}+\frac{G}{G^{3/4}\log G}
 \ \ll G^{1/4}.
 \tag{10}
$$

Indeed at $p\le G$ one may bound by the sum over all integers, and at $p>G$ the number dividing $N$ is at most $\log(2Y)/\log G$. Thus $Q_0^{-1/4}\mathcal A(N)^{O(1)}=\exp(-4Z+O(G^{1/4}))$ has arbitrary fixed log saving. This removes the rational-completion moment restriction outright at this common cap, independently of the Page zero. The other moment of R87 is used only to approximate the bracket by the planted Dickman profile; it is not needed in (9). The estimate of the absent formal $r$-multiples in R87 (5) and the actual principal part on these arcs in R87 (7) are already uniform and negligible by $r>G^J$ for each fixed $J$, from classical Siegel there. R87's bounded-variation and arithmetic calculations therefore give the auxiliary major as the exact $\mathcal B_\pm+\mathfrak E_\pm+O_A(YG^{-A})$ before any planting restrictions. All its progression-estimate and real cutoff errors retain their original arbitrary fixed log savings; there is no need to strengthen those errors to stretched exponentials.

To obtain the actual full sum, add the genuinely common complement using [the common fixed-arc bound](r86-spectral-universal-good-scale-windows.md#2-common-analytic-inputs-and-disjoint-error-budgets), which costs $Ye^{-Z}$ off $O(YG^{O(1)}e^{-6Z})$ ambient targets. To get the actual original major, subtract the [true moving original minor](r79-spectral-original-minor-power-exception.md), of size $O(Y^{1-1/40000})$ off $O(Y^{1-3/10000})$ ambient targets. These exceptions are both $O_A((Y/K)G^{-A})$ when restricted to any $K\le e^{2Z}$. If a zero exists, (8) now takes care of the only remaining correction at the stated accuracy and exceptional count. For $K\le G^M$, $r/g\ge r/G^M$ makes (8) automatic for all sufficiently large $G$, by the same classical conductor lower bound. The case $K=1$ is (9) on the ambient family. Without a zero the correction is identically zero and (8) is not needed.

The bracket in (9) is radical-sensitive; no sharper leading constant for a prescribed sparse radical is being inferred from the ambient estimate. Equation (2) also does not remove the residual on all planted dyads when the old exceptional conductor overlaps substantially with the planting radical. Those are separate questions from ambient mean square.
