# Two overlapping small-prime alphabets for the true signed critical boundary

Keep the fixed-target critical-prime shell, actual hard prime box (arbitrary fixed $|E(u,v)|\le1$ and true possibly active gate), and three exact signed least-prime branches of the [signed full-small-part proof](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md). In particular $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, true weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$, and $p=P^-(m)$. Here $N$ is even, $X=\sqrt N$, $L=\log N$, and $L_2=\log L$.

Fix $0<\gamma<1$, put $Z=\exp(L^\gamma)$ and $\lambda=\log Z$. The exact $Z$-small part $r_Z(h)$ is the product of the primes below $Z$ dividing squarefree $h$. Let $\mathscr P_d,\mathscr P_k$ be arbitrary sets of primes below $Z$, allowed to depend on $N$ but not on the rational point. Retain exactly the original signed terms on the three branches for which $p\le W<Z$, every prime of $r_Z(d)$ belongs to $\mathscr P_d$, and every prime of $r_Z(k)$ belongs to $\mathscr P_k$. Write $D_{\mathscr P_d,\mathscr P_k}$ for the resulting polynomial. No cap on either small part's magnitude or number of factors, and no gap within the selected prime sets, is necessary.

For any fixed $J>0$, uniformly in $2\le W<Z$ and in the hard cuts, unconditionally

$$
\begin{split}
\int_0^1 |D_{\mathscr P_d,\mathscr P_k}(\alpha)|^2\,d\alpha
 &\ll_{\gamma,J}
 \frac{N(1+\log W)(1+L_2)}{\lambda^2}
  \prod_{\ell\in\mathscr P_d\triangle\mathscr P_k}(1+1/\ell)
  \prod_{\ell\in\mathscr P_d\cap\mathscr P_k}(1+4/\ell)
 + N L^{-J}\\
 &\ll_{\gamma,J}
 \frac{N(1+\log W)(1+L_2)}{\lambda}
 \prod_{\ell\in\mathscr P_d\cap\mathscr P_k}(1+3/\ell)
 + N L^{-J}.
\end{split}
\tag{1}
$$

The absolute values of the full and the double-centered **signed** pairings with $P$, summed across those two choices on the entire shell, are bounded by $O(\sqrt N)$ times the square root of the right side. For instance if $W$ is a fixed power of $L$ and the overlap has reciprocal prime mass at most $(1/3-\varepsilon)\log\lambda+O(1)$ for a fixed $\varepsilon>0$, the signed contribution is $o(N)$ on every sufficiently large even target. In particular disjoint sets suffice, even when *both* one-sided allocation energies are much too large. An arbitrary further selection of the two exact small parts together does not increase the upper bound, provided it depends on those parts and the target alone, not on the rough partners or the rational point.

## 1. Exact allocation multiplicity, not either marginal energy

At a true squarefree product put $b=r_Z(m)$, $v=m/b$; then $p\le W<Z$ is determined by $b$, and $r=r_Z(d)$ and $s=r_Z(k)$ give $b=rs$, $(r,s)=1$. Once $b,r$ are fixed one has $s=b/r$ and the two rough partners in $v$ are $d/r$ and $k/s$. In the small-$b$ range $b\le N^{1/10}$ they are at least $N^{.39}$, since $d/r\ge X/b$ and $k/s>t/b$. The original unit and sharp interval restrictions are exactly those in the fixed-$b,r$ signed short-divisor proof, even when $r$ has no a priori size cap. In particular the sign remains $\mu(r)\mu(d/r)$ on true support, with the common $\mu(v)$ factor on the complemented orientation. The [fixed-allocation bound and its long-lcm correction](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md#4-the-signed-positive-form-and-summation) therefore give squared energy $O_\gamma((N/b)(1+\log W)(1+L_2)/\lambda^2)$ per allocation. Restrictions on $r,s$ alone are now constants and do not alter the actual signed interval. The universal $b>N^{1/10}$ Rankin error of the [arbitrary-mask proof](weak-s-type-ii-critical-prime-few-small-prime-slots.md#1-exact-allocation-and-its-reciprocal-moment) is unchanged: bound a coefficient by $\tau(b)\tau(v)$, then use the shifted reciprocal moment, giving $O_{\gamma,J}(NL^{-J})$.

Let $T(b)$ be the number of allowed allocations of squarefree $b$. If $b$ contains a prime outside the union, $T(b)=0$. Otherwise an individual prime in the symmetric difference has a forced allocation, and one in the overlap has exactly two choices. Dropping $p\le W$ and any extra selection on $r,s$ only for the positive allocation count,

$$
\sum_{\substack{b\ {\rm squarefree}\\P^+(b)<Z}}\frac{T(b)^2}{b}
=\prod_{\ell\in\mathscr P_d\triangle\mathscr P_k}(1+1/\ell)
 \prod_{\ell\in\mathscr P_d\cap\mathscr P_k}(1+4/\ell)
$$

for the unfiltered allowable count. This is a joint moment: it is not obtained by bounding $T$ independently from either side. Cauchy over the $T(b)$ actual allocations, followed by the disjoint sum over $b$, proves the first bound in (1). For the second, use $\prod_{\ell<Z}(1+1/\ell)\ll\lambda$ and $(1+4/\ell)/(1+1/\ell)\le1+3/\ell$. Restriction to the disjoint critical arcs, and separate centering over nonzero numerators at fixed $q,\beta$, contract ordinary $L^2$. Ordinary Prime-box Parseval is $O(N)$ even with the fixed general selector, so Cauchy with the true phase $e(-N\alpha)$ gives the stated signed conclusions on all moduli, numerators and aliases.

## 2. Both true marginal reciprocal-LCM masses can be large

For a concrete disjoint choice, allocate the primes $3,5,7,\ldots$ below $Z$ alternately to $\mathscr P_d$ and $\mathscr P_k$, starting $3$ in $\mathscr P_d$. Their reciprocal masses are each $(\log\lambda)/2+O(1)$ by prime Mertens and the bounded alternating sum of decreasing reciprocals. If $\mathcal A_i$ comprises all squarefree products from its alphabet, its one-sided mass is

$$
\sum_{r,r'\in\mathcal A_i}\frac1{[r,r']}
 =\prod_{\ell\in\mathscr P_i}(1+3/\ell)\asymp\lambda^{3/2}.
