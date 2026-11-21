# Pointwise cancellation at the very-long end of the mixed survivor

**Claim (global Dirichlet GRH).** Keep the exact one-good/one-rough mixed survivor of [R20](r20-arithmetic.md) on the physical prefix 0<x≤b, with 1≤b≤N, Z=ceil(4bN), D=floor(Z^(1/3)), and D²<Q≤Z². On the orientation where n is good, retain only the arithmetic terms for which the other divisor e≥E, with 1≤E≤Z. Include the reflected orientation for a good second leg. The central estimate is

    ∥C^{mixed}_{e≥E}∥HS ≪_ε b^(7/6) N^(1/6+ε) E^(-1/4).             (1)

All signs, masks, unit restrictions and original raw log factors are kept. This is pointwise in every sufficiently large even N, no average. The estimate gives a power gain whenever E≥N^θ b^(14/3) with fixed θ>2/3, after allowing ε. There is usable parameter room below e≤bN for b≤N^β, β<1/11, by choosing θ sufficiently close to 2/3. In particular for b=N^(3/40), Q=N^(7/8), set E=N^(21/20): this is below bN/3 for large N, and (1) gives O_ε(N^(-1/120+ε)). The bound is smaller than the R15 threshold N^-1/400, though weaker than the earlier R20 error N^-7/480. For fixed b and E=N^(3/4), the bound is O_ε(N^(-1/48+ε)).

The Dirichlet GRH assumption now controls **twisted Möbius sums for the auxiliary progressions**, not only RH for ζ and not only local GRH(N). Local GRH(N) identifies the original Hardy operator. This estimate removes just a very-long subrange of the narrowed mixed term; the other mixed divisors, rough–rough terms and exterior crosses are not bounded here, and neither S nor R follows.

## 1. Uniform twisted Mertens, including extra excluded primes and nonreduced residues

We use the following consequence of Dirichlet GRH. Uniformly in q,W_0≥1, a mod q and Y≥1,

    |∑_{e≤Y, e≡a mod q, (e,W_0)=1} μ(e)|
        ≪_ε (qW_0)^ε Y^(1/2+ε).                              (2)

