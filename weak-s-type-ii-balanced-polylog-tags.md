# Cancellation on the full fixed balanced Type II box by polylogarithmic tags

**Conditional on global Dirichlet GRH.** Let $N=2^j$, $X=\sqrt N$, $L=\log N$, $L_2=\log L$. Keep the exact [R44 balanced Type II box](weak-s-type-ii-near-full-conductor-core.md),

$$
 I=[.740X,.745X],\qquad J=[.715X,.720X],\qquad D=[.445X,.450X].
$$

For arbitrary hard subintervals of these three intervals, with $u,v,d$ odd and $uv\equiv N\bmod d$, write

$$
 W(u,v,d)=\mu(u)\mu(d)\mu^2(N-uv)w(v),\qquad
 w(v)=\sum_{\substack{N^{.024}<p\le N^{.2499}\\p\mid v}}\log p
$$

where the sum is over primes. Then

$$
                  \left|\sum W(u,v,d)\right|
                    \ll_C \frac{N L_2^2}{L}=o(N).
 \tag{1}
$$

The dyadic numerator, full signs, squarefree gate, and fixed box are unchanged. By the earlier [unconditional short-divisor calculation](weak-s-type-ii-balanced-short-divisor.md), this also bounds the original $b_{\rm II}$-weighted sum on this fixed box (up to the global sign convention). The result does not cover the whole balanced transition, other moduli $N$ or weak S.

The change from R41–R44 is that the long-variable **exact zero-frequency energy is averaged over moduli**, instead of paying the worst individual GRH bound for all characters. The large-gcd trimming also replaces pointwise divisor bounds by actual divisor moments. Together these allow transfers from a tag range starting at a fixed power of $\log N$, not at $\exp(C L/L_2)$.

## 1. A centered dispersion bound with only logarithmic loss in the diagonal terms

Suppose $MU\asymp N,\ M,U,Q=N^{1/2+o(1)},\ Q/U=o(1)$, and $\alpha_m,\beta_n$ are $1$-bounded on dyadic intervals at scales $M,U$. Let $\beta$ be supported on odd squarefree $n>1$. Assume the pointwise bound $|\sum_n\beta_n\chi(n)|\ll\sqrt U N^{.03}$ for nonprincipal characters modulo $q\asymp Q$ (only conductors $\le N^{.05}$ will use it, and it will be checked on the genuine transferred coefficients). Let

$$
 \Delta=\sum_{\substack{q\asymp Q\\(q,N)=1}}
 \left|\sum_{mn\equiv N\bmod q}\alpha_m\beta_n
       -\frac1{\varphi(q)}\sum_{(mn,q)=1}\alpha_m\beta_n\right|.
$$

The dyadic interval here has a fixed bounded ratio, with the smooth enlargement used below. Then for a fixed absolute $\delta>0$,

$$
         \Delta \ll N L^6\sqrt{Q/U}+N^{1-\delta}.
 \tag{2}
$$

First prove the averaged zero-mode estimate

$$
 Z_\beta=\sum_{q\asymp Q}\frac1{q\varphi(q)}\sum_{\chi\bmod q,\ \chi\ne\chi_0}
                           \left|\sum_n\beta_n\chi(n)\right|^2\ll U .
 \tag{3}
$$

This includes all $q$, not only those prime to $N$. If $\chi$ is induced by a primitive $\psi\bmod f$, set $h=q/f$. Exactly $\chi(n)=\psi(n){\bf1}_{(n,h)=1}$, since primes of $f$ are already masked by $\psi$. One always has $\varphi(q)\ge\varphi(f)\varphi(h)$, including shared primes. For any fixed $f$ the sum of $1/\varphi(h)$ over $h\asymp Q/f$ is $O(1)$. Thus the number of low-conductor terms with weight $1/(q\varphi(q))$, counting primitive characters by $\varphi(f)$, is $O(N^{.05}/Q)$; the assumed bound makes their contribution $O(U N^{.11}/Q)=o(U)$.

For $f>N^{.05}$ expand ${\bf1}_{(n,h)=1}$ by Möbius inversion on $r\mid h$, and expand the conjugate similarly with $s\mid h$. For $\ell=[r,s]$,

