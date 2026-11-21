# Sparse exceptions for a growing full physical prefix

**Joint theorem (global Dirichlet GRH).** Let F(r)=a₂r²+a₁r+a₀∈ℤ[r] be fixed with a₂>0, and take R<r≤2R, N=2F(r), and X=C_F R² with a fixed C_F large enough that c_F X≤N≤X for all large R. Put L=log X. In the paper's physical-log coordinate p=log x, let Π_b=1_{p≤log b}; in particular the physical prefix starts at x=0, with no lower coordinate cutoff in the result. For each fixed 0<δ<1/12 and ε>0, uniformly for b≥1 and 0<τ≤1 with b²τ^(-2)≤X^(δ/2),

    #{r∈(R,2R] : ∥Π_b T_{2F(r),log} Π_b∥HS>τ}
       ≪_{F,δ,ε} τ^(-4) b^(13/3+δ/2) X^(1/3+δ/2+ε).       (1)

This bounds the number of exceptions for the operator norm as well. For instance b=X^(1/100), τ=X^(-1/400), δ=3/50 give exponent strictly below 0.42 on choosing ε sufficiently small. The eligible full prefix contains all scales 0<x≤X^(1/100) (n up to N X^(1/100)), not just the first Beta-active square: it includes the central range, near-zero interactions, all within-prefix cross blocks and a growing collection of genuine signed sum/difference shifts. Any fixed quadratic F is permitted, not just F(r)=r². This is not a representability record, an all-square or all-even theorem, an exterior-cross bound, or a proof or disproof of S/R.

