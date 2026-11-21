# R20: an every-modulus microscopic-to-fine exterior estimate, and the remaining true residue matrix

**Claim.** Use the manuscript's local GRH(N); none of the arithmetic estimates here uses global GRH for auxiliary moduli or an average over N. In the genuine unitary dimensionless physical coordinates, let P_U denote 1_(0,U/N] with 1≤U≤N/4 (U is a raw integer scale), and let Q_Y=1_[Y,∞) with Y≥2. Divide [Y,∞) into adjacent intervals I_j=[Y+jD,Y+(j+1)D), with 1≤D≤Y, and on each remove exactly one high cell direction, the normalized copy of r_N(y)1_{I_j}(y). Explicitly P_C is the orthogonal projection onto the direct sum of these coarse directions, and F_{Y,D}=Q_Y−P_C. Write L_Y=log(2NY). The following is a true full crossing to all exterior **fine** data:

    ||P_U T_N F_{Y,D}||_HS ≪ D L_Y sqrt(U/(NY)).                    (1)

Adjunction gives the reverse crossing. For any fixed 0<γ<1, set Y=N^γ, U≤Y, D=1. Then (1) is o(δ_N), where δ_N=sqrt(S(N)/N)(log N)^(3/2). It covers the unbounded exterior beginning at H=γ log N in the dimensionless log coordinate, and includes the original low endpoint x=0. This improves, on the microscopic input range, estimates for unrestricted rows of fine high cells; it does not bound their coarse directions or the full exterior. In particular γ=3/40 treats the polynomial exterior beginning at the last complete-prefix scale, though only for this low—fine crossing.

The full microscopic-to-exterior crossing P_U T_N Q_Y has a further quantitative reduction: after deleting the proved o(δ_N) fine term, its coarse part is the finite-dimensional weighted covariance of **actual signed zero residues** described in §3, with a total o(δ_N) HS error at the stated U,Y. Thus no spacing hypothesis or proxy covariance is used in identifying the remaining arithmetic target. We do not estimate that last covariance. No remote writes and neither S nor R is settled.

## 1. Bound the genuine fine crossing by cumulative increments

Write L=log N, α=1/L, β=1/8, S=S(N), and use the exact two-trace Hardy physical kernel from the manuscript and [source-round2.md](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/source-round2.md):

    w_N(x)=[(Nx)^(-2α)+(Nx)^(-2β)]^(-1),  r_N(x)=x^(-3/2)w_N(x)^(-1/2),
    K_T(x,y)=2π r_N(x)r_N(y)M_N(x,y),
    M_N(x,y)=∫_(0,x]×(0,y] sqrt(uv) dμ_N(u,v).

Here μ_N is the unit-restricted arithmetic-minus-model alias measure, the exact diagonal removed; the signs are + for either nonzero difference and − for the sum. On 0<u≤x≤U/N≤1/4, y≥Y≥2, the high output lines have v=k+u or v=k−u, k positive. The reverse difference with v=u−k is impossible.

Let y_j=Y+jD. On I_j subtract the row kernel 2π r_N(x)r_N(y)M_N(x,y_j), which is killed on the right by F_{Y,D}. The difference of the cumulative M_N values restricts m/N to (y_j,y], y∈I_j. In the arithmetic part, each low n≤Nx has O(D) possible partners because each permitted residue class has spacing N in m. Each partner has Λ(m)≤log(2Ny), and each sqrt(uv)≤sqrt(xy). For Nx≥1, Chebyshev therefore gives

    |Δ M_arith(x,y)| ≪ N^(-1)sqrt(xy) D log(2Ny) Σ_(n≤Nx) Λ(n)
                    ≪ x^(3/2)sqrt(y) D log(2Ny).

If Nx<1, the arithmetic increment vanishes. For the model part, the same counting of aliases for each 0<u≤x gives

    |Δ M_model(x,y)| ≪ S loglog(5+y) x^(3/2)sqrt(y) D.

Here k≈y on the interval since D≤Y, and S(kN)≪S(N)loglog(5+k) by the usual prime-factor product and Mertens. Also S(N)loglog(5+y)≪log(2Ny) uniformly: S(N)≪loglog N, and the product of the two logarithms-of-logarithms is bounded by a constant times log N+log(5+y). Combining both increments gives the uniform pointwise envelope for the difference kernel,

    |Δ K_T(x,y)| ≪ D log(2Ny)/(y sqrt(w_N(x)w_N(y))).

In the low integral, ∫_0^(U/N) dx/w_N(x)=N^(-1)∫_0^U (t^(-2α)+t^(-2β))dt≪U/N, using U≥1 and 2β<1. In the high integral, w_N(y)^-1≤2 on y≥Y and ∫_Y^∞ y^-2 log²(2Ny)dy≪L_Y²/Y. Thus the difference kernel is HS at the asserted cost. Since T_N itself is HS under local GRH(N), the piecewise subtracted kernel is also HS; it acts only on the specified coarse directions. Multiplying the difference on the right by the contraction F_{Y,D} proves (1) for all the infinitely many cells at once. No sum of individual cell operator norms has been substituted for a bound on their actual combined crossing.

## 2. Deterministic terms are small on the entire microscopic crossing

Write D_N, K_N for the exact diagonal and Beta model operators (the capital cell width D is unrelated). The exact diagonal physical kernel is

    K_diag(x,y)=2π r_N(x)r_N(y) N^(-2) Σ_(n≤N min(x,y),(n,N)=1) Λ(n)² n.

