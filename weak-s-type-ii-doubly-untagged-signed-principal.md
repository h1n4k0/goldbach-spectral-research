# The signed principal on the doubly untagged Type II core

Work with the exact balanced box of [R42](weak-s-type-ii-medium-prime-opposite-tags.md): $N=2^j,\ X=\sqrt N,\ L=\log N,\ L_2=\log L,\ L_3=\log L_2$,

$$
 I=[.740X,.745X],\quad J=[.715X,.720X],\quad D=[.445X,.450X].
$$

The sum is over odd $u,v,d$ in these intervals with $uv\equiv N\bmod d$, and the actual signed summand is $W=\mu(u)\mu(d)\mu^2(N-uv)w(v)$, where $w(v)=\sum_{N^{.024}<p\le N^{.2499},\,p\mid v}\log p$ over primes. Put $S=\exp(C L/L_2)$, $z=N^{.001}$, $\mathcal P=[S,z]\cap\mathbb P$, and let $\mathcal P_*\subset\mathcal P$ be R42's narrower tag band, ending at $S^{L_3/\log^2(2L_3)}$. A tagged variable is divisible by a prime in the named band. Fix $C$ sufficiently large, as in R41/R42.

**Results.**
1. Under global Dirichlet GRH, the exact signed sum on the R42 residual slice

$$
 v\text{ has no }\mathcal P\text{ tag};\qquad
 u\text{ has no }\mathcal P_*\text{ tag but has a }\mathcal P\text{ tag}
$$

is $O_A(NL^{-A})$ for every fixed $A$, uniformly on arbitrary hard subintervals of $I,J,D$. Its unconditional unsigned mass on the full box is $\asymp_C NL/(L_2 H_*)$, $H_*=L_3/\log^2(2L_3)$. The underlying transfer uses the actual sign $\mu(d)$ to remove the complete principal density. It does not assert cancellation for the sifted short Möbius coefficient at an individual modulus.
2. On the still smaller core with neither variable $\mathcal P$-tagged, all principal terms of the truncated genuine square completion already cancel to all inverse-log orders, unconditionally. Its actual unsigned mass on the full box is $\asymp_C NL/L_2^2$. Even after subtracting the exact principal for the single square-completion term $c=1$, summing the absolute values over $(d,u)$ on a fixed positive-density set of moduli costs $\asymp_C NL/L_2^2$ in original weight units. This is a limitation of that termwise absolute-value method, not a lower bound for the signed $c=1$ covariance or the total signed core. The signed remaining nonprincipal correlations are open.

## 1. Signed summation of the principal density

Let $B=\exp(L_2^2)$. Fix odd squarefree $c\le B$, fix $g\mid c$, and retain squarefree odd $d$ in any hard subinterval of $D$ with $(d,c)=g$. Set $q=[d,c^2]$, and optionally restrict $q$ to a hard dyadic subinterval. Let $\alpha_m,\beta_n$ be any fixed, finitely supported coefficients on positive integers $\le N^{O(1)}$, independent of $d$ within this piece. Then

$$
 \left|
 \sum_d \frac{\mu(d)}{\varphi(q)}
   \sum_{(m,q)=1}\alpha_m\sum_{(n,q)=1}\beta_n
 \right|
 \ll \frac{\|\alpha\|_1\|\beta\|_1}{\varphi(c^2)}
              \exp(-c_0\sqrt L).
 \tag{1}
$$

In the sum only nonzero $\mu(d)$ matters. Write $d=ge$: then $(e,c)=1$, $\mu(d)=\mu(g)\mu(e)$, $q=c^2e$, and $\varphi(q)=\varphi(c^2)\varphi(e)$. For each $m,n$ discard unless $(mn,c)=1$; its remaining mask is $(e,2cmn)=1$, with $e$ in an interval at scale $Y\asymp X/g$. In particular $Y=N^{1/2-o(1)}$ and the mask is polynomial-sized.

Uniformly for such $Y$ and any polynomial-sized mask $V$, the harmonic sum $\sum_{e\in H,\,(e,V)=1}\mu(e)/\varphi(e)$ on a hard subinterval $H$ at scale $Y$ is $O(\exp(-c_0\sqrt L))$. To verify this, use $e/\varphi(e)=\sum_{h\mid e}\mu^2(h)/\varphi(h)$, obtaining exactly

$$
 \sum_{\substack{h\ll Y\\(h,V)=1}}\frac{\mu(h)}{h\varphi(h)}
       \sum_{\substack{k\in H/h\\(k,hV)=1}}\frac{\mu(k)}k .
$$