$$
       \sum_{\substack{h\asymp Q/f\\\ell\mid h}}\frac1{\varphi(h)}
          \ll 1/\varphi(\ell).
$$

This is the [R44, §2](weak-s-type-ii-near-full-conductor-core.md#2-large-sieve-over-the-remaining-variable-part) bound: use $\varphi(\ell k)\ge\varphi(\ell)\varphi(k)$ and $\sum_{k\asymp Z}1/\varphi(k)\ll1$. At fixed $r,s$ in a dyad $f\asymp F$, use the primitive multiplicative large sieve and Cauchy. The coefficients after $n=r b$ have squared norm $\ll U/r$, and the factor $\psi(r)$ has modulus at most 1. With weight $1/\varphi(f)$ the sieve factor is $O(F+U/F)$ on each squared norm. Since $\sum_{r,s\ {\rm sf}}(\sqrt{rs}\varphi([r,s]))^{-1}<\infty$ by its Euler product, the result per dyad is $O((U/Q)(F+U/F))$. The dyads from $N^{.05}$ to $O(Q)$ give $O(U(1+U/(Q N^{.05})))=O(U)$. This proves (3) without individual GRH loss for the large-conductor energy.

For clarity, in the centered dispersion calculation let $B_{q,\lambda}=\sum_{n\equiv\lambda\bmod q}\beta_n$, $C_q=\varphi(q)^{-1}\sum_{(n,q)=1}\beta_n$. After Cauchy, $\Delta^2\ll MQ\,\mathcal W$, where $\mathcal W$ is bounded by the nonnegative smoothed sum of $|B_{q,\lambda}-C_q|^2$ over all $q\asymp Q$, unit $\lambda$, and $m\equiv N\bar\lambda\bmod q$ at scale $M$. Extending the nonnegative sum to all $q$ is as in the [centered neighboring-tile calculation, §2](weak-s-type-ii-medium-prime-tagged-slice.md#2-a-centered-neighboring-tile-estimate). Poisson in $m$ has zero factor $O(M/q)$. Exact multiplicative Parseval of the full centered zero mode therefore bounds it by $O(M Z_\beta)=O(MU)$.

The only other terms in the cited proof that do not have a fixed power saving after multiplication by $MQ$ are the large-gcd removal and zero restoration from $|B_{q,\lambda}|^2$. Use $G=N^\kappa,\ \kappa=10^{-5}$. If $g=(n_1,n_2)>G$ and $n_1\equiv n_2\bmod q$ are units, their quotients by $g$ are congruent since $(q,g)=1$. For fixed $m,n_1$, the number of possible $q$ is at most $\tau(|N-mn_1|)$, well-defined since $n_1>1$ is odd and $N=2^j$. Per divisor $g>G$ of $n_1$ there are $O(1+U/(GQ))$ possibilities for $n_2$. In place of a pointwise divisor bound use

$$
 \sum_{m,n_1}\tau(n_1)\tau(|N-mn_1|)
 \ll\sum_{\substack{t\ll N\\t\ne N}}\tau(t)^2\tau(|N-t|)
 \ll N L^9 .
$$

Here $t=mn_1$, the number of representations is at most $\tau(t)$, and the last bound is Cauchy with the standard fourth and second divisor moments. The support of the fixed smooth majorants stays at $mn_1\ll N$. For Poisson zero restoration count $n_2$ the same way, and use the weight $M/q$ and $\sum_{n_1\asymp U}\tau(n_1)\ll U L$. These give a joint $O(MU L^{10}(1+U/(GQ)))$ for the large-gcd pieces.

The remaining nonzero, small-gcd neighboring-tile bound uses only $1$-bounded odd squarefree $\beta$, together with $H_f=(Q/M)N^\kappa$, $G=N^\kappa$, and the existing fixed-residue Bettin–Chandee fallback, not an individual character estimate. Explicitly, the terms in the variance are

$$
 \ll_\epsilon N^{30\kappa+\epsilon}
       (Q^{-1}U^{23/8}+M^{3/20}U^{59/20}Q^{-23/20})
       +N^{2\kappa+\epsilon}U^{5/2}/Q+N^{\kappa+\epsilon}U^2/Q .
$$

These are precisely the nonzero terms of [R40, §3](weak-s-type-ii-medium-prime-growing-tags.md#3-a-uniform-centered-dispersion-budget). The proof cited there tiles at lengths $O(Q|r|)$ with $r=(n_1/g-n_2/g)/q$, so only $g|r|\ll U/Q$ occurs; its tile count and the complete/incomplete cross estimates require $Q\ll U$, not $Q/U\le N^{-\epsilon}$. Briefly, the analytic partial summations use $H_f M/Q=N^\kappa$ and $N H_f/(UQ)=O(N^\kappa)$; the phases and support sizes do not involve the assumed low-conductor transform. The smooth Poisson tails are negligible with this cutoff. After multiplying by $MQ$, the two trilinear exponents tend to $1.9375$ and $1.975$ before $30\kappa+\epsilon$; the other two have a fixed margin, and the $1/G$ part just proved gives $O(N^2 L^{10}/G)$. The remaining part costs $O(N^2 L^{10}Q/U)$. Taking small fixed $\epsilon$ and then square roots proves (2) (with spare logarithm and fixed $\delta$).

## 2. Transfer low tags in two directions

Use $S=\exp(C L/L_2)$, $z=N^{.001}$, and the previously published broad tag band $[S,z]$. Put

$$
   S_0=L^{10000},\qquad B=L^{250},\qquad \eta=L^{-10}.
$$

For all sufficiently large $N$, $B<S_0<S<z$. The new tags are the primes in $[S_0,S)$. In this section both variables originally have no broad tag. First handle those tuples with at least one new tag on $v$. Then, among the remaining tuples, handle those with at least one new tag on $u$.

In the first transfer, assign $v$ to its first occupied cell, using a partition into ordered multiplicative cells of ratio at most $1+\eta$. Within that cell replace occupancy by the sum of its individual prime divisors $s$. The cost is $O(NL(\eta+S_0^{-1})L_2)$ by pairs of distinct cell primes: each $v,d$ determines at most one $u$, the same-cell reciprocal sum is $O(\eta+S_0^{-1})$ by counting integers, and the full reciprocal sum is $O(L_2)$. These facts are unchanged in the second transfer with $u,v$ interchanged. The assigned earlier-cell exclusion always stays on the short variable after a tag is moved; the tag is not itself in a forbidden earlier cell. The original broad exclusions also persist because the new and broad bands are disjoint. There are at most $O(L)$ tag representations of any integer of polynomial size.

First suppose $v=s\ell$. Discard those labeled tuples with $s\mid u$ so that $n=su$ will be squarefree on $\mu(u)$'s support. To bound the discarded weights, the *union* of pairs $u,v\ll X$ sharing a prime $\ge S_0$ has size $O(N/S_0)$. The number of possible $d$ is at most $\tau(N-uv)$. Moreover $\sum_{u,v}\tau(N-uv)^2\ll N L^{O(1)}$ by $t=uv$ and Cauchy with the second and fourth divisor moments; only $t<N$ occurs here. Thus the cost is $O(N L^{O(1)}S_0^{-1/2})$ even counting label multiplicity $O(L)$. More explicitly $\tau(t)\tau(N-t)^2$ gives logarithmic exponent at most 9 in that squared sum, and restoring $w$ and multiplicity costs at most $L^2$ outside its square root. Freeze $\ell\in J/T$ in place of $J/s$, where $T$ is the left endpoint of the cell. All changes have $v$ in $O(\eta X+1)$ integers at the two endpoints, so the total endpoint error before square completion is $O(L^2 X(\eta X+1))$, independent of the number of cells. The new dyadic variables are $m=\ell$, $n=su$, and $mn=uv$. The short coefficient has $w(\ell)/L$, oddness, no broad or earlier-cell tag, and the frozen interval, using $w(s\ell)=w(\ell)$. The long coefficient carries the true $\mu(u)$, no broad tag on $u$, oddness, $(s,u)=1$, and the hard $I$ interval, with the sum over $s$ in that cell. A normalizing factor $O(L)$ makes it $1$-bounded, and restoring this and the short normalization costs $O(L^2)$.

In the second transfer $v$ has no tag in the **full** band $[S_0,z]$. Write $v=a^2b$ uniquely with $b$ squarefree, and discard $a>B$ at cost $O(NL/B)$ by counting affected $v\le X$ and then $d$. For $a\le B<S_0$, the full exclusion on $v$ is that on $b$, and $w(v)=w(b)$. Assign $u$ to its first new-tag cell and use its labels as above. Write $u=s\ell$, replace $\mu(s\ell)$ by $-\mu(\ell)$, and discard the discrepancy $s^2\mid u$ at cost $O(NL/S_0)$ by unique $v$ for each $u,d$. Freeze $\ell\in I/T$ rather than $I/s$, with the same endpoint count. Use

$$
                    m=a^2\ell,\qquad n=sb,\qquad mn=uv.
$$

The short coefficient has $-\mu(\ell)$, oddness and the original broad and earlier-cell exclusions on $\ell$. The long coefficient sums the exact $w(b)$, hard $b$-interval $J/a^2$, squarefree and odd masks, and full-band exclusion, over $s$ in the cell. It is odd squarefree since $s$ is forbidden on $b$. Restoring normalization to make the long coefficient $1$-bounded costs $O(L^2)$. The square part is placed in the short variable; there is no change of residue $N$ or reciprocal-square multiplier.

In both transfers the exact squarefree gate is truncated at $c\le B$ **after** the deterministic comparisons. The enlarged $u,v$ support preserves the fixed box margins. Missing square divisors affect $O(N/B)$ values of $N-uv$. Each value costs at most the tag multiplicity times $w(v)$ times $\tau(uv)\tau(N-uv)^2$, using the number of factorizations, the modulus divisors, and the omitted square sum. Hölder with exponents $4,4,2$ and the fourth/eighth divisor moments gives an error $O(N L^{70}B^{-1/2})$, since their powers after the quarter factors sum to $67.5$, and numerator weight/multiplicity costs $L^2$. In particular all errors in both transfers are $O(NL^{-7})$.

## 3. Check the low-conductor transform and reassemble

For the long coefficient of the first transfer, the unnormalized transform at any nonprincipal character of modulus polynomial in $N$ is

$$
 \left(\sum_{s\ {\rm in\ cell}}\chi(s)\right)
       \sum_{\substack{u\in I\\u\ {\rm odd,\ no\ broad\ tag}}}\mu(u)\chi(u)
 +\sum_{s\ {\rm in\ cell}}\chi(s)^2
       \sum_{\substack{b'\in I/s\\(b',2s)=1,\ b'\ {\rm no\ broad\ tag}}}
                                     \mu(b')\chi(b').
$$

This is the exact removal of $s\mid u$, since $\mu(s b')=-\mu(b')$ on $(s,b')=1$; $s$ is not in the broad tag band. For the second transfer the transform factors into the cell prime sum and the $w(b)$-weighted squarefree transform of $b$ with the full-band exclusion.

Both transforms are $O(\sqrt U N^{.03})$ on the actual dyadic $U$. Here is why the low end $S_0$ does not harm the needed character estimate. Use hard Perron on the fixed line $\Re s'=1/2+.01$ at height $N^4$, not the moving line in R42. The [shifted prime bound, R42 §1](weak-s-type-ii-medium-prime-opposite-tags.md#1-the-long-transform-with-the-exact-wide-euler-exclusion) bounds the excluded prime Euler linear terms under global GRH by $L^{O(1)} S_0^{-.01}=o(1)$, with at most a fixed $L^5$ factor by its $O(\sqrt Y L^3)$ bound and partial summation. Higher terms converge absolutely. The same argument handles the marked medium-prime sum with lower endpoint $N^{.024}$. The $L(s',\chi)^{\pm1}$ factors are $\exp(O(L/L_2))$ by [R40 §1](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums), which also permits imprimitive finite corrections. Any single $2s$ mask is bounded on this line as well. For the Möbius sequence use its reciprocal $L$-series with inverse excluded Euler factors, and for the squarefree $w$ sequence use exactly the R42 marked Euler series, now with the full exclusion. The fixed shift and Perron at an endpoint scale $Y\le N$ give $O(\sqrt Y N^{.02})$ for either interval transform for large $N$. Each cell prime sum is $O(\sqrt T L^2)$ by GRH with endpoint subtraction (no short-interval distribution assumption). In the first formula the second term is bounded by $O(T)$ tags times the estimate at scale $X/T$; in the second transform the other scale is $X/a^2$. Since $U\asymp XT$ or $XT/a^2$ respectively, and all remaining logarithms fit inside $N^{.01}$, this proves the bound required for (3). No estimate for the masked short coefficient is used.

At fixed square completion variable $c\le B$, split $\mu(d)\ne0$ by $g=(d,c)$ and take $q=[d,c^2]$ injectively. Here $q$ is odd, $q\in[X/5,O(XB^2)]$, and the congruence is $mn\equiv N\bmod q$. Both transfers have $MU\asymp N$, $M,U,Q=N^{1/2+o(1)}$, and $Q/U\ll B^4/S_0$. Apply (2) on all actual dyads. Signed principal sums, without any pointwise principal estimate, are $O(Ne^{-c_1\sqrt L})$ per piece by [R43 §1](weak-s-type-ii-doubly-untagged-signed-principal.md#1-signed-summation-of-the-principal-density), keeping the actual $\mu(d)$, since the short and long coefficients are independent of $d$. The total reassembly count is at most $O(L^{762})$: $O(L^{11})$ cells, $O(L)$ dyads, and crudely $B^3$ for $a,c,g$. The coefficient normalization contributes $O(L^2)$. Consequently the main term of (2) reassembles at most as $O(N L^{770}(B^4/S_0)^{1/2})=O(NL^{-7})$; the fixed power savings and the exponential principal bounds absorb all overhead. This proves $O(NL^{-7})$ on each new-tag family in original weight units.

## 4. Bound the remaining unsigned weight and combine

The remaining doubly untagged integers avoid the full band $[S_0,z]$ in both variables. Its one-dimensional sieve density is $\asymp\log S_0/\log z\ll L_2/L$. The [elementary R41 upper sieve, §3](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich) still applies at this lower $S_0$: each geometric log band has reciprocal mass at most 1 for large $N$, uniformly by Mertens, and the sum of the relative factorial errors over all bands is bounded independently of their number. The support remains $r\le z^{30}=N^{.03}$. For fixed odd $d$ ignore the squarefree gates and use the product of the two nonnegative upper sieves. At $r_1\mid u,r_2\mid v$, there is no solution unless $(r_1r_2,d)=1$. Otherwise the same rectangular Weil count as in [R42 §3](weak-s-type-ii-medium-prime-opposite-tags.md#3-actual-double-untagged-unsigned-scale) has area main $|I||J|\varphi(d)/(4r_1 r_2d^2)$ and error $O_\epsilon(d^{1/2+\epsilon})$; hard subintervals have the identical bound with their lengths. The product density is $O((L_2/L)^2)$ uniformly in $d$, since omitting the tag primes dividing $d$ changes each log product by $O(L/S_0)=o(1)$. Summing $d,r_1,r_2$ gives at most $O(N(L_2/L)^2+N^{.81+\epsilon})$ tuples, since the product upper weights have modulus at most 1. Multiplying by $w(v)\le L$ gives $O(N L_2^2/L)$ even with absolute values.

Finally the exact earlier broad-tag families (v broad tagged, or v not broadly tagged and u broadly tagged) have signed $O_A(NL^{-A})$ under global GRH by R41 and R42–R43, with exact disjoint masks. The two new-tag families above and the last raw bound therefore prove (1) on the full fixed box. All transfer identities preserved $N/2<uv<9N/16$, $(N-uv)/d>X$ if integral, and the unit masks. No claim is made about other boxes or the complete central Type II term.
