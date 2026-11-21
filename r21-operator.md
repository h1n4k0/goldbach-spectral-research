# Post-R20 operator lane: exact coarse bridge covariance and a proved near-cell deletion

**Scope.** We work on the true microscopic-to-exterior cross from r20-operator.md, now on the actual retained coarse coefficients, not on a toy spectrum. The statement estimates the contributions from pairs of equal or nearby physical high cells in the squared coarse crossing. It identifies the exactly weighted, well-separated signed covariance and the one remaining uncentered direction. Neither of those two terms is bounded here. No remote writes. Local GRH(N) is used for the Li–Liu Hardy identification and to justify convergence on the infinite exterior. The new estimates on finite prime sums are unconditional and use no averaging over N.

Let L=log N, α=1/L, β=1/8, S=S(N), δ_N=sqrt(S/N)L^(3/2), and fix 0<γ<1 and Y=N^γ. The low physical projection is P_U=1_(0,U/N] with 1≤U≤min(Y,N/4), and the exterior projection is Q_Y=1_[Y,∞). Thus U is raw n scale and Y dimensionless physical scale. We use unit high cells I_j=[y_j,y_j+1), y_j=Y+j, j=0,1,..., and the true r20 coarse basis

    w_N(x)=[(Nx)^(-2α)+(Nx)^(-2β)]^(-1),
    r_N(x)=x^(-3/2)w_N(x)^(-1/2),
    c_j=||r_N 1_(I_j)||₂,   e_j=c_j^(-1) r_N 1_(I_j).

For every unit n≤U define the actual signed opposite-progression prefix

    A_n(y)=Σ_(m≤Ny) Λ(m)sqrt(m/N) [1_(m≡n mod N)−1_(m≡−n mod N)].

Here the residues themselves guarantee m is a unit. On the low output Hilbert space L²((0,U/N],dx) set

    b(y)(x)=(2π/N) r_N(x)
              Σ_(n≤Nx,(n,N)=1) Λ(n)sqrt(n/N) A_n(y),
    b_k=b(y_(k+1))−b(y_k).

These are genuine signed increments on high cells, with weights unchanged from the cumulative physical kernel. Define the sampled coarse map R:ℓ²(j≥0)→L²((0,U/N]) by columns R e_j^seq = c_j b(y_j). It is an actual o(δ_N) approximation in HS to the complete microscopic-to-exterior crossing after embedding the high coarse coordinates (see §1).

Put c=(c_j)_j, let F_c project in ℓ² onto c^⊥, and set W_k=Σ_(j>k)c_j² for k≥0, W_-1=Σ_(j≥0)c_j². The exact covariance of R F_c is

    (R F_c)(R F_c)^* = Σ_(k,l≥0) Γ_(k,l) b_k⊗b_l,
    Γ_(k,l)=W_max(k,l)−W_k W_l/W_-1,                             (1)

with simultaneous square cutoffs for the sum. The projection removes one direction, not a formal centering by an unweighted cell average. The removed direction is explicitly

    R(c/||c||)=||c|| b(Y) + Σ_(k≥0) [W_k/||c||] b_k.              (2)

For every integer D≥0 let C_near be (1) restricted to |k−l|≤D, and let C_far be the remaining separated-cell sum. Then uniformly in N,U,D,

    ||C_near|| ≤ ||C_near||_1 ≪_γ (D+1) S (U/N) L².               (3)

In particular if (D+1)U=o(L), the true norm of the microscopic-to-exterior crossing on the high coarse subspace c^⊥ differs from sqrt(||C_far||) by o(δ_N), and the full crossing is o(δ_N) if and only if this separated covariance is o(δ_N²) and (2) is o(δ_N). This is a genuine deletion of the signed same-cell and short-separation covariance at the R scale. **The R-scale deletion does not cover R20's polynomial U=N^(3/40)**, even with D=0. For that U the numerical estimate in (3) is still an inverse-polynomial error in the squared norm, hence negligible at any fixed inverse-log S rate (for fixed D, or modest polynomial D). The separated covariance and the direction (2) remain unknown at either scale. No full R/S conclusion follows.

## 1. Verify the sampled coarse map and the initial direction

In the exact physical coordinates of r20-operator.md, odd character orthogonality gives the character covariance kernel on the crossing as K_P(x,y)=r_N(y)b(y)(x). Indeed the product of the two true Volterra atoms is (2π/N²) r_N(x)r_N(y) times the double Λ(n)Λ(m)sqrt(nm) sum, with signed congruence 1_(m≡n)−1_(m≡−n), and the square-root normalization in A_n and b puts this in the displayed form. Both residues occur with their real signs; no new centering is used. The diagonal and Beta differences on the entire microscopic crossing are respectively

    O(log(2U) U/(NY)),     O(S loglog(5+Y) sqrt(U/(NY)))

