# A general-even moving Vaughan slab, with two explicit modulus caps

Let $N$ be any sufficiently large even integer, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and $V=N^{.2499}$. Use the actual Vaughan coefficient

$$
       b_{\rm II}(v)=\sum_{r\mid v,\,r>V}\Lambda(r).
$$

Assume GRH only for primitive nonprincipal Dirichlet characters of conductor at most $N^{.05}$, with the same individual interpretation as in [R46](weak-s-type-ii-slanted-near-balanced-slab.md). There is no hypothesis on $\zeta$ or on primitive conductors above this range. Uniformly for $N^{.49999}\le t\le N^{.50001}$, $N/2\le y\le9N/16$, and hard subintervals of the displayed variable ranges, consider

$$
 \mathcal V_N(D_{\max})=
 \sum_{\substack{uv+dk=N,\ N/2<uv\le y,\ k>t,\ (uv,N)=1\\
          N^{.488}\le u,v\le N^{.512},\quad 1\le d\le D_{\max}}}
        \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk).
$$

Then the two bounds are:
* If $D_{\max}=XL^{10}$, then $\mathcal V_N(D_{\max})\ll N L_2^4/L$.
* Separately, for any fixed $0<\rho<1/4$, if $D_{\max}=X\exp(L^\rho)$, then $\mathcal V_N(D_{\max})\ll_\rho N L^{4\rho-1}$.

Both are $o(N)$. The quantitative bound $N L_2^4/L$ is not asserted up to the larger cap. In either case the upper modulus restriction is automatic when $t\ge N/D_{\max}$; the restriction on $u,v$ remains. This works for arbitrary odd factors of $N$, includes the small moduli down to $d=1$, and retains the actual unit condition, signs and squarefree gate. No claim is made for $d$ above the chosen cap, for all of Type II, or for weak S.

## 1. Common conventions and exact boundary control

Write $D_{\max}=X e^H$, taking $H=10L_2$ and $H=L^\rho$ in the two cases, respectively. Let $n=uv$. From $(u,N)=(v,N)=1$ and $d\mid N-n$ one has $(d,N)=1$. In the square completion $\mu^2(N-n)=\sum_{c^2\mid N-n}\mu(c)$ one also necessarily has $(c,N)=1$. Thus the completed modulus $q=[d,c^2]$ is coprime to $N$ on the actual tuples, regardless of the odd factors of $N$. These unit conditions are kept, not replaced by oddness.