$$

This order remains after requiring both $r,r'$ to have at least $\lfloor(\log\lambda)/2\rfloor$ prime factors and both to be $\le N^{1/100}$, so the large marginal moment is not due just to very small arity or impossibly large integers. To verify it, normalize the reciprocal-lcm weights to a probability measure on $(r,r')$. At each allowed prime $\ell$, independently, the weights for neither, only $r$, only $r'$, and both are $1,1/\ell,1/\ell,1/\ell$. Each marginal prime count has mean $\sum_{\ell\in\mathscr P_i}2/(\ell+3)=\log\lambda+O(1)$ and variance at most its mean. Chebyshev excludes the low-count event with probability $o(1)$. Each marginal expected logarithm is $O(\lambda)$ by $\sum_{\ell<Z}(\log\ell)/\ell\ll\lambda$, so Markov excludes the event above $N^{1/100}$ with probability $o(1)$ because $\lambda=o(L)$. A union bound gives the assertion. Nevertheless (1) with disjoint alphabets saves with fixed polylogarithmic $W$ for both large-count marginals at once.

## 3. Actual terms with many allowed primes on both sides

Take $N$ along large powers of two, $\gamma=1/2$, and the alternating alphabets above. Set $K=\lfloor(\log\lambda)/2\rfloor$ and

$$
H_j=\exp\!\left(L^{j/(2(K+1))}\right),\qquad 1\le j\le K.
$$

The intervals $[H_j,4H_j]$ are disjoint subsets of $(3,Z)$ for large $N$: successive logarithms have ratio tending to $e^2$, the first logarithm tends to $e^2$, and the last to $e^{-2}\lambda$ in relative size. By Bertrand twice, each contains at least two consecutive odd primes in the prime ordering, hence one $a_j\in\mathscr P_d$ and one $b_j\in\mathscr P_k$. Put

$$
r=3\prod_{j\le K}a_j,\qquad s=\prod_{j\le K}b_j.
$$

Choose distinct primes $g\in[1.05X/r,1.06X/r]$, $h\in[.43X/s,.44X/s]$ and set $d=rg$, $k=sh$. The ordinary prime number theorem supplies these choices, since $\log(rs)=O(\lambda(1+\log\lambda))=o(L)$, so both $g,h$ are above $Z$ and each interval has arbitrarily many primes. With $I_0=[X,2X]$, $t=N^{.49999}$, $y=9N/16$ and $W\ge3$, this gives a true squarefree $N$-unit term, $p=3$, $d/3<X$, hence an actual branch-1 summand of sign $\mu(d)\ne0$. Both exact small parts have at least $K$ factors.

For any fixed earlier exponent $\gamma'\in(0,1)$, the exact small part of $d$ at cutoff $\exp(L^{\gamma'})$ contains a prime $a_j$ with exponent $j/(2(K+1))$ in a fixed nonempty subinterval of $(\gamma'/3,\min(\gamma',1/2))$. Its logarithm therefore exceeds $L^{\gamma'/3}$ by a power of $L$, so it is outside all earlier size regimes $\log R=O(L^{\gamma'/3})$. Also for fixed $\gamma'\le1/2$, at least $(\gamma'/4+o(1))L_2$ of the $a_j$ lie below that cutoff (count exponents below $\gamma'/2$); for fixed $\gamma'>1/2$ all $K\sim L_2/4$ do. Both counts exceed the earlier unrestricted slot cap $(\gamma'/6)L_2$. This is an actual support witness outside the prior size and unrestricted slot conditions, not a lower bound on the signed covariance.

No estimate of the unrestricted coupled allocation, both full signed bands without such constraints, or weak S follows from (1).
