# Coherent short-divisor data do not determine central prime positivity

**Scope.** This is a fixed-$N$ obstruction for specified short, coherent divisor statistics, not a counterexample for the actual von Mangoldt function, arbitrary residue classes, or Hypothesis S. A reservoir of **actual shifted primes with high-factor squarefree composite complements** is proved first. A separate artificial weight on those same prime positions preserves all the stated coherent data and the actual signed composite short coefficient, while eliminating its central prime-pair sum.

Fix an integer $K\ge2$ and a fixed real $J\ge1$. Let $N$ be large and even, $L=\log N$, $S=\mathfrak S(N)$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Partition the real central interval $(N/2,9N/16]$ into $M=\lceil L^J\rceil$ equal half-open cells of length $H=N/(16M)$. There exists a fixed sufficiently small $\beta>0$, depending on $K$, such that the following assertions hold for $z=N^\beta$ and every sufficiently large $N$. Here $z$-rough means having no prime factor $<z$.

1. In every such cell $I$ the true reservoir

$$
 \mathcal C_I=\{n\in I:n\text{ prime},\ m=N-n\text{ squarefree and }z\text{-rough},
                                       \ \omega(m)>K\}
$$

has total $\lambda$-weight $\gg SH/(\beta L)$. In contrast the true prime-partner set $\mathcal P_I=\{n\in I:n,N-n\text{ both prime}\}$ has total $\lambda$-weight $O(SH/L)$.
2. There is an artificial weight $\widetilde\lambda_N$ with $0\le\widetilde\lambda_N\le(1+O(\beta))\lambda$, supported on a subset of the genuine prime positions and equal to $\lambda$ off the central interval, with no positive weight at any $\mathcal P_I$. It retains each cell total exactly. If $\delta_N=\widetilde\lambda_N-\lambda$, then for all real $y$ and every integer $d>1$ having a prime factor $<z$,

$$
 \sum_{\substack{N/2<n\le y\\n\le9N/16\\d\mid N-n}}\delta_N(n)=0,\qquad
 \sup_y\left|\sum_{\substack{N/2<n\le y\\n\le9N/16}}\delta_N(n)\right|
       \ll SH/L.                                                \tag{1}
$$

Both statements hold unchanged if the summands are multiplied by $\mu^2(N-n)$. In fact the perturbation is identically zero wherever $N-n$ is not squarefree.
3. For every split of the [broad smooth central form](spectral-broad-split-rare-support.md) with $0<a<b\le\beta$, the perturbation leaves $\lambda(n)D_N(N-n)\mathbf1_{N-n\ {\rm composite}}$ exactly unchanged **at each position**. The true prime part, and hence its prime-pair sum, is removed.

The arithmetic and construction are unconditional. Taking $J$ arbitrarily large gives arbitrarily high inverse-log precision for the normalized coherent prefix data; this is one constructed weight per $N,J$, not a single global replacement for $\Lambda$.

## 1. A true reservoir at each small relative window

On the central interval, a prime $n$ is automatically coprime to $N$, since $N/2<n<N$; thus so is $m=N-n$. On each cell $I$, sieve the true positive sequence of weights $\lambda(n)$ by the prime divisibility $p\mid m$ for $p<z$, $p\nmid N$. For a squarefree sieve modulus $d$ the condition is the reduced coherent progression $n\equiv N\bmod d$, with ordinary main term $H/\varphi(d)$. Use the maximal [Bombieri–Vinogradov theorem](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206) up to $D=\sqrt N L^{-B}$, taking $B$ sufficiently large depending on the desired inverse-log power. Its uniform maximum over prefixes and reduced residues gives aggregate error $O_A(NL^{-A})$ for each cell, including differences of two real endpoints. Passing from $\Lambda$ to $\lambda$ costs at most $O(D\sqrt N L)$ in the aggregate by the total number of proper powers, also absorbed by enlarging $B$.

The sieve has dimension one, since the local density is $1/(p-1)$ at the selected odd primes and zero elsewhere, and it is bounded away from one. Apply the [fundamental sieve, Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) with $s=\log D/\log z$, which tends to $1/(2\beta)$. Choose $\beta$ small enough that its relative $O(e^{-s})$ lower error is at most $1/2$ for all large $N$. Then the weighted mass of $z$-rough $m$ is

$$
 \gg H V_z,\qquad
 V_z=\prod_{\substack{p<z\\p\nmid N}}\left(1-\frac1{p-1}\right)
       \asymp \frac{S}{\beta L}.
$$

The additive BV error is smaller than this uniformly in the cells by choosing $A>J+3$. For the product, use the identity $1-1/(p-1)=(1-1/p)(1-1/(p-1)^2)$ at the odd unit primes, together with Mertens. Compared with the full singular series, the omitted primes dividing $N$ above $z$ contribute $1+o(1)$, since there are at most $L/\log z$ such primes and each reciprocal is $O(1/z)$. The omitted nondividing tail of absolute square order also tends to one. Removing $m$ that are not squarefree costs at most $NL\sum_{p\ge z}p^{-2}\ll NL/z$ raw for a cell, from counting positive multiples of $p^2$, negligible here.

