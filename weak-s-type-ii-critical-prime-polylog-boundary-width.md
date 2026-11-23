# The three true critical boundary bands can have fixed polylogarithmic width

Keep the exact sharp critical-shell prime and complementary polynomials $P,D$, with the original unit/gcd masks, from the [least-prime boundary reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). In particular the prime leg may have any fixed $|E(u,v)|\le1$ and an active upper product gate. Use the actual three signed boundary types and the [signed least-prime energy argument](weak-s-type-ii-critical-prime-signed-boundary-energy.md), including its interval complementation and continuous and discrete large-lcm corrections.

Write $L=\log N$, $L_2=\log L$, $L_3=\log L_2$ for sufficiently large even $N$. For any fixed $A>0$, set $Z=L^A$. With $D^{>Z}$ retaining all genuine common coefficients with least prime greater than $Z$, the unconditional estimate is

$$
\int_0^1|D^{>Z}(\alpha)|^2\,d\alpha\ll_A N/L_3 .
\tag{1}
$$

Consequently both the full and double-centered critical-shell pairings change by in total $O_A(N/\sqrt{L_3})$ upon replacing $D$ by its three signed boundary types on least primes $\le Z$. The three retained bands have multiplicative width at most $L^A$. This includes every critical modulus, numerator and alias. It is not a bound for the dense covariance of those retained bands.

## 1. What the signed argument needs

Use the exact signed orientation with short divisor at most $\sqrt n$, where $m=pn$ and $p=P^-(m)$. As in the signed proof, the original squarefree and unit restrictions are relaxed only after squaring each signed divisor sum. The extended underlying variable $n$ is $p$-rough. Write $Y=N/p$ and use the original fixed envelope of ratio $O(p)$ for each moving divisor interval. The following two parameters make its dependence explicit:
- an even Bonferroni order $r$, giving the rough count $V(p)|J|+O(|J|L^{-20}+p^{r+1})$ in any real interval $J$, with $V(p)=\prod_{\ell\le p}(1-1/\ell)\asymp1/\log p$;
- a signed cutoff $\Xi=p^\sigma$, such that every prefix $\sum_{a\le u,\,a\ p\text{-rough},\,(a,g)=1}\mu(a)/a$ is $O(L^{-20})$ for $\Xi\le u\le N$ and $g\le N$.

If $\log p\max(r,\sigma)=o(L)$ uniformly and $p^{-(r+3)}\ll L^{-20}$, the detailed small-lcm, large-lcm and positive-form steps of that proof give the fixed-$p$ signed energy bound

$$
O\!\left(\frac{Y(1+r+\sigma)}{\log p}\right).
\tag{2}
$$

Indeed, the small-lcm partition is $[a,b]\le Y/Q$, $Q=p^{2(r+2)}$. Its total floor and density error is $O(YL^{-17})$. In each large-lcm correction the remaining shared rough harmonic range has ratio $O(pQ)$, giving $O(1+r)$ instead of $O(L_2)$ in the proof with the original parameter. The same factor bounds the continuous integral with density $V(p)$; the short divisor forces $z=n/[a,b]\ge1$. Finally the large-$g$ portion of the positive signed lcm form has a harmonic range of ratio $O(p\Xi)$ and gives $O(1+\sigma)$; its other portion uses the signed prefix bound. This accounts for every occurrence of those two parameters, with the same original exact intervals.

## 2. The polylogarithmic range

Take $L^A<p\le\exp(L_2^2)$. Here $\sum_{\ell\le p}1/\ell=O(L_3)$ on primes. Thus the Bonferroni construction with the even $r$ chosen of size $C L_2/L_3$ works: its truncation gap is at most

$$
\frac{(\sum_{\ell\le p}1/\ell)^{r+1}}{(r+1)!}\ll L^{-20}
$$

by Stirling for a sufficiently large absolute $C$. The total floor count remains $O(p^{r+1})$ because every retained squarefree divisor is at most $p^{r+1}$.

The signed bound, **including** the extra $(a,g)=1$ condition, also holds with $\sigma=C_A L_2/L_3$. To see this, let $\mathscr S$ be the union of primes $\le p$ and primes dividing $g$. By the reciprocal-zeta coefficient convolution,

$$
\sum_{\substack{a\le u\\a\ p\text{-rough}\\(a,g)=1}}\frac{\mu(a)}a
=\sum_{\substack{b\le u\\\text{all prime factors of }b\in\mathscr S}}
 \frac{M_1(u/b)}b,\qquad M_1(u)=\sum_{j\le u}\frac{\mu(j)}j,
