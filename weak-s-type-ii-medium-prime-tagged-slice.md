# A signed tagged-prime slice of the balanced medium-prime remainder

**Conditional on global Dirichlet GRH.** Keep $N=2^j,\ X=\sqrt N,\ L=\log N$, the exact box $I=[.740X,.745X]$, $J=[.715X,.720X]$, $D=[.445X,.450X]$, and the actual [medium-prime weight](weak-s-type-ii-medium-prime-character-shells.md)

$$
 w(v)=\sum_{\substack{N^{.024}<p\le N^{.2499}\\p\ {\rm prime},\,p\mid v}}\log p.
$$

Put $S=N^{.01}$, and let $T_S(u)$ indicate the existence of a prime $s\in[S,2S]$ dividing $u$. On the same precise $N/2<uv\le9N/16,\ k=(N-uv)/d>\sqrt N,\ (uv,N)=1$ geometry, the signed term

$$
 {\cal B}=\sum_{\substack{u\in I,\ v\in J,\ d\in D\\
 u,v,d\ {\rm odd},\ uv\equiv N\bmod d}}
  T_S(u)\,\mu(u)\mu(d)\,\mu^2(v)\mu^2(N-uv)\,w(v)
$$

is $O(N/L)$, uniformly on replacing $I,J,D$ by arbitrary subintervals. On the full boxes the sum of absolute values of these very terms has order $N$, **unconditionally**; see §4. This is thus signed cancellation on a genuine arithmetic slice of the old medium-prime remainder, retaining both Möbius signs and all medium primes $p$. It is not a bound for $v$ nonsquarefree, for untagged $u$, the full signed remainder, or weak S.

## 1. Deterministic tag, ratio, and squarefree errors

Since $|J|<d$, for each $d,u$ at most one $v$ is possible (if $(u,d)>1$ none is possible, since $N$ is a power of two and $d$ is odd). The analogous assertion holds interchanging $u$ and $v$. Replace $T_S(u)$ by the sum over prime tags $s\in[S,2S]$ dividing $u$. The discrepancy is bounded by the number of pairs of distinct tags. There are at most $X/(s_1s_2)$ eligible $u\le X$ per pair, at most $X$ choices of $d$, and $w(v)\le L$. Thus the error is $O(N/L)$ by $\sum_{S\le s\le2S}1/s\ll L^{-1}$ over primes, from the prime number theorem (or Chebyshev). No random-tag assumption is used.

Discard $s\mid v$, at cost $O_\epsilon(N^{1+\epsilon}/S)$: for each $s$ the counts of $u,v$ divisible by $s$ are each $O(X/s)$, and there are at most $\tau(N-uv)\ll_\epsilon N^\epsilon$ choices of $d$. Use $w\le L$ and absorb logarithms. Set $u=sm$; its signed factor is exactly $-\mu(m){\bf1}_{s\nmid m}$. Removing that last mask costs $O(NL/S)$, by $u$ divisible by $s^2$, $d$-count $O(X)$, and uniqueness of $v$. Choose the small fixed $\epsilon$ below .01.

Subdivide $[S,2S]$ into intervals of relative ratio at most $1+\eta$, $\eta=L^{-10}$. On each block with left endpoint $s_0$, replace the exact interval $m\in I/s$ by $m\in I/s_0$. A mismatch has $u=sm$ within $O(\eta X+1)$ integers of the two original endpoints. A given $u$ near this range has only $O(1)$ tags $s\ge S$ by the product bound. For each such tag and $d$ there is again at most one $v$. The total error is $O(LX(\eta X+1))=o(N/L)$. The boxed inequalities for $uv,N-uv,k$ have fixed proportional margin, so they still hold on any enlarged support for large $N$.

