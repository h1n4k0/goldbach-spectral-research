# Pointwise cancellation in a genuine long–long product sector

**Theorem (RH for ζ, arithmetic kernel).** Use the [pinned Round 17 decomposition](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/ROUND17.md), with N even, 1≤b≤N, Z=ceil(4bN), D=floor(Z^(1/3)) and physical prefix 0<x≤b. In the true double-long divisor sum for each signed line keep exactly

    d>D, e>D, de≤Q,     1≤Q≤Z².

Retain the two original Möbius signs, all cofactors and the exact unit restriction modulo N. Do not add any continuous model to this component. In the full physical cumulative representation its prefix operator C_{≤Q} satisfies

    ∥C_{≤Q}∥HS ≪_ε b^(1/2)(Q/N)^(1/2) N^ε + b^(11/12) N^(-1/12+ε).       (1)

In particular Q=N^(7/8), b=N^(3/40) gives O_ε(N^(-7/480+ε)) for **every** even N on ζ RH. This is a literal product cutoff, not a union of rectangles missing a boundary strip. It includes, for example, the whole nonempty two-long box D<d,e≤N^(7/16) at those parameters, as well as asymmetric divisor ranges. Only local GRH(N) is needed for the paper's operator identification; combining this result with the full original-to-double-long replacement of Round 17 uses its stronger auxiliary Dirichlet GRH assumptions. No estimate is obtained for the surviving product sector de>Q, the exterior crosses, or S/R.

## 1. The exact line and its lattice error

Fix h=jN, 1≤j≤2b, and one of n+m=h, n−m=h or m−n=h. Restrict (n/N,m/N) to an arbitrary hard rectangle in [0,b]². The desired raw coefficient on that line is

    ∑_{line in rectangle,(nm,N)=1}
      ∑_{d|n,e|m,d,e>D,de≤Q} μ(d)μ(e) log(n/d)log(m/e).

For any fixed d,e, the raw n variable lies on an interval, with m affine of slope ±1. Divisors d,e>Z cannot contribute to the integer count and are omitted throughout, including in the ensuing density integral. Divisors with (de,N)>1 cannot contribute under the unit rule. Otherwise the two congruences are soluble if and only if gcd(d,e)|h, and then give one class modulo [d,e]. The unit restriction on n is exactly the restriction on both n,m because h is a multiple of N. Inclusion–exclusion over c|N gives density (φ(N)/N)/[d,e], with O(2^ω(N)) counting error on any interval, as c and [d,e] are coprime whenever μ(c)≠0. The marker log(n/d)log(m/e) on n,m≥1 has supremum and total variation O(log² Z) along this line, so partial summation costs O_ε(N^ε) per d,e after absorbing logs. There are ≤Q(1+log Q) possible pairs d,e with de≤Q. Thus the raw count equals its density integral up to O_ε(Q N^ε). Powers or composite values of n,m were not removed; the argument is for the genuine divisor coefficients on all integers.

It remains to bound the density multiplier *pointwise in the raw real coordinates* T_1=n,T_2=m with T_i∈[1,Z]:

    (φ(N)/N)∑_{D<d,e≤Z,de≤Q,(de,N)=1,gcd(d,e)|h}
             μ(d)μ(e)/[d,e] · log(T_1/d)log(T_2/e).             (2)

The original line model is already spent in Round 17 and does not enter (2).

## 2. Cancellation on the curved product boundary

Group (2) by g=gcd(d,e), so g|h, (g,N)=1. Nonzero terms are squarefree d,e. Write d=g a,e=g c; then (a,c)=1, (ac,gN)=1, and

    μ(d)μ(e)/[d,e] = μ(a)μ(c)/(g a c),
    D/g<a≤Z/g,     D/g<c≤min{Z/g,Q/(g² a)}.

For a fixed g,a the allowed c's form **one exact interval**, with the unit condition (c,agN)=1. No rectangular approximation to the product cut is needed.

The standard [RH Mertens bound, Titchmarsh Theorem 14.25(C)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf) also gives, uniformly in W and Y≥1,

    ∑_{c≤Y,(c,W)=1} μ(c) ≪_η W^η Y^(1/2+η).

