# A pointwise all-alias critical-shell bound for targets with few missing small primes

Keep the true critical-prime setup and the three exact signed complementary boundaries of the [least-prime reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and $L_3=\log L_2$. The prime polynomial $P$ keeps the two disjoint proportional hard prime boxes, their arbitrary hard subintervals, the gate $N/2<uv\le y\le9N/16$, $(uv,N)=1$, and genuine weight $-E(u,v)\log v$ with any fixed $|E(u,v)|\le1$. The selector and sharp cuts are fixed independently of the rational point. The complementary polynomial $D$ keeps $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. No changes are made to strict endpoints.

Fix $0<A<1$ and set $W=L^A$. Write

$$
\mathscr R_N(W)=\prod_{\substack{\ell\le W,\ \ell\ {\rm prime}\\ \ell\nmid N}}
   (1+4/\ell).
$$

The unconditional pointwise bound for the full and the double-centered signed critical-shell pairings is

$$
|\mathcal I(P,D)|+|\mathcal C(P,D)|
 \ll_A N \sqrt{\frac{\mathscr R_N(W)}{L_3}}.
\tag{1}
$$

Here the $q$ are all primes in $[.8X,.9X]$, all nonzero numerators are used, and $|\beta|\le1/(10N)$. Thus this gives $o(N)$ on any target family with $\mathscr R_N(W)=o(L_3)$, including families for which the sum of reciprocals of the omitted small primes is bounded, or all but a bounded number of the primes $\le W$ divide $N$. No average over $N$ and no alias selection is used. The small-least-prime bands need not be zero on this family.

## 1. Fix the actual small part and its allocation

By the [polylogarithmic least-prime energy estimate](weak-s-type-ii-critical-prime-polylog-boundary-width.md), the genuine part with $P^-(m)>W$ has ordinary squared energy $O_A(N/L_3)$.

Now take $P^-(m)\le W$. An eligible product $m$ is squarefree. Write $m=rn$, where $r$ is the product of its prime factors $\le W$ and $n$ is $W$-rough (no prime factor $\le W$). Because $(m,N)=1$, all primes of $r$ belong to the omitted set in $\mathscr R_N(W)$; $r>1$ and $p=P^-(m)=P^-(r)$. The preceding exact least-prime exchange applies at this $m$, so only its three signed boundary types remain. For fixed $r$, split the actual terms further according to the unique allocation $r=r_d r_k$ of its prime factors between $d,k$. Thus $d=r_d a$, $k=r_k b$ with $ab=n$, $a,b$ divisors of $n$, unless the coordinates are reversed as specified below. The original gcd and squarefree conditions now follow on every squarefree $n$ from this allocation; the original $N$-unit and product masks are retained until after squaring.

For each allocation and the indicated compatible boundary type, the coefficient at $m$ is, up to a common sign of modulus one on squarefree $n$, a signed divisor sum $\sum_{a\mid n,\,a\in I,\,n/a\in J}\mu(a)$. Its two intervals are exact for that type:
- When $p\mid r_d$ and $d/p\notin I_0$, use $a=d/r_d$, $b=k/r_k$. Require $r_da\in I_0$, $(r_d/p)a\notin I_0$, and $b>t/r_k$. The failed membership is at the lower end, so $a$ lies within $[\inf I_0/r_d,p\inf I_0/r_d]$. The sign factor is $\mu(r_d)$.
- When $p\mid r_k$ and $pd\notin I_0$, use $a=d/r_d$, $b=k/r_k$. Require $r_da\in I_0$, $p r_da\notin I_0$, and $b>t/r_k$. The failed membership is at the upper end, so $a$ lies within $[\sup I_0/(p r_d),\sup I_0/r_d]$ if the type is nonempty. The sign factor is again $\mu(r_d)$.
- When $p\mid r_k$, $pd\in I_0$, and $k/p\le t$, use the opposite orientation $a=k/r_k$, $b=d/r_d$. Require $t/r_k<a\le pt/r_k$ and both $r_d b,p r_d b\in I_0$. The sign factor is $\mu(r_d)\mu(n)$, since $\mu(b)=\mu(n)\mu(a)$ for squarefree $n$.

The conditions on either coordinate are contiguous intervals, with their original open or closed endpoints. One interval in each case lies in a multiplicative envelope of ratio $p\le W$. Set $Y=N/r$. The original product window for $n$ is contained in $[7Y/16,Y/2)$. Also $\log r\le \sum_{\ell\le W}\log\ell\ll W=o(L)$ by the prime upper bound, so $\log Y\sim L$ uniformly for all $r$ in this decomposition.

## 2. The fixed roughness moment applies even when the toggled prime is small

For these exact signed divisor sums the fixed-cutoff steps in the [polylogarithmic energy proof, §§1–2](weak-s-type-ii-critical-prime-polylog-boundary-width.md) give a squared sum $O_A(Y/L_3)$ for each fixed allocation and type. We spell out why its fixed-$p$ estimate can be used without identifying the *roughness threshold* with the much smaller toggled prime.

The original signs are exactly those needed for the short-divisor step of the [signed lcm proof](weak-s-type-ii-critical-prime-signed-boundary-energy.md). Split the variable in the displayed sum at $\sqrt n$, and on its long half exchange it with $n/a$ using the common factor $\mu(n)$. After the resulting at-most-two pieces are squared separately, the original squarefree and $N$-unit conditions may be relaxed for an upper bound by adding nonnegative squares on all $W$-rough $n$. Each short moving interval has ratio $O(p)\le O(W)$ in its fixed proportional ambient envelope, and its membership for each fixed integer divisor is an interval condition on $n$ because the inequalities only test $a,n/a$ and $a\le\sqrt n$ (or strict in the exchanged case). Thus the same interval and discrete/continuous lcm arguments apply.

In those fixed-cutoff arguments every occurrence of the former fixed prime as a roughness threshold is now the real number $W=L^A$, and every gate ratio is $O(W)$. No use of primality of the threshold is needed there. The Bonferroni order and the logarithmic exponent for the signed rough harmonic cutoff are $O_A(L_2/L_3)$, with the $g$-coprimality enforced by the joint reciprocal-zeta Euler mask in the polylogarithmic proof. These parameter estimates hold at $W$ itself, with the same floor and tail sizes: $\log W=A L_2$, $\log Y\sim L$, and $W^{O_A(L_2/L_3)}=Y^{o(1)}$ uniformly. The resulting bound $O_A(Y(1+r_0+\sigma_0)/\log W)$, with $r_0,\sigma_0$ those two parameters, is $O_A(Y/L_3)$. Here the variable $\mu(a)$ is never replaced by an unsigned count in the short-lcm main term. The long-lcm corrections are bounded as in that proof. The later step summing over least primes in the published proof is *not* used for this fixed allocation.

## 3. Combine the genuine coefficients

For fixed $r$, Cauchy–Schwarz for at most $3\cdot 2^{\omega(r)}$ allocation/type sums, followed by the last per-sum energy bound, gives

$$
\sum_{n}\bigl|\text{actual coefficient at }m=rn\bigr|^2
 \ll_A \frac{N}{r L_3}\,4^{\omega(r)}.
$$

Distinct $r$ give disjoint supports in the original integer coefficient $m$. Hence the true low-least-prime energy is at most

$$
\frac{O_A(N)}{L_3}
 \sum_{\substack{r>1,\ r\ {\rm squarefree}\\
             \ell\mid r\Rightarrow \ell\le W,\ \ell\nmid N}}
             \frac{4^{\omega(r)}}{r}
=
\frac{O_A(N)}{L_3}\bigl(\mathscr R_N(W)-1\bigr).
$$

The true high-least-prime energy accounts for the missing $1$ in this factor. By Parseval, the whole ordinary squared energy of $D$ is $O_A(N\mathscr R_N(W)/L_3)$.

The prime polynomial has ordinary squared energy $O(N)$ by disjoint prime boxes, unique ordered prime factorizations, and the prime upper bound. The critical arcs are disjoint; subtracting the separate numerator means is an orthogonal contraction on them. Cauchy–Schwarz proves (1) for both the full and double-centered integrals. It uses the actual common coefficient before evaluating at any rational point: no additional condition on $q\mid m$ was imposed. A term divisible by $q$ merely projects to a numerator constant and disappears after centering.

## 4. Nonvacuity and the generic unresolved part

For example, let $N$ range over primorials with the prime $3$ omitted, with the upper primorial cutoff tending to infinity. These $N$ are even and, since $A<1$, every prime $\le W$ other than $3$ divides $N$ for all large targets by the prime number theorem. The class includes actual nonzero small-least-prime coefficients. To see this, take $I_d=[X,2X]$, $t=N^{.49999}$, $y=9N/16$, and primes $a\in[.49X,.50X]$, $b\in[.30X,.31X]$, which exist for large $N$ and exceed the primorial cutoff. For $m=3ab$, the original product window holds and $(m,N)=1$. Its only admissible complementary pair is $(d,k)=(3a,b)$: $3b<X$, both $a,b<X$, and divisors with both large primes are above $2X$. The pair has coefficient $\mu(3a)\mu^2(b)=1$ and fails its lower-endpoint partner test since $d/3=a<X$. This verifies a genuine low-prime boundary coefficient, without asserting that its signed pairing alone is a lower bound.

For general exceptional $N$, the omitted-prime Euler factor can be much larger than $L_3$; for $N$ a power of two it is of order $(\log W)^4$. The pointwise estimate then supplies no saving. To remove this restriction requires new arithmetic controlling the signed allocation sum without the $4^{\omega(r)}$ loss or obtaining cancellation jointly with the prime leg across the dense critical shell. The almost-all critical estimate and the pointwise bound here do not resolve those generic targets, other arc ranges, or weak S.
