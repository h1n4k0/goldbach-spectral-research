# A power-growing signed cutoff on primorials with fixed omissions

**Scope.** This complements the [growing-cutoff test for a least missing prime tending to infinity](spectral-l1-growing-cutoff-moment.md). Here the least missing prime is fixed: among primes up to a growing threshold, exactly a fixed finite set do not divide the even integer. This one-sided reduction absorbs the true signed low-cutoff terms, rather than estimating their absolute profile. It uses no GRH or averaging over even integers. The surviving profile is not estimated and Hypothesis S is not established.

Fix a nonempty finite set $\mathcal A$ of odd primes, and write

$$
 P=\prod_{r\in\mathcal A}r,\qquad
 p_*=\min\mathcal A,\qquad \Phi=p_*(p_*-1),\qquad
 \alpha=\prod_{r\in\mathcal A}\frac{r-2}{r-1},\qquad
 M=2^{|\mathcal A|}.
$$

Consider even integers $N$ with real $z=z(N)\to\infty$ for which the primes not dividing $N$ among the primes $\le z$ are exactly $\mathcal A$. Thus $p_*=p_0$ eventually, and $z\ll_{\mathcal A}\log N$ by Chebyshev. Set

$$
 \lambda=\frac{1+e^\gamma}{2},\qquad \Delta=\frac{\lambda-1}{2\lambda},\qquad
 0<\eta\le\min\!\left\{\frac18,\frac{\lambda-1}{2},
                 \frac{\Delta\alpha}{16M},\frac1{64\Phi}\right\},
 \qquad X=z^{1+\eta},
$$

where $\gamma$ is the Euler–Mascheroni constant and $\eta$ is fixed.

Use $L=\log N$, $S=\mathfrak S(N)$, the fixed nonzero $W\ge0$ in $C_c^1((1/2,9/16))$, and $Q_0,M_1$ from the [smooth bridge](spectral-signed-rectangle-smooth-bridge.md) and its [absolute-profile addendum](spectral-signed-rectangle-l1-no-jump.md). For a sufficiently large smooth-cut exponent, the single remaining-profile condition

$$
 \mathcal R_N(X):=\int_X^{7Q_0/32}\frac{M_1(t)}t\,dt
         +\frac{L}{Q_0}\int_{7Q_0/32}^{Q_0/2}M_1(t)\,dt=o(NS)
$$

implies $G_W\gg_{\mathcal A,W} S$ and hence $\gg_{\mathcal A,W} SN/L^2$ actual prime-pair representations on the test support. The [upper-tail BV estimate](spectral-l1-profile-upper-tail.md) permits replacing this profile by $\int_X^{\sqrt N L^{C_A}} M_1(t)\,dt/t$ with the same conventions on the upper cutoff as in that note. No conclusion is asserted for general bounded $p_0$.

## 1. Factor the exact small-prime part

Retain the positive normalized functional of the [one-sided test](spectral-l1-absorb-low-cutoff.md):

$$
 \mathbb E_N[f]=N^{-1}\sum_{\substack{N/2<n\le9N/16\\(n,N)=1}}
                    \Lambda(n)W(n/N)f(N-n).
$$

The same exact signed Abel step works with the real cutoff $X$ since $X\ll_{\mathcal A,\eta} L^2<7Q_0/32$. The integrated contribution of $q<X$ has weight $\log(X/q)$ and satisfies

$$
 G_W=S\int W-\mathbb E_N[\mu C_X]+O_{A,W}(L^{-A}+\mathcal R_N(X)/N),
 \qquad
 C_X(m)=S+\sum_{\substack{q<X\\(q,N)=1}}\mu(q)\log(X/q)
                       \left(\mathbf1_{q\mid m}-\frac1{\varphi(q)}\right).
 \tag{1}
$$

The endpoint $q=X$ has zero weight and $q=1$ has zero discrepancy. Only squarefree $q$ matter. Because $X<z^2$ and $P<X$, they are exactly the $d\mid P$ and the $dr<X$ with $d\mid P$ and a single prime $r>z$ not dividing $N$. These representations are unique. The part involving $d\mid P$ alone factors to

$$
 C_0(m)= S+(\mathbf1_{(m,P)=1}-\alpha)\log X
         -\sum_{d\mid P}\mu(d)\log d
                      \left(\mathbf1_{d\mid m}-\frac1{\varphi(d)}\right).
$$

In particular $C_0\ge S-\alpha\log X-O_{\mathcal A}(1)$. This is an identity with actual divisibility indicators; no prime-pair asymptotic is used.

