# Post-R15: the deterministic high-tail benchmark is stationary to polynomial accuracy

**Scope.** This proves an all-mode operator statement about the actual diagonal D_N plus Beta model K_N on a doubly exterior sector. It does not estimate the signed T_N=P_N−D_N−K_N there, since the genuine character covariance P_N still has to cancel this stationary term. It requires only local GRH(N), not auxiliary global GRH.

Put L=log N, α=1/L, β=1/8. Here x and y designate the **dimensionless log** of the physical variables u and v; raw log size is L+x or L+y. Work in the true unitary L²(dx) realization from [source-round2.md](https://github.com/h1n4k0/goldbach-spectral-research/blob/c7e28563c459509a1a14676888bfc63cdf2bb1d8/source-round2.md). Define

    m_N(x)=w_N(e^x)^(-1/2)=[e^(-2α(L+x))+e^(-2β(L+x))]^(1/2),
    b_N=Σ_(p|N) log p/(p−1),
    a_N(t)=[L−log π−b_N+Re ψ(3/4+it/2)]/(1+t²),

where ψ=Γ′/Γ. Let C_N be convolution on L²(R,dx) with kernel k_N(x−y)=∫_R e^(it(x−y)) a_N(t)dt, so its Fourier multiplier for the unitary Fourier convention is 2π a_N. Let Q_h=1_(x≥h), and fix 0<κ<1/3. For all h≥0 and sufficiently large N satisfying local GRH(N),

    ||Q_h(D_N+K_N−M_m C_N M_m)Q_h||_HS
      ≪_κ e^(-2α(L+h)) [
            exp(−κh+C_κ L^κ) + N^(-1/2)e^(-h/2)(L+h)^3 ].           (1)

The weighted convolution in this statement need only be defined after Q_h, where M_m is bounded. In particular, for h=γ L with any fixed γ>0, the approximation error is O_(γ,κ)(N^(-κγ+o(1))+N^(-(1+γ)/2)L³). The benchmark itself has exterior operator norm ≍ L e^(-2α(L+h)) for h≥γL, hence of logarithmic order at the polynomial cutoff h=γL. It is **not** a small high tail on its own.

## 1. Exact diagonal and a uniform error on the whole quadrant

Remove the separable factors m_N(x)m_N(y) temporarily, calling the remaining kernel bare. In the diagonal rank-one kernel the coefficient is Λ(n)²/n and the physical atom is sqrt(2π)r(u)(n/N)1_(n≤Nu), r(u)=u^(-3/2)/sqrt(w_N(u)), as in operator-round7.md. Changing measure to log coordinates gives the exact bare diagonal

    D_bare(x,y)=2π (N²e^(x+y))^(-1) Σ_(n≤N e^(min(x,y)), (n,N)=1) Λ(n)² n.

Under RH, part of the local GRH hypothesis, θ(T)=T+O(sqrt(T)(log(2+T))²). Abel summation with p log p, and the O(sqrt(T)) proper prime powers, give

    Σ_(n≤T) Λ(n)²n = (T²/2)(log T−1/2)+O(T^(3/2) log³(2+T)).

Removing prime powers of bases dividing N costs O(T Σ_(p|N)(log p)²)≪T L², since the sum of powers of each fixed base up to T is at most twice T. For T≥N this is absorbed. With d=x−y and q=min(x,y), the diagonal therefore is

    D_bare(x,y)=π e^(-|d|)(L+q−1/2)
                 + O(N^(-1/2)e^(-q/2)e^(-|d|)(L+q)^3),  x,y≥0.         (2)

Squared integration over x,y≥h bounds the bare remainder's HS norm by O(N^(-1/2)e^(-h/2)(L+h)^3), as in the integral of e^(−q)e^(−2|d|) over each triangular half-plane. The restored weights are at most 2 e^(-2α(L+h)) together.

## 2. Shift the exact Beta kernel in its joint Mellin variable

In the original (2.12), write H(s)=X_1(s)/(1+s), X_1(s)=Γ((3/2−s)/2)/Γ((3/2+s)/2), and w=s+z, where z denotes the reflected holomorphic input coordinate. Factor the scalar model as

    Z_N(w)=π^w ζ(1−w)ζ(1+w) A_N(w),

    A_N(w)=2C₂(1−2^(-1−w))
           · Π_(p|N,p>2) [(p−1)/(p−2)](1−p^(-1−w))
           · Π_(p∤N,p>2)(1+p^(-w)/(p−2))(1−p^(-1−w)).

The appearance of 2C₂ is the manuscript's singular-series normalization. This is the same Euler factor used in source-round3.md. The last product is absolutely convergent for Re w>−1/2 by cancellation of the first-order p^(-1−w) terms; on Re w≥−κ each factor differs from 1 by O(p^(-2+2κ)). For the bad prime factors a bound exp(C_κ L^κ) is uniform in Im w: split the sum of p^(-1+κ) over p|N at p=L, use an integer bound below and at most L/log L primes above. Thus |A_N|≪exp(C_κ L^κ) uniformly on the contour strip. Also A_N(0)=1 and A_N′(0)=b_N: the good factors have zero individual logarithmic derivative at 0, the bad ones supply log p/(p−1), and the factor at 2 gives log 2. It follows that

    Z_N(w)=−w^(-2)−(log π+b_N)w^(-1)+O_N(1)

near 0; the first-order Euler-constant terms of ζ(1−w)ζ(1+w) cancel.

In log coordinates remove m_N(x)m_N(y). The Beta bare kernel is the (distributional, initially) double inverse

    (1/(2π)) ∬ e^(s x+z y) Z_N(s+z) H(s)H(z) dt du,
    s=α+it, z=α+iu.                                            (3)

Indeed the pair of unitary height inverses contributes 1/(2π). The original factor N^(-(s+z)) is canceled by replacing both raw log variables by L+x and L+y. The residual exp(−α(2L+x+y)) from the Laplace heights and the paired Hardy factors sqrt(1+e^(−2(β−α)(L+x))) (and analogous y) are exactly m_N(x)m_N(y), which have been removed. Thus (3) is not an independent-boundary normalization.

Set τ=(x+y)/2 and d=x−y. Change variables to w=2α+iη, s=w/2+it′, z=w/2−it′; the real Jacobian from (η,t′) to (t,u) has modulus 1. Define

    J(w,d)=(1/(2π))∫_R e^(it′d) H(w/2+it′)H(w/2−it′)dt′.

Then (3) is (1/i)∫_(2α) e^(wτ) Z_N(w) J(w,d) dw. Shift Re w to −κ and keep t′ real in the underlying double integral. A rigorous implementation is to pair (3) first with a compact smooth test in x,y, so the transform is rapidly decreasing in both heights on the fixed strips. For fixed t′, horizontal contributions vanish in the w shift; the polynomial bounds and joint Schwartz decay justify Fubini on both lines and in the residue. The only crossed pole is w=0: H has no poles between Re s=−κ/2 and α (nor does H(z)), and A_N is holomorphic there as a function of w. Pairing defines the two-dimensional shifted inverse in L² as verified below, so this is a genuine kernel identity.

The residue contribution is

    −2π[(τ+log π+b_N)J(0,d)+∂_w J(0,d)].                    (4)

The factor 2π comes from (1/i) times the usual contour residue factor 2πi. One has X_1(it′)X_1(−it′)=1, and J(0,d)=(1/2)e^(-|d|). Differentiating the product H(w/2+it′)H(w/2−it′) at 0 gives

    −Re ψ(3/4+it′/2)/(1+t′²) − 1/(1+t′²)².

The logarithmic derivative of X_1 gives the first term; the average of 1/(1+it′) and 1/(1−it′) gives the second. Both are L¹ in t′, so the resulting residue function is ordinary. The inverse transform of (1+t′²)^(-2) with factor 1/(2π) is (1/4)(1+|d|)e^(-|d|). Combining (4) with (2), q−τ=−|d|/2 and this last transform cancel exactly. The sum is the claimed k_N(d), plus the shifted and diagonal remainders. In particular the order-h contribution of the two individual kernels has canceled.

## 3. Weighted L² error on the actual exterior, and its interpretation

On the shifted lines Re s=Re z=−κ/2, Stirling gives |H(s)|≪(1+|t|)^(-1+κ/2) and similarly for z. The ζ(1−w) factor is absolutely bounded, and Euler summation gives ζ(1+w)≪_κ(1+|t+u|)^κ there. Use (1+|t+u|)^κ≤(1+|t|)^κ(1+|u|)^κ. The squared double height integrand is integrable with one-variable exponents −2+3κ<−1, and L² norm of the unsquared kernel is at most O_κ(exp(C_κ L^κ)). By two-dimensional Plancherel, its inverse has the same bound before the multiplier exp(−κ(x+y)/2) from the real parts. On x,y≥h this multiplier is at most exp(−κh); the two restored Hardy weights supply the further factor O(e^(-2α(L+h))). Adding the diagonal error proves (1) on the whole unbounded quadrant, not only on a fixed window.

For positivity and size, the digamma series gives Re ψ(3/4+it/2)≥ψ(3/4) and O(log(2+|t|)) in magnitude. By splitting p|N at L as above and the Chebyshev bound for Σ_(p≤L)log p/p, b_N≪log L. Thus a_N(t)≥c L/(1+t²) for large N and sup a_N≪L. For the weighted compressed convolution the upper bound is O(L e^(-2α(L+h))). For a lower Rayleigh test choose a fixed nonzero smooth bump f on (0,1), and a normalized vector proportional to m_N(x)^(-1) f(x−h). The normalization factor is comparable to e^(-α(L+h)), and the bare convolution quadratic form on its fixed profile is ≫L by Plancherel and the positive symbol. This proves the opposite lower bound. The error in (1) is negligible relative to it for any h≥γL, γ>0 fixed.

At the R15 exterior cutoff, h≈(3/40)L, the deterministic benchmark has norm ≍L and cannot be thrown away as an inverse-log error. In exact terms the remaining target is Q_h(P_N−M_m C_N M_m)Q_h (and the two crossings). It requires cancellation in the *genuine* normalized character covariance, not a supremum bound on the unsigned kernel. This note supplies a stationary deterministic comparison on all exterior modes, but neither such covariance cancellation nor any global S/R inference.
