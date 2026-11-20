# Round 8: signed bounds and an arithmetic barrier for the retained coarse row

We use the exact unitary physical kernel of source-round2.md for the [Li–Liu operator](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf). Fix 0<a<b<1. Put L=log N, S=S(N), α=1/L, β=1/8, w_N(x)=(Nx)^(2α)/(1+(Nx)^(−2(β−α))), r_N(x)=x^(−3/2)w_N(x)^(−1/2). On these coordinates the true operator is T_N with kernel

    K_N(x,y)=2π r_N(x)r_N(y) M_N(x,y),
    M_N(x,y)=∫_(0,x]×(0,y] sqrt(uv) dμ_N(u,v).

Here μ_N is the discrete minus modeled signed alias measure, exact diagonal removed. Local GRH(N) identifies this kernel with the true T_N; the bounded-region kernel itself is defined arithmetically regardless of GRH. For an arbitrary nonempty interval J⊂[a,b], write e_J=r_N 1_J/||r_N 1_J||₂, the normalized coarse vector which was excluded from the smaller Round 7 bound. We obtain a signed bound for **all** such J, without removing e_J, for almost all moduli, and an every-modulus lower barrier for part of its row. No result controls the full norm for every modulus.

## 1. Signed upper bound for almost every modulus, including arbitrarily thin adaptive strips

Write X<r≤2X, N=2r. In this section all expectations use this dyadic family. Assume **global** Dirichlet GRH for the arithmetic-power input. Take A=X^(10^−6) and define

    V_N(A)= sup_{a≤x≤b} ( ∫_0^A |K_N(x,y)|²dy )^(1/2).

Then

    E_r V_N(A)² ≪_{a,b} X^(−1/10000).                              (1)

In particular, apart from O_{a,b}(X^(1−1/20000)) moduli in the family, simultaneously for every interval J⊂[a,b], even chosen after N and of any positive width,

    ||1_J T_N 1_{(0,A]}||_HS ≤ |J|^(1/2) X^(−1/40000),
    ||1_{(0,A]} T_N e_J||₂ ≤ |J|^(1/2) X^(−1/40000).                (2)

The key new gain relative to the earlier complete-prefix averaged theorem is the explicit factor sqrt(|J|), with no minimum width and simultaneous choice of J. Absolute cutoff and lower bounds for mesh widths are not imposed on J itself. This still does not rule out any infinite exceptional subfamily or any crossing into y>A.

**Pointwise arithmetic variance then kernel variance.** For any fixed rectangular test R contained in 0<u≤b, 0<v≤A, use arithmetic-power.md §3 with each positive/negative alias parameter k≤A+b (there are O(A) choices). Passing from N to kN costs O(k³) in the second moment: both the normalization and model scale by k, and dropping the divisibility restriction in a nonnegative square costs k. The rescaled interval endpoints in the auxiliary normalization yield a permissible range for the hard-interval estimate. Thus Minkowski's inequality over aliases yields

    E_r |μ_N(R)|² ≪ A^5 X^(−0.0004),

uniformly in the endpoints. The negligible errors from removing nonunit proper powers and the at most one equal prime pair per relevant summation alias are absorbed by the same bound as in arithmetic-power.md. Insert sqrt(u) and sqrt(v) on the cumulative rectangle by writing sqrt(u)=∫_0^u dt/(2sqrt(t)), and likewise for v, then use Minkowski under these integrals. This gives

    E_r |M_N(x,y)|² ≪ xy A^5 X^(−0.0004),

uniformly on the support. The measures are locally finite and the integrals are absolutely convergent on bounded rectangles, so signed Fubini is legitimate. If x≤b then y<1−b has no aliases. On x∈[a,b], y≥1−b, one has |r_N(x)|≪_{a,b}1 and |r_N(y)|≪_b y^(−3/2) for large N. Consequently for each x,

    E_r ∫_0^A |K_N(x,y)|²dy ≪_{a,b} A^5 X^(−0.0004),