For $h\le \sqrt Y$ use the unconditional masked Mertens argument of [moving tags, §1](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums), now by partial summation to harmonic weight. Its proof applies at every polynomial scale $Y'\ge N^{.2}$: convolve $\mu$ with the finite correction at primes dividing $hV$, use ordinary zero-free-region Mertens on indices up to $\sqrt{Y'}$, and bound higher indices by the quarter-power Rankin tail. Fixed polynomial size of $hV$ gives uniform constants. Here $Y/h\ge N^{.2}$ for large $N$. For $h>\sqrt Y$ the inner harmonic sum is $O(1)$ trivially (the interval is at scale $Y/h$), and $\sum_{h>\sqrt Y}1/(h\varphi(h))\ll Y^{-1/2}\log(2Y)$. This proves (1) by exact reversal of finite sums. No claim about a principal sum with arbitrary signs on a subfamily of $d$ is made; the hard $d$-interval and exact $\mu(d)$ are essential.

## 2. Annular transfer with the original signs

The fixed-width box implies a unique $u$ for each $(v,d)$ and a unique $v$ for each $(u,d)$ on the congruence. The same holds for the tiny enlargements below. Both $N/2<uv<9N/16$ and $(N-uv)/d>X$ hold with fixed margins. No alias or original moving cutoff changes.

First write $v=a^2b$ uniquely with $b$ squarefree. Discard $a>B$ at absolute cost $O(NL/B)$ by counting affected $v\le X$ and then $d$. For $a\le B<S$, $b$ has the exact $\mathcal P$-exclusion and $w(b)=w(v)$. Partition $\mathcal P\setminus\mathcal P_*$ into ordered multiplicative cells of ratio at most $1+\eta$, $\eta=\exp(-L_2^2)$, with left endpoints $T$. Assign $u$ to its first occupied cell, maintaining its full narrow-band exclusion. Replace that occupancy by summing the individual prime divisors $s$ in the cell. The overcount costs

$$
 O\!\left(NL\sum_{\rm cells} (\sum_{s\ \rm in\ cell}s^{-1})^2\right)
 \ll NL(\eta+S^{-1})\log(2L_2)
$$

by counting multiples of two distinct cell primes in $u$ and using unique $v$ for each $u,d$. This uses only the elementary per-cell harmonic bound $O(\eta+S^{-1})$ and the total $O(\log(2L_2))$. All tag multiplicities per integer of polynomial size are $O_C(L_2)$.

Write $u=s\ell$. Replacing $\mu(s\ell)$ by $-\mu(\ell)$ fails only on $s^2\mid u$, costing $O(NL/S)$ by the same uniqueness and $\sum_{s\ge S}s^{-2}\ll1/S$. The narrower-band and earlier-cell exclusions on $u$ now sit entirely on $\ell$, since $s$ belongs to neither forbidden set. Freeze $\ell\in I/T$ instead of $I/s$; the differences put $u$ within $O(\eta X+1)$ of an endpoint. Thus the total cost is $O(L L_2 X(\eta X+1))$ before square completion, summed over actual affected $u,d$ and all their original tags. The error estimates do not multiply by the number of cells. Truncate the completion of $\mu^2(N-uv)$ at square-root divisor $c\le B$; the same divisor-moment $4,4,2$ Hölder bound as in R41 costs $O(NL^{O(1)}L_2 B^{-1/2})$, counting $O(N/B)$ exceptional values of $N-uv$, at most $\tau(uv)$ factorizations, divisor-multiplicity weight of $N-uv$, and the tag multiplicity. Every error beats any fixed inverse logarithm.