in HS, by r20-operator.md §2. They are o(δ_N) for U≤Y=N^γ. Replacing b(y) by b(y_j) in each cell incurs HS O(log(2NY) sqrt(U/(NY))=o(δ_N): each n has O(1) partners m≡±n in that unit physical cell, the change in their weighted sum is at most O(sqrt(y) log(2Ny)), and Chebyshev on the low weighted sum gives the envelope log(2Ny)/(y sqrt(w_N(x)w_N(y))) after the kernel factors. The low x integral is O(U/N), even below 1/N, and the high y integral of log²(2Ny)/y² is O(log²(2NY)/Y). Thus replacing the true T by R composed with the exact high coarse coefficient map is an actual o(δ_N) error in HS. This does not first drop coarse modes.

Let u_k=(c_j 1_(j>k))_j. With inner product linear in the first slot and rank-one a⊗b mapping f↦⟨f,b⟩a, the finite increment formula is b(Y)⊗c+Σ_(k≤K)b_k⊗u_k. As K→∞ this converges in HS to R. Indeed the entries are exact up to column K+1, and the remaining approximating columns are the single frozen value b(y_(K+1)) times the tail c_j. Their HS mass tends to zero at fixed N: by GRH(N) and the character explicit formula, A_n(y)≪_N y(log(2Ny))² (uniform constants in N not needed for this convergence), giving ||b(y)||≪_N y(log(2Ny))², while ||(c_j)_(j>K)||≪_N y_(K+1)^(-1−α). The genuine tail also tends to zero since R is HS by the approximation above. There is no assertion of absolute convergence of the whole double covariance as a sum of trace norms.

Now ⟨F_c u_k,F_c u_l⟩ is exactly the real coefficient Γ_(k,l) in (1), since ⟨u_k,u_l⟩=W_max and ⟨u_k,c⟩=W_k. In particular 0≤Γ_(k,l)≤sqrt(W_k W_l). Taking simultaneous limits of the finite approximations to R F_c gives (1) in trace norm, since products of convergent HS operators converge in trace norm. Applying R to c/||c|| gives (2) in the same limit. These computations integrate the tail weight, rather than substituting c_k² or a unit cell count for W_k.

## 2. A genuinely per-progression Λ² bound, including the prime powers

For every V≥Y and every unit a mod N we need

    Σ_(m≤3NV,m≡a (N)) Λ(m)² ≪_γ S V log(2NV).                   (4)

For ordinary primes use [Montgomery–Vaughan's Brun–Titchmarsh inequality, The large sieve, Theorem 2](https://doi.org/10.1112/S0025579300004708) and bound the weight by log²(3NV). This gives O((N/φ(N)) V log²(3NV)/log(3V)), which is bounded as in (4) since V≥N^γ and N/φ(N)≪S by the explicit Euler factors.

Proper powers require care: dropping the residue constraint for squares at V=N^γ would give a bound ≫V when γ<1. Choose an integer J depending only on γ with J+1>2(1+1/γ). For each fixed exponent 2≤j≤J the number of unit roots t^j≡a mod N is ≤2 j^{ω(N)} (or a fixed multiple per prime power); use cyclic unit groups at odd prime powers and the product of a group of order two with a cyclic group at a power of 2. This is O_(J,ε)(N^ε) for every fixed ε. The count of positive t≤(3NV)^(1/j) in these roots is therefore O_(J,ε)(N^ε[1+(3NV)^(1/j)/N])≪_(J,ε) N^ε(1+sqrt(V/N)). Take ε<γ/4 and use V≥N^γ to get O_γ(V^(3/4)). Summing the bounded number of exponents and multiplying by log²(3NV) is still O_γ(V log(2NV)). For j>J all powers, even dropping congruences, number at most (3NV)^(1/(J+1))·O(log(2NV))≪_γ V^(1/2)log(2NV). Their squared Mangoldt weights are O(log²(3NV)), also absorbed as above. This proves (4) without GRH on any arithmetic progression and uniformly for arbitrarily large V.

For each fixed n and cell k, the increment A_n(y_(k+1))−A_n(y_k) sums at most a bounded number of terms in the two reduced progressions because the raw cell length is N. Cauchy over that fixed number bounds its square by O(y_k) times the sum of Λ(m)² in the same two raw residue segments (only y_k≥Y≥2 used). Sum over cells y_k∈[V,2V), disjoint in m, and apply (4):

    Σ_(V≤y_k<2V) |A_n(y_(k+1))−A_n(y_k)|²
        ≪_γ S V² log(2NV).                                  (5)

## 3. Norm of the nearby-cell band and the remaining signed condition

For fixed low x, apply weighted Cauchy to the low n sum in b_k(x) with the nonnegative weights Λ(n)sqrt(n/N). Their sum is ≪N x^(3/2) by Chebyshev (and is zero below 1/N). Use (5) uniformly in n before integrating. This gives

    Σ_(V≤y_k<2V) |b_k(x)|² ≪_γ S V² log(2NV)/w_N(x),
    Σ_(V≤y_k<2V) ||b_k||₂² ≪_γ (U/N) S V² log(2NV).

On each such dyad W_k≲V^-2 (NV)^(-2α), directly integrating r_N(y)^2 on y≥V. Summing V=2^jY, j≥0, gives

    Σ_k W_k ||b_k||₂² ≪_γ S (U/N) L²,                         (6)

since Σ_j log(2N·2^jY)(N·2^jY)^(-2α)≪_γ L² when Y=N^γ and α=1/L. Now 0≤Γ_(k,l)≤sqrt(W_kW_l) as shown above. For |k−l|≤D the trace norms of the rank-one terms sum to at most (2D+1)Σ_k W_k||b_k||² by Cauchy or 2ab≤a²+b². This proves (3) including absolute convergence of this particular near-band sum. The separated remainder C_far is therefore well-defined by the simultaneous-square limit in (1) minus that convergent near sum, not by silently asserting absolute convergence.

The covariance in (1) is positive, so its norm is ||R F_c||². By the triangle inequality for self-adjoint operators, | ||R F_c||²−||C_far|| |≤||C_near||. Comparing square roots, and then using the o(δ_N) *norm* approximation from §1, gives the claimed crossing estimate when (D+1)U=o(L). We do not multiply an o(δ_N) linear error by an unbounded norm to claim an o(δ_N²) squared error for the true T. The orthogonal splitting into c and c^⊥ gives the criterion for the full cross. The next unanswered operation at the R scale is real cancellation in the inertia-sensitive, well-separated signed matrix (1) together with (2), or some arithmetic substitute for it. No bound was proved for that separated signed term, for the initial coarse moment, or for the full high-high block.
