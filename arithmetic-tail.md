# Every-modulus outer-row cutoff by changing the Hardy strip

**Uniform but not an S/R bound.** Under the preprint's local GRH(N), the full operator and both of its crossing blocks can be truncated past a very large physical scale with controlled error. This statement does not require averaging over N. It uses the physical conjugation derived in source-round2.md and the variable-left-boundary estimate in Li–Liu §6.5.

Write α=1/log N, β=1/8, and t=Nx, the physical integer scale (x is the dimensionless variable). For 0<σ≤α let H_σ denote the unitary realization of the paper's T_{N,σ} in a *common* L²(dx). The discrepancy measure is independent of σ. The only σ dependence in the cumulative kernel is through w_σ(x)^(-1/2) in each variable, where

    w_σ(x)=1/(t^(-2σ)+t^(-2β)).

Consequently for σ<α we have the bounded multiplier factorization

    H_α = M_m H_σ M_m,       m(x)=√( w_σ(x)/w_α(x) ).

The identity holds first on compactly supported physical tests away from zero and infinity by the kernel formula; since m is bounded, it extends by density. For t≤1, m²≤2 because t^(-2β) dominates both sums; for t≥1, m²≤2t^{-2(α−σ)}. Therefore, writing P_R for multiplication by 1_{Nx≥R}, R≥1,

    ∥P_R H_α∥op = ∥H_α P_R∥op
      ≪ R^{−(α−σ)} [(log N)²+σ^(-2)].

The brackets follow from Li–Liu §6.5 with constants uniform in σ and N (boundary realization at β fixed). The HS estimate for the middle operator gives the same bound with HS norms. It follows that the difference H_α−(1−P_R)H_α(1−P_R) is at most twice this bound in either norm, including the exterior-interior crosses.

Setting σ=α/2 gives the simple bound O(R^(-1/(2log N)) log² N). For R≥N⁴ set σ=2/log R≤α/2. Then

    ∥P_R H_α∥op ≤ ∥P_R H_α∥HS ≪ (log R)² exp(−log R/log N).

For any fixed A>0, ε>0, taking R=N^{(A+2+ε)log log N} gives O_{A,ε}((log N)^{-A}); taking R=exp((1/2+ε)(log N)²) gives o(√(S(N)/N)log^{3/2}N) since S(N) is bounded below for even N. Constants refer to bounds, not an admissible exact equality at the endpoint of Hypothesis R. Reducing the remaining full norm to the precise R threshold still requires margin for this truncation error.

The unconditional arithmetic mean savings and the global-GRH power-window result control physical prefixes in the density sense, while this far-tail estimate is uniform under local GRH(N). They do not meet: between physical n around N^{1+γ} and n around N^{C log log N} (or farther for the R tolerance) lies a large unknown interval, with unknown coupling, and exceptional individual N remain.
