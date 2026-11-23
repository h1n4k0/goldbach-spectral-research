# Two divisor gates improve the energy of the genuine critical boundary tail

Keep the exact fixed-prime-box $P$, sharp complementary polynomial $D$, and full and double-centered critical-shell pairings $\mathcal I(P,F)$ and $\mathcal C(P,F)$ from the [least-prime boundary reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). In particular $N$ is even, $X=\sqrt N$, $L=\log N$, the original complementary interval is $I_0=I_d\cap[X,\infty)$ with endpoints $A=\inf I_0$ and $U=\sup I_0$, and $k>t\ge N^{.49999}$. The common integer product $m=dk$ lies in $[N-y,N/2)$ with $y\le9N/16$, is a unit modulo $N$, and is squarefree on every nonzero summand. The weight is $\mu(d)\mu^2(k)$ with exact gcd mask. The prime leg retains any fixed $|E(u,v)|\le1$ and the original hard intervals and product gate, independently of the point $q,\beta$.

For $2\le Z\le N^{1/10}$, define $D^{>Z}$ to keep **all** original coefficients with $P^-(m)>Z$, and let $D_{\partial,\le Z}$ be the three exact signed boundary classes from the preceding reduction when $P^-(m)\le Z$. The polynomial identity remains $D=D^{>Z}+D_{\partial,\le Z}$. The new unconditional estimate is

$$
\int_0^1 |D^{>Z}(\alpha)|^2\,d\alpha
 \ll \frac{N L}{(\log Z)^2}.
\tag{1}
$$

It follows that, for any fixed $1/2<\theta<1$ and $Z=\exp(L^\theta)$,

$$
|\mathcal C(P,D)-\mathcal C(P,D_{\partial,\le Z})|
+|\mathcal I(P,D)-\mathcal I(P,D_{\partial,\le Z})|
  \ll N L^{1/2-\theta}.
\tag{2}
$$

Every surviving exact band has multiplicative width at most $\exp(L^\theta)$, in its original $d$ or $k$ variable. The earlier estimate used $NL^3/(\log Z)^4$ for the energy in (1), and required $\theta>3/4$ for a saving in (2). The new argument makes a saving already at $\theta=2/3$, for example $O(N/L^{1/6})$. It uses common integer coefficients and exact signed cancellation, with no selection of moduli, numerators, or aliases. It does not estimate the complementary signed covariance on the bands with $P^-(m)\le Z$.

## 1. Apply the exact sign toggle also above the cutoff

Fix a least prime $p$ of an actual nonzero coefficient and write $m=pn$. Then $n$ is squarefree with all prime factors $>p$, and $(m,N)=1$. The exact operation of exchanging $p$ between $d$ and $k$ still pairs the two opposite signs at this fixed integer $m$, even when $p>Z$. It preserves all the original data other than the tested endpoints, so all admissible pairs cancel as before.

For each of the three surviving types the absolute coefficient at fixed $m$ is at most a divisor count for $n$ in an interval of relative width $p$:
- If $p\mid d$ and $d/p\notin I_0$, put $a=d/p\mid n$. Then $A/p\le a\le A$.
- If $p\mid k$ and $pd\notin I_0$, put $a=d\mid n$. Then $U/p\le a\le U$; this type is absent if $U=\infty$.
- If $p\mid k$, $pd\in I_0$, and $k/p\le t$, put $a=k/p\mid n$. Then $t/p<a\le t$.

In each type $a$ determines the original pair $(d,k)$ uniquely. The containing interval can be taken closed for the upper bound; the signed coefficient itself keeps all exact endpoint tests and masks. For the square of the sum of the three type coefficients use $|c_1+c_2+c_3|^2\le3\sum_i|c_i|^2$. Thus it suffices, at fixed $p$ and each applicable $H\in\{A,U,t\}$, to bound the second moment of the divisor count in $[H/p,H]$ on $n$ in the actual product range. No summation across least primes is taken inside this square: each integer $m$ has a unique $p$.

## 2. Elementary rough count and harmonic bounds

For prime $p\ge2$, write $p$-rough for positive integers with no prime factor $\le p$, including one. Uniformly for real $V\ge p$,

$$
\#\{j\le V:j\text{ is }p\text{-rough}\}\ll V/\log p.
\tag{3}
$$

