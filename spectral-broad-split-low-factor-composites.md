# Two-prime sieve bounds for actual low-factor central coefficients

**Scope.** This proves two signed-component bounds for the genuine broad smooth central split, rather than just support counts. The first removes part of the remaining one- and two-small-factor sectors across their entire permitted small-prime band. The second gives an arbitrarily small budget for composites with any fixed bounded number of prime factors, after choosing the free split parameter. It does not estimate the full remaining signed weight or prove central positivity or Hypothesis S.

Use the notation $I=(1/2,9/16]$, $m=N-n$, $L=\log N$, $\ell=\log L$, $S=\mathfrak S(N)$, $D_N(m)$, $F_N(s)$ and $\mathbb E_N$ of the [broad split](spectral-broad-split-rare-support.md), with fixed $0<a<b<1/2$ and fixed central BV $W$. Let $\mathbb E_N^{|W|}$ be the same normalized sum with weight $|W|$. For the first bound use $z_1=\exp(L/\ell^{30})$, $z_2=\exp(L/\ell^{12})$ and $\omega_i$ of the [ultrasmall deletion](spectral-broad-split-ultrasmall-factor.md). Write $\omega_>(m)=\#\{p>z_2:p\mid m\}$, and $J=\lfloor\log\ell\rfloor$.

1. For $j=1,2$, on the exact surviving selection $\{\omega_1=0,\ \omega_2=j,\ \omega_>\le J\}$,

$$
 \mathbb E_N^{|W|}\big[|D_N(m)|\mathbf1_{\omega_1=0,\ \omega_2=j,\ \omega_>\le J}\big]
          \ll_{a,b}\|W\|_\infty S\,\ell^{6-12j}.                  \tag{1}
$$

Thus this is an actual $o(S)$ bound, even though the one or two small factors can lie anywhere in $(z_1,z_2]$. In (1) the same bound holds for the sum of absolute values taken after each complete small-factor signed orbit and before summing the orbit bases.

2. For each **fixed** integer $K\ge2$, choose the split with $a=b/2$, $0<b\le1/(4K)$, using the same fixed shape $R$. Independently of the $\omega_i$ classifications,

$$
 \mathbb E_N^{|W|}\big[|D_N(m)|\mathbf1_{2\le\omega(m)\le K}\big]
 \ll_{K}\|W\|_\infty\big[S\,b(1+\log(1/b))^{K-2}
                         +L^3N^{-1/(4K)}\big].                 \tag{2}
$$

Here $\omega(m)$ counts all distinct primes of $m$. The constant is independent of $b$ in the stated interval (with the asymptotic range allowed to depend on fixed $b$); the shape $R$ is fixed. For fixed $W\ge0$ with $\int W>0$ and any prescribed $\varepsilon>0$, first choose $b$ sufficiently small that the first term is at most $(\varepsilon/2)S\int W$, then take $N$ large. This gives budget $\varepsilon S\int W$ for that composite sector, not $o(S)$ for each arbitrary fixed $b$. A prime $m$ is not discarded.

All estimates are unconditional at every sufficiently large even $N$.

## 1. The exact two-prime upper sieve

On any squarefree unit $m$ under consideration select its largest prime $q$ and write $m=Cq$, with $(C,N)=1$. The integer $C$ is odd. With $U=N/C$, the central $q$-interval is of length $U/16$ and lies between $7U/16$ and $U/2$. For any upper estimate one may remove the test that $q$ is largest after bounding $C$ and the weights using that test. We still sieve for both $q$ and $n=N-Cq$ prime, not just one of them.

Use the same [dimension-two upper sieve](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) (Corollary 19) at $Y=U^{1/100}$, $D=U^{1/2}$ as in the three-factor deletion. Both actual primes exceed $Y$ when $U$ tends uniformly to infinity. At $p\mid C$ the second form has no root, so there is just the root $q\equiv0\bmod p$; at $p\mid N$ there is just one root because the two coincide. At all other primes there are two distinct roots. In particular $2\mid N$ causes no zero local factor. The fixed dimension follows from at most two roots at odd primes, with the single root at $2$. The CRT error is $O(2^{\omega(d)})$ for each squarefree sieve modulus $d$; the total is $\ll U^{1/2}\log(2U)$.

