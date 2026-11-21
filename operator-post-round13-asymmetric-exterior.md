# Post-R13: a genuinely asymmetric exterior strip using only ordinary Vaughan minor arcs

**Claim, conditional on global Dirichlet GRH.** Write X=8R², L=log X, N=2r², R<r≤2R, and P_U=1_(0,U] in the exact dimensionless physical coordinate. There are O_ε(X^(97/200+ε)) exceptions for which

    ||P_B T_N P_Y||_HS > X^(-1/400),  B=X^(1/100), Y=X^(1/20).     (1)

In particular this controls the genuine low/exterior crossing P_B T_N 1_(B,Y] and its adjoint for all other members of that thin family. The inequality is not a complete prefix through Y: 1_(B,Y]T_N1_(B,Y], the two crossings beyond Y, and exterior-to-exterior beyond Y are not bounded here. Global Dirichlet GRH enters the auxiliary major arcs and local GRH(N) identifies the exact arithmetic kernel. The result does not use the extra fixed-weight fourth-moment preprint, does not close S/R, and is not an every-modulus bound. It is an asymmetric extension of the ordinary Vaughan plus Plancherel method in the [pinned Round 13 theorem](https://github.com/h1n4k0/goldbach-spectral-research/blob/7b82bf321965f419f1d2c7cf7223434c78134d0b/ROUND13.md), rather than a smaller exception count on its same window.

## 1. Unequal-scale major arcs

Let 1≤B≤Y≤X^(1/8), W=4BX and Z=8YX, and write P=Z^(2/5); factors 4,8 are harmless. On each alias in the physical rectangle x≤B,y≤Y, n is the short integer leg supported in [0,W] and m the long leg inside [0,Z]. The magnitude of each shifted sum or difference s=kN is ≤Z, even as k ranges over all aliases (k≤2Y). An arbitrary pair of moving physical hard intervals collapses to one adaptive interval I_r in n by the relation m=kN−n or m=n±kN. Take the other prime factor uncut on [0,Z]. For raw intervals with a leg bound U=W or U=Z, let E_I(a,q,β) denote the standard major-arc error in decomposing its prime exponential sum into μ(q)V_I(β)/φ(q), V_I the continuous interval transform. Use disjoint arcs |β|≤P/(qZ). The R13 character Parseval identity remains exact.

The useful difference is in the integrated error energy when the leg limit U is short. Every primitive or induced character's prefix error, after the principal term is removed, is O(sqrt(U)L²) on [0,U] under global GRH; the required cutoff q≤P is smaller than sqrt(W), since Y≤X^(1/8), and even smaller prefixes are bounded by Chebyshev if the quoted conditional theorem assumes prefix length at least q. Use Abel endpoint terms of size O(sqrt(U)L²) and the Fourier transform of the interval-restricted cumulative error of squared L² norm O(U²L⁴). With H=P/(qZ),

    ∫_(−H)^H |ℰ_(χ,I)(β)|²dβ ≪ L⁴(UH + U²H²).

The first term is the endpoint piece, the second by real-line Plancherel, exactly as in R13. Multiply by q and average over the characters to obtain total energy over a mod q. The nonunit part costs O(qH L⁴) per q and is also absorbed. Summing all q≤P gives

    Σ_(q≤P) Σ_(a mod q) ∫_(−H)^H |E_I|²
       ≪ L⁵[(U/Z)P² +(U/Z)²P²] ≪ L⁵ (U/Z)P².

For the principal part, integrating over all β by Plancherel and summing (a,q) costs squared norm O(U Σ_(q≤P) 1/φ(q))=O(UL). Hence mixed terms in the actual *unequal* product, using Cauchy in (a,q,β), cost at most O(sqrt(W) P L³) each: the principal factors have norms O(sqrt(WL)) and O(sqrt(ZL)); the respective error factors are O(P sqrt(W/Z)L^2.5) and O(P L^2.5). The product of errors costs O(P² sqrt(W/Z) L⁵)≤O(sqrt(W) P L⁵) as P≤sqrt Z. These bounds are individual in r and hold for every admissible hard interval, not just averaged endpoints. Conjugation for a difference does not alter them.

For the centered principal model, the Ramanujan coefficient tails at |s|≤Z are exactly those in pinned R11, and the full interval transform has |V_I(β)|≪min(Z,1/|β|). Using this conservative bound even on the short side, the singular integral and Ramanujan tails together cost O_ε(Z^(1+ε)/P). Thus the total individual major discrepancy per line, before /N normalization, is

    O_ε(sqrt(W) P L⁵ + Z^(1+ε)/P).                              (2)

When comparing with the stated raw-coordinate geometry, enlarging the long interval to [0,Z] after collapsing the short one has not altered any actual summand or continuous overlap. Endpoints can be half-open or rounded at O(log² Z), absorbed in (2).

## 2. Selected adaptive minor arcs with the short factor

Fix an arbitrary selected set E of M moduli and let σ_r be arbitrary real signs with |σ_r|≤1. Use the existing R12 dyadic interval decomposition in I_r, grouping selected r by dyadic input interval. At each level the intervals are disjoint and contained in [0,W], so the relevant sum of prime L² energies is O(WL) by Parseval, not O(ZL). The uncut long factor on minor arcs has L⁴ norm O(Z^(3/4) P^(-1/4) L^C) by Vaughan and Parseval, since P≤Z^(2/5); this needs no cited extra fourth-moment theorem. For each group, the fourth moment of Σ_(r∈E_I) σ_r e(±2kr²θ) is O_ε(|E_I|² X^ε) by the divisor-bound square-difference argument. The fixed integer k cancels in the equality of differences. The selected groups satisfy Σ_I |E_I|≤2M per level. Hölder (2,4,4) and Cauchy across the groups therefore give total minor discrepancy

    O_ε(sqrt(M) sqrt(W) Z^(3/4) P^(-1/4) X^ε)

after absorbing logarithmic levels. The same applies to each signed alias; selecting signs gives an absolute discrepancy bound over E. Normalize by N≈X in magnitude or absorb X/N into the selected coefficients. Restricting to unit pairs costs at most O(sqrt(Z)L²/X) per line: an offending ordinary prime on either leg forces both ordinary primes to be equal, and each proper prime-power summand determines its unique partner on its line. Sum over k≤2Y and all orientations. The resulting bound for any actual dimensionless hard rectangle contained in (0,B]×(0,Y] is

    Σ_(r∈E) |μ_N(rectangle)| ≪ C_E,

    C_E = sqrt(M) sqrt(B) Y^(7/4) X^(1/4+ε) P^(-1/4)
         + M [Y sqrt(B/X) P L⁵ + Y² Z^ε/P + Y^(3/2)L² X^(-1/2)].    (3)

Here μ_N is the true arithmetic-minus-Beta signed alias measure with exact diagonal removed. The inequality stays uniform as endpoints vary, and the selected set may depend on the eventual kernel norm.

## 3. Transfer to the true asymmetric kernel, including x=0

Use the original exact physical kernel K_N(x,y)=2π r_N(x)r_N(y)M_N(x,y) as in source-round2.md, M_N the cumulative √(uv)-weighted signed discrepancy, r_N(x)=x^(-3/2)/sqrt(w_N(x)). For x+y<1 the kernel is zero, so min(x,y)<1/4 forces the other coordinate ≥3/4. The shorter-axis two-form upper-sieve estimate and edge estimate in arithmetic-round12-prefix.md §§2–3 apply unchanged with the upper support limit Y: it uses only max(raw n,raw m)≲YX, log(YX)≍L, length N min(x,y), and the divisor sum Σ_(k≤2 max(x,y)) S(kN)≪S(N) max(x,y). Explicitly, on min(x,y)≥a=X^-1/4,

    |M_N(x,y)| ≪ S(N)(xy)^(3/2),  so |K_N(x,y)|≪S(N).

For 1/N≤min(x,y)<a use the trivial integer bound per alias instead of the sieve to get |K_N|≪L²; the y or x other coordinate is ≥3/4. Below 1/N the discrete contribution is zero and the model costs O(S(N)(N min(x,y))^(-β)), β=1/8. Both directional edges of the rectangle have squared HS mass O(Y L⁴X^-1/4), uniformly and before selecting any moduli.

On the bulk, layer cake applied to (3) bounds Σ_E |M_N(x,y)| by sqrt(xy) C_E. Since w_N≥1/2 there, dividing by the standard factors gives Σ_E |K_N(x,y)|≪C_E/(xy). Multiply by the genuine individual sieve cap above, bound S(N)≪L, and integrate over a≤x≤B,a≤y≤Y. The two reciprocal integrals cost O(L²). Thus, with T_N in its true physical coordinates,

    Σ_(r∈E) ||P_B T_N P_Y||_HS² ≪ L³ C_E + M Y L⁴X^-1/4.            (4)

This argument does not assume sign cancellation between different aliases or a growing-window two-point hypothesis; cancellation comes from the centered thin-family minor/major estimates, and all operator points in the exterior strip are included by the cumulative representation.

## 4. Numbers and exact limitation

For B=X^.01, Y=X^.05, τ=X^(-1/400), P≈X^.42, the major leading coefficient Y sqrt(B/X)P is X^(-.025), compared to τ²=X^(-.005), and the series/nonunit/edge coefficients are smaller still (the edge X^(-.2)). Taking the actual exception set E and moving these linear terms to the left in (4) leaves

    M τ² ≪_ε sqrt(M) sqrt(B) Y^(7/4) X^(1/4+ε) P^(-1/4).

If M>0, squaring after division proves M≪_ε τ^-4 B Y^(7/2) X^(1/2+ε) P^(-1/2)≈τ^-4 B Y^(33/10) X^(3/10+ε)=X^(97/200+ε). For small ε this is o of the ≍X^(1/2) doubled squares. The proof supplies an actual extension of the cross rows from the published B to Y, and not the entire larger Y-square. Taking B=Y=X^.05 at this same precision in our budget gives an exponent exceeding 1/2; no such inference is permitted. For output much larger still, the major/minor inputs and chart count in (3) do not remain controllable at inverse-log thresholds. The old far-cutoff starts only at much larger scales. Neither the remaining same-modulus genuine-prime covariance nor the full upper exterior block is solved.
