# Round 4: a uniform all-mode test on logarithmic scales

The operator and notation are those of Li–Liu's [13 November 2026 manuscript](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf), with the sum of the two height boundary norms. Let N be even and satisfy local GRH(N), let L=log N, α=1/L, β=1/8, Δ=β−α, and let S denote the Goldbach singular series. This note supplies a finite, uniform coverage theorem, not the needed estimates for its finite matrix. It uses the actual operator, not discretization at sampled kernel points.

**Statement.** For any fixed 0<a<1/2 and all sufficiently large admissible N, project in the unitary Hardy log-coordinate realization to constants on intervals of length at most d≤1 partitioning [0,Y], and to zero outside. Use equal intervals except possibly a last short one. Write Q for this projection; Y>0. Then

    ||T_N − Q T_N Q|| ≪_a L² d^a + S N^(−3/4) + L(L+Y) exp(−Y/L).        (1)

The rank of Q is at most 1+Y/d. For any fixed A>0, Y=(A+3)L log L and d=L^(−(A+2)/a) give error O_a,A(L^(−A)) and dimension O_A,a(L^(1+(A+2)/a) log L). Hence the qualitative full norm target o(S) is equivalent to o(S) for this particular deterministic series of growing matrices. To check a specific prescribed S or R threshold, choose the precision and leave the required margin; a bound exactly at an endpoint does not transfer. Neither S nor R is established.

## 1. Uniform pointwise mean square in the characters

The source's argument for Lemma 6.4 also gives the following pointwise statement at the true moving boundary:

    Av_{odd χ mod N} |gχ(α+it)|² ≪ log²(N(2+|t|)), uniformly in real t,       (2)

where gχ(s)=L′/L(1/2+s,χ). To verify it, use σ₀=2α and the smoothed polynomial with endpoint X=N/2 and x=√X from (6.12). Before integrating in height, (6.12) and (6.10) yield |gχ(σ₀+it)|≪|Pχ(1/2+σ₀+it)|+log(N(2+|t|)), since the coefficient of the positive nontrivial-zero sum is less than 2/3 for these parameters. Odd-character orthogonality leaves exactly the diagonal in the average of |Pχ|²: n,m≤N/2 allows equality modulo N only for n=m, and only a zero-weight endpoint could be opposite. The diagonal sum is at most Σ Λ(n)² n^(−1−2σ₀)≪σ₀^(−2) by the elementary Chebyshev mean of Λ² and partial summation. This proves the pointwise claim at σ₀.

To move to α without any additional mean-value hypothesis, use the difference of the two primitive completed logarithmic derivatives from Lemma 3.3. For each ordinate γ on GRH(N), the absolute difference of its two Cauchy terms is bounded by

    α / (|α+i(t−γ)| |2α+i(t−γ)|) ≤ 2α / ((2α)²+(t−γ)²).

Summing gives the positive zero sum Qχ(2α,t) of the source, which is bounded by |gχ(2α+it)|+C log(N(2+|t|)) by (6.10). The conductor term cancels in the difference. The two gamma terms contribute at most O(log(2+|t|)) by uniform digamma bounds in the fixed real strip; removed Euler factors contribute O(log N) by the absolute logarithmic derivative of their finite factors on Re(1/2+s)≥1/2. Thus |gχ(α+it)| is bounded by a fixed multiple of |gχ(2α+it)|+log(N(2+|t|)), pointwise. Squaring and averaging proves (2), with no zero-spacing assumption.

## 2. Fractional Sobolev control of the actual log kernel

Let b(x,y) denote the inverse-height Fourier kernel of Bαα, using the log coordinate x=log of the raw additive size; the sign conventions are as in operator-round2.md §2. For every fixed 0<a<1/2 and all sufficiently large N depending on a, one has

    ||b||_{H^a_x L²_y} + ||b||_{L²_x H^a_y} ≪_a L².                     (3)

For the character kernel, the pointwise Cauchy–Schwarz inequality and (2) give

    |P_N(α+it, α−iu)| ≪ log(N(2+|t|)) log(N(2+|u|)).

The diagonal is pointwise at most D_N(2α)≪L². The Beta component, by (2.12) and Proposition 6.5's separate Euler-product comparison, satisfies

    |K_N(α+it, α−iu)| ≪ L²(2+|t−u|)^(2α).