Divide the local product by $\prod_{p<Y}(1-1/p)^2$. Its factor for $p\mid N$ is $(1-1/p)^{-1}$, otherwise $1-1/(p-1)^2$, except that for $p\mid C$ we gain a factor $(p-1)/(p-2)$ compared with the corresponding $p\nmid CN$ case. The truncated singular product without the extra $C$-factor is $O(S)$, since omitted nondividing tails have a positive absolute lower bound and omitted dividing terms are at least one. The sifted number is therefore at most

$$
 \ll \frac{U S}{(\log U)^2}\prod_{p\mid C}\frac{p-1}{p-2}
                     + U^{1/2}\log(2U).                         \tag{3}
$$

The product over all prime factors of $C$ only increases the bound. The normalizing left weight is at most $L\|W\|_\infty/N$. Proper prime powers on that side are always treated separately; there are $O(\sqrt N)$ and $|D_N(m)|\le L\tau(m)\ll_\delta L N^\delta$ for fixed $\delta>0$.

## 2. Remove one or two genuine tiny factors with few other prime factors

For (1) squarefree $m$ has $j$ small factors with product $s$, uniquely determined, and $r=\omega_>\in[1,J]$. The case $r=0$ is impossible on $m\asymp N$ since $s\le z_2^2$. The chosen largest $q>z_2$ satisfies $q\ge (m/s)^{1/r}\ge N^{1/(2J)}$ for all sufficiently large $N$, hence $C\le N^{1-1/(2J)}$. Write $C=s d$, with all prime factors of $d$ greater than $z_2$, and $\omega(d)=r-1$. This representation for each $C$ is unique. In (3) the $C$-factor is bounded by an absolute constant: the at most two factors from $s$ cost at most four, and the rest have product $\le \exp(O(J/z_2))$.

After summing the complete signed orbit on the $j$ small factors for each rough base, the absolute orbit weight is at most

$$
 C_{a,b}L^{1-j}\left(\prod_{p\mid s}\log p\right)2^r .
$$

This uses the fixed-order Gevrey derivative estimate, and holds before possible cancellation among the rough bases. Inserting (3), the main normalized bound is

$$
 \ll_{a,b} \|W\|_\infty S J^2 L^{-j}
    \sum_{s}\frac{\prod_{p\mid s}\log p}{s}
        \sum_{0\le h<J}2^{h+1}\frac{H^h}{h!},
 \qquad H=\sum_{z_2<p\le N}\frac1p .
$$

Here $J^2$ comes from $\log U\ge L/(2J)$. We summed the rough squarefree products $d$ of $h=r-1$ distinct primes by their reciprocal weights, at cost $H^h/h!$. For $s$, the harmonic prime-log estimate gives $\ll(\log z_2)^j$, even when enlarging to all primes $\le z_2$. Mertens gives $H\le13\log\ell$ for large $N$. For $h\le J$, Stirling's elementary lower bound gives

$$
 (2H)^h/h!\le \exp\!\big(h\log(26e\,\log\ell/h)\big)
        \le \ell^{\log(26e)}
 \quad(h\ge1),
$$

because the exponent increases in $h$ up to $\log\ell$. Thus the $h$-sum is $O(\ell^5)$ and $J^2\ell^5\le\ell^6$ for sufficiently large $N$.

The additive errors in (3), using that each $C$ appears once for each fixed $j$, sum after normalizing to

$$
 O_{a,b}\!\left(\|W\|_\infty L^3 2^J N^{-1/(4J)}\right),
$$

by $\sum_{C\le N^{1-1/(2J)}} (N/C)^{1/2}\ll N^{1-1/(4J)}$. These errors and the separate proper-power errors are smaller than every fixed inverse log power. This proves (1).

## 3. An arbitrarily small budget for bounded-factor composites

Define the short function $A_N(t)=t-F_N(t)=t(1-R(2t/(bL)-1))$ for the choice $a=b/2$. For squarefree composite $m$, the full affine divisor sum $\sum_{d\mid m}\mu(d)\log d$ vanishes, so

