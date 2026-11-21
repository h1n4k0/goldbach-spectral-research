# A genuine prime–semiprime cancellation near the critical divisor cutoff

**Scope.** A pointwise unconditional bound for one combined actual sector of the upper central complementary-divisor sum. It pairs selected prime divisors with actual semiprime divisors of the *same* $N-n$. It is not a bound for all prime or semiprime sectors at the same cutoff, for the full signed rectangle discrepancy, or for S/R.

Write $L=\log N$, $S=\mathfrak S(N)$, and $m=N-n$. Use even integers $N$ and central unit pairs $N/2<n\le9N/16$, $(n,N)=1$. In the [complementary form](spectral-critical-level-diagonal.md), the genuine term at divisor $e\mid m$ is
$$
 \Lambda(n)\mu^2(m)\mu(e)\mathbf1_{e<m/t}.
$$
The log-weighted complementary form replaces $\mu(e)$ by $\mu(e)\log e$, and its sign is reversed if inserted in the original negative Möbius divisor expansion. A separately imposed long-divisor lower cutoff must retain both members of each pair; a sufficient condition is that it be below $D_0/5$. The cutoff $e<m/t$ is strict in both forms.

## 1. Exact opposite-parity pairs, with no term reused

Fix $0<\delta\le10^{-5}$, take $2\le Z\le N^\delta$ and $\sqrt N/Z\le D_0\le\sqrt N$, and set
$$
 t=\frac{N}{Z D_0}.
$$
In particular $\sqrt N/Z\le t\le\sqrt N$. Let $\mathcal D(m)$ be the prime divisors $d$ of $m$ with $D_0/5\le d\le D_0/3$. For squarefree $m$, write $p_m=P^-(m)$, the least prime divisor, and retain the following indices for the **combined sector**:
$$
 \mathcal E_Z(m)=\mathcal D(m)
 \ \cup\ \{p_m d: d\in\mathcal D(m),\ p_m\le Z\}.
$$
Nonsquarefree $m$ contribute zero. This selected set is a literal subset of the complementary divisor sum. Indeed $m\ge 7N/16$, and for $p_m\le Z$,
$$
 d\le D_0/3< m/t,\qquad p_m d\le ZD_0/3<(7/16)ZD_0\le m/t .
$$
Every $d$ here is larger than $Z$ for all sufficiently large $N$, thus it is distinct from $p_m$. This makes $p_m d$ squarefree and semiprime; it has a uniquely identifiable large prime factor $d$ and cannot itself be a base prime. For fixed $n$, no two selected $d$ therefore reuse the same semiprime. Across different $n$ they are different summands of the original sum. Neither $d$ nor $p_m d$ belongs to the [discarded Maynard structured class](spectral-maynard-structured-critical.md): their possible small prime is at most $N^{10^{-5}}$, and their large prime is at least $N^{1/2-10^{-5}}/5$, disjoint from both of the defining bands.

For each squarefree $m$, directly using the actual Möbius values,
$$
 \begin{split}
 \sum_{e\in\mathcal E_Z(m)}\mu(e)
 &= -\mathbf1_{p_m>Z}|\mathcal D(m)|,\\
 \sum_{e\in\mathcal E_Z(m)}\mu(e)\log e
 &= \mathbf1_{p_m\le Z}|\mathcal D(m)|\log p_m
    -\mathbf1_{p_m>Z}\sum_{d\in\mathcal D(m)}\log d .
 \end{split} \tag{1}
$$
Thus pairing is exact without log and leaves only the small logarithm $\log p_m$ with log. In the original long sum with an overall minus sign, when both members are retained, the identity has the opposite overall sign but the same bound.

## 2. Roughness bound on the actual prime-divisor mass

For $1\le r\le Z$ let
$$
 U(r)=\sum_{\substack{N/2<n\le9N/16\\(n,N)=1;\ P^-(N-n)>r}}
         \Lambda(n)\mu^2(N-n)|\mathcal D(N-n)|.
$$
Unconditionally and uniformly in the displayed parameter ranges,
$$
 U(r)\ll \frac{S N}{L\log(2r)}. \tag{2}
$$
To prove this, fix a base prime $d\nmid N$ and write $q=(N-n)/d$. Its full interval is $[7N/(16d),N/(2d))$, of length comparable to $N/D_0\ge\sqrt N$. Since $d>r$, the condition $P^-(m)>r$ requires $q$ to have no prime factor at most $r$. Dropping squarefreeness only increases the count.