For fixed $a$ and cell set $m=a^2\ell,\ n=sb$. Then $mn=uv$ exactly, and $n$ is odd and squarefree since $b$ has no broad tag. Put $-\mu(\ell)$, oddness, the frozen interval and the narrow and earlier-cell masks on $\alpha_m$. Put $w(b)$ and the exact $b$-interval and exclusions, summed over tag representations, on $\beta_n$; divide by $O(LL_2)$ to make it $1$-bounded. Both coefficients are independent of $d$ and have lengths $M\asymp Xa^2/T,\ U\asymp XT/a^2$, with $MU\asymp N$. For every nonprincipal $\chi$ (including imprimitive), the long transform factors before normalization into $\sum_{s\ {\rm in\ cell}}\chi(s)$ and the actual R42 masked squarefree transform of $b$ at scale $X/a^2$. The GRH prime bound $O(\sqrt T L^2)$ plus [R42's bound (1)](weak-s-type-ii-medium-prime-opposite-tags.md#1-the-long-transform-with-the-exact-wide-euler-exclusion) give $\sqrt U\exp(O(L/L_2))$. The arbitrary short mask thus need not satisfy a character transform bound. The argument also permits optional squarefree/nonsquarefree $v$, by choosing $a=1$ or $a>1$, and the previous old fixed tag exclusion of $v$ via the R42 transform.

For each odd squarefree $c\le B$ fix $g=(d,c)$, so $q=[d,c^2]$ is injective in $d$, odd and coprime to $N$. The exact congruence is $mn\equiv N\bmod q$. On dyads $Q\asymp q$ one has $U\ll N^{.501}$ and $Q/U\ll B^4/S$. Apply the same quantitative centered variance as [R41, §2](weak-s-type-ii-medium-prime-first-cell.md#2-uniform-centered-dispersion-for-the-actual-transferred-term). The $MU$ variance terms after Cauchy are $O(N^2(Q/U)\exp(O(L/L_2)))$; the other terms have a fixed power margin. With $C$ large, this beats the external factor $\exp(O(L_2^2))$ counting $a,c,g$, dyads, cells and the coefficient normalization. Keep the actual $\mu(d)$ in the principal term, and apply (1) rather than an absolute bound per $q$. This proves the signed assertion on the annular slice. The local coupling of the principal term to $d$ has only the unit masks, which enter (1); the squarefree $N-uv$ gate was not dropped.

## 3. The actual centered obstruction on the residual double-wide core

Use the proof of [R42, §3](weak-s-type-ii-medium-prime-opposite-tags.md#3-actual-double-untagged-unsigned-scale) with $\mathcal P$ in both variables. This is only a use of its unconditional two-variable sieve calculation: both divisor levels remain $z^{30}=N^{.03}$; both numbers of bands and all error terms are unchanged; the local overlap factors are identical, and both single-variable densities become $\asymp_C 1/L_2$. Hence the actual double-wide untagged mass is $\asymp_C NL/L_2^2$. Its lower bound comes from the same true tuples with $9p\mid v$, $p\in[N^{.10},N^{.11}]$; one can and does restrict the moduli to a positive-density subset $D_0$ of odd squarefree $d\in D$, $3\nmid d$, with $\varphi(d)/d\ge c_1>0$, as in that proof (its lower model and all absolute errors hold on this restriction). The resulting number of distinct tuples is $\gg_C N/L_2^2$ and $w(v)\ge .10L$ on them. Comparing with the original R42 mass gives the claimed size of the disjoint annular slice since $H_*=o(L_2)$.

On the whole double-wide core, complete $\mu^2(N-uv)$ at $c\le B$ without transfer. The omitted square tail is $O_A(NL^{-A})$ by the same divisor-moment bound, now without multiplicity. Apply (1) directly to the coefficients $\alpha_u=\mu(u){\bf1}_{u\ {\rm odd,\ no\ broad\ tag}}$ and $\beta_v=(w(v)/L){\bf1}_{v\ {\rm odd,\ no\ broad\ tag}}$, on the original hard intervals. Summing over $c,g$ and dyads and restoring $L$ still gives an unconditional $O_A(NL^{-A})$ for the **signed total principal**. Thus only the centered nonprincipal terms remain at the target scale.

For a concrete limitation at $c=1$, put $A_d=\{u\in I:\ u\text{ odd, squarefree, not broadly tagged},\ (u,d)=1\}$, and, for $u\in A_d,\ d\in D_0$, put

$$
 E_d(u)=\sum_{\substack{v\in J\\uv\equiv N\bmod d}}\beta_v
         - \frac1{\varphi(d)}\sum_{\substack{v\in J\\(v,d)=1}}\beta_v .
$$

The second term is the exact principal of this $c=1$ piece. It is $O_C(1/L_2)$ uniformly in $D_0$, since the number of broadly untagged $v\in J$ is $O_C(X/L_2)$ by [R41, §3](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich). Each true occupied tuple just counted gives a distinct $(d,u)$, by uniqueness of $v$, and has $|E_d(u)|\ge .05$ for large $N$. Conversely the number of potentially occupied pairs is $O_C(N/L_2^2)$ by the upper joint-sieve bound, which ignores all square gates. Also $\# A_d=O_C(X/L_2)$, so the sum of the absolute principal over $d,u$ is $O_C(N/L_2^2)$. The pointwise bound $|E_d(u)|=O(1)$ follows from uniqueness. Thus

$$
 \sum_{d\in D_0}\sum_{u\in A_d}|E_d(u)|
 \asymp_C
 \sum_{d\in D_0}\sum_{u\in A_d}|E_d(u)|^2
 \asymp_C N/L_2^2 .
$$

Multiplication by $L$ gives the stated absolute-value barrier for $c=1$. It does not determine the signed correlations with $\mu(u)\mu(d)$ or cancellation between square-completion terms, so it does not settle the double-wide core, the full central box, or weak S.
