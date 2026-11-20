# Round 5: isolate the all-mode long-range coupling and its zero residues

The notation and normalization are those of the [Li–Liu manuscript](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf). Use local GRH(N), L=log N, α=1/L, β=1/8, Δ=β−α, S=the Goldbach singular series. Work in the unitary log-coordinate Hardy realization, with x the log of raw additive size (x=log(Nu) in normalized physical coordinate u). Fix 0<κ<1/2 and take N sufficiently large depending on κ. Let A=P−D−K be the signed operator after compression to x≥0. The discarded sector costs O(S N^(−3/4)) including crosses, by operator-round2.md. The following separates long-range and short-range tests uniformly in all log profiles, but does not bound the critical remaining terms.

## 1. The diagonal and Beta model are exponentially small off the logarithmic band

For B>0 and for each J=D,K, the kernel (with both Hardy weights included) satisfies

    || 1_{x,y≥0, |x−y|≥B} J(x,y) ||_{L²(dxdy)} ≪_κ L² e^(−κB).          (1)

For concreteness consider x−y≥B. The ambient α×α kernel has two holomorphic Mellin coordinates (the second is the reflection of the height input). Shift their real parts from (α,α) to (α−κ,α+κ), keeping w=s+z fixed. For the diagonal D(w), the absolutely convergent Dirichlet series stays on Re w=2α. In the model K of (2.12), all density, ζ and (π/N)^w factors likewise retain their real parts. The gamma factors X₁(s),X₁(z) have no poles on this move: first positive poles are at 3/2, while α+κ<3/2. The two (1+s),(1+z) weights have no poles on it either. To justify the simultaneous shift distributionally, pair with compact smooth product tests in x,y, change coordinates from (s,z) to (s,w), and move the s line with w fixed. The rapid vertical decay of the Mellin transforms of the tests and polynomial growth of the kernels justify Fubini and vanishing horizontal contributions. Thus the α×α inverse-height kernel is the shifted one times exp(−κ(x−y)); equality holds locally as distributions and hence a.e. once HS integrability is checked.

On the shifted lines the weighted diagonal kernel has HS norm O_κ(L²) by D(2α)≪L². The Beta bound on the unshifted factor (π/N)^w S A_N(w) ζ(1−w) is O(L²(2+|t−v|)^(2α)) at height t,v. Stirling gives |X₁(α−κ+it)|≪_κ(2+|t|)^(κ−α), and |X₁(α+κ−iv)|≪_κ(2+|v|)^(−κ−α). Divide by the two linear denominators. Using (2+|t−v|)^(4α)≪(2+|t|)^(4α)(2+|v|)^(4α) in the squared kernel, the first height exponent above its inverse quadratic denominator is 2κ+2α<1 for sufficiently large N; the second is −2κ+2α<1. Hence the shifted kernel has HS norm O_κ(L²). On the positive log quadrant the passage from the ambient kernel to the true log kernel multiplies by sqrt(W(x)W(y)), W(t)=1+e^(−2Δt); this is bounded by 2. The other half follows by adjunction. This establishes (1) and is not restricted to fixed smooth window profiles.

## 2. What survives the identical shift for the character covariance

For a line of real part a used below, let f_{χ,a}(x) be the unitary inverse height Fourier transform, with kernel e^(itx)/sqrt(2π), of gχ(a+it)/(1+a+it), where gχ(s)=L′/L(1/2+s,χ). The ambient character kernel is Av_χ f_{χ,α}(x) conj(f_{χ,α}(y)), the average over all odd characters modulo N. Define the zero distribution

    Z_χ(x) = Σ_γ m_χ(γ) e^(iγx)/(1+iγ),

where γ runs over distinct ordinates of primitive nontrivial zeros of the inducing primitive odd character and m_χ is the multiplicity. The sum is interpreted against compact smooth tests, not by absolute pointwise summation. Then

    f_{χ,α}(x) = e^(−κx) f_{χ,α−κ}(x) + sqrt(2π)e^(−αx) Z_χ(x),
    f_{χ,α}(y) = e^( κy) f_{χ,α+κ}(y).                                 (2)

For the first identity, move the line for gχ(s)/(1+s) from α to α−κ. Under GRH(N) the only poles crossed are s=iγ, with residues mχ(γ)/(1+iγ). Removed-Euler zeros have Re s=−1/2, trivial zeros of the primitive odd L function have Re s≤−3/2, and 1+s stays nonzero. On compact smooth log-coordinate tests, the Mellin transform of the test has rapid decay, and horizontal lines avoiding the ordinates, as in the proof of (6.12), justify the contour limit. Explicitly, local zero counts allow a sequence separated from ordinates by a small inverse power of log(2+N|t|); the Hadamard logarithmic derivative bound on these segments is polynomial in log(2+N|t|), sufficient for vanishing contributions. The residue sum converges absolutely on tests by the same local zero counts. The sqrt(2π) factor is from the unitary Fourier normalization. No poles are crossed on the right shift, giving the second identity. Both are equalities of distributions; in particular Zχ is represented by a locally L² function by (2).

