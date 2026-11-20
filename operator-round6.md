# Round 6: a genuine uniform bound at the onset of the first sum alias

**Scope.** This is an estimate for an actual nonzero-width compression of Li–Liu's full Hardy operator, for every sufficiently large even N satisfying their local GRH(N), not an average or an approximation argument. It treats a particular near-diagonal onset region, not the near band from Round 5 as a whole or the largest full-space eigenvalue. There is no proof or refutation of S or R.

Use the exact physical cumulative kernel of source-round2.md §1, which follows from the [original Li–Liu Mellin realization](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf). Thus raw integer coordinates are Nu,Nv and the unitarily conjugated operator on L²(du) has kernel

    𝒦_N(x,y) = 2π M_N(x,y)/( (xy)^(3/2) sqrt(w_N(x)w_N(y)) ),
    M_N(x,y) = ∫_(0,x]×(0,y] sqrt(uv) dμ_N(u,v),
    w_N(x) = (Nx)^(2α)/(1+(Nx)^(−2(β−α))), α=1/log N, β=1/8.

Here μ_N has actual Λ(n)Λ(m)/N atoms restricted to units and the subtracted continuous Hardy–Littlewood model, with the signs of the difference and sum aliases. Write S for S(N), L=log N. For 0<ε≤1/8, let P_ε multiply in these unitary coordinates by 1_{0<x≤1/2+ε}.

## 1. The bound

Uniformly for Nε≥1, one has

    || P_ε T_N P_ε ||_HS ≪ S ε² [ L / log(2+Nε) ]².                (1)

If Nε<1 then the stronger bound O(S ε²) holds. For each fixed η>0, whenever Nε≥N^η the logarithmic quotient in (1) is bounded by a constant depending on η. In particular the choice ε=L^(−a/2) gives O_a(S L^(−a)) for any fixed a>0; the choice ε=N^(−1/4)L^(1/2) gives o(δ_N), where δ_N=sqrt(S/N)L^(3/2), since S≪loglog N. The latter is an interval of raw width proportional to N^(3/4)sqrt(log N) about N/2, not a statement about a single Mellin test.

**Geometry and exact reduction.** Throughout the prefix square both raw-normalized coordinates are <1. The off-diagonal positive difference aliases cannot occur, the exact diagonal has already been removed, and the sole possible alias is the negative sum u+v=1. Therefore the kernel vanishes when max(x,y)≤1/2 or, more generally, when x+y<1. In the prefix it is supported, up to null sets, entirely on the square 1/2−ε≤x,y≤1/2+ε. On that square the kernel is explicitly

    M_N(x,y) = S∫_[1−y,x] sqrt(t(1−t)) dt
                − N^(−1) Σ_{n/N∈[1−y,x], (n,N)=1} sqrt((n/N)(1−n/N)) Λ(n)Λ(N−n),       (2)

with both expressions zero if the interval is empty. This uses the negative sign of the sum alias in μ_N. It also proves that the entire cross to x<1/2−ε from y≤1/2+ε vanishes, not just the corner restriction. Kernel factors involving x,y,w_N are uniformly bounded above and below on this small square, as 3/8≤x,y≤5/8 and (Nx)^(2α) is bounded above and below. These uniform facts allow a pointwise bound for M_N to give the HS bound after multiplication by the square root of the support area, at most 2ε.

**Upper sieve in a moving, short interval.** Set H=Nε≥1. All sums in (2) are bounded by the unsigned total Λ(n)Λ(N−n) on the central interval |n−N/2|≤H. The standard two-dimensional upper-bound sieve used in source-round2.md §3 and arithmetic-round4.md §A, applied to the two integer forms n and N−n on that interval, gives

    Σ_{|n−N/2|≤H} Λ(n)Λ(N−n) ≪ S (H+1) L² / log²(2+H).            (3)

