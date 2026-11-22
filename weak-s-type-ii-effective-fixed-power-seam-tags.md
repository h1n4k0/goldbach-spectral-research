# Effective signed fixed-power tags in the genuine central seam

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and $V=N^{.2499}$. Use the true summand

$$
 \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk),\qquad
 b_{\rm II}(v)=\sum_{r\mid v,\ r>V}\Lambda(r),
$$

on $uv+dk=N,\ N/2<uv\le y,\ k>t,\ (uv,N)=1$. Uniformly for $t\ge N^{.49999}$, $N/2\le y\le9N/16$, impose $d\ge X$, $u,v\le N^{.50002}$, and optional hard subintervals of the three variables. Take the fixed-power tag band

$$
                 \mathcal P=[N^{.00004},N^{.001}]\cap\mathbb P .
$$

For every fixed $A>0$, the actual signed sum on each of the following disjoint selectors is $O_A(NL^{-A})$, unconditionally with effective constants:
* $v$ has a prime divisor in $\mathcal P$;
* $v$ has none and $u$ has a prime divisor in $\mathcal P$.

There is no additional upper $d$-cap; the true $k>t$ gives $d<N^{.50001}/2$. This is a marked contribution in the jointly near-square-root seam left by [R48](weak-s-type-ii-unconditional-moving-slab.md) and [R49](weak-s-type-ii-beyond-near-balance.md), including $d$ polynomially above $X$. No bound on the full unsigned or signed untagged complement is inferred. Section 5 gives a different, exactly specified local tag band and box in this same seam where the true doubly untagged absolute mass is $\asymp NL$, despite the corresponding signed tagged estimate. This is a barrier to closing that local split by absolute values, not a lower bound for its signed remainder. Nothing here proves weak S.

The new analytic ingredient is to remove the whole polylogarithmic-conductor projection **in the signed sum**, then bound the nonzero frequencies introduced by doing so. This removes the need for any individual low-conductor character transform, Siegel–Walfisz, or GRH; fixed-power exclusions therefore cause no Euler-product difficulty.

## 1. Remove the low conductors with the actual modulus signs

Take $P=\lceil A\rceil+5,\ F_0=L^{10000P}$, and square-completion cutoff $B=L^{400P}$. On a hard rectangle keep the signed squarefree completion $c\le B$ for $c^2\mid N-uv$. Since $(uv,N)=1$, both $d,c$ and $q=[d,c^2]$ are coprime to $N$. On the support of $\mu(c)\mu(d)$, fix $c,g=(c,d)$, write $d=ge,\ q=c^2e$, and if $f=\operatorname{cond}(\chi)$ write $f=f_0f_1$ with $f_0\mid c^2,\ f_1\mid e$, and $e=f_1h$. Here $(e,c)=1$. This covers the principal by $f=1$. For fixed $c,g,f,\psi$, where $\psi$ is the primitive inducing character, the completed modulus has

$$
 \varphi(q)=\varphi(c^2)\varphi(f_1)\varphi(h),
 \qquad \mu(d)=\mu(g)\mu(f_1)\mu(h).
$$

After reversing two arbitrary bounded coefficient sums on exact products $mn=uv$ and lengths $M,U$ with $MU\asymp N$, a remaining $h$-sum is $\sum\mu(h)/\varphi(h)$ on a hard interval with a finite mask $(h,2cNf_1mn)=1$; if any fixed prime of $cf_1$ makes $mn$ a nonunit, the term is already zero. The factor $\overline{\chi(N)}=\overline{\psi(N)}$ is independent of $h$ on the actual $q$'s. The $d$-interval and any completed modulus dyad give a single hard interval in $h$ at scale $d/(g f_1)\gg N^{.5-o(1)}$. Thus the [R43 unconditional masked harmonic reversal](weak-s-type-ii-doubly-untagged-signed-principal.md#1-signed-summation-of-the-principal-density) gives $O(Ne^{-c_1\sqrt L}/(\varphi(c^2)\varphi(f_1)))$ per inducing character. Sum $f\le F_0$, counting at most $\varphi(f_0)\varphi(f_1)$ pairs for given conductors and $\sum_{f_0\mid c^2}\varphi(f_0)=c^2$. The resulting factors are polynomial logarithms. This estimate uses only the effective ordinary zeta zero-free region, since the long harmonic sum is untwisted; no estimate for the individual transform on $f\le F_0$ is required. The exact $\mu(d)$ cannot be replaced by arbitrary signs in this step.

## 2. A high-only centered variance

