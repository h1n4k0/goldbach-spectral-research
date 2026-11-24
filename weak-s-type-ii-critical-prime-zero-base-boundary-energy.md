# Sharp physical and divisor edges in the zero-base even-lattice shell

**Scope.** This is an unconditional boundary estimate for the actual critical-prime Type II correlation. It keeps both unit conditions and the genuine signs. All sharp physical and divisor endpoints in a fixed proportional complementary divisor range can be smoothed at arbitrary fixed inverse-logarithmic relative widths, at signed cost $o(N)$, after exact parity-preserving zero-base compensation. The dense interior of the resulting even-lattice residual is not estimated.

## 1. Actual coefficients and boundary estimates

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and fix $C>1$. Use the genuine integer polynomials $P,D$ of the [critical-prime setup](weak-s-type-ii-critical-prime-least-prime-boundaries.md), with $I_d\subset[X,CX]$ an arbitrary hard interval (which may move with $N$). Thus $P$ is from the two original distinct prime boxes and original unit and product gates, with any fixed bounded selector $|E(u,v)|\le1$; it has coefficient $P_{uv}=-E(u,v)\log v$. On the complementary side take $N/2\le y\le 9N/16$, $J=[N-y,N/2)$, $t\ge N^{.49999}$, and keep the complete

$$
 D_m=\mathbf1_{m\in J}
      \sum_{\substack{dk=m,\ d\in I_d,\ k>t\\(dk,N)=1,\ (d,k)=1}}
           \mu(d)\mu^2(k).
 \tag{1}
$$

One may independently intersect $k$ with any other hard interval. In the nonempty physical range, both labels $d,k$ are between positive fixed multiples of $X$, with constants depending at most on $C$.

The following are uniform in all these hard endpoints, for sufficiently large $N$.

* For any additional hard physical interval of length at most $H$, with $1\le H\le N$, the restriction $D^{\rm phys}$ of (1) has

$$
 \sum_m |D^{\rm phys}_m|^2
 \ll_C H\big(1+\log(N/H)\big)+N^{3/4}.
 \tag{2}
$$

* For every fixed $B>0$, if one of the two true divisor labels $d,k$ is further restricted to any hard interval of length at most $X L^{-B}$, the resulting actual signed coefficient $D^{\rm lab}$ has

$$
 \sum_m |D^{\rm lab}_m|^2 \ll_{B,C} N L^{-B}.
 \tag{3}
$$

In (3) the other label and physical interval may still carry all their original moving hard restrictions. Both conclusions remain valid, with constants depending on a fixed variation bound, for bounded-variation multipliers supported on the stated intervals and additional bounded-variation weights in the label coordinates. On multiplying an already formed coefficient by a bounded function of $m$ the ordinary square norm only contracts. The sign estimates are on the complete coefficients for the stated slices, not on sums of magnitudes of their individual representations.

### Exact signed square and the gcd split

One can use either label as the signed divisor variable $a$. If $a=d$ the sign on the squarefree support is directly $\mu(a)$. If $a=k$, it equals $\mu(m)\mu(a)$, with the same common factor $\mu(m)$ in every term. In fact every nonzero term of (1) has squarefree $m$ by the two squarefreeness conditions and $(d,k)=1$; conversely every splitting at squarefree $m$ is already relatively prime. At each such $m$ its allowed $a$ comprise the integer points of an interval $\mathcal J(m)$: one has the hard interval in $a$, and the corresponding reciprocal interval from the restriction on the other label. Restrictions on $m$ itself are a separate hard interval $U\subset J$. If we also use $\mathcal J(v)$ at real $v>0$, the two tests retain their actual strict or inclusive endpoints. For fixed $a,b$ the permitted real $v$ form an interval (possibly empty), being the intersection of $U$ and the two cofactor intervals scaled by $a$ and $b$.

After taking the square, adding the nonnegative squares at every nonunit or nonsquarefree $m$ is legitimate. It gives the upper bound

$$
 \sum_{m\in U\cap\mathbb Z}
       \left|\sum_{\substack{a\mid m\\a\in\mathcal J(m)}}\mu(a)\right|^2
 =\sum_{a,b}\mu(a)\mu(b)
      \#\{m\in U\cap\mathbb Z:[a,b]\mid m,\ a,b\in\mathcal J(m)\}.
 \tag{4}
$$

The new summand at an added $m$ need not equal the original coefficient there; the enlargement is only after squaring. Both divisor labels on the right satisfy $a,b\asymp_C X$. Let $G\ge1$ be a cutoff. For $g=(a,b)>G$ the multiple count differs from its interval length divided by $[a,b]$ by $O(1)$ per pair, regardless of endpoints. The total absolute floor error in this range is

