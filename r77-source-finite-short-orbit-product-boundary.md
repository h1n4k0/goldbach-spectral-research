# Finite short-divisor orbits at the below-square-root product boundary

Use the actual selected lower prime $s$, squarefree products $W,U$, upper split $V_X^2\le Z\le X^{\delta_0}$, both parities, and genuine typical exceptional count of $WU$ from the [growing-residual theorem](r75-source-dynamic-giant-growing-rough-residual.md). In particular the two fixed excluded neighborhoods stabilize the true count over the target window. As in the [singleton theorem](r76-source-below-square-root-singleton-carrier.md), $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\mathcal J=[X/2,(1+\Delta)X/2]$ and $\mathcal X=[X,(1+\Delta)X]$, with $\rho,\Delta$ as there. Write $n=hF$, $m=kG$, where $h=sWU$, $k=s'W'U'$ and $F,G$ are prime. The two operands are in $\mathcal J$ and on their genuine sum line $n+m=N$. Both are squarefree $N$-units. The true cutoffs $D_N=\lfloor\sqrt N\exp(-20T_N)\rfloor$, $Q_N=\lfloor N\exp(-20T_N)\rfloor$, $T_N=\log N/\log\log N$, all original tests $d>D_N,e>D_N,de>Q_N$, and the external minus sign are unchanged.

Fix parameters $a,b$ satisfying $0\le a,b<20$ and $a+b\le20$. The actual prime floors are

$$
              F\ge\sqrt N\exp(-aT_N),\qquad
              G\ge\sqrt N\exp(-bT_N).
 \tag{1}
$$

There is no added cap on the arities or largest primes of $U,U'$ and no fixed $h,k$ window in the stated selection. Denote the original signed sum at $I=I_0$ by $R_{N,Z}^{a,b}$.

**Theorem (unconditional).** Uniformly in the genuine split $Z$,

$$
      \sum_{\substack{N\in\mathcal X\\2\mid N}}
             |R_{N,Z}^{a,b}|^2\ll_{\rho,a,b}X^3\ell^{-1/5}.
 \tag{2}
$$

In particular this reaches the symmetric $a=b=10$ product boundary, with actual corrections indexed by more than the singleton. For example all but $O_{\rho,a,b}(X\ell^{-1/10})$ targets have magnitude at most $X\ell^{-1/20}$. This is a mean-square theorem for a prescribed carrier, not a pointwise bound, a theorem across $a+b>20$, an unrestricted no-giant theorem, or Hypothesis S.

## 1. The actual short orbits and the endpoint pair

Set $F_0=\sqrt X e^{-aT}$ and $G_0=\sqrt X e^{-bT}$. For fixed $a,b$ the two real floors in (1) increase across $\mathcal X$ for large $X$; each varies by $O(1)$ in logarithm. Work first with these fixed external lower floors, and restore the actual thresholds below. The prime $F$ on this fixed comparison is unique and largest: two prime factors at least $F_0$ would leave at most $O(e^{2aT})$ in $n$. The true exceptional count supplies a third prime exceeding $2V_X$, which is much larger than this; the two near-square-root primes themselves lie above the exceptional range. The same argument excludes a repeated $F$. The reflected comparison is identical with $b$. Each $h$ is composite since it contains $s$ and a prime of $U$. Also $F,G>D_N$ uniformly, since $a,b<20$ with the parameters fixed.

Write $d=h/r$ and $e=k/t$ for the labels not containing their distinguished prime. On each genuine fixed opposite long label $e>D_N$, the complete unrestricted $F$-containing orbit sums to $-\Lambda(h)=0$. Removing the labels that fail the curved test leaves exactly

$$
       \sum_{\substack{z\mid h\\Fze>Q_N}}
                      \mu(Fz)\log(h/z)
          =\sum_{\substack{z\mid h\\Fze\le Q_N}}
                      \mu(z)\log(h/z).
 \tag{3}
$$

There are no other excluded labels since $F>D_N$. The same identity holds on the $G$ side. In the containing-containing interaction the two unrestricted complete sums both vanish, and one must subtract the forbidden products; after the external minus this is **plus** the sum of their forbidden products with the two short signs. Thus the entire original pair mark is the following four terms:

$$
 \begin{split}
 &-\mu(h)\mu(k)
       \sum_{\substack{r\mid h,\ t\mid k\\d=h/r>D_N,\ e=k/t>D_N\\de>Q_N}}
                    \mu(r)\mu(t)\log(Fr)\log(Gt),\\
 &-\mu(k)\sum_{\substack{z\mid h,\ t\mid k\\e=k/t>D_N,\ (Fz)e\le Q_N}}
                    \mu(z)\mu(t)\log(h/z)\log(Gt),\\
 &-\mu(h)\sum_{\substack{r\mid h,\ w\mid k\\d=h/r>D_N,\ d(Gw)\le Q_N}}
                    \mu(r)\mu(w)\log(Fr)\log(k/w),\\
 &+\sum_{\substack{z\mid h,\ w\mid k\\(Fz)(Gw)\le Q_N}}
                    \mu(z)\mu(w)\log(h/z)\log(k/w).
 \end{split}
 \tag{4}
$$

This uses $\mu(h/r)=\mu(h)\mu(r)$ on squarefree support. In the second and third rows only the mate bears a full cofactor-parity sign. The finite orbit itself has the genuine short-divisor sign; it is not replaced by a singleton or claimed to have a full-parity saving.

All contributing $h,k$ are at least $H_-=\tfrac12\sqrt X e^{-20T}$. A long label $h/r$ requires $h>D_N$, and a short correction involving $Fz$ implies $Fz\le Q_N/(D_N+1)<\sqrt N$, hence $h\gg\sqrt X$. This also covers the fourth row because each opposite containing label is long. The upper bounds on $h,k$ on the fixed comparison are $(1+\Delta)X/(2F_0)$ and $(1+\Delta)X/(2G_0)$, respectively. Both log windows therefore have length $O_{a,b}(T)$. In the first row $rt<hk/Q_N\ll e^{(20+a+b)T}$. In a mixed row the ordinary mate removal is at most $k/D_N\ll e^{(20+b)T}$ or its reflection, and the short factor on the $F$ side is at most $Q_N/(F(D_N+1))\ll e^{aT}$ or its reflection. Consequently all labels we need in the first three rows are at most

$$
                         M=\exp((22+a+b)T).
 \tag{5}
$$

Since $Z\gg M$, each divides the corresponding $sW$. Its number of prime factors is bounded in terms of the fixed parameters, by the lower bound $\exp(5T/4)$ for every prime. The actual lower count cap consequently gives only $(1+\log\ell)^{O_{a,b}(1)}$ enumerated labels per operand. The unit correction remains individually $O_A(XL^{-A})$ for every $A$, even with all these labels: any common prime divides $N$, there are $O(\ell)$ eligible primes of $N$ and $O(X/p)$ possible first operands for each $p\ge\exp(5T/4)$.

The last row of (4) is empty on the fixed comparison if $a+b<20$, since then $F_0G_0=Xe^{-(a+b)T}>Q_N$ for all large $X$. At the endpoint $a+b=20$ the ratio $Q_N/(F_0G_0)$ is bounded uniformly. The last test then forces $z=w=1$ as any other factor is $\ge\exp(5T/4)$. It also forces both prime coordinates into fixed log-width-$O(1)$ slivers from their external lower floors. This gives a small positive comparison in §3 despite the absence of either full-parity sign. In particular we do not silently discard the equality case on the curved boundary.

## 2. Fourier estimates for the compound orbit

Use the fixed arithmetic carrier above, with separate leg-dependent prime floors and fixed $h,k$ windows, and keep every old true factor, count, size and exceptional-band selector. Ordinary label polynomials are those of the singleton theorem with the new bound $M$ and the fixed cofactor and prime windows. An orbit polynomial has actual marks

$$
          \mu(z)\log(h/z),\qquad z\mid sW,\ z\le M,\qquad
                              \log(Fz)\in J ,
 \tag{6}
$$

where $J$ is a fixed hard log bin and $hF\in\mathcal J$ as always. Its positive version replaces $\mu(z)$ by $1$. The orbit coordinate is the genuine product $Fz$, not the prime $F$ alone. In this section all real-band comparisons are of these actual integer polynomials.

