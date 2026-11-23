# An unconditional sparse-alias exclusion at critical prime denominators

Let $N$ be a large even integer, $X=\sqrt N$, $L=\log N$, and $e(z)=e^{2\pi iz}$. Retain the [critical-shell fixed prime boxes](weak-s-type-ii-critical-prime-double-centered.md) $I_u=[.740X,.745X]$, $I_v=[.715X,.720X]$, with arbitrary hard subintervals and any fixed selector $|E(u,v)|\le1$. Define $P$ and $D$ using the exact coefficients

$$
\begin{split}
p(u,v)&=-E(u,v)\log v,\quad
u,v\text{ prime in the respective boxes},\quad N/2<uv\le y,\quad (uv,N)=1,\\
d_0(d,k)&=\mu(d)\mu^2(k)\mathbf 1_{(d,k)=1},\quad
d\in I_d,\ d\ge X,\ k>t,\quad N-y\le dk<N/2,\quad (dk,N)=1,
\end{split}
$$

zero outside these conditions. Here $y\le9N/16$, $t\ge N^{.49999}$, and $I_d$ is arbitrary. Thus $P(\alpha)=\sum p(u,v)e(\alpha uv)$ and $D(\alpha)=\sum d_0(d,k)e(\alpha dk)$. These are true Vaughan weights in these boxes, with $\mu(u)=-1$ and $b_{\rm II}(v)=\log v$.

Write $\mathcal Q=\{q\text{ prime}:.8X\le q\le .9X\}$ and $\mathcal B=[-1/(10N),1/(10N)]$. For integers $j$, set

$$
T_q(j)=\sum_{uv+dk=N+qj}p(u,v)d_0(d,k).
$$

For each $q,\beta$ choose any set $\mathcal J(q,\beta)$ of at most $J$ integers, measurably as a function of $\beta$; it may vary arbitrarily with $q$, and $J$ may depend on $N$. The selected part of the *uncentered congruence term* obeys the effective unconditional bound

$$
\int_{\mathcal B}
 \sum_{q\in\mathcal Q} q\,\left|\sum_{j\in\mathcal J(q,\beta)}
                T_q(j)e(\beta qj)\right|\,d\beta
 \ll \frac{NJ}{L}.
\tag{1}
$$

In particular $J=1$ removes the actual alias $j=0$ at cost $O(N/L)$; a list of $O(L^{1-\eta})$ aliases costs $O_\eta(NL^{-\eta})$ for any fixed $0<\eta<1$. No unsigned mass assertion about all other aliases is used.

## Uniform coefficient bound

For any integer $M$, let

$$
T(M)=\sum_{uv+dk=M}p(u,v)d_0(d,k).
$$

We show $\sum_{uv+dk=M}|p(u,v)d_0(d,k)|\ll N$, a uniform stronger form of $|T(M)|\ll N$. The actual $k<X/2$ because $dk<N/2$ and $d\ge X$. In particular the prime inputs $u,v$ exceed $k$. For each $k$, $d$ is determined, and we may drop its hard and divisibility cuts for an upper bound. The congruence $uv\equiv M\pmod k$ has no such prime inputs unless $(M,k)=1$. It is enough to show

$$
\sum_{1\le k<X/2}\#\{u\in I_u,\ v\in I_v : u,v\text{ prime},\ uv\equiv M\pmod k\}
\ll \frac{N}{L}.
\tag{2}
$$

An extra factor $L$ bounds $|p(u,v)|$. The proof even allows all $k$ in (2), not only squarefree ones.

Put $R=N^{1/100}$ and, for fixed $k$, let

$$
G_k=\sum_{\substack{r\le R\\ (r,k)=1}}\frac{\mu^2(r)}{\phi(r)}.
$$

Take real weights $\lambda_d$ supported on $d\le R$, $(d,k)=1$, determined by $\sum_{r\mid d}\lambda_d/d=\mu(r)/(G_k\phi(r))$ when $r\le R$ and $(r,k)=1$, and zero otherwise on the right. The sum on the left is over multiples $d$ of $r$. Inversion on multiples gives $\lambda_1=1$, squarefree support, and $|\lambda_d|\le d/\phi(d)\le \tau(d)$: for squarefree $d$ the inverted numerator is a sum of $\mu^2(m)/\phi(m)$ over $m\le R/d$ coprime to $dk$, divided by $G_k$, times $\mu(d)d/\phi(d)$. The identity $\sum_{r\mid h}\phi(r)=h$ gives

$$
\sum_{d,e}\frac{\lambda_d\lambda_e}{[d,e]}
=\sum_r\phi(r)\left(\sum_{r\mid d}\lambda_d/d\right)^2=\frac1{G_k}.
\tag{3}
$$

For a prime in either box, $(\sum_{d\mid u}\lambda_d)^2=1$ since $u>R$; the square is nonnegative on all other integers. Use this majorant on both input sides.

To evaluate the expansion, fix two least common multiples $\ell_1,\ell_2\le R^2$ arising on the two sides. They are coprime to $k$. The congruence after the substitutions $u=\ell_1 a$, $v=\ell_2 b$ is $ab\equiv M(\ell_1\ell_2)^{-1}\pmod k$. For any two integer intervals $U,V$ of sizes $O(X)$ and any $m$ coprime to $k$, the count of $a\in U,b\in V$ with $ab\equiv m\pmod k$ is

