# Geometry-adaptive cancellation in the middle of the mixed survivor

**Claim (global Dirichlet GRH).** Keep the genuine mixed remainder from [R20](r20-arithmetic.md), with even N, 1≤b≤N, Z=ceil(4bN), D=floor(Z^(1/3)) and D²<Q≤Z². On the orientation where n has the selected two small prime factors and m has at most one, each term has d,e>D, n=d k, m=ℓ e and the exact R20 tests a=d/(d,L(n))≤D, ae>Q. Define

    M(n,m)=max{1,n/N,m/N}.

Retain precisely the terms for which

    ℓ √e · M(n,m) ≤ H,                                         (1)

and reflect the condition on the other mixed orientation. Keep the genuine signs and all original units. The arithmetic kernel of this selected term, compressed to the entire physical prefix 0<x≤b, obeys

    ∥C_H∥HS ≪_ε (D H/N)^(1/2) N^ε                             (2)

uniformly for H>0 and every sufficiently large even N; an additional interval restriction on e is allowed. In particular H=N^(1−η)/D, any fixed η>0, gives O_ε(N^(-η/2+ε)). This is an exact curved selection on genuine arithmetic summands, not a nominal interval at each scale. It covers middle exponents absent from the previous two R21 sectors, with a nonzero surviving orbit exhibited in §3. No bound is obtained for the complement of (1), the rough–rough sector, or exterior crosses, and no conclusion about S/R follows.

Global GRH is needed for the uniformly masked twisted Möbius progression estimate of [R21 high-e](r21-arithmetic-high-e.md) on auxiliary moduli. The local GRH of the original paper identifies the Hardy operator; comparison with the actual residual also uses the hypotheses of R17 and subsequent reductions. There is no averaging in N here.

## 1. One masked progression per choice of the fixed factors, with at most two intervals

Work first on one orientation, with n the good integer. Apply the same least-two and rough Boolean expansions as R20/R21. A fixed sector imposes P|n and R|m, P,R dividing the small-prime product W, with fixed two-prime choice L|P. The exact coefficient mass is N^o(1), and P,R≤N^{O(1)}. This expansion is valid on the exact R20 survivor because the selected pair L stays fixed in each expansion term, and the projected low/rough conditions are precisely the corresponding Boolean masks.

Fix one alias h=jN, a hard rectangle in (n/N,m/N), and d and ℓ. The constraint on d implies D<d≤D(log N)^2. On the line m=ℓ e and n is h+ℓ e, h−ℓ e, or ℓ e−h. Discard d or ℓ nonunit modulo N. Then the original restrictions [d,P]|n and R/(R,ℓ)|e impose at most a single residue class for e by CRT, and (nm,N)=1 reduces to (e,N)=1. The progression modulus is ≤Z^{O(1)} and may be nonreduced; this is allowed by R21's explicitly proved uniform bound.

Take fixed dyadic ranges for the two positive physical integer positions n and m (start at 1, normalize by N) and a dyadic range E≤e<2E. These dyadic tests only intersect the hard-coordinate intervals and do not change the signs. For fixed d,ℓ all the prior raw predicates (positivity, d,e>D, ae>Q, the two hard-coordinate intervals, and the three scale boxes) give one e-interval, possibly empty. To impose (1) on that interval, intersect the three sublevel conditions

    ℓ√e≤H,    ℓ√e·n(e)≤NH,    ℓ√e·m(e)≤NH.

The first and third are monotone. The second is monotone in each of the increasing positive orientations. In the orientation n=h−ℓe it is a sublevel condition for a positive unimodal function √e(h−ℓe); its derivative is (h−3ℓe)/(2√e). It therefore gives at most two intervals. Intersecting with all the other tests still leaves at most two intervals. This argument enforces the curved cutoff exactly.

The marker log(n/d) is monotone with supremum and total variation O(log Z) on each positive interval; μ(d)log ℓ is fixed. By the R21 masked Möbius progression bound and Abel summation, each resulting signed e-sum is O_ε(N^ε √E), including arbitrary endpoints.

## 2. The physical factor M cancels the alias multiplicity

For the current n,m scale boxes write M_0=max{1,U,V}, where U,V are the lower endpoints for n/N,m/N. Throughout the boxes M(n,m)≥M_0 and M(n,m)≪M_0. At most O(M_0) integer shift multiples jN can meet the boxes: any such j satisfies j≤n/N+m/N≪M_0. Under (1) and e≥E, the cofactor satisfies

    ℓ≤H/(M_0√E).

