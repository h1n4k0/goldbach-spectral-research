# Transfer from the opposite variable on the true untagged Type II remainder

Use the exact $N=2^j$ balanced box $I,J,D$, the signed summand $W(u,v,d)=\mu(u)\mu(d)\mu^2(N-uv)w(v)$, and the oddness and congruence conditions of [first-cell transfer](weak-s-type-ii-medium-prime-first-cell.md). Set $X=\sqrt N,\ L=\log N,\ L_2=\log L,\ L_3=\log L_2$. As there, a broad tag of $v$ lies in $\mathcal P=[S,N^{.001}]\cap\mathbb P$, with $S=\exp(C L/L_2)$ and $C$ a sufficiently large fixed constant. Define a narrower band for $u$ by

$$
 H_*=\frac{L_3}{\log^2(2L_3)},\qquad z_*=S^{H_*},
 \qquad \mathcal P_*=[S,z_*]\cap\mathbb P \subset\mathcal P
$$

for all sufficiently large $N$. Under global Dirichlet GRH the exact signed sum over $v$ with no broad tag and $u$ with at least one narrow tag is $O_A(NL^{-A})$ for every fixed $A>0$, uniformly on arbitrary subintervals of $I,J,D$. This also holds with optional squarefree/nonsquarefree $v$ and/or the previous exclusion of prime divisors of $v$ in $[N^{.002},2N^{.002}]$.

Unconditionally, the remaining absolute mass on the full box, with neither a broad tag of $v$ nor a narrow tag of $u$, is

$$
             \asymp_C \frac{NL}{L_2 H_*}.
$$

The lower bound already holds on nonsquarefree $v$ with the old fixed-tag exclusion. Thus this opposite transfer controls a genuinely disjoint portion of the previously unsigned-order-$NL/L_2$ remainder; its unsigned scale is itself $\asymp_C NL/L_2$. Neither theorem gives $o(N)$ for the signed doubly untagged box, and none asserts weak S.

## 1. The long transform with the exact wide Euler exclusion

Uniformly for possibly imprimitive nonprincipal $\chi\bmod q$, $q\le N^{C_1}$ with $C_1$ fixed, and $|t|\le N^4$, GRH gives

$$
   \sum_{n\le Y}\Lambda(n)\chi(n)n^{-it}\ll_{C_1}\sqrt{Y}\,L^3,\qquad 2\le Y\le N.
$$

