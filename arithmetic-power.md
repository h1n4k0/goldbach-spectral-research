# Global-GRH refinement: power-saving mean on a power-sized physical window

**Working theorem (not full S or R).** Assume GRH for *all* Dirichlet L-functions, not only GRH(2r) for the individual modulus being tested. Put γ=10^{-6}, a=X^{-γ}, b=X^γ. With N=2r, X<r≤2X, and the same physical-window projection as in arithmetic.md, one obtains

    E_r ∥Π_N[a,b] T_N Π_N[a,b]∥² ≪ X^{-1/10000}.

No claim of optimality, novelty, uniform smallness for individual N, or effective numerical threshold. The constants were chosen conservatively. Global GRH is used in the arithmetic estimates for auxiliary moduli unrelated to 2r. This does not prove the full-norm zero-free region.

## 1. Box energy for four primes

Let intervals I_j⊂[0,Z] be arbitrary. The number weighted with four von Mangoldt factors on x_1+x_2=x_3+x_4, with x_j∈I_j, equals

    V ∏_p(1+(p−1)^(-3)) + O(Z^{3−1/20}),

where V is the volume in the three free coordinates satisfying the four interval conditions. This familiar conditional four-prime estimate is uniform as the interval endpoints vary. Here are details to track the saving needed below.

Define e(t)=exp(2πit), T_j(α)=∑_{n∈I_j}Λ(n)e(nα), V_j(β)=∫_{I_j}e(xβ)dx, and P=Z^{1/16}. Major arcs around reduced a/q for q≤P have radius P/(qZ). Distinct arcs on the torus do not overlap for large Z: the minimum separation is 1/(qq'), and P(q+q')<Z. The total length is O(P²/Z). Dirichlet approximation at denominator floor(Z/P) places any minor-arc point within 1/q² of a/q with q≳P and q≪Z/P (enlarge constants at endpoints or take ceiling(Z/P)). The [Vinogradov–Vaughan exponential-sum bound](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf) for a prefix up to T≤Z is O((T q^{-1/2}+T^{4/5}+√(Tq))log⁴(2Z)); when the denominator exceeds T, the trivial bound is sufficient since √(Tq)≥T. Subtracting prefixes handles all intervals. Thus on minor arcs ∥T_j∥∞≪Z P^{-1/2}log⁴Z. Parseval and Chebyshev give ∥T_j∥₂²≪Z log Z. Bounding two factors by sup and two by Cauchy gives an integrated minor-arc error O(Z³P^{-1}log^9 Z).