Let $B$ be a bound for the logarithmic width of each relevant $h$ interval at a fixed physical real $x\in\mathcal J$ and fixed divisor label. For an ordinary label bin or an orbit bin of width $\Omega=L/\ell^2$, take $B=\Omega$. For a positive all-label polynomial restricted to a prime sliver of log width $O(1)$, take $B=O(1)$; for the full positive polynomial take $B=O(T)$. The fourth norms used below are bounded by

$$
 \begin{array}{ll}
  O(X^{3/4}\{(\ell B/L)\ell^{-1/10}+\ell/L\})
       &\text{for an ordinary signed label},\\
  O(X^{3/4}\ell(B+1)/L)
       &\text{for any positive comparison or either orbit version}.
 \end{array}
 \tag{7}
$$

The constants can depend on $\rho,a,b$. We verify both the new minor separation and the new real prime-band constraint, retaining the old signed mate argument.

**Exact minors.** Use the same reduced Dirichlet arcs, with $P=L^C$, denominators at most $P$ and upper approximation limit $\lfloor X/P\rfloor$, as in the singleton theorem. Dyadically split the two variables $h,F$, keeping only rectangles that meet $hF\in\mathcal J$. Both variables are below $X^{.6}$ and the product of their dyadic sizes is $\asymp X$. The true hard physical window is separated by the same truncated half-integer Perron integral on integer $hF$. For (6) additionally separate each of the two true endpoints of the **integer product $Fz$** by a second half-integer Perron integral. Open or closed real endpoints are converted to the corresponding strict half-integer tests on integers separately. The twists from this second integral are $F^{-\sigma-iv}$ and $z^{-\sigma-iv}$ with $\sigma=1/L$. The latter stays inside the $h$-divisor coefficient. They do not create a new independent summation variable in the bilinear estimate. The mark $\log(h/z)$ is already in that coefficient.

To bound the truncation errors, take height $X^4$ in both integrals. On the relevant rectangles all products $hF$ and $Fz$ are $O(X)$ for large $X$ (indeed $Fz<X^{.7}$). Comparable thresholds have a log gap $\gg X^{-1}$ from a half-integer to an integer product, and noncomparable thresholds only improve the gap. The real Perron powers are bounded by a constant since the ratios are polynomially bounded. Thus the errors are $O(X^{-3})$ per product test, and multiplying two approximations costs the sum of their errors up to a constant, since each approximates a zero-one indicator. The sum of these errors is negligible even after all allowed labels, weights and dyads. The two separated integral kernels cost $O(L^2)$ rather than $O(L)$; the bin endpoints remain genuinely hard.

In the separated bilinear form the product of coefficient bounds is $O(L(1+\log\ell)^{O(1)})$, unchanged by either twist. The reciprocal-distance bound of the singleton proof for reduced $P<q\le X/P$ then gives a minor supremum $O_K(XL^{-K})$ for any fixed $K$, choosing $C$ sufficiently large to absorb both Perron integrals and the dyadic count. The actual coefficient energy is $O(XL^2(1+\log\ell)^{O(1)})$ by unique $n=hF$ and the pointwise label count. Therefore the actual minor fourth norms save any fixed inverse log power required by (7). For ordinary label polynomials, the same argument uses only the first product integral and the coefficient split for $\log F+\log r$.

**Exact majors.** For fixed actual $h,z$, the gate $Fz\in\exp(J)$ is a hard interval in the prime $F$. Apply ordinary Siegel–Walfisz only in $F$, with this interval, the fixed floor, and the physical window $\mathcal J/h$. The phase and the logarithmic prime weights are handled by partial summation exactly as in the singleton theorem. At a reduced numerator over $q\le P$, the rational factor is $\mu(q)/\varphi(q)$ since every prime divisor of $h$ exceeds $P$. The real density in physical $x$ has a factor $1/h$ and the real orbit mark

$$
             \frac{\log(h/z)}{\log(x/h)} .
$$