Indeed |N^(−w) S A_N(w)|≪(Re w)^−1 for w=2α+i(t−u); Euler summation at 2+|t−u| bounds the zeta factor by O(α^−1(2+|t−u|)^(2α)); Stirling bounds both gamma quotients. In all three components we divide by (1+s)(1+conj z). Plancherel turns the left part of (3) into the weighted height integral with factor (1+t²)^a. Character logarithms are integrable because 2a<1. For the Beta square, use (2+|t−u|)^(4α)≪(2+|t|)^(4α)(2+|u|)^(4α); choose N so large that 2a+4α is bounded below 1 by a positive margin depending on a. The right part follows by Hermitian symmetry. This derives (3) uniformly on admissible N and is unrelated to the fixed-N Schatten index in round 3.

The Fourier–Laplace trace pairing expresses the true Hardy norm, in the left boundary coordinate, as ∫ W(x)|u(x)|²dx, where W(x)=1+exp(−2Δx); the right boundary trace is exp(−Δx)u(x). On a positive band the true unweighted log-coordinate kernel is therefore

    A(x,y)=sqrt(W(x)) b(x,y) sqrt(W(y)).                              (4)

For example, the α output in trace coordinates from an input left trace u is Bαα(Wu), since the right-input block transports with exp(−Δy). Multiplication by sqrt(W) is the unitary map from the weighted left trace space. To work globally in applying (3), extend sqrt(W(x)) from x≥0 by sqrt(W(max(x,0))); this extension is bounded and uniformly Lipschitz. Multiplication by it is bounded on H^a for 0<a<1 with constants uniform in Δ, as seen by splitting the fractional difference quotient of a product into the difference of the function and that of the multiplier. Thus (4) has the same bound (3) on the square of any positive band, via this extension.

## 3. Projection, matrix, and what remains

For an interval I of length ℓ≤d, writing f_I for the average of a Hilbert-space-valued function f, one has

    ∫_I ||f−f_I||² = (2ℓ)^−1 ∫_{I×I}||f(x)−f(z)||² dx dz
                 ≤ (d^(2a)/2) ∫_{I×I}||f(x)−f(z)||² / |x−z|^(1+2a) dx dz.

Sum over the partition and apply this first in x, then in y, to the positive-band kernel (4), with the other coordinate treated as the L²-valued codomain. By (3) the HS error made by averaging in both variables is O_a(L² d^a). The two omitted outside-band sectors have the operator error O(S N^(−3/4)+L(L+Y)exp(−Y/L)) by the proofs in operator-round2.md §§3–4; they include the crossing sectors. This proves (1). No Hardy projection is replaced by independent left/right height truncation.

The exact matrix in the normalized cell-indicator basis has entries

    M_ij=(|I_i||I_j|)^−1/2 ∫_{I_i×I_j} A(x,y) dx dy.

Equivalently use the actual cumulative discrepancy kernel 𝒦_N of source-round2.md §1. Put u=e^x/N,v=e^y/N. Then A(x,y)=sqrt(uv)𝒦_N(u,v), by the unitary map between log and physical measures and the same Hardy identification. Thus every matrix entry is a finite integral of the cumulative arithmetic-minus-model discrepancy on a bounded rectangle, with all interface terms retained. All relevant prime powers and alias indices are theoretically finite, but can be very large; the polylogarithmic **dimension** is not a polynomial-time evaluation claim. This is also not a quadratic form on a single Goldbach weight. A sufficient uniform goal is ||M_N||/S→0, or more strongly a bound on the maximal absolute row sum; pointwise convergence of individual entries at a fixed index does not imply this as the matrix grows. By (1), ||M_N||≤||T_N||≤||M_N||+error. At the R accuracy the same approach uses a much finer mesh, for example d=N^(−1/(2a)−ε) and the high endpoint from round 2; the rank then no longer has polylogarithmic size.

As a functional warning, even uniform vanishing on translated fixed smooth probes would not alone control top modes. Let two real smooth disjoint profiles of width O(1) in the log variable be centered at (1+θ)L and (1+θ′)L, with fixed distinct positive θ,θ′, and multiply both by cos(Lx); normalize them in L² to obtain f_N,g_N. Their cross rank-two kernel S(f_N⊗g_N+g_N⊗f_N) has norm S, has H^a_xL²_y+L²_xH^a_y=O(SL^a) compatible with (3), lives inside the intermediate band, and has zero same-side compression to either supporting cell. Against any translates of fixed smooth compact profiles the pairings vanish faster than any power of L after normalization by S, by repeated integration by parts (uniform derivative bounds under translation). This is only an example distinguishing fixed probes from growing all-mode controls, not a candidate for the arithmetic kernel. The finite-matrix estimate missing from (1) is precisely such a growing all-mode bound on the actual signed discrepancies.
