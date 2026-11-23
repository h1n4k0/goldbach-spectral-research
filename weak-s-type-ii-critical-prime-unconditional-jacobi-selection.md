# Unconditional selections of true critical-prime Jacobi products

This sharpens the [sparse Jacobi-product estimate](weak-s-type-ii-critical-prime-sparse-jacobi-products.md) using the [genuine complementary energy bound](weak-s-type-ii-critical-prime-true-shifted-projection.md). It does not control the dense Jacobi-product sum.

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and use the actual fixed proportional prime boxes, arbitrary hard subintervals, $N/2<uv\le y\le9N/16$, mask $(uv,N)=1$, and weight $-E(u,v)\log v$ with any $|E(u,v)|\le1$. The selector and all hard cuts can vary with $N$, but are fixed independently of the rational point $q,\beta$. The complementary $D$ has all original sharp $d\ge X$, hard $I_d$, $k>t\ge N^{.49999}$, $N-y\le dk<N/2$, and unit and gcd masks, with actual coefficient $\mu(d)\mu^2(k)$. Use the shell

$$
\mathcal Q=\{q\text{ prime}:.8X\le q\le .9X\},\qquad
\mathcal B=[-1/(10N),1/(10N)].
$$

Denote the genuine unit-centered residue masses by $p_q^*,d_q^*$, both zero at residue zero, and their exact covariance by $C(q,\beta)=q\sum_r p_q^*(r)d_q^*(N-r)$, with the $\beta$ phases included in the masses.

For $q\nmid N$, use the exact Jacobi product classes $C_\omega(q,\beta)$ of this covariance. At each $q,\beta$ select any at most $K$ nonprincipal product characters $\omega$, measurably in $\beta$, independently across primes. Unconditionally, the sum of the selected classes costs $O(KN^{3/4})$ on the shell, even when taking the absolute value of their sum separately at each $q,\beta$ before integration. The principal-product class on $q\nmid N$ costs $O(N^{1/2})$. The **entire** centered covariance at the primes $q\mid N$ costs $O(N/L)$, with no restriction on its characters. These assertions also hold with the outer unit phase $e(-N\beta)$ included. Thus any $K\le N^{1/4-\delta}$ selected nonprincipal classes with fixed $\delta>0$ have power saving, without GRH and without requiring a separable selector or an inactive prime product gate.

## Proof

Distinct prime pairs in the two disjoint boxes give distinct integers $uv$. Both prime counts are $O(X/L)$ and the weight is bounded by $L$. Consequently Parseval gives $\int_0^1|P(\alpha)|^2d\alpha\ll N$ for the stated fixed arbitrary selector and endpoints. On the other side, the cited complementary energy bound gives $\int_0^1|D(\alpha)|^2d\alpha\ll N$ for these exact sharp windows. The rational arcs are disjoint; unit centering is subtraction of the mean on the nonzero additive numerator coordinates, hence is an orthogonal contraction there. Additive Parseval gives

$$
\int_{\mathcal B}\sum_{q\in\mathcal Q}q\|p_q^*\|_2^2\,d\beta\ll N,\qquad
\int_{\mathcal B}\sum_{q\in\mathcal Q}q\|d_q^*\|_2^2\,d\beta\ll N.
\tag{1}
$$

For $q\nmid N$ the [exact product-class formula](weak-s-type-ii-critical-prime-sparse-jacobi-products.md) is

$$
C_\omega=\frac{q\overline\omega(N)}{(q-1)^2}
  \sum_{\substack{\chi,\psi\ne1\\\chi\psi=\omega}}
  \widehat p(\chi)\widehat d(\psi)J(\overline\chi,\overline\psi),
$$

where $\widehat p(\chi)=\sum_r p_q^*(r)\chi(r)$ and $\widehat d$ is defined similarly. The Jacobi modulus for every term is $\sqrt q$ if $\omega\ne1$ and one if $\omega=1$. Since $\psi=\omega\bar\chi$ is a permutation of the full character group, Cauchy–Schwarz within just this class and multiplicative Parseval bound the sum of $|\widehat p(\chi)\widehat d(\psi)|$ by $(q-1)\|p_q^*\|_2\|d_q^*\|_2$. Hence

$$
|C_\omega|\le \frac{q}{q-1}\|p_q^*\|_2\|d_q^*\|_2
\begin{cases}
\sqrt q,&\omega\ne1,\\
1,&\omega=1.
\end{cases}
\tag{2}
$$

The triangle inequality over the selected classes and Cauchy–Schwarz in (1) give $O(KN X^{-1/2})$ and $O(NX^{-1})$, respectively. No individual character estimate is used.

When $q\mid N$, do not use the Jacobi formula containing $\overline\omega(N)$. The full covariance instead is $q\sum_r p_q^*(r)d_q^*(-r)$, so its bound per modulus is $q\|p_q^*\|_2\|d_q^*\|_2$. There are at most two primes of the shell dividing $N$ for sufficiently large $N$. For each of these, the uniform two-prime residue upper bound in the [critical-prime double centering analysis](weak-s-type-ii-critical-prime-double-centered.md) applies to every nonzero residue. With the bounded selector, sharp cuts, weight $\log v$ and unit centering, it gives $|p_q^*(r)|\ll q/L$. The integrated prime energy in (1) restricted to $q\mid N$ is therefore at most $O(N/L^2)$ (a bounded number of moduli contribute $O(q^4/L^2)$ each before integration of length $1/(5N)$). Applying Cauchy–Schwarz with the full complementary energy in (1) gives $O(N/L)$ as asserted.

The estimates do not extend to a dense subset of the order-$X$ product classes by summing (2). In particular they prove neither the full squared-shell control of a smaller order than (1), nor cancellation in the unrestricted centered covariance, nor weak S.
