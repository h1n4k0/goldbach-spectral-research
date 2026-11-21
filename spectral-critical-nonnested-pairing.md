# Non-nested opposite-parity cancellation at the exact square-root cutoff

**Scope.** An unconditional, pointwise cancellation of the whole prime-divisor dyad from the [critical floor](spectral-critical-prime-sector-floor.md) **after** it is grouped with a specified, actual even-parity companion sector. This pairing works at the exact switch $t=\sqrt N$, by using complementary divisors instead of multiples of a prime. It is an alternative partition which can overlap the [Maynard structured removal](spectral-maynard-structured-critical.md); their gains cannot be added without proving an overlap estimate. No estimate for the full discrepancy or S/R is asserted.

Use even $N$, $L=\log N$, $S=\mathfrak S(N)$, and units in the upper central interval $N/2<n\le9N/16$. Set $m=N-n$, and on squarefree $m$ let $\mathcal D(m)$ consist of **all** its prime divisors $d\in[\sqrt N/5,\sqrt N/3]$. All are below the strict complementary threshold $m/\sqrt N$, since $m\ge7N/16$. The true summand in that complementary form includes $\Lambda(n)\mu^2(m)\mu(d)$, optionally weighted by $\log d$ as in the divisor expansion.

Fix $0<\delta\le10^{-5}$ and $7\le Z\le N^\delta$. If $m$ has at least two distinct prime factors in $[7,Z]$, let $p_1<p_2$ be its least two in this interval, and choose
$$
 r=r(m)=
 \begin{cases}
  p_1,&\mu(m)=+1,\\
  p_1p_2,&\mu(m)=-1 .
 \end{cases}
$$
Call these $m$ paired. For each base prime $d\in\mathcal D(m)$ on a paired $m$, take the companion
$$
 e=e(m,d)=\frac{m}{rd}.
$$
Otherwise take no companion, but retain all base primes in the selected sector.

## 1. Geometry, sign and uniqueness

Because both small factors are at most $Z$ and $d\ge\sqrt N/5$, $r$ is coprime to every base $d$ and $e$ is an integer divisor. Also $rd\ge(7/5)\sqrt N>\sqrt N$, so $e<m/\sqrt N$ strictly. It satisfies
$$
 e\ge\frac{21}{16}\frac{\sqrt N}{Z^2}>1.
$$
The sign is exact: $\mu(r)=-\mu(m)$, $\mu(d)=-1$, and $m$ is squarefree, so $\mu(e)=+1$. In particular $e$ is not prime, hence does not collide with the original prime class even when $m$ has two eligible base primes. Since $r(m)$ is fixed independently of $d$, the map $d\mapsto e$ is injective for each $m$; different $n$ correspond to different summands. Therefore this is a literal selection of terms, not a duplication with compensating weights. The companions can be semiprime but need not all be. In particular they can contain the two designated Maynard band primes, so no disjointness from that other removal is claimed.

Each paired contribution satisfies
$$
 \mu(d)+\mu(e)=0,\qquad
 \mu(d)\log d+\mu(e)\log e=\log(m/d^2)-\log r .
$$
Since $m/d^2$ lies between positive absolute constants, the absolute log residual is $O(1+\log p_2)$. In the original long expression with a leading minus sign the signs reverse but the same absolute estimate holds. If that expression additionally imposes a lower cutoff $D$ on divisors, **both** members must exceed $D$: for example $D<\sqrt N/(5Z^2)$ is sufficient. The result below is stated first for the complementary sum without that extra cutoff.

## 2. An at-most-one-factor upper sieve

For $1\le R\le Z$, let $U_2(R)$ be the actual nonnegative mass
$$
 \sum_{\substack{N/2<n\le9N/16;\ (n,N)=1\\
   |\{p\text{ prime}:7\le p\le R,\ p\mid N-n\}|\le1}}
       \Lambda(n)\mu^2(N-n)|\mathcal D(N-n)|.
$$
Then uniformly and unconditionally,
$$
 U_2(R)\ll \frac{S N}{L\log(2R)}\bigl(1+\log\log(3R)\bigr).
 \tag{1}
$$