On a=α+κ the Dirichlet logarithmic derivative has the usual O_κ(log(N(2+|t|))) bound from the Hadamard comparison with the absolute convergence line, by distance from the critical line. On a=α−κ≤−κ/2 the same bound follows by the functional equation for the odd primitive logarithmic derivative to the line −a≥κ/2 in s coordinates. Gamma and conductor terms are O_κ(log(N(2+|t|))); imprimitive corrections are O_κ(log N) on 1/2+a≥1/2−κ>0 by summing the absolute Euler-factor logarithmic derivatives (and using ∑_{p|N}log p≤L). Thus ||f_{χ,α±κ}||₂≪_κ L uniformly in χ. The contribution of the first term of (2) to the covariance on x−y≥B has HS norm ≪_κ L²e^(−κB), by shifting the right factor and using the product of these norms, then averaging. The true Hardy factors on x,y≥0 are again bounded. Define the Hermitian kernel Z on the positive quadrant away from x=y by

    Z(x,y)=sqrt(2π W(x)W(y)) e^(−αx) Av_χ[ Z_χ(x) conj(f_{χ,α}(y)) ] (x>y),
    Z(x,y)=conj(Z(y,x))                                            (x<y).

By (1) and (2), its far-band restriction lies in L², and

    || 1_{x,y≥0, |x−y|≥B} ( A(x,y)−Z(x,y) ) ||₂ ≪_κ L²e^(−κB).         (3)

Equivalently one may replace Z in (3) by P using (1). Version (3) identifies the exact crossed-pole obstruction to the contour shift; the character term does not admit the pole-free proof used for the two other terms. An absolute sum over the atoms of Zχ is not a valid bound: the usual zero count for every fixed primitive odd Dirichlet L function gives divergence of ∑_γ mχ(γ)/|1+iγ|. A phase-sensitive estimate for the family-average covariance or its operator projection is needed. This does not assert that such cancellation is logically independent of GRH(N).

## 3. An exact audit rule for the growing matrix

Fix A₀>0 as the desired inverse-log exponent (e.g. the rate of h(N)=L^{A₀}), and take the Round 4 matrix M for accuracy o(L^(−A₀)), on the log band [0,Y], with cell lengths at most d≤1 and centers c_i. For example use A=A₀+1 in operator-round4.md. Let η be any fixed smooth real even cutoff equal to 1 on [−1,1] and 0 off [−2,2]. Take B=(A₀+4)κ^−1 log L. Split the finite Hermitian matrix into

    M_near,ij = η((c_i−c_j)/B) M_ij,
    M_far,ij  = [1−η((c_i−c_j)/B)] M_ij .

This particular cutoff is important: entrywise multiplication by the near mask is bounded in operator norm by a constant independent of dimension, B or centers. Fourier inversion writes the map as an integral of unitary diagonal conjugations diag(exp(it c_i/B)) with integrable coefficients proportional to the Fourier transform of η. The far map is bounded by 1 plus the same constant. Hence ||M|| is bounded by the sum of the two norms, and each is bounded by a constant times ||M||.

Let M_far^Z be the same far mask applied to the log-cell integrals (with normalized indicator vectors) of Z instead of A, defining the masked entries as zero where the factor vanishes. Every retained cell pair has |x−y|≥B−2d, so (3), B≫1, and Hilbert–Schmidt contraction by orthogonal compression give ||M_far−M_far^Z||≪_κ L²e^(−κ(B−2d))=o(L^(−A₀)). The same assertion holds using the finite compressed P instead of Z. In particular the finite, all-mode equivalence is

    ||T_N|| = o(S L^(−A₀))  iff  ||M_near|| + ||M_far^Z|| = o(S L^(−A₀)).

There is an analogous equivalence in big-O up to constants. The norm threshold with exact coefficient 1 still needs a positive margin and an actual numeric estimate. Neither test on the right is presently bounded at that rate. The first is the signed cancellation on nearby log scales, the second is raw (or zero-residue) covariance across distant log scales. Any actual rate claim based on bounding signed discrepancies separately on one common smooth profile leaves the operator-norm condition on this finite near/far matrix unchecked. In particular, even after eliminating reciprocal-density and Gamma contributions off-band at earned inverse-log accuracy, the off-band family covariance itself is not small by the shift. No proof or refutation of S or R is supplied.