$$
 D_N(m)=-\sum_{d\mid m}\mu(d)A_N(\log d).
$$

Only prime factors $\le N^b$ can enter the nonzero support of this short function. If there are none, the displayed sum vanishes; the $d=1$ term is zero. If these small factors are $p_1,\ldots,p_j$, their full short Möbius sum is the $j$-fold signed finite difference of $A_N$ at zero, with increments $\log p_i$. Because $A_N(t)=bL\,F_*(t/(bL))$ with fixed smooth $F_*(x)=x(1-R(2x-1))$ for $x\ge0$, its absolute value is at most

$$
 B_j (bL)^{1-j}\prod_{i=1}^j\log p_i
$$

for constants $B_j$ independent of $b$. This takes the full short signed sum before bounding it, including the cut transition. For example, for a semiprime $m=pq$ with $p<q$, since $q>N^b$ one has exactly $D_N(m)=A_N(\log p)\ge0$.

When $m$ has $2\le r\le K$ factors, its largest $q$ is $\ge N^{1/(2K)}>N^b$ for sufficiently large $N$, so all these $j$ small factors belong to $C=m/q$. Hence $1\le j\le r-1$ when the coefficient is nonzero, and the factor in (3) is at most $2^K$ because $C$ has at most $K-1$ odd prime factors. The harmonic sum over $C$ with its logarithmic weights is bounded by

$$
 C_K (bL)^j\big(1+\log(1/b)\big)^{r-1-j}.
$$

Each designated small prime contributes at most $\sum_{p\le N^b}\log p/p\ll bL$, and each other prime at most $\sum_{N^b<p\le N}1/p\ll1+\log(1/b)$. Distinctness, the order and the product condition can all be dropped for this positive bound. Multiplying by $(bL)^{1-j}$ and using $\log U\ge L/(2K)$ in (3) gives precisely the main bound in (2) after summing the finitely many $j,r$. The additive errors are $O_K(\|W\|_\infty L^3 N^{-1/(4K)})$ since $C\le N^{1-1/(2K)}$, each $C$ has its classified factors uniquely, and the absolute coefficient is $\le C_K L$. The separate proper-power terms on the $n$ side are smaller. This proves (2).

## 4. A remaining signed weight must persist

These estimates concern prime factors of the integer $m$ in a central Goldbach test and the exact smooth single-leg coefficient. They are different from the earlier [critical prime–semiprime pairing](spectral-critical-opposite-parity-pairing.md), which compares types of **divisors** inside a hard complementary cutoff.

The persistent obstruction can already be quantified without assuming Goldbach. Pointwise on composite squarefree $m$, $D_N(m)$ is exactly the short-leg coefficient by the affine cancellation just used. At prime $m\asymp N$ the short coefficient is zero; at nonsquarefree $m$ both coefficients carry $\mu^2(m)=0$. Thus the short main-term proof gives

$$
 \mathbb E_N[D_N(m)\mathbf1_{m\ {\rm composite}}]
          =S\int W+O_{A,a,b}(\|W\|_{\rm BV}L^{-A})
$$

with no assertion about the magnitude of individual signed pieces. Fix nonnegative $W$ of positive integral and choose $b$ as in (2) for a prescribed $\varepsilon>0$. After also making the three-small-factor and ultrasmall deletions, and (1), the remaining **composite** sector with $\omega_1=0,\ \omega_2\le2,\ \omega(m)>K$ and $\omega_> > J$ whenever $\omega_2\in\{1,2\}$ still has aggregate signed weight at least $(1-\varepsilon)S\int W-o(S)$. Each removal bounds the normalized sum of $|D_N(m)|$ over its own class, so overlaps can be removed once without any additional cancellation assumption. In particular the uniform removal of bounded-factor composites does not turn the remaining composite weight into a small error. The full test still needs to distinguish the genuine helpful prime term $D_N(m)=-\log m$; simply asking the surviving composite weight to be $o(S)$ would contradict the signed main term above.
