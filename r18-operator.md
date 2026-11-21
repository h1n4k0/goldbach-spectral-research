# R18: sharp genuine mixed-tail decay at a fixed modulus, and a doubly exterior rank obstruction

**Scope.** Under the manuscript's local GRH(N), we prove two statements about the actual signed operator, not the deterministic benchmark alone. They quantify the far-tail obstruction; they give neither a violation nor a proof of S or R at its natural scale. The first lower bound is asymptotic in tail position for **fixed N** and its constant is not claimed uniform. This note starts from [pinned R17](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/ROUND17.md).

Let L=log N and α=1/L, β=1/8. Use dimensionless log coordinate x=log(n/N), and let Q_H project to x≥H in the true unitary log realization. The notation P,D,K denotes the character covariance, exact diagonal, and Beta operators in T_N=P−D−K. Write m_N(x)=w_N(e^x)^(-1/2)=[e^(-2α(L+x))+e^(-2β(L+x))]^(1/2).

1. For each fixed sufficiently large even N satisfying local GRH(N), there is a unit Hardy vector v_N supported in a short raw window around one unit prime p≪log N, and constants c_N>0,H_N<∞, such that

       ||Q_H T_N v_N|| ≥ c_N e^(-αH)                         (H≥H_N).      (1)

   In particular its support is inside each prefix n/N≤N^γ with γ>0 fixed, for large N. The corresponding logarithmic decay rate is exactly −α. One cannot replace the existing one-sided exponent by a strictly faster exponential in H uniformly for all large H at each such fixed modulus, even for this single genuine low input. This is compatible with an inverse-log small norm at H≈γ log N: (1) provides neither a uniform c_N nor a useful threshold H_N in that regime.

2. Uniformly in every sufficiently large admissible N, for H≥9L,

       ||Q_H T_N Q_H|| ≥ c e^(-2α(L+H)) L³/φ(N)².                         (2)

   Together with the two-sided shifted-line upper bound O((L+H)² e^(-2α(L+H))) below, this gives exact fixed-N logarithmic exponent −2α for the doubly exterior compression. The polynomially rescaled lower bound L³/φ(N)² is too small to settle S/R.

## 1. No simultaneous cancellation of all primitive residues in a nonzero character combination

Let χ run through all odd characters modulo the fixed N and χ* denote the primitive inducing character, of conductor dividing N. Distinct χ modulo N induce from distinct primitive characters (each primitive character has a unique inflation to modulus N on units). Suppose complex coefficients c_χ satisfy

    Σ_χ c_χ m_χ(γ)=0 for every ordinate γ,

where m_χ(γ) is the multiplicity of the nontrivial zero 1/2+iγ of L(s,χ*) and zero means no such zero. Then all c_χ=0.

To prove this, use the completed primitive L-functions with common odd gamma factor Γ((s+1)/2). They are entire of order one, and their zeros are exactly the nontrivial zeros. The logarithmic-derivative Hadamard formula is a constant plus the normally convergent sum of (s−ρ)^(-1)+ρ^(-1) away from zeros; the tails are absolutely convergent at fixed regular s, by the usual local zero count. The hypothesis cancels every zero term of the finite combination, so the combined completed logarithmic derivative is constant. On real s→+∞ all the uncompleted L′/L tend to zero, whereas ψ((s+1)/2) grows like log(s/2); the conductor terms are constants. The common gamma coefficient Σ c_χ must therefore be zero, and taking the same limit shows Σ c_χ (L′/L)(s,χ*)=0 identically. Uniqueness of the absolutely convergent Dirichlet series on s>1 gives Σ c_χ χ(p)=0 at every prime p∤N. Dirichlet's theorem supplies a prime in every unit class modulo N, so finite character orthogonality forces all c_χ=0. Neither simplicity nor disjointness of zeros across different Dirichlet L-functions was assumed.

## 2. A genuine prime input retains a nonzero slowly damped high output

