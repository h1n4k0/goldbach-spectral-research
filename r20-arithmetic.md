# One-sided divisor switching leaves a narrow mixed high-product survivor

**Claim.** Keep the parameters of R17–R19: N even, 1≤b≤N, Z=ceil(4bN), D=floor(Z^(1/3)), D²<Q≤Z² (the sector is empty above Z²), w=log N, and W=∏_{p≤w,p∤N}p. Call an integer good if it has at least two distinct prime divisors in W, and rough-for-this-step otherwise (zero or one such prime). Work on the exact signed high-product geometry d,e>D, de>Q after the original diagonal deletion. When n is good and m is rough-for-this-step, put L(n)=pq, where p<q are the least two distinct primes from W dividing n. Define the base a=d/gcd(d,L(n)).

On this mixed sector the exact kernel can, with Hilbert–Schmidt error

    O_ε(b^(1/2)(Q/N)^(1/2)N^ε + b^(11/12)N^(-1/12+ε)),        (1)

be replaced on the entire physical prefix 0<x≤b by just its original arithmetic terms with

    a≤D,   a e>Q.                                               (2)

In particular these survivors satisfy D<d≤D(log N)² and e>Q/D. The reflected mixed sector has the reflected conclusion. This is a restriction of the genuine original signed coefficient, not an insertion of a conjectural compensating model. The arithmetic bound uses RH for ζ only; combining with the exact Hardy construction uses local GRH(N), and with the full R17 original-to-double-long estimate uses its auxiliary Dirichlet GRH. No estimate of the narrowed survivor, the rough–rough sector, or exterior crosses is claimed.

## 1. The exact split of one good-leg orbit

For fixed n,m,e and the chosen L=pq|n, write every squarefree d|n as d=a t with t|L, (a,L)=1. For each fixed base a all four divisor choices t are available since p,q|n. All weights except μ(d)log(n/d) are constant in this orbit. If ae>Q and a>D, the tests de>Q and d>D are automatic on the whole orbit and

    ∑_{t|L} μ(t) log(n/(a t))=0.

This is the exact double finite difference of an affine logarithm, not cancellation averaged over pairs. If ae>Q and a≤D, keep any original terms that satisfy d>D. They are precisely (2), with d=a t≤D L and e>Q/a≥Q/D. If ae≤Q, the only surviving high-product terms satisfy the **exact boundary mask**

    d,e>D,   Q<de≤Q(d,L).                                      (3)

Conversely on the original high-product sector (3) means ae≤Q. Thus the actual mixed kernel decomposes into the exact narrow survivor and the exact boundary (3), with the other orbits canceled. The argument counts all integers n,m including those with prime-power factors. An upper cut of the form de≤Qw² alone would be wrong: it might leave only part of a fully canceled orbit. We only use this upper bound to count the number of pairs in (3), while retaining its whole membership-dependent condition for the signed density.

## 2. Local selection and the signed boundary estimate

The least-two selection can be expanded exactly. For each fixed pair p<q in the ordered set of primes dividing W, its mask is

    1_{pq|n} ∏_{ℓ|W, ℓ<q, ℓ≠p} (1−1_{ℓ|n}),

where ℓ ranges over primes. These masks are disjoint and cover the good integers. Expanding them writes them as sums of divisibility conditions P|n with P|W, L=pq|P, and coefficients of size 1; **L remains the originally selected pair in each expansion term**, not the least pair dividing the expanded P. Similarly the rough-for-this-step mask is the complement of

    ∑_{R|W, ω(R)≥2}(−1)^ω(R)(ω(R)−1)1_{R|m},

the exact binomial formula for at least two factors. The total absolute coefficient mass of all these expansions is N^o(1), since π(w)=O(w/log(2w)) and W≤exp(O(w))≤N^C. It suffices to bound (3) uniformly on each fixed sector P|n,R|m with P,R|W, and with the chosen two-prime product L|P.

Fix h=jN and one orientation n+m=h, n−m=h, or m−n=h, with both normalized positions in an arbitrary hard rectangle in [0,b]². In the raw n-coordinate n,m≥1 the marker log(n/d)log(m/e) has supremum and total variation O(log² Z). For each d,e in (3), CRT with the imposed divisibilities tests gcd([d,P],[e,R])|h, and, if compatible and (de,N)=1, gives density

    (φ(N)/N)/lcm(d,e,P,R).