For normalized coefficients $\alpha_m,\beta_n$ of lengths $M,U$, let $\beta$ be supported on squarefree odd $n>1$ with $(n,N)=1$. Assume $MU\asymp N$, $Q/U=o(1)$, $Q\ge X/O(1)$, $Q\le N^{.50001+o(1)}$, and $U\le N^{.50102+o(1)}$. On unit residues $\lambda\bmod q$ define

$$
  B_q(\lambda)=\sum_{n\equiv\lambda\bmod q}\beta_n,\qquad
  C_q(\lambda)=\frac1{\varphi(q)}
     \sum_{\substack{\chi\bmod q\\\operatorname{cond}\chi\le F_0}}
                    \overline{\chi(\lambda)}\,\widehat\beta(\chi),
      \quad \widehat\beta(\chi)=\sum_n\beta_n\chi(n).
$$

Thus $B_q-C_q$ is the full high-conductor projection, not only principal subtraction. Actual $(q,N)=1$ moduli contribute $\sum_{m:(m,q)=1}\alpha_m(B_q-C_q)(N\bar m)$. Bound the sum of absolute values over $q$ by Cauchy as in [R45 §1](weak-s-type-ii-balanced-polylog-tags.md#1-a-centered-dispersion-bound-with-only-logarithmic-loss-in-the-diagonal-terms). The squared factor is $MQ$; the nonnegative variance may be enlarged to all $q\asymp Q$ and all smoothed $m\equiv N\bar\lambda\bmod q$, $\lambda$ a unit, even for $q$ not prime to $N$. This enlargement does not assert an original congruence at nonunit $N$.

In its exact Poisson zero mode only conductors $f>F_0$ remain. The $(n,h)=1$ de-masking with $q=fh$ and primitive large sieve of [R48 §3](weak-s-type-ii-unconditional-moving-slab.md#3-rebalance-the-averaged-energy-the-conductor-split-is-polylogarithmic) bound the weighted character energy by $O(U(1+U/(QF_0)))$ (the joint squarefree divisor sum weighted by $1/\varphi([r,s])$ is absolutely convergent). Multiplying by the Poisson factor $M$ and by $MQ$ gives the squared error $O(N^2(Q/U+F_0^{-1}))$. There is no low-conductor energy term.

For the nonzero frequencies of $|B_q|^2$ use the exact centered neighboring-tile Bettin–Chandee calculations of R45/R47, using that part only, with $G=N^\kappa$, $H_f=(Q/M)N^\kappa$, $\kappa=10^{-5}$. The large-gcd removal and restoration of its zero part cost $O(MU L^{10}(1+U/(GQ)))$ in the variance, by the divisor moments at nonzero $N-mn_1$. Here $mn_1=N$ is impossible since $n_1>1,(n_1,N)=1$. The two trilinear squared exponents after $MQ$ are $1+(15/8)p$, $23/20+(9/5)p-(3/20)z_1$, before $30\kappa+\epsilon+o(1)$, with $p=\log U/L\le .50102+o(1)$, $z_1=\log Q/L\ge .5+o(1)$. Both retain fixed margin. These statements use no earlier conditional character estimate. It remains to justify the two genuinely different nonzero cross terms from this projection.

**Mixed term $B_q\overline{C_q}$.** Write $e(x)=e^{2\pi i x}$. Opening $\widehat\beta$ at a fixed nonzero frequency $j$ yields, apart from the smooth weights and the factor $M$, sums of

$$
 \sum_{\substack{q\asymp Q\\ f\mid q,\ (q,n_1n_2)=1}}
     \frac{1}{q\varphi(q)}
       e(Nj\overline{n_1}/q)
$$

with outer coefficients $\beta_{n_1}\overline{\beta_{n_2}}\psi(n_1)\overline{\psi(n_2)}$ for primitive $\psi\bmod f,\ f\le F_0$. Indeed the inducing factors on both $n_i$ are independent of $q$ after their exact unit masks. If $(f,n_1n_2)>1$ there is no term. By reciprocity the phase is $e(-Nj\bar q/n_1)e(Nj/(q n_1))$. Pull out $Q^{-2}$ with smooth weight, and handle $q/\varphi(q)=\sum_{r\mid q}\mu^2(r)/\varphi(r)$. Writing $q=fk$, the condition $r\mid q$ (squarefree $r$) is equivalently $r/(r,f)\mid k$. Drop incompatible primes and impose the residual $(k,n_2)=1$ by divisor inclusion–exclusion. On each surviving progression $q=b\ell$, $(b,n_1)=1$, $(\ell,n_1)=1$, the inverse phase is $e(-Nj\bar b\bar\ell/n_1)$; the length is $O(Q)\ll n_1$. Completing in $\ell\bmod n_1$ gives $O_\epsilon(U^{1/2}N^\epsilon(j,n_1)^{1/2})$ by the classical incomplete Weil bound, since $(N,n_1)=1$. The $q/\varphi(q)$ divisor sum costs $O(L)$ by $\sum_{r\ll Q}1/\varphi(r)\ll L$, and the $n_2$-mask costs a divisor factor absorbed in $N^\epsilon$. Smooth partial summation costs $O(N^\kappa)$, because $|j|M/Q,\ |Nj|/(UQ)\ll N^\kappa$ for $|j|\le H_f$. This is the same incomplete Kloosterman input as the principal cross in R45, here along the actual progressions $f\mid q$. Summing $\sum_{1\le |j|\le H_f}(j,n_1)^{1/2}\ll_\epsilon H_f N^\epsilon$, both $n_i$'s and at most $O(F_0^2)$ inducing characters bounds the full mixed term by

$$
                    O_\epsilon(F_0^2 N^{2\kappa+\epsilon} U^{5/2}/Q).
$$

This is a variance bound before the factor $MQ$.

**Term $|C_q|^2$.** After inversion of the unit variable, the complete inner sum is of the form

$$
              \sum_{a\bmod q}^{*}\omega(a)e(Nja/q),
$$

where $\omega$ is induced by a primitive character of conductor $\ell\mid\operatorname{lcm}(f_1,f_2)$, $\ell\le F_0^2$, including $\ell=1$. For any integer $z$ the absolute value of $\sum^*_{a\bmod q}\omega(a)e(za/q)$ is at most $\sqrt\ell\,\tau(q)(z,q)$. Indeed write $q=\ell r$ and $\omega(a)=\psi(a){\bf1}_{(a,r)=1}$; expand the extra mask by $b\mid r$. Terms with $(b,\ell)>1$ vanish. Set $a=bm$, with $m\bmod \ell(r/b)$, group by $m\bmod\ell$, and sum the other $r/b$ lifts. This vanishes unless $r/b\mid z$; otherwise it gives $r/b$ times a primitive Gauss sum of modulus $\ell$, bounded by $\sqrt\ell$. This proves the bound without a squarefree restriction on $q$. Use $\#\{\chi:\operatorname{cond}\chi\le F_0\}\ll F_0^2$, $|\widehat\beta|\ll U$, and $\sum_{q\asymp Q}(Nj,q)\ll Q\tau(Nj)$ by divisor expansion. Summing the frequencies and the $q^{-1}\varphi(q)^{-2}$ factors bounds this term by $O_\epsilon(F_0^5 N^{\kappa+\epsilon}U^2/Q)$. The fixed power gaps after $MQ$ in both new nonzero terms absorb their polynomial logarithms. Smooth Poisson tails are negligible, also with these low-projection factors, by a sufficiently high fixed Schwartz decay bound.

Combining these bounds, the sum of absolute high-projection discrepancies on the actual $q$'s is

$$
           O_A\bigl(N L^6\sqrt{Q/U}+N F_0^{-1/2}
                                      +N^{1-\delta}\bigr)
$$

for a fixed $\delta>0$ in these ranges. Any signed modulus weight of modulus at most one can be restored in this high part. The low part was handled with the exact signs in §1.

## 3. Two disjoint true tag transfers

Use the [R49 strict moving grid](weak-s-type-ii-beyond-near-balance.md#1-exact-reduction-of-strict-moving-cuts-and-square-completion) with $\eta=L^{-20P}$, and its boundary moment estimate, before any tags. The total changed $(d,uv)$ is $O(\eta NL+N^{.50001})$, and the weighted error is $O_A(NL^{-A-1})$. The frozen rectangles keep genuine factor and $N$-unit masks, $uv,N-uv\asymp N$, and the lower bound $\min(U_0,V_0)\gg N^{.49998}$ since the larger factor is $\le N^{.50002}$. The exact $d$-cap from $k>t$ is imposed first.

On each rectangle use the [R47 two first-cell transfers](weak-s-type-ii-general-even-moving-slab.md#5-transfers-coprimalities-and-total-cost), now with the displayed fixed-power band and relative cell ratio $1+\eta'$, $\eta'=L^{-200P}$. Each label $s$ is prime to $N$. First transfer from $v=s\ell$ to $m=\ell,\ n=su$, requiring $(s,u)=1$. The weights are the exact unit-masked $\mu(u)$ on the long coefficient, with the short earlier-cell exclusion and $b_{\rm II}(\ell)$; replacing $b_{\rm II}(v)$ differs only at $s^2\mid v$ because $s<V$. Second, on $v$ with no tag, use $v=a^2b$, $a\le B$, $b$ squarefree and both unit modulo $N$, and move the tag from $u=s\ell$ to $m=a^2\ell,\ n=sb$. Then $b$ has no tag, $b_{\rm II}(b)=b_{\rm II}(v)$ since $B^3<V$, and $n$ is squarefree. Use $-\mu(\ell)$ for $\mu(s\ell)$ with discrepancy only at $s^2\mid u$. Earlier-cell exclusions in both transfers sit entirely on the short coefficients. All products are exact, no factor $\mu(d)$ changes, and the mask $(n,N)=1$ always follows from the actual factor masks. Only the moduli of normalized coefficients, not long character transforms, are needed here.

Here are the full error bounds for these parameter choices. If $S_0=N^{.00004}$ is the lower tag end, actual same-cell multiple tags affect $O(N(\eta'+S_0^{-1})L_2)$ pairs, and shared or repeated tags affect $O(N/S_0)$ pairs, by reciprocal counting before the modulus sum. Freezing a divided interval at a tag cell left endpoint affects $O(\eta' N+\max(U_0,V_0))$ pairs per outer rectangle; this counts the affected endpoints only once across all cells. For each pair family of size $H$, Cauchy with $\sum_{u,v}\tau(N-uv)^2\ll NL^9$ and $O(L^2)$ weight/multiplicity gives $O(L^2\sqrt{H N L^9})$. Discarding $a>B$ costs $O(NL^6 B^{-1/2})$ per rectangle by the same moments. Square completion is after these comparisons and costs $O(NL^{70}B^{-1/2})$ per rectangle. These beat $NL^{-A}$ after the $O_A(L^{40P+2})$ outer rectangles.

The two long scales are $U\asymp sU_0$ or $sV_0/a^2$ at the cell scale. Consequently $U\ll N^{.50102}$, $Q/U\ll N^{-.00001}B^4$, and $MU\asymp N$. There are at most $O_A(L^{240P+3})$ outer rectangles and cells together, $B^3$ for the square variables and $(d,c)$ groups, $O(L)$ dyads of $q$, and $O(L^2)$ for normalization. The $NF_0^{-1/2}$ term and all fixed powers save beyond these losses. Apply §2 to the high part; for the whole removed projection apply §1 with actual $\mu(c)\mu(d)$. This proves both claimed signed tagged estimates.

## 4. A local polynomially super-square-root box

For a second application take $N=2^j$, $D=N^{.5000001}$, $t=N^{.49999}$, $y=9N/16$, and

$$
 I=[.740X,.745X],\qquad J=[.715X,.720X],\qquad D_0=[D,2D],\qquad
 \mathcal P_0=[N^{.0000003},N^{.0000006}]\cap\mathbb P .
$$

Every tuple in the box with odd factors and $d\mid N-uv$ retains the actual cuts: $N/2<uv<9N/16$ with fixed margins, and $k=(N-uv)/d\gg N^{.4999999}>t$. This box lies beyond every R48 stretched cap with fixed $\rho<1/4$, and outside the R49 wings because $u,v\asymp X<N^{.50002}$. The same two signed tagged estimates hold with this local band and box, also for their hard subintervals. To check the only changed exponent, the lower tag exponent .0000003 exceeds $d/\min(U_0,V_0)$'s exponent .0000001; hence $Q/U\ll N^{-.0000002}B^4$. The upper tag exponent only shrinks $U$. The lower tag endpoint is still a fixed power, so all comparisons in §3 keep their savings. This local application uses exactly the same selectors and the ordinary coprimality masks.

## 5. The real local doubly untagged mass

In §4's exact box the absolute sum of the **genuine signed summand** on both variables without tags in $\mathcal P_0$ is $\asymp NL$. The upper bound follows by ignoring gates other than the congruence and using the rectangular Weil count at fixed $d$ with main $\ll N/d$, error $O_\epsilon(d^{1/2+\epsilon})$, and weight at most $L$. For the lower bound force $9p\mid v$ with a labeled prime $p\in[N^{.24992},N^{.24994}]$. Thus $p>V$ contributes at least $.24992L$ to the actual $b_{\rm II}(v)$, not to an altered coefficient. Retain squarefree $u,d,N-uv$. Restrict $d$ to odd squarefree integers prime to $3p$, with $\varphi(d)/d$ bounded below, as in [R42 §3](weak-s-type-ii-medium-prime-opposite-tags.md#3-actual-double-untagged-unsigned-scale). Before omitting $p\mid d$ this is a positive-density subset of $[D,2D]$. The exclusion $p\mid d$ changes the reciprocal $p$-sum by $O(N^{-.24992})$.

Use even/odd Bonferroni of depths 4 and 5 for each tag-free condition, with a joint lower sieve equal to the product of upper weights minus the sum of the two individual upper-minus-lower errors times the other upper weight. This is precisely the product-minus-one-error construction of [R41 §3](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich), here with one band per variable. Each tag divisor $r_i$ is at most $N^{.000003}$, and $\sum_{s\in\mathcal P_0}1/s\to\log 2$. For the multiplicative one-variable densities below each mean is at most 1 eventually, the independent no-tag density is at least $e^{-2}$, and the relative error in each of the two Bonferroni differences is at most $e^2/5!$. Hence their joint lower sieve gives a fixed positive multiple of the independent product density.

Complete $a^2\mid u$ and $b^2\mid N-uv$ at $B_0=N^{.000001}$ with signed Möbius weights, keeping parity. For $r_1\mid u,r_2\mid v$, put $q=[d,b^2]$ and use $u=[r_1,a^2]u_1,\ v=9p r_2 v_1$. The exact unit constraint is $([r_1,a^2]9p r_2,q)=1$, otherwise the congruence with $N=2^j$ is impossible. For odd $u_1,v_1$, the rectangular Weil count of R42 gives main

$$
                   \frac{|I||J|}{36p r_2 [r_1,a^2]}
                                 \frac{\varphi(q)}{q^2},
$$

and error $O_\epsilon(q^{1/2+\epsilon})$. All side lengths are $O(q)$. Summation over $d,p,r_1,r_2,a,b$ costs a total Weil error

$$
  O_\epsilon\!\bigl(N^{.5000001+.24994+.000006+.000003+.25000005+\epsilon}\bigr)
       =O_\epsilon(N^{.99994915+\epsilon})=o(N).
$$

Here $.000003$ includes both square variables and the $B_0$ factor from $q^{1/2}$; $\epsilon$ can absorb the accompanying $q^\epsilon$ loss. The raw omitted-square errors are $O((N/B_0)\exp(O(L/L_2)))=o(N)$, by counting $u,v$ or $N-uv$ with the omitted square and using divisor bounds for representations, modulus choices and sieve multiplicities. The actual lower count therefore keeps both squarefree gates.

Extend only the model $a,b$ sums to infinity; half-power Rankin as in R42 bounds the per-$(d,p,r_1,r_2)$ error by $O((N/(d p r_1r_2)) B_0^{-1/2}\exp(O(\sqrt L)))$, using the absolute local factors at primes of $d r_1$. Their sum is $o(N)$ since the remaining reciprocal sums cost at most powers of $L$. The common positive model coefficient before sifting is $\gg N/(dp)(\varphi(d)/d)^2$, exactly as in R42's $9p\mid v$ calculation. At a tag prime $s\nmid d$ its base squarefree factor is $F_s=1-2/s^2+1/s^3$. Relative factors for forcing the tag to divide $u$, $v$, or both, are

$$
      \frac{1-1/s}{sF_s},\qquad
      \frac{1-1/s^2}{sF_s},\qquad
      \frac{1-1/s}{s^2 F_s},
$$

respectively. These follow because any forced tag prohibits it in $b$, and if it is forced on $u$, the optional $a^2$ adds only one further factor $1/s$ after the base divisibility. If $s\mid d$, any forced tag factor is zero. Thus the two-variable model differs from the product of its two separate tag densities only by relative $1+O(s^{-2})$ at a shared prime, with total error $O(L/S_0^2)$, $S_0=N^{.0000003}$. Summing this error against the bounded sieve weights and the harmonic factors gives $o(N)$. The one-variable products are bounded below by positive constants: the tag harmonic sum is bounded and removing tags dividing $d$ compounds no adverse factor. The joint lower sieve therefore gives $\gg N$ genuine labeled tuples, since $\sum_{d\ {\rm good}}1/d\gg1$ and $\sum_{p}1/p\asymp1$ on the fixed exponent band. At most $O(1)$ such primes divide any $v$.

All these tuples have $\mu(u)\mu(d)\mu^2(N-uv)\ne0$, $|\mu(u)\mu(d)|=1$, and true weight $b_{\rm II}(v)\gg L$. This proves the claimed lower bound on the actual untagged absolute mass. No assertion about how the signs divide this mass is made. In particular it does not extend to a different, broader tag band or to the signed untagged sum.
