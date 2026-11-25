# Dependency-labeled implication of a uniform real-zero gap for the planted law

**Scope.** This records a separate, elementary implication for independent review. It is not a new proof of the uniform zero-gap statement, nor part of the hard-cut R88 theorem. The conclusion below is explicitly conditional on importing the pinned external result. Do not describe it as a new proof of Hypothesis S, a statement about every individual even target, or an independent verification of the entire external mathematical argument.

## Exact input and recorded verification

Use the following input, weaker than a zero-free half-plane:

$$
 {\rm (UZG)}:\quad \exists\,c>0,\ r_0\ge3:
 (1-\beta)\log r\ge c
$$

for every real zero $0<\beta<1$ of a primitive nonprincipal real Dirichlet $L$-function of conductor $r\ge r_0$. This is the exact statement needed, not GRH or the separate quasi-Riemann manuscript.

* [OpenAI, *Uniform exclusion of Landau–Siegel zeros*, 1 October 2026, Theorem 1, pinned source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex) asserts this with $r_0=3$. At the same pinned release the [formal theorem exists_absolute_real_zero_gap](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean) quantifies over natural level $r\ge3$, primitive nonprincipal complex-valued Dirichlet characters all of whose values have zero imaginary part, and real $0<\beta<1$. It uses the ordinary `DirichletCharacter.LFunction`, not an independently postulated Hecke $L$-function. The [pinned Mathlib analytic continuation file](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean) proves agreement with its Dirichlet series on $\Re s>1$; this revision is listed in the [release manifest](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/lake-manifest.json).
* The independent [cert-machine kernel report](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json), entry `SiegelZeros` on that same release commit, records Comparator exit zero, zero definition holes and acceptance by both Lean's kernel and nanoda, with only the three standard allowed axioms stated in the report. This is externally reported reproducibility evidence, not a local rerun here.
* [William D. Banks, arXiv:2610.15483v1, 11 October 2026, Theorem 1.1](https://arxiv.org/html/2610.15483v1#S1.SS2) independently reconstructs the proof in a detailed preprint and states $c=0.003$ for $r\ge10^{10}$. Its separate small-conductor computational corollary is not needed here. I have verified the statements and versions, not reviewed all steps of either external argument or asserted a refereed publication.

## Implication in the literal all-scale formula

Keep exactly the setup of [R87, formula (3)](r87-spectral-all-scale-exceptional-left-reduction.md): $G=\log Y$, $Q_0=\exp(16\sqrt G/\log G)$, the prescribed planting threshold $G^\epsilon\le z\le\sqrt G/\log G$, and the actual hard/BV tests and exact parity coefficients. If its exceptional term were nonzero by the necessary Page-zero condition, there would be a primitive real character of conductor $r\le Q_0$ with $b=1-\beta<4a_0/\sqrt G$. By R87's classical small-conductor argument, such $r$ eventually exceeds every fixed power of $G$, so (UZG) would apply for any fixed $r_0$. But then

$$
       0<c\le b\log r
       \le \frac{4a_0}{\sqrt G}\log Q_0
       =\frac{64a_0}{\log G}\longrightarrow0,
$$

a contradiction. Thus the entire exceptional term in R87 is exactly absent for every sufficiently large dyad under this imported input, not merely small after averaging. Its R88 hard representative is absent too. No further estimate for the color or Ramanujan weight is needed.

All other terms of R87 were already unconditional: the same genuine full and original-moving-major correlations therefore have the R86 Dickman base on **every** sufficiently large dyad, outside the same relative-density-zero planted target sets of R87, simultaneously across the stated hard/BV tests and both parities. This keeps the original moving minor estimate, leaves exact-radical and prescribed target questions untouched, and does not remove the relative exceptional sets. It strengthens only the admissible *ambient scales* when the pinned external dependency (UZG) is admitted.