Now complete $\mu^2(N-uv)=\sum_{b^2\mid N-uv}\mu(b)$, truncating at $B=L^{J_1}$ for a sufficiently large absolute $J_1$. The usual tail bound $O(NL^C B^{-1/2})$ follows because the $O(N/B)$ eligible values of $n=N-uv$ contribute at most $O(L\tau(N-n)\tau(n)^2)$ each (bounded tag multiplicity), and by Hölder exponents $4,4,2$ with fixed divisor moments. Thus this costs $o(N/L)$. The freezes above were performed before square completion.

## 2. A centered neighboring-tile estimate

Here is the precise variation of the [near-balanced pointwise estimate](weak-s-type-ii-wright-near-balanced.md) needed below. Let $a=N$, $U\asymp N^{.51}$, $M\asymp N^{.49}$, $MU\asymp N$, $N^{.4974}\le Q\le N^{.5001}$; the implied scale constants are fixed. Let real $|\alpha_m|,|\beta_n|\le1$ have dyadic supports of scales $M,U$ respectively, with $\beta_n$ supported on odd squarefree $n$. Assume, for every fixed $\epsilon>0$, uniformly for nonprincipal characters modulo $q\asymp Q$,

$$
 \left|\sum_n\beta_n\chi(n)\right|\ll_\epsilon N^\epsilon\sqrt U. \tag{1}
$$

There is **no** assumption on the principal sum. For $\kappa=10^{-5}$, the following centered bound then holds:

$$
 \sum_{\substack{Q\le q<2Q\\(a,q)=1}}
 \left|\sum_{mn\equiv a\bmod q}\alpha_m\beta_n
 -\frac{1}{\varphi(q)}
      \Big(\sum_{(m,q)=1}\alpha_m\Big)\Big(\sum_{(n,q)=1}\beta_n\Big)\right|
 \ll N^{1-\kappa/3}. \tag{2}
$$

To check the modification, let $\psi$ be the same nonnegative smooth majorant as in the earlier estimate (supported in $[1/2,5/2]$, equal to 1 on $[1,2]$). Write $B_{q,\delta}=\sum_{n\equiv\delta(q)}\beta_n$ and $C_q=\varphi(q)^{-1}\sum_{\delta\bmod q}^* B_{q,\delta}$. Cauchy on the original units, followed by *positive* all-modulus extension of the variance, bounds the left side squared by $O(MQ\,W)$, where

$$
 W=\sum_q\psi(q/Q)\sum_{\delta\bmod q}^*
       |B_{q,\delta}-C_q|^2\sum_{m\equiv a\bar\delta(q)}\psi(m/M).
$$

At the original good moduli the substitution $m\mapsto a\bar m$ permutes the units. At added bad moduli the displayed expression is simply nonnegative; it is not a replacement for the original congruence there.

Use Poisson in $m$ with $H=(Q/M)N^\kappa$ and retain nonzero $|h|\le H$, with negligible Schwartz tails. The exact zero mode of this centered variance is $O_\epsilon(N^\epsilon MU)$: orthogonality in $\delta$ uses (1) on nonprincipal characters only. For the nonzero mode from $|B_{q,\delta}|^2$ we use precisely the bounds (3) and (6) of the near-balanced note, with the all-$g$ zero mode removed. That proof uses only $|\beta_n|\le1$, squarefree odd $n$, and, on dropping the large-gcd tail, $mn-a\ne0$; the latter holds here since $n$ is odd and $a=N=2^j$. In detail, replacing the original and Poisson zero-frequency large-gcd portions by the $g=(n_1,n_2)\le N^\kappa$ portions together costs $O_\epsilon(N^\epsilon(MU+MU^2/(QN^\kappa)))$. The nonzero small-gcd part is bounded by

$$
 N^{30\kappa+\epsilon}
  \left(Q^{-1}U^{23/8}
         +M^{3/20}U^{59/20}Q^{-23/20}N^{-.0036}\right);
$$

squarefree $n_i$ is exactly what ensures $(g,n_i/g)=1$ in the switched neighboring tiles. This part is unchanged by centering.

