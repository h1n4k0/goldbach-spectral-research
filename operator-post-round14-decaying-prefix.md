# Post-R14: a larger complete prefix via GRH decay of the actual physical kernel

**Claim (global Dirichlet GRH).** Set X=8R², L=log X, N=2r², R<r≤2R, and let P_Y be the actual projection in dimensionless physical coordinates onto 0<x≤Y. For

    Y=X^(3/40),    τ=X^(-1/400),

one has, for every ε>0,

    #{r : ||P_Y T_N P_Y||_HS>τ} ≪_ε X^(193/400+ε).               (1)

For ε<7/400 this is a power-saving fraction of the ≍sqrt(X) moduli. The square is complete: all lower/upper and high/high within-prefix terms are included. In particular this independently closes the missing high-high block over X^(.01)<x,y≤X^(.05) left by [pinned Round 14](https://github.com/h1n4k0/goldbach-spectral-research/blob/c7e28563c459509a1a14676888bfc63cdf2bb1d8/ROUND14.md), and goes farther than its high endpoint. It does not use the optional extra fourth-moment theorem cited in Round 13. Global GRH is needed for the auxiliary major arcs. The new pointwise cap uses local GRH(N), which also identifies the true Hardy realization. This is not an all-N theorem, a global exterior estimate, or a proof or refutation of S or R.

## 1. A decaying cap for the whole signed kernel, not its unsigned arithmetic mass

In the actual coordinate of source-round2.md §1, put

    r_N(x)=x^(-3/2)w_N(x)^(-1/2),
    w_N(x)=[(Nx)^(-2/log N)+(Nx)^(-1/4)]^(-1).

Write the true signed kernel as K_T(x,y)=2π r_N(x)r_N(y) M_N(x,y), with M_N the weighted cumulative signed alias discrepancy. The three uncentered terms P,D,K_model of the original operator can be treated individually for a cap. We assert, uniformly for X^-1/4≤x,y≤X^(1/8),

    |K_T(x,y)| ≪ L⁴/(sqrt(xy)).                                  (2)

This is different from the earlier sieve cap O(S(N)), which bounds the positive and negative atoms by absolute masses. Character cancellation and sign cancellation in the explicit model are important for (2).

**Character covariance.** In physical coordinates its atoms are exactly

    p_χ(x)=−sqrt(2π) r_N(x)/N · Σ_(n≤Nx) Λ(n)χ(n)sqrt(n),

for the odd characters modulo N, and the kernel is the normalized average of p_χ(x)overline(p_χ(y)). This is the inverse Laplace transform of (L′/L)(1/2+s,χ)/(1+s), as in spectral-round2.md and operator-round7.md; the strip transformation includes both strip boundary weights. All these χ are nonprincipal. The standard uniform GRH character bound ψ(t,χ)≪sqrt(t)log²(N(2+t)) applies also for t<N: for t≥2, see [Montgomery–Vaughan, Multiplicative Number Theory I, Thm. 13.7, equation (13.19)](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/17.0_pp_419_451_Conditional_estimates.pdf). Equivalently the estimate follows from the explicit formula applied at height t to the inducing primitive character, the local zero count summed in unit shells, and the finite Euler correction O(log N log(2+t)). The bounded t case is immediate. This argument does not require the extra x≥q restriction present in some explicit-constant estimates. Abel summation then gives |Σ_(n≤Nx)Λ(n)χ(n)sqrt(n)|≪Nx L². Since Nx≫1 on the bulk, w_N≥1/2, so |p_χ(x)|≪L²/sqrt(x), uniformly in χ and x. The asserted cap follows for the averaged character term.

**Exact diagonal.** The physical atom for n^(-s)/(1+s) is sqrt(2π)r_N(x)(n/N)1_(n≤Nx); its kernel coefficient is Λ(n)²/n (with the unit restriction). Thus apart from bounded weights the diagonal kernel is bounded by

    (1/(N² (xy)^(3/2))) Σ_(n≤N min(x,y)) Λ(n)² n
     ≪ L min(x,y)²/(xy)^(3/2) ≤ L/(sqrt(xy)).

Here Chebyshev and partial summation give Σ_(n≤t)Λ(n)²n≪t² log(2+t).

**Model, with its three signs.** By symmetry take x≤y, and fix 0<u≤x. At each integer k≥1 the model coordinates v are u+k, u−k>0 and k−u>0 with signs +,+,− respectively, each truncated to 0<v≤y and weighted by sqrt(v). Write

    F_N(t)=Σ_(1≤k≤t) S(kN)=c_N t+O(S(N)log(2+t)),
    c_N=S(N)Σ_d a_(N,d)/d,

where a_(N,d)≥0 is the standard squarefree divisor coefficient in S(kN)/S(N). Indeed Σ_(d≤t)a_(N,d)≪log(2+t) by its Euler bound and Mertens, and t Σ_(d>t)a_(N,d)/d≪log(2+t) by partial summation. Inserting floors therefore gives the displayed estimate. For each of the three functions of k, the supremum plus the total variation is O(sqrt(y)) and k≤u+y. Under the continuous replacement c_N dk, the two positive charts partition all 0<v≤y (one above u, the other below u), while the negative chart covers the same range once; all three have |dk|=dv and the same sqrt(v) weight. Hence the replacement cancels exactly for every u,y. Abel summation leaves O(S(N)sqrt(y)log(2+u+y)) for the signed inner sum. The extra sqrt(u) integrated on 0<u≤x gives

    |M_model(x,y)|≪S(N)x^(3/2)sqrt(y)log(2+x+y).

Hence |K_model(x,y)|≪S(N)log(2+x+y)/y ≤ O(L²/sqrt(xy)) on the stated bulk, using S(N)≪loglog N. There is no omission of the reverse difference family for u>1. This proves (2).

## 2. Apply the actual signed thin-family estimate scale by scale

Fix any selected set E of M indices in the doubled-square dyad. Partition the bulk [a,Y]², a=X^-1/4, into dyadic physical rectangles (U,2U]×(V,2V], trimmed to the bulk as necessary, and use symmetry to take U≤V. The true residual kernel has support x+y≥1 by exact diagonal subtraction, so only rectangles with V≥1/4 can be nonzero. The short and long raw maximum scales are W=4UX, Z=16VX; use P=Z^(2/5), with absolute constants unimportant. This choice covers each signed alias k≤4V and all adaptive intervals in each rectangle. Here U may be below 1, but W≳X^(3/4) and log W≍L.

The [asymmetric selected rectangle estimate (3) of Round 14](https://github.com/h1n4k0/goldbach-spectral-research/blob/c7e28563c459509a1a14676888bfc63cdf2bb1d8/operator-post-round13-asymmetric-exterior.md) now gives, for every hard rectangle contained in the cumulative rectangle (0,2U]×(0,2V],

    Σ_(r∈E)|μ_N(rectangle)| ≪ C_E(U,V),

    C_E(U,V) = sqrt(M) sqrt(U) V^(7/4) X^(1/4+ε) P^(-1/4)
        + M[V sqrt(U/X) P L⁵ + V² (VX)^ε/P + V^(3/2)L² X^(-1/2)].       (3)

For clarity the reason that this use of the argument extends to a≤U<1 is the ψ(t,χ) bound uniform in t and conductor noted above, for all auxiliary q≤P; the earlier simplifying condition P<sqrt(W) is unnecessary. The principal error energy of the short leg on arcs of width P/(qZ) is O((W/Z)P²L⁵) by exactly the R14 finite Parseval and real-line Plancherel (endpoint term U_raw P/(qZ), variation term U_raw²(P/(qZ))² for U_raw=W). The long leg has energy O(P²L⁵); the principal transforms have squared mass O(WL) and O(ZL), so integrated mixed and double-error total O(sqrt(W)P L⁵), before normalizing by N. The individual centered Ramanujan and integral tails are O((VX)^(1+ε)/P). In the minor arc estimate the adaptive (collapsed) shorter interval dyadically decomposes in [0,W], and gives a square Parseval factor O(WL). The uncut longer factor uses only Vaughan with P=Z^.4; the R14 selected difference-of-squares fourth moment is unchanged by a fixed k. Proper powers and nonunits cost O(sqrt(Z)L²/X) per line. Sum over O(V) lines and normalize by N≍X to get (3). This uses each line centered before summing; no conjectural cancellation among distinct k is assumed.

Insert the positive layer cake for sqrt(uv) into the cumulative M_N to get Σ_E |M_N(x,y)|≪sqrt(xy) C_E. On the bulk w_N≥1/2, so Σ_E|K_T(x,y)|≪C_E/(xy). Multiply by the decaying individual cap (2) and integrate over this particular dyadic rectangle. The factors x^(-3/2)y^(-3/2) integrate to O(1/sqrt(UV)). Its selected squared HS mass is therefore O(L⁴ C_E(U,V)/sqrt(UV)). The leading term loses all dependence on U,

    sqrt(M) X^(3/20+ε) V^(23/20),

after absorbing L powers and using P≈(VX)^(2/5). The leading linear term is O(M X^(-1/10)V^(9/10)L⁹). The Ramanujan/integral tail after division by sqrt(UV) is O(M X^(-11/40+ε) V^(11/10)L⁴), using U^(-1/2)≤X^(1/8) up to a constant. The nonunit term is O(M X^(-3/8) V L⁶). All these powers are uniform for the stated charts. Summing all O(L²) rectangles costs only logarithms, using the same selected set E for each; there is no per-rectangle exceptional-set union or extrapolation from overlapping strips.

## 3. Endpoint, absorption, and the exception count

The genuine small endpoint min(x,y)<a has squared HS mass O(Y L⁴ X^-1/4) for each N by the elementary edge argument already audited in Round 14: the other coordinate is ≥3/4 if the kernel is nonzero, for min≥1/N the trivial per-integer bound across O(max) lines gives |K_T|≪L², and below 1/N it is model-only with integrable bound S(N)(N min)^(-1/8). Thus no region near x=0 is discarded from the theorem. With Y=X^(3/40), the major linear exponent −1/10+(9/10)(3/40)=−13/400, the Ramanujan linear exponent −11/40+(11/10)(3/40)=−77/400 (before ε), the nonunit exponent −3/8+3/40=−3/10, and the endpoint exponent −1/4+3/40=−7/40. Each is strictly below the target τ²=X^(-1/200) even after logarithms (choose the internal ε small for the Ramanujan tail).

Take E to be the actual exceptional set for the whole prefix with size M. Subtract these dominated linear terms. If M>0 we obtain

    M τ² ≪_ε sqrt(M) X^(3/20+ε) Y^(23/20).

After division and squaring this gives M≪_ε τ^-4 X^(3/10+ε)Y^(23/10) = X^(193/400+ε), with ε relabeled. The same proof restricted to the old high-high region with upper limit Y=X^(1/20) gives the smaller O(X^(17/40+ε)) bound at the same τ. It is a conclusion about the actual operator block, not an estimate on the separate high-side atoms at S precision.

## 4. Comparison and remaining obstacle

The published Round 13 optional fixed-weight theorem's already-transferred prefix condition b²τ^-2≤X^1/40 cannot be plugged in at this Y. This proof uses only Vaughan and improves the operator transfer by supplementing the signed collective arithmetic bound with (2); it does not require a stronger minor-arc theorem. Beyond the new Y it does not control P_Y T_N(1−P_Y), its adjoint, or the doubly exterior block. The very far cutoff from moving Hardy lines starts at much larger scales, and the exceptional set O(X^(193/400+ε)) can contain infinitely many moduli. Thus no uniform same-modulus signed prime covariance, nor global S/R, follows.