Indeed the restricted coefficients are a convolution of μ with the sequence having local coefficients 1 on all powers of the primes dividing W, and its absolute Dirichlet mass at s=1/2+η is ∏_{p|W}(1−p^(-s))^(-1)≪_η W^η. By partial summation the series with additional weight 1/c or log(c)/c converge, and their tails beyond Y are O_η(W^η Y^(-1/2+η)(log(2Y))^j), j=0 or 1. No values of their limits are needed: taking an interval difference cancels those constants.

If g≤D apply these tail bounds to the lower endpoint Y=D/g and the upper endpoint in the exact interval, with W=agN and marker log(T_2/g)−log c. Its inner density sum is O_ε(Z^ε(D/g)^(-1/2+η)) for arbitrarily small η after absorbing logarithms and the removed-factor loss; W≤Z² because ga=d≤Z for any nonzero term. If g>D use the trivial harmonic sum O(log²Z). For these estimates one can always intersect with c≤Z/g, which remains one interval. The entire sum over the other variable a, using |μ(a)|/a and its marker, costs only O(log²Z). Therefore with σ=1/2−η the absolute size of (2) is bounded by

    O_ε(Z^ε) ∑_{g|h} g^-1 min{1,(D/g)^-σ}
       ≤ O_ε(Z^ε) D^-σ ∑_{g|h}g^(-1+σ)
       ≪_ε Z^ε D^-σ .

The same estimate works for a product band Q_1<de≤Q: the lower endpoint is then max(D/g,Q_1/(g²a)) and the same lower-tail bound applies. This proof cancels the true two-long signs in the CRT density total; it is not a prime-in-progression estimate for one leg or an average over h.

The raw integration length is O(Z), so dividing by N the contribution from each line in each hard rectangle is

    O_ε(Q N^(-1+ε) + b^(5/6)N^(-1/6+ε)).                     (3)

Here D≈Z^(1/3) and Z≈bN, with b≤N, and auxiliary powers were relabeled into ε. Both difference orientations and the sum are included; (3) is independent of the choice of their outer signs.

## 3. Uniform cumulative and the real x=0 edge

After the exact removal of n=m in R17, let μ_Q be the normalized signed line measure just estimated. There are O(b) possible shifts in [0,b]², and the hard-rectangle discrepancy is O_ε(U), where

    U=b Q N^(-1+ε) + b^(11/6)N^(-1/6+ε).

Writing A(x,y)=∫_{(0,x]×(0,y]}√(uv)dμ_Q(u,v), the positive layer cake gives |A(x,y)|≪ U√(xy). For a complementary bound, use absolute divisor sums: for each pair the raw coefficient is O_ε(Z^ε log²Z), since the number of choices is at most d(n)d(m), and the restriction de≤Q can only reduce this absolute count. If x≤y, nontrivial lines require x+y≥1, and each small integer n≤Nx has O(y) possible partners. Thus |A(x,y)|≪_ε Z^ε log²Z (xy)^(3/2) everywhere. In physical log coordinates the kernel is 2π A(x,y)/(xy√(w_N(x)w_N(y))) as in R17.

On x,y≥1/N, multiplying the two complementary magnitude bounds controls the square of the log kernel by O_ε(U Z^ε log²Z); the log area costs only O(log²N). On x<1/N the true arithmetic cumulative is exactly zero (no positive integer in the small coordinate); its reflection is also zero. In particular there is no unremoved Beta term at zero in this product component. Taking the square root proves (1), including all coarse directions and internal crosses of the prefix.

For the example parameters D has order N^(43/120), and Q^(1/2)=N^(7/16), while the two exponents in (1) are −1/40 and −7/480 (up to ε). The complementary high-product sector is not controlled by this method: the lattice error used in §1 is O(Q N^ε), which no longer saves once Q approaches N at fixed prefix scale. Pointwise cancellation across those short lattice fibers remains necessary; no individual-fiber estimate meeting that task is claimed here.