This uses that P,R are units modulo N, that n and m are simultaneous units because h is a multiple of N, and that inclusion–exclusion over c|N costs O(2^ω(N)) per raw progression. Partial summation therefore bounds the raw lattice error by O_ε(N^ε) per pair. Since d,e≤Z for actual divisors and de≤Qw² on (3), and #{d,e:de≤Qw²}≪Qw² log(2Qw²), the lattice error is O_ε(QN^ε) even after summing the local expansions.

For the CRT density itself, write d=u d_0,e=v e_0, where u,v|W and (d_0e_0,W)=1, and omit nonsquarefree values since μ already kills them. Put K=lcm(u,v,P,R) and t=(u,L). In this fixed local sector d,e meet the product condition Q<uv d_0e_0≤Qt. The local compatibility gcd([u,P],[v,R])|h is independent of (d_0,e_0)|h, since the parts use disjoint primes. Put g=(d_0,e_0), d_0=g c,e_0=g f. When compatible, the weighted CRT denominator is K g c f, and the remaining signs are μ(c)μ(f), times fixed μ(u)μ(v). In particular for each fixed u,v,g,c the f-variable runs over exactly one interval

    max{D/(vg), Q/(uvg²c)}
       < f ≤ min{Z/(vg), Qt/(uvg²c)},     (f,cgNW)=1.

The outer c-variable obeys D<ug c≤Z. By the coprime ζ-RH Mertens tail proved in [R18](r18-arithmetic.md), summing μ(f)/f with model marker log(T_2/(vg f)), T_2∈[1,Z], costs O_ε(Z^ε min{1,(D/(vg))^(-σ)}) for σ=1/2−η, η>0 arbitrarily small. This uses one interval difference, so the unrestricted constants cancel, and the omitted-Euler-factor modulus cgNW≤Z^{O(1)}. If vg>D the trivial harmonic/log bound suffices. Use min{1,(vg/D)^σ}≤D^-σ v^σ g^σ in both cases. The other marker and c harmonic sum cost only O(log²Z), the sum of g^(-1+σ) over g|h is ≤τ(h)≪_ε Z^ε, and v^σ/K≤1 absorbs the lower-cutoff factor v^σ. Summing over local u,v and P,R masks thus gives signed density bound O_ε(Z^ε D^-σ) uniformly in the raw continuous coordinates T_1,T_2∈[1,Z]. There is no main term retained on this exact boundary. Integrating over O(Z) raw length and using 1/N normalization gives O_ε(QN^(-1+ε)+b^(5/6)N^(-1/6+ε)) on each exact line and hard rectangle. Neither this step nor the orbit switch replaces either Möbius sign by an artificial sequence.

## 3. Hardy transfer and quantified survivor

The line estimates sum over O(b) shifts and the original orientations. Layer cake for √uv bounds the physical cumulative A(x,y) of the actual boundary by √xy times O_ε(b Q N^(-1+ε)+b^(11/6)N^(-1/6+ε)). Independently, the raw absolute divisor bound on the exact (3) mask, including the genuine least-two/rough selection rather than its expansion, gives |A(x,y)|≪_ε Z^ε(log Z)^2(xy)^(3/2): for x≤y, nontrivial lines require x+y≥1, and each n≤Nx has O(y) partners, each with at most d(n)d(m) divisor choices. On x,y≥1/N the log-coordinate Hardy kernel is 2π A(x,y)/(xy√(w_N(x)w_N(y))), with w_N≥1/2. Multiplying the two complementary bounds and integrating over log area O(log²N) gives (1). At the true lower edge x<1/N or y<1/N the arithmetic cumulative is zero, as no positive integer is present, with no Beta term in this boundary.

Combining R18's control of de≤Q, R19's control of the both-good high-product sector, and this one-sided estimate yields an exact narrow description of the uncontrolled prefix kernel up to the stated power-scale error:

1. The original high-product long–long pairs with both legs rough-for-this-step.
2. The original high-product mixed pairs on each orientation, but only when the good divisor meets (2), and hence D<d≤D(log N)² while the other divisor satisfies e>Q/D. Reflect for a good second leg.

For b=N^(3/40), Q=N^(7/8) the Hilbert–Schmidt error is O_ε(N^(-7/480+ε)), D has size N^(43/120), and Q/D has size N^(31/60). These are actual divisor-index restrictions, not all-modulus norm estimates on the survivors. The scope includes the full prefix geometry and no exterior cross or unbounded tail. Neither the rough–rough nor the narrowed mixed signed covariance is shown small; no conclusion about S/R follows.
