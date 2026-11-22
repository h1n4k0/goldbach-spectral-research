# Signed exchange of two large prime divisors in the small-radical seam

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $V=N^{.2499}$, $Z=N^{.00004}$, and $H=N^{.000035}$. Keep the actual [R54 seam and remaining selectors](weak-s-type-ii-composite-seam-transport.md): the summand is

$$
 \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk),
 \qquad b_{\rm II}(v)=\sum_{r\mid v,\ r>V}\Lambda(r),
$$

on $uv+dk=N$, $N/2<uv\le y\le9N/16$, $k>t\ge N^{.49999}$, $(uv,N)=1$, $d\ge X$, $u,v\le N^{.50002}$, with optional hard subintervals of $u,v,d$. Suppose neither $u$ nor $v$ has a prime factor in $[Z,N^{.001}]$, and their small radicals $R(w)=\prod_{p<Z,\ p\mid w}p$ satisfy $R(u),R(v)<H$.

**Theorem.** Add the selector that there exist primes $r\mid u,\ s\mid v$, both $>N^{.001}$, for which

$$
       N^{.000035}\le \max(s/r,r/s)\le N^{.0009}.
$$

For every fixed $A>0$, the genuine signed sum on this selector is $O_A(NL^{-A})$, unconditionally and with effective constants, uniformly in those hard and slanted cuts. This applies with the full possible modulus range $X\le d<N^{.50001}/2$. The same estimate holds on each of the two disjoint selectors: a pair with $s/r$ in the band exists, or none exists in that orientation but a pair with $r/s$ in the band does.

The argument exchanges two large primes rather than moving one prime or a small-radical product. It needs only their ratio to transport the scale; both primes may individually be around $N^{1/4}$, too large for that variance estimate to use as single labels. Section 4 verifies a genuine occupied family in the previous remainder. This does not estimate the signed no-exchange complement or prove weak S.

## 1. Exact first-pair selection and bounded separation norm

After ignoring zero $\mu(u)$ terms, write $u=r\ell$ for a prospective prime $r$ and let $v=a^2 b$ be the unique square decomposition, with $b$ squarefree, not necessarily coprime to $a$. We will keep $a\le B$, a fixed power of $L$ chosen in §2. A prime $s>N^{.001}$ dividing $v$ must then divide $b$ and not $a$, and we write $b=s w$. Both $\ell$ and $w$ are squarefree. All eligible prime lists below use distinct primes $>N^{.001}$.

Both variables and all residual quotients are $\ll N^{.50002}$ even after relative endpoint perturbations. Each therefore has fewer than $K=600$ eligible primes for sufficiently large $N$, since a product of $K$ such primes exceeds $N^{.6}$. Enumerate a fixed set of labels: first the orientation $s/r$, then $r/s$, and within each orientation the lexicographic pairs of indices $(i,j)$ in the increasing eligible-prime lists of $u,v$, respectively, padded with zeros after the last actual prime. Choose the first label that meets the ratio band and has both primes nonzero. This assigns each actual selected tuple exactly once and makes the two oriented selectors disjoint.

For a fixed label, insert $r$ as rank $i$ in the list for $\ell$, and $s$ as rank $j$ in that for $w$. The rank conditions are exactly two comparisons for each: the rank $i-1$ prime of $\ell$ is $<r$ and $r$ is less than the rank $i$ prime of $\ell$, using 0 for rank 0 and $+\infty$ for every missing positive rank in this rank test; similarly for $s,w$. This also proves $(r,\ell)=(s,w)=1$ in the recombined expression. For comparing other original rank pairs use the zero-padded lists of $\ell,w$ with the two insertions at the specified ranks. Each rank in the result is either the selected prime or a specific rank of the indicated quotient. It is therefore a function of just one of the two legs in either exchange of §2. Impose that the selected ratio is in the band and all earlier label predicates fail. Each ratio predicate consists of nonzero masks for both operands and two comparisons, including endpoints. Its failure is one minus that exact predicate, not a change of either endpoint.

