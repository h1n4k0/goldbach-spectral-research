# A broad smooth divisor split leaves a rare central support

**Scope.** This is an unconditional estimate for a genuine signed part of the central long-divisor sum. A broad smooth split makes all divisor orbits on integers with many small prime factors negligible, including the orbits crossing the cutoff transition. The surviving set has actual Mangoldt mass at most $(\log N)^{-1+o(1)}$ after normalization. This is a support estimate, not a bound on the signed weight carried by that set. No Goldbach lower bound or Hypothesis S is proved.

Fix $0<a<b<1/2$, and a bounded-variation weight $W$, with zero extension of bounded variation, on the central interval $I=(1/2,9/16]$. We use $L=\log N$, $\ell=\log L$, $S=\mathfrak S(N)$, $m=N-n$, and

$$
 \mathbb E_N[f]=\frac1N\sum_{\substack{n/N\in I\\(n,N)=1}}
                   \Lambda(n)W(n/N)f(N-n).
$$

The expectation notation is linear in $W$; it is positive when $W\ge0$. For $A\ge1$ fixed put

$$
 z=\exp(L/\ell^6),\qquad
 k=\left\lceil\frac{(A+10)\ell}{\log\ell}\right\rceil,\qquad
 \omega_z(m)=\#\{p\le z:p\text{ prime},\ p\nmid N,\ p\mid m\}.
$$

All estimates here are for every sufficiently large even $N$, with $A,a,b$ fixed.

Take a fixed smooth nondecreasing $R$, zero on $(-\infty,0]$, one on $[1,\infty)$, with

$$
 \|R^{(j)}\|_\infty\le C^{j+1}(j!)^2 \qquad(j\ge0).
$$

An explicit construction is given below. Put

$$
 F_N(s)=sR\!\left(\frac{s-aL}{(b-a)L}\right),
 \qquad
 D_N(m)=\mu^2(m)\sum_{d\mid m}\mu(d)F_N(\log d).
$$

Then the following deletion and mass bounds hold:

$$
 \begin{split}
 \left|\mathbb E_N[D_N(m)\mathbf1_{\omega_z(m)\ge k}]\right|
     &\ll_{A,a,b}\|W\|_\infty L^{-A},\\
 \mathbb E_N[\mathbf1_{\omega_z(m)<k}]
     &\ll_{A,W} L^{-1+o(1)}\qquad(W\ge0).
 \end{split}                                                     \tag{1}
$$

The first estimate in fact bounds the mass after taking the absolute value of each *complete signed orbit sum* on those integers, not of its individual divisors.

In the normalized actual central Goldbach test $G_W$, the same split gives

$$
 G_W=S\int W-\mathbb E_N[D_N(m)\mathbf1_{\omega_z(m)<k}]
                       +O_{A,a,b}(\|W\|_{\rm BV}L^{-A}).          \tag{2}
$$

Here $G_W=N^{-1}\sum_{n+m=N,\,(nm,N)=1}\Lambda(n)\Lambda(m)W(n/N)$. In particular the remaining signed coefficient generally cannot be discarded just because its support is small: a prime $m\asymp N$, which is in that support, has $D_N(m)=-\log m$.

## 1. Keep the split exact and preserve the original main term

Use the [smooth divisor bridge](spectral-signed-rectangle-smooth-bridge.md), but make the real cutoff a broad transition in $\log d$: the long weight is $F_N(\log d)$ and the short weight is $\log d-F_N(\log d)$. The two weights add to the original $\log d$ in $\Lambda(m)=-\sum_{d\mid m}\mu(d)\log d$, with no change in signs or units. Inserting $\mu^2(m)$ in the Goldbach test deletes only proper prime powers at normalized cost $O(\|W\|_\infty N^{-1/2}L^2)$.

The short term retains $S\int W+O_{A,a,b}(\|W\|_{\rm BV}L^{-A})$. In detail, complete $\mu^2(m)=\sum_{r^2\mid m}\mu(r)$ exactly, truncate at $r\le L^J$ with $J$ a sufficiently large fixed number, and use the same actual and model l.c.m. tail as in the smooth bridge. The short modulus $d$ is now at most $N^b$ and the short multiplier after factoring $\log d$ lies in $[0,1]$; counting positive multiples of $[d,r^2]$ and summing produces the same upper bound on both tails. Maximal ordinary [Bombieri–Vinogradov](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206) applies at the reduced residue $N\bmod[d,r^2]$, since $[d,r^2]\le N^b L^{2J}$. For each $r$ and fixed $(r,d)=g$, the modulus $r^2d/g$ is injective in the squarefree $d$; multiplicity, the coefficient $\log d$, and the extra removal of nonunit prime powers all cost only fixed logarithmic losses or smaller power terms, as in the bridge. Abel summation transfers this to $W$.

For the model apply the full squarefree Euler factor calculation from the bridge. Its logarithmic short moment at every hard cutoff $Y\in[N^a,N^b]$ is the same $S$ to every inverse log power by the classical zero-free-region estimate, uniformly over this range of $Y$. The short multiplier $1-R$ in $\log d$ is monotone from one to zero; averaging the hard cutoff values against its nonnegative Stieltjes variation measure of total mass one gives the same $S$. This proves the stated main term without narrowing the cutoff transition. The long term is exactly $-\mathbb E_N[D_N(m)]$.

## 2. Cancel every complete orbit, including at the smooth transition