For $n$ prime, use the standard upper-bound sieve on the integers $q$ in this interval, with sieving primes up to $z_s=N^{1/100}$ and a squarefree level $N^{1/4}$. The base prime $d$ is larger than $z_s$. At a sieving prime $\ell\le r$, exclude the roots of $q(N-dq)\equiv0\bmod\ell$: they are two distinct roots if $\ell\nmid N$, and one if $\ell\mid N$. For $r<\ell\le z_s$, exclude only the single root of $N-dq$. In particular the count at $2$ is one because $N$ is even. Every actual prime $n>N/2$ avoids the roots of its primality form, since it exceeds $z_s$.

The general fundamental upper-bound sieve applies here, for example [Tao, Notes 4, Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/). Its dimension bound is at most two uniformly: across prime intervals the inverse product of $(1-\nu_\ell/\ell)$ is bounded by an absolute multiple of the square of the Mertens ratio, since $\nu_\ell\le2$ for odd primes and the factor at $2$ is finite. For any squarefree modulus $a$ up to the level the interval-count remainder is $O(2^{\omega(a)})$ by the Chinese remainder theorem, hence $O(N^{1/4}L)$ in total with the bounded sieve coefficients. The sieve product is
$$
 \prod_{\ell\le z_s}(1-1/\ell)
 \prod_{\substack{3\le\ell\le r;\ell\ \mathrm{prime}\\\ell\nmid N}}
      \frac{\ell-2}{\ell-1}
 \ll \frac{S}{L\log(2r)} .
$$
Indeed $(\ell-2)/(\ell-1)\le1-1/\ell$, so a second Mertens product costs $1/\log(2r)$ and restoring its deleted $\ell\mid N$ costs at most $O(S)$ by the even Goldbach Euler product. This proves a count $O((N/D_0)S/(L\log(2r))+N^{1/4}L)$ for each $d$. After putting back the log weight of primes and summing $O(D_0/L)$ base primes, the main bound in (2) results; the errors are $O(N^{3/4}L)$ since $D_0\le\sqrt N$.

Proper prime powers in $n$ add only $O(\sqrt N L^2)$. There are $O(\sqrt N L)$ such integer candidates, each weight at most $L$, and any fixed $m<N$ has at most two distinct prime factors in $[D_0/5,D_0/3]$: the product of three is larger than $N$ for large $N$ since $D_0\ge N^{1/2-10^{-5}}$. Both power errors are absorbed in (2), also at the maximal $r$.

## 3. Quantitative combined-sector conclusion

For any bounded central weight $W(n/N)$, including the truncated upper-half weights of the rank-two block, multiply (1) by $\Lambda(n)\mu^2(m)W(n/N)$ and sum over units. All bounds below also hold uniformly for each prefix inside the upper central half. The unweighted combined sum, before division by $N$, is at most
$$
 \ll \|W\|_\infty\frac{S N}{L\log(2Z)} .
$$
For the log-weighted version, the unpaired terms are at most $L U(Z)$. The paired log residual is bounded by
$$
 \int_1^Z U(r)\,\frac{dr}{r}
 \ll \frac{S N}{L}\log\log(3Z),
$$
using $\log p=\int_1^p dr/r$ for the least prime on paired terms. Thus the log-weighted combined sum **after normalization by $N$** is at most
$$
 \ll \|W\|_\infty S
     \left(\frac{1}{\log(2Z)}+\frac{\log\log(3Z)}{L}\right). \tag{3}
$$
For $Z=N^\delta$ with fixed $0<\delta\le10^{-5}$ these are respectively $O_\delta(\|W\|_\infty SN/L^2)$ unweighted and $O_\delta(\|W\|_\infty S\log L/L)$ normalized log-weighted. This is an actual cancellation of opposite divisor parities combined with an upper bound on the unpaired rough part, not an estimate that each sign is separately small.

At $D_0=\sqrt N$ this calculation uses the base-prime dyad of the [critical floor](spectral-critical-prime-sector-floor.md), but lowers $t$ to $\sqrt N/Z$. At the *exact* cutoff $t=\sqrt N$ it instead uses $D_0=\sqrt N/Z$, and companions can extend up to the critical size. It does not remove the original dyad at the exact cutoff: for $n>N/2$ the cutoff there is $m/t<\sqrt N/2$, whereas multiplying $d\ge\sqrt N/5$ by any unit prime factor of $m$ costs at least a factor three (all units here are odd), putting that nested companion outside the cut. Other semiprimes, prime moduli not paired in this sector, and the rest of the signed discrepancy are not controlled by (3).
