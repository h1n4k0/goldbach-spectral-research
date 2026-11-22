# Removing an ultrasmall prime from the three-factor residual

**Scope.** This is a separate signed estimate inside the residual of the [three-small-factor deletion](spectral-broad-split-three-factor-deletion.md), not another change of the divisor split. The exact one- and two-small-factor sectors containing a yet smaller prime are negligible. The resulting higher-roughness signed residual, which still includes primes and many composites, is not estimated. There is no GRH assumption or conclusion on Hypothesis S.

Keep the $F_N,D_N,G_W,\mathbb E_N$ and fixed $0<a<b<1/2$ of the [broad split](spectral-broad-split-rare-support.md), and $L=\log N,\ \ell=\log L,\ S=\mathfrak S(N)$. Put

$$
 z_1=\exp(L/\ell^{30}),\qquad z_2=\exp(L/\ell^{12}),\qquad
 \omega_i(m)=\#\{p\le z_i:p\mid m,\ p\nmid N,\ p\ {\rm prime}\}.
$$

For all sufficiently large even $N$ and fixed central bounded-variation $W$, we prove the actual normalized weighted bounds

$$
 \begin{split}
 \big|\mathbb E_N[D_N(m)\mathbf1_{\omega_2=1,\ \omega_1\ge1}]\big|
     &\ll_{a,b}\|W\|_\infty S\ell^{-6},\\
 \big|\mathbb E_N[D_N(m)\mathbf1_{\omega_2=2,\ \omega_1\ge1}]\big|
     &\ll_{a,b}\|W\|_\infty S\ell^{-18}.
 \end{split}                                                       \tag{1}
$$

They also hold for the sum of absolute values after taking each complete signed orbit. Combining with the previous deletion removes every $m$ with $\omega_1\ge1$ or $\omega_2\ge3$, so one has

$$
 G_W=S\int W-
       \mathbb E_N[D_N(m)\mathbf1_{\omega_1=0,\ \omega_2\le2}]
       +O_{a,b}\!\left(\|W\|_{\rm BV}(\ell^{-2}+S\ell^{-6})\right).
 \tag{2}
$$

In particular this is a relative $o(S)$ error. The surviving coefficient itself is not asserted to be $o(S)$ in average.

## 1. Keep the full tiny product, and form the complete orbit first

We use absolute $W$ in upper estimates. Only squarefree $m$ carry weight in $D_N$. At an original unit point with $\omega_2(m)=j\in\{1,2\}$ and $\omega_1(m)\ge1$, let $s$ be the full product of the $j$ primes $\le z_2$ of $m$. These primes are coprime to $N$, distinct, and at least one is $\le z_1$. The decomposition $m=s m_>$, with $P^-(m_>)>z_2$ (and $P^-(1)=+\infty$), is unique. The $j$-fold complete orbit on these $j$ small factors, as in the broad split, has absolute weight at most $C_{a,b}L^{1-j}\prod_{p\mid s}\log p$ per divisor base of $m_>$. Thus after taking the complete signed orbits the total absolute weight is bounded by

$$
 C_{a,b} L^{1-j}\left(\prod_{p\mid s}\log p\right)2^{\omega(m_>)} .
 \tag{3}
$$

No unsigned divisor of $s$ is counted before this step.

Pair each divisor of $m_>$ with its complementary divisor. Since $m_>$ is squarefree, the $2^{\omega(m_>)}$ bases are at most twice the number of squarefree $d\mid m_>$ with $d\le\sqrt N$. In the upper bound keep only $d$ with prime factors $>z_2$ (these include $d=1$) and $(sd,N)=1$. For each fixed $s,d$, write $m=sd u$ and retain $P^-(u)>z_2$. This holds on every original point; the upper estimate can now drop the other restrictions on $u$ apart from its central interval and the primality of $n=N-sd u$. It does not assign the coefficient of a different $s$ to a genuine point.

## 2. Exact roots for the constrained sieve

Put $U=N/(sd)$, so the central $u$-interval has length $U/16$ and $U\ge N^{1/2-o(1)}$ uniformly because $s\le z_2^2$. Use the [dimension-two upper sieve](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/), Corollary 19, at sifting bound $Y=U^{1/100}$ and level $D=U^{1/2}$; $z_2<Y$ for large $N$. Exclude $N-sdu\equiv0\bmod p$ for $p<Y$ and $u\equiv0\bmod p$ for $p\le z_2$. The central prime $n>N/2>Y$ passes the first exclusions. The number of excluded roots behaves as follows:

- At $p\mid s$, there is no root from the primality form since $p\nmid N$, and the roughness root is present.
- At $p\mid d$, there is no primality root and no roughness root since $p>z_2$.
- At $p\mid N$, one has $p\nmid sd$, the primality root is $0$, and it coincides with the roughness root if the latter occurs.
- At the other primes there is one root, plus a distinct second root when $p\le z_2$.

Thus there is no two-root case at $2$. The density has fixed dimension at most two by the product comparison with at most two roots at odd primes. Each squarefree sieve modulus has CRT discrepancy $O(2^{\omega(q)})$, so the total remainder is $O(U^{1/2}\log(2U))$, as in the three-factor proof. The leading local product is bounded by

$$
 \ll \frac{1}{\log Y}\frac{d}{\varphi(d)}
       \prod_{\substack{p\le z_2\\p\nmid Ns}}
            \left(1-\frac1{p-1}\right)
 \ll \frac{S}{\log Y\log z_2}\frac{d}{\varphi(d)} .
$$