The uniform GRH [prime number theorem for progressions](https://academic.oup.com/qjmath/article/74/4/1505/7240642) gives a prefix residue error O(√Z log²(qZ)) (for the finitely small endpoints one can use a uniform O((1+√Z)log²(qZ)) bound). Summing the φ(q) reduced classes and removing nonunit prime powers, then using partial summation, gives uniformly on major arcs

    T_j(a/q+β)= μ(q)V_j(β)/φ(q) + O(√Z P² log³(2Z)).

Indeed q≤P, Z|β|≤P, and nonunit powers contribute O(log q log Z). Each original and model factor is O(Z) by Chebyshev or interval length. Multiplying and integrating over the arcs costs O(Z^{5/2}P⁴log³Z). The main term's q sum is ∑_{q≤P} μ²(q)/φ(q)^3. Its tail is O(P^{-2+o(1)}). Extending each β integral past the arc gives in total O(Z³P^{-2+o(1)}): use |V_j|≤min(Z,O(1/|β|)) and ∑_{q≤P} q³/φ(q)^3 ≪ P^{1+o(1)}. The full β integral is the three-variable convolution volume V by Fourier inversion; the full q product is the one displayed. All estimates are O(Z^{3−1/20}) with room for the indicated logarithms.

## 2. Uniform convex region and parity normalization

In the unrestricted unit-shift second moment for h=2s one counts n,h±n,m,h±m, all positive. Change from (s,n,m) to three of the prime coordinates, e.g. (n,q=h±n,m); the fourth is determined by one relation with signs two plus, two minus. The image of each hard-interval domain and any s upper cutoff is a convex polytope with O(1) faces inside [0,Z]^3 for Z=O((1+C)Y) when the interval endpoints for n/(2s),q/(2s) lie in [0,C], with Y<s≤2Y. The condition that h be even is automatic for triples of odd primes or odd prime powers. The lost contributions involving an even prime power in one coordinate are ≪Z² log^{O(1)} Z on the complete body: there are O(log Z) possibilities for that coordinate and at most O(Z²) free choices left.

To pass from boxes to the convex body, tile the three independent prime coordinates by cubes of side Z/R, R=ceil(Z^{1/200}); the fourth coordinate has one full interval covering its positive range (enlarge the ambient box to 4Z if needed). Inscribed and circumscribed unions have O(R³) cubes and bracket the positive prime sum. The discrepancy of their continuous volumes restricted to the fourth interval is O(Z³/R): the boundary of a convex polytope with bounded face count inside a fixed cube has surface area O(Z²); a boundary neighborhood of thickness O(Z/R) has that volume bound. The box errors total O(R³ Z^{3−1/20})=O(Z^{3−0.035}), below the boundary-volume error. Half-open boxes or assigning faces consistently causes no difficulty; faces contribute at most O(Z² log^{O(1)}Z) for bounded-face bodies on the original grid, and including the internal box-grid faces costs at most O(R Z² log^{O(1)}Z). Thus before dyadic weights the error is O(Z^{3−1/200}). This argument uses positivity to bound boundary mass, not an unproved uniform upper bound for primes in a thin slab.

The Jacobian d(n,q,m)=2 d(s,n,m) supplies a factor 2. The p=2 factor of the four-prime relation in prime coordinates is 2; after conversion this becomes the local M₂=4 in the s-coordinate calculation. For odd p it is 1+(p−1)^(-3)=E_s σ_p(s)² since 2 is invertible. Thus the continuous main term after division by dyadic count and Abel against (2s)^(-2) agrees *exactly* with c²∏M_p from arithmetic-quantitative.md. For any intervals in [0,C], C≤Y^γ, the normalized four-prime error is O(Z^{3−1/200}/Y³)=O(Y^{−1/200+3γ}); rounding the dyadic normalization is negligible.

## 3. Quantitative centering with growing divisor cutoff

Set T=Y^{1/1000}. The Rankin argument from arithmetic-quantitative.md gives ∥S(2s)−F_T∥₂≪T^{-1/2}=Y^{-0.0005}. The second moment of S(2s) differs from its limiting Euler product by O(T^{-1/2}+T²/Y). The preceding four-prime estimate implies ∥A∥₂≪1+C, and |c|≤C.

For each odd squarefree d≤T the conditional mixed term still equals its archimedean main term 2c/φ(2d), now with power-saving error. In the independent (n,q) coordinates of the preceding report use a polygon grid with R_0=ceil(Y^{1/100}) subdivisions per coordinate. The area discrepancy in the bracketing polygon sums after normalizing is O((Z/Y)²/R_0). On each box and for each reduced class t mod 2d the two prime interval estimates have errors O(√Z log²(dZ)). Summing products over the φ(2d) compatible classes, the error per box is O((Z^{3/2}+dZ)log^4(dZ)), uniformly in endpoints. After multiplying by O(R_0²), dividing by Y², and using Abel for the 1/(2s) weight, this term is smaller than Y^{-0.45}. Nonunit pairs for these congruences force both numbers to be powers of a common prime dividing 2d, and are negligible (or use the bivariate bound for such pairs). The polygon error O(Y^{2γ−.01}) also holds for its main term because 1/φ(2d)≤1. Summing over d≤T loses at most Y^.001. Combined with the mean-square truncation bounds (for both sampled and limiting moments) this yields uniformly

    E_s |A(s)−c S(2s)|² ≪ Y^{-0.0004},      C≤Y^γ,    γ=10^{-6}.

For transparency, the worst truncation loss is O((1+C)²T^{-1/2}), which has exponent −.0005+2γ. The squared-singular-series rounding contribution has exponent at most 2γ+.002−1, and the mixed polygon rounding after summing coefficients and multiplying by c has exponent at most 3γ+.001−.01. The four-form contribution has exponent −.005+3γ. All are smaller than Y^(-.0004). Proper prime powers differ from the required unit-restricted shapes by O(√(CY)log²(CY)/Y) pointwise, apart from at most one equal prime pair, which is negligible when squared or handled by Cauchy.

## 4. Returning to all physical rectangle tests

As before k≤2b, Y=kX, C≤b≤Y^γ. Replacing original-shift r by s=kr in a nonnegative square costs at most O(k³). Summing O(b) shapes in a rectangular signed discrepancy costs O(b²) after squaring. Integration over a rectangle of area ≤b² and the factor a^{-4} from the derivative norm give the total loss O(b^7 a^{-4})=O(X^{11γ}) relative to the unit-shift estimate. Since .0004−11γ>.0001, the theorem follows with exponent 1/10000. For example the number of even moduli in the dyadic family with this compression norm >X^{-1/40000} is O(X^{1−1/20000}). Still neither an all-modulus theorem nor a full-operator bound.
