# GRH localizes the genuine large-prime boundary contribution on the entire critical shell

Keep the true fixed prime boxes, arbitrary fixed $|E(u,v)|\le1$, and sharp cuts of the [least-prime boundary reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Put $X=\sqrt N$, $L=\log N$, and $L_2=\log L$. The exact complementary terms are squarefree $m=dk$, $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m<N/2$, $(m,N)=1$, and weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. Use only the exact surviving three signed boundary types after toggling $p=P^-(m)$, with $p\le L^A$ for a fixed $A>0$.

Fix $B\ge0$ with $A+B<1$. Inside those actual three types retain every term for which

$$
d=\ell g,\qquad g\text{ prime},\quad g\ge X,\quad \ell\le L^B.
$$

Write $D_{\mathrm{giant}}$ for this signed polynomial. Under Dirichlet GRH, for every sufficiently large even $N$ its full and double-centered signed pairings with the genuine prime box on the entire critical shell are

$$
O_{A,B}\!\left(NL^{-(1-A-B)/2}(1+L_2)^4\right).
\tag{1}
$$

The critical shell uses all primes $q\in[.8X,.9X]$, all nonzero numerators, and $|\beta|\le1/(10N)$. No modulus, numerator, or alias selections are made. The rest of the actual three boundary bands is not estimated.

## 1. Exact labels and smoothed rectangles

A prime $g\ge X$ is unique in an eligible $m<N/2$ with this property, since two such prime factors have product at least $N$. For fixed $\ell$ and $p$, retain all original unit and squarefree conditions; in particular $(\ell,N)=1$, $\mu^2(\ell)=1$, $(g,N)=1$, and $(k,\ell N)=1$ are required. Since $k<X/2$ and $g\ge X$, no $g\mid k$ is possible, and since $\ell\le L^B$, no $g\mid\ell$ is possible.

If $p\mid\ell$, then $p=P^-(\ell)$ and the surviving type is exactly type 1, with $d/p$ failing the lower endpoint of $I_0$. The short coefficient on $k$ restricts its prime factors to be $>p$ by squarefreeness and the fixed gcd mask. If $p\mid k$, then $p=P^-(k)<P^-(\ell)$ (with $P^-(1)=+\infty$); the surviving types are 2 and 3, with either $pd$ failing the upper endpoint of $I_0$, or $pd\in I_0$ and $t<k\le pt$, respectively. In all cases the selected weight in a block is the exact constant $-\mu(\ell)$ times the nonnegative $k$ coefficient $\mu^2(k)$ with its indicated masks. Every interval restriction on $d$ is a sharp interval on $g=d/\ell$ for fixed labels.

For each such type and label pair, split $g\asymp G$, $k\asymp K$ into usual disjoint dyadic intervals. If the block is nonempty then $\ell G K\asymp N$. The surviving boundary condition confines either $d$ or $k$ to an interval of relative width at most $p$; the product constraint confines the other coordinate to relative width $O(p)$ as well. Hence at most $O((1+L_2)^2)$ dyadic pairs are needed for each fixed $\ell,p$ and type. Use the symbol $s=1$ when $p\mid\ell$ and $s=p$ when $p\mid k$. The $k$ coefficient has squared sum $O(K/s)$ in the block, using the multiple-of-$p$ condition when $s=p$ and the fact that $K\gg N^{.49999}$ up to an absolute factor, in particular $K/p\gg1$.

In each block, approximate inward the hard $g$ interval (including its dyadic range) by a smooth weight $w(g/G)$ and the hard product interval by $v(\ell g k/N)$, at relative width $\eta=L^{-20}$. One may convolve the interval eroded by width $\eta$ with a nonnegative smooth bump of mass one at scale $\eta$; for an interval of width at most $2\eta$ use zero. Both smooth weights are bounded by one, supported in the required intervals up to endpoints of zero weight, approximate the indicator except in relative $\eta$ boundary strips, and have first derivative $L^1$ norm $O(1)$ and second derivative $L^1$ norm $O(\eta^{-1})$. All other masks, including the $k$ interval and least-prime condition, remain exact. For fixed $\ell,p,G,K$, each $m$ has at most one representation in this block. The ordinary squared error from the $g$ strips is at most $O((\eta G+1)K)$ by counting pairs, and the product-strip error is $O(\eta N+1)$ by unique representation. Both are $O(\eta N+X)$ together. Summing error norms over $O(L^{A+B}(1+L_2)^2)$ blocks gives $O(\sqrt N L^{-2})$ or better, since $A+B<1$. This cost remains valid on the disjoint critical arcs and after subtracting numerator means.

## 2. Smooth prime character transform on the long leg

For prime $q\in[.8X,.9X]$ every nonprincipal $\chi\bmod q$ is primitive. Under GRH, uniformly for real $\tau$,

$$
\left|\sum_{\substack{g\ {\rm prime}\\(g,N)=1}}
 \chi(g) w(g/G)e(\tau\log(g/G))\right|
\ll \sqrt G(1+L_2)\left(1+\frac{\log(2+|\tau|)}L\right).
\tag{2}
$$

Here $G$ is within a factor two of the allowed prime scale, with $\log G\asymp L$. To verify (2), the compact-test explicit formula is obtained by inserting Mellin inversion against $-L'/L(s,\chi)$ and shifting past its zeros (the usual [smooth explicit formula, Iwaniec–Kowalski, Theorem 5.11](https://doi.org/10.1090/coll/053), in the one-sided test supported at positive integers $x\asymp G$). Equivalently one sums the nontrivial and trivial zero Mellin residues; there is no pole at one for this nonprincipal character. Apply it to $\Lambda(n)\chi(n)$ with test $w(n/G)e(\tau\log(n/G))/\log n$. Removing the prime powers costs $O(\sqrt G)$ by bounding the count at each exponent, since the factor at a prime power of exponent $j$ is $1/j$; removing $g\mid N$ costs $O(1)$. The trivial-zero transforms together are $O(1)$ on this support.

For a nontrivial zero $\rho=1/2+i\gamma$, the test transform at $\rho$ is bounded by

$$
C\frac{\sqrt G}{L}
 \min\!\left(1,\,(1+|\gamma+2\pi\tau|)^{-1},
              \eta^{-1}(1+|\gamma+2\pi\tau|)^{-2}\right)
$$

with a larger absolute constant in the first two factors. This follows in the log coordinate by zero, one, and two integrations by parts, using the stated derivative bounds and the smooth factor $\log G/\log(G e^z)$ on a bounded interval of $z$. The standard Dirichlet zero count on any unit ordinate interval is $O(\log(q(2+|T|)))$ at height $T$ (e.g. [Montgomery–Vaughan, Theorem 10.17](https://doi.org/10.1017/CBO9780511618314.012)). Grouping the zeros by unit distance from $-2\pi\tau$ gives a harmonic sum up to $\eta^{-1}$ and a summable $1/j^2$ tail. The sum is $O((1+L_2)\log(q(2+|\tau|))+(1+L_2)^2)$ before the factor $\sqrt G/L$, proving (2). This argument applies to the true complex-modulated smoothed weight, rather than a sharp-cut bound whose error grows with the modulation frequency.

## 3. Centered local energy and all-arc pairing

For a smoothed block and $\beta$, use the log-Mellin transform of $z\mapsto v(e^z)e(\beta N e^z)$ to separate $v(\ell gk/N)e(\beta\ell gk)$. Its Fourier transform has weighted absolute integral

$$
O(1+L_2)\quad\text{with weight}\quad
1+\log(2+|\tau|)/L,
\tag{3}
$$

uniformly in $|\beta|N\le1/10$. The support is in a fixed bounded interval and the same first and second derivative bounds give (3) by splitting the Fourier integral at $1$ and $\eta^{-1}$. The separated factors are phases at $g/G$ and $k/K$, and a constant of modulus one $e(\tau\log(\ell GK/N))$.

Every block product is a unit modulo $q$: $q<g$, $k<X/2<q$, and $\ell\ll q$. For a product transform with such unit support, its additive numerator mean is exactly $-D(\beta)/(q-1)$ on $a\ne0$. The squared sum of the numerator-centered values equals $q/(q-1)$ times the squared sum of the nonprincipal multiplicative hats, by Gauss Parseval. In the separated $(g,k)$ hats the extra factor $\chi(\ell)$ has modulus one. The $k$ values are injective modulo $q$, so multiplicative Parseval bounds their squared nonprincipal hats by $(q-1)O(K/s)$ even after any Mellin modulation. Combine this with the uniform prime bound (2), $\sum_{q\ {\rm in\ shell}}q\ll N/L$, and Minkowski in (3), to get a bound

$$
 \ll (1+L_2)^2\sqrt{\frac{G K N}{s L}}
$$

for the $\ell^2$ norm over $q$ and nonzero $a$ of the centered block at each $\beta$. Integrating the squared bound over $\beta$ of length $1/(5N)$ gives a local norm $O((1+L_2)^2\sqrt{N/(\ell s L)})$.

Use the triangle inequality over dyads and fixed labels. When $p\mid\ell$ there is only one possible least prime of $\ell$, and when $p\mid k$ the extra factor $p^{-1/2}$ is available. Thus the centered norm over the whole shell for $D_{\mathrm{giant}}$ is bounded by

$$
\ll (1+L_2)^4\sqrt{N/L}\ \sum_{\ell\le L^B}\ell^{-1/2}
               \left(1+\sum_{p\le L^A}p^{-1/2}\right)
\ll (1+L_2)^4\sqrt N\, L^{-(1-A-B)/2}.
\tag{4}
$$

This includes the smaller smoothing error from §1.

For the uncentered norm, the ordinary total absolute mass of the sharp polynomial is at most $O(N(1+L_2)^4/L)$: per block count $O(G/L)$ possible $g$ and $O(K/s)$ possible $k$, then sum the reciprocal labels and the logarithmic number of dyads. Since the support is unit modulo every shell prime, the constant part in the numerator sum has integrated squared norm at most

$$
 \ll \frac1N\sum_q\frac1{q-1}\left(N(1+L_2)^4/L\right)^2
 \ll N(1+L_2)^8/L^3.
$$

It is absorbed by (4). In both cases the true prime box has shell norm $O(\sqrt N)$ by ordinary Parseval on disjoint arcs (and by contraction after centering). Cauchy–Schwarz now gives (1) with the exact outer phase $e(-N\alpha)$.

The result is pointwise in the target but conditional on the stated GRH, and only for a genuine selected factor structure within the remaining boundary bands. It estimates neither the complementary composite sector, the full critical shell on a generic exceptional target, nor weak S.
