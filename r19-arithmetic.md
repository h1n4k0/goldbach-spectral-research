# Pointwise cancellation in the high-product sector with two small primes on each leg

**Claim (ζ RH for the arithmetic estimate).** Use the R17 and R18 genuine signed double-long geometry: N even, 1≤b≤N, Z=ceil(4bN), D=floor(Z^(1/3)), and Q>D². Set w=log N. Keep the true terms d,e>D, de>Q, and impose additionally that **each** of n and m has at least two distinct prime divisors p≤w with p∤N. Keep the exact unit restriction modulo N and the three original signed line families after exact diagonal removal. Insert no Beta model. The resulting physical-prefix kernel C^{two-small}_{>Q} satisfies

    ∥C^{two-small}_{>Q}∥HS ≪_ε b^(1/2)(Q/N)^(1/2)N^ε + b^(11/12)N^(-1/12+ε).       (1)

For b=N^(3/40), Q=N^(7/8) this is O_ε(N^(-7/480+ε)) for every even N on RH. This is an actual high-product component, not the low-product cut redefined. Complete Möbius divisor orbits cancel exactly before evaluating the terms near the product threshold. Local GRH(N) identifies the genuine Hardy kernel; combining with the original-to-double-long reduction of R17 further uses global GRH for the short-divisor progression input. The remaining high-product term (with at least one leg having at most one such prime divisor) is **not bounded here**. The remaining class is not asserted to be sparse uniformly in N, and neither S nor R follows.

## 1. Exact Boolean selection, then a genuine divisor switch

Let W=∏_{p≤w,p∤N}p. For a positive integer n write ω_W(n)=#{p|W:p|n}. The identity

    1_{ω_W(n)≥2} = ∑_{P|W,ω(P)≥2} (−1)^ω(P)(ω(P)−1) 1_{P|n}

holds for all n. For k=ω_W(n)≥2, it is the binomial identity ∑_{j=0}^k (−1)^j(j−1)binom(k,j)=0 with its j=0 term −1; for k=0,1 both sides are zero. Chebyshev gives W≤exp(O(w))≤N^C and τ(W)=2^{ω(W)}=exp(O(w/log(2w)))=N^o(1). Therefore the total absolute coefficient mass in the two Boolean expansions is N^o(1).

It suffices to bound every fixed divisibility sector P|n, R|m with P,R|W each having ≥2 distinct prime factors, uniformly in P,R. Choose fixed products L_1|P and L_2|R of two distinct prime factors each, so L_1L_2≤w⁴. Given a pair (n,m) in this sector, organize the squarefree divisors as

    d=d_* a,   a|L_1,   (d_*,L_1)=1,
    e=e_* c,   c|L_2,   (e_*,L_2)=1.

Because L_1|n and L_2|m, every divisor choice a,c in each such orbit is available, even if n or m are not squarefree. Consider an orbit with d_*e_*>Q>D². Then product de>Q is automatic for all a,c, and one of d_*,e_* exceeds D. On that axis all four Möbius terms satisfy the long cutoff, and its entire sum is exactly zero:

    ∑_{a|L_1} μ(a)log(n/(d_*a)) = 0.

The equality is the double finite difference of the affine logarithm with respect to the two distinct primes. The other axis may be truncated by e>D, but its restriction then separates and cannot break this cancellation. Thus only orbits with base product d_*e_*≤Q survive. Their exact original mask is

    d,e>D,     Q<de≤Q(d,L_1)(e,L_2).                         (2)

In particular de≤Qw⁴. The upper limit in (2) depends on the actual divisor memberships. Replacing (2) by the plain band Q<de≤Qw⁴ would be incorrect: it could cut a fully canceled orbit and leave part of it. The membership-dependent mask is retained throughout.

## 2. CRT and the conditional Möbius tails in this exact mask

Fix a line n+m=h, n−m=h or m−n=h, h=jN, and a hard rectangle of normalized u=n/N,v=m/N. For each d,e in (2), the two divisibilities on the line are now [d,P]|n and [e,R]|m. Values where (de,N)>1 do not contribute. Since P,R are units modulo N, CRT requires gcd([d,P],[e,R])|h and gives line density

    (φ(N)/N)/lcm(d,e,P,R).

The unit error is O(2^ω(N)) per pair by inclusion–exclusion, and marker log(n/d)log(m/e) again has O(log² Z) size and total variation on raw n,m≥1. Any actual d,e≤Z, and there are O(Qw⁴ log(2Qw⁴)) allowed pairs in (2). The total raw lattice error is consequently O_ε(Q N^ε). Nothing here assumes support only on primes or removes proper powers from n,m.