Here is the needed uniformity argument for short H. Use a sieve level H^c with fixed small c>0 and a cutoff z=H^(c/u) for fixed sufficiently large u. For p|N the forbidden class modulo p is just 0; otherwise the forbidden classes are 0 and N. The local progression counts have error O(2^ω(d)) for squarefree d at the sieve level by interval counting; their accumulated O(H^c log(2H)) (or a fixed higher log power with nontrivial coefficient bounds) is absorbed by (H+1)/log²(2+H). The local product is ≪S/log²(2+H), by Mertens and the same Euler-factor comparison as the source. See [Matomäki–Merikoski, Lemma 3.2 and its upper sieve argument](https://www.utupub.fi/server/api/core/bitstreams/8f46b427-a8ed-4ffd-af2e-0534078bc62c/content) for this usual Selberg upper weight; its use here involves only the stated residue counts on an interval. All pairs of prime powers whose two bases exceed z pass the sieve, regardless of their exponents, and each pair contributes at most L². Small bases in either form contribute at most O(z L²): for each fixed prime base the total Mangoldt weight of its powers up to N is ≤L, and the other coordinate's weight is bounded by L. Since z log²(2+H)≪H+1, they are absorbed as well. Constants for bounded H are covered by the trivial interval count. This proves (3), without invoking a prime number theorem for short intervals or assuming asymptotics for Goldbach pairs.

Using H+1≤2H in (3), (2) has absolute value O(S ε L²/log²(2+H)), since the continuous part is O(S ε). If H<1, the sole possibly active integer is n=N/2, which is not a unit for N>2; hence (2) is model-only and O(S ε). The support area and denominator comparison prove (1). The argument bounds the actual Hilbert–Schmidt operator, not an arithmetic projection with the two interface vectors removed.

## 2. The quadratic onset exponent when there are no atoms

If the central interval contains no active unit prime-power pairs, the scaling ε² reflects the actual local operator. With the dilation x=1/2+εr, y=1/2+εs, r,s∈[−1,1], and unitary measure rescaling, one has

    (S ε²)^(-1) (dilated compression) = [8π/w_N(1/2)] A₀ + O_HS(ε),
    A₀(r,s) = max(r+s,0).                                         (4)

Indeed (2) now gives S ε max(r+s,0)/2 plus a uniformly smaller O(S ε²) kernel error, since sqrt(t(1−t))=1/2+O(ε) on this interval. The denominator in (2)'s operator at x=y=1/2 is w_N(1/2)/8, with relative O(ε) variation by differentiating w_N on [3/8,5/8]. The factor ε from the unitary dilation completes (4). The operator A₀ is nonzero, compact and real self-adjoint; for example testing the constant function proves ||A₀||>0. Thus the onset exponent ε² cannot be improved in general even without any actual prime pair there. In particular (4) applies for all N with Nε<1; w_N(1/2)→e² as N grows. It is not used for the upper bound (1) at wider windows with atoms.

Model-only windows can also have H→∞ as a purely arithmetic statement. Given a large integer H, choose two distinct primes q₁,q₂>H with q_i≤4H by Bertrand's postulate. Take M by CRT with M divisible by the primorial through H and M≡1 mod q₁q₂, and choose a representative M comparable to the product modulus. Set N=2M. For n=M+j with 2≤|j|≤H, a prime factor of j divides N and n; j=0 is nonunit; j=±1 has one member M−1 divisible by both q₁ and q₂, so that its Mangoldt weight is zero. There are no active pairs throughout this interval. Chebyshev's bound for the primorial logarithm gives log N≍H. The operator consequence is conditional on local GRH for such N; no claim is made that GRH(N) has been verified along this sequence.

## 3. Tested boundary of the argument

The geometric proof ceases to save a shrinking ε factor if the upper endpoint is a fixed distance beyond 1/2. At a general intermediate near-diagonal scale, the physical cumulative rectangles already include many full aliases below their upper edges: a sieve bounds the positive and negative masses individually, retaining a possible main-term signed error. Projecting to zero-moment functions inside each short physical cell kills the interfaces, but that is the fine subspace already covered in arithmetic-round4.md §B and is not the full near block. The finite-dimensional near matrix from Round 5 still contains both coarse endpoint modes, whose signed correlation is not controlled by (3). This note delivers one genuine local block, not a larger-eigenvalue bound.
