# Quantitative follow-up: a polylogarithmically expanding physical window

**Claim and limitations.** Fix B>0 and A>0. Let X<r≤2X, N=2r, L=log X, a=L^{-B}, b=L^B, and W_N[a,b] be the closed span of Hardy vectors with physical support in [aN,bN], as in arithmetic.md. Then under the family GRH used only to identify these vector forms with T_N,

    E_{X<r≤2X} ∥Π_N T_N Π_N∥op² ≪_{A,B} L^{-A}.

The corresponding centered arithmetic result is unconditional. Constants may be ineffective. Replacing L by log N in the window is harmless by monotonicity of compressed selfadjoint forms and taking a slightly larger fixed B. This is not a full-norm estimate; it excludes neither exceptional moduli nor large cross-window action. No priority is claimed.

## 1. Uniform hard-interval estimate, unit shift

Let Y<s≤2Y, h=2s, and C≥1 with C≤(log Y)^B' for a fixed B'. Use any two intervals I,J⊂[0,C], and either sign. Put

    A(s)=h^{-1}∑_{n,q≥1, q=h±n} Λ(n)Λ(q) 1_I(n/h)1_J(q/h),
    c=∫ 1_I(u)1_J(1±u)du.

Then for every D>0,

    E_s |A(s)−c S(2s)|² ≪_{B',D} (log Y)^{-D},

uniformly in interval endpoints, including moving ones. Half-open versus closed intervals cause at most O(log²(CY)/Y) at sample endpoints per s. The arithmetic unit condition may be included: prime powers with exponent ≥2 cost O(√(CY)log²(CY)/Y) uniformly; among prime–prime pairs, a nonunit forces equality of the two primes and accounts for at most one term.

**Uncentered second moment.** Apply [J. Leng, *Efficient Equidistribution of Nilsequences*, arXiv:2312.10772v5, Theorem 5, p. 6](https://arxiv.org/pdf/2312.10772#page=6) to the four fixed forms n,2s±n,m,2s±m. They are pairwise linearly independent. All interval conditions are linear inequalities in s,n,m, and cutting off s at a variable upper endpoint preserves convexity. The ambient box has size O((C+1)Y), while the coefficient bound is absolute, independent of C,I,J,Y. Theorem 5 has error O_H(((1+C)Y)^3(log Y)^{-H}) for any H, uniformly in the convex body. Abel summation in s inserts (2s)^(-2); divide by the number of s. The main term is c²∏_p M_p, with M_p=E_{s mod p}σ_p(s)² from arithmetic.md §5 (k=1). The O((C+1)^3) loss can be absorbed by choosing H larger. Integer versus continuous dyadic normalization costs at most a polylogarithm times 1/Y.

**Quantitative singular-series truncation.** Use S(2s)=2C₂∑_{d|s}a_d with a_d=μ²(d)∏_{p|d}(p−2)^(-1) for odd d and zero otherwise. For T≥2 let F_T sum only d≤T with the same coefficient 2C₂. Then

    E_s |S(2s)−F_T(s)|² ≪ T^{-1}.

Indeed the terms d,e>T require [d,e]≤2Y and their common divisibility probability is ≪1/[d,e]. On this tail 1≤(de)^(1/2)/T. The double series ∑a_d a_e (de)^(1/2)/[d,e] converges, since a prime appearing only once contributes O(p^{-3/2}) and one appearing twice contributes O(p^{-2}). This also bounds E_s S(2s)² uniformly. Finite averages of 1_{d|s}1_{e|s} equal 1/[d,e]+O(1/Y); for d,e≤T the sum of rounding errors is O(T²/Y), since a_d≤1. Thus E_s S(2s)²=∏M_p+O(T^{-1/2}+T²/Y), with the limiting Euler product checked as in arithmetic.md §5.

**Quantitative mixed moment.** For d≤T=(log Y)^J, d odd and squarefree, let q=h±n. The condition d|s on the pair (n,q) is q≡±n (mod 2d), with the sign as in q=2s±n. Changing from (s,n) to the independent prime coordinates (n,q) multiplies area by 2; requiring congruent unit classes contributes 1/φ(2d). The Siegel–Walfisz prime number theorem in progressions, applied once in each coordinate, gives

    E_s [A(s) 1_{d|s}] = 2c/φ(2d) + O_{H,B',J}((log Y)^(-H))

for arbitrary H, uniformly in d,I,J. To see the uniformity on the polygon explicitly, intersect the dyadic s slice with the ratio constraints: the resulting convex polygon lies in a square of side O((C+1)Y). Use a square grid with side Y/(log Y)^K and approximate the polygon from inside and outside. Its perimeter is O((C+1)Y) and the area of boundary cells is O((C+1)Y²/(log Y)^K) (with the usual extra one-cell area). Apply Siegel–Walfisz in each coordinate of each grid cell as a difference of endpoint sums. Endpoint errors can be taken O_{H',J,B'}(Y/(log Y)^{H'}) by choosing the prime-theorem exponent freely (very small endpoints have a trivial bound). The numbers of cells and residue classes are polylogarithmic, so all summed errors are still O_H(Y²/(log Y)^H) by choosing K and then H' sufficiently large. Nonunit contributions arise only from powers of primes dividing 2d and are negligible using the proper-power bound and the at most one equal prime pair per s. Abel in s (adding one dyadic cutoff face) inserts 1/(2s). This yields the displayed mixed moment. Its coefficient is precisely c times the limiting mean of S(2s)1_{d|s}: the mean of S(2s) is 2 and at each odd prime dividing squarefree d the ratio is 1/(p−1).

Choose J as large as needed and sum over d≤T with the coefficients. Cauchy–Schwarz handles replacement of F_T by S(2s) using the tail bound above, the uncentered A² bound O((1+C)²), and the bounded second moment of S. The same divisor bound handles the tail in the limiting mixed moment. This yields E_s A(s)S(2s)=c∏M_p+O((log Y)^(-D')) for any requested D' (increase J to absorb c≤C). Combining all three moments proves the unit-shift hard-interval variance estimate.

## 2. Remove growing coefficients by a nonnegative subsampling bound

For any integer k≥1 with k≤2b, put s=kr and Y=kX. Original weights 1_I(n/(2r)) and 1_J(q/(2r)) with q=2kr±n become interval indicators for I/k,J/k in n/(2s),q/(2s). Both the normalized sum and the matching model integral in the original r coordinates are k times their counterparts in the unit-shift s coordinates. The unit restriction on n,q may be discarded at negligible cost uniformly for k≤2b, as above (if a prime dividing 2r divides n, it also divides q). For the square, dropping k|s only increases the unrestricted sum. Thus the mean squared error per original shape is at most O(k³) times the corresponding unit-shift mean over Y<s≤2Y, plus negligible prime-power errors if the unit restriction is imposed. Every k³ loss is polylogarithmic, so arbitrary inverse-log savings remain uniform. Only the plus orientation n=q+2kr requires interchanging I,J. This step is why the fixed-coefficient hypothesis of Leng's theorem suffices for the growing window.

## 3. Recover the compressed operator norm without loss of uniformity

Let μ_N be the finite signed measure on [a,b]² given by discrete congruence pairs, **with the exact diagonal subtracted**, minus the three continuous shape measures. For rectangular tails put D_N(s,t)=μ_N([s,b]×[t,b]). There are O(1+b) shifted shapes, each covered by §2; triangle/Cauchy in that finite sum costs only O((1+b)²). Hence the pointwise rectangle variance E|D_N(s,t)|² is O_{H,B}(L^(-H)) uniformly in s,t∈[a,b], for every H.

For f,g smooth supported in (a,b), integration of f' and g' from the lower endpoint and Fubini give

    B_N(f,g)=∫_a^b∫_a^b f'(s)g'(t)D_N(s,t) ds dt

for real data (insert conjugation for complex tests). Hardy normalization in (7.15) controls ∥f'∥₂≪a^(-1)∥v_f∥: the Fourier multiplier weight in (7.15) is at least 1/2 since Nu≥1; with F(x)=e^{x/2}f(e^x), ∥(1−∂_x)F∥₂ controls both ∥F∥₂ and ∥F'∥₂, and ∥f'∥²₂=∫e^(−2x)|F'−F/2|² dx. The bound is uniform in N even for this expanding window. Therefore

    ∥Π_N T_N Π_N∥² ≤ O(a^(-4)) ∫_a^b∫_a^b |D_N(s,t)|² ds dt.

The area O(b²) and a^(-4) cost only powers of L. Choosing H large proves the claim. In particular for any C₀,D₀>0 the number of r∈(X,2X] with compressed norm exceeding L^(−C₀) is O_{B,C₀,D₀}(X L^(−D₀)). This follows from Markov with exponent A≥2C₀+D₀.

**Gap to S/R.** An exceptional set of size O_D(X/log^D X) for every fixed D still can contain infinitely many integers, and matrices with vanishing interior compression can have large exterior or cross blocks. The argument neither proves nor refutes S or R. Nested slowly growing windows faster than a prespecified polylogarithm can be obtained non-effectively by diagonal choice of cutoffs, but there is no implication for a whole power-of-N window from the estimates above alone.
