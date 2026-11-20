# Round 2: the mixed Hardy boundary block

Source: Jiamin Li and Jianya Liu, [A Conditional Proof of the Goldbach Conjecture](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf), public 13 November 2026 manuscript. Use its kernel and arc-length convention. Write L=log N, α=1/L, β=1/8, Δ=β−α, S=the Goldbach singular series. Assume the source's GRH(N), and take N sufficiently large. Write Bστ for the ambient operator from L²(τ+iR) to L²(σ+iR) with kernel E(s,conj z)/[(1+s)(1+conj z)]. In particular the four α,β blocks give the ambient boundary operator whose restriction to H² is T_N. The mixed blocks are adjoints. None of the results below establishes S or R.

## 1. Improved mixed estimate and effective rank

The true mixed block has ∥Bαβ∥HS ≪ L. Moreover for any real X in [4,N/2], there is a specified operator U_X of rank at most the number of unit prime powers ≤ X such that

    ∥Bαβ − U_X∥HS ≪ L² X^(−β) + S N^(−β).                  (1)

All constants are absolute. Thus for any fixed A>0 one can approximate this block in HS, and hence operator, norm by O_A(L^(8(A+2)))-rank operators with error O_A(L^(−A)), for all sufficiently large N. This leaves their largest singular values uncontrolled.

Set D_{n,σ}(t)=n^(−σ−it)/(1+σ+it), p_{χ,σ}(t)=−gχ(σ+it)/(1+σ+it), and let E_χ denote the equally weighted average of odd characters modulo N. The symbol D_{n,σ} here is a vector, not the full paper's diagonal kernel. Let w_X be the smoothed cutoff equal to 1 for n≤X/2, log(X/n)/log 2 for X/2<n≤X, and 0 beyond X; let p^X_{χ,β}=Σ_{n≤X} Λ(n)χ(n)w_X(n)D_{n,β}/√n. Equation (6.12) works for x=X/2 and X with denominator log 2: the Perron kernel retains residue 1 and O(|v|^−2) decay on fixed vertical lines. At fixed β the bound for zeros in successive unit intervals gives

    |p_{χ,β}(t) − p^X_{χ,β}(t)| ≪ X^(−β) log(N(2+|t|))/|1+β+it|.

The trivial zeros and the removed Euler factors satisfy this bound by the argument immediately following (6.12). Therefore (E_χ∥p_{χ,β}−p^X_{χ,β}∥₂²)^(1/2) ≪ L X^(−β), uniformly in X. Lemma 6.4 gives (E_χ∥p_{χ,α}∥₂²)^(1/2)≪L. The ambient character block is the averaged rank-one kernel p_{χ,α}(t)conj(p_{χ,β}(y)). Replacing the right vector costs O(L² X^(−β)) in HS by the rank-one norm identity and Cauchy–Schwarz. Replace the exact diagonal by the same smoothed coefficient w_X (not its square, since only one variable was approximated). The error is at most C Σ_{n>X/2} Λ(n)^2 n^(−1−α−β) ≪ X^(−β) log(2X) by the Chebyshev estimate and partial summation. The mixed Beta block has HS norm O(SN^(−β)): in (2.12) the real part of w=s+conj z is at least β, so the Euler product is bounded; retaining N^(−Re w) and using the same weighted zeta height estimate as in operator.md proves the claim.

For unit n≤X put

    F_n(t)= E_χ[p_{χ,α}(t) conj(χ(n))] − Λ(n)D_{n,α}(t)/√n.

The explicit approximant U_X has kernel Σ_{n≤X, (n,N)=1} w_X(n)Λ(n)F_n(t)conj(D_{n,β}(y))/√n. This proves the rank bound and (1). For the O(L) mixed estimate, apply the one-sided approximation at X=N/2 without replacing p_{χ,α}. Odd orthogonality forces the average squared size of p^X_{χ,β} to be diagonal (the opposite endpoint has zero weight). Its height integral is O(Σ_n Λ(n)^2 n^(−1−2β))=O(1). Hence (E_χ∥p_{χ,β}∥²)^(1/2)=O(1), and the mixed character HS bound is O(L), while the true diagonal and model are O(1) by the bounds just given.

The remaining functions F_n carry exact arithmetic information. Before shifting to α, on Re s>1/2 the unweighted function (1+s)F_n equals

    Σ_{m≥1, m≠n} Λ(m) m^(−1/2−s) [1_{m≡n mod N} − 1_{m≡−n mod N}],

