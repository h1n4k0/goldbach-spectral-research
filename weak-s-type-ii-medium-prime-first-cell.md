# First-cell transfer and the absolute mass of the untagged balanced remainder

Let $N=2^j$, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and use the exact balanced box and true medium-prime weight

$$
 I=[.740X,.745X],\quad J=[.715X,.720X],\quad D=[.445X,.450X],
 \qquad
 w(v)=\sum_{\substack{N^{.024}<p\le N^{.2499}\\p\mid v}}\log p .
$$

The prime sum is over actual primes. All sums of tuples below impose $u,v,d$ odd and $uv\equiv N\pmod d$, with weight

$$
 W(u,v,d)=\mu(u)\mu(d)\mu^2(N-uv)w(v).
$$

For a fixed sufficiently large absolute constant $C$, put $S=\exp(C L/L_2)$, $z=N^{.001}$, and $\mathcal P=\{s\ \mathrm{prime}:S\le s\le z\}$. A tag means a divisor in $\mathcal P$. Then:
* **Conditional signed estimate:** Under global Dirichlet GRH, $\sum_{v\text{ has a tag}} W(u,v,d)\ll_A NL^{-A}$ for every fixed $A>0$, uniformly on arbitrary subintervals of $I,J,D$. The same estimate holds with the extra restriction that $v$ be squarefree, or nonsquarefree, or that it have no prime divisor in $[N^{.002},2N^{.002}]$, or both one squarefreeness restriction and the latter exclusion.
* **Unconditional size:** The sum of $|W|$ on the full box is $\asymp N L$; the sum of $|W|$ on the full box with no tag of $v$ is $\asymp_C N L/L_2$. Both lower bounds already hold on nonsquarefree $v$ with no old fixed tag. All implied constants are independent of $j$.

Thus the tagged estimate covers all but $O_C(1/L_2)$ of the true absolute weight. This is not an $o(N)$ bound on the signed untagged weight: on the contrary, its absolute weight has the larger order $NL/L_2$. In particular the signed estimate alone proves neither cancellation for the full box nor weak S. The relative size of the band in the logarithm of the primes is now $\log z/\log S=L_2/(1000C)$, not a fixed ratio. It contains the previous moving tag band for all sufficiently large $N$.

## 1. Assign each occupied integer to its first cell

As in the [moving-tag argument](weak-s-type-ii-medium-prime-growing-tags.md), for fixed $v,d$ there is at most one $u$ (and conversely) by uniqueness modulo $d$; nonunit $v$ or $u$ cannot solve the congruence. The box has $N/2<uv<9N/16$ and $k=(N-uv)/d>X$, both with fixed margins, and oddness is the exact unit condition. In what follows use the estimates (3), (4) of that argument for hard-interval Möbius character sums and the unconditional principal mask. In particular, for each fixed polynomial range of $q,W_0$, global GRH gives the nonprincipal bound $\sqrt{Y}\exp(O(L/L_2))$ at scale $Y\le N$ with additional mask $(n,W_0)=1$. The constant in the exponent is uniform and independent of $S$. The unconditional principal bound at scale $X$ with $W_0\le N^{O(1)}$ is $O(Xe^{-c\sqrt L})$.

Partition $[S,z]$ into disjoint consecutive multiplicative cells of ratio at most $1+\eta$, where $\eta=e^{-L_2^2}$; order them increasingly. Assign a tagged $v$ to the first occupied cell. For the cell $E$ with left endpoint $T$, replace occupancy of that cell by summation of its individual prime divisors $s\mid v$, keeping the condition that $v$ has no prime divisor in previous cells. The error is bounded by pairs of distinct primes in the same cell. Indeed each $v,d$ gives at most one $u$; for distinct $s,t$ at most $X/(st)$ positive $v\le X$ have $st\mid v$. Thus, using $w(v)\le L$, the total absolute error is

$$
 \ll NL\sum_E\left(\sum_{s\in E}\frac1s\right)^2
 \ll NL(\eta+S^{-1})\log(2L_2).
$$

Here the maximum harmonic mass of a cell is $O(\eta+S^{-1})$ by counting all integers in it; the total is $O(\log(2L_2))$ by Mertens' theorem. No distribution of primes on the scale of a cell is used.