Here is a proof, including the conductor and bounded-height dependence. The standard reciprocal estimate used in the Perron argument is stated in [H. Liu–W. Zhai, Lemma 2.1](https://www.impan.pl/shop/en/publication/transaction/download/product/83763); the following derivation makes its bounded-height form explicit. For any fixed 0<δ<1/2, nonprincipal χ modulo q and σ≥1/2+δ, GRH gives

    |1/L(σ+it,χ)| ≪_{δ,ε} (q(|t|+2))^ε.

Indeed log L has a branch on Re s>1/2 from the absolutely convergent Euler-product log on Re s>1, because there are no zeros there. For nonprincipal χ the character prefixes are O(q), so partial summation gives polynomial growth of L uniformly in q and |t| on every fixed closed strip in Re s>0. Apply Borel–Carathéodory on a disk about 2+it of radius 3/2−δ/4, using polynomial growth for the real part of log L and the O(1) Euler bound at the center. On the inner radius 3/2−δ/2 this gives |log L|≪_δ log(q(|t|+2)), in particular on the line Re=1/2+δ/2, uniformly at all heights. On the right-hand line Re=1+δ/2 the Euler logarithm is O_δ(1). To interpolate at a chosen height t, apply three lines to log L(s+it,χ)/(s+2)^2 in that strip: the factor makes the left supremum O_δ(log(q(|t|+2))) and the right O_δ(1). At Re≥1/2+δ it yields |log L|≪_δ [log(q(|t|+2))]^(1−δ) (farther right the Euler bound suffices). Exponentiation gives the reciprocal estimate with arbitrary ε. Imprimitive nonprincipal characters obey the same periodic prefix growth and are zero-free in this half-plane, since their omitted primitive Euler factors introduce no zeros there.

For the principal character, apply the same argument to ζ(s)(s−1)/(s+1), which is holomorphic and nonzero on Re s>1/2 under RH including at the removed pole. Its polynomial bound follows, for example, from the integral formula for ζ on Re s>0; the extra logarithm of (s−1)/(s+1) is uniformly bounded on the right-hand line. Restoring the ζ reciprocal multiplies by (s−1)/(s+1), of modulus ≤1 here. The omitted unit Euler factors for a principal character cost O_{δ,ε}(q^ε), since ∏_{p|q}(1−p^(-σ))^-1≪_{δ,ε}q^ε: for large p each factor is ≤p^ε, and finitely many smaller primes cost a constant.

The Dirichlet series of μ(n)χ(n)1_{(n,W_0)=1} is

    L(s,χ)^(-1) ∏_{p|W_0}(1−χ(p)p^-s)^(-1).

The finite factor costs O_{δ,ε}(W_0^ε) by the same argument. Apply truncated Perron at y=floor(Y)+1/2, initial line Re=2 and height T=y³ (small y is trivial). For bounded coefficients at a half-integer, its error on this initial line is O(y²/T): near y use |log(y/n)|≳|y−n|/y and ∑_{n≈y}1/(y|n−y|)≪(log y)/y, and the remaining denominator is bounded below. Shift to Re=1/2+δ with no poles. The vertical contribution is ≪ y^(1/2+δ)(qW_0T)^ε log(2T); horizontal parts cost ≪y²(qW_0T)^ε/T. Choosing δ and the auxiliary ε small proves the twisted bound O_ε((qW_0)^εY^(1/2+ε)). For a reduced class average over χ using character orthogonality, with no extra φ(q) loss.

For a nonreduced class, write g=(a,q), e=gz, q′=q/g and a′=a/g. If g is not squarefree or (g,W_0)>1 all terms vanish. Otherwise μ(gz)=μ(g)μ(z)1_{(z,g)=1}, and z lies in the reduced class a′ mod q′ with (z,gW_0)=1. Applying the preceding masked bound gives (2), since (q′)(gW_0)=qW_0. The same estimates bound differences of two prefixes on any interval.

## 2. Apply (2) inside the exact R20 membership masks

Fix one signed line of shift h=jN and any hard rectangle in (n/N,m/N), and take n good, m rough-for-this-step. Expand the least-two and rough masks exactly as in R20. Each expansion sector imposes P|n and R|m, with P,R dividing W=∏_{p≤log N,p∤N}p, and a fixed L=pq|P that is the chosen two-prime product throughout that expansion term. The coefficient mass is N^o(1), and P,R≤W≤N^C by Chebyshev. This expansion is applied to the actual R20 survivor a=d/(d,L)≤D, ae>Q, not to a superset obtained by dropping the membership condition.

For a fixed d and cofactor ℓ=m/e, the narrow survivor forces D<d≤D L≤D(log N)^2 and ℓ≤Z/E. Discard d or ℓ nonunit modulo N, since the summands are required to be units. On the line n is h±ℓ e or ℓe−h. To enforce d|n and P|n, require [d,P]|n. This is either insoluble or one residue class for e modulo q_1=[d,P]/gcd([d,P],ℓ). The other divisibility R|m is equivalent to R/(R,ℓ)|e, so intersecting with it gives either the empty set or still a single residue class modulo lcm(q_1,R/(R,ℓ)). This modulus is ≤Z^{O(1)}; (2) handles it whether or not the class is reduced. The exact unit condition on n,m is then simply (e,N)=1 because ℓ is already a unit and the shift is a multiple of N.

For these fixed d,ℓ the inequalities e≥E, e>D, ae>Q, the raw positivity bounds, and **both** original hard-coordinate interval cuts give one interval in e, contained in [1,Z/ℓ]. This is because n and m are affine in e. The weights are μ(d)μ(e) log(n/d)log ℓ. Pull out μ(d)log ℓ; the remaining log(n/d) marker has size and total variation O(log Z) on raw n≥1. Thus (2) with W_0=N and Abel summation, including all original integer endpoints, give an absolute bound

    O_ε(N^ε √(Z/ℓ))

for the signed e-sum, after absorbing the logarithms and relabeling ε. There are O(D(log N)^2) choices of d, and ∑_{ℓ≤Z/E}ℓ^(-1/2)≪√(Z/E). Summing and restoring the exact Boolean coefficients costs

    O_ε(D Z E^(-1/2) N^ε)

per raw hard rectangle on a single line, for each even N. The arithmetic normalization is 1/N. No claim of cancellation in the short/e-small fibers is made; this is an actual one-variable Möbius cancellation only where e is long enough, not a claim for all double-long terms.

## 3. Full-prefix transfer

The O(b) possible shifts and original line orientations give any hard-rectangle mass O_ε(b²D E^-1/2 N^ε), since Z≈bN. The √uv layer cake therefore bounds its cumulative A(x,y) by this times √xy. The independent absolute bound for the original masked integer coefficient is O_ε(Z^ε(log Z)^2) per pair (there are at most d(n)d(m) choices): when x≤y and an off-diagonal line is present, y≥1/2 and each n≤Nx has O(y) possible partners. This gives |A(x,y)|≪_ε Z^ε(log Z)^2(xy)^(3/2).

The log-coordinate Hardy kernel is 2π A/(xy√(w_N(x)w_N(y))). For x,y≥1/N use w_N≥1/2, multiply the two complementary bounds on A to bound the squared kernel, and integrate over O(log²N) log-area. If either coordinate is below 1/N the arithmetic cumulative is exactly zero, and no Beta term is present. Thus the squared HS norm is O_ε(b²D E^-1/2 N^ε). Taking a square root and D≈(bN)^{1/3} proves (1), with no assumption on the signed covariance of the remaining mixed sector.
