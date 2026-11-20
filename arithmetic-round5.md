# Why one-dimensional progression estimates do not close the signed residual

**Scope.** This is a countermodel to a specified proof strategy, NOT a counterexample to Li–Liu's Hypotheses S or R for the true von Mangoldt function. We preserve strong first-order arithmetic progression/character bounds, a large-modulus mean square, and, in a related finite-window operator model, the arithmetic projection and analytic Gram mechanisms. We deliberately do not preserve the exact weights at true primes, the local Euler factors, or the standard functional equation for Dirichlet L-functions. These distinctions are substantive.

## 1. Reflection anticorrelation with the same one-point statistics

For an even N let L=log N and consider only the balanced interval [N/3,2N/3]. Form the disjoint unordered pairs {n,N−n} whose members are coprime to N and both have nonzero Mangoldt weight. There is no active pair with n=N/2 for N>4. Independently for each pair with n<N/2, choose a sign ε=±1:

    λ_N(n)=Λ(n)(1+ε),       λ_N(N−n)=Λ(N−n)(1−ε).

Elsewhere leave λ_N=Λ. Write δ=λ_N−Λ. Pointwise 0≤λ_N≤2Λ and E λ_N=Λ; every balanced unit pair has product zero, and all modified weights remain supported on actual prime powers. In particular for every balanced test weight of the preprint the normalized mocked count is exactly zero, regardless of the signs.

The mass of squares on modified positions satisfies

    M_N := ∑_{n modified} Λ(n)² ≪ N S(N).

Indeed the two-dimensional upper sieve gives O(S(N)N/L²) balanced prime–prime pairs. Pairs involving a proper prime power number O(√N), as each power determines its partner. Each altered squared weight is O(L²), giving the claim. In particular replacing the diagonal built from Λ² by the exact λ_N² changes a compact normalized scalar diagonal by at most O(S(N)), much smaller than its macroscopic leading scale L. Also 0≤λ_N≤2Λ preserves the upper pointwise sieve and square-mass envelopes.

## 2. Uniform first-order constraints

For a fixed modulus q, residue a, interval I, and (separately) each Dirichlet character χ mod q, the perturbation on the test is a sum of independent signed coefficients:

    Δ(q,a;I) = ∑_{n∈I,n≡a mod q} δ(n),
    Δ(χ;I)   = ∑_{n∈I} δ(n) χ(n).

Only the intersection of I with the support window matters, so at most O(N²) different endpoint choices occur. If the length of this intersection is H, the coefficient square sum for the first test is O(L²(1+H/q)) and for the second O(L²(1+H)): each arithmetic point is used at most once and a reflection sign occurs at most twice. The exponential Rademacher bound gives, simultaneously,

    |Δ(q,a;I)| ≪ L sqrt((1+H/q) log(2qN)),
    |Δ(χ;I)|   ≪ L sqrt((1+H)   log(2qN)).

To justify the infinite union, the failure probability per test, including the real and imaginary parts for χ, can be taken ≤(2qN)^(-10) by choosing the absolute constant; summation over O(N²) endpoint pairs, q classes and ≤q characters for all q≥1 is o(1). Thus the perturbation is strictly below the customary GRH-shaped square-root/log² prefix errors. For prefixes x<N/3 it vanishes; otherwise H≪x and log(2qN)≪log(2qx). For q>N a residue class has at most one modified position, giving the simpler bound O(L) for residue tests. These are simultaneous tests of one common realization, not a choice made for each q.

## 3. Large-Q variance is stable, not just the separate residue maxima

The same realization can be chosen so that for every interval I and all Q≥L⁵,

    ∑_{q≤Q}∑_{a mod q} |Δ(q,a;I)|² ≪ Q N S(N).                 (1)

Discarding nonunit classes only decreases this expression. To prove it let U encode the independent pair signs as a vector of point perturbations on I∩[N/3,2N/3]. Its columns have disjoint two-point supports (or one-point supports after the cutoff), so ∥U∥²≪L². Set

    M_Q(n,m)=∑_{q≤Q} 1_{q | (n−m)},       B=Uᵀ M_Q U.

