# Uniform intermediate-scale sampling bounds (Round 4 working note)

**Status.** Local GRH(N) is needed to identify the arithmetic bilinear form with the Hardy operator and for the paper's separate character Gram bound. No average over N, S or R is assumed in the following estimates. They remove a hyperbolic region of cross interactions and certain within-cell fluctuations, not the coarse-scale residual. There is no proof or disproof of S/R.

Keep N even, L=log N, α=1/L and β=1/8. Use the common physical unitary coordinates of source-round2.md. An arithmetic test f on the dimensionless physical axis u=n/N corresponds, up to the fixed factor (2π)^(-1/2), to √w a_f in L²(du), with

    a_f=f/2−u f',   w(u)=1/((Nu)^(-2α)+(Nu)^(-2β)),
    f(u)=√u∫_u^∞ a_f(v)v^(-3/2)dv.

Denote the unitarily conjugated T_N by H. Compact smooth arithmetic tests are dense; estimates below extend by continuity. For unit tests the last identity implies |f(u)|≪u^(-1/2) if Nu≥1, and ≪N^(-β)u^(-1/2−β) otherwise. In particular, ∫₀^{M/N}|f|≪√(M/N) for M≥1 and ∫₀¹|f|≪1. If the physical L² data vanish above u_0 then so does f. Integration by parts also gives ∫wu²|f'|²≤∫w|a_f|² because w is increasing and the difference equals ∫(3w/4+uw'/2)|f|² for compact tests.

## A. A hyperbolic region whose contribution is small for every N

For any 1≤M≤N/4 and K≥1 define the prefix-to-prefix cross operator

    C(M,K)=1_{Nu≤M} H 1_{v≤K}.

Then uniformly

    ∥C(M,K)∥ ≪ S(N)√(MK/N) · log(2NK)/log(2 max(M,K)).        (A1)

This is a bound on the full block including its physical interface vectors, not just on particular smooth probes. After removal of the exact diagonal only m=kN±n with k≥1 and k≲1+K can occur. For normalized test data the envelopes above give |f(n/N)|≪√(N/n), |g((kN±n)/N)|≪k^(-1/2). For the continuous model ∫₀^{M/N}|f|≪√(M/N) suffices and ∑_{k≤1+K} S(kN)/√k≪S(N)√K. The last estimate follows by partial summation from the nonnegative divisor expansion S(kN)/S(N)=∑_{d|k}a_{N,d}, with a_{N,d}=μ²(d)∏_{p|d}(p−2)^(-1) on (d,2N)=1, zero off that support; ∑_d a_{N,d}/d≪1 absolutely.

For the discrete part use either of two complementary upper sieve estimates. First fix k, take n∈[U,2U], U≤N/4 (intersect with the actual input). On this dyadic segment

    ∑ Λ(n)Λ(kN±n) ≪ S(kN) U log(2NK)/log(2U).

Apply the standard two-dimensional upper sieve on an interval of size U, with cutoff U^{1/c} for a sufficiently large fixed c and level U^{1/2}; there is one excluded residue if p|kN, two otherwise. Squarefree progression errors are O(2^{ω(d)}). All outputs/input prime powers with both bases above the cutoff pass the sieve; each such pair has weight O(log(2U)log(2NK)). For powers with a small base p≤U^{1/c} in either argument the sum of its own Mangoldt weight up to T is ≤log T per p; multiply by the other argument's maximum weight. Total bad weight is O(U^{1/c}log(2U)log(2NK)), absorbed for every U≥2. Small U is trivial. Sum dyadics with 1/√n and then k with 1/√k; this proves (A1) with denominator log(2M).

Alternatively fix n coprime to N and sieve k∈[V,2V] in the single form kN±n. For each p∤N there is one excluded residue, none at p|N. The same upper sieve and small-base argument give ∑_k Λ(kN±n) ≪ (N/φ(N))V log(2NV)/log(2V). Here N/φ(N)≪S(N); the factor from the even prime is a fixed constant and the Euler ratios at odd primes are bounded. The dyadic summation with 1/√k, followed by Chebyshev's ∑_{n≤M}Λ(n)/√n≪√M, yields denominator log(2K). Taking the better result proves (A1). The model is absorbed since log(2NK)≳log(2max(M,K)).

