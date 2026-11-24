# More genuine critical aliases can be removed on the true signed count saddle

Keep the actual fixed proportional prime boxes, arbitrary fixed $|E(u,v)|\le1$, and real hard cuts of the [sparse-alias calculation](weak-s-type-ii-critical-prime-sparse-aliases.md). Thus $N$ is large and even, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, the genuine left prime polynomial $P$ has weight $p(u,v)=-E(u,v)\log v$ at each oriented prime pair in its original support, and $D$ is the true signed complementary polynomial with \(d\in I_d\cap[X,\infty)\), \(k>t\ge N^{.49999}\), \(N-y\le m=dk<N/2\), and all original unit and squarefree masks. Write $D_m$ for the **complete signed coefficient** of $m$ in $D$.

Let $Z_1=\exp(L^\delta)$, with $0<\delta<1$ fixed, and choose $Z_0=2$ or $Z_0=\exp(L^\gamma)$ for fixed $0<\gamma<\delta$. Put $R=\log Z_1/\log Z_0$ and let $\omega_1(m)$ count the distinct prime factors of $m$ in $[Z_0,Z_1)$. Take $D_{\rm sad}$ to be $D$ retained on the actual [count saddle](weak-s-type-ii-critical-prime-signed-count-saddle.md) for this band, with the original $p=P^-(m)\le W$ if desired. One may impose any additional mask on the product $m$ alone. Let $D_{\rm sad}(m)$ denote its coefficient, and set
$$
T_{\rm sad}(M)=\sum_{u,v}p(u,v)D_{\rm sad}(M-uv)
$$
for arbitrary integer $M$. Unconditionally, for every fixed $\epsilon>0$,
$$
\sup_{M\in\mathbb Z}|T_{\rm sad}(M)|
  \ll_{\epsilon,\gamma,\delta} N R^{-(2\log2-1)/2+\epsilon}.
\tag{1}
$$
The statement uses no prime-for-prime surrogate on the opposing leg.

For each critical-prime $q\in[.8X,.9X]$ and $\beta\in[-1/(10N),1/(10N)]$, let $\mathcal J(q,\beta)$ be any measurable choice of at most $J$ aliases. Then the selected **true congruence portion** of the numerator sum is at most
$$
\int_{|\beta|\le1/(10N)}\!
 \sum_{q\ {\rm prime}}q
  \left|\sum_{j\in\mathcal J(q,\beta)}
       T_{\rm sad}(N+qj)e(\beta qj)\right|\,d\beta
 \ll_{\epsilon,\gamma,\delta}\frac{NJ}{L}\,R^{-(2\log2-1)/2+\epsilon}.
\tag{2}
$$
In particular in the one-scale case $Z_0=2$, every fixed $\eta>0$ permits arbitrary lists with $J\le L^{1+\delta(2\log2-1)/2-\eta}$, costing $O_\eta(N L^{-\eta/2})$ after choosing $\epsilon$ sufficiently small. This extends the previous sparse-alias budget **on the genuine saddle**; it neither bounds the densely many aliases nor assigns a separate centered value to an individual alias.

## 1. Force the saddle primes on the actual shifted product

Let $K=\lfloor2\log R-10\sqrt{\log R(1+\log L_2)}\rfloor$, positive for large $N$. Every retained product has $\omega_1(m)\ge K$. For such positive integers,
$$
\mathbf1_{\omega_1(m)\ge K} \le 2^{-K}
 \sum_{\substack{h\mid m,\ h\ {\rm squarefree}\\
                  \ell\mid h\Rightarrow Z_0\le\ell<Z_1\\
                  \omega(h)\le K}}1 .
\tag{3}
$$
Indeed all subsets of any $K$ of the actual counted primes give distinct eligible divisors, including $1$. Every modulus $h$ in this sum is at most $Z_1^K=\exp(O(L^\delta\log L))=N^{o(1)}$. This truncation is essential: it does not require a prime distribution estimate at moduli as large as the full squarefree product.

For $h>1$ in this range the congruence $uv\equiv M\bmod h$ is impossible unless $(M,h)=1$, since all the actual $u,v$ exceed $h$. If $M$ is a unit, each unit class of $u$ prescribes exactly one unit class of $v$. The [Montgomery–Vaughan Brun–Titchmarsh inequality, Theorem 2, (1.10)](https://backend.production.deepblue-documents.lib.umich.edu/server/api/core/bitstreams/5adbb05b-05d0-4779-b1fd-304ec1ec257a/content#page=3), on a containing fixed interval of length $\asymp X$, gives $O(X/(\varphi(h)L))$ primes in each prescribed class in either box. The logarithmic denominator is $\log(\asymp X/h)\asymp L$ uniformly because $h=N^{o(1)}$. After summing over at most $\varphi(h)$ possible unit classes on the first side, the count of prime pairs is $O(N/(\varphi(h)L^2))$, including $h=1$ by the elementary prime upper bound. Dropping original hard masks only enlarges this positive count.

Take $m=M-uv$ in (3) for each prime pair with $m$ actually on the saddle. Swapping the positive divisor count and the prime pairs, then extending the nonnegative reciprocal totient product, gives uniformly in $M$
$$
\begin{split}
\#\{(u,v):M-uv\text{ retained}\}
 &\ll \frac{N\,2^{-K}}{L^2}
      \prod_{Z_0\le\ell<Z_1}\bigl(1+1/(\ell-1)\bigr)\\
 &\ll \frac{N}{L^2} R^{1-2\log2+\epsilon}.
\end{split}
\tag{4}
$$
The product is $O(R)$ by prime Mertens, and the loss from the square-root window in $K$ is $R^{o(1)}$ for these fixed cutoff powers. This is an upper bound on *joint* actual shifted support, not the product of standalone densities for $uv$ and $m$.

## 2. Retain the signs in the opposing coefficient

The disjoint prime boxes identify a unique oriented prime pair for each $uv$. For fixed $M$, the map from the actual prime products to $M-uv$ is therefore injective. By the [sharp ordinary complementary bound](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy), and because the mask is on the product alone, $\sum_m |D_{\rm sad}(m)|^2\ll N$. Cauchy on this true shifted pairing keeps this signed coefficient norm before using (4):
$$
 |T_{\rm sad}(M)|
 \le \left(\sum_{\substack{u,v\\M-uv\ {\rm retained}}}|p(u,v)|^2\right)^{1/2}
      \left(\sum_m |D_{\rm sad}(m)|^2\right)^{1/2}.
$$
Since $|p(u,v)|\le L$, this is (1), adjusting $\epsilon$. Formula (2) follows by the exact finite geometric sum over nonzero rational numerators (its congruence part is $q\sum_j T_{\rm sad}(N+qj)e(\beta qj)$ with the original outer phase), followed by the upper prime count $O(X/L)$ for the shell and its arc width $1/(5N)$. The constant-numerator and centering terms are **not** split into aliases here; if working with the centered shell, exclude the displayed genuine terms from its exact algebraic congruence portion and leave every other term unchanged.

The count tails removed to form $D_{\rm sad}$ and the additional omitted $P^-(m)>W$ component at polylogarithmic $W$ have their own true ordinary bounds. Neither (1) nor (2) estimates the signs of the densely many unremoved aliases, the full saddle covariance, or weak S.
