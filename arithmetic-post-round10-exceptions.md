# Sparse-support exceptional bound for the Beta-active block on doubled squares

**Candidate theorem (full Dirichlet GRH).** Let R be large, X=8R², L=log X, and N=2r² for R<r≤2R. On the physical logarithmic axis let J=[log(1/2),log(9/16)] and T_{N,J}=1_J T_{N,log}1_J, using the exact odd-character residual, diagonal and Beta subtraction of Li–Liu. For fixed 0<δ<1/12 and ε>0,

    #{r∈(R,2R]: ∥T_{2r²,J}∥HS>τ}
      ≪_{δ,ε} τ^(-6) X^(1/3+δ/2+ε),     X^(-δ/4)≤τ≤1.       (1)

In particular the exceptional count at any fixed inverse-log threshold τ=L^(-A) is O_{A,ε}(X^(1/3+ε)), or O_{A,ε}(R^(2/3+ε)) after changing ε. The estimate also bounds the count for the smaller operator norm. For example τ=X^(-1/100) and δ=1/20 yield O(X^.43) exceptions (choose ε small), among ≍X^.5 doubled-square moduli. The GRH assumption for major arcs includes Dirichlet conductors up to the auxiliary cutoff P below, **not just** conductors dividing 2r²; the identification with the original Hardy operator additionally uses local GRH(N). This is a statement about a centered HS compression, not a representability record, an all-square or all-even theorem, or a proof or disproof of S/R.