**Simultaneous hyperbolic mask.** Partition small physical input Nu into dyadic bands P_i and output v into dyadic bands Q_j (i,j≥0), with the bottom cells extending to zero and respective upper bounds 2^{i+1},2^{j+1}. Use only rows with 2^{i+1}≤N/4; a final partial row up to N/4 is also permitted with harmless constants. For T≥2, the *single* operator sum

    A_T=∑_{2^{i+j}≤T} P_i H Q_j

satisfies ∥A_T∥≪ S(N)√(T/N) log(2N(2+T))/log(2T). Indeed (A1) bounds each block by a constant times S(N)log(2N(2+T)) N^{-1/2}·2^{(i+j)/2}/(1+i+j). In each row and column the sum of this scalar geometric envelope is dominated by its endpoint at floor(log₂T), even for truncated rows. The block Schur test gives the claim without an extra factor for the number of bands. For polynomial T with T=o(N/h(N)²) and log T comparable to L, this is o(S(N)/h(N)). Only the masked interactions are controlled.

## B. Orthogonal fine fluctuations deep inside the large-scale region

Fix 0≤θ<1/2. Starting at J≥2, arrange a partition of [J,∞) into consecutive cells I=[u_I,u_I+B_I] with B_I comparable to u_I^θ and B_I≥1 (e.g. B_I=u_I^θ). Let F_J be the orthogonal projection on the closed direct sum of {v_f:f∈C_c^∞(I°)} over these cells. They are orthogonal by the local norm formula. This is not the entire physical high half-line: in each L²(I) the closed image has codimension one. Its orthogonal complement on that cell represents the endpoint condition ∫_I a_f(u)u^{-3/2}du=0 imposed on the image (the complement vector is proportional to w(u)^(-1/2)u^{-3/2}1_I). Indeed the tail integral formula reconstructs either vanishing endpoint from the other and this condition.

We claim the full-row estimate

    ∥F_J H∥=∥H F_J∥
      ≪_θ [L^{3/2}(1+log(2J)/L)+S(N)log(2+J)] J^{θ−1/2}.      (B1)

In particular θ=0 allows acting against *any* Hardy vector, not just against functions in separate rich cells. For J much larger than h²L³ with log J not excessively large, the fine tail can be below the S threshold. The precise test is the displayed expression, not this illustrative comparison.

**Arithmetic character part.** Let P be the positive character Gram operator. For a compactly supported arithmetic test g define the finite residue vector

    E_r(g)=∑_{m≡r (N)}Λ(m)g(m/N)−∑_{m≡−r (N)}Λ(m)g(m/N),  r a unit.

The odd-character Parseval identity gives ∑_r|E_r(g)|²=2N⟨P v_g,v_g⟩≪NL²∥v_g∥² by Li–Liu Proposition 6.5. It is essential to keep the ℓ² norm on residues rather than multiply a pointwise GRH bound by the number of classes. With complex tests take the usual conjugations.

For f supported in one cell, the H¹ derivative estimate and f=0 at cell endpoints yield ∥f∥∞≪√B_I/u_I ·∥v_f∥. A one-dimensional upper sieve in the physical interval of length NB_I gives

    ∑_{n/N∈I} Λ²(n) ≪ NB_I (log(2N u_I))²/L.

Indeed primes with base > (NB_I)^{1/c} pass a one-residue upper sieve on that interval; per-base weighted contributions from smaller prime powers are bounded by log(2Nu_I), as in A. Use the maximum Λ once more, and log(2NB_I)≥L. Each residue occurs O(B_I) times. Therefore the ℓ² norm over r of A_r=∑_{n≡r}Λ(n)f(n/N) is at most the square root of O(B_I) times the weighted square mass. Pair N^(-1)∑_r A_r conjugate(E_r(g)), to get

    |⟨P v_f,v_g⟩| ≪ √L log(2Nu_I) B_I^{3/2}/u_I ·∥v_f∥∥v_g∥.