The lower bound on $S$ comes from comparing the Euler factors below $z$ to those of the full primorial. At each omitted $r\in\mathcal A$ the ratio of the nondividing factor $r(r-2)/(r-1)^2$ to the dividing factor $r/(r-1)$ is $(r-2)/(r-1)$. Beyond $z$ keep the smaller nondividing factors to obtain a lower bound. Thus [Mertens' product theorem](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf) gives

$$
 S\ge\alpha\prod_{r\le z}(1-1/r)^{-1}
        \prod_{r>z}(1-1/(r-1)^2)
   =\alpha(e^\gamma+o(1))\log z\ge\alpha\lambda\log z.
$$

Products are over primes. Since $(1+\eta)/\lambda\le1-\Delta$, it follows that $C_0\ge\Delta S-O_{\mathcal A}(1)$.

## 2. Pay for the mixed part with the actual first moment

Let $\mathcal P_z=\{r\text{ prime}:z<r<X,\ r\nmid N\}$ and put

$$
 H(m)=\sum_{r\in\mathcal P_z}\mathbf1_{r\mid m},\qquad
 h=\sum_{r\in\mathcal P_z}\frac1{r-1},\qquad w=\eta\log z .
$$

At a fixed such $r$, every allowed $d\mid P$ has $0\le\log(X/(dr))\le w$; the condition $dr<X$ is kept, not replaced by a rectangular upper cutoff. For the progression part use $\mathbf1_{dr\mid m}\le\mathbf1_{r\mid m}$, and for the baseline use $1/\varphi(dr)=1/((r-1)\varphi(d))$. Consequently

$$
 |C_X(m)-C_0(m)|\le M w\,(H(m)+h).
$$

The reciprocal-prime Mertens estimate gives $h\le\log(1+\eta)+o(1)\le2\eta$ for sufficiently large $z$. Also $Mw\le(\Delta/16)S$ by our choice of $\eta$. Since $S\to\infty$, the deterministic prior error and the term $Mwh$ can therefore be absorbed to obtain

$$
 C_X(m)\ge(\Delta/2)S-MwH(m)
$$

for large $N$. In particular this is positive at $H=0$; on $H>0$ the negative part is bounded by $MwH$.

Ordinary Siegel–Walfisz and Abel give each $\mathbb E_N[\mathbf1_{d\mid m}]=\int W/\varphi(d)+O_{B,W}(L^{-B})$ at reduced residue $N\bmod d$, uniformly in the coprime moduli $d<X\ll L^2$, and also at $d=p_*^2$. The nonunit prime powers removed have total raw weight $O(L^2)$ per modulus. Request enough additional logarithmic savings to sum over the actual moduli with their logarithmic weights. It follows that

$$
 \mathbb E_N[C_X]=S\int W+O_{A,W}(SL^{-A}),\qquad
 \mathbb E_N[H]=h\int W+o(1),\qquad
 \mathbb E_N[\mathbf1_{p_*^2\mid m}]=\frac{\int W}{\Phi}+o(1).
$$

Let $E=\{p_*^2\mid m\}$. Because $\mu(m)=0$ on $E$ and $0\le1-\mu(m)\le2$ everywhere, the two cases $H=0$ and $H>0$ imply

$$
 (1-\mu(m))C_X(m)\ge
       (\Delta/2)S\mathbf1_E -(\Delta/2)S\mathbf1_{H>0}-2MwH(m).
$$

The overlap of $E$ and $H>0$ is covered by the second term. The expected loss after the first term is at most $(5\Delta/8)S\mathbb E_N[H]$, since $\mathbf1_{H>0}\le H$. Using $h\le2\eta\le1/(32\Phi)$, for all sufficiently large $N$ one has

$$
 \mathbb E_N[\mathbf1_E]\ge\frac{\int W}{2\Phi},\qquad
 \mathbb E_N[H]\le\frac{\int W}{16\Phi}.
$$

This leaves $\mathbb E_N[(1-\mu)C_X]\gg_{\mathcal A,W} S$. Insert into (1) together with the mean of $C_X$, and then use the hypothesis on $\mathcal R_N(X)$. Proper prime-power pairs cost $O_W(N^{-1/2}L^2)$ after normalization, so they do not affect the lower count.

For example, on $N=\prod_{r\le z,\ r\ne 3}r$ one has $p_0=3$ and $z\sim\log N$. The test then starts at $X=z^{1+\eta}$ instead of the fixed threshold $8$ for $p_0=3$. The newly absorbed range contains all primes between $z$ and $X$, which are coprime to these $N$, and some of their products with $3$. This family restriction is essential to the stated argument; the proof does not estimate $\Lambda\mu$ correlations or any part of the remaining profile.