Here is the needed separated expansion. For any comparison $F\le G$ or $F<G$ between functions on different legs, form the ordered union of the possible values of the two operands, assigning identical values the same rank and including any sentinel separately. This union has $O(N)$ entries: an operand is one prime or sentinel from the supported ranges, possibly scaled by a fixed ratio cutoff, and separate ranks handle equal real values. On the two ranks the comparison is a fixed interval of their difference in a cyclic group of twice the rank range plus three, without wraparound ambiguity. Its Fourier expansion is a sum of products of two modulus-one factors with the coefficient $\ell^1$ norm $O(L)$ by the geometric sum formula, just as in [R54 §1](weak-s-type-ii-composite-seam-transport.md#1-greedy-divisors-and-exact-separation-of-order). A comparison on one leg needs just its bounded indicator. Products of expansions multiply their $\ell^1$ bounds, and subtraction from one adds at most one. In particular the full selected-label condition, including rank validity and failure of all earlier pairs, has an exact separated expansion of $\ell^1$ norm $O(L^{C_*})$ with $C_*=4K^2+8$ a fixed constant. Indeed there are at most $2K^2$ earlier predicates, costing at most two powers each; the four rank comparisons and the selected ratio cost at most six more powers. Nonzero masks cost no extra power. These norm bounds hold without restrictions on how fast phases vary, and do not count the number of Fourier frequencies as a loss.

## 2. Exact exchange, coprimalities and hard endpoints

Set $P=\lceil A\rceil+C_*+10$, $B=L^{400P}$, $F_0=L^{10000P}$. First use the [strict moving grid](weak-s-type-ii-beyond-near-balance.md#1-exact-reduction-of-strict-moving-cuts-and-square-completion) with mesh $1+L^{-20P}$ in $u,d$, after imposing the automatic $d<N^{.50001}/2$. It costs $O_A(NL^{-A-1})$ also with these selectors: each changed $(d,uv)$ is among the same three boundary bands, and its weight never exceeds $L\tau(uv)$. The $O(L^{40P+2})$ hard rectangles have physical dyadic scales $U_0,V_0$ with $U_0V_0\asymp N$, $\min(U_0,V_0)\gg N^{.49998}$, $\max(U_0,V_0)\ll N^{.50002}$. Products and complements remain $\asymp N$.

On each rectangle discard $a>B$, which affects $O(N/B)$ factor pairs by summing the square divisors of the $v$-range. If the chosen transfer would introduce a square on its new long leg, also discard that tuple. Such a pair must share an eligible prime $p>N^{.001}$ between $u,v$, and the number of pairs sharing any such prime is $O(N\sum_{j>N^{.001}}j^{-2})=O(N^{.999})$. This is only an upper bound for the loss: the exact new support requires squarefreeness of the transferred long product, not a prohibition on all common primes. The removed pairs cost $O(N L^6(B^{-1/2}+N^{-.0005}))$ per outer rectangle. For this and subsequent endpoint comparisons use

$$
  \sum_{u,v}\tau(N-uv)^2\ll NL^9
$$

on the slightly enlarged support, by $uv=x$ and the second/fourth ordinary divisor moments, and multiply each lost pair by at most $L\tau(N-uv)$ before Cauchy. The assigned label is unique, so there is no factor for the number of possible prime pairs in these comparisons.

For the retained fixed $a$, $b_{\rm II}(v)=b_{\rm II}(b)$ because the whole prime-power contribution at a prime dividing $a$ is at most $a^2p\le B^3<V$. Since $b=s w$ is squarefree,

$$
 \mu(u)b_{\rm II}(v)=-\mu(\ell)\bigl(b_{\rm II}(s)+b_{\rm II}(w)\bigr).
$$

The absence of old tags and the small-radical gates on $u,v$ are respectively exactly the masks on $\ell$ and on $a^2 w$, since $r,s>N^{.001}$. Keep all $N$-unit masks on the labels, residual factors, and fixed $a$. In particular, $N$ remains even, so actual unit factors are odd.

In the first orientation define $m=a^2 r w,\ n=s\ell$. The $m$-leg holds $(r,w)$ and the $n$-leg holds $(s,\ell)$. In the second define $m=a^2 s\ell,\ n=r w$, with the legs reversed. In both orientations $mn=uv$, the true sign above is a sum of two separable weights on the new legs, and all the individual $N$-unit and residual squarefree masks can be imposed per leg. Explicitly impose $(s,\ell)=1$ in the first orientation and $(r,w)=1$ in the second, a one-leg condition implementing the loss just bounded. Thus the long input is supported on odd squarefree $n>1$ with $(n,N)=1$ even in each individual Fourier term. The short input may be nonsquarefree. There is no assertion that $(m,n)=1$ is necessary. The chosen-rank gate ensures all original squarefreeness conditions at recombination, not a squarefree assumption on $v$. The factors $\mu(d)$ and $\mu^2(N-uv)$ and the congruence numerator $N$ are unchanged.

Partition $r,s$ separately into cells $[R,R(1+\eta'))$, $[S,S(1+\eta'))$ with $\eta'=L^{-200P}$. Use the original order predicates, not a frozen ratio: only consider cell pairs whose ratio range intersects a qualifying ratio for the orientation. Freeze the divided hard intervals $\ell\in J_u/r,\ w\in J_v/(a^2s)$ as $\ell\in J_u/R,\ w\in J_v/(a^2S)$. This separates the two divided cuts from the labels; the exact ratio and earlier-pair conditions use the Fourier separation in §1. Before expanding these predicates, each pair $(u,v)$ still has its unique actual first label and cells, with uniquely determined $a,b,\ell,w$. Therefore every mismatch is counted once and is confined to endpoints of $u$ or $v$ with widths $O(\eta' U_0+1)$ and $O(\eta' V_0+1)$. There are $O(\eta' N+U_0+V_0)$ such pairs per outer rectangle. The above moment bound costs $O(L\sqrt{(\eta' N+U_0+V_0)NL^9})$. Sharp boundaries and equality tests are covered by the additive integers in the endpoint counts or by the exact comparison, respectively.

## 3. Polylogarithmic coefficients and signed dispersion

Before expanding the first-pair predicate, impose $\tau(m),\tau(n)\le L^{300P}$. By exact product equality, removed pairs have $\tau(uv)>L^{300P}$. Reconstruction is unique while the predicate is still in place. The total loss per outer rectangle is

$$
 L^{1-300P}\sum_{\substack{x\asymp N\\x<N}}\tau(x)^2\tau(N-x)
   \ll N L^{10-300P}.
$$

At fixed $m,a$ each possible prime label dividing $m/a^2$ determines its short-leg quotient, and at fixed $n$ each possible prime divisor determines its long-leg quotient. Thus after Fourier separation, the uniform product of coefficient normalizations is at most $L^{600P+1}$ in each of the two weights; it is not necessary to assume one representation on a separated leg. The individual phases have modulus one and the full coefficient sum is controlled by the $\ell^1$ bound.

Complete $\mu^2(N-uv)$ at $c\le B$ before expanding the predicate. The usual [square-tail bound in the seam](weak-s-type-ii-effective-fixed-power-seam-tags.md#3-two-disjoint-true-tag-transfers) costs $O(NL^{70}B^{-1/2})$ per outer rectangle; again unique reconstruction prevents multiplication by the number of chosen cells or Fourier terms. On the support of $\mu(c)\mu(d)$, fix $g=(c,d)$ and put $q=[d,c^2]=c^2d/g$. This is injective in $d$, and $c,d,q$ are units modulo $N$ in the actual sum. The congruence is $mn\equiv N\pmod q$ with the exact modulus sign.

In the first orientation the new long scale is $U\asymp (S/R)U_0$; in the second it is $U\asymp (R/S)V_0/a^2$. The short scale satisfies $MU\asymp N$ in either. Whole cells contributing to the chosen orientation have the relevant ratio within a factor $(1+\eta')^2$ of the displayed band. Therefore

$$
  N^{.500015}B^{-2}\ll U\ll N^{.50092},\qquad
  X\ll Q\ll N^{.50001}B^2,\qquad Q/U\ll N^{-.000005}B^4
$$

in every completed modulus dyad. These are within [R51's effective high-only variance](weak-s-type-ii-effective-fixed-power-seam-tags.md#2-a-high-only-centered-variance) for arbitrary bounded coefficients with the stipulated long support. Apply its $NL^6\sqrt{Q/U}+NF_0^{-1/2}+N^{1-\delta}$ high-conductor bound; the actual sign may be restored there. For the removed low conductors use [R51's signed harmonic reversal](weak-s-type-ii-effective-fixed-power-seam-tags.md#1-remove-the-low-conductors-with-the-actual-modulus-signs), including the principal, with the exact signs $\mu(c)\mu(d)$. All factor labels, Fourier weights and tests within a piece are independent of $d$, and the hard $d$-cut and $q$-dyad still give a single interval in the remaining harmonic variable. This uses the effective ordinary zeta estimate of that reversal, not a Dirichlet GRH or Siegel–Walfisz estimate on any oscillatory leg.

There are constantly many first labels, $O(L^{40P+2})$ outer rectangles, $O(L^{400P+2})$ pairs of prime cells, at most $B^3$ external choices for $a,c,g$, and $O(L)$ completed modulus dyads. Restoring normalizations and the separated comparison norm costs a total $O(L^{2240P+C_*+6})$ even before any saved logarithm. This is beaten by $F_0^{-1/2}=L^{-5000P}$, the fixed power savings, and the effective exponential in the harmonic reversal. All comparison errors sum over the outer rectangles only, and the displayed choices beat their logarithms. This proves the two signed estimates.

## 4. Actual support outside small-radical transport

For arbitrarily large real $Y$, choose odd primes $r\asymp Y^{.2501}$ and $s\asymp Y^{.2506}$, in fixed multiplicative intervals, and then odd primes $\ell,w$ so that

$$
 .740\sqrt Y\le u=r\ell\le .745\sqrt Y,\qquad
 .715\sqrt Y\le v=s w\le .720\sqrt Y .
$$

Choose odd primes $d\in[.100,.101]Y^{.500009}$ and $k\in[4.70,4.75]Y^{.499991}$ and set $N=uv+dk$. The prime number theorem applies to all intervals, including those for $\ell,w$, since they have fixed positive relative width and scales $\asymp Y^{.2499},Y^{.2494}$. All primes are distinct for large $Y$ by their different scales, so $N$ is even, $(uv,N)=1$, $\mu^2(dk)=1$, and $\mu(u)\mu(d)\ne0$. The physical ratios give $N\asymp Y$, $N/2<uv<9N/16$, $k>N^{.49999}$, $d\ge X$, and $u,v<N^{.50002}$. In fact $d/X$ grows as a fixed power, outside the earlier stretched caps, and $u,v\asymp X$ miss the power-separated wings. Neither variable has any prime in the old or the small-radical bands: $R(u)=R(v)=1$. The true marked weight is $\log s>0$, since $s>N^{.2499}$ and $w<N^{.2499}$ eventually. The pair $r,s$ has ratio $\asymp Y^{.0005}$ and triggers the proved selector. Moving either of those primes alone would instead put the long scale far beyond the variance range. This establishes strict additional occupied support, not a density claim or a signed lower bound.