For D, use positivity with ∥D∥≪L (arithmetic.md §3) and N^(-1)∑ Λ²|f|²≪B_I²(log(2Nu_I))²/(L u_I²)∥v_f∥². Each single-cell estimate for D is at most O(B_I log(2Nu_I)/u_I)∥v_f∥∥v_g∥, dominated by the displayed P bound.

**Continuous model against any g.** For fixed u∈I, K acts in its other test coordinate by sampling at positive v=u+k, u−k, k−u with signs +,+,− respectively and weights S(kN), k≥1. The cumulative signed mass on 1≤v≤V is O(S(N)log(2+u+V)). To see this, the divisor expansion above gives

    ∑_{k≤t} S(kN) = c_N t+O(S(N)log(2+t)),   c_N=S(N)∑a_{N,d}/d.

Here ∑_{d≤t}a_{N,d}≪log(2+t) by the Euler product up to t and Mertens; partial summation bounds t∑_{d>t}a_{N,d}/d by the same order. In the continuous replacement of the three k-intervals (positive real k), their signed lengths total zero because the two positive differences partition the whole v interval except one point and the negative sum covers it once. Integer endpoints only cost O(S(N)log(2+u+V)). Abel summation against compact g and ∫₁∞v²w(v)|g'|²≤C∥v_g∥² give a contribution O(S(N)log(2+u)∥v_g∥) per u: use w(v)≥1/2 and ∫₁∞ log²(2+u+v)/v² dv≪log²(2+u). Any boundary atom at 1 is harmless. For 0<v<1 there are O(1) samples per u, with coefficients O(S(N)loglog(5+u)) (from the standard pointwise bound for S(k)). Their integrals over the u-cell are O((1+B_I)S(N)loglog(5+u_I)∥v_g∥): on each unit subinterval the sample is g({u}) or g(1−{u}), and ∫₀¹|g|≪∥v_g∥. Multiplying by ∥f∥∞ shows the single-cell K contribution is O(S(N)log(2+u_I) B_I^{3/2}/u_I) in normalized units.

Finally apply Cauchy–Schwarz in the orthogonal cell components of f; ∑ B_I³/u_I² times the squared slowly varying coefficients is bounded by the corresponding integral ∫_J∞ u^{2θ−2}du with its log weights. This converges for θ<1/2 and gives (B1). Taking θ=0, J a large fixed power of L and a sufficiently slow h gives a genuine uniform reduction to one mode per high unit cell plus the low prefix. It leaves infinitely many coarse modes and their signed interactions.

**Even cheaper if both sides are fine.** For unit cells indexed by integers i,j≥1 only O(1) integer shifts meet a pair of cells. With the common 1/i and 1/j test-supremum bounds, the two-form sieve of A on n ranges of length N (starting at iN) gives a block norm at most

    O(S(N) [(1+log(2i)/L)(1+log(2j)/L)/(ij)] loglog(5+i+j)).

The continuous model is bounded by this order as well; k=0 is absent because the exact diagonal was removed. In the sieve the large-base weights are log(2Ni),log(2Nj), and the small-base terms are bounded by the same products times N^{1/c}, independently of the locations of the cells. Dominating loglog(5+i+j) by a constant times the sum of its i and j versions gives a sum of two positive separable comparison matrices. Its squared-summable row factors yield ∥F_J H F_J∥≪ S(N)(1+log(2J)/L)²loglog(5+J)/J for unit cells. This sharper two-sided estimate is not interchangeable with the full-row bound (B1).

**Unresolved:** cells with nonzero endpoint mode on both sides, slopes whose product lies at or above the hyperbolic threshold, and the possible exceptional moduli for averaged central windows. No RH-type spectral bound follows yet.