It is supported by the exact interval $\log h\in\log x+\log z-J$, intersected with the fixed $h$ window and the real prime-floor interval. On the ordinary branch the mark is $1+\log r/\log(x/h)$ and the interval is the fixed $h$ window and log label test, intersected with the same real prime-floor interval. For a prime sliver there is an additional fixed prime band $F\in\mathcal F$, corresponding to $\log h\in\log x-\log\mathcal F$. All these real marks are uniformly bounded with bounded variation in $h$, and their $x$ derivatives are $O(1/X)$ for fixed $h$.

For each fixed $s,W$ and divisor label, use the growing-residual theorem's reciprocal prime-product replacement for $U$ with its exact remaining tag set $K$. The variable $\log U/L$ stays in $[.4,.6]$; its normalized count-restricted continuum density in either parity has uniform supremum and Lipschitz bound $O(\tau^{-1})$, $\tau=\log Z/L$, with arbitrary inverse logarithmic replacement error. No gate here changes a prime alphabet in $U$. The lower labeled reciprocal profile is $O(\ell\tau)$: each choice of a short divisor is covered by doubling the prime weight on $[\exp(4T),M]$, a fixed log-ratio band of bounded reciprocal mass, and at most two choices for the old prime $s$. The continuous density size is therefore $O(\ell B/L)$ in all positive comparisons, including the orbit. This argument also bounds the reciprocal size of the discrete label sums required in Siegel–Walfisz; all accumulated uniform approximation errors on a major arc are $O_A(XL^{-A})$ for every fixed $A$ after accounting for its fixed polylogarithmic denominator scale.

For the ordinary signed mate, split out the untagged factors of $W$ in $[\exp((23+a+b)T),V_X/4]$, above every enumerated divisor label. For fixed remaining factors and label, neither the actual tag set $K$ nor the integration domain in $\log h$ depends on those split factors. The growing-residual theorem's signed low-product argument thus applies literally: replacing the count cap in the real density loses a relative $O(\ell^{-(2\log2-1)})$, the Lipschitz argument shift and the hard size strip have errors $O((1+\Delta_0)/L)$ with $\Delta_0=3(\log\ell)\log V_X$, and the resulting independent signed Euler ratio is $O(\ell^{-1/10})$. These comparisons can be applied at each physical $x$ even with the prime-floor endpoint, because that endpoint only uses $h,x$. They yield size $O((\ell B/L)\ell^{-1/10})$ and the same bound for the scaled derivative of the real mark on a fixed log interval.

After replacing by the real continuum, variation in $x$ is estimated exactly as in the singleton argument. For each fixed label, changing $x$ to $y$ moves any real prime-band endpoint in $\log h$ by $|\log x-\log y|$; the normalized symmetric difference of clipped intervals is $O(|\log x-\log y|/L)$. This is also true with both the orbit band and the floor present, since their intersection is a fixed prime interval after $z$ is fixed. Bound endpoint variation positively by $O(\ell|\log x-\log y|/L)$; on the common part use the prior signed or positive estimate for the difference of the real marks divided by $|x-y|/X$. Thus total variation is bounded by the asserted supremum scale plus $O(\ell/L)$, without differentiating a discrete prime trace. The uniform replacement errors are integrated directly. The real transform on each arc then has the indicated bound times $\min(X,|\beta|^{-1})$, with $\beta$ the arc offset. The fourth mean uses $\int_{\mathbb R}\min(X,|\beta|^{-1})^4d\beta=O(X^3)$ and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$. The errors are negligible on the major measure $O(P^2/X)$. This proves (7) including the compound orbit.

## 3. True seams, prime-floor slivers and endpoint

For the first row of (4), use the ordinary log-label bins of width $\Omega=L/\ell^2$. There are $O(\ell)$ on each leg. The ranges of $\log D_N,\log Q_N$ have width $O(1)$ over the scale, including the literal floors. The two coordinate cuts and the diagonal cut therefore yield only $O(\ell)$ ambiguous bin pairs; for the latter each first bin meets at most a fixed number of possible opposite boundary bins. Accepted rectangles consist wholly of actual accepted label pairs for every target, rejected ones of none, and ambiguities are bounded only positively. The signed fourth norms in (7) are $O(X^{3/4}\ell^{-1-1/10})$ per bin, and positive ones are $O(X^{3/4}\ell^{-1})$. Parseval and Hölder, summed over $O(\ell^2)$ accepted and $O(\ell)$ ambiguous pairs respectively, give $\ell^2(N)$ norms $O(X^{3/2}\ell^{-1/5})$ and $O(X^{3/2}\ell^{-1})$.