Flatten the product and strict quotient cuts by the [R46 multiplicative grid, §1](weak-s-type-ii-slanted-near-balanced-slab.md#1-flatten-the-genuine-cut-with-one-total-weighted-boundary-bound). Explicitly partition $u,d$ into half-open relative cells of ratio at most $1+\eta$, $\eta=L^{-100}$, splitting the $d$-range also at $N^{.49}$. For fixed left endpoints $u_0,d_0$, the exact comparisons are replaced by $v>N/(2u_0)$, $v\le y/u_0$, $v<(N-td_0)/u_0$, retaining the strict inequalities and all independent interval and unit masks. The $O(L^{202})$ resulting rectangles may be split into a bounded number of dyadic pieces in $v$; their scales $U_0,V_0,D_0$ satisfy $U_0V_0\asymp N$. At every changed tuple, either the original or frozen acceptance gives $td=O(N)$, so some $|n-N/2|,|n-y|,|n+td-N|$ is $O(\eta N)$ and $n,N-n\asymp N$. This includes equality at every strict moving endpoint.

For each fixed $d$ the union of boundary strips contains $O(1+\eta N/d)$ integers $n\equiv N\bmod d$. Hence the total number of changed $(d,n)$ is $O(\eta N L+X e^H)$. Dropping unit masks for an absolute error and using

$$
 \sum_{d,n:\ d\mid N-n,\ n,N-n\asymp N}\tau(n)^2
    \le\sum_n\tau(n)^2\tau(N-n)\ll N L^9
$$

gives a total weighted error $O(NL^6\sqrt\eta+N^{3/4+o(1)})=O(NL^{-40})$: the original weight for fixed $(d,n)$ is at most $L\tau(n)$. Both cases have $H=o(L)$. This error is summed once, before forming any other subpieces.

Within each rectangle set $B=L^{1000}$. Truncating the square completion at $c\le B$ costs at most $O(NL^{70}B^{-1/2})$ per rectangle, even in the later tag-labeled variants: the $O(N/B)$ affected values of $N-n$ carry at most $L^2\tau(n)\tau(N-n)^2$, using the tag multiplicity and the square-completion tail, and Hölder $4,4,2$ and the fourth/eighth divisor moments apply. This bound is sufficiently small after the outer rectangle summation. At each retained squarefree $c$ with $(c,N)=1$, group the nonzero squarefree $d$ by $g=(d,c)$. Then $q=c^2d/g$ is injective on that group and the exact congruence is $mn\equiv N\bmod q$ whenever a later transfer writes the product $uv=mn$.

## 2. The individual transforms, with all finite unit masks

We use hard Perron at height $N^4$ on $\Re s=.51$, exactly as in R46, for a nonprincipal $\chi$ modulo a polynomial-sized modulus, whose primitive inducing character has conductor $f\le N^{.05}$. The [shifted prime estimate of R42](weak-s-type-ii-medium-prime-opposite-tags.md#1-the-long-transform-with-the-exact-wide-euler-exclusion) is $O(\sqrt Y L^3)$ for $\sum_{p\le Y}\chi(p)(\log p)p^{-i\tau}$, uniformly up to $|\tau|\le N^4$. Its zero input is only GRH for that inducing character; the finite imprimitive omissions cost $O(L)$ by their logarithmic weight. The [individual $L^{\pm1}$ bound of R40](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums) on this strip is $\exp(O(L/L_2))$. Any product of Euler factors at prime divisors of a polynomial-sized integer, including $N$ or $Ns$ for a tag $s$, costs at most $\exp(O(\sqrt L))$ in this contour estimate (split primes at $L$). At primes already killed by $\chi$ the factor is $1$.

In particular the hard $\mu(j)$-transform with $(j,W)=1$ for such a finite mask $W$ is $O(\sqrt Y N^{.02})$ at scale $Y\le N$. Its series is the inverse $L$-function with the inverse local factors at the primes of $W$. The exact non-squarefree Vaughan sequence with $(v,N)=1$ has series

$$
 L(s,\chi)\prod_{p\mid N}(1-\chi(p)p^{-s})\,
        \sum_{\substack{p^k>V\\p\nmid N}}(\log p)\chi(p)^k p^{-ks}.
 \tag{2}
$$

Here one marks divisibility by each prime power $p^k$ without excluding additional $p$'s in the unmarked part. For transforms of intervals below $N$ the marked powers can be restricted to $p^k\le N$, without changing a coefficient in those intervals. The terms $k\ge2$ on $\Re s\ge.51$ are absolutely bounded by $\sum_p(\log p)p^{-1.02}/(1-p^{-.51})<\infty$; for $k=1$ use the shifted prime estimate and partial summation above $V$, subtracting the $p\mid N$ terms at cost $O(L V^{-.51})$. Thus its hard transform is also $O(\sqrt Y N^{.02})$.

If the variable is squarefree, the actual Vaughan weight is instead marked by $\sum_{p>V,\ p\nmid N}(\log p)\chi(p)p^{-s}/(1+\chi(p)p^{-s})$ in the series

$$
      \frac{L(s,\chi)}{L(2s,\chi^2)}
        \prod_{p\mid N\ {\rm or}\ p\in\mathcal P}
                     (1+\chi(p)p^{-s})^{-1},
 \tag{3}
$$

where the optional $\mathcal P$ is an excluded tag band with least prime $S_0\ge L^{100000}$ and largest prime $N^{.001}<V$; take the union of the two prime masks, with no duplication. A prime $p>V$ is never a tag. The inverse factor at $2s$ needs no zero hypothesis because $\Re(2s)>1$. The linear log of the tag product is $O(L^5 S_0^{-.01})=o(1)$ by shifted prime partial summation; higher log terms are absolute. The denominator in the marked prime sum changes its linear term only by an absolutely convergent square tail. Again finite primes dividing $N$ cost the same harmless factor, including if some occur in $\mathcal P$. These estimates and hard Perron prove $O(\sqrt Y N^{.02})$ for (3) with its exact mark. The cell-prime transform at scale $T$, keeping $(s,N)=1$, is $O(\sqrt T L^2)$ by endpoint subtraction and discarding at most $O(L)$ primes dividing $N$. Thus multiplying an actual interval transform by a tag transform costs at most $\sqrt U N^{.03}$ at resulting scale $U$, as required by the low-conductor part of R45. No such bound is asserted or needed for larger primitive conductors.

## 3. The small moduli $d\le N^{.49}$: a separate two-leg estimate

This paragraph does not use squarefree support of the long variable or the large-modulus dispersion estimate. On a transferred-free rectangle take the actual $\alpha_u=\mu(u){\bf1}_{u\in I,(u,N)=1}$ and $\beta_v=L^{-1} b_{\rm II}(v){\bf1}_{v\in J,(v,N)=1}$, of respective lengths $O(U_0),O(V_0)$. At fixed $c,g$, the completed modulus $q$ is $O(N^{.49} B^2)$; allow all $q$ in each of its dyads after an absolute bound. Exact orthogonality on the actual units gives the principal plus the weighted nonprincipal sum of the product of their transforms. If $f$ is a nonprincipal primitive conductor and $q=fh$, the elementary weight bound

$$
     \varphi(q)\ge\varphi(f)\varphi(h),\qquad
        \sum_{h\asymp Q/f}\varphi(h)^{-1}\ll1
$$

bounds the total nonprincipal weighting for $f\le N^{.05}$ by $O(N^{.05})$, counting at most $\varphi(f)$ primitives per $f$. By (2) and the analogous Möbius estimate, the transform product is $O(XN^{.04})$, so this part is $O(N^{.59})$.

For $f>N^{.05}$, expand the two induction masks $(u,h)=(v,h)=1$ by Möbius divisor inversion. For mask divisors $r_1,r_2$, the reciprocal totient sum over $h$ divisible by $[r_1,r_2]$ costs $O(1/\varphi([r_1,r_2]))$, by [R44 §2](weak-s-type-ii-near-full-conductor-core.md#2-large-sieve-over-the-remaining-variable-part). Then Cauchy and the primitive multiplicative large sieve on $f\asymp F$ bound the product, with $1/\varphi(f)$, by

$$
  \ll \frac{X}{\sqrt{r_1 r_2}}
       \sqrt{(F+U_0/F)(F+V_0/F)} .
$$

Here the two coefficient norms are bounded by $O(\sqrt{U_0/r_1})$, $O(\sqrt{V_0/r_2})$ after dividing the indices by their mask divisors; the character factors at the divisors have modulus at most 1. The phase $\overline{\chi(N)}$ can be bounded by 1. The joint squarefree mask sum converges absolutely after the reciprocal totient weight, as in R44. Since $\max(U_0,V_0)\ll N^{.512}$, summing the dyads $N^{.05}\ll F\ll Q$ geometrically gives $O(X(Q+N^{.462}))=N^{.99+o(1)}$. Shift of interval support and the finite $N$ masks do not affect this large sieve.

For the principal here, $\sum_{u\in I,(u,qN)=1}\mu(u)\ll U_0 e^{-c_1\sqrt L}$ is the classical unconditional masked Mertens estimate of R40, at $U_0\gg N^{.488}$ with polynomial-sized mask $qN$. The other leg is trivial, and $\sum_{q\asymp Q}1/\varphi(q)\ll1$. Thus the principal is $O(Ne^{-c_1\sqrt L})$ per dyad, even without using modulus signs. Restoring $L$, and summing the polynomial-logarithmic square completion, dyads and rectangles, proves that the genuine small-$d$ portion is $O(N L^{-10})$, including the separately bounded square and slanted boundary errors. This estimate is valid even when there are no conductors above the low cutoff.

## 4. Larger $d$: incidence and character changes from the dyadic numerator

For $d>N^{.49}$, apply the [R46 argument, §§2–3](weak-s-type-ii-slanted-near-balanced-slab.md#2-the-extended-dispersion-estimate), with the following explicit range and mask details. The centered estimate is

$$
        \Delta\ll N L^6\sqrt{Q/U}+N^{1-\delta}
 \tag{4}
$$

for the transferred short and long scales $M,U$ and completed modulus scale $Q$. The enlarged range is $MU\asymp N,\ N^{.49}\ll Q\ll X e^H B^2,\ U\ll N^{.512+o(1)}$, with $Q/U=o(1)$. Indeed the high-character zero estimate of R45 still has factor $U/(QN^{.05})=O(N^{-.028+o(1)})$; the low estimate has $N^{.11}/Q=o(1)$. In the nonzero terms put $p=\log U/L,z_1=\log Q/L$. The exponents after the squared Cauchy factor are bounded by $1+(15/8)p$ and $23/20+(9/5)p-(3/20)z_1$, whose upper limits are $1.96$ and $1.9981$, before $30\kappa+\epsilon+o(1)$, $\kappa=10^{-5}$. The remaining terms and $1/N^\kappa$ large-gcd piece also retain power margin, with $\epsilon$ fixed small. No estimate from a wider range than the proven neighboring-tile Bettin–Chandee fallback is required.

In the smoothed centered variance, extending from the actual $(q,N)=1$ moduli to all $q\asymp Q$ is a nonnegative enlargement. The genuine long coefficients below are on squarefree integers $n>1$ with $(n,N)=1$, so $mn=N$ is impossible. Thus the large-gcd divisor-moment argument counts divisors of a genuinely nonzero $N-mn$, even in the smoothed ranges and for the enlarged moduli. The nonzero mixed term uses $(N,n_1)=1$ in the incomplete Kloosterman bound, exactly as in R45; this property is supplied by the long mask here, not by oddness alone. The constant-square term uses $\sum_{q\asymp Q}(Nh,q)\ll Q\,\tau(Nh)$ for nonzero $h$, which follows by divisor expansion for any $N$, and has the same $N^\epsilon$ loss. The reciprocal identities within the small-gcd tiles require only their previously enforced unit residues and the actual phases with numerator $N$. Thus the auxiliary all-$q$ variance does not impose $(q,N)=1$; it retains the termwise unit masks and the genuine long-variable coprimality just stated.

The principal in this range uses the actual $\mu(d)$. At fixed completion $c,g=(d,c)$ write $d=g e,\ q=c^2 e$. The restriction $(d,N)=1$ is now the extra $(e,N)=1$ in the [R43 signed reversal](weak-s-type-ii-doubly-untagged-signed-principal.md#1-signed-summation-of-the-principal-density). Reverse the coefficient sums; besides the fixed $c$-unit condition it leaves the mask $(e,2cNmn)=1$ and the exact hard interval in $e$. This mask is polynomial-sized, $e\asymp d/g\gg N^{.49-o(1)}$, and the masked harmonic Mertens estimate used there applies without any extra GRH. The principal remains $O(Ne^{-c_2\sqrt L})$ per coefficient piece before normalization.

## 5. Transfers, coprimalities and total cost

As in R46 use the direct argument if $\max(U_0,V_0)\ge D_0 L^{20000}$. A direct long $u$ carries the real $\mu(u)$ and the exact hard $(u,N)=1$ mask. If $v$ is larger, split $v=a^2 b$, $b$ squarefree, requiring both $(a,N)=1$ and $(b,N)=1$; discard $a>B$ with the same $O(N L^6 B^{-1/2})$ per-rectangle divisor-moment bound as R46. For $a\le B$, all prime-power parts of $v$ at primes dividing $a$ are at most $B^3<V$, so $b_{\rm II}(v)=b_{\rm II}(b)$ exactly. Use long $b$, short $a^2u$, keeping the exact $u$-unit mask. The product is unchanged and $Q/U\ll L^{4000-20000}$.

Otherwise use the single band $\mathcal P=[S_0,N^{.001}]\cap\mathbb P$, with

$$
       S_0=\exp(10^5(H+L_2)),\qquad \eta'=L^{-2000}.
$$

For both caps $S_0<N^{.001}$ eventually and $S_0\ge L^{100000}$. In the first occupied-cell transfer from $v$, take $v=s\ell$ with a prime label necessarily satisfying $(s,N)=1$. Thus the exact unit restriction passes from $v$ to $\ell$ on the short coefficient; the genuine $u$ with its unit mask and $(s,u)=1$ goes to the long $n=su$. The actual $v$ weight can be replaced by $b_{\rm II}(\ell)$ except on $s^2\mid v$, as in R46. Earlier-cell exclusions stay on $\ell$. The long transform is the product of the cell prime transform with the true unit-masked Möbius interval, plus the coprime correction from $s\mid u$ with $(j,Ns)=1$ in $u=sj$; the formula and sign are as in R46.

Among $v$ with no tag in the full band, move a tag $s$ from $u=s\ell$, with $(s,N)=1$ and $(\ell,N)=1$. Replacing $\mu(s\ell)$ by $-\mu(\ell)$ fails only on $s^2\mid u$. With the same $v=a^2b$ split and both $(a,N)=(b,N)=1$, take short $m=a^2\ell$, long $n=sb$. The no-tag mask and weight pass exactly to $b$ since $a\le B<S_0$, $B^3<V$. In particular $s\nmid b$, and $n$ is squarefree and coprime to $N$. The earlier-cell mask stays on the short $\ell$. Here the long transform is the cell prime sum times the hard unit-, tag- and squarefree-masked Vaughan transform of (3). In both directions labels $s\mid N$ do not occur in an original tuple, are not introduced by a freeze, and can be absent from a cell prime transform at the cost checked in §2. If a tag is excluded because it divides $N$ the original integer was already prohibited from having that factor; the exact no-tag condition continues to use the entire band.

The deterministic transfer comparisons are the R46 bounds, which use *pair counts and divisor moments*, not uniqueness of a solution of the complementary congruence. Specifically same-cell overcount affects a union of $O(N(\eta'+S_0^{-1})L_2)$ pairs in a rectangle, shared or repeated tags affect $O(N/S_0)$ pairs, and freezing a quotient interval at the cell left endpoint affects $O(\eta' N+\max(U_0,V_0))$ pairs, counted once across all label cells. In each case Cauchy with $\sum_{u,v}\tau(N-uv)^2\ll N L^9$ and weight/multiplicity $O(L^2)$ suffices. Dropping unit masks may only increase these errors. The square completion is applied after these comparisons. All modified short/long products are exact and the enlarged support still has $uv,N-uv\asymp N$. These errors and the square completion tails beat $NL^{-10}$ even after summing the entire outer grid.

On tag rectangles the failure of the direct test and $U_0V_0\asymp N$ give

$$
       D_0\gg X L^{-20000},\qquad
       X e^{-H} L^{-20002}\ll U_0,V_0\ll X e^H L^{20002}.
$$

The first transfer has $U\asymp T U_0$; the second has $U\asymp T V_0/a^2$. Hence in either $Q/U\ll e^{2H} L^{24004}/S_0$, and $U\le N^{.501+o(1)}$. In the direct case $U\le N^{.512+o(1)}$. The transformations of §2 verify the low-conductor input of (4) in both cases; a single tag representation introduces only the stated $\sqrt T L^2$ factor and the at most $O(T)$ coprime-correction terms in the first direction fit the $\sqrt U N^{.03}$ bound. The exact solubility masks $c,d,q$ from §1 are not lost. At reassembly the maximum overhead is $O(L^{5212})$, including $O(L^{202})$ outer rectangles, $O(L^{2001})$ tag cells when needed, $B^3$ for $a,c,g$, $O(L)$ $q$-dyads, up to $L^2$ normalization and $L^6$ in (4). Without tag cells it is $O(L^{3211})$. The displayed $Q/U$ gains, the fixed power errors in (4), and the signed principal bound then show that all these direct or tagged terms total $O(NL^{-10})$.

## 6. The unsigned term and the distinction between the two caps

Only the tag rectangles where both $u,v$ avoid $\mathcal P$ remain. The [R41 upper sieve](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich) applies because every geometric log band has uniformly bounded reciprocal mass and the factorial error is summable over all bands. Its divisor level stays $N^{.03}$ and each one-variable prime product is $O((H+L_2)/L)$. For a fixed actual $d$ keep $(d,N)=1$ and use the product upper sieve, dropping squarefree and $u,v$-unit constraints only for the unsigned upper bound, but keeping parity. A divisor pair with $(r_1r_2,d)>1$ is impossible since $N$ is a unit; otherwise use the same rectangular Weil main $|I||J|\varphi(d)/(4r_1r_2 d^2)$. Wider intervals can be divided into periods of length at most $d$, as in R46, at cost at most $e^{O(H)}L^{O(20000)}=N^{o(1)}$ in the Weil error. Summation of the error across all $d\le Xe^H$, two sieve indices and the grid gives $O_\epsilon(N^{.81+\epsilon+o(1)})$. The actual single-variable sieve density deletes primes of $\mathcal P$ dividing $d$; this changes its log product by $O(L/S_0)=o(1)$, uniformly in $d$.

For the principal area at fixed $d$, its $d$-cell is unique, the $u$-cells partition disjointly, and $|J|\ll N/u_0$ on every rectangle. The harmonic $u$-range on these tag rectangles costs $O(H+L_2)$ by the bounds above; the harmonic $d$-range costs the same. Hence $\sum |I||J|/d\ll N(H+L_2)^2$. There is no grid-count loss in this main term. The two sieve factors and the weight $b_{\rm II}\le L$ now give the total $O(N(H+L_2)^4/L)$. This is $O(NL_2^4/L)$ in the first case $H=10L_2$, and $O_\rho(NL^{4\rho-1})$ in the separate second case $H=L^\rho$. Together with all signed and boundary estimates this proves both statements.