One may use the [Selberg square construction at modulus one](weak-s-type-ii-critical-prime-sparse-aliases.md), with level $R=\lfloor\min(p,V^{1/10})\rfloor$ and all $R\ge2$. On a rough integer all the nontrivial divisors in the support of the weights are absent, so its Selberg square is one. The density is $O(1/\log R)=O(1/\log p)$ for large $p$ and the floor error is $O(R^2(1+\log R)^2)$, at most $O(V/\log p)$. Bounded $p$ can be covered by increasing the absolute constant. Partial summation now gives, for any fixed $C\ge1$ and interval $[B_1,B_2]$ with $0<B_1\le B_2\le C p B_1$,

$$
\sum_{\substack{B_1\le j\le B_2\\j\text{ is }p\text{-rough}}}\frac1j
\ll_C 1.
\tag{4}
$$

The factor one costs at most one, and all other terms are $>p$. If that range is nonempty, use (3) above $\max(B_1,p)$ and integrate $O(1/(x\log p))$ over a ratio at most $Cp$. We also use the unrestricted harmonic bound

$$
\sum_{\substack{j\le N\\j\text{ is }p\text{-rough}}}\frac1j
\le\prod_{p<r\le N,\ r\ {\rm prime}}(1-1/r)^{-1}
\ll L/\log p
\tag{5}
$$

by the prime Mertens estimate.

## 3. Keep two gates regardless of the largest variable

Let $p\le N^{1/10}$, $Y=N/p$, and fix $H>0$. An ordered pair of divisors of a squarefree $n$ counted in the squared divisor sum is uniquely $gx,gy$, with $g$ their gcd. Write $n=gxyz$. All four factors are $p$-rough, and their pairwise coprimality can be dropped for an upper bound. The original range of $m$ gives $7Y/16\le n<Y/2$. In addition to the divisor gates

$$
gx,gy\in[H/p,H],
$$

the two complementary quotients satisfy

$$
xz,yz\in[7Y/(16H),pY/(2H)].
$$

Their interval also has ratio $O(p)$.

Choose one largest variable from $g,x,y,z$, bounding the total by summing over four choices in case of ties. If the largest variable is $z$, the remaining variables still satisfy the pair of gates $gx,gy$; if it is $g$, they satisfy $xz,yz$. If it is $x$, use $gy,yz$; if it is $y$, use $gx,xz$. Thus in every case two products of the remaining three variables are gated, with one shared variable.

The product $W$ of the three remaining variables is at most $Y^{3/4}$ in every actual tuple. The largest variable therefore has upper cutoff $Y/W\ge Y^{1/4}\ge p$ for the stated range of $p$, so (3) bounds its choices by $O(Y/(W\log p))$. After this factor has been extracted, the other three variables are summed harmonically. For fixed shared variable, each of the other two ranges has ratio $O(p)$, so (4) costs $O(1)$ on each. The shared variable costs $O(L/\log p)$ by (5). Consequently the squared divisor count at fixed $p$ for each of the three bands is bounded by

$$
O\!\left(\frac{N}{p}\frac{L}{(\log p)^2}\right),
\tag{6}
$$

uniformly in $H$ and the sharp endpoints. The improvement comes from keeping two independent harmonic restrictions even when the largest variable occurs in an original gate. Dropping the complementary gates would not give (6) by this argument.

## 4. Sum the true least-prime tail

Sum (6) for $Z<p\le N^{1/10}$; by the prime upper bound and partial summation,

$$
\sum_{p>Z}\frac{1}{p(\log p)^2}\ll\frac1{(\log Z)^2}.
$$

For $p=P^-(m)>N^{1/10}$ there are at most ten prime factors in $m\le N$, and the absolute coefficient is at most $\tau(m)$, hence bounded by an absolute constant. The number of such $m$ is $O(N/L)$ by the same elementary sieve (with the primes $\le N^{1/10}$). This extra energy is dominated by the right side of (1) since $Z\le N^{1/10}$. Parseval proves (1).

The disjoint prime boxes give $\int_0^1|P(\alpha)|^2d\alpha\ll N$ with the true fixed selector. Cauchy–Schwarz on the disjoint arcs bounds the cross with $D^{>Z}$ by $O(N\sqrt L/\log Z)$; subtracting the separate means over nonzero numerators is an orthogonal contraction and gives the same estimate after double centering. A term with $q\mid m$ is included in the ordinary polynomial, and only becomes constant and disappears on the centered numerator array; no extra $q$ filter is imposed. Applying the exact split proves (2).

All aliases, including a dense set, were retained in removing the actual high-least-prime tail. There is still no bound here on the dense signed covariance of the three residual bands, the full critical shell, or weak S.
