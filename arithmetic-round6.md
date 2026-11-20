# Genuine signed arithmetic on a shrinking logarithmic diagonal

**Fixed scope.** Under the preprint's local Dirichlet GRH(N), the exact residual admits a uniform estimate on the *literal* logarithmic diagonal band of half-width ρ:

    ∥ H_{N,ρ} ∥op ≪ ρ (log N)^4,      0<ρ≤log 2.              (1)

Here apply the physical unitary representation of source-round2.md followed by x=e^p and the isometry to L²(dp); H_{N,ρ} is obtained by multiplying the exact kernel by 1_{|p−q|≤ρ}. The indices p,q range over the full real line. Thus for arbitrary fixed A>0, ρ=(log N)^(-A−4) gives O((log N)^(-A)) uniformly for **every** eligible even N, including the whole cell-interface directions rather than only the fine Dirichlet probes. This controls a shrinking, not a fixed-width, part of the near band. It gives no estimate for its complement, and does not prove or refute S/R.

The two signed cancellations used here are actual odd-character cancellation in the von Mangoldt sums and the exact plus-plus-minus cancellation of the continuous model. We do not claim new mutual cancellation between P, D, and K. First obtain pointwise log-kernel bounds for each on x,y≥1/4 and then use the no-alias structure of the exact subtraction near the origin.

## 1. The genuine character Gram

Put L=log N, α=1/L, β=1/8, and

    w(x)=1/((Nx)^(-2α)+(Nx)^(-2β)).

In the physical representation a compact test is reconstructed as f(u)=√u∫_u∞ a_f(x)x^(-3/2)dx and has Hardy norm squared (2π)^(-1)∫w(x)|a_f(x)|²dx. Consequently a character feature for the Gram P, up to the fixed √(2π), is

    F_χ(x)= [∑_{n≤Nx} Λ(n)χ(n)√n] / [N x^(3/2)√w(x)].

To verify, insert the inverse f into N^(-1/2)∑ Λ(n)χ(n) f(n/N) and interchange the finite sum and the integral on compact physical probes. This is exactly the character Mellin test in Li–Liu with its normalizing factor; the equality extends by the bounded Gram form. With the unitary log-coordinate map x=e^p the feature acquires a factor √x.

Every odd χ mod N is nonprincipal. The [GRH prime number theorem for characters/progressions](https://academic.oup.com/qjmath/article/74/4/1505/7240642) yields Ψ(t,χ)≪√t log²(2Nt) uniformly. For imprimitive χ the removed prime powers cost at most ω(N)log(2t), inside that bound, so only GRH on conductors dividing N is used. Abel summation with √n gives

    |∑_{n≤Nx} Λ(n)χ(n)√n| ≪ Nx log²(2N²x).

Thus for x≥1/4,

    |√x F_χ(x)| ≪ log²(2N²x)/√w(x) ≪ L².

The last bound is global: √w(x)≥(Nx)^(1/L)/√2 when Nx≥1, and (2+t)²e^(-t) has bounded supremum for t=(log x)/L≥-(log4)/L. Absolute-value summation without the true character cancellation would instead leave a positive power of Nx. The finite Gram average therefore has log-coordinate kernel bounded pointwise by O(L⁴) on x,y≥1/4, independently of how large the physical cutoffs are.

## 2. Exact diagonal and the two opposite signs of the model

The log-coordinate diagonal kernel equals, up to the fixed normalization,

    [∑_{(n,N)=1, n≤N min(x,y)} n Λ(n)^2] /
    [N² xy √(w(x)w(y))].

Chebyshev's bound ∑_{n≤t}Λ(n)²≪t log(2t) makes this O(L) on x,y≥1/4; the factor min(x,y)²/(xy) is at most one, and the log weight absorbs growth.

For K, write the signed model mass at a fixed u∈(0,x] sampled in the v variable. Its cumulative coefficient is

    A_u(V) = ∑_{k≥1,0<u+k≤V} S(kN)
           + ∑_{k≥1,0<u−k≤V} S(kN)
           − ∑_{k≥1,0<k−u≤V} S(kN).

By the divisor expansion used in arithmetic-round4.md,

    ∑_{k≤t} S(kN)=c_N t+O(S(N)log(2+t)),

uniformly in t, with c_N comparable to S(N). Indeed the nonnegative divisor coefficients have ∑_{d≤t}a_{N,d}≪log(2+t) by Mertens and t∑_{d>t}a_{N,d}/d admits the same bound by partial summation. The continuous k lengths for the two positive samplings partition (0,V] up to one point, and those for the negative sampling cover that interval once. Thus c_N cancels exactly. Including integer endpoints, A_u(V)=O(S(N)log(2+u+V)).

Abel summation against √v now gives a weighted signed mass O(S(N)√y log(2+u+y)) through v≤y. Integrate it against √u through u≤x and then use symmetry in x,y. In the log-coordinate kernel, whose cumulative normalization is (xy√(w(x)w(y)))^(-1), this gives

    |K_log(log x,log y)| ≪
     S(N) sqrt(min(x,y)/max(x,y)) log(2+x+y) / √(w(x)w(y)).

This is O(S(N)L) for x,y≥1/4, again by the exact Hardy weight. Without the signed length cancellation, the number of model shifts could grow proportionally to max(x,y), so this step is not a triangle bound on individual shifts.

## 3. Literal log-band and quantifiers

If min(x,y)<1/4 and |log x−log y|≤log 2, then x,y≤1/2. In that rectangle, the true positive congruence gives only n=m, subtracted exactly. The negative congruence would require n+m=N and can only hit n=m=N/2, which is not a unit. Every model difference line is absent; a potential model sum line n/N+m/N=1 meets the rectangle at most in a single zero-mass boundary point. Thus the exact residual cumulative kernel vanishes there.

On all other points of the log band the preceding pointwise bounds give |H_log(p,q)|≤C L⁴. Each row and column of the mask has measure at most 2ρ, so Schur's test yields (1). Uniformity uses no averaging over N and no coefficient truncation in x or y. It is a true operator-kernel estimate, not merely a bound for adjoining compression rectangles.

The same argument controls any masked subset of the |p−q|≤log2 region of row and column measures O(ρ). It does not allow tiling a fixed-width diagonal band with many small cells while keeping the factor ρ: their total row measure is then fixed. Bounding that wider strip by O(L^(-A)) would still need mutual signed cancellation of the genuine character Gram and its two subtractions, beyond the inputs used here.