Choose any prime p∤N, p≪L, which exists by Chebyshev's lower bound for the primorial logarithm (take a sufficiently large fixed multiple of L). Since N is even this p is odd. Choose a real smooth physical bump F supported in (p−1/2,p+1/2) in the raw coordinate, F(p)>0, and set f(u)=F(Nu). Normalize the genuine Hardy representing vector v_N=v_f/||v_f||. In the true physical L² coordinates its profile is proportional to sqrt(w_N)(f/2−u f′), so it is supported in the same raw window. The covariance atoms p_χ of the manuscript satisfy, by the exact Mellin formula (see pinned operator-round7.md),

    ⟨p_χ,v_f⟩=−N^(-1/2) Σ_n Λ(n)χ(n) f(n/N)
              =−N^(-1/2)(log p)χ(p)F(p).

The absolute former identity extends from the regular Mellin line by local GRH. In particular the coefficient vector c_χ=(2/φ(N))⟨v_N,p_χ⟩ in P v_N=Σ_χ c_χ p_χ is nonzero, including all complex conjugation according to the inner product's linear-first convention.

Recall the actual pole shift checked in [operator-round5.md §2](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/operator-round5.md). Using the raw log height u=L+x, define the zero distribution

    Z_χ(u)=Σ_γ m_χ(γ) e^(iγu)/(1+iγ)

(sum tested on compact smooth functions). Shifting g_χ(s)/(1+s), g_χ(s)=(L′/L)(1/2+s,χ), from α to α−κ for any fixed α<κ<1/2 crosses exactly the poles s=iγ. Imprimitive Euler-factor zeros have Re s=−1/2 and the trivial poles/denominator are farther left. With unitary inverse-height convention the residue is sqrt(2π)e^(−αu) Z_χ(u), with plus sign. The shifted transform itself lies in L² and is multiplied by e^(−κu); the normalized Hardy boundary factor sqrt(1+e^(−2(β−α)u)) is bounded on u≥0. Thus in the actual log L² representation

    Pv_N(x)=sqrt(2π)m_N(x) Z_c(L+x) + r_N(x),
    Z_c=Σ_χ c_χ Z_χ,     ||Q_H r_N||₂=O_N(e^(−κH)).             (3)

All these identities are distributional on compact tests; (3) is also a local L² identity. The estimate follows from L² on the shifted height lines by the functional equation a fixed distance off the critical line, or directly from R5 §2. Support of v_N lies at raw log n>0. By the anti-diagonal shift estimate in R5 §1, D+K across the gap from that fixed support to Q_H has HS norm O_N(e^(−κH)). Hence replacing P by T_N in (3) only changes the same error. This subtraction is essential; the slow tail belonged to the actual signed T_N after removing the faster deterministic crossing.

By §1, some coefficient b_(γ0)=Σ_χ c_χ m_χ(γ0)/(1+iγ0) is nonzero. Choose q∈C_c^∞(0,1) such that q(v)=e^(iγ0 v) η(v) for a nonzero real nonnegative smooth η. Put q_γ=∫ e^(iγv) overline(q(v))dv. The test of the zero distribution by a translate q(x−t) is

    Θ(t)=Σ_γ b_γ q_γ e^(iγ(L+t)),

an absolutely and uniformly convergent trigonometric series by the local zero count and rapid decay of q_γ. The frequency γ0 term is nonzero. For all H, averaging Θ(t)e^(−iγ0 t) on t∈[H,H+M_0] approaches b_(γ0) q_(γ0) e^(iγ0 L) as M_0→∞, uniformly in H: truncate the absolutely convergent series first, then the finitely many off-frequency averages are O(1/(M_0|γ−γ0|)). Fix M_0=M_0(N, q, c) large enough. Every interval [H,H+M_0] thus contains t where |Θ(t)| is at least half that coefficient magnitude.