On 0<x≤U/N≤1/4<Y≤y, the weighted Chebyshev bound Σ_(n≤t) Λ(n)²n≪t²log(2+t) gives

    |K_diag(x,y)|≪log(2U) sqrt(x)/(y^(3/2)sqrt(w_N(x)w_N(y)).

Integration gives ||P_U D_N Q_Y||_HS≪log(2U) U/(NY), using ∫_0^(U/N) x dx/w_N(x)≪(U/N)².

For the Beta model retain its two signs. For each u<1/4, all k with k+u≤y contribute the signed difference sqrt(k+u)−sqrt(k−u)≪u/sqrt(k), and there are at most two incomplete endpoint integers k∈(y−u,y+u] with contribution O(S(N)sqrt(y)loglog(5+y)). The positive divisor expansion gives Σ_(k≤t) S(kN)≪St, hence Σ_(k≤t) S(kN)/sqrt(k)≪S sqrt(t). Thus the entire signed model inner sum is O(S sqrt(y)loglog(5+y)), rather than O(S y^(3/2)) obtained by summing both legs absolutely. Integrate sqrt(u) over 0<u≤x and restore r_N(x)r_N(y): the model kernel is bounded by S loglog(5+y)/(y sqrt(w_N(x)w_N(y))). Consequently

    ||P_U K_N Q_Y||_HS≪S loglog(5+Y) sqrt(U/(NY)).                (2)

The last high integral follows as above; with y=Yv, loglog(5+Yv) is bounded by loglog(5+Y)+O(log(2v)), and v^-2 makes it integrable. For U≤Y=N^γ both deterministic terms are o(δ_N) uniformly. This argument controls them including the retained high coarse directions, and is separate from the operator fine projection.

## 3. Exact arithmetic target on the retained coarse cells, at the natural height

In physical variables the covariance P_N is the average over odd χ modulo N of p_χ⊗p_χ, where

    p_χ(x)=−sqrt(2π) r_N(x) N^(-1) Σ_(n≤Nx) Λ(n)χ(n)sqrt(n).

This is the exact Volterra transform of g_χ(s)/(1+s) used in operator-round7.md, g_χ(s)=(L′/L)(1/2+s,χ). On the high coordinate y, shift the line from α to α−κ with fixed 0<κ<1/2 and α<κ. Use the genuinely crossed residues as in [operator-round5.md](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/operator-round5.md):

    Z_χ(u)=Σ_γ m_χ(γ)e^(iγu)/(1+iγ),
    p_χ(y)=sqrt(2π) y r_N(y) Z_χ(log(Ny)) + ε_χ(y),
    ||Q_Y ε_χ||₂≪_κ L(NY)^(-κ).

The equality of profiles uses y r_N(y)=y^(-1/2)w_N(y)^(-1/2), from undoing the logarithmic change of measure. Zero sums are distributions on compact smooth raw-log tests, and the displayed difference represents their locally L² realization. The primitive functional equation on a line a fixed distance to the left of the critical line, plus the absolutely bounded missing Euler factors in Re(1/2+s)>1/2−κ, gives shifted-height L² norm O_κ(L); the log multiplier (Ny)^(-κ) and bounded paired Hardy factor give the stated uniform remainder. The pole sign/constant are those of the contour residue in R5; imprimitive zeros at Re s=−1/2 are not crossed. By the averaged atom estimate (paper Prop. 6.5), (Avg ||p_χ||₂²)^(1/2)≪L. Hence the crossing P_U P_N Q_Y changes in HS by at most O_κ(L²(NY)^(-κ)) when high atoms are replaced by the written genuine residues. At any fixed γ>0 choose 1/[2(1+γ)]<κ<1/2; this error is then o(δ_N) for Y=N^γ.

For n in the finite set J_U={n≤U : (n,N)=1, Λ(n)>0} define the genuinely signed residue signal and its exterior coarse moments by

    Z_n(u)=Avg_odd χbar(n) Z_χ(u),
    c_j=||r_N 1_(I_j)||₂,       e_j(y)=c_j^(-1)r_N(y)1_(I_j)(y),
    ζ_(n,j)=c_j^(-1)∫_(I_j) y r_N(y)² Z_n(log(Ny))dy.

Thus ζ_(n,j) is the exact weight on the actual ordinates from the genuine cell geometry; it is not a single unweighted sample at log(Ny_j). Each row ζ_(n,·) is ℓ² by the preceding L² identity and the orthonormality of the disjoint e_j. Let G be the finite positive matrix indexed by J_U with G_(n,m)=Σ_j overline(ζ_(n,j))ζ_(m,j). Define B:ℓ²(J_U)→L²((0,U/N]) by

    (B a)(x)=r_N(x) Σ_(n∈J_U, n≤Nx) Λ(n)sqrt(n) a_n.

The residual matrix acts only on P_C and its action on any high vector with coordinates z_j=⟨f,e_j⟩ is x↦−(2π/N) B[Σ_j z_j overline(ζ_(n,j))]_n. This follows from multiplying the exact low p_χ(x) by the conjugated high residue and averaging, giving χ(n)overline(Z_χ)⇒overline(Z_n). Its operator norm is exactly (2π/N)||B G^(1/2)|| by forming the product with its adjoint. In particular the finite-column structure comes from true prime-power samples, not a global numerically rounded Hardy projection.

Combining (1), (2), the diagonal estimate, and the high-residue replacement shows that for D=1, U≤Y=N^γ (0<γ<1 fixed), the full microscopic-to-exterior crossing differs from this embedded matrix in HS by o(δ_N). Equivalently a bound of size δ_N with adequate margin would follow from ||B G^(1/2)|| sufficiently below Nδ_N/(2π). Neither R19's untranslated low-ordinate witness nor the motion of the one-sided contour estimates this genuinely translated weighted covariance. We have removed a large fine sector of the actual exterior and all fast errors at the R scale, but not the retained signed residue matrix or the other exterior directions.