For fixed $d\nmid N$, let $q=(N-n)/d$ in the interval $[7N/(16d),N/(2d))$. It is of length $\asymp\sqrt N$ and $d>R$. First take the case of **no** prime factor of $q$ in $[7,R]$. In the variable $q$, forbid the zero of the primality form $N-dq$ at each sieve prime $\ell\le z_s=N^{1/100}$, and also forbid $q\equiv0$ for $7\le\ell\le R$. The roots coincide exactly when $\ell\mid N$ in the two-form range. Every actual prime $n>N/2$ exceeds $z_s$, so it avoids the primality roots. As in the [nested pairing sieve](spectral-critical-opposite-parity-pairing.md), the local product is
$$
 V_R=\prod_{\ell\le z_s}(1-1/\ell)
      \prod_{\substack{7\le\ell\le R;\ell\text{ prime}\\\ell\nmid N}}
                  \frac{\ell-2}{\ell-1}
      \ll \frac{S}{L\log(2R)} .
$$
The finite omission of $2,3,5$ from the additional roughness sifting only changes an absolute constant. The estimate follows from Mertens and the even Goldbach Euler product.

For **exactly one** prime $p\in[7,R]$ dividing $q$, write $q=pv$. Because $m$ is squarefree, $v$ has no prime factor in $[7,R]$, including $p$. If $p\mid N$ there is no unit contribution, so assume $p\nmid N$. Now the primality form is $N-dp v$, while $v$ is confined to an interval of length $\asymp\sqrt N/p$. All local root counts are the same as in the zero-factor sieve except at $p$: the primality form is never zero there ($N\not\equiv0\bmod p$), and the roughness condition forbids just $v\equiv0$. Replacing the old factor $1-2/p$ by $1-1/p$ increases the product by $(p-1)/(p-2)\le6/5$.

In both cases the dimension is at most two uniformly, by the same product argument as before; use the [fundamental upper-bound sieve, Tao Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) at squarefree level $N^{1/4}$. The interval lengths are at least a fixed multiple of $N^{1/2-\delta}$; each squarefree remainder is $O(2^{\omega(a)})$ at modulus $a$, by counting the CRT roots, so the total per progression problem is $O(N^{1/4}L)$. After restoring the at most $L$ weight of a prime and summing $O(\sqrt N/L)$ base primes, the zero-factor main bound is $O(S N/(L\log(2R)))$. The one-factor main bound has the additional factor $\sum_{7\le p\le R}1/p\ll1+\log\log(3R)$, from the interval length $\sqrt N/p$. Summing all progression remainders costs $O(N^{3/4+\delta}L)$, which the asserted bound absorbs. Dropping squarefreeness after imposing the stated roughness on $v$ only increased counts. Finally, proper prime powers in $n$ are $O(\sqrt N L)$ candidates of weight at most $L$, and each fixed $m<N$ can contain at most two distinct eligible $d$ (the product of three exceeds $N$). This gives $O(\sqrt N L^2)$ more, also absorbed. This proves (1) without any Ramanujan, zero-distribution or GRH input.

## 3. The quantitative exact-cutoff cancellation

Take any bounded nonnegative or signed central weight $W(n/N)$, and any prefix in the stated upper central interval. The unweighted selected sum, in absolute value before division by $N$, is bounded by $\|W\|_\infty U_2(Z)$: all paired contributions cancel exactly, and the rest are the prime contributions with at most one eligible factor.

For the log-weighted sum, the unpaired part is at most $\|W\|_\infty L U_2(Z)$. For the paired part, the mass with $p_2>R$ is at most $U_2(R)$, since there are then at most one distinct prime divisor in $[7,R]$. Layer cake and (1) bound it by
$$
 \ll \|W\|_\infty
      \left(U_2(1)+\int_1^Z U_2(R)\,\frac{dR}{R}\right)
 \ll \|W\|_\infty\frac{SN}{L}(1+\log\log(3Z))^2 .
$$
Thus the total log-weighted selection, after division by $N$, is at most
$$
 \ll \|W\|_\infty S
  \left(\frac{1+\log\log(3Z)}{\log(2Z)}
       +\frac{(1+\log\log(3Z))^2}{L}\right).
 \tag{2}
$$
For $Z=N^\delta$ with fixed $\delta$ the raw unweighted bound is $O_\delta(\|W\|_\infty S N\log L/L^2)$ and the normalized log-weighted bound is $O_\delta(\|W\|_\infty S(\log L)^2/L)$. For an original long lower cutoff $D=\lfloor\sqrt N/L^C\rfloor$ with fixed $C>0$, take instead $Z=L^c$ with $0<c<C/2$ to retain every pair; the bound (2) is still $o(S)$ for bounded weights.

The prime dyad alone can have raw size $\gg N/L$ with bounded $S$ on a positive proportion of moduli, as shown in the critical-floor note. On those same moduli its cancellation here comes from actual even-parity complementary terms, not from the prime mass becoming smaller. The leftover divisor subset and any overlap with the Maynard structured estimate remain independent tasks.