The [pinned Round 10 result](https://github.com/h1n4k0/goldbach-spectral-research/blob/df49c707d35986232009cff619b9b23cdaa4dad3/ROUND10.md) gave HS² mean O(X^(-1/400)) under full GRH. Its Markov corollary at fixed inverse-log threshold is O(X^(199/400)L^(2A)), and at τ=X^-1/100 supplies no power-saving exception count. The new dependence on the actual exceptional support and the larger, individually controlled major arcs are essential.

## 1. Fixed boxes: all selected indices, not merely the whole dyad

For arbitrary intervals I_1,I_2⊂[0,X], set s=2r²,

    A_s=∑_{n+m=s, n∈I_1,m∈I_2} Λ(n)Λ(m),     V_s=∫1_{I_1}(u)1_{I_2}(s−u)du.

We show that every subset E⊂(R,2R] of cardinality M satisfies, uniformly in I_1,I_2,

    (1/X) ∑_{r∈E}|A_{2r²}−S(2r²)V_{2r²}|
      ≪_{δ,ε} √M X^(1/4+ε) P^(-1/4) + M X^(-δ),
      P=X^(1/3−δ).                                          (2)

For any real |σ_r|≤1 supported on E, use e(t)=exp(2πit), P_j(α)=∑_{n∈I_j}Λ(n)e(nα), and Q(α)=∑_{r∈E}σ_r e(−2r²α). Orthogonality expresses ∑σ_r A_s as ∫P_1P_2Q. Choose σ_r to be signs of the final discrepancies to obtain (2).

### Minor arcs and the selected fourth moment

Take the major arcs about reduced a/q, q≤P, of width |β|≤P/(qX), disjoint since 2P²<X. Dirichlet approximation with denominator ceiling(X/P) gives on the complement a reduced approximant with P<q≲X/P and error ≤1/q². The [Vinogradov–Vaughan bound](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf) on each prime sum, by subtracting prefixes (or using the trivial bound if a prefix is shorter than q), implies |P_j|≪XP^(-1/2)L⁴ there; the X^(4/5) term is smaller for this P. Parseval and ∑_{n≤X}Λ(n)^2≪XL give ∥P_1P_2∥₁≪XL. Interpolating yields ∥P_1P_2∥_{4/3,minor}≪X^(5/4)P^(-1/4)L^(11/4).

For the fourth moment of Q, let D_E(t)=#{(r,u)∈E²:r²−u²=t}. Taking absolute values in the orthogonality expansion gives ∥Q∥₄⁴≤∑_t D_E(t)^2. Here D_E(0)=M. For t≠0 the factorization (r−u)(r+u)=t implies D_E(t)≤d(|t|), and |t|≪X. The elementary divisor bound and ∑_{t≠0}D_E(t)≤M² give ∥Q∥₄≪_ε M^(1/2) X^ε. Consequently the minor-arc integral is ≪_ε √M X^(5/4+ε)P^(-1/4), allowing an arbitrarily small chosen ε after absorbing logs. This is valid for arbitrary selected signs and saves the essential factor (M/R)^(1/2) over use of a whole-dyad fourth moment.

### Individual major arcs via character Parseval

Let V_j(β)=∫_{I_j}e(βu)du. Uniformly on each arc,

    P_j(a/q+β)=μ(q)V_j(β)/φ(q) + E_j(a,q,β),
    |E_j(a,q,β)|≪√(Xq)L²(1+X|β|).                          (3)

Indeed on the unit residue classes expand e(an/q) in characters. The unnormalized Gauss coefficients τ(χ,a)=∑_{b mod q,(b,q)=1} e(ab/q) overline(χ(b)) satisfy ∑_χ |τ(χ,a)|²=φ(q)², by finite character orthogonality. Hence φ(q)^(-1)∑_χ |τ(χ,a)|≤√q. For each χ, the [GRH PNT for characters and progressions](https://arxiv.org/abs/2301.13457) bounds the untwisted prefix error after removing the principal main term by O(√X L²), uniformly for prefixes up to X. If using the bound only at x≥q, smaller prefixes here are harmless by the trivial Chebyshev bound q≤P<√X. Abel summation supplies 1+X|β|; the principal coefficient is μ(q). Nonunits contribute only powers of primes dividing q, O(L²), and q=1 follows from RH for ζ.

For a fixed r the weight e(−sα) has modulus one. Expand the two errors rather than inserting their maximum. Since |V_j(β)|≪X/(1+X|β|), each mixed term, summed over a at fixed q, has integrated absolute size O(√X P L²/√q). The double-error term has integrated size at fixed q at most

    φ(q)q L⁴ ∫_{|t|≤P/q}(1+|t|)²dt ≪ P³ L⁴/q,
    t=Xβ.

Thus the entire major-arc expression differs from its principal model, **individually for each r**, by O(√X P^(3/2)L²+P³ L⁵). With P=X^(1/3−δ) this is O_δ(X·X^(-δ)). This larger parameter would not follow from using an absolute maximum of the two prime errors over the entire arc union.

### Uniform individual Ramanujan and integral tails

Summing over a gives μ²(q)c_q(s)/φ(q)^2 times the truncated β integral. For squarefree q, write q=q_1 q_2 where q_1|rad(s) and (q_2,s)=1. In absolute value the coefficient before the integral is exactly 1/[φ(q_1)φ(q_2)^2]. For every ε>0, uniformly s≤X and P≤X,

    ∑_{q>P} μ²(q)|c_q(s)|/φ(q)^2 ≪_ε X^ε/P,
    ∑_{q≤P} q μ²(q)|c_q(s)|/φ(q)^2 ≪_ε X^ε.

For the first, sum over q_1|rad(s). If q_1≤P, use ∑_{q_2>Y}φ(q_2)^(-2)≪_η Y^(-1+η) with Y=P/q_1, so the contribution per q_1 is ≤ X^{O(η)}/P. If q_1>P, use the convergent unrestricted q_2 series and φ(q_1)^(-1)≤X^{O(η)}/P. The divisor count costs X^η. For the second, use q_1/φ(q_1)≤X^η and ∑_{q_2≤P}q_2/φ(q_2)^2≪_η P^η, then choose η sufficiently small given ε. Both estimates are individual, not averages over the dyad.

The omitted β integral past P/(qX) is O(qX/P) by |V_j(β)|≪min(X,|β|^-1); the resulting error and the singular-series tail are O_ε(X^(1+ε)/P), contained in the claimed major error on taking ε small enough. The full stationary integral is V_s (the overlap length defined above), and the full Ramanujan series is S(s) by its Euler factors, with absolute convergence for each fixed s. Summing the individual errors over E therefore costs only M; combine with the signed minor estimate to prove (2).

## 2. Arbitrary selected sets under moving ratios and the cumulative Beta kernel

Take a partition of the r interval into K subintervals of equal length. On one subinterval bracket each moving box interval [as,bs] with fixed inner [a s_+,b s_−] (empty if reversed) and outer [a s_−,b s_+], where the endpoints of the original dimensionless intervals lie in [0,1] and s_+−s_−=O(X/K). The corresponding overlap lengths differ by O(X/K). Pointwise positivity brackets the arithmetic counts. Apply (2) to the selected indices E_i in each subinterval for both brackets. Since ∑_i√|E_i|≤√(KM), and S(s)≪L uniformly, the dimensionless signed rectangle discrepancy d_s satisfies

    ∑_{r∈E}|d_{2r²}| ≪_{δ,ε}
       √(KM) X^(1/4+ε)P^(-1/4) + M(X^(-δ)+L/K),           (4)

uniformly in both dimensionless intervals. Here normalize each count by s≈X. No union over hard-interval endpoints or assumption of equidistribution of E is made. Restricting to unit pairs changes each discrepancy by O(X^-1/2 L²): distinct prime summands are units, at most one equal prime pair is excluded, and there are O(√X) proper prime powers, each determining its partner. This is absorbed in (4).

To pass to the positive √u√v weights in the Volterra cumulative, use √u√v=∫_0^u∫_0^v da db/(4√(ab)) and integrate (4) for the moving hard rectangles [a,x]×[b,y]. The bound persists uniformly for x=e^p,y=e^q with p,q∈J, because the two positive layer-cake weights have bounded total integral. By exact cancellation of D, on J the only discrete offdiagonal is n+m=s and the only model line is u+v=1. Hence the resulting signed cumulative with the model subtracted is exactly the residual kernel up to factors uniformly bounded on J (including the factors xy and the original Hardy weights); this is the same identity as in the pinned R10. The two-dimensional upper sieve gives pointwise residual magnitude O(S(s))≪L, since the genuine prime pairs in these windows number O(S(s)X/L²). Multiplying (4) by that magnitude bound and integrating over the fixed J² yields

    ∑_{r∈E} ∥T_{2r²,J}∥HS² ≪_{δ,ε}
       L√(KM) X^(1/4+ε)P^(-1/4) + M(LX^(-δ)+L²/K).        (5)

The order matters: the uniform estimate for an arbitrary selected set is proved *before* integration, so one may choose E using the full kernel norm, not just one matrix element.

Finally take E={r:∥T_{2r²,J}∥HS>τ}, K=ceil(L³ τ^-2). For τ≥X^-δ/4, K≪R and the last two errors in (5) are o(Mτ²). If M>0, rearranging the first term gives M≪L²K τ^-4 X^(1/2+2ε)P^-1/2. Substituting K and P and relabeling ε proves (1). The surviving excluded moduli may still contain arbitrary hard cases; this proof neither bounds the whole Hardy operator nor supplies a uniform all-even estimate.
