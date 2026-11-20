# Arithmetic lane: normalized residual and what the sieve actually controls

**Status.** No proof or disproof of S or R. New derivations below are working lemmas, not claims of priority. The positive results are uniform component and fixed-scale compression bounds; neither supplies uniform cancellation on the full Hardy space.

**Sources.** J. Li and J. Liu, [2026 preprint](https://mrc.sdu.edu.cn/english/info/1018/1514.htm), especially (2.1), (2.11)–(2.17), Proposition 6.5, Lemma 7.2, and Proposition 7.4. [T. Tao, 254A, Notes 4](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/), upper-bound sieve and Exercises 24–25. The centered conclusions below are derived, not statements attributed to those sources.

## 1. Two-weight identity

Write L=log N, α=1/L, β=1/8. In this note N is even, N>e^10, and GRH(N) is assumed when interpreting a Hardy operator or moving the L-function contours. For real f,g smooth and compactly supported in (0,∞), let v_f,v_g be the paper's Riesz test vectors with companions √u f(u), √u g(u). Conjugations for complex weights follow by sesquilinearity. Define

    H_fg(y) = ∫ [f(u)g(u+y) + g(u)f(u+y)]du − ∫ f(u)g(y−u)du,

with functions extended by zero. Define A_fg as the normalized sum over n,m≥1, (nm,N)=1, of Λ(n)Λ(m)f(n/N)g(m/N), weighted by

    [1_{n≡m (N)} − 1_{n=m} − 1_{n≡−m (N)}]/N.

Then the signed form, with the arguments in either order for real f,g, is exactly

    B_N(f,g) = A_fg − ∑_{k≥1} S(kN) H_fg(k).

Indeed odd-character orthogonality gives the discrete term, as in the preprint. The two difference-model integrals over y>0 partition the positive quadrant, whereas the sum-model integral covers that quadrant once. Thus ∫H_fg=0 even without symmetry of either weight. This cancels the pole of the density series at 1; compact support and smoothness give the Mellin decay needed in Lemma 7.2, yielding the finite sum displayed here. Each separated kernel and Hardy functional is the same as in §§5–7. In particular the canonical balanced Goldbach weight gives the signed scalar c_f S(N)−G(N), where c_f=∫f² and G includes the factor 1/N. It is not a norm identity.

**A different necessary projection.** For nonzero b∈C_c^∞((1/5,1/4)), use f(u)=b(u), g(u)=b(u−1). The sole permitted relation is m−n=N: sums lie strictly between 1.4N and 1.5N. The resulting form is

    J_b(N)−S(N)∫b²,     J_b(N)=(1/N)∑_{(n,N)=1}Λ(n)Λ(n+N)b(n/N)².

The two vector norms are uniformly bounded. S implies an asymptotic with relative error O_b(1/h(N)) here, and R an absolute error O_b(δ_N). This is a positive-shift prime-pair problem for every sufficiently large even shift in the GRH regime, not a proof of the fixed-shift twin prime conjecture. It also precludes identifying the single balanced Goldbach test with the full norm.

## 2. Genuine uniform bound for an infinite-dimensional compression

Fix 0<a<b<∞ independently of N. Let W_N[a,b] be the closed span of vectors v_f for f∈C_c^∞((a,b)); let Π denote its orthogonal projection. Then

    ∥Π T_N Π∥op ≪_{a,b} S(N).

This is an order estimate, not little-o. To verify uniformity, subtract the exact diagonal first. There are at most O_b(1) shifts kN, with k≤2b, for any of the three remaining linear relations. The local number of excluded residue classes for n and kN±n is 1 at p|kN and 2 at all other primes. The ordinary two-dimensional upper sieve on an interval of length O_b(N) gives O_b(S(kN)N/L²) prime pairs uniformly for the finitely many k. More explicitly, the interval sequence has squarefree level-d progression error at most ν(d)≤2^{ω(d)}, with level N^{1/2} and sieve cutoff N^{1/u} for a sufficiently large fixed u. The elementary upper sieve yields the uniform local product ∏_{p≤N^{1/u}}(1−ν(p)/p)≪S(kN)/L² by Mertens. The levels' total divisor-weighted error is O(N^{1/2}log^{O(1)}N); both primes exceed the cutoff on the macroscopic windows. Each prime pair has weight O_b(L²). Pairs with at least one proper prime power give an additional O_b(√N L²) in the unnormalized sum since there are O_b(√N) such integers and a bounded number of partners per shift. Moreover S(kN)≪_b S(N). The continuous models are bounded by the same order. Thus the total variation of the signed normalized arithmetic-minus-model functional on this window is O_{a,b}(S(N)).

By (7.15) the norm of v_f, on this fixed window, is comparable uniformly in N to the L²(dx) norm of (1−∂_x)F, with x=log u, F(x)=exp(x/2)f(exp x). Integration by parts gives ∥(1−∂_x)F∥₂²=∥F∥₂²+∥F'∥₂². Thus ∥f∥∞≪_{a,b}∥v_f∥ by the one-dimensional Sobolev inequality. Applying the total-variation bound to f⊗g proves the displayed compression bound on the generating space and then its closure.

**Qualitative compactness criterion, not a proven cancellation input.** If B_N(f,g)=o(S(N)) holds for each fixed smooth pair supported on the same window, then ∥Π T_N Π∥=o(S(N)). The unit family in the equivalent H¹ norm is uniformly bounded and equicontinuous, hence admits finite ε-nets in the sup norm; take net centers from smooth members of the family. Approximation uses the uniform total-variation estimate above. This argument gives neither the prescribed rate 1/h(N) nor control of escaping physical scales or cross blocks. The local arithmetic hypothesis remains unproved uniformly in even N.

## 3. Individual operator estimates

In the decomposition T=P−D−K (character Gram, exact diagonal, continuous model), one can sharpen the separate *operator* bounds for the last two terms:

    ∥D∥op ≍ L,     ∥K∥op ≪ L.

These are not Hilbert–Schmidt bounds. Set d_n(s)=n^(-s)/(1+s). On the two boundary lines the Gram kernel of d_n,d_m is exactly

    π ∑_{σ∈{α,β}} (mn)^(-σ) exp(−(1+σ)|log(n/m)|)/(1+σ).

The nonzero spectrum of D is that of the positive Gram matrix with row/column factors a_n=Λ(n)/√n restricted to units. On each line apply the weighted Schur test with weight a_n on indices with a_n>0. The weighted row quotient is bounded by a constant times

    ∑_{m≥1} [Λ(m)²/m] (mn)^(-σ) exp(−(1+σ)|log(m/n)|).

Write j≤log m<j+1, k≤log n<k+1. Chebyshev bounds the mass of block j by O(1+j). The kernel weights on each block are at most a constant times e^(−2σk) e^(−|j−k|) (when j<k the factor e^{σ(k−j)} is absorbed by the 1+σ in the decay). The remaining block sum is O(e^(−2σk)(1+k))=O(1/σ). Summing the two boundaries proves the upper estimate. For the lower estimate test D on the unit vector proportional to d_N (a Hardy test vector, not an index in the diagonal). Its norm is bounded above and below by absolute constants. Its overlap with d_p is ≫1 on N<p≤2N from the left boundary. All these primes are units; the ordinary prime number theorem gives ∑_{N<p≤2N}(log p)²/p ≫L. Alternatively on a common bump supported in (1/5,1/4), both the character and diagonal forms are exactly the same and ≍L; the model vanishes. Removal of primes dividing N costs o(1) there. In particular ∥P∥op≳L as well, not a bound on T.

For K, formula (2.12) factors out S(N)(π/N)^w P_N(w), where w=s+z̄, and two bounded separable gamma ratios. Expand P_N(w)=∑a_d d^(−w) with a_d≥0. On a given boundary block set v=Re w≥2α. The phases (Nd)^(-it) are unitary multipliers. In ζ(1−w)=−1/w+R(w), the pole term is, up to the separable bounded factors, convolution with 1/(v+i(t−y)) and has L² operator norm at most 2π by Fourier transformation. The remainder is bounded uniformly on bounded heights and satisfies |R(w)|≪(2+|Im w|)^{1/4}log(2+|Im w|) uniformly 0≤v≤1/4 by Euler summation cut at height 2+|Im w|. After inserting 1/(1+s)(1+z̄), this remainder has a uniformly bounded Hilbert–Schmidt norm: the convolution of the two Cauchy weights is 2π/(4+t²). The boundary-block bound after summing in d is therefore O(S(N)N^(−v)P_N(v))=O(1/v) by the uniform Euler-product bound in the proof of Proposition 6.5. The four blocks imply ∥K∥op≪1/α. The character operator is still only bounded above here by the preprint's O(L²).

## 4. An unconditional but weak averaged arithmetic check

For the positive-shift bump above let c=∫b². Then

    (1/X) ∑_{X<N≤2X, N even} [J_b(N)−c S(N)] → 0.

This is a signed first moment, not a mean-absolute error or an exceptional-set bound. Indeed the weighted measure X^(-1)∑_p(log p)δ_{p/X} converges weakly to Lebesgue measure on compact positive intervals by the ordinary prime number theorem. Apply its product to the bounded, almost-everywhere continuous weight 1_{1<y−x≤2} b(x/(y−x))²/(y−x). All relevant primes are odd, so differences are automatically even, and distinct primes are automatically units for their difference. Proper powers contribute o(1) after the averaging. With r=y−x, u=x/r, the integral equals ∫₁²dr ∫b(u)²du=c. Also S(2m)=2C₂∑_{d|m,d odd squarefree} ∏_{p|d}(p−2)^(-1); the mean of the divisor sum over all m is ∏_{p>2}(1+1/[p(p−2)])=1/C₂. Convergence follows by truncating using ∑_d a_d/d<∞ (or by summing up to X before differencing the dyadic range). Hence X^(-1)∑_{X<N≤2X,N even}S(N)→1. This proves the signed-mean statement, which is compatible with failures on individual N.

## 5. A stronger averaged result: fixed-window compressed norm in mean square

Here is a further derivation using [B. Green and T. Tao, *Linear equations in primes*, Annals of Mathematics (2010)](https://annals.math.princeton.edu/2010/171-3/p08), whose generalized prime-pattern asymptotic in complexity at most two is unconditional. We only need complexity one. Fix 0<a<b<∞ once and for all. Write E_X for uniform average over integers X<r≤2X, put N=2r, and let Π_N project onto the window defined in §2. Under GRH for the family, one obtains

    E_X ∥Π_N T_N Π_N∥op² → 0  as X→∞.

The arithmetic bilinear forms and their averaged decay do not require GRH. Without family GRH, the corresponding sum restricted to N for which GRH(N) holds, still divided by the full dyadic count, is o(1). No density estimate relative to that subset is asserted. No rate or result for growing [a,b] is claimed.

**Step 1: one shape, two moments.** Each of the three families at a fixed k≥1 can after swapping n,m if needed be written as m=2kr+n or m=2kr−n, with n,m positive on the weight. Define

    A(r)=(2r)^(-1)∑_n Λ(n)Λ(2kr±n) f(n/(2r))g((2kr±n)/(2r)),
    c=∫ f(u)g(k±u)du.

Take f,g real first. The unit restriction alters A by o(1) uniformly: proper prime powers give O(√N log²N/N), and if two prime terms are both divisible by a prime divisor of N they must coincide, contributing at most O(log²N/N). The same observations permit the retained or unrestricted conventions. On the squares of the sums the four forms in (r,n,m) are n,2kr±n,m,2kr±m. They are pairwise linearly independent. Any three among them are linearly independent for k≠0, and for each target form the other three can be partitioned into a pair and a singleton whose linear spans exclude the target. This verifies complexity at most one even in the minus case. The Green–Tao theorem applies unconditionally with k f﻿ixed. It covers the present scaled compact Riemann-integrable archimedean weights by box approximation: the Λ-products are nonnegative and the weighted variables remain in an O_{a,b,k}(X) box. The factors (X/(2r)) and its square are smooth and bounded on the r-range. For the first and second moments, at fixed continuum r, changing n=2ru (and independently m=2rv) shows that the archimedean factors for the normalized averages are c and c².

For each prime p put σ_p(r)=(1−ν_p(2kr)/p)/(1−1/p)², where ν_p(h)=1 if p|h and equals 2 otherwise. The product over p is S(2kr). Set M_p=E_{r mod p} σ_p(r)². At fixed r mod p the two free residues n,m are independent, so the four-form local factor is exactly M_p, including p|2k (not just generic primes). For p∤2k, the values of σ_p(r) are p/(p−1) with probability 1/p and 1−1/(p−1)² otherwise. Thus Eσ_p=1 and M_p=1+O(p^{-3}). The four-form theorem gives

    lim_{X→∞} E_X A(r)² = c² ∏_p M_p.

**Step 2: center by the actual singular series.** Take Y≥2k fixed, let W=∏_{p≤Y}p and S_Y(r)=∏_{p≤Y}σ_p(r). Apply the two-form prime asymptotic on each of the finitely many classes r mod W (replace r by Wt+j). Local factors at p|W are the stated σ_p(j); factors outside W average to one. The same archimedean change of variables and summation over j show

    lim E_X A(r)S_Y(r) = c ∏_{p≤Y} M_p,
    lim E_X S_Y(r)² = ∏_{p≤Y} M_p.

To justify use of the full singular series, write S(2kr)=C_k∑_{d|r} a_d for a fixed C_k>0 and nonnegative, squarefree coefficients a_d=∏_{p|d}(p−2)^(-1) on d coprime to 2k, zero otherwise. Both ∑ a_d/d and ∑_{d,e} a_d a_e/[d,e] converge by their Euler products. For the unweighted means, tails are dominated using [d,e]≤2X for contributing terms and P_{X<r≤2X}([d,e]|r)≤3/[d,e] for X sufficiently large (enlarging 3 to 4 handles all floor roundings). One can therefore pass termwise to the limiting moments. Equivalently in these means the residues at the finitely many primes are independent, and the factorized limiting moments extend by convergence. This gives lim E_X S(2kr)²=∏M_p, lim E_X S(2kr)S_Y(r)=∏_{p≤Y}M_p (all factors outside Y have mean one), and hence

    lim_{Y→∞} limsup_{X→∞} E_X |S(2kr)−S_Y(r)|²=0.

Combining the moment identities, followed by Y→∞, proves E_X |A(r)−c S(2kr)|²→0. The matching is essential: a signed first moment, or an uncentered four-prime upper bound, would not imply this conclusion. Summing finitely many shapes and splitting complex tests into real and imaginary parts now gives E_X |B_N(f,g)|²→0 for each fixed smooth pair.

**Step 3: the operator norm on the window.** All normalized pre-Hilbert test functions belong to a common bounded H¹ ball in the fixed log-u interval by §2 (constants independent of N). This set is precompact in C⁰. Fix ε and choose a finite sup-norm ε-net of fixed smooth functions for the relevant smooth ball. Uniform total variation from §2 bounds replacing either normalized test by its net center by O_{a,b}(ε S(N)); the net-center sup norms are bounded. Thus the operator-norm square is bounded by a constant times the sum of finitely many squared matrix elements plus O_{a,b}(ε² S(N)²). Step 2 and bounded dyadic second moments of S(N) let X→∞ and then ε→0, proving the displayed assertion. In particular for every fixed window and threshold ε>0 the proportion of even N with compressed norm >ε tends to zero. This still permits infinitely many exceptions and says nothing about portions of the full operator escaping fixed physical scales. No claim of novelty is made; this is a synthesis of known arithmetic estimates with the stated Hardy realization.

## 6. Outstanding issue

The GRH(N) estimate on the full character covariance still controls its size before cancellation, not its difference from D+K in supremum over all unit Hardy vectors. Even exact cancellation on separated no-alias windows and bounded relative size on macroscopic windows do not establish the signed cancellation required simultaneously on all scales. S needs the zero-free threshold S(N)/(2h(N)√(1−η_N)) for h fixed in advance; R needs δ_N=√(S(N)/N)L^{3/2}. Neither follows from an O(S(N)) compressed bound, the signed average, or the separate logarithmic bounds.
