# The same pointwise compensation for two short divisor legs

**Claim.** Keep N even, 1≤b≤N, Z=ceil(4bN), D=floor(Z^(1/3)), and Λ_D(n)=∑_{d|n,d≤D} μ(d)log(n/d), as in the short-leg result. On each of the three signed nonzero-shift lines, replace both arithmetic factors by Λ_D, keep exactly the original Beta line model and physical cumulative normalization, and form the centered operator on the full prefix 0<x≤b. Denote this centered operator by C^{ss}_{N,b,D}. Then under RH for ζ the arithmetic kernel satisfies

    ∥C^{ss}_{N,b,D}∥HS ≪_ε b^(11/12) N^(-1/12+ε).             (1)

No prime-in-progression theorem is needed for (1). To relate the genuine Hardy operator to the arithmetic kernel use local GRH(N); to combine with the earlier mixed short/true-leg result also use GRH for the auxiliary progression moduli d≤D. In particular, under global Dirichlet GRH, there is a pointwise same-sized error when replacing the original prefix operator by the **pure long–long** kernel, with no model subtraction. No upper bound on that long–long kernel is obtained, and neither S nor R follows. No averaging in N enters this result.

## 1. CRT on a single line, including the actual unit condition

Fix any h=jN with 1≤j≤2b. On a hard rectangle in [0,b]² consider n+m=h, n−m=h, or m−n=h. Let m=m(n) be the corresponding affine function of slope ±1. Expanding the two short divisor legs gives coefficients μ(d)μ(e) for d≤D dividing n and e≤D dividing m. On the true unit restriction (nm,N)=1, a term with (de,N)>1 is empty. For (de,N)=1 the two divisibilities are consistent precisely when gcd(d,e)|h, and then specify one class modulo [d,e]. Because m≡±n mod N, it suffices to impose (n,N)=1. Inclusion–exclusion over c|rad(N) with μ(c) gives a progression modulo c[d,e], since c and [d,e] are coprime. Its main density is

    ∑_{c|N} μ(c)/(c[d,e]) = (φ(N)/N)/[d,e].

For fixed d,e, each such counting function differs from its density model on a prefix by O(1); the unit-restricted error is O(2^ω(N)). On n,m≥1 the marker log(n/d)log(m/e) has supremum and total variation O((log Z)^2) along the line: both log factors are bounded by O(log Z) and have variation O(log Z) on this interval. Partial summation and summing d,e therefore costs O_ε(D² N^ε (log Z)^2) in the raw count. This step is entirely integer CRT; it retains all original integers, including proper prime powers, under the exact unit restriction and makes no assumption that the short weights are supported on prime powers.

## 2. The bivariate Euler factor and tensor truncation

Define the coefficients for the density calculation

    g_{h,N}(d,e) = (φ(N)/N) μ(d)μ(e) 1_{(de,N)=1,(d,e)|h}/[d,e].

In the region of absolute convergence write their Dirichlet series as

    ∑_{d,e≥1} g_{h,N}(d,e)d^(-s)e^(-t)
       = ζ(1+s)^(-1) ζ(1+t)^(-1) H_{h,N}(s,t).

At a prime p write A=p^(-1−s), B=p^(-1−t). Before division by (1−A)(1−B), the local numerator is 1−A−B if p∤h; it is 1−A−B+pAB if p|h,p∤N; it is 1 if p|N (h is a multiple of N). The scalar φ(N)/N is included in H. Thus the H factors away from p|N are respectively 1−AB/[(1−A)(1−B)] and 1+(p−1)AB/[(1−A)(1−B)]. At s=t=0 the resulting factors are p(p−2)/(p−1)^2 off h, and p/(p−1) on h, the latter including the scalar contribution at p|N. Hence

    H_{h,N}(0,0)=S(h).

This is the exact same shifted density as the original Beta line, with the correct leading factor 2.

Fix 0<η<1/4 and put σ=1/2−η. If H_{h,N}(s,t)=∑ h_{h,N}(u,v)u^(-s)v^(-t), the absolute coefficient mass ∑|h_{h,N}(u,v)|(uv)^σ is O_{η,ξ}(h^ξ) for every ξ>0. Indeed at p∤h the absolute factors differ from 1 by O_η(p^(-1−2η)), so the unrestricted product converges. At p|h,p∤N the additional term is O_η(p^(-2η)); at p|N the denominators contribute O_η(p^(-1/2−η)) beyond 1. For all sufficiently large p each finite exceptional factor is at most p^ξ; the fixed smaller primes cost a constant. This uniform **two-variable** bound is what controls both truncations, including those involving a divisor of the shift.

