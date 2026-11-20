# An AP-only obstruction on escaping coarse modes

**Scope.** This strengthens the strategy countermodel in arithmetic-round5.md: the counterfeit residual can remain of main-term size on a genuine coarse vector at a growing physical scale, even when the corresponding actual T_N is small on that scale. It is still not a counterexample for the real Mangoldt weights or to S/R. Assume global Dirichlet GRH only to identify the genuine Hardy operators and preserve the stated true one-point estimates. The arithmetic variance input on balanced counts is unconditional as in arithmetic-quantitative.md.

## 1. A valid pair of scales and actual low-error examples

Let X<r≤2X, N=2r, L=log X, k=ceil(L^{20}), and H=kN. The integer k is kept fixed on this dyadic block. Choose the paper's real nonzero nonnegative symmetric bump ϕ supported in [1/3,2/3]. Put f_N(u)=k^{-1/2}ϕ(u/k), supported in [k/3,2k/3]. The corresponding normalized physical Hardy vector has norm comparable to 1: its differential a_{f_N}=k^{-1/2}a_ϕ(u/k) and w_N(u) is bounded above and below uniformly on u≈k because log k=o(log N).

The dyadic quantitative arithmetic estimate from earlier rounds shows two properties hold simultaneously for a proportion 1−o(1) of r:

1. ∥Π_N[(log X)^(-21),(log X)^{21}] T_N Π_N[(log X)^(-21),(log X)^{21}]∥=o(1) in density, so ⟨T_Nv_{f_N},v_{f_N}⟩=o(1) for these r after taking any fixed inverse-log threshold.
2. The genuine balanced weighted count G_ϕ(H) around the target H satisfies G_ϕ(H)=c_ϕ S(H)+o(1) there. For hard rectangles this is the quantitative centered variance result; applying the H¹ compression bound (or integrating the rectangle variance against the fixed smooth test derivatives) gives the same inverse-log savings for the fixed smooth bump. It applies over all even H in the dyadic block near kX. Restricting to H=2kr multiplies the upper bound on the exceptional proportion by at most O(k); since the dyadic exceptional bounds save arbitrary powers of log(kX), it still tends to zero.

Thus these properties are not two incompatible subsequence assertions. Note S(H)≥S(N)≫1 because N divides H.

## 2. Change exactly one off-diagonal family in expectation

At each such N reflect around H rather than N: for every active unordered pair {n,H−n} of unit prime powers modulo N with both members in [H/3,2H/3], double one of its two weights and zero the other using a separate independent Rademacher sign. Let λ be the modified weights and continue to form the operator at modulus N, not H. There is no active self-pair because H/2 shares a factor N/2 with N.

Keep the exact λ² diagonal and the same model K_N. All off-diagonal products from different reflection pairs have the same expectation as before, because signs on different pairs are independent and Eλ(n)=Λ(n). Every active product in the negative sum family n+m=H=kN disappears. In the quadratic form for f_N its normalization is precisely 1/(Nk)=1/H. Consequently

    E[⟨T̃_N v_{f_N},v_{f_N}⟩−⟨T_N v_{f_N},v_{f_N}⟩]
      = (1/H)∑_{n+m=H,(nm,N)=1} Λ(n)Λ(m)ϕ(n/H)ϕ(m/H)
      ≥ G_ϕ(H).

The inequality holds since units modulo H are units modulo N; the weights are nonnegative. A coin flip alters at most two n positions, and for each changed position the congruences n≡±m (mod N) allow O(k) partners in the support. Each term is O(L²/H) uniformly. Hence the bounded change per sign is O(L²/N) and the sum of squared bounds is O(kL⁴/N)=o(1), since there are O(H) signs. By the bounded differences inequality the quadratic form is within o(1) of its expected value with probability tending to 1 (e.g. at threshold N^(-1/8)).

## 3. Compatibility with first-order bounds and the log² spectral baseline

The first-order and large-Q variance concentration arguments in arithmetic-round5.md apply to the H-sized reflection with center H, not to the original smaller N window. Here the selected pairs may include prime powers nonunit at H, but the upper-sieve bound on their square mass is still O(HS(H)), independent of the unit restriction. All arithmetic progression/character bounds therefore hold with probability tending to 1, along with O(QHS(H)) total squared perturbation for Q≥(log H)^5. There is no demand to change the mock differently for different moduli in these tests.

For the finite analytic realization (at modulus N), the perturbing polynomial's expected trace is O(S(H)). Indeed on the left boundary or the right boundary the expected χ-average square is at most

    2∑_{n modified} Λ(n)² n^(-1−2σ) ≪ S(H).

This follows by taking the sign expectation first: the terms from different reflection pairs vanish (even if they alias modulo N), and twice the diagonal bounds each pair internally. This step is needed because the window is much longer than the modulus N. Markov yields perturbation Gram trace ≤L² with probability 1−O(S(H)/L²). The difference of the exact diagonals has trace norm O(S(H)) by the rank-one diagonal formula and H-sized square-mass estimate. Holomorphy of finite perturbations is as in the central countermodel. Taking the intersection of the probability-1−o(1) events proves there is one choice for which the mocked T̃_N retains the Hardy compactness and O(L²) baseline, satisfies the one-point/BDH arithmetic constraints, and has ⟨T̃_N v_{f_N},v_{f_N}⟩≫ S(N).

## 4. The witness is coarse, not a missed fine fluctuation

Take the orthogonal physical cell decomposition from arithmetic-round4.md with unit cells; let P_C be the projection onto the direct sum of the one-dimensional cell complements (the coarse modes) on all cells intersecting [k/3,2k/3]. A reference coarse vector on a cell is proportional to w_N(u)^(-1/2)u^(-3/2). On each cell near u≈k, the physical vector representing f_N, namely w_N(u)^{1/2}a_{f_N}(u) up to fixed normalization, has amplitude O(k^(-1/2)) and derivative O(k^(-3/2)). A scalar multiple of the coarse vector matching it at the midpoint also varies by O(k^(-3/2)) over the cell, since |∂_u log(w_N(u)^(-1/2)u^(-3/2))|≪1/k. Summing the squared residual over O(k) cells gives

    ∥v_{f_N}−P_Cv_{f_N}∥ ≪ 1/k.

The same bound covers cells touching the support boundary because ϕ and its derivatives vanish outside its compact support. Since both the true and mocked full norms are O(L²), replacing both test slots by P_Cv_{f_N} changes each quadratic form by O(L²/k)=o(1). Consequently the genuine coarse vector has only o(1) signed form for these N, while the mock has a signed form ≫S(N) on exactly that vector.

**Interpretation.** First-order AP and even conventional large-Q residue mean-square estimates do not exclude a main-term error in the remaining intermediate-scale coarse block. The arithmetic input omitted is concrete: substantial anticorrelation within one two-point reflection family (here at kN with k→∞) can be invisible to those statistics. A successful route must use further exact prime information; no actual operator has been contradicted.