For the second row bin the actual $\log(Fz)$ against $\log e$ with the same width. The short-orbit label lies between the fixed lower floor of $F$ and $\sqrt{(1+\Delta)X}$ on active support, since $e>D_N$. This is $O(T)$ in log. The genuine conditions are $e>D_N$ and $(Fz)e\le Q_N$, with the weak curved test inherited from (3). The same grid has $O(\ell^2)$ possible accepted and $O(\ell)$ ambiguous pairs. An accepted coefficient is the convolution of the actual orbit polynomial with an ordinary signed mate, times the external minus. The polynomial lengths and signs are those in (4) and (6), not an average model. Use one ordinary signed fourth norm and one orbit fourth norm in (7), giving $O(X^{3/2}\ell^{-2-1/10})$ per accepted pair in $\ell^2(N)$. The ambiguous pairs admit the two positive estimates and cost $O(X^{3/2}\ell^{-1})$ altogether. Hence the second row has norm $O(X^{3/2}\ell^{-1/10})$, and the third follows by reflection. Strict and weak boundary equalities are handled by including the applicable bin pair in ambiguity, never by discarding its integer terms.

To restore (1), a difference requires one prime in a fixed log-width-$O(1)$ sliver beginning at its external lower floor. The absolute label sums in (4) are controlled on that side by the positive all-label polynomial in the sliver, because $\log(h/z)\ll\log F$ and the same cap $M$ enumerates the short labels as well. Use the whole opposite positive all-label polynomial. The fourth norms in (7) have scales $X^{3/4}\ell/L$ and $X^{3/4}$ respectively, giving an error $O(X^{3/2}\ell/L)$ in $\ell^2(N)$. In the remaining fourth row at $a+b=20$, the $z=w=1$ terms are controlled by this same positive comparison, since their prime coordinates lie in such fixed slivers by §1. Thus there is no loss from the exact product boundary or possible equality. The individually negligible unit corrections can also be included. The combined norm is $O(X^{3/2}\ell^{-1/10})$, proving (2).

## 4. A non-singleton occupied example at the endpoint

Take $a=b=10$ and $Z=V_X^2$. Choose two distinct primes $F,G$ near $\sqrt X e^{-5T}$ and two distinct old lower primes $s,s'$ near $e^{3T/2}$. Take $W=1$ on the first side and $W'=p$ with one prime near $e^{24T}$ on the second. That prime is in the true old untagged range below $Z$ for large $X$. On each leg choose the same number $\lfloor(1-\theta)\log\ell\rfloor$ of distinct upper tagged primes near $\exp(3T\ell^\theta)$ and two more free primes of size $X^{1/4+o(1)}$, adjusting the second by the PNT so that $hF,kG$ lie strictly inside $\mathcal J$. The product of the tagged factors has log size $o(L)$, so all these prime choices can be made in fixed proportional windows with distinct primes throughout. They give true central units and an even target in $\mathcal X$. The genuine floors (1) hold with a margin, and both primes are below $\sqrt N$.

The mate $e=k/p$ has $\log(e/\sqrt X)=-19T+O(1)$, so $e>D_N$ and both $F e$ and $F s e$ fail the strict product test. The short orbit against it has exactly $z=1,s$, hence the actual residual is $\log h-\log(h/s)=\log s$ before mate weighting. The mate $k/(s'p)$ fails $D_N$, while $k,k/s'$ give no correction. There is no reflected correction since the first side has only $1,s$ as possible ordinary omitted labels. The ordinary row keeps both of its labels against $t=1,s',p$. Also $\mu(h)\mu(k)=-1$ by the equal upper arity and the extra prime $p$. Since $FG>Q_N$ in this example, the exact total mark is

$$
       \log s\log s' + (1+\mu(k))\log s\,\log(Gp)>0 .
$$

All of these tests are stable under the target-dependent cutoffs and their floors because the margins are exponential in $T$. This is a genuine occupied non-singleton correction, not a lower bound for the total mean.