To see this with the needed height uniformity, use the local-zero logarithmic derivative formula (for example [Koukoulopoulos, The Distribution of Prime Numbers, Chapter 11](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf)). It follows by subtracting the Hadamard logarithmic derivative at $2+i\tau$ from that at $\sigma+i\tau$: zeros farther than 1 from $\tau$ contribute $O(\log(q(|\tau|+2)))$ using the unit-band zero count and a squared-denominator sum; for the remaining $O(L)$ zeros GRH gives the denominator $\gg 1/L$ for $\sigma\ge1/2+1/L$. The logarithmic derivative at $2+i\tau$ is $O(1)$, and the gamma and imprimitive factor terms are $O(L)$. Hence $|(L'/L)(\sigma+i\tau,\chi)|\ll L^2$ throughout $1/2+1/L\le\sigma\le2,\ |\tau|\le 2N^4+2$. Take half-integer endpoints and truncate Perron for $-L'/L(s+it,\chi)$ at height $N^4$ from $\Re s=2$, then shift to $\Re s=1/2+1/L$. There is no pole since $\chi$ is nonprincipal, the horizontal and truncation errors are $O(Y^2 L^{O(1)}/N^4)$, and the shifted segment loses at most another factor $L$. The prime-only version (weighted by $\log p$) follows by removal of prime powers at cost $O(\sqrt Y L^2)$.

Let $\mathcal E$ be the union of the broad tag band and, if desired, the old fixed band. Uniformly on $1/2+1/L_2\le\sigma\le 2,\ |t|\le N^4$, the product

$$
      \prod_{p\in\mathcal E}(1+\chi(p)p^{-\sigma-it})^{-1}
$$

has modulus $O(1)$. Indeed use the twisted bound above and Abel in $p^{-\sigma}$ (and $1/\log p$ when unweighted) on each of the at most two prime intervals. The linear sum $\sum_{p\in\mathcal E}\chi(p)p^{-\sigma-it}$ is bounded by $L^{O(1)}S^{-(\sigma-1/2)}=o(1)$. The higher terms in the Euler logarithm are bounded by $O(\sum_{n\ge S}n^{-2\sigma})=o(1)$. This is not an absolute bound for the magnitude of the linear prime terms.

For the squarefree, odd, excluded-prime sequence weighted by the genuine $w$, its Dirichlet series at $s=\sigma+it$ is, first for $\sigma>1$,

$$
 \frac{L(s,\chi)}{L(2s,\chi^2)}
   (1+\chi(2)2^{-s})^{-1}
   \prod_{p\in\mathcal E}(1+\chi(p)p^{-s})^{-1}
   \sum_{N^{.024}<p\le N^{.2499}}\log p\,
                  \frac{\chi(p)p^{-s}}{1+\chi(p)p^{-s}} .
$$

This follows from the squarefree Euler product by marking one included prime, and $\mathcal E$ is disjoint from the marked interval. The finite marked sum is $O(1)$ on the contour: its linear term is bounded by the same twisted partial summation with lower endpoint $N^{.024}$, and corrections by $O(\sum_{n\ge N^{.024}}(\log n)n^{-2\sigma})=o(1)$. The $2$-factor is bounded and the reciprocal at $2s$ bounded by $\zeta(2\sigma)=O(L_2)$, even for $\chi^2$ principal. Finally the proof of [(2) in moving tags](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-möbius-sums) bounds the absolute value of $\log|L(s,\chi)|$ by $O(L/L_2)$, not just its negative part. All Euler factors are holomorphic in the shifted half-plane. Half-integer hard Perron at height $N^4$, shifting from 2 to $1/2+1/L_2$, therefore gives the required bound

$$
 \left|\sum_{\substack{\ell\in H,\ \ell\ \mathrm{odd}\\
                         (\ell,\prod_{p\in\mathcal E}p)=1}}
              \mu^2(\ell)w(\ell)\chi(\ell)\right|
                 \ll \sqrt Y\exp(O(L/L_2))
 \tag{1}
$$

on any hard interval $H$ at scale $Y\le N$. The starting truncation and horizontal sides cost $O(Y^2\exp(O(L/L_2))/N^4)$, with polynomial logarithms absorbed. The constant does not depend on the number of excluded primes or on $C$ when $C$ is above a fixed positive constant. The old fixed exclusion enters only if requested.

## 2. Transfer at fixed square part without changing the numerator

Set $B=e^{L_2^2}$. Write $v=a^2 b$ uniquely with $b$ squarefree and $a$ odd, with no need to require $(a,b)=1$. Discard $a>B$ at total absolute cost $O(NL/B)$: the number of such $v\le X$ is $O(X/B)$ and each $v,d$ determines at most one $u$. For $a\le B<S$, the excluded-prime conditions on $v$ and $b$ are identical, as are their medium weights $w(v)=w(b)$; requested squarefree/nonsquarefree restrictions on $v$ mean $a=1$ or $a>1$ exactly.

Set $K=\lceil L_2\log(2L_3)/L_3\rceil$. Expand the narrow occupancy indicator of $u$ through order $K$ by Bonferroni. The error, by unique $v$ for each $u,d$, is

$$
      O\left(NL\,\frac{\big(\sum_{s\in\mathcal P_*}s^{-1}\big)^{K+1}}{(K+1)!}\right)
           = O_A(NL^{-A}) .
$$

Here the reciprocal sum is $O(\log(2H_*))$, and the log of the factorial relative to its numerator grows like $L_2\log(2L_3)$. For each retained $h\le K$ write the selected primes as an ordered distinct tuple with coefficient $(-1)^{h-1}/h!$, $r=\prod_{i=1}^h s_i$, and $u=r\ell$. One has $S\le r\le z_*^K=N^{o(1)}$ (indeed $\log r/L\ll C/\log(2L_3)$); each integer of size $\le N^{O(1)}$ has $O_C(L_2)$ eligible primes, hence at most $\mathfrak C=\exp(O(K\log(2L_2)))=\exp(o(L_2^2))$ representations. Replace $\mu(r\ell)$ by $\mu(r)\mu(\ell)$, failing only if some selected $s_i^2\mid u$. This costs $O(NL\mathfrak C/S)$ by unique $v$ for each $u,d$, and $\mu(r)=(-1)^h$ is constant per retained order.

For each position put its prime into a multiplicative cell of ratio at most $1+\eta$, $\eta=e^{-L_2^2}$; let $r_0$ be the product of the left endpoints. Replace $\ell\in I/r$ by $\ell\in I/r_0$, costing $O(LX\mathfrak C(K\eta X+1))$ on actual affected $u$ near the two endpoints of $I$. The counting is over unique $v$ for each $u,d$, not over all cells. The exact $v=a^2 b\in J$ interval is untouched. Both errors are before the square completion of $N-uv$, which can now be truncated at square root divisor $c\le B$ as in first-cell transfer, at cost $O(NL^{O(1)}\mathfrak C B^{-1/2})$ by divisor moments. These errors are all below every inverse-log scale. Counting $a,c$, dyads, gcd groups and all cell choices contributes $\exp(O(KL_2^2))$, whose log is $o(L/L_2)$ and $o(\sqrt L)$.

In a fixed block tuple use

$$
                    m=a^2\ell,\qquad n=r b.
$$

This retains $mn=uv$ and the exact fixed numerator $N$ in every modulus, with no inverse-square multiplier. The short coefficient is $\mu(\ell)$ on odd integers $\ell\in I/r_0$, placed on $m=a^2\ell$; this is $1$-bounded. The long coefficient is the sum of $w(b)$ over representations $n=rb$ with the prescribed distinct primes in the cells and $b$ in the fixed interval $J/a^2$, odd squarefree, and with the exact Euler exclusions. Normalize by $L\mathfrak C$ to be $1$-bounded. Because $b$ has no broad tag and the narrow tags are in the broad band, $n$ is squarefree with no coprimality correction. The dyadic lengths are

$$
               M\asymp X a^2/r_0,\qquad U\asymp Xr_0/a^2,
                  \qquad MU\asymp N .
$$

After taking $\chi(n)=\chi(r)\chi(b)$, (1) bounds the $b$-transform. Distinctness of the tag primes can be imposed by inclusion–exclusion over pairs of positions, just as in [moving tags, §3](weak-s-type-ii-medium-prime-growing-tags.md#3-a-uniform-centered-dispersion-budget): singleton groups get $\sqrt{T_i}O(L^2)$ by the nonprincipal prime sum at the $i$-th scale $T_i$; collision groups with $h'\ge 2$ get at most $O(\prod_{i\text{ in group}}\sqrt{T_i})$ trivially, as intersecting cells are at comparable scales. This gives $\sqrt{r_0}\exp(O(K^2+KL_2))$ for the tag factor, hence $|\sum_n\beta_n\chi(n)|\ll\sqrt U\exp(O(L/L_2))$ for every nonprincipal $\chi$. For the principal density use the short Möbius coefficient instead, with exact mask $(\ell,2q)=1$ when $(a,q)=1$, zero otherwise. The unconditional masked Mertens argument applies uniformly at scale $X/r_0\ge N^{.499}$ eventually. Combined with the trivial $O(U)$ long bound, the contribution on any dyad is $O(Ne^{-c\sqrt L})$, absorbing a logarithm from $\sum_{q\asymp Q}\varphi(q)^{-1}$.

For odd squarefree $c\le B$ complete the modulus $q=[d,c^2]$ on each fixed $(d,c)$ group as in [first-cell transfer, §2](weak-s-type-ii-medium-prime-first-cell.md#2-uniform-centered-dispersion-for-the-actual-transferred-term), and apply the same quantitative centered dispersion. Here $U\le O(N^{.501})$ for all large $N$, $Q\ll XB^2$ and $Q/U\ll B^4/S$. Nonzero terms retain fixed power margins while the exact $MU$-variance terms after Cauchy are $O(N^2(Q/U)\exp(O(L/L_2)))$. Choose $C$ above the fixed constants in the transform/variance as in first-cell transfer. This term saves $\exp(-cL/L_2)$ relative to $N^2$ and permits all external overhead. The principal-density bound also permits that overhead. This proves the claimed signed estimate with original $\mu(d)$, odd conditions, and varying hard endpoints.

## 3. Actual double-untagged unsigned scale

Apply the elementary sieve sandwich of [first-cell transfer, §3](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich) to both variables, using their respective tag intervals. One may treat the geometric log bands of $u$ and $v$ as separate families and apply its product-minus-one-error formula over the combined list. The sandwich weights, $\lambda^\pm_{r_1,r_2}$, are supported on squarefree $r_1\le z_*^{30}\le N^{.03}$, $r_2\le (N^{.001})^{30}=N^{.03}$; $|\lambda^\pm_{r_1,r_2}|\ll1+\log(2L_2)$. Under an independent multiplicative two-variable model they give upper and lower main terms within factors 2 and $1/2$ of the product local density. In fact there are at most two geometric bands at each depth, so the combined relative factorial-error sum in that proof remains $<1/10$.

For the upper bound ignore squarefreeness and take fixed odd $d$. If $(r_1r_2,d)>1$ there are no tuples with $r_1\mid u,\ r_2\mid v$. Otherwise use rectangular Weil (as in first-cell transfer) on $u=r_1u_1,\ v=r_2v_1$ with the inherited parity:

$$
  \#\{(u,v)\}=\frac{|I||J|}{4r_1r_2}\frac{\varphi(d)}{d^2}
                                  + O_\epsilon(d^{1/2+\epsilon}).
$$

The two local factors separately are $1/s$ for $s\nmid d$ and 0 for $s\mid d$. At most $O(L_2)$ tag primes divide $d$, so the product density is $\asymp_C 1/(L_2 H_*)$ by the two prime products, uniformly in $d$. Summing over $d,r_1,r_2$ costs $O_\epsilon(N^{.81+\epsilon}(1+\log(2L_2)))$ in error. Multiply by $w(v)\le L$ to obtain the upper bound.

For the lower bound force $9p\mid v$, $p\in[N^{.10},N^{.11}]$ labeled, with actual squarefree $u,d,N-uv$, as in [first-cell transfer, §4](weak-s-type-ii-medium-prime-first-cell.md#4-matching-lower-bound-on-occupied-untagged-tuples). Keep its notation $X_{d,p}$ for the positive model before sifting. Now with $r_1\mid u,\ r_2\mid v$ perform the two square completions at $B_0=S^{1/10}$, using $u=[r_1,A^2]u_1,\ v=9pr_2 v_1$ when completing $A^2\mid u$ and $b_0^2\mid N-uv$. The modulus is $q=[d,b_0^2]$ with the same exact parity and coprimality as before. The main term is

$$
      \frac{|I||J|}{36p r_2 [r_1,A^2]}\frac{\varphi(q)}{q^2},
$$

and the sum of Weil errors over both sieve indices is $O_\epsilon(N^{.92+\epsilon}B_0^{3+2\epsilon}(1+\log(2L_2)))$. The tails of the two square expansions cost $N B_0^{-1}\exp(O(L/L_2))$ as before: the two sieve divisibility multiplicities are at most $\tau(u)\tau(v)$. Choose $C$ large enough for all these absolute errors. In extending only the model to all $A,b_0$, the half-power Rankin bound now loses extra factors $1+O(s^{-1/2})$ at $s\mid r_1$ (from $[r_1,A^2]$), as well as those at $s\mid d$; their product is $\exp(O(\sqrt L))$. Thus the summed extension error is $O(NL^{O(1)}B_0^{-1/2}\exp(O(\sqrt L)))$, using the reciprocal weights $1/(pr_1r_2d)$. All errors are $o(N/(L_2H_*))$.

In this model put $F_s=1-2/s^2+1/s^3$ for a tag prime $s\nmid d$; tag primes are automatically coprime to $6p$. The four local factors relative to $X_{d,p}$, in cases of $s$ dividing neither $r_i$, just $r_1$, just $r_2$, or both, are respectively

$$
                 1,\qquad
        \frac{1-1/s}{sF_s},\qquad
        \frac{1-1/s^2}{sF_s},\qquad
        \frac{1-1/s}{s^2F_s}.
$$

Indeed once $s$ divides either variable, it cannot divide the square modulus $b_0$. If forced on the $u$ leg, imposing $s^2\mid u$ costs only $1/s$, not $1/s^2$, after the base $s\mid u$ is imposed; this is exactly the lcm in the main coefficient. If $s\mid d$, any forced choice has factor zero. Hence the true model differs from the product of its two separate $g_d^u,g_d^v$ models only for shared primes of $r_1,r_2$, by relative factor $F_s/(1-1/s^2)=1+O(s^{-2})$ each. Both indices are polynomial-sized, so total relative error is $O(L_2/S^2)$. Summed against the sieve weights it costs $o(N/(L_2H_*))$, using the two harmonic sums up to $N^{.03}$ and $0\le g_d^u(s),g_d^v(s)\le s^{-1}+2s^{-3}$. For the independent product model the local density is uniformly $\asymp_C 1/(L_2H_*)$ since the $u$ factor differs from $1/s$ by $O(s^{-2})$, the $v$ factor by $O(s^{-3})$, and dividing primes of $d$ remove at most $O(L_2/S)$ in logarithm. The same positive-model average $\sum_{d,p}X_{d,p}\gg N$ and bounded number of labels $p\mid v$ prove $\gg_C N/(L_2H_*)$ true occupied tuples. With $w(v)\ge.10L$, this is the asserted lower bound. The old fixed-tag exclusion deletes only $O(N/L)=o(N/(L_2H_*))$ tuples; $9\mid v$ ensures nonsquarefreeness as claimed.
