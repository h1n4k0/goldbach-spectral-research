# Signed composite-divisor transport in the doubly untagged Type II seam

Put $X=\sqrt N$, $L=\log N$, $V=N^{.2499}$, $Z=N^{.00004}$, and $H=N^{.000035}$, for even $N$. Keep the exact [effective fixed-power seam](weak-s-type-ii-effective-fixed-power-seam-tags.md): the statistic has summand

$$
  \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk),\qquad
  b_{\rm II}(v)=\sum_{r\mid v,\ r>V}\Lambda(r)
$$

on $uv+dk=N$, $N/2<uv\le y\le9N/16$, $k>t\ge N^{.49999}$, $(uv,N)=1$, $d\ge X$, $u,v\le N^{.50002}$, with optional hard subintervals for $u,v,d$. Require **neither** variable to have a prime factor in the old band $[Z,N^{.001}]$. Write

$$
 R(w)=\prod_{\substack{p\mid w\\p<Z}}p .
$$

This includes every prime below the old band, not only primes in a narrower selected range.

**Theorem.** For every fixed $A>0$, the signed sum is $O_A(NL^{-A})$ unconditionally, with effective constants, on each of the two disjoint selectors

$$
                  R(v)\ge H,\qquad
                  R(v)<H\text{ and }R(u)\ge H .
$$

The estimate is uniform in the above hard intervals and slanted cuts, with no upper cap on $d$ except its actual consequence $d<N^{.50001}/2$. In both cases a canonical, possibly many-prime divisor is transported. A single eligible prime need not be large enough to rebalance the congruence, even where the earlier variance argument needs the ratio $Q/U$ to decrease. Together with the earlier single-prime estimate, this leaves the signed remainder $R(u),R(v)<H$ and no old-band prime. This theorem does not bound that residual or prove weak S.

## 1. Greedy divisors and exact separation of order

For a fixed allowed prime set $\mathcal Q\subseteq\{p:p<Z\}$ and threshold $H'>1$, select the smallest initial segment of the increasing list of allowed prime divisors of a squarefree integer $z$ whose product is at least $H'$. If it exists, write $z=\gamma\ell$, where $\gamma$ is that product. Equivalently $\gamma$ is a squarefree product of allowed primes,

$$
  \gamma/p_{\max}(\gamma)<H'\le\gamma<H' Z,
  \qquad p_{\min,\mathcal Q}(\ell)>p_{\max}(\gamma),
$$

where the minimum on a missing set is interpreted as infinity and $\ell$ is squarefree. The last condition also gives $(\ell,\gamma)=1$. These conditions give at most one decomposition for each $z$; they are valid as well when the short-variable interval is later moved.

The last condition has a separated expansion of total coefficient norm $O(L)$. Number all primes $<Z$ from 1 to $J$, and let $i$ be the rank of $p_{\max}(\gamma)$ and $j$ that of $p_{\min,\mathcal Q}(\ell)$, using $J+1$ for infinity. On the cyclic group of size $K=2J+3$, expand the indicator of the residues $1,\ldots,J+1$ into its Fourier series. On these ranks it is exactly $\mathbf1_{i<j}$, with expansion

$$
   \mathbf1_{i<j}=\sum_{h\bmod K}c_h e(hj/K)e(-hi/K),
   \qquad \sum_h |c_h|\ll \log(2K)\ll L ,
$$

where $e(s)=e^{2\pi i s}$. The bound follows by the geometric sum estimate $|c_h|\ll (1+|h|_K)^{-1}$ for the centered frequency length. It holds for a subset $\mathcal Q$ using ranks in the full set, so deleting the primes of a fixed integer requires no further separation. This is a weighted Fourier expansion; the number of frequencies does not multiply a uniform bound.

## 2. Preserve the true weights, overlaps and cutoffs