If this upper bound is less than 1 there are no terms; otherwise the same number bounds the count of possible ℓ. Sum the signed e-bound from §1 over these ℓ and O(D(log N)^2) choices of d. The result is O_ε(N^ε D H/M_0) per alias for this set of scale boxes. Summing the O(M_0) aliases cancels that denominator. There are O((log N)^3) dyadic triples since all n,m,e≤Z≤O(N²), and restoring the Boolean sector coefficients is another N^o(1). Thus each genuine selected **hard rectangle**, before normalization, has absolute signed mass O_ε(N^ε D H). This does not use any cancellation between different aliases; the exact density of aliases is accounted for in (1).

Normalize by N and apply the positive √uv layer cake to get the bound O_ε(N^ε D H/N · √(xy)) for the cumulative A(x,y). Independently the actual masked divisor coefficient is bounded in absolute value by O_ε(Z^ε(log Z)^2) per pair, because the number of possible divisor pairs is at most d(n)d(m) even before the selection. At x≤y a nonzero line requires x+y≥1, and each n≤Nx has at most O(y) partners, giving |A|≪_ε Z^ε(log Z)^2(xy)^(3/2). Multiply the two bounds in the square of the Hardy log kernel 2π A/(xy√(w_N(x)w_N(y))). On x,y≥1/N both weights are bounded below and the log area is O((log N)^2); if either coordinate is below 1/N, the true arithmetic cumulative is zero. The squared HS norm is therefore O_ε(N^ε D H/N), proving (2).

At b=N^(3/40), D≈N^(43/120), η=1/100 and H=N^(1−η)/D, when n,m≤C N for fixed C the cut includes every retained mixed term with e≥max(1,C)^4 D² N^(2η), a bound of order N^(221/300). Indeed ℓ√e=m/√e and M≤max(1,C). More precisely, on the fixed physical compression x,y≤C, take H=max(1,C)^2 N^(5/8) and impose the additional interval e≥N^(3/4): all those actual terms satisfy (1), and (2) gives HS norm O_{C,ε}(N^(-1/120+ε)) while keeping the original wide-prefix D. This uses the proof with an extra interval, not monotonicity of the norm under deleting signed terms. The estimate here reaches e of order N^(3/4), far below the earlier wide-prefix high-e cutoff N^(21/20). At the largest physical scale M≈b the estimate instead agrees with the previous worst-case upper-end tradeoff. This is a variable exact set, not a claim that all middle divisors at every height have been removed.

## 3. A genuine new nonzero switched orbit, not a claim about the aggregate

Use X as an independent large construction parameter and set r=43/120. By the prime number theorem choose four distinct primes in fixed 1%-relative windows whose left endpoints are

    a ≈ (1/2)X^r,        k ≈ (2/15)X^(1−r),
    e ≈ 2X^(3/4),        ℓ ≈ (1/2)X^(1/4).

More precisely take each in the interval from the indicated endpoint to 1.01 times it. The powers are distinct and grow, so the four primes differ from one another and from 3,5. Define n=15 a k, m=eℓ, N=n+m. Then n,m are odd, N is even, n,m∈[X,1.0201X] and hence n,m≈N/2 on the actual first alias h=N. Their prime factor sets are disjoint, so (nm,N)=1. In particular 3,5∤N; the least two primes of n from W are exactly 3,5, while m has no prime ≤log N. Thus the actual R20 mixed selection, not just the nominal coordinates, holds.

Take b=N^(3/40), Q=N^(7/8) and D as stated. Since N∈[2X,2.0402X] and a∈[X^r/2,1.01 X^r/2], the quotient D/a lies in (3,5) for all large X (its central constant is 2·4^(1/3)·2^r≈4.07). Thus a≤D and the allowed factors of 15 with a·t>D are exactly t=5,15. Moreover ae≈N^(r+3/4)≫Q, e>D and m=eℓ has the chosen nonzero logarithmic cofactor. The genuine two-term orbit for this fixed e therefore has raw signed value

    μ(a)μ(e) log ℓ · [−log(n/(5a)) + log(n/(15a))]
       = −log(3)log(ℓ)≠0,

before the common outer line sign. Both choices have the same exact base a. Since M=1 and ℓ√e≈N^(5/8)<N^(1−η)/D for η=1/100, they fall under (1). The divisor e actually exceeds N^(3/4) by a fixed factor in the chosen windows, yet is below N^(21/20); it is in particular strictly between the wide-prefix R21 low and high ranges e≤N^(3/5) and e≥N^(21/20). This constructs a genuine admissible nonzero switched orbit in the new set along arbitrarily large even N. It says nothing about noncancellation of the sum over other orbits; that signed aggregate is bounded only by (2) on the selected set.
