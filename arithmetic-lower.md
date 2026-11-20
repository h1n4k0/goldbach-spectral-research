# An actual full-norm lower bound from a single asymmetric prime pair

There are infinitely many even N, indeed ≫X/log X in each sufficiently large dyadic interval [X,2X], for which under GRH(N)

    ∥T_N∥op ≫ (log N)/√N.

The selection and the underlying finite arithmetic certificate are unconditional; the operator identification assumes GRH(N), as elsewhere. Under family GRH the lower bound thus holds on all the selected infinitely many moduli. One may also impose S(N)≤C for a fixed absolute C at the cost of a constant proportion of this family. This closes neither the remaining √log N factor to the R threshold on this family nor the much larger gap to refuting S.

**Construction.** Let p run through the primes p≡41 (mod 70) and take N=p−3. Dirichlet's theorem (or the ordinary prime number theorem in this fixed progression for the count) supplies the claimed selection. Then N is even, (N,3)=1, N+3=p is prime, and N−3=p−6 is divisible by both 5 and 7. Hence Λ(N−3)=0, not just “nonprime.”

Choose a real bump F compactly supported in (5/2,7/2) with F(3)=1 and put f_N(u)=F(Nu). Take a fixed real g supported in (0.9,1.1) equal to 1 on (0.95,1.05). For each fixed N large enough the exact two-weight identity in arithmetic.md applies. The only input unit prime power is 3, and the only allowed congruence partners in the output window are N±3. The exact diagonal is absent. In the continuous model, both the positive difference and negative sum at k=1 integrate to ∫f_N because g(1+u)=g(1−u)=1 throughout the support; all other shape terms are zero. Thus the normalized identity has exactly

    B_N(f_N,g)=(log 3)(log p)/N.

Formula (7.15) of Li–Liu gives ∥v_{f_N}∥²=(2πN)^(-1)∫w_N(t/N)|(1/2−t∂_t)F(t)|²dt, where w_N(t/N)=(t^{-2α}+t^{-2β})^{-1}. This weight is bounded above and below uniformly on the fixed t interval, so ∥v_{f_N}∥≍N^{-1/2}. The fixed g has ∥v_g∥≍1. Dividing gives the claimed actual residual norm lower bound. It is a crossing interaction between unnormalized physical scales 3 and N; it is NOT a lower bound for every N, nor a consequence of separate component norms.

**Keeping the singular series bounded.** Use S(p−3)=2C₂∑_{d|p−3} a_d from arithmetic-quantitative.md. For the chosen primes, any contributing odd squarefree d is coprime to 3·5·7. For d≤X^{1/4}, the congruences p≡41 mod 70 and p≡3 mod d give a single reduced class modulo 70d, so the Brun–Titchmarsh inequality bounds its prime count by O(X/(φ(d)log X)) uniformly. The convergent series ∑a_d/φ(d) bounds the weighted contribution by O(X/log X). Larger d contribute at most O(X∑_{d>X^{1/4}}a_d/d)=O(X^{7/8}) using the convergence of ∑a_d/d^{1/2}; here the trivial count of all integers divisible by such d in [1,3X] is ≤3X/d. The dyadic mean of S(p−3) over the chosen primes is consequently bounded, and Markov retains a positive proportion with S(p−3)≤C. On that subset the ratio of the proved lower bound to δ_N is of order 1/√log N, not a contradiction.

The same data certify no upper bound: a large matrix element is legitimate evidence from below, and one small matrix element cannot control a supremum. The mean-square local upper bounds in the other notes and this sparse cross element are compatible.

## Matching every-modulus bound for the microscopic-to-macroscopic corner

Use the common physical L² coordinates from source-round2.md, with unnormalized scale n=Nx. For any fixed b>0, 1≤Y≤N/4, define the actual corner C=1_{Nx≤Y} H_N 1_{y≤b}. Under GRH(N) for the realization,

    ∥C∥op ≪_b L√(Y/N),     L=log N.

Indeed reversing the Volterra transform gives f(u)=√u∫_u^∞ a_f(t)t^{-3/2}dt, with ∫w_N|a_f|² bounded for unit vectors. The inverse test for a source supported in Nu≤Y vanishes beyond u=Y/N. For u≥1/N one has |f(u)|≪u^{-1/2} by Cauchy–Schwarz and w_N≥1/2; for u<1/N one has |f(u)|≪N^{-β}u^{-1/2−β} by the explicit weight, β=1/8. In particular ∫₀^{Y/N}|f(u)|du≪√(Y/N). The unit output test g, supported in unnormalized scales up to bN after inversion, is uniformly O(1) on v≥3/4 by the same estimate. All off-diagonal partners of the input live there when x≤1/4. There are only O_b(1) partners per input n and O_b(1) modeled shifts; S(kN)≪_b S(N). Thus the centered form in absolute value is

    ≪_b (L/√N) ∑_{n≤Y} Λ(n)/√n + S(N)√(Y/N)
    ≪_b L√(Y/N)

by Chebyshev. The exact two-weight arithmetic formula applies to inverse tests by cutoff and density, as in the cumulative-kernel derivation. For any fixed Y>7/2 and b>1.1 this matches the infinite-family lower bound up to a constant. No uniform lower bound of this size is claimed at other N.

When 1≤Y≤√N/4, a two-prime upper sieve refines the corner estimate to

    ∥C∥op ≪_b N^{-1/2}[ S(N)L√Y/log(2Y) + L log(2Y)
                          + L log(2L) + S(N)√Y ].

To verify, decompose n≤Y into dyadic ranges n≈M. For prime–prime pairs n,kN±n the same uniform upper sieve as in arithmetic.md on the interval of length M gives O_b(S(kN)M/log²(2M)). The progression-count errors depend only on the at most two excluded residues per prime, not on kN. Both prime values exceed the cutoff M^{1/u} for any sufficiently large fixed u (bounded M can be absorbed by constants). Multiplying by O(log(2M)L/√M) and summing all dyadics costs O_b(S(N)L√Y/log(2Y)). For input proper powers the sum of Λ(p^j)/p^{j/2} is O(log(2Y)): j=2 uses ∑_{p≤√Y} log p/p≪log(2Y); j≥3 sums absolutely. For output proper powers m≈_b N the range in m has length O(M) per shape. Distinct j-th powers in [3N/4,(b+1)N] are separated by ≫√N uniformly for j≥2 (derivative of t^j is j t^{j−1}, and j≥2). Thus O_b(1) occur per exponent. Each prime power m=p^j has Λ(m)≤O_b(L/j), and j≤O_b(L). The sum of output Λ weights is O_b(L log(2L)) on each dyadic range. Multiplying by log(2M)/√M and summing the resulting geometrically decaying dyadic series gives O_b(L log(2L)). Finally the continuous-model terms are already O_b(S(N)√(Y/N)).

**Consequence.** For every fixed ε>0 with ε<1 and b fixed, the corner is o(δ_N) uniformly over even N satisfying GRH(N) when Y≤L(log L)^{1−ε}; use S(N)≪log L and its positive lower bound. For the maximal endpoint the main ratio is O((log L)^{−ε/2}), and smaller Y follow by restriction monotonicity of the corner norm. If S(N) is bounded along a sequence, the same conclusion holds for Y≤L(log L)^{2−ε}. This rules out this small-input/fixed-output corner as the sole cause of a violation of R; accumulation of other blocks and the exact R threshold still matter.