since n is a unit and odd orthogonality has weight 2/φ(N). Continue this equality as a holomorphic function via the actual character average. This is not GRH cancellation for the signed progression tails. Fixing n, taking the trivial residue-class counting bound to X=N^c gives a saving for c<2, while smoothing g_χ on α leaves a factor roughly exp(−c) times powers of L; c must increase for that technique's error to decay, at which point the residue-counting bound loses its saving. The two approximations do not give a uniform estimate for F_n.

## 2. A different exact reduction by logarithmic frequency support

Let ℱ denote the unitary inverse Fourier map on the height variable, with +itx in the exponential; use it independently on the two boundary spaces. The Fourier conjugate of Bαα has an L² kernel bαα(x,y) in logarithmic additive coordinates and

    bαα(x,y)=0 a.e. if x,y<log(N/2),
    bαβ(x,y)=exp(−Δ y)bαα(x,y) a.e.                       (2)

Here the second statement is for the mixed boundary operator; no mapping of independent boundary data to the Hardy space is asserted. For the first statement, the unweighted double inverse of E(α+it, α−iu), taken with +itx−iuy, is a tempered distribution by the source's height bounds. Its pairings against compact smooth product tests in x,y are precisely the polarized Mellin pairings from §§7.1.1–7.1.2, using raw additive coordinates e^x,e^y (multiply tests by the appropriate e^(±αx) factors). Character orthogonality subtracts the exact diagonal, leaving only m≠n with congruences m≡±n (mod N); all such points have max(m,n)≥N/2. The model similarly consists of differences or sums at positive integer multiples of N. To justify the model pairing for these tests, the sum of the two continuous difference masses equals the continuous sum mass, each the product of the two integrals of the physical test weights after the square-root normalization. Thus the Mellin residue at w=1 cancels, as in the paper's proof of (7.12). For tests supported where both e^x,e^y<N/2, all sampled convolutions vanish. Finite sums of product tests are dense in smooth compact tests on rectangles, proving the claimed unweighted support on that open square.

The denominators (1+s)(1+conj z) multiply vertically; their inverse transforms in the above convention are proportional to e^(−(1+α)x)1_{x≥0}, and the analogous function of y. Truncate these responses to [0,M] first. Convolution with two such compactly supported distributions preserves vanishing on x,y<log(N/2). The discarded multiplier is e^(−(1+α+it)M)/(1+α+it) on each line; multiplying E and pairing with any Schwartz function makes this error tend to 0, by polynomial vertical growth and the exponential M factor. This proves that weighting also preserves the support. Plancherel applies by the HS result of the source. To prove the second equality in (2) first pair the transforms against compact smooth log-coordinate tests, and shift the second Mellin line between α and β. Holomorphy from GRH(N), the source's polynomial growth estimates there, and rapid decay of the compact tests' Mellin transforms justify the shift. Accounting for the real part produces the multiplier exp(−Δ y). Equality as distributions gives the stated a.e. identity between locally L² functions. The reverse mixed block is the adjoint.

Let Q_Y be multiplication by 1_{logarithmic coordinate≥log Y} after ℱ. By (2) and the GRH baseline ∥Bαα∥HS≪L², for all Y>0

    ∥Bαβ Q_Y∥HS ≪ L² Y^(−Δ).

Writing Y=N/2, the exact square support identifies Bαβ as Q_Y Bαβ(1−Q_Y) plus an error O(N^(−β)L²) in HS; N^α=e. Thus the only leading mixed direction can carry small right logarithmic frequencies to large left ones. Taking Y=N^A for any fixed A>4 shows that the very high right-frequency portion alone lies below the R scale for all sufficiently large N. This cannot test R for the complementary directions. More generally the two-sided support reduction does not bound the left-left block, where the worst directions for S and R may remain. The inward strip shift gains damping only on the variable that is shifted.

## 3. The genuinely subunit physical sector is negligible even at the R scale

Let P₋ be the projection in the actual Hardy space obtained by truncating the inverse-height Fourier transform of both boundary traces to the logarithmic frequency x<0 (raw size exp(x)<1). This is a legitimate orthogonal Hardy projection: in the Paley–Wiener characterization of Lemma 5.2 a trace on line τ is the common Fourier–Laplace density multiplied by exp(−τx), up to an overall sign convention for x; cutting x<0 commutes with this relation. Then the **whole** operator satisfies

    ∥T_N P₋∥ = ∥P₋ T_N∥ ≪ S N^(−3/4),
    ∥T_N − (1−P₋)T_N(1−P₋)∥ ≪ S N^(−3/4) = o(δ_N).  (3)

The same proof permits cutting x<log 2, with a harmless fixed constant. This concerns only the subunit/first-integer edge, not longer escape toward infinity.