To bound the main density with its true signs, decompose d=u d_0,e=v e_0 where u,v|W and (d_0e_0,W)=1; restrict to squarefree divisors as required by μ. Let κ_1=(u,L_1), κ_2=(v,L_2) and K=lcm(u,v,P,R). At fixed u,v the exact mask becomes

    Q<uv d_0 e_0≤Q κ_1 κ_2.

The compatibility condition on primes in W is gcd([u,P],[v,R])|h, and the remote one is (d_0,e_0)|h. They are independent because d_0,e_0 are coprime to W. Put g=(d_0,e_0), d_0=g a,e_0=g c. For an admissible term, g|h and (ac,gNW)=1, (a,c)=1. In absolute value the static W-density is ≤1/K and the Möbius-weighted density of the other divisors is μ(a)μ(c)/(g a c), up to the fixed signs μ(u)μ(v). More explicitly the full density multiplier used in the line integral has this form times φ(N)/N.

For fixed u,v,g,a, the admissible c's are exactly in the interval

    max{D/(vg), Q/(uv g² a)} < c ≤ min{Z/(vg), Q κ_1 κ_2/(uv g² a)},
    (c,ag N W)=1.

(The outer a variable also obeys D<ug a≤Z.) Thus the moving mask still has *one* interval after the local split. Use the same coprime Mertens tail from [R18](r18-arithmetic.md), a consequence of ζ RH after restoring the finitely many omitted Euler factors. For σ=1/2−η with fixed small η>0, the signed inner sum with marker log(T_2/(vg c)), T_2∈[1,Z], is bounded by

    O_ε(Z^ε min{1,(D/(vg))^-σ}).

For vg≤D both endpoints of a nonempty interval exceed 1, so this follows by subtracting coprime tails and the constants cancel exactly; if vg>D use the trivial harmonic/log bound. The excluded-factor modulus agNW≤Z^{O(1)}, even when P,R involve many small primes. The outer sum over a costs only O(log²Z) in absolute value. Summing g|h and using ∑_{g|h}g^(-1+σ)≤τ(h)≪_ε Z^ε, the density multiplier at fixed u,v is

    O_ε(Z^ε D^-σ · v^σ/K).

Crucially K≥v, so v^σ/K≤1. Summing all u,v|W costs N^o(1); summing all P,R Boolean terms costs another N^o(1), with no polynomial loss. The estimate is uniform in the raw coordinates T_1,T_2∈[1,Z]. Integrating over O(Z) raw length, dividing by N and applying D≈Z^{1/3} proves, on each exact signed line/hard rectangle,

    O_ε(Q N^(-1+ε)+b^(5/6)N^(-1/6+ε)).

There is no conjectural main term for this component. The cancellations used are the exact Möbius orbit switch on the integer coefficients, followed by ζ-RH Mertens on the residual CRT density.

## 3. Transfer and exact remainder

Sum the preceding hard-rectangle estimate over at most O(b) shifts and the original orientations. For the true signed cumulative A(x,y)=∫ √(uv)dμ up to x,y the layer cake gives |A|≪_ε√xy[b Q N^(-1+ε)+b^(11/6)N^(-1/6+ε)]. The other bound is the actual absolute divisor bound on the true high-product component before any expansions: |A|≪_ε Z^ε(log Z)^2(xy)^{3/2} since for x≤y with x+y≥1 each n≤Nx has O(y) line partners, and for each pair there are at most d(n)d(m) divisors. Both bounds apply with the exact Boolean masks. On x,y≥1/N multiply them after dividing by the square of xy√(w_N(x)w_N(y)) in the log kernel; w_N≥1/2 there, and the area costs O(log²N). On x<1/N or y<1/N the genuine cumulative is exactly zero, with no Beta term added. The result is exactly (1).

The R18 sector de≤Q may now be discarded along with the R19 high-product contribution on which both summands have ≥2 prime factors from W, at the stated power-scale error for b=N^(3/40), Q=N^(7/8). What is left is the true high-product long–long covariance on pairs for which at least one n,m has ≤1 prime divisor from W. The mod-N unit restriction can make W small, so no uniform density saving for the remaining pairs is asserted. Controlling the remaining signs across the actual short lattice fibers, as well as all exterior crosses, is still open in this approach.