We next bound above the part of this genuine squarefree rough mass with at most $K$ prime factors. Select the largest factor $q$ of $m=Cq$; the case $m$ prime has $C=1$. Since $m\asymp N$, $q\ge N^{1/(2K)}$ and hence $C\le N^{1-1/(2K)}$ for all sufficiently large $N$. The $q$-interval corresponding to $n\in I$ has length $U=H/C$, with $\log U\ge L/(3K)$ uniformly. The positive two-prime sieve (as in the [low-factor central estimate](spectral-broad-split-low-factor-composites.md)) on $q$ and $N-Cq$ now gives

$$
 \#\{q\text{ in interval}:q,N-Cq\text{ prime}\}
      \ll_K \frac{S H}{C L^2}+U^{1/2}\log(2U).                  \tag{2}
$$

Indeed the roots are distinct at primes not dividing $CN$, collapse to one at primes dividing $N$, and consist only of the $q$-root at primes dividing $C$. Such $C$ are odd units, with at most $K-1$ prime factors, so the extra factor $\prod_{p\mid C}(p-1)/(p-2)$ is $\le 2^K$; the dimension and root bounds are uniform. Apply the sieve at $Y=U^{1/100}$, level $U^{1/2}$; both actual prime values exceed $Y$. Sum CRT remainders $O(2^{\omega(d)})$ over the squarefree sieve moduli to get the second term of (2). The interval may be located near $N/C$, not necessarily near zero; counting its residue classes costs the same error.

After multiplying by $L$ for $\lambda$, sum (2) over squarefree $z$-rough $C$ with $\omega(C)\le K-1$. The main bound is

$$
 \ll_K \frac{SH}{L}\big(1+\log(1/\beta)\big)^{K-1},
$$

because $\sum_{z\le p\le N}1/p\ll 1+\log(1/\beta)$, and the reciprocal sum over products of $j$ distinct such primes is at most its $j$th power divided by $j!$. The combined additive errors are $O_K(N^{1-1/(4K)}L^2)$, using $H\le N$ and the upper limit on $C$, so are negligible uniformly in the cells. For prime $m$, taking just $C=1$ gives $O(SH/L)$ with absolute constant. Choose the fixed $\beta>0$ small enough that $\beta(1+\log(1/\beta))^{K-1}$ times the upper constant above is smaller than one quarter of the lower constant for the rough mass. Subtracting these low-factor and squareful masses proves the asserted high-factor reservoir bound. The choice of $J$ affects the asymptotic threshold, not the required smallness of $\beta$.

## 2. Transfer within the exact coherent null space

Write $P_I=\sum_{\mathcal P_I}\lambda(n)$ and $C_I=\sum_{\mathcal C_I}\lambda(n)>0$. On each cell set $\widetilde\lambda_N=0$ on $\mathcal P_I$ and $\widetilde\lambda_N=(1+P_I/C_I)\lambda$ on $\mathcal C_I$; leave all other values unchanged. This uses only genuine prime positions, and $P_I/C_I\ll\beta$ by the true upper and lower bounds just proved. Each cell has zero net perturbation. The support of the perturbation has squarefree $m$ with no factor $<z$: the prime $m\asymp N$ has that property as does every reservoir point. Thus (1) for $d>1$ is an exact absence of moved mass in the coherent progression. For $d=1$ all complete cells cancel and the partial cell contributes in absolute value at most $P_I$ (its positive and negative masses are both $P_I$). The same logic gives the assertion with the squarefree gate. Tests involving $r^2\mid m$ for $r>1$ also see no perturbation.

For every $b\le\beta$, at a receiving point $m\in\mathcal C_I$ every divisor $d>1$ of $m$ satisfies $d\ge z\ge N^b$. Thus its long weight $F_N(\log d)$ equals $\log d$; the equality holds also at $d=1$. The exact complete affine sum vanishes for this squarefree composite $m$, so $D_N(m)=0$. At any removed prime partner the term with the composite gate was already zero. At the remaining positions the weights are unchanged. Consequently the signed composite contribution for every specified split and for any further test weight or additional **composite** selection is unchanged pointwise, not just to the accuracy of its Euler main term. Meanwhile the prime-pair test with the left weight $\widetilde\lambda_N$ and the actual right prime weight is exactly zero.

The receiving points lie in the previously surviving $\omega(m)>K$ class with no prime $\le \exp(L/(\log L)^{12})$, not in one of the already bounded tiny sectors. The argument does not say that they themselves carry any of the signed composite main mass: their exact coefficient is zero. Rather, they can conserve the ordinary coherent inputs while removing the positive prime term, without changing the composite main mass anywhere. The construction here does not preserve arbitrary residue class statistics, a positive lower comparison with $\lambda$, or $\mu(m)$-twisted coherent tests. In particular it does not bypass the need for additional information sensitive to parity.
