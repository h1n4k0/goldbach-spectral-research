# Operator lane | 2026-11-20 | conditional mathematical research

Primary source: Jiamin Li and Jianya Liu, *A Conditional Proof of the Goldbach Conjecture*, 2026-11-13, [announcement](https://mrc.sdu.edu.cn/english/info/1018/1514.htm), [63-page manuscript](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf). Manuscript equation and section numbers below. Hypotheses S and R are not proved in this note.

## The real operator

Write L=log N, α=1/L, β=1/8, S=the Goldbach singular series, Γ the union of the two vertical boundaries. With respect to positive dt on both components, (2.17) has boundary kernel E(s,conj z)/[(1+s)(1+conj z)]. Equations (2.11)–(2.13) give E=P−D−K, where P is the equally weighted odd-character covariance of gχ(s)=(L′/L)(1/2+s,χ); D(w)=Σ_{(n,N)=1} Λ(n)^2 n^(−1−w); K(s,z)=S(π/N)^(s+z) A_N(s+z) ζ(1−s−z) X1(s)X1(z), with A_N(w)=∏_{p>2,p∤N}(1+p^(−w)/(p−2)) and X1(s)=Γ((3/2−s)/2)/Γ((3/2+s)/2). Theorem 6.2 gives ∥T_N∥ ≤ ∥T_N∥HS ≪ L² under GRH(N). Theorem 6.1 gives precisely the norm tests in the assignment. The threshold for S is on the full space and is not a theorem about one line or one vector.

## New restricted theorem: cancellation away from the left boundary

Let 1/L ≤ σ ≤ β. Let Bσσ be the integral operator on L²(R,dt) whose kernel is the weighted E(σ+it, σ−iy) above. It is the actual right-right boundary block for σ=β. For general σ it is an interior restriction of the **kernel**. For sufficiently large even N satisfying GRH(N), with absolute constants,
    
    ∥Bσσ∥HS ≪ N^(−σ) L/σ + S N^(−2σ)/σ².                  (O1)

This statement, an independent deduction from the source's estimates, is not attributed to the paper. It is uniform in N, σ. In particular ∥Bββ∥HS ≪ N^(−1/8) log N, and on σ=A loglog N/log N, for fixed A>2, the block tends to zero at least as fast as O_A(L^(2−A)/log L). This only localizes a difficult boundary layer, not the norm or even all mixed blocks. Here is a derivation:

1. Put X=N/2, H=1/(2σ), x=X exp(−H). Then x≥sqrt(N)/2, log(X/x)=H and x^(−σ)≪N^(−σ). Use the logarithmically tapered Dirichlet polynomial pχ(s)=Σ_{n≤X}Λ(n)χ(n)n^(−1/2−s)w(n), w=1 on n≤x, w=log(X/n)/H on x<n≤X, w=0 otherwise. Equation (6.12) with the kernel (Xᵛ−xᵛ)/(H v²) applies verbatim: its residue is 1, and its contour decay and zero residues are unchanged.
2. In the norm (χ,t) with normalized odd-character counting and vertical measure dt/(1+t²), lemmas (6.9),(6.10) give ∥Qχ(σ,t)∥₂ ≪ L+1/σ ≪ L, where Qχ=Σγ σ/[σ²+(t−γ)²]. The nontrivial-zero residues in −gχ−pχ are pointwise at most (x^(−σ)+X^(−σ)) Qχ/(σ H) ≪ N^(−σ)Qχ under GRH(N). By the bounds following (6.12) the trivial and removed Euler-factor residues are O((L/H)x^(−1/2−σ)); this is O(N^(−σ)L) uniformly. Thus ∥gχ+pχ∥₂≪N^(−σ)L. Replacing the vertical measure with |1+σ+it|^(−2)dt only multiplies norms by bounded constants.
3. Orthogonality on n,m≤N/2 gives the polynomial covariance exactly equal to the diagonal with coefficient w(n)^2. Equality mod N forces n=m; opposition mod N is impossible except for the zero-weight endpoint. Consequently ∥pχ∥_(χ,t)≪1/σ by Chebyshev Σ_{n≤y} Λ(n)^2≪y log(2y). The covariance difference has HS norm at most 2∥pχ∥₂∥gχ+pχ∥₂+∥gχ+pχ∥₂², by the rank-one triangle and Cauchy–Schwarz over χ. The last square N^(−2σ)L² is ≪ N^(−σ)L/σ since (σL)exp(−σL)≤1.
4. The omitted positive diagonal has trace ≪Σ_{n>x} Λ(n)^2 n^(−1−2σ) ≪ x^(−2σ)(L/σ+1/σ²) by partial summation; this is ≪N^(−2σ)L/σ. The trace dominates the HS norm.
5. On w=2σ+i(t−y), |A_N(w)|≪1/σ by the all-prime product comparison in Proposition 6.5. Its proof gives |ζ(1−w)|≪σ^(−1)(2+|t−y|)^(2β), and |X1|≪1. Retain the factor N^(−2σ) instead of discarding it. The squared height majorant (2+|t−y|)^(4β)/[(1+t²)(1+y²)] has an absolute finite integral since 4β<1. Hence ∥Kσσ∥HS≪ S N^(−2σ)/σ². The triangle inequality completes (O1).
6. At σ=α neither damping factor tends to zero. The source's double Mellin test also has an N^σ multiplier in each variable, so a naive contour shift does not transfer the block's decay to the Goldbach pairing. No argument permits extrapolation across the narrow layer with uniform constants.

## Exact low-scale zero forms

For smooth compactly supported real weight profiles f,g with both additive supports in (0,N/2), use the polarized versions of (7.2)–(7.12), without the original Goldbach support restriction. The support/symmetry of the original cutoff enters only in the last evaluation; the general signed continuum model samples both difference convolutions minus the sum convolution at kN, k≥1. Its Mellin residue at w=1 still vanishes: integration of the two differences partitions the product mass, equal to the integral of the sum convolution. Arithmetic P−D vanishes identically against these tests since n≡m implies n=m and n≡−m is impossible. The continuous K terms likewise vanish on the support. Thus the residual form vanishes exactly for each such pair (and by continuity on the closed span of these Riesz test vectors). This is not a claim that applying T to that span gives zero, nor does it control any off-diagonal block.

## Assessment

The novel estimate is a decay theorem for Bσσ in the interior, in contrast to bounding P,D,K separately everywhere. It leaves precisely unestimated left-boundary covariance cancellation as well as mixed control needed for the whole-space norm, and cannot imply S or R. Additional detailed first-period projections are handled separately by the spectral lane. This is a deductive derivation, not a numerical test.

## Additional theorem: the true Beta component has operator norm of exact logarithmic order

For all sufficiently large even N on the source's strip, ∥K_N∥op ≍ log N. This is a statement about **K**, not E or T. The Beta kernel and its Hardy-space realization use no GRH: its Hermitian analyticity and integrable boundary growth are explicit, so the construction of the kernel action applies verbatim. Under GRH(N), one may simply use the separate operator in Proposition 6.5.

Proof of the upper bound. For w=r+iu with 0<r≤2β, put C_N(w)=S A_N(w)/ζ(1+w). After removing the p=2 factor, for p∤N the Euler multiplier is (1+p^(−w)/(p−2))(1−p^(−1−w))=1+O(1/p²). For p|N, p>2, the multiplier is (p−1)(1−p^(−1−w))/(p−2). Its modulus is bounded by 1+O(1/p²+min(1,|w|log p)/p), by subtracting its value at zero and using |1−exp(−w log p)|≤min(2,|w|log p). Hence |C_N(w)|≪1 if |w|≤1/loglog N, and |C_N(w)|≪(loglog N)^c globally for some absolute c. Indeed ∑_{p|N}(log p)/p≪loglog N and ∑_{p|N}1/p≪logloglog N+1, by splitting at log N, Chebyshev/Mertens for the small primes, and ∑_{p|N}log p≤log N for the rest.

Each boundary pair has w=σ_1+σ_2+i(t−y). In the near region |w|≤1/loglog N use the simple zeta poles to bound |ζ(1+w)ζ(1−w)|≪|w|^(−2). The remaining factors (π/N)^w, X1(s), X1(conj z), and the H² kernel denominators are uniformly bounded. Schur's test against Lebesgue measure on each line gives O(1/(σ_1+σ_2)) via ∫ du/(r²+u²)=π/r. In the complementary region, Euler summation at 2+|u| bounds |ζ(1+w)ζ(1−w)| by C(2+|u|)^(2β)[log(2+|u|)+1/|w|]^2. As 1/|w|≤loglog N, the source's boundary denominators and 4β<1 yield HS norm ≪(loglog N)^(c+2). Combining the four ambient blocks gives O(log N), also on the Hardy trace subspace.

Proof of the lower bound. Take s_0=2α real, so eventually α<s_0<β. For positive real w=4α, C_N(w)≳1 uniformly: each Euler multiplier for p>2 is at least 1, while 2C₂(1−2^(−1−w))≥C₂. Thus |ζ(1+w)ζ(1−w)|≍α^(−2), (π/N)^w≍1, X1(s_0)≍1. The weighted kernel on (s_0,s_0) has magnitude ≳α^(−2). The point-evaluation Riesz kernel k_{s_0} has squared norm, by Lemma 5.2, equal to (2π)^(−1)∫e^(2s_0 τ)/(e^(2ατ)+e^(2βτ))dτ ≪(s_0−α)^(−1)+(β−s_0)^(−1)≪α^(−1). The model section is an H² vector by its vertical decay; applying reproduction in both variables gives ⟨K k_{s_0},k_{s_0}⟩=K(s_0,s_0)/|1+s_0|². The norm quotient is therefore ≳α^(−1). This proves the two-sided result. Together with the independent diagonal estimate, it confirms the actual component scales and why separate-component bounds cannot prove S. No lower bound for ∥P−D−K∥ follows.