$$
 \ll_C\sum_{G<g\ll_C X}(X/g)^2\ll_C N/G.
 \tag{5}
$$

It suffices to bound the actual and continuous contributions at $g\le G$ with absolute coefficients, and to retain the sign in the **full** continuous quadratic form

$$
 \int_U \mathfrak F(\mathcal J(v))\,dv,\qquad
 \mathfrak F(I)=\sum_{a,b\in I\cap\mathbb N}\frac{\mu(a)\mu(b)}{[a,b]} .
 \tag{6}
$$

For (2) use $\mathfrak F(I)\ll1$ uniformly for any interval $I$. This is the consequence of the bounded signed prefix form of Dress–Iwaniec–Tenenbaum used in [the sharp ordinary energy estimate](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy): the kernel is positive semidefinite, and an interval vector is the difference of two prefix vectors. For small $g$, write $a=g u,b=g v$ and $m=g u v r$, with $(u,v)=1$, $u,v\asymp_C X/g$ and necessarily $r\asymp_C g$ because $m\asymp N$. For fixed $g,r,u$ the possible $v$ belong to an interval of length at most $H/(g r u)$ from $m\in U$. Dropping any additional gates and coprimality for this absolute estimate gives $O_C(H/g+X)$ for each $g$: the harmonic sums in $r,u$ are bounded, and there are $O_C(g)\,O_C(X/g)=O_C(X)$ pairs. The continuous contribution at this $g$ is at most $H\sum_{u,v\asymp_C X/g}1/(g u v)\ll_C H/g$. Thus (4) is bounded by

$$
 \ll_C H(1+\log(2G))+XG+N/G.
$$

Choose $G=\max(1,\lfloor\min(N/H,\sqrt X)\rfloor)$. If $G$ is limited by $N/H$, one has $N/G\ll H$; otherwise both $XG$ and $N/G$ are $O(N^{3/4})$. This proves (2).

### A signed narrow continuous form and actual label edges

If $I$ is an interval at scale $X$ of length at most $\delta X$, for $0<\delta\le1$ we claim

$$
 \mathfrak F(I)
 \ll_{A,C} \delta+X^{-1}+\delta^2 L_2^3+L^{-A}
 \quad\text{for any fixed }A>0.
 \tag{7}
$$

The constant is uniform when the endpoints at scale $X$ lie in any fixed positive proportional range. The standard gcd identity gives the exact positive expansion

$$
 \mathfrak F(I)=
 \sum_{g\ge1}\frac{\varphi(g)\mu^2(g)}{g^2}
       \left|\sum_{\substack{n\in I/g\\(n,g)=1}}\frac{\mu(n)}n\right|^2.
 \tag{8}
$$

Let $Z=\exp(L_2^3)$. For $g\le X/Z$, both prefix endpoints of the inner interval in (8) are at least $c_C Z$. The harmonic Möbius prefixes with the actual coprimality mask obey

$$
 \left|\sum_{\substack{n\le Y\\(n,g)=1}}\frac{\mu(n)}n\right|
       \ll_{A,C} L^{-A}\qquad(c_C Z\le Y\ll_C X,\ g\ll_C X)
 \tag{9}
$$