Set $P=\lceil A\rceil+5$, $B=L^{400P}$, $F_0=L^{10000P}$. Use the [strict moving grid](weak-s-type-ii-beyond-near-balance.md#1-exact-reduction-of-strict-moving-cuts-and-square-completion) as in [the seam proof, §3](weak-s-type-ii-effective-fixed-power-seam-tags.md#3-two-disjoint-true-tag-transfers). The mesh is $1+L^{-20P}$ in $u,d$, after imposing the automatic $d<N^{.50001}/2$. This changes at most $O(N L^{1-20P}+N^{.50001})$ pairs of $(d,uv)$ on the three exact cut boundaries. The cited divisor-moment proof with the actual weight $\ll L\tau(uv)$ gives $O_A(NL^{-A-1})$ error, also in the presence of any of our selectors. There are $O(L^{40P+2})$ disjoint hard rectangles, with dyadic scales $U_0,V_0$, $U_0 V_0\asymp N$, $\min(U_0,V_0)\gg N^{.49998}$, $\max(U_0,V_0)\ll N^{.50002}$. Their products, also after the finer freezing below, have $uv,N-uv\asymp N$.

Use the unique $v=a^2 b$ with $b$ squarefree, not necessarily coprime to $a$. We may require $a\le B$. On each rectangle pairs lost to larger $a$ number $O(N/B)$, by summing $V_0/a^2$. We will also remove a selected shared squarefree divisor $g>B$ common to $u,v$; the union of all pairs with such a divisor is at most $O(N\sum_{g>B}g^{-2})=O(N/B)$. Each lost pair carries at most $L\tau(N-uv)$ in absolute value across all $d$. The standard divisor moments give $\sum_{u,v}\tau(N-uv)^2\ll NL^9$ on the support, by $uv=x$ and Cauchy with the second/fourth divisor moments. Thus these removals cost $O(N L^6 B^{-1/2})$ per outer rectangle. We remove only the selected overlap described below, not all common small prime factors. For $a\le B$, a prime dividing $a$ has its whole prime-power contribution to $v$ at most $B^3<V$, so $b_{\rm II}(v)=b_{\rm II}(b)$. Also $a$ has no old-band prime.

**First selector (eligibility on $v$).** With $a$ fixed, take $\mathcal Q=\{p<Z:p\nmid a\}$ and $H'=H/R(a)>1$. Indeed

$$
        R(v)=R(a)\prod_{\substack{p\mid b,\ p<Z\\p\nmid a}}p .
$$

Use the greedy decomposition $b=\gamma\ell$ at $H'$, and put $g=(\gamma,u)\le B$. Fix $g$ and set $\gamma=g r,\ u=g w$, so $r,w$ are squarefree, $(r,w)=1$, and $(g,rw)=1$ on the nonzero Möbius support. Define

$$
             m=a^2 g^2\ell,\qquad n=r w,\qquad mn=uv .
$$

The actual weight on the short leg is $b_{\rm II}(\ell)$, because all factors of $\gamma$ are $<Z<V$ and $b$ is squarefree. The long leg carries exactly $\mu(gw)$, the $u$-interval and $u$'s no-old-tag mask. The short leg carries squarefreeness and the original no-old-tag mask for $\ell$, which is exactly the old-band mask on $v$ since $a,\gamma$ have none. The order condition uses the first $\mathcal Q$-prime of $\ell$ and last of the full $\gamma=gr$. Its order condition also enforces $(\gamma,\ell)=1$, so it is not imposed by an independent approximation.

**Second selector (eligibility on $u$, ineligibility on $v$).** The nonzero $u$ is squarefree. Use $\mathcal Q=\{p<Z\}$, $H'=H$, and the greedy decomposition $u=\gamma\ell$. Now let $g=(\gamma,b)\le B$, write $\gamma=g r, b=g w$, and use the same $m=a^2g^2\ell,n=rw$. The short leg carries $\mu(\ell)$, the old-band exclusion and the order condition, and the long leg carries $\mu(\gamma)b_{\rm II}(w)$ with $a^2 g w$ in the $v$-interval. These are exact, since $\mu(u)=\mu(\gamma)\mu(\ell)$ and all primes of $g$ are $<Z$ and occur only to the first power in $b$. The hard gate $R(a^2 g w)<H$ and the absence of old tags in $v=a^2gw$ are on the long leg; the absence in $u$ is on $\ell$. Possible overlap with the square part $a$ does not cause a second copy in $n$. Both the exact gcd split and squarefreeness of $b$ impose $(r,w)=1,(g,rw)=1$.

In both cases restrict $a,g$ to units modulo $N$, and impose the true unit masks on the remaining factors. Equivalently $(mn,N)=1$ with these fixed units, and the long sequence consists of squarefree odd $n>1$ with $(n,N)=1$. No assumption $(m,n)=1$ is needed. The modulus sign $\mu(d)$, the completion sign and numerator $N$ will not change. Every split retains the exact chosen overlap $g$, because $(r,w)=1$ and squarefreeness of both parent factors are enforced; $(\gamma,\ell)=1$ is the exact order gate above.

## 3. Freeze just the transported product, then use signed dispersion

Partition $\gamma$ into intervals $[T,T(1+\eta'))$ of ratio $1+\eta'$, $\eta'=L^{-200P}$, using at most $O(L^{200P+1})$ cells. Fix $a,g,T$ for the separated expression. On the first selector, replace the hard constraint $\ell\in J_v/(a^2\gamma)$ by $\ell\in J_v/(a^2T)$ for the original $v$-interval $J_v$. On the second selector replace $\ell\in J_u/\gamma$ by $\ell\in J_u/T$. Before separating the order condition, the inverse reconstruction of $u,v$ is still unique, including the choice of the greedy product, its cell, $a,g$, and its short quotient. Thus the total mismatches are among $O(\eta' N+\max(U_0,V_0))$ pairs per outer rectangle, from the two endpoint bands of the changed factor. This estimate counts endpoints once, not once per Fourier term or per admissible product. Using the squared divisor moment above costs at most

$$
  O\bigl(L\sqrt{(\eta' N+\max(U_0,V_0))NL^9}\bigr)
$$

per outer rectangle. The sharp inequalities at integral endpoints are included by the $O(1)$ in the corresponding one-dimensional endpoint count.

Before separating order also require $\tau(n)\le L^{300P}$, a mask on the long leg. In the actual reconstructed product $n\mid uv$, so every removed pair has $\tau(uv)>L^{300P}$. With unique reconstruction, their full cost per rectangle is at most

$$
 L^{1-300P}\sum_{x\asymp N,\ x<N}\tau(x)^2\tau(N-x)\ll N L^{10-300P}.
$$

This permits long coefficients bounded by a power of $L$, even when $\gamma$ has an unbounded number of prime factors: at fixed $n,a,g,T$ each possible $r\mid n$ gives $w=n/r$, hence there are at most $\tau(n)$ representations. Apply the Fourier expansion from §1 after all coefficient comparisons; its $j$-phase belongs to the short variable $\ell=m/(a^2g^2)$, and the $i$-phase to the chosen $\gamma=gr$ in the long coefficient. In each separated expression the product of the short and long coefficient normalizations is at most $L^{300P+1}$.

Complete $\mu^2(N-uv)$ at $c\le B$. In the proof this is performed on the exactly reconstructed post-freezing sum with the exact order indicator before expanding that indicator; the error $O(N L^{70}B^{-1/2})$ per outer rectangle is the square-tail error in the earlier seam proof. Uniqueness again avoids charging a Fourier or cell multiplicity. At fixed $c,g_0=(c,d)$, set $q=[d,c^2]=c^2d/g_0$ on the squarefree $c,d$ support; the resulting map is injective in $d$, and $q$ is a unit modulo $N$ in the actual statistic. The exact congruence is $mn\equiv N\pmod q$.

The transported lengths are

$$
 U\asymp T U_0/g^2\quad\text{or}\quad U\asymp T V_0/(a^2g^2),\qquad MU\asymp N.
$$

As $H/B\le\gamma<H Z$, these satisfy $U\gg N^{.500015}B^{-5}$, $U\ll N^{.500095}$. Every hard completed modulus dyad has $Q\gg X$, $Q\ll N^{.50001}B^2$, hence $Q/U\ll N^{-.000005}B^7$. The arbitrary bounded normalized coefficients satisfy the precise hypotheses of [the effective high-only variance, §2](weak-s-type-ii-effective-fixed-power-seam-tags.md#2-a-high-only-centered-variance); no separate Möbius or prime transform on these coefficients is assumed. Use its $NL^6\sqrt{Q/U}+NF_0^{-1/2}+N^{1-\delta}$ bound for the high projection, restoring the actual signs. For the low projection keep those signs and apply [its signed harmonic reversal, §1](weak-s-type-ii-effective-fixed-power-seam-tags.md#1-remove-the-low-conductors-with-the-actual-modulus-signs) for the actual $c,g_0,d$-piece. The new labels carry no $d$-dependence inside one piece, and its $d$-interval and each $q$-dyad still give a single hard harmonic interval. This supplies the necessary cancellation with $\mu(d)$, not an unsigned upper bound on the low modes.

Reassembly costs at most $O(L^{40P+2}L^{200P+1}B^4 L^{300P+1}L^2)$, from the outer rectangles, product cells, $a,g,c,g_0$, coefficient normalizations, Fourier coefficient norm and modulus dyads. This is $O(L^{2140P+6})$. The $NF_0^{-1/2}$ term, the two fixed-power savings, and the effective harmonic reversal beat this loss. All earlier comparison errors, summed over the outer rectangles only, are $O_A(NL^{-A})$: in particular $B^{-1/2}=L^{-200P}$ dominates their $L^{70}$ and the outer count, and $\eta'^{1/2}=L^{-100P}$ dominates the endpoint comparison. This proves both assertions.

## 4. A genuine occupied family that requires a product

There are arbitrarily large even $N$ with an actual nonzero occurrence on the second selector for which transferring any **single** sub-band prime of $u$ would still leave $Q/U$ growing as a power. To construct them, let a real parameter $Y\to\infty$. Choose five distinct odd primes $p_i\in[Y^{.0000078},1.01Y^{.0000078}]$ and put $\gamma=\prod_i p_i$. Choose odd primes $\ell,v,d,k$ respectively so that

$$
  .740\sqrt Y\le u=\gamma\ell\le .745\sqrt Y,\quad
  .715\sqrt Y\le v\le .720\sqrt Y,\quad
  .100Y^{.500009}\le d\le .101Y^{.500009},\quad
  4.70Y^{.499991}\le k\le 4.75Y^{.499991}.
$$

All intervals have fixed multiplicative length at scales tending to infinity, so existence follows from the prime number theorem. Set $N=uv+dk\asymp Y$. The fixed margins put $uv/N\in(1/2,9/16)$, $k>N^{.49999}$, $d\ge X$, and $u,v<N^{.50002}$ eventually. The primes in $uv$ and $dk$ are disjoint by their different power scales, so $(uv,N)=1$; the odd products make $N$ even. The true squarefree gate is one, the two Möbius factors are nonzero, and $b_{\rm II}(v)=\log v>0$. Neither variable has an old-band prime. Here $R(v)=1$ and $R(u)=\gamma\asymp Y^{.000039}>H$; in fact all five primes are needed to meet $H$. A single factor $p_i$ would leave $d/(p_i v)\asymp Y^{.0000012}\to\infty$ even before square completion. The whole product makes the ratio decrease. Also $d/X\asymp Y^{.000009}$, beyond every earlier stretched $d$-cap with a fixed exponent below 1, and $u,v\asymp X$ do not fall in the power-separated wings. This verifies strict relevance to the polynomially super-square-root seam, not a claim about how many such tuples exist for a prescribed $N$, or about any lower bound for the signed residual.
