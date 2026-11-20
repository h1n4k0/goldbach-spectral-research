# Genuine compensated near-block means on the thin family N=2r²

**Claim.** Use the physical log coordinate p=log x and let J=[log(1/2),log(9/16)], the fixed Beta-active near block from arithmetic-round8.md. For X=8R² and the doubled squares N=2r², R<r≤2R, the exact centered kernel satisfies

    (1/R)∑_{R<r≤2R} ∥1_J T_{2r²,log} 1_J∥HS² ≪_A (log X)^(-A)       (2)

for every fixed A>0 where the original Hardy operator is realized. The underlying arithmetic kernel bound is unconditional; the preprint's local GRH is needed only for identification with its operator. Under **full** Dirichlet GRH for the auxiliary major-arc moduli, the right side improves to O(X^(-1/400)). Both are averages over a thin family of ≈√X moduli, not over all evens or over selected check points. A density-one theorem with earlier exceptional size O(X/log^A X), or the earlier conditional power exponent near X^(1−0.0001), does not imply this assertion on doubled squares. This is a genuine sharply centered variance bound, not just a signed first moment; it does not exclude exceptional squares, does not cover any other near block or its exterior crosses, and does not establish S/R.

The proof uses classical major/minor arcs and the arbitrary-sign device used in polynomial Goldbach problems; see for context [Althöfer–Chen–Perelli–Pintz, *The exceptional set of Goldbach numbers among polynomial values*](https://arxiv.org/abs/2611.09386). We do not use their exceptional-set theorem or claim novelty. The needed signed-count estimate and its transfer to this exact Beta-centered kernel are given below.

## 1. Uniform mean absolute error for fixed hard intervals

Let I_1,I_2 be any intervals inside [0,X]. Put e(t)=exp(2πit), s=2r², and

    A_s=∑_{n+m=s, n∈I_1,m∈I_2} Λ(n)Λ(m),
    V_s=∫ 1_{I_1}(u)1_{I_2}(s−u)du.

There is no unit restriction for now. We show uniformly in both interval endpoints that

    ∑_{R<r≤2R}|A_{2r²}−S(2r²)V_{2r²}| ≪ RX ε_X,           (3)

where unconditionally ε_X=(log X)^(-M) for any requested M; under full Dirichlet GRH one can take ε_X=X^(-1/100).

Take arbitrary real coefficients |τ_r|≤1, and write P_j(α)=∑_{n∈I_j}Λ(n)e(nα), Q_τ(α)=∑_{R<r≤2R}τ_r e(−2r²α). Orthogonality represents ∑τ_r A_s as ∫₀¹P_1P_2Q_τ. Choosing signs of the real errors at the end yields (3). Thus a signed first moment without arbitrary τ would not suffice.

**Minor arcs.** For parameter P (either a large fixed logarithmic power or X^(1/16)), major arcs are |α−a/q|≤P/(qX) for reduced q≤P, disjoint for large X. On the complement Dirichlet approximation with denominator ceil(X/P) gives P<q≲X/P and distance ≤1/q². The [Vinogradov–Vaughan bound](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf), applied by subtracting prefixes, gives |P_j|≪XP^(-1/2)(log X)^4 on the minor arcs; the X^(4/5) term is smaller in our range. Parseval and Chebyshev yield ∫|P_1P_2|≪X log X. Therefore, by interpolation,

    ∥P_1P_2∥_{4/3,minor} ≪ X^(5/4)P^(-1/4)(log X)^(11/4).

For *all* choices of τ, expanding ∥Q_τ∥₄⁴ and taking individual absolute values is bounded by the number of r_1²+r_2²=r_3²+r_4². The classical identity r_2(n)=4∑_{d|n}χ_4(d) gives r_2(n)≤4d(n), and d(n)^2≤d_4(n) prime power by prime power, so the count is O(X(log X)^3) by summing d_4. Consequently ∥Q_τ∥₄≪X^(1/4)(log X)^(3/4). Hölder gives minor contribution O(RX P^(-1/4)(log X)^(7/2)). This is a power saving when P=X^(1/16); the exponent 1/64 absorbs the stated logs to give 1/100. With P arbitrarily large logarithmic power it saves any prescribed logarithmic power. No pointwise Weyl estimate for an arbitrary signed quadratic sum is being assumed.

**Major arcs.** Write α=a/q+β, Ṽ_j(β)=∫_{I_j}e(uβ)du. The PNT in progressions followed by partial summation gives

    P_j(a/q+β) = μ(q)Ṽ_j(β)/φ(q) + error.

For P=(log X)^K, Siegel–Walfisz gives error O_D(X(log X)^(-D)) for arbitrary D after absorbing the factors φ(q) and 1+X|β|. For prefixes much smaller than X/(log X)^{D'} use the trivial bound; this ensures the estimate uniformly even for arbitrary small interval endpoints, with D' suitably larger. Under full GRH, use the [GRH character/AP estimate](https://arxiv.org/abs/2301.13457) to bound the error by O(√X P²(log X)²), including removed nonunit powers. Here only q≤P are needed, not necessarily divisors of the tested s. The total arc measure is O(P²/X) and |Q_τ|≤O(R). Expanding the product and using |P_j|,|Ṽ_j|≪X, the integrated approximation error under GRH is O(R√X P⁴(log X)²), which is smaller than RX X^(-1/100) for P=X^(1/16); in the unconditional log regime it saves any desired logarithmic power by choosing D. The quadratic sum is kept **exact** on these arcs.

Summing over a first, each r's resulting main expression has coefficient μ²(q)c_q(2r²)/φ(q)^2 in front of the β integral through |β|≤P/(qX). For all squarefree q,

    (1/R)∑_{R<r≤2R}|c_q(2r²)| ≪ 2^{ω(q)}.               (4)

Indeed at each odd prime p|q, |c_p(2r²)|=1+(p−2)1_{p|r}; at p=2 the factor is 1. Expand over squarefree d|q and use (1/R) #{R<r≤2R:d|r}≤2/d (it vanishes if d>2R). Thus the average is at most 2∏_{p|q,p>2}(1+(p−2)/p). This holds for arbitrarily large q, with no equidistribution assumption on r mod q. In particular the average tail of the singular series beyond P is O_ε(P^(-1+ε)), by 2^{ω(q)}/φ(q)^2≪_ε q^(-2+ε). Extending the β integration to the real line for q≤P incurs O(qX/P) per coefficient, since |Ṽ_j(β)|≪min(X,1/|β|), and the same average bound yields total O_ε(RX P^(-1+ε)). The absolutely convergent Ramanujan series ∑_q μ²(q)c_q(s)/φ(q)^2 is exactly S(s), as seen from the Euler factors; the β integral is V_s by Fourier inversion. Positivity of absolute values makes these averaged errors uniform for arbitrary signs τ. Major and minor estimates now give (3).

## 2. Moving ratio endpoints and the exact compensated kernel

We require n/s and m/s in fixed *dimensionless* intervals [a,b], [c,d]⊂[0,1], uniformly in these endpoints. Divide R<r≤2R into J_0 equal subdivisions of r, J_0=ceil(X^(1/200)) in the power regime. On one such subdivision let s_−≤s≤s_+ with s_+−s_−=O(X/J_0). Each scaled arithmetic interval, for example [as,bs], is bracketed between the fixed inner interval [as_+,bs_−] (empty if reversed) and the outer interval [as_−,bs_+]. The integral V_s for either bracket differs from the moving one by O(X/J_0), since each endpoint moves by this much. The discrete counts are bracketed pointwise by positivity; absolute error of the moving count is therefore bounded by the sum of the two bracket errors from (3) and O(S(s) X/J_0). For each subdivision apply (3) with signs **supported on that subdivision**; the global RX bound is unchanged, so totaling costs at most J_0. Also (1/R)∑_r S(2r²)≪1: S(2r²)=S(2r) and the positive divisor expansion has convergent ∑ a_d/d. After division by s≈X this gives uniform mean absolute error O(X^(-1/200)) for the power case. In the log case choose J_0 a sufficiently large log power and the exponent M in (3) larger again, so the corresponding normalized error is O_A((log X)^(-A)) for every A.

Restoring the restriction (nm,s)=1 only incurs o of either error scale: distinct actual primes in a sum to s are automatically units, and at most one equal prime pair is excluded; the total contribution from proper prime powers in an individual normalized count is O(X^(-1/2)(log X)^2), since each determines its partner. Multiply by √(n/s)√(m/s) inside the prefix x,y using the positive layer cake √u√v=∫₀ᵘ∫₀ᵛ ds_1 ds_2/(4√(s_1s_2)). The inner tests are precisely moving hard rectangles [s_1,x]×[s_2,y], already controlled uniformly. Fubini and the triangle inequality give the same mean absolute bounds for the weighted difference, without needing one exceptional set uniform in physical endpoints.

On the square p,q∈J, x=e^p,y=e^q∈[1/2,9/16], after exact D subtraction the only actual offdiagonal family is n+m=s and the only Beta line is u+v=1. The exact deweighted signed kernel is therefore S(s)∫_{1−y}^x√(u(1−u))du minus the corresponding normalized weighted sum, all divided by xy (as in arithmetic-round8.md). This is the weighted difference just estimated; the physical Hardy factors are bounded on J. Finally the two-dimensional upper sieve bounds its pointwise size by O(S(s)) uniformly: there are O(S(s)X/log² X) genuine prime pairs, each with weight O(log² X), plus the negligible proper-power contribution. With S(s)≪loglog(3X), mean absolute error upgrades to mean squared kernel error with only a loglog factor. Integrating over the fixed J² proves (2), and the power estimate O(X^(-1/400)) safely absorbs that factor.

**What remains.** This test of the actual nonstationary D+K centering controls all modes within one fixed-width genuine Beta-active window for almost all doubled squares. It does not control every member of this thin family, any cross outside J, or the full operator; the all-even uniform quantifier in S remains open.