for every fixed $A$, uniformly. Here is the reason for the moving cutoff $Z$. The effective ordinary Mertens estimate, e.g. [Lee and Leong, Theorem 2.2 (23)](https://arxiv.org/html/2208.06141v5#S2.SS2), gives $M_1(u)=\sum_{n\le u}\mu(n)/n\ll \exp(-c(\log u)^{3/5}(\log\log u)^{-1/5})$ at large $u$, by Abel summation with a smaller $c$. Its convergent full sum is zero by the limit of $1/\zeta(s)$ as $s\downarrow1$. The exact coprimality correction convolves $M_1$ with reciprocals of the integers supported on the primes dividing $g$. Its portion with convolution variable at most $\sqrt Y$ is bounded by $M_1$ at arguments at least $\sqrt Y$ times the total reciprocal Euler weight. That weight is $\ll L^{O(1)}$, for instance by the following stronger-exponent estimate. For the remaining portion use that $M_1$ is bounded and Rankin with $\epsilon=1/\log L$; its bound is

$$
 Y^{-\epsilon/2}\prod_{p\mid g}(1-p^{-1+\epsilon})^{-1}
       \le Y^{-\epsilon/2}\exp(O_C(\log L)).
$$

Indeed for $p\le L^2$ use $p^\epsilon\le e^2$ and the ordinary harmonic sum, and above $L^2$ there are at most $O_C(L/\log L)$ such prime divisors, each contributing $O(L^{-2})$ to the logarithm. This proves (9), including arbitrary hard interval endpoint differences (an isolated endpoint contributes $O_C(Z^{-1})$). The small-$g$ part of (8) is now $O_{A,C}(L^{-A})$, taking a stronger input log exponent in (9).

For $X/Z<g\le\delta X$, the unsigned inner sum in (8) is $O_C(\delta)$: there are at most $1+\delta X/g$ terms, each of size $O_C(g/X)$. The harmonic sum of $1/g$ in this range is $O(L_2^3+1)$, contributing $O_C(\delta^2 L_2^3)$. For $g>\delta X$, an interval of length at most $\delta X/g<1$ contains at most one integer. Reversing the order then bounds this part by

$$
 \sum_{a\in I\cap\mathbb N}\frac1{a^2}\sum_{g\mid a}\varphi(g)
 =\sum_{a\in I\cap\mathbb N}\frac1a\ll_C\delta+X^{-1}.
$$

This proves (7) with all signs intact.

Now in (4) use the globally short label as the signed label, and let $\delta=L^{-B}$. For all $v\in U$, its interval $\mathcal J(v)$ has length at most $\delta X$, so the full (6) is $O_{B,C}(N\delta)$ by (7). Take $G=\lfloor L^{B+2}\rfloor$. The actual small-$g$ part is

$$
 \ll_C\sum_{g\le G}g(1+\delta X/g)^2
 \ll_C N\delta^2(1+\log(2G))+\delta XG+G^2 .
 \tag{10}
$$

Indeed, use $m=g u v r$ as before, but now both $u,v$ lie in the *same fixed* interval of length at most $\delta X/g$, and $r\asymp_C g$. Dropping all moving gates in this count yields the first bound. The continuous small-$g$ part has the same upper bound from $|U|\ll N$ and $1/(g u v)\ll_C g/X^2$. Each term after the second inequality in (10), and the large-$g$ floor error (5), is $O_{B,C}(N\delta)$. This proves (3).

To pass from hard restrictions to the variation assertions, use one-dimensional partial summation in each actual label. On an interval a weight of bounded supremum and total variation is an integral of its prefix indicators against a finite signed or complex measure with bounded total variation (or the same finite summation-by-parts representation on the integer labels). This uses only intervals inside the original label range. Minkowski in coefficient square norm applies to these prefix coefficients. A bounded weight on the physical coordinate itself is applied after the sum giving (1). The stated variation extensions of (2) and (3) follow without any comparison of sums of unsigned representations.

## 2. Exact even-lattice high-pass compensation

Write $e(x)=\exp(2\pi i x)$, $\mathcal Q=[.8X,.9X]\cap\mathbb P$, and $\mathcal B=[-1/(10N),1/(10N)]$. Set

$$
 A_D(h)=\operatorname{sinc}(h/(5N))
              \sum_{n+m=N+h}P_nD_m,\qquad
 \mathcal L_N(A)=\frac1{5N}\sum_{q\in\mathcal Q}
           \sum_{a=1}^{q-1}\sum_{h\in\mathbb Z}A(h)e(ah/q),
$$

where $\operatorname{sinc}(z)=\sin(\pi z)/(\pi z)$ continuously at zero. By exact integration in $\mathcal B$, $\mathcal L_N(A_D)$ is the signed full critical-prime shell. Both original $N$-unit gates force $n,m$ odd, so $A_D$ is supported at even $h$. The genuine physical bounds give $|h|\le .037N$. No omission of any signed term containing the zero-numerator base is made in this identity.

For an integer $1\le M\le N/1000$, form the symmetric even-lattice average and actual residual

$$
 S_M A(h)=\frac1{M^2}\sum_{r,s=0}^{M-1}A(h+2r-2s),
       \qquad R_{D,M}=A_D-S_M A_D .
 \tag{11}
$$

Then $R_{D,M}$ is exactly even-supported and has exactly zero total sum. Its support lies in $|h|<N/20$. Every $q\in\mathcal Q$ is odd and every numerator here is nonzero, so $\|2a/q\|_{\mathbb R/\mathbb Z}\ge1/q$. The multiplier of $S_M$ at $a/q$ is $\left|M^{-1}\sum_{r=0}^{M-1}e(2ra/q)\right|^2$, of size $O(\min(1,(X/M)^2))$. Moreover

$$
 \sum_h A_D(h)e(\alpha h)
    =5N\int_{\mathcal B}
          P(\alpha+\beta)D(\alpha+\beta)e(-N(\alpha+\beta))\,d\beta.
$$

The actual arcs at $a/q$ are disjoint modulo one, and $\|P\|_2,\|D\|_2\ll_C\sqrt N$ on the full circle by unique prime product factorization and the sharp ordinary energy. Consequently

$$
 |\mathcal L_N(S_M A_D)|\ll_C N\min(1,(X/M)^2).
 \tag{12}
$$

This uses actual $P,D$ on their original arcs, rather than an independent major model. It also works for any of the boundary pieces above, with $N$ in (12) replaced by $O(\sqrt N\,\|D_{\rm piece}\|_2)$.

The exact finite Ramanujan identity is

$$
 \mathcal L_N(R)=\frac1{5N}\sum_{q\in\mathcal Q}
                 \left(q\sum_{q\mid h}R(h)-\sum_h R(h)\right).
$$

For $R=R_{D,M}$ the second sum is **zero**, not assumed negligible. Put $\mathcal H_N=\{h:0<|h|<N/20,\ \exists q\in\mathcal Q,\ q\mid h\}$ as in the [unmasked zero-base obstruction](weak-s-type-ii-critical-prime-unmasked-zero-base-omega.md). On this set the prime $q(h)$ is unique and $|\mathcal H_N|\ll N/L$. The repeated $h=0$ term contributes $O_C(N/L)$, by $|R_{D,M}(0)|\ll_C N$ (coefficient Cauchy and the normalized average). Thus

$$
 \mathcal L_N(A_D)
 =\frac1{5N}\sum_{\substack{h\in\mathcal H_N\\h\ {\rm even}}}
       q(h)R_{D,M}(h)
    +O_C\!\left(N/L+N\min(1,(X/M)^2)\right).
 \tag{13}
$$

Only even offsets occur. A sufficient square estimate for the remaining signed sum would be $\sum_{h\in\mathcal H_N,\ h\ {\rm even}}|R_{D,M}(h)|^2=o(N^2L)$; it is **not** proved here. The unmasked large zero-base and literal odd-start obstruction do not lower-bound this different compensated residual.

## 3. Removing all actual endpoint layers in the signed compensated shell

Fix $B>0$ and replace each of the true hard gates on $m,d,k$ in (1) by a weight between zero and one, vanishing off its true allowed interval and equal to one outside its own interior edge layers. Take the layer widths to be at most $O(NL^{-B})$ for $m$ and $O(XL^{-B})$ for $d,k$, and take fixed bounded variations for these cutoff weights. Smooth such cutoffs are allowed, and any gate already inactive can be left unchanged. Keep every true coprimality condition and the original $\mu,\mu^2$ weights. Call the resulting complete coefficient $D^{\rm sm}$, with corresponding $A_{D^{\rm sm}}$ and $R_{D^{\rm sm},M}$.

Telescope through the three coordinate cutoffs. The physical difference is a bounded multiplier after the coefficient is formed and occupies at most two physical edge intervals. Each label difference is subject to at most two genuine narrow label intervals; the remaining label cutoffs have uniformly bounded variation, so the extension of (3) applies. The physical weight contracts each square norm. Therefore (2)–(3) give

$$
 \|D-D^{\rm sm}\|_2
       \ll_{B,C}\sqrt N\,L^{-B/2}\sqrt{L_2}+N^{3/8}.
 \tag{14}
$$

Passing to signed shell integrals by disjoint-arc Cauchy, the error is at most $\|P\|_2$ times (14). The even-lattice construction (11) remains exact on $D^{\rm sm}$: the weights introduce no value off the actual support and do not change parity. Apply (13) to obtain

$$
 \mathcal L_N(A_D)
 =\frac1{5N}\sum_{\substack{h\in\mathcal H_N\\h\ {\rm even}}}
        q(h)R_{D^{\rm sm},M}(h)
 + O_{B,C}\!\left(
       N L^{-B/2}\sqrt{L_2}+N^{7/8}
           +N/L+N\min(1,(X/M)^2)\right).
 \tag{15}
$$

For example, $M=\lceil X L^2\rceil$ makes every term of this error $o(N)$ for each $B>0$. This removes all genuine endpoint layers at that signed scale, even when the cutoffs originally move with the target. The conclusion does not remove the smooth interior signed correlation, does not estimate the full shell at scale $o(N)$, and does not settle weak S.