For T∈[1,Z] put

    B_u(T)=∑_{a≤D/u} μ(a)/a · log(T/(u a)).

By [RH Mertens](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), ∑_{a≤Y}μ(a)/a=O_η(Y^-σ) and ∑_{a≤Y}μ(a)log a/a=−1+O_η(Y^-σ log(2Y)); the limits follow from ζ(1+s)^(-1)=s+O(s²) at zero and partial summation. It follows that for u≤D, B_u(T)=1+O_η((log Z)(u/D)^σ). For u>D, B_u=0, and the same bound on |B_u−1| still holds. Convolving the two Möbius factors with H then gives the pointwise two-cutoff density

    ∑_{d,e≤D} g_{h,N}(d,e)log(T_1/d)log(T_2/e)
      = ∑_{u,v} h_{h,N}(u,v)B_u(T_1)B_v(T_2)
      = S(h)+O_ε(Z^ε D^(-1/2+η))                             (2)

uniformly T_1,T_2∈[1,Z] and h≤Z, on choosing ξ small and absorbing logs into ε. To see uniformity even if B_u is large, write B_uB_v−1=(B_u−1)+(B_v−1)+(B_u−1)(B_v−1); the two-variable weighted mass controls all three terms. D=Z^{1/3}+O(1) and arbitrarily small η give density error O_ε(Z^(-1/6+ε)).

Insert (2) with T_1=n,T_2=m(n) into the raw line integral from §1. The integral is taken only where both n,m≥1; extending the already-constant model to n,m>0 changes the raw overlap length by O(1), hence costs O(S(h)) before normalization. With the same normalization 1/N as the original line, the short-short arithmetic form on each hard rectangle is therefore S(h) times its normalized line length plus O_ε(Z^{5/6+ε}/N). The CRT error D²N^ε(log Z)^2 is smaller. This holds for both difference orientations and sums; the outer positive or negative line signs are the unchanged Li–Liu signs.

## 3. Full prefix transfer and what is left

Sum the individual rectangle errors over the O(b) nonzero shifts; the pointwise hard-rectangle discrepancy is O_ε(b^{11/6}N^(-1/6+ε)). The positive √u√v layer cake bounds its weighted cumulative by this times √xy. Complementarily, |Λ_D(n)Λ_D(m)|≪_ε Z^ε(log Z)^2 by the divisor bound. At x≤y, every active line has x+y≥1, so y≥1/2 and each n≤Nx has O(y) partners. Using this trivial bound for the two-short product and O(log Z) for each line density gives the same absolute cumulative bound O_ε(Z^ε(log Z)^2(xy)^(3/2)) as for the mixed short-leg kernel. In the physical log kernel 2π times the cumulative divided by xy√(w_N(x)w_N(y)), multiplication of the two magnitude bounds makes the squared log kernel integrable on the bulk x,y≥1/N, at cost O(log²N) area. On x<1/N a nonzero term forces y≥3/4; integrating the absolute bound uses ∫₀^{1/N}dx/w_N(x)≪1/N, giving edge HS² ≪_ε b Z^ε N^-1(log Z)^4 (and its reflection). These are the full-prefix calculations of the earlier short-leg result, now with the genuine two-short weights; they yield (1).

Let R_D=Λ−Λ_D. For each individual pair, with the unit restriction and exact deletion of n=m still in force,

    Λ(n)Λ(m) = Λ(n)Λ_D(m)+Λ_D(n)Λ(m)−Λ_D(n)Λ_D(m)+R_D(n)R_D(m).

Subtracting the exact model once, the first three terms are precisely twice the earlier centered mixed short-leg block minus this centered short-short block. This proves that replacing the actual prefix by the original signed line geometry with arithmetic weights R_D(n)R_D(m) alone incurs at most O_ε(b^{11/12}N^-1/12+ε) in HS norm under global GRH. In particular b=N^{3/40} gives O_ε(N^(-7/480+ε)) for every even N in the hypothesis, without any square-family assumption. The long–long kernel has terms of the form

    (1/N)∑_{k,ℓ≥2} (log k)(log ℓ)
       ∑_{d,e>D, k d±ℓ e=h, (kℓde,N)=1}
          μ(d)μ(e) · 1_{(k d/N,ℓ e/N) in the rectangle},

with k,ℓ≤Z/D, and the reflected orientation, before the same cumulative and weighting. All proper prime powers and other values of the long weights are retained by the exact decomposition. **Nothing here estimates these long–long sums or the exterior crosses.** The two signed variables are genuinely linked, so the tensor Mertens estimate used for the CRT main term cannot simply be substituted into this inner correlation.