Write $v=sm$ but do not transfer the earlier-cell condition to a long character sum: it lives **only on $m$**, since $s$ is not in any previous cell. Also $w(sm)=w(m)$ and the optional old-tag exclusion is unchanged, since $s\le N^{.001}$. Discard $s\mid u$ at total cost $O(NL S^{-1}\exp(O(L/L_2)))$: for each such $s$, both $u,v$ are multiples of $s$, and $d\mid N-uv$ gives at most $\tau(N-uv)\le\exp(O(L/L_2))$ choices. If a squarefree/nonsquarefree condition on $v$ is imposed, replace it by that on $m$, with error only when $s^2\mid v$; count $v,d$ and then the unique $u$, costing $O(NL/S)$. All retained tag multiplicities on an integer of size $\le N^{O(1)}$ are $O(L_2)$. Comparisons here and in the next paragraph precede square completion.

Freeze $m$ in $J/T$ rather than $J/s$. Actual differences can only occur for $v$ within $O(\eta X+1)$ integers of the two endpoints of $J$, with at most $O(L_2)$ tag incidences per $v$. Hence the total error is $O(L L_2 X(\eta X+1))$, independent of the number of cells. The tiny enlargement preserves all box margins. Truncate the square completion $\mu^2(N-uv)=\sum_{b^2\mid N-uv}\mu(b)$ at $B=e^{L_2^2}$. The [moving-tag square tail](weak-s-type-ii-medium-prime-growing-tags.md#2-deterministic-errors-for-growing-depth-transfer), by divisor moments and $4,4,2$ Hölder on the $O(N/B)$ different values of $N-uv$ with a missing square divisor, is $O(N L^{O(1)}L_2 B^{-1/2})$. All these errors are $O_A(NL^{-A})$ for every fixed $A$.

## 2. Uniform centered dispersion for the actual transferred term

On a cell let $n=su$, so the new lengths are $U\asymp XT$, $M\asymp X/T$. The short coefficient divided by $L$ is $1$-bounded; it contains the previous-cell sieve mask, optional old fixed mask, $w(m)/L$, oddness, $m\in J/T$, and any prescribed squarefreeness restriction on $m$. No cancellation estimate for this short coefficient is assumed. The long coefficient $\beta_n$ is $1$-bounded after normalizing by an $O(L_2)$ bound for the number of tag representations, and is supported on odd squarefree $n$ because of $\mu(u)$ and $(s,u)=1$.

For a possibly imprimitive nonprincipal character $\chi$, abbreviate the masked Möbius sum to $\mathcal M_\chi(H;W_0)=\sum_{u\in H,(u,W_0)=1}\mu(u)\chi(u)$. Before normalization the exact long transform is

$$
 \left(\sum_{s\in E}\chi(s)\right)\mathcal M_\chi(I;2)
   +\sum_{s\in E}\chi(s)^2\mathcal M_\chi(I/s;2s),
$$

where the second term follows from $\mu(s\ell)=-\mu(\ell){\bf1}_{(\ell,s)=1}$. The short-cell GRH bound $O(\sqrt T L^2)$ for $\sum_{s\in E}\chi(s)$ follows by subtracting endpoint estimates for the ordinary prime character sum (no smooth or short-interval hypothesis). For the second term count $O(T)$ possible $s$ and use the hard Möbius bound at scale $X/s$. Consequently $|\sum_n\beta_n\chi(n)|\ll\sqrt U\exp(O(L/L_2))$ uniformly. The principal transform is $O(XT e^{-c\sqrt L})$ by applying the masked sum with $W_0=2sq$ for each $s$, before summing $s$; its contribution to the principal densities on any modulus dyad is $O(Ne^{-c'\sqrt L})$ by $M\asymp X/T$ and $\varphi(q)^{-1}\ll\log(2q)/q$.

At each odd squarefree $b\le B$, split $d$ by $(d,b)$; then $q=[d,b^2]$ is injective in $d$ and odd with $(q,N)=1$. All moduli are in dyads $Q$ with $X/5\le Q\ll XB^2$; the exact joint congruence is $mn\equiv N\bmod q$. Apply the variance calculation of [moving tags, §3](weak-s-type-ii-medium-prime-growing-tags.md#3-a-uniform-centered-dispersion-budget), with the actual short coefficient above and the just-proved uniform long transform. It applies when $MU\asymp N,\ Q\ll U,\ U\le N^{.502+o(1)}$: the $MU$-sized variance terms after multiplying by $MQ$ cost $O(N^2(Q/U)\exp(C_0 L/L_2))$; all other terms in that section have a fixed power saving with $\kappa=10^{-5}$ and small fixed $\epsilon$. Here $Q/U\ll B^2/T$, $T\ge \exp(C L/L_2)$, and $U\le O(N^{.501})$. Choose $C>C_0+10$, enlarging it as necessary for the absolute errors below. The number of cells is $O(1+(\log z)/\eta)$, and the number of square-completion variables, gcd groups, and modulus dyads together contributes only $\exp(O(L_2^2))$. Hence the entire centered term, with the original $\mu(d)$ and arbitrary choice of subinterval endpoints, beats every inverse logarithm. The principal estimate beats this external overhead as well. This proves the claimed conditional estimates.

## 3. A small elementary sieve sandwich

For any squarefree tag product $r$ write $g(r)=\prod_{s\mid r}g(s)$, where $0\le g(s)\le s^{-1}+2s^{-3}$. Sieve for no primes in $[S,z]$ with real weights $\lambda_r^\pm$ supported on squarefree tag products $r\le z^{30}=N^{.03}$, with

$$
 \sum_{r\mid v}\lambda_r^-\le {\bf1}_{v\text{ has no tag}}\le \sum_{r\mid v}\lambda_r^+,\qquad
 \tfrac12\prod_{s\in\mathcal P}(1-g(s))
 \le\sum_r\lambda_r^-g(r)\le\sum_r\lambda_r^+g(r)
 \le2\prod_{s\in\mathcal P}(1-g(s)).
$$

For completeness, take bands $z^{2^{-i-1}}<s\le z^{2^{-i}}$ intersected with $[S,z]$, $i=0,\ldots,i_{\max}$, with consistent endpoint assignment. About $O(\log(2L_2))$ bands suffice. Each has $\sum_s g(s)\le1$ for large $N$ by the prime number theorem and Mertens' theorem, uniformly because the lowest prime is at least $S\to\infty$. Let $A_i$ indicate no prime of the band dividing $v$; let $U_i,V_i$ be its even and odd Bonferroni truncations at depths $12+2i$ and $13+2i$. Then $U_i\ge A_i\ge V_i$, $U_i\ge0$, and

$$
 \prod_i U_i-\sum_i(U_i-V_i)\prod_{k\ne i}U_k
 \ \le\ \prod_i A_i\ \le\ \prod_i U_i
$$

by telescoping the difference between the two products with nonnegative factors $U_i,A_i$. This yields the stated $r$-support since $\sum_i (13+2i)2^{-i}=30$; the coefficients satisfy $|\lambda_r^\pm|\le O(1+\log(2L_2))$. Under independent Bernoulli divisibility events of means $g(s)$, $\mathbb E A_i=\prod_{s\text{ in band } i}(1-g(s))\ge e^{-2}$. Both $\mathbb E(U_i-A_i)$ and $\mathbb E(U_i-V_i)$ are at most $1/(13+2i)!$ by the factorial moment. Their sum over the bands, relative to $\mathbb E A_i$, is smaller than $1/10$. Independence between bands evaluates the product and correction expectations; expansion by squarefree products gives the displayed inequalities.

With $g(s)=1/s$, counting in $J$ with remainder $O(1)$ per divisor and using the upper weight bounds the number of untagged $v\in J$ by

$$
 O\left(X\prod_{S\le s\le z}(1-s^{-1})+N^{.03}\log(2L_2)\right)=O_C(X/L_2).
$$

The product is $\asymp\log S/\log z$ by Mertens' theorem. Uniqueness of $u$ for each $v,d$ and $w(v)\le L$ give the unconditional upper bound $O_C(NL/L_2)$ for the absolute untagged mass.

## 4. Matching lower bound on occupied untagged tuples

Force $9p\mid v$ for a labeled prime $p\in[N^{.10},N^{.11}]$, and retain squarefree $u,d,N-uv$, oddness, and the original congruence in the full box. Fix $d$ odd squarefree with $3\nmid d$ and $p\nmid d$. Write $A_{d,p}(r)$ for the number of such tuples for this $d,p$ with $r\mid v$. For squarefree tag products $r\le N^{.03}$ one has a model

$$
 A_{d,p}(r)=X_{d,p} g_d(r)+R_{d,p}(r),\qquad
 X_{d,p}\gg \frac{|I||J|}{dp}\left(\frac{\varphi(d)}d\right)^2 ,
$$

where $g_d(r)$ is multiplicative on tag products and

$$
 g_d(s)=
 \begin{cases}
 0,&s\mid d,\\[2pt]
 \displaystyle\frac{1-1/s^2}{s(1-2/s^2+1/s^3)},&s\nmid d .
 \end{cases}
$$

In particular $0\le g_d(s)\le 1/s+2/s^3$ for all large $S$. The total error against the sieve weights satisfies

$$
 \sum_{d,p}\sum_{r\le N^{.03}}|\lambda_r^\pm R_{d,p}(r)|=o(N/L_2),
$$

summing $r$ only on squarefree tag products.

Here is the verification. If $(r,d)>1$ there are no tuples and the model is zero. Otherwise complete $a^2\mid u$, $b^2\mid N-uv$ at $B_0=S^{1/10}$ with Möbius coefficients, and take $q=[d,b^2]$. Require $(9pra,q)=1$, mandatory since the right side is $N=2^j$ and $q$ is odd. The substitution $u=a^2 u_1,\ v=9pr v_1$ with $u_1,v_1$ odd uses the [parity-sensitive rectangular Weil estimate, (4)](weak-s-type-ii-exactly-balanced-diagonal.md#1-exact-support-and-a-squarefree-counting-lemma), giving

$$
 \frac{|I||J|}{36pr a^2}\frac{\varphi(q)}{q^2}
       +O_\epsilon(q^{1/2+\epsilon}).
$$

Here both side lengths are $O(q)$, and $(9pra,q)=1$ ensures the transformed residue is a unit. Summed over $d,p,r,a,b$ this error is $O_\epsilon(N^{.89+\epsilon}B_0^{3+2\epsilon}(1+\log(2L_2)))=o(N/L_2)$: the exponent .89 comes from $.50+.11+.03+.25$, and $B_0=N^{o(1)}$.

The raw deleted square tails also cost $o(N/L_2)$ in this summed error. For $a>B_0$ there are $O(X/B_0)$ affected $u$, then $O(X)$ candidate $v$ and at most $\tau(N-uv)$ moduli. For $b>B_0$ there are $O(N/B_0)$ affected values of $N-uv$, at most $\tau(uv)$ choices of $u,v$, and at most $\tau(N-uv)$ choices of $d$. The magnitude of any truncated square expansion, the multiplicity of sieve divisors $r\mid v$, and the bounded multiplicity of the labels $p\mid v$ together introduce at most $\exp(O(L/L_2))$, with an absolute constant. Since $B_0=\exp(C L/(10L_2))$, $C$ can absorb this and make the error $o(N/L_2)$.

Extending only the model coefficients to all squarefree odd $a,b$ costs

$$
 \ll \frac{|I||J|}{dpr} B_0^{-1/2}\exp(O(\sqrt L))
$$

per $d,p,r$ by half-power Rankin on the omitted $a,b$ sums. In this absolute Euler product the only factors of size $1+O(s^{-1/2})$, rather than $1+O(s^{-3/2})$, come from $b$-primes dividing $d$; split prime divisors of $d$ at $L$ to obtain the $\exp(O(\sqrt L))$ factor. This bound is uniform in all excluded primes. The reciprocal sums over $d\in D$, $p\in[N^{.10},N^{.11}]$ are bounded, and $\sum_{r\le N^{.03}}1/r \ll L$, enough for the summed model tails. In the resulting signed Euler product, a prime $s\nmid 6dpr$ can occur in $a$, in $b$, or in neither, not in both because $(a,[d,b^2])=1$. Its factor is $1-2/s^2+1/s^3$. At a prime dividing $3pr$ one must omit the $b$-choice, changing the factor to $1-1/s^2$. At each prime dividing $d$ the two factors are $(1-1/s)^2$ after extracting $1/d$, one from the base modulus and one from the optional $b$-choice. This proves the model with the stipulated $g_d$ and a positive $X_{d,p}$ (the product with $r=1$).

Uniformly in $d$, $\prod_{s\in\mathcal P}(1-g_d(s))\asymp_C 1/L_2$: the change from $g(s)=1/s$ at primes $s\nmid d$ has convergent $O(\sum_{s\ge S}s^{-3})$ logarithmic cost; at the $O(L_2)$ tag primes that can divide $d$ it costs $O(L_2/S)$. A positive proportion of $d\in D$ are odd squarefree, coprime to 3, and have $\varphi(d)/d$ bounded below by an absolute constant (squarefree counting and averaging $\sum_{s\mid d}1/s$). For each such $d$, omitting $p\mid d$ loses $O(N^{-.10})$ from a reciprocal prime sum of constant order. Hence $\sum_{d,p}X_{d,p}\gg N$, and the lower sieve sandwich gives $\gg_C N/L_2$ labeled occupied untagged tuples. Each $v$ has only $O(1)$ labels $p$ in that band, and $w(v)\ge .10L$ on them. These are actual tuples with $|W|=w(v)$ and $9\mid v$. Discarding old fixed tags removes only $O(N/L)$ unweighted tuples, by counting their $v,d$ and using uniqueness of $u$, so the untagged lower bound persists with the old exclusion. Finally the same model at $r=1$, with the same errors, has $\gg N$ labeled tuples even before the tag sieve. This gives the asserted full unsigned lower bound, also on nonsquarefree $v$ with no old tag. The upper bound is immediate from uniqueness and $w(v)\le L$.