For an explicit $R$, set $f(x)=e^{-1/x}$ for $x>0$, zero otherwise, and use the normalized indefinite integral of $f(x)f(1-x)$. On the disk $|\zeta-x|\le x/2$, $x>0$, one has $\operatorname{Re}(1/\zeta)\ge 2/(9x)$. Cauchy's formula then gives $|f^{(j)}(x)|\le j!(2/x)^j e^{-2/(9x)}$. The maximum over $x>0$ is at most $C_1^{j+1}(j!)^2$ by $j!\ge(j/e)^j$; the same derivative estimates tend to zero at the origin for each fixed order, justifying the extension there. The product rule and the fixed normalization give the stated bounds for $R$. Scaling and differentiating $F_N$ now give

$$
 \sup_{0\le s\le L}|F_N^{(j)}(s)|
          \le C_{a,b}^{j+1}(j!)^2 L^{1-j} \qquad(j\ge1).
$$

If $m$ is not squarefree then $D_N(m)=0$. For squarefree $m$ with $\omega_z(m)\ge k$, choose the least $k$ distinct primes $p_i\le z$ dividing $m$, and write $P=\prod p_i$. For each $e\mid m/P$ all choices $d=e\prod_{i\in J}p_i$, $J\subseteq\{1,\ldots,k\}$, occur. Their signed coefficient equals $\mu(e)$ times the signed $k$th finite difference of $F_N$ at $\log e$ with increments $\log p_i$. For every such orbit, including those meeting either transition endpoint, the integral formula for that difference gives the uniform absolute bound

$$
 C_{a,b}^{k+1}(k!)^2 L^{1-k}\prod_{i=1}^k\log p_i
         \ \le\ C_{a,b} L\left(\frac{C_{a,b} k^2}{\ell^6}\right)^k .
$$

All points in the derivative integral lie in $[0,\log m]\subset[0,L]$. This grouping is disjoint and does not truncate an orbit when it meets a transition: the multiplier vanishes smoothly below $N^a$. Since $C_{a,b}k^2\le\ell^3$ for large $N$, bounding the number of orbits by $\tau(m)$, using $\Lambda(n)\le L$ and $\sum_{m\le N}\tau(m)\ll NL$, gives an aggregate normalized bound $\ll_{a,b}\|W\|_\infty L^3\ell^{-3k}$. This gives the first estimate of (1), and therefore (2).

The earlier [R19](r19-arithmetic.md) and [R20](r20-arithmetic.md) arguments used complete orbit cancellation for hard-cut weights away from an explicit cutoff boundary. The [R27 one-giant reduction](r27-source-zero-small-subpower-orbit.md) likewise estimates a hard-cut boundary in its own restricted sector. Here the splitting is changed on a single central divisor leg, with the main short moment verified again. The high-order smooth difference controls *all* orbits on the indicated integers, without a hard-boundary counting argument.

## 3. An upper mass bound on the true shifted prime sequence

Assume $W\ge0$. Let $\mathcal P=\{p\le z:p\text{ prime},\,p\nmid N\}$ and $h=\sum_{p\in\mathcal P}1/(p-1)$. Mertens' reciprocal-prime estimate gives

$$
 \ell-O(\log\ell)\le h\le 2\ell
$$

for large $N$. Indeed $\log\log z=\ell-6\log\ell$; primes dividing $N$ at most $L$ remove $O(\log\ell)$, and primes dividing $N$ above $L$ remove at most $O(1/\ell)$ by counting them from their product. The difference of $1/(p-1)$ and $1/p$ is absolutely summable.

For $0<v<1$, define $u=1-v$ and take $J_0=\lceil50\ell\rceil$. Even Bonferroni gives the pointwise upper bound

$$
 v^{\omega_z(m)}
       \le \sum_{j=0}^{2J_0}(-u)^j\binom{\omega_z(m)}j .
$$

For example this follows by selecting each actual prime factor in $\mathcal P$ with independent probability $u$ and applying truncated inclusion–exclusion to the event that none is selected. Expand the binomial coefficient by divisibility by a product $d$ of $j$ distinct primes in $\mathcal P$. Each $d$ appears once in the combined sum, with coefficient of absolute value at most one, and

$$
 d\le z^{2J_0}=\exp(O(L/\ell^5))=N^{o(1)},\qquad(d,N)=1.
$$

By maximal BV and Abel summation against $W$, one can replace these $\mathbb E_N[\mathbf1_{d\mid m}]$ by $(\int W)/\varphi(d)$ at aggregate cost $O_W(L^{-10})$. To impose the unit condition on $n$ after applying the untwisted theorem costs at most $O_W(L^2)$ raw per modulus from prime powers supported on primes dividing $N$, harmless over $N^{o(1)}$ moduli. The motion in $N\bmod d$ is covered by the maximum over reduced residues, not by averaging $N$.

The difference between the truncated density polynomial and its full product $\prod_{p\in\mathcal P}(1-u/(p-1))$ is bounded in absolute value by $\sum_{j>2J_0}h^j/j!\ll L^{-10}$, using $h\le2\ell$, the factorial lower bound and the geometric ratio beyond $2J_0$. Thus

$$
 \mathbb E_N[v^{\omega_z(m)}]\le
       \left(\int W\right)e^{-(1-v)h}+O_W(L^{-10}).
$$

Choose $v=(\log\ell)^{-1/2}$ for large $N$; then $v\to0$ and $v^{-k}=\exp(o(\ell))=L^{o(1)}$. Since $\mathbf1_{\omega_z<k}\le v^{-k}v^{\omega_z}$, this proves the second estimate of (1). The absolute magnitude of $D_N(m)$ on this support need not be bounded by a constant, so the mass estimate alone supplies no error bound for the last signed term of (2).