since the resulting y integrand is bounded by y^(−2) for y≥1−b. This is a pointwise estimate in x, not yet uniform for arbitrary N-dependent rows.

**Uniform grid interpolation.** Put d=X^(−1/10000) and take an x grid of mesh ≤d covering [a,b], with O_{a,b}(1/d) points. For x,x' in this interval with |x−x'|≤d, the difference in M_N consists of alias lines within one interval in u of length at most d. Use the two-form upper-sieve argument of operator-round7.md §3 on an interval of raw length at most Nd, by extending it to length Nd to bound absolute masses. Here log(Nd)≍log N and log(2NA)≍log N, so those log quotients are bounded. Multiplying by sqrt(uv) and summing over k≤y+b costs at most C S(1+y)^(3/2), by the positive divisor expansion for S(kN). The model obeys the same bound. It follows that, for 1−b≤y≤A,

    |r_N(y)(M_N(x,y)−M_N(x',y))| ≪_{a,b} S d.

The same argument on the entire u interval (0,x'] with raw bounding length N gives |r_N(y)M_N(x',y)|≪_{a,b} S. Also r_N is uniformly Lipschitz on [a,b] by differentiating its explicit formula. Therefore

    ||(K_N(x,·)−K_N(x',·))1_{(0,A]}||₂ ≪_{a,b} S d sqrt(A).

This argument includes the endpoints of discrete jumps, by the usual interval count with O(1) endpoints; it does not assume continuity of the atomic cumulative function. Every x is within d of a grid point. Bounding the grid maximum squared by the sum of squares, then taking expectation, yields

    E_r V_N(A)² ≪_{a,b} d^(−1) A^5 X^(−0.0004) + (loglog X)^2 d² A.

The first exponent is −0.000295 and the second is −0.000199 apart from logarithms, using S(N)≪loglog N. This proves (1) with room. Markov and the elementary inequality ||1_J T_N 1_{≤A}||_HS²≤|J| V_N(A)² prove (2), since e_J is a unit vector on J and T_N is Hermitian.

**Unconditional logarithmic arithmetic variant.** With A=(log X)^B for any fixed B>0, use the unconditional hard-interval variances of arithmetic-quantitative.md §§1–2 instead. They give O_{D,B}((log X)^(−D)) for the centered term for any requested D after summing the polynomial-logarithmic number of aliases. The same layer-cake and interpolation proofs, with d=(log X)^(−K) and K chosen large for the intended error, show E_r V_N(A)²≪_{a,b,B,D}(log X)^(−D) for every fixed D. This is an unconditional assertion on the bounded arithmetic kernels; whenever GRH(N) holds it applies to the actual operator at that N. It does not assert a density estimate relative to an unknown sparse set of admissible moduli. No global GRH is needed for this logarithmic arithmetic variance.

## 2. An actual lower bound and the localized Goldbach obstacle for a single retained row

Return to **local** GRH(N). Fix a nonempty open interval I=(c,d) with closure contained in (0,min(a,1/2)) and put I*=1−I. Let Q_{I*} be the true orthogonal Hardy projection onto the closed span of v_g with g smooth and compactly supported in I*. Let the one-variable positive atomic measure and its cumulative signed discrepancy on I be

    ν_N = N^(−1) Σ_{n+m=N, (n,N)=1} Λ(n)Λ(m) δ_{n/N},
    D_N(u) = S(u−c) − ν_N((c,u]),  c<u<d.

Write overline(D_N) for its interval average. Then, uniformly over all J⊂[a,b] of positive width ε,

    ||Q_{I*} T_N e_J|| ≍_{I,a,b} sqrt(ε) ||D_N − overline(D_N)||_{L²(I)}.      (3)

This is a statement about an actual part of the retained row, not an equality for the entire operator or the entire row. For each such N there is the explicit lower bound

    ||Q_{I*} T_N e_J|| ≫_{I,a,b} sqrt(ε) S/(m_I+1)
                         ≫_{I,a,b} sqrt(ε) L²/N,                         (4)

where m_I is the number of distinct active abscissae (unit prime powers on both sides, with positive weights) in I. If there are no prime–prime pairs in I at a sufficiently large N, the left side is instead ≫_{I,a,b} S sqrt(ε). More generally a fixed positive relative deficit against any one fixed smooth positive test implies a lower bound of that order, with its test-dependent constant. Thus proving a o(S sqrt(ε)) upper uniformly for this single coarse row already entails the localized binary Goldbach asymptotic for smooth tests on I and in particular representations on each sufficiently large admissible modulus. The standard width or moment-removal estimate alone cannot supply that cancellation.

**Proof of (3).** The inverse Volterra formula from source-round2.md shows that the test f_J whose physical vector is e_J satisfies, identically to the left of J,

    f_J(u) = C_{N,J} sqrt(u),
    C_{N,J}=sqrt(2π)||r_N 1_J||₂ ≍_{a,b} sqrt(ε).

In fact a_f=(sqrt(2π)/sqrt(w_N)) e_J, and inserting it into f(u)=sqrt(u)∫_u^∞ a_f(x)x^(−3/2)dx gives the stated constant exactly. Its support is below sup J<1. For g supported in I*, both test supports are in the first period, so the only nonzero alias in their pairing is the sum n+m=N, with negative arithmetic sign. Consequently

    ⟨T_N e_J, v_g⟩ = C_{N,J} ∫_I sqrt(u) conj(g(1−u)) [S du−dν_N(u)].

The inverse formula and pairing hold for the indicator-defined vector e_J by approximating its physical vector in L² by smooth compact physical vectors, as in source-round2.md; on I its inverse weights converge uniformly, and all pairings here involve finite measures. On I*, the exact Hardy norm of v_g is comparable to ||g'||₂, uniformly in N by the fixed compact support, positivity of w_N, and integration by parts in ∫|g/2−xg'|², which yields ∫(x²|g'|²+3|g|²/4). The map g(v)→ψ(u)=sqrt(u)g(1−u) is an isomorphism between the two H₀¹ intervals with derivative norm comparability. Integration by parts gives the signed measure pairing as −∫_I D_N ψ', and the range of derivatives of H₀¹(I) is the closed zero-mean L² subspace. Its dual norm is exactly ||D_N−overline(D_N)||₂. Taking the supremum over v_g in the defining projected space proves (3).

**Proof of (4) and the arithmetic consequence.** In each interval between consecutive atoms (also use the two endpoint gaps), D_N has constant slope S. For a gap of length ℓ, its squared L² distance to any single scalar is at least S²ℓ³/12. The sum of cubes of the m_I+1 gap lengths is at least |I|³/(m_I+1)² by convexity. This proves the first lower bound in (4), for any positive atom weights. On a fixed I the two-prime upper sieve gives O_I(S N/L²) prime–prime pairs, and pairs involving a proper prime power add O(sqrt(N)+N^(1/3)L) possible abscissae. This proves the second bound since S is bounded below and the proper-power count is smaller. If no prime pairs occur, the proper-power measure has total mass O(L²/sqrt(N)) and cannot cancel the ramp of size S on fixed I. A smooth deficit is tested directly by the above pairing. Conversely, an estimate o(S sqrt(ε)) for this row forces every smooth weighted discrepancy on I to be o(S) by the same duality; taking a fixed nonnegative nonzero smooth test and subtracting proper powers gives true prime pairs, not just prime powers.

The density-one upper bound (1) is consistent with both lower estimates and is not an every-N statement. It resolves an averaged portion of the coarse row bypassed by Round 7, while the localized fixed-modulus obstacle in (3) remains at the core of any universal smallness proof.