Indeed the single root at a forced prime $p\mid s$ substitutes for, rather than adds to, its primality root. Deleting the at most two factors at primes of $s$ in the second-root product costs a factor at most four because these primes are odd. For the product with all unit primes present, write $1-1/(p-1)=(1-1/p)(1-1/(p-1)^2)$ at every odd prime. Mertens and $\prod_{p\mid N}(1-1/p)^{-1}\ll S$, the latter by the positive absolute lower bound of the nondividing Euler product, give the stated uniform bound. This proves that the sifted count for this $s,d$ is

$$
 \ll \frac{U S}{L\log z_2}\frac{d}{\varphi(d)}
            + U^{1/2}\log(2U),
$$

since $\log Y\asymp L$. Only a positive upper sieve has been used on the complete-orbit absolute weights.

## 3. Sum the forced prime logarithms

Multiply this last bound by $L\|W\|_\infty/N$ for the left Mangoldt weight and by $C_{a,b}L^{1-j}\prod_{p\mid s}\log p$ from (3). The sieve remainders summed over all $s,d$ are $O_{a,b}(\|W\|_\infty N^{-1/4+o(1)})$, since $s$ ranges over at most $z_2^2=N^{o(1)}$ integers, $\sum_{d\le\sqrt N}(N/d)^{1/2}\ll N^{3/4}$, and the prime logarithm weights cost only powers of $L$. Proper prime powers in $n$ are negligible separately: the total absolute orbit weight per such point is bounded by $L\tau(m)\ll_\epsilon LN^\epsilon$, and there are $O(\sqrt N)$ points. This bound already uses the unique original $s$.

The main contribution after normalization is bounded by

$$
 \ll_{a,b}
  \|W\|_\infty\frac{S L^{1-j}}{\log z_2}
    \sum_{\substack{s\text{ admissible}\\\omega(s)=j}}
          \frac{\prod_{p\mid s}\log p}{s}
    \sum_{\substack{d\le\sqrt N,\ d\ {\rm squarefree}\\p\mid d\Rightarrow p>z_2}}
         \frac1{\varphi(d)}
 \ll_{a,b}
  \|W\|_\infty S\,L^{2-j}
     \frac{\log z_1(\log z_2)^{j-1}}{(\log z_2)^2} .
$$

The last $d$-sum is $O(L/\log z_2)$ by its finite Euler product. For $s$ designate a prime $\le z_1$ and bound the other possible prime by $\le z_2$; the Chebyshev harmonic log-prime estimate gives $\sum_{p\le x}\log p/p\ll\log x$, so the positive upper bound is $\ll\log z_1(\log z_2)^{j-1}$, allowing harmless overcount of an $s$ with two such primes. For $j=1$ the final displayed bound equals $O_{a,b}(\|W\|_\infty S\ell^{-6})$; for $j=2$ it is $O_{a,b}(\|W\|_\infty S\ell^{-18})$. This proves (1), and (2) follows from the already bounded $\omega_2\ge3$ sector and the unchanged short term. The proof does not apply the same saving to a residual with its one or two small factors only between $z_1$ and $z_2$, or to those with none below $z_2$.

## 4. The deleted class has actual shifted-prime support

For a fixed odd squarefree $s>1$ with $\omega(s)=j\in\{1,2\}$, the class with this exact $s$ is not empty or supported only on prime powers. More quantitatively, on sufficiently large even $N$ with $(s,N)=1$, and fixed $W\ge0$ with $\int W>0$, the actual normalized Mangoldt mass of **squarefree** $m=s u$ with $P^-(u)>z_2$ is $\asymp_{s,W} S/\log z_2$. All prime factors of such fixed $s$ are eventually below $z_1$. This is a count of the actual shifted-prime support, not of its signed orbit weight.

Here is the ordinary BV calculation. Within $s\mid m$, requiring $f\mid u$ for a squarefree product of primes $p\le z_2$, $p\nmid N$, is the single reduced progression $n\equiv N\bmod sf$. Its continuous mass divided by the base density $1/\varphi(s)$ is multiplicative in $f$, with prime factor $1/p$ if $p\mid s$, and $1/(p-1)$ otherwise. Truncate inclusion–exclusion for $P^-(u)>z_2$ on both an odd and an even degree of size $100\ell+O(1)$. As in the broad split's mass calculation, all products $sf$ are $N^{o(1)}$ and occur once at each degree cutoff, so maximal BV pays $O_{s,W}(L^{-10})$ in total, including removal of nonunits. The absolute model truncation error is also $O(L^{-10})$ by the factorial tail with reciprocal-prime sum $\le2\ell$. The full local product is comparable to $S/\log z_2$: use Mertens and the Euler identity above, noting that the missing factor contribution from primes dividing $N$ above $z_2$ is $1+o(1)$, since their number is at most $L/\log z_2$. The nondividing factors above $z_2$ also form a tail product $1+o(1)$. Changing the factors at the fixed primes dividing $s$ only changes the constant. Finally, the discarded $u$ with a square prime divisor above $z_2$ cost $O_W(L/z_2)$ by counting positive multiples of $sr^2$ for $r>z_2$, and proper prime powers on the $n$ side cost $O_W(N^{-1/2}L)$, so the same bound applies on actual prime $n$.

There are also literal nonzero complete orbit coefficients in the deleted class. For example take $m=3q$ with $q$ a large prime, and choose a distinct prime $n$ close to $1.13m$ by the prime number theorem. Then $N=n+m$ is even, $n/N\in I$, $(n,N)=1$, $\omega_2(m)=1$ and $\omega_1(m)\ge1$. The two large divisors $q,3q$ both lie in the affine part of the long weight and the others lie in its zero part, so $D_N(m)=\log 3>0$. This does not imply an aggregate lower bound on the signed coefficient.