For this t, use test g_t(x)=m_N(x)^(-1) q(x−t) in Q_H; its norm is comparable to e^(α(L+t))||q||₂ for all large t. Pairing T_N v_N with g_t and normalizing yields a main term of magnitude ≫_N e^(−αt), hence ≫_N e^(−αH) since t−H≤M_0, and an O_N(e^(−κH)) error by (3). Taking large H and κ>α proves (1). For fixed N the upper bound O_N((1+H)²e^(−αH)) already follows from the ordinary GRH ψ error in each atom and then squared integration; alternatively use the previously proved whole-row shifted-line upper. This gives the stated exact logarithmic rate. Neither the smallest noncancelled residue nor the frequency-isolation window M_0 is bounded uniformly here; assertions at growing N and H≈γL would require additional quantitative arithmetic.

## 3. Actual high-high lower bound from the stationary infinite-rank benchmark

By [operator-post-r15-stationary-tail.md](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/operator-post-r15-stationary-tail.md), in Q_H the D+K kernel differs in HS from m_N(x) C_N(x−y)m_N(y) by at most

    C_κ e^(-2α(L+H))[ exp(−κH+C_κL^κ) + N^(-1/2)e^(-H/2)(L+H)^3 ].

The Fourier multiplier of C_N is bounded below by cL/(1+t²), uniformly at sufficiently large N, from the explicit stationary symbol and the bounded-below digamma term. Let r_N=φ(N)/2, the rank upper bound for P. In the (r_N+1)-dimensional space of the first Dirichlet sine modes on [H,H+L], extended by zero, choose a nonzero g such that f=m_N^(-1)g is orthogonal to all r_N covariance atoms. This is possible by at most r_N linear constraints; then P f=0. All functions are in the true log Hilbert space. For the unitary Fourier transform Cauchy gives

    ∫ |ĝ(t)|²/(1+t²) dt ≥ ||g||₂⁴/(||g||₂²+||g′||₂²)
                      ≥ ||g||₂²/[1+π²(r_N+1)²/L²].

The factor m_N varies by at most absolute constants times e^(−α(L+H)) on that interval. Therefore the normalized Rayleigh quotient for the stationary approximation along f is at least c L³ e^(−2α(L+H))/φ(N)², using the standard φ(N)≫N/loglog N (or retaining L/(1+(r_N/L)²)). Fix κ=1/4. If H≥9L the normalized HS error above is o(L³/N²), uniformly as N→∞; the first term is N^(-9/4+o(1)) and the second decreases for H≥9L. So ⟨T_N f,f⟩ is negative with its absolute quotient bounded below as in (2). This is a rank nullspace argument for actual P on the far tail, not a hypothetical frame or a constraint on character eigenvalues.

For the upper, use the same arithmetic kernel for the alternative positive left boundary ρ=min(α/2,1/(L+H)) of the Hardy strip, other boundary unchanged. The normalization in the true log coordinates now replaces m_N by m_(N,ρ)(x)=[e^(−2ρ(L+x))+e^(−2β(L+x))]^(1/2). The common arithmetic kernel is independent of ρ. The original separate Hilbert–Schmidt component bound on this strip is O(L²+ρ^(-2)) (Li–Liu Lemma 6.4 and variable-boundary Appendix A; diagonal and model bounds as in pinned arithmetic-tail.md). On x≥H the multiplier ratio m_N/m_(N,ρ)≤sqrt(2)e^(−(α−ρ)(L+H)). Apply it on **both** sides of the high-high compressed kernel. Since ρ(L+H)≤1, this yields O((L+H)²e^(−2α(L+H))) in HS as claimed.

These sharp exponents are tail-in-H statements. At natural polynomial cutoffs, the rank lower bound is far smaller than R, and the lack of uniform residue isolation in (1) prevents substituting H=γ log N. The missing normalized prime covariance cancellation against the known stationary benchmark at those scales is not estimated here.