Full Dirichlet GRH covers the auxiliary major-arc conductors; merely GRH(N) for a tested member of the thin family would not give the same arithmetic input. Local GRH(N) supplies the original Hardy realization and physical coordinate identification. The result builds on the individually controlled major arcs of [pinned Round 11](https://github.com/h1n4k0/goldbach-spectral-research/blob/95818f1d66a3a937f6e17a1b8b046a0fde3c64c1/ROUND11.md); the exact one-interval adaptive decomposition is from the spectral lane, and the shorter-axis bound and near-zero transfer from the operator lane. They are combined below to give the explicit coverage and exponent.

## 1. Adaptive rectangles on every signed shift line

Take Z=ceil(4bX), P=Z^(1/3−δ), and let E be any set of r of size M in the tested dyad. For a fixed integer 1≤k≤2b, consider one of n+m=kN or n−m=kN (the opposite difference is covered by interchanging coordinates). Prescribe any two dimensionless compact intervals I_r,J_r⊂[0,b], which may depend arbitrarily on r. Let Δ_r denote the normalized error between the weighted unit sum on this one line with (n/N,m/N)∈I_r×J_r and its model, S(kN) times the length in the normalized first coordinate; the arithmetic normalization is 1/N, not 1/(kN).

Then for every ε₀>0,

    ∑_{r∈E}|Δ_r| ≪_{F,δ,ε₀}
        √M D + M b X^(-δ),     D=Z^(5/4+ε₀) P^(-1/4)/X.     (2)

For clarity take the unrestricted Mangoldt counts first. Given the line and r, m is determined by n, so intersect the first variable's interval with the preimage of the second and use a single integer interval I'_r in the first factor. The second factor is now the full prime exponential sum over [1,Z]; for the difference use its conjugate. Replacing any raw real endpoints by rounded interval endpoints, if needed to use exact integer dyadic intervals, changes the model length by O(1) and the corresponding weighted count by O(log² Z). An empty interval causes no issue. The full second interval and the chosen first interval have the exact archimedean overlap length, up to that same O(1).

For any signs |σ_r|≤1 supported on E, the major integral with I'_r is computed individually for every r. The argument of the pinned R11 works with Z in place of X, cut P, and individual shift kN≤Z. Gauss-coefficient Parseval and the GRH PNT for characters give a prime factor error O(√(Zq)(log Z)²(1+Z|β|)), and integrating the mixed term and the two-error term separately gives O(√Z P^(3/2)(log Z)²+P³(log Z)^5). The individual Ramanujan and singular integral tails contribute O_{ε₁}(Z^(1+ε₁)/P): split the squarefree conductor q=q₁q₂ with q₁|rad(kN), (q₂,kN)=1. This is uniform in k,r and endpoints (difference conjugation does not affect the estimates, and c_q(−kN)=c_q(kN)). Together these errors are O_δ(Z^(1−δ)), so total at most M times this, here requiring GRH for the auxiliary q≤P. This use of individual major errors is necessary for adaptive cutoffs.

On minor arcs split each integer interval I'_r into a disjoint dyadic cover with at most two intervals per level. At a fixed level group by dyadic interval I; its selected set E_I obeys ∑_I |E_I|≤2M. Let Q_I(α)=∑_{r∈E_I}σ_r e(−kNα). The sparse fourth moment is

    ∥Q_I∥₄ ≪_{F,ε₀} |E_I|^(1/2) X^ε₀.

Indeed for unequal indices the integer difference F(r)−F(u) factors as (r−u)(a₂(r+u)+a₁); a nonzero value has O(d(|F(r)−F(u)|)) representations, since a factor r−u determines r+u. The zero difference is just r=u for large R. Multiplying all frequencies by fixed k has no effect on energy. The additive energy (sum of squared multiplicities of the differences) is therefore O_{F,ε₀}(|E_I|² X^ε₀) after relabeling ε₀. By the [Vinogradov–Vaughan bound](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf) and Parseval the full prime sum U on these minor arcs has ∥U∥₄≪Z^(3/4)P^(-1/4)(log Z)^(9/4). For each dyadic I use Hölder (2,4,4) for its prime sum U_I, the fixed full U and Q_I. Summing over I by Cauchy–Schwarz, disjointness on each level gives

    ∑_I ∥U_I∥₂∥U∥_{4,minor}∥Q_I∥₄
      ≪_{F,ε₀} √M Z^(5/4+ε₀)P^(-1/4).

There are O(log Z) levels, absorbed by relabeling ε₀. This step has no moving-grid loss and allows entirely arbitrary intervals per r. Normalize by N≈_F X (or absorb the bounded factors X/N into the arbitrary coefficients), and choose signs of the final errors. The major errors become O(M b X^-δ). To restore the unit condition modulo N: two distinct primes with sum or difference a multiple of N must both be units, and at most one equal pair can be discarded on a fixed line. Proper prime powers are O(√Z), each determining at most one partner, and their removal costs O(√Z (log Z)²/X) for an individual normalized line, absorbed in b X^-δ. This proves (2).

## 2. Multiply the selected L¹ estimate by a genuine uniform bulk bound

Let μ_N denote the normalized arithmetic-minus-model signed measure on positive (u,v) after exact subtraction of n=m. In [0,b]² only k≤2b in the three line families can contribute. Summing (2) over those lines bounds the selected sum of absolute discrepancies of each moving rectangle by O(b√M D+M b²X^-δ). In particular with

    A_N(x,y)=∫_{(0,x]×(0,y]}√(uv) dμ_N(u,v)

the layer cake √u√v=∫₀ᵘ∫₀ᵛ ds dt/(4√(st)) gives, uniformly x,y≤b,

    ∑_{r∈E}|A_N(x,y)| ≪_F √(xy) (b√M D+M b² X^-δ).        (3)

All signs are centered line by line before summation; the selection E may depend on the ultimate compression norm. The precise log kernel is 2π A_N(x,y)/(xy√(w_N(x)w_N(y))), where w_N(x)=1/[(Nx)^(-2/log N)+(Nx)^(-1/4)].

On the bulk a≤x,y≤b with a=X^-1/4, notice the stronger pointwise arithmetic bound

    |A_N(x,y)| ≪_F S(N)(xy)^(3/2).                          (4)

Here is the short-axis sieve justification. By symmetry take x≤y. The discrepancy vanishes unless x+y≥1, so y≥1/2; any contributing shifts satisfy k≤2y. For one line sum or difference, the smaller variable spans at most T=Nx≥c_F X^(3/4). The ordinary two-form upper sieve on the interval of length T counts O(S(kN)T/log²(2T)) values where both prime factors have bases above T^(1/c) for a sufficiently large fixed c: each local prime excludes two residues unless it divides kN, when it excludes one, and squarefree remainder costs at most its number of excluded residues. Such terms have weights O(log² Z). If either base prime is ≤T^(1/c), sum over powers of each such prime: their Mangoldt weights total O(log Z), even for the translated/reflected form; the other factor is at most O(log Z). These small-base weights thus total O(T^(1/c)log² Z), absorbed in O(S(kN)T). Since b≤X follows from the theorem's condition, log Z/log T is bounded. Dividing by N bounds a line's total variation by O(S(kN)x), also true for the continuous model. The weighted bound follows since weights ≤√(xy) and ∑_{k≤2y} S(kN)≪S(N)y for y≥1/2; the latter follows by the nonnegative divisor expansion of S(kN)/S(N) whose mean coefficients ∑a_{N,d}/d are uniformly bounded. This proves (4) without using pair asymptotics.

On this bulk w_N(x),w_N(y)≥1/2. Thus (3) bounds the selected sum of absolute **log** kernels by O((b√M D+M b²X^-δ)/√(xy)), while (4) bounds an individual log kernel by O(S(N)√xy). Multiplying cancels the factors √xy. Since S(N)≪L and the bulk log area is O(L²), the selected integral of the squared log kernels on the bulk is bounded by O(L³[b√M D+M b² X^-δ]).

## 3. The genuine x=0 edge and the exceptional count

For x<a (large R ensures a<1/4), a nonzero cumulative forces y≥1−x≥3/4: all nontrivial lines have x+y≥1. Use the trivial bound per small n≤Nx with O(y) possible integer shifts across the other leg, weight ΛΛ≤C L² and √(uv)≤√(xy). Together with the continuous divisor mean this gives |A_N(x,y)|≪_F L²(xy)^(3/2) for x<a. Therefore the squared log kernel on this edge is O(L⁴ xy/(w_N(x)w_N(y))). In the log measure dp dq=dx dy/(xy) its integral is O_F(b L⁴ a): one has ∫₀ᵃ dx/w_N(x)≪a+1/N≪a, by explicitly integrating the exponent 1/4 below x=1/N, and ∫_{3/4}^b dy/w_N(y)≪b. The opposite edge is the same, and both-small coordinates have exactly zero kernel. This is a deterministic per-r bound at the true edge, not an assumption of uniform Hardy weights at x=0.

With a=X^-1/4 and δ<1/12, the edge bound is absorbed in the bulk's second term, giving

    ∑_{r∈E}∥Π_b T_{2F(r),log}Π_b∥HS²
       ≪_{F,δ,ε₀} L³ [b√M D+M b² X^-δ].

Choose E to be the actual exceptional set for threshold τ. By b²τ^-2≤X^{δ/2}, the second term is o(Mτ²). If M>0, this leaves M≪ τ^-4 b² L⁶ D². Since D²=(Z^(7/3+δ/2+2ε₀))/X² and Z≈bX, absorbing logs and b^{2ε₀} via b≤X, and relabeling ε₀, proves (1). The only norm controlled is the full prefix compression; outside-prefix crosses and the possibility of infinitely many remaining exceptions are untouched.
