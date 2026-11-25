# An unconditional density versus saving tradeoff for the true critical prime shell

Keep the actual prime polynomial, complementary coefficient $D$, hard interval cuts, and the critical prime shell from the [unconditional joint determinant theorem](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md). In particular $N$ is even, $L=\log N$, and $I_d\subset[\sqrt N,C\sqrt N L^\gamma]$ with fixed $C>1,\gamma\ge0$. The energy $\mathcal E_N(D)$ and the full, centered, and parity-preserving signed shell pairings are exactly those in that theorem, with the same bounded prime selector and all the original true units.

On $Y\le N\le2Y$, put $v=\log\log Y$ and choose a common real cutoff parameter $b$ with

$$
 \max(2,\log v)\le b\le v/2,\qquad
 u=v/b,\qquad z=e^b,\qquad
 K(u)=u\log(2u),\qquad
 W_Y(b)=\frac{K(u)}{e^b\log v}.
$$

There are fixed absolute constants $c,c'>0$ such that, for each choice of $b$, outside at most $O(Y e^{-cK(u)})$ even targets, one has uniformly in the original cutoffs

$$
 \mathcal E_N(D)
       \ll_{C,\gamma,\varepsilon}
             N\left(L^{-1/2+\varepsilon}+W_Y(b)\right)
 \tag{1}
$$

and each of the three actual signed pairings is

$$
 O_{C,\gamma,\varepsilon}\!
      \left(N\big[L^{-1/4+\varepsilon}+W_Y(b)^{1/2}\big]\right).
 \tag{2}
$$

For instance, $b=\sqrt{v\log v}$ gives both a signed proportion $O_{C,\gamma}(e^{-c'\sqrt{v\log v}})$ and an exceptional proportion $O(e^{-c'\sqrt{v\log v}})$. Alternatively, $b=v/f(v)$ with $2\le f(v)\le v/\log v$ gives exceptional proportion $O(e^{-c f(v)\log(2f(v))})$ and

$$
 W_Y(b)=\frac{f(v)\log(2f(v))}{\log v}\exp(-v/f(v)).
$$

Taking $f$ slowly increasing makes the former proportion tend to zero with a rate adjustable against the signed saving in (2). The earlier arbitrary fixed inverse-log exceptional count and triple-log signed scale is not replaced by the balanced example; they impose different exception tolerances. All conclusions are unconditional and pertain only to the stated shell, not an all-target assertion or Hypothesis S.

## Two true multiplicative tails

Let $R_N=\prod_{p\mid N,\ p\le z}p$ and $V_N=\sum_{p\mid N,\ p>z}1/p$. These are the actual full retained prime product and the actual omitted reciprocal mass on each target. For sufficiently large even targets $R_N$ is even. We prove the two tails jointly by a union bound, not a probabilistic independence assumption on prime divisibility.

Use the normalized sum $(2Y)^{-1}\sum_{1\le n\le 2Y}$ to dominate all exceptional even $N$ in the dyad. For any real $a>0$, expand the actual positive divisibility product for $R_n^a$ and count multiples of every squarefree divisor. Since $\#\{n\le2Y:d\mid n\}\le2Y/d$, this gives

$$
 \frac1{2Y}\sum_{n\le2Y} R_n^a
    \le\prod_{p\le z}\left(1+\frac{p^a-1}{p}\right).
$$

The logarithm of the right side is at most $O(a b e^{ab})$, because $p^a-1\le a(\log p)e^{ab}$ and
$\sum_{p\le z}(\log p)/p\ll\log z$ by the elementary Chebyshev bound and partial summation. Choose $a=(\log(2u))/(2b)$. Since $\log L=\log\log N\ge v$, the threshold $R_N>L^{F}$ with fixed $F$ has Markov bound

$$
 O\left(Y\exp\!\left(-\frac{F}{2}\,K(u)
                          +O\!\left(\sqrt{2u}\log(2u)\right)\right)\right).
 \tag{3}
$$

Take $F$ a sufficiently large absolute constant. Since $u\ge2$, (3) is $O(Y e^{-c_1K(u)})$ for an absolute $c_1>0$. In particular the needed true retained product, not just its prime count, is $\le L^F$ outside these exceptions.

Similarly, for $s>0$ use the positive expansion of the actual product for $e^{sV_n}$, obtaining

$$
 \frac1{2Y}\sum_{n\le2Y}e^{sV_n}
  \le \prod_{p>z}\left(1+\frac{e^{s/p}-1}{p}\right).
$$

The infinite product is a harmless majorant since all factors are positive and the sum of the logarithms converges at fixed $s,z$. The elementary prime upper bound gives $\sum_{p>z}p^{-2}\ll 1/(z\log z)$, by summing prime dyads. Bounding $e^{s/p}-1$ by $(s/p)e^{s/z}$ and taking $s=z(\log v)/4$, the logarithm of this product is at most

$$
 O\left(\frac{v^{1/4}\log v}{b}\right)
       =o(K(u))
 \tag{4}
$$

uniformly in the displayed $b$ range, since the ratio is
$O(v^{-3/4}\log v/\log(2u))$. For a sufficiently large absolute constant $C_0$, Markov at the threshold $V_N>C_0W_Y(b)$ now costs $O(Y e^{-c_2K(u)})$; the threshold times $s$ is $C_0K(u)/4$. The intersection of the genuine two target families satisfies both retained-product and omitted-reciprocal hypotheses. Invoke the pointwise bound of the cited theorem with this $F$ and the actual $R_N$. Its exceptional sets here depend only on target divisibility and on $Y,b$, not on any prime selector or moving cutoff. This proves (1)–(2), including the unchanged parity-preserving residual. The examples follow by substitution; in the balanced example $K(u)\asymp\sqrt{v\log v}$ and $\log W_Y(b)=-b+O(\log v)$.