For the two new nonzero terms, the constant-square part $|C_q|^2$ has inner complete sum $c_q(ah)$ (a Ramanujan sum). Since $|C_q|\ll U/\varphi(q)$ and $\sum_{q\asymp Q}(ah,q)\ll_\epsilon QN^\epsilon$ uniformly for $1\le|h|\le H$, its size is $O_\epsilon(N^{\kappa+\epsilon}U^2/Q)$. The gcd sum follows from expanding the gcd by $\varphi(r)$ over $r\mid ah$ and counting multiples in the support $q\le (5/2)Q$.

For the cross part $B_{q,\delta}\overline{C_q}$, summing over $n_1,n_2\asymp U$ leaves an inner $q$-sum with factor

$$
 \frac{1}{q\varphi(q)}\psi(q/Q)\widehat\psi(hM/q)\,
          e(ah\overline{n_1}/q),\qquad (q,n_1n_2)=1 .
$$

As in [Fouvry–Radziwiłł, §3.3 and Lemma 2.4](https://arxiv.org/html/1812.00562v2#S3.SS3), by reciprocity the oscillation is $e(-ah\overline q/n_1)e(ah/(n_1q))$. Pull out $Q^{-2}$, keeping $q/\varphi(q)$ in the inner sum. The remaining smooth part costs $O(N^\kappa)$ in partial summation since $HM/Q$ and $aH/(UQ)$ are $O(N^\kappa)$. The resulting incomplete Kloosterman sum modulo $n_1$, with $q/\varphi(q)$ weight and $(q,n_2)=1$, is $O_\epsilon(N^\epsilon U^{1/2}(h,n_1)^{1/2})$: use the cited lemma on the interval of length $O(Q)<n_1$ and $(a,n_1)=1$. The lemma's weight can equivalently be handled by $q/\varphi(q)=\sum_{r\mid q}\mu^2(r)/\varphi(r)$, inclusion–exclusion for $n_2$, and Fourier completion on each resulting progression. Summing the gcd bound over $1\le|h|\le H$ costs $O_\epsilon(H N^\epsilon)$, by divisor expansion. The full cross error is therefore $O_\epsilon(N^{2\kappa+\epsilon}U^{5/2}/Q)$, including the outside factor $M$ of Poisson and $H=(Q/M)N^\kappa$.

After multiplying by $MQ$, both new exponents are less than $1.77+2\kappa+\epsilon$ (respectively $1+.51$ and $1+1.5(.51)$). The zero, large-gcd and inherited trilinear terms satisfy the same upper exponents as in the earlier estimate, in particular $O(N^{2-2\kappa/3})$ on choosing $\epsilon$ small. This proves (2) with all constants uniform on the indicated scales.

## 3. Apply the centered estimate after moving the actual tag

For each ratio block after §1, let $n=sv$. The long coefficient is

$$
 \beta_n=\frac1{100 L}
  \sum_{\substack{s\mid n,\ s\ {\rm prime\ in\ block}\\v=n/s\in J,\ v\ {\rm odd}\\(v,s)=1}}
          \mu^2(v)\,w(v).
$$

The extra fixed normalization ensures $|\beta_n|\le1$ since $n\ll N^{.51}$ has at most 52 prime divisors $\ge N^{.01}$ for sufficiently large $N$; $\beta_n$ is supported on odd squarefree integers on one dyad at scale $U\asymp XS$. The short coefficient is $\alpha_m=-\mu(m){\bf1}_{m\in I/s_0,\ m\ {\rm odd}}$, supported on one dyad at scale $M\asymp X/S$. Both are independent of $d$. At fixed odd $b$, group the nonzero squarefree $d$ by $g=(b,d)$, taking $q=[d,b^2]=b^2d/g$, injective within each group. The exact two divisibilities become $mn\equiv N\bmod q$. Here $q$ is odd, so good, with all relevant dyads $Q=N^{.5+o(1)}$ in (2). Any omitted $q$'s or $\mu(d)$ factors of modulus ≤1 cause no loss in the $q$-absolute bound there; the conditioned principal terms are treated separately.

To see (1) under global GRH, for a nonprincipal $\chi$ the Dirichlet series of the true squarefree $v$-weight is

$$
 \sum_v\frac{\mu^2(v)w(v)\chi(v)}{v^z}
 =\frac{L(z,\chi)}{L(2z,\chi^2)}
       \sum_{N^{.024}<p\le N^{.2499}}
          \frac{(\log p)\chi(p)p^{-z}}{1+\chi(p)p^{-z}},
 \tag{3}
$$

where the inner sum is over primes. The prime polynomial without the denominator is $O_\epsilon(N^\epsilon)$ on $\Re z\ge1/2+\delta$ at polynomial height, by the height-uniform twisted prime estimate and partial summation on the real weight, as justified in [the character-shell note, §3](weak-s-type-ii-medium-prime-character-shells.md#3-uniform-global-grh-sparse-family-estimate). Restoring the denominator changes it by $O_\delta(1)$ since $\sum_p(\log p)p^{-1-2\delta}<\infty$. Under GRH $L(z,\chi)$ is subpower there, and $1/L(2z,\chi^2)$ is absolutely bounded for fixed $\delta>0$. Exact Perron on half-integer endpoints (height $N^4$, shift to $1/2+\delta$ with $\delta$ small) therefore gives the bound $O_\epsilon(N^\epsilon\sqrt X)$ for the squarefree $v$-sum on $J$. The same proof, uniformly for $s$ in our tag block, bounds the sum of $\mu^2(\ell)w(\ell)\chi(\ell)\mathbf1_{(\ell,s)=1}$ on $J/s$ by $O_\epsilon(N^\epsilon\sqrt{X/S})$: the only extra factor in (3) is the inverse Euler factor $1/(1+\chi(s)s^{-z})$, since $s<N^{.024}$ is outside the medium prime range. All input moduli $\asymp Q$ and heights are polynomial, and the arguments apply to imprimitive nonprincipal characters as well.

Without the $(s,v)=1$ mask the β transform factors, and $|\sum_{s\ {\rm in\ block}}\chi(s)|\ll_\epsilon N^\epsilon\sqrt S$ by the same GRH prime estimate (partial summation dividing by $\log s$). The correction from $s\mid v$ replaces $v$ by $s\ell$, with $\mu^2(v)=\mu^2(\ell){\bf1}_{(\ell,s)=1}$ and $w(v)=w(\ell)$, as $s$ is not medium. Summing the bound $N^\epsilon\sqrt{X/S}$ over $O(S)$ values costs at most $N^\epsilon\sqrt{XS}$. Dividing by $100L$ and taking $U\asymp XS$ proves (1). The principal β sum need not cancel at all.

For the principal comparison in (2) use the actual $\alpha_m$: the global-GRH coprime Mertens bound on its sharp interval is $O_\epsilon(N^\epsilon\sqrt M)$ (mask $2q\le N^{O(1)}$), and $|\sum_{(n,q)=1}\beta_n|\ll U$. Hence the entire dyad of the principal comparison is $O_\epsilon(N^\epsilon\sqrt M\,U)=O_\epsilon(N^{.755+\epsilon})$. The centered term has the power bound (2). Reinstating $100L$, along with only polynomially many in $L$ ratio blocks, $b,g$ groups and dyads, gives $o(N/L)$ for the whole truncated, retagged correlation. The explicit errors in §1 now establish ${\cal B}=O(N/L)$.

## 4. Actual occupancy: the unsigned mass has order $N$

This section uses no GRH. For the lower bound count incidences with the same tags $s\in[S,2S]$, with an additional prime $p\in[N^{.10},N^{.11}]$ dividing $v$, and require squarefree $u,v,N-uv$ and odd squarefree $d$, as in the actual sum. This $p$ is in the medium range. Each $u,v$ has $O(1)$ possible $s,p$ and $w(v)\ge .10 L$ when it has such a $p$. It suffices to show that this count is $\gg N/L$.

Complete the three squarefree indicators at $a^2\mid u,\ f^2\mid v,\ b^2\mid N-uv$, cutting all completion variables at $B_0=N^{10^{-5}}$. The tail costs $O_\epsilon(N^{1+\epsilon}/B_0)$ by the same elementary incidence counts as in the [occupied-diagonal note](weak-s-type-ii-exactly-balanced-diagonal.md#1-exact-support-and-a-squarefree-counting-lemma): for a bad $u$ or $v$ there are $O(X/B_0)$ choices, $O(X)$ of the other, and at most $\tau(N-uv)$ of $d$; for bad $m=N-uv$ there are $O(N/B_0)$ values and at most $\tau(N-m)\tau(m)$ choices of $u,v,d$. All square-divisor weights cost $N^\epsilon$ and tag multiplicities are bounded. Since $B_0<S<p$, $u=s a^2 u_1,\ v=p f^2 v_1$ with $u_1,v_1$ odd are exactly the retained divisibility conditions. For $q=[d,b^2]$, discard $(s p a f,q)>1$; otherwise $u_1v_1\equiv N\overline{s p a^2 f^2}\bmod q$. The rectangular Weil completion (same cited note, formula (4), including parity) gives main term

$$
 \frac{|I||J|}{4sp}\frac{\varphi(q)}{a^2 f^2 q^2},
 \qquad\text{and error }O_\epsilon(q^{1/2+\epsilon}).
$$

Here $q\ll XB_0^2$; summing over $d,s,p,a,f,b$ gives total error $O_\epsilon(N^{.87004+\epsilon})$, since the number of choices is $O(X N^{.01} N^{.11}B_0^3)$.

For the main, $(sp,q)=1$ here is simply $(sp,d)=1$, because $b\le B_0<S$. Extend the retained main-coefficient sums in $a,f,b$ to the three unrestricted squarefree sums with only $(af,[d,b^2])=1$ (and odd variables). The extension error, after factoring out $|I||J|/(4sp)$, is $O_\epsilon(N^\epsilon/(d\sqrt{B_0}))$ by Rankin with a half-power on each tail, as in the occupied-diagonal note: the $a,f$ tails have square-decay; the $b$-local multiplier for a prime $\ell$ is $1/\ell$ if $\ell\mid d$ and $1/\ell^2$ otherwise. This extends an absolutely convergent main-coefficient model, not an assertion of the same exact divisibility substitution for variables beyond $B_0$.

At each odd prime $\ell\mid d$, $a,f$ cannot use $\ell$, and the $b$-choice yields $1-1/\ell$ on top of the initial factor $\varphi(d)/d^2$. At $\ell\nmid d$, either $\ell\nmid b$ and the two independent square choices give $(1-\ell^{-2})^2$, or $\ell\mid b$ and neither $a$ nor $f$ can use $\ell$, contributing $-(1-\ell^{-1})\ell^{-2}$. Their sum is $1-3\ell^{-2}+\ell^{-3}+\ell^{-4}$. All factors are positive, so the resulting main coefficient is $\gg d^{-1}(\varphi(d)/d)^2$. As before a positive proportion of the odd squarefree $d\in D$ have $\varphi(d)/d$ bounded below (average the reciprocal sum over prime divisors and apply Markov). Uniformly in such $d$, dropping $s\mid d$ or $p\mid d$ changes the two reciprocal prime sums by at most $O(1/S)$ and $O(N^{-.10})$ respectively, since $d=O(X)$ has only $O(1)$ such prime divisors. The remaining $s,p$ sums are $\asymp L^{-1}$ and $\asymp1$ respectively by the prime number theorem. Thus the total positive main is $\gg N/L$, and all square, Fourier, and Rankin errors are $o(N/L)$. This proves the claimed lower bound for occupancy. The upper bound for the unsigned sum is $O(N)$ directly, from the $O(X\sum_s1/s)$ tagged $u$, the $O(X)$ possible $d$, uniqueness of $v$, and $w(v)\le L$.