First, the P and D character and diagonal blocks have zero negative input. For P, the inverse Fourier transform of −gχ(s) before weighting on any line Re s>1/2 is the Dirichlet atomic measure on x=log n, n≥2. Its support statement transfers to α or β in tempered-distribution pairings with compact smooth log-coordinate tests, by the contour argument from §2 and GRH(N). Convolution with the causal response for 1/(1+s) does not enlarge support to the left. The exact diagonal has the same support by direct Dirichlet expansion in the two variables. Thus only the Beta model acts on this input sector.

For the model, take the actual output line σ=α or β and a much farther right input line ρ=3/4 (outside the Hardy strip, but inside the holomorphic range 0<Re z<3/2 of (2.12)). The corresponding auxiliary model block has HS norm ≪S N^(−3/4). Indeed on w=σ+ρ+i(t−u) the Euler product is uniformly bounded since Re w≥3/4, the X1 factors are uniformly bounded by Stirling, and N^(−Re w)≤N^(−3/4). The classical zeta convexity estimate on 0≤a≤1, |ζ(a+ib)|≪_ε(2+|b|)^((1−a)/2+ε) away from the pole, applies here with a=1−σ−ρ∈[1/8,1/4] and ε=1/32. For clarity, this estimate follows by the functional equation and bounded absolutely convergent Dirichlet series on 1+ε and Phragmén–Lindelöf across the strip after removing the pole. Squaring our kernel therefore leaves height dependence at most (2+|t−u|)^(15/16)/[(1+t²)(1+u²)], integrable by the same Cauchy convolution as in §6.4.2 of the source.

Next transport this auxiliary block back to the input line τ=α or β, only on y<0. The same contour shift as for (2), now of the explicit Beta model alone, multiplies its transformed kernel by exp((ρ−τ)y), at most 1 on this sector. Hence each of the four actual blocks is HS O(S N^(−3/4)) on this negative input. Restricting the ambient two-trace action to the true Hardy space proves the first assertion of (3); adjunction and the triangle inequality give the second. Since S≪loglog N, S N^(−3/4)/(sqrt(S/N) L^(3/2))→0. The geometry for exp(y)≥1, including physically meaningful prime inputs and the unbounded positive-frequency tail, is not resolved by this argument.

## 4. The extremely large positive-frequency tail can also be cut

For Y≥0 let P_{≥Y} be the genuine Hardy projection to logarithmic Fourier frequencies at least Y, via the same trace description as for P₋. Then

    ∥T_N P_{≥Y}∥ = ∥P_{≥Y}T_N∥ ≪ L² exp(−Y/(2L)).       (4)

To see this, place the auxiliary input line at ρ=α/2. The kernel is analytic between it and either actual input boundary τ. The HS bound O(L²) for B_{σρ} follows for σ=α or β by the same separate estimates of §6.4: the mean square height bound in Lemma 6.4 gives an individual trace-vector norm in averaged L² of size O(L) on both lines; the diagonal coefficient sum is O((σ+ρ)^(−2))=O(L²), and the Beta majorant (6.16) likewise uses σ+ρ≳1/L and 4β<1. Fourier transport from the auxiliary input line to τ multiplies the kernel by exp(−(τ−ρ)y), whose modulus is at most exp(−Y/(2L)) on y≥Y. Combine the four blocks and use adjunction. No limit through Re z=0 is taken.

For fixed ε>0 the truncation Y=(1+ε)L² makes the norm error O(L² N^(−(1+ε)/2))=o(δ_N). A scale Y=A L log L makes the error O(L^(2−A/2)); any specified inverse-log accuracy follows by taking a large enough fixed A. Combining (3) and (4), compression to the genuine Hardy band 0≤y≤(1+ε)L² approximates the full operator in norm to o(δ_N). This is an infinite-dimensional band whose upper physical scale is exp((1+ε)L²), not a finite matrix or a fixed bounded multiple of N. The modes at scales comparable to N or powers N^c remain inside the band and may contain all of the hard spectral mass.

The cutoff can be sharpened by using ρ=min(α/2,1/Y) for Y>0. Lemma 6.4 gives a mixed character HS bound O(L(L+ρ^(−1))); the diagonal and Beta bounds still cost only O(L²), using σ+ρ≥α. Transport then gives the improved uniform bound O(L(L+Y)exp(−Y/L)), since ρY≤1. Thus for any fixed c>3/2 one may instead take Y=L²/2+c L log L, with o(δ_N) error; for Y=A L log L the improved error is O_A(L^(2−A) log L). In particular the argument is uniform at the much smaller auxiliary line ρ≈L^(−2); it never takes a boundary value on the critical line. Since R has its exact coefficient 1, even a compressed bound ≤δ_N would not by itself establish R unless there is a margin covering the truncation error.