$$

with one included. Use the [effective ordinary Mertens bound](https://arxiv.org/pdf/2208.06141v5#page=5) (Theorem 2.2 (19) followed by Abel summation as in the signed proof). In particular $M_1$ is bounded everywhere and decays as $O(\exp(-c(\log u)^{3/5}(\log\log u)^{-1/5}))$ for large $u$.

For uniform Euler products put $T=\max(p,L)$ and $\delta=L_3/(2\log T)$. At shift $\delta=0$ the reciprocal product on $\mathscr S$ is $O(\log T)$. At the stated positive shift, the small-prime part satisfies

$$
\prod_{\substack{\ell\in\mathscr S\\\ell\le T}}
 (1-\ell^{-1+\delta})^{-1}
 \ll \log T\ \exp(O(\sqrt{L_2}L_3)).
\tag{3}
$$

Indeed $\delta\log T=L_3/2$ and
$\sum_{\ell\le T}(\ell^\delta-1)/\ell
 \ll \delta e^{\delta\log T}\sum_{\ell\le T}\log\ell/\ell
 \ll \sqrt{L_2}L_3$.
Higher powers are uniformly bounded since $\delta=o(1)$. For primes $\ell>T$ in $\mathscr S$ only those dividing $g$ occur. For $g\le N$ their number is at most $L/\log T$, and their contribution to the logarithm of the shifted product is

$$
\ll (L/\log T)T^{-1+\delta}
 \le \sqrt{L_2}/\log T\ll L_2^{-1/2}.
$$

In particular the product bound (3) also holds without the condition $\ell\le T$, and at zero shift the same argument with ordinary Mertens gives the asserted $O(\log T)$.

For $u\ge \Xi=p^{C_A L_2/L_3}$ the contribution of $b\le\sqrt u$ in the convolution is $O_A(L^{-20})$: $\log u\ge A C_A L_2^2/L_3$, so the ordinary stretched exponent is larger than any fixed multiple of $L_2$ asymptotically, and the unshifted reciprocal product is $O(L_2^2)$. The rest has reciprocal weight at most $u^{-\delta/2}$ times the shifted product. Now $\log T\le\max(1,A^{-1})\log p$, so by choosing $C_A$ large the factor $u^{-\delta/2}$ is at most $\exp(-25L_2)$. The product in (3) is $\exp(o(L_2))$. This proves the signed prefix requirement, with its exact extra unit mask.

Both parameters are therefore $O_A(L_2/L_3)$, with $\log p\max(r,\sigma)\ll_A L_2^3/L_3=o(L)$ and $p^{-(r+3)}\ll_A L^{-20}$. Applying (2) and summing over this prime band gives

$$
\ll_A \frac{NL_2}{L_3}
 \sum_{p>L^A}\frac1{p\log p}
 \ll_A N/L_3 .
\tag{4}
$$

The last prime reciprocal tail follows by partial summation and the prime upper bound.

## 3. Upper range and shell estimate

For $\exp(L_2^2)<p\le\exp(L^{3/4})$ use the original broad choices $r,\sigma\asymp L_2$ in the signed proof. Its parameter checks hold uniformly here: $\log p\max(r,\sigma)=o(L)$; the prime harmonic bound is $O(L_2)$; the ordinary Mertens bound at $\log u\ge C L_2\log p>C L_2^3$ is more than sufficient; and the extra gcd error $O(L^2/(p(\log p)^2))$ used there is $O(L^{-20})$. The contribution by (2) is at most

$$
O\!\left(NL_2\sum_{p>\exp(L_2^2)}\frac1{p\log p}\right)=O(N/L_2).
$$

For $p>\exp(L^{3/4})$, invoke the [absolute two-gate energy bound](weak-s-type-ii-critical-prime-boundary-two-gate-energy.md) at this cutoff; it contributes $O(N/L^{1/2})$. Disjointness of the genuine least-prime supports and Parseval give (1) from these three ranges.

The true prime energy is $O(N)$, since each product of primes in the disjoint boxes has a unique factorization of that orientation. On disjoint critical arcs, ordinary Cauchy–Schwarz bounds the full cross with $D^{>Z}$ by $O_A(N/\sqrt{L_3})$. Subtracting separate means on nonzero numerators is an orthogonal contraction, giving the identical estimate for the double-centered cross. The original signed boundary identity now yields the asserted reduction. As before, it introduces no extra restriction involving $q\mid m$ in the integer polynomial, and no averaging over targets or restriction on the alias set. The covariance of the polylogarithmic-width three signed bands and weak S remain open.