$$
\frac{|U|\,|V|\phi(k)}{k^2}
+O\left(\tau(k)^2\sqrt{k}\,(1+X/k)\log^2(2k)\right)
\tag{4}
$$

for $k\ge2$. Indeed, the normalized residue Fourier coefficients of an interval satisfy $\widehat U(0)=|U|/k$ and $|\widehat U(h)|\ll1/\min(h,k-h)$ for $h\ne0$, even when full periods are present. The complete inner sum is a Kloosterman sum, bounded by $\tau(k)\sqrt{k}(h,j,k)^{1/2}$ by [Iwaniec–Kowalski, Corollary 11.12](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf#page=14); the unit $m$ does not change the gcd. Use $(h,j,k)^{1/2}\le\sum_{g\mid(h,j,k)}g^{1/2}$. For each $g\mid k$, the nonzero multiples of $g$ have total Fourier weight $O(\log(2k)/g)$ for either interval. Removing the pair $(0,0)$ leaves the two terms with at most one zero frequency and the term with both nonzero. Their sums over $g$ have weights $g^{-1/2}$ or $g^{-3/2}$, so they give (4). The $k=1$ leading count is exact.

For $H_u,H_v$ the lengths of the hard subintervals in the original two boxes, the scaled integer interval sizes are $H_u/\ell_1+O(1)$ and $H_v/\ell_2+O(1)$. Replacing the main count in (4) by its continuous length analogue costs $O(1+X/k)$ per term, absorbed by the same aggregate bound. Equation (3) now gives the prime-count majorant for each valid $k$:

$$
\frac{H_u H_v\phi(k)}{k^2G_k^2}
+O\left(R^4(1+\log R)^4\,\tau(k)^2\sqrt{k}\,(1+X/k)\log^2(2k)\right).
\tag{5}
$$

The interval extension only adds nonnegative weights. In deriving the error, $\sum_{d\le R}|\lambda_d|\ll R(1+\log R)$ suffices.

The positive sum $G_1\gg\log R$ follows, for example, by summing $\mu^2(r)/r$ using the elementary squarefree counting estimate. Splitting squarefree $r$ into its part supported on primes dividing $k$ and its coprime part gives $G_1\le G_k\prod_{p\mid k}(1+1/(p-1))=G_k k/\phi(k)$. Thus the main term in (5) is $O(N/(L^2\phi(k)))$. Also

$$
\sum_{k<X/2}\frac1{\phi(k)}\ll L,\qquad
\sum_{k<X/2}\tau(k)^2\sqrt{k}\,(1+X/k)\log^2(2k)\ll_\epsilon X^{3/2+\epsilon}.
$$

The first uses $k/\phi(k)=\sum_{a\mid k}\mu^2(a)/\phi(a)$ and the convergent sum $\sum_a\mu^2(a)/(a\phi(a))$; the second follows from the elementary divisor bound. Since $R^4 X^{3/2+\epsilon}=N^{.79+\epsilon/2}$, the error is power smaller than $N/L$. This proves (2) and the coefficient bound. In (1) use $T_q(j)=T(N+qj)$, Chebyshev's upper bound $|\mathcal Q|\ll X/L$, $q\ll X$, and $|\mathcal B|=1/(5N)$.

## Centered interpretation

Let $P^*,D^*$ be the additively double-centered transforms of the [critical-shell identity](weak-s-type-ii-critical-prime-double-centered.md) on the nonzero numerators. Let $C^*$ be their total signed integral on the shell, including $e(-N(a/q+\beta))$. Define

$$
S_{\mathcal J^c}=\int_{\mathcal B}\sum_{q\in\mathcal Q}q
  \sum_{j\notin\mathcal J(q,\beta)}T_q(j)e(\beta qj)\,d\beta.
$$

Then the previously bounded two projections and (1) imply

$$
C^*=S_{\mathcal J^c}
+O\!\left(\frac{NJ}{L}+\frac{N\log L}{L^2}\right).
\tag{6}
$$

This does not assign a centered weight to each alias. To see (6), the exact uncentered numerator sum, with the outside phase included, is

$$
q\sum_j T_q(j)e(\beta qj)-P(\beta)D(\beta)e(-N\beta).
$$

Its second term summed and integrated is negligible by the effective [denominator-one major bound](weak-s-type-ii-signed-seam-major-arcs.md) for $D(\beta)$, the trivial bound $|P(\beta)|\ll N/L$, and $\mathcal B$'s length. Changing $PD$ to $P^*D^*$ costs at most $O(N\log L/L^2)$ by the [full complementary principal projection](weak-s-type-ii-critical-prime-arcs-full-principal.md) and the complementary constant-mode removal.

The available alias interval has length $O(X)$, not $O(L)$. Neither (1) nor (6) estimates a dense set of aliases, the full double-centered covariance, or weak S. The proof is unconditional; it makes no use of GRH or cancellation in the arithmetic signs along a dense alias set.