The left side of (1) is εᵀBε, with B positive semidefinite. A single pair contributes at most Λ(n)²+Λ(m)² to the trace of a single modulus: if the two selected points have the same residue, their coefficients have opposite signs. Therefore tr B≤QM_N. The row sums of M_Q are O(Q+N log(2Q)) by counting multiples of q in an interval of length O(N); consequently ∥B∥≪L²(Q+N log(2Q)) and ∥B∥_F²≤∥B∥tr B. By [Rudelson–Vershynin's Hanson–Wright inequality](https://arxiv.org/abs/1306.2872), for Q∈[L⁵,N] the probability that this quadratic form exceeds a sufficiently large constant times QNS(N) is at most 2 exp(−cQ/L³), using S(N)≫1. This is summable over the O(N³) possible interval and Q choices. For Q>N extend the Q=N estimate: each new modulus has at most one modified point per residue so its sum of squares is at most M_N deterministically. This proves (1) along with the events in §2.

When the ambient prefix x is comparable to N, the additional norm on the combined progression-residue space is O(√(QNS(N))), which is o(√(QN log N)) since S(N)≪loglog N. In particular it preserves any Barban–Davenport–Halberstam bound stated at that standard scale in its range of applicability, and does not alter a leading asymptotic of that size if one is available. This does not assert a BDH asymptotic outside known ranges.

**A fixed, rather than triangular, arithmetic sequence.** Choose even N_j growing at least as N_{j+1}≥N_j^4, with disjoint balanced windows. On each independently select an admissible realization proved above and patch the modifications into a single λ. Uniform prefix perturbations satisfy all GRH-shaped character and residue error scales from §2, by the triangle inequality and lacunarity (only N_j≤3x matter). Similarly for Q≥C(log(2x))⁵, combining (1) in the combined progression-residue norm gives an added norm O(√(Qx loglog(3x))). The total difference of second moments satisfies |∑_{n≤x}(λ(n)²−Λ(n)²)|≪x loglog(3x). Yet every balanced unit count at N_j is zero. Conditional on actual GRH for all q, the fixed model therefore obeys the usual GRH first-order AP/character inequalities everywhere, preserves the dominant ∑Λ² scale and large-Q BDH-scale variance bounds, and still fails uniform balanced Goldbach. The arithmetic construction itself and its assertions on the perturbations are unconditional.

## 4. A separate finite-window spectral countermodel

For each individual N use the above λ_N, not the infinite patched function. In the preprint's notation, define modified g_χ(s) by replacing the coefficients of −L'/L(1/2+s,χ) by λ_N where the series absolutely converges, and then by finite-polynomial perturbation throughout the original half-plane. All the original poles/zeros used to discuss these logarithmic derivatives are unchanged: one can write the modified derivative as that of

    L̃_χ(u) = L(u,χ) exp(∑_n δ(n)χ(n)n^(−u)/log n).

The added factor is entire and never zero. It is NOT a Dirichlet L-function with the original Euler factors, functional equation, or usual finite order. In particular identical nontrivial zeros here do not license the preprint's original Dirichlet-specific explicit formulas for the modified generators.

For clarity one can verify the Hardy norm baseline directly, without invoking any such formulas. On each strip boundary σ≥1/L the perturbing polynomial satisfies

    (2/φ(N)) ∑_{χ odd} |∑ δ(n)χ(n)n^(−1/2−σ−it)|²
       ≤ 2∑ δ(n)² n^(−1−2σ) ≪ S(N).

The first inequality is exact odd-character orthogonality (only the diagonal and opposite reflection are possible) followed by 2|ab|≤|a|²+|b|² for pairs. It includes all unit characters and the bound is uniform in t. Integrating with the paper's |1+s|^(-2) boundary weight gives O(S(N)) trace for the perturbation's positive Gram. Hence the modified character Gram still has trace O(L²) by the original GRH(N) trace bound and (a+b)²≤2a²+2b². Replacing the diagonal with exact λ_N² has trace-norm difference O(S(N)), using the rank-one diagonal decomposition. The model kernel K is kept fixed. Thus the complete modified residual still defines a compact selfadjoint Hilbert–Schmidt Hardy operator with O(L²) baseline and with the **same** exact finite projection/model bridge, now for its own weights. For any one fixed original nonzero balanced bump, the quadratic form equals c_ϕ S(N) since the modified arithmetic count vanishes. Its Riesz-vector norm stays O_ϕ(1), so the modified operator norm is ≳_ϕ S(N). Both S and R scales are out of reach in this model.

These implications separate the information in the one-point estimates, the coarse upper sieve, and the analytic/operator baseline from what is needed for the original problem. A valid proof must use additional arithmetic about Λ: for example signed two-point information strong enough to exclude the constructed reflection anticorrelation, or a mechanism exploiting the exact Euler/functional equations beyond the input inequalities. No actual T_N, S or R has been disproved.
