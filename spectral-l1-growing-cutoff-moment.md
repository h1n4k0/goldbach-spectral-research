# A growing signed cutoff from a prime-factor moment

**Scope.** The [one-sided central test](spectral-l1-absorb-low-cutoff.md) can absorb a genuinely growing initial band, without estimating its absolute rectangle profile, on sequences where the least prime not dividing the even integer tends to infinity. We use ordinary prime-distribution theorems and the actual weights, not GRH or an average over even integers. The remaining profile is still unestimated; this is neither a Goldbach asymptotic nor Hypothesis S.

Let $N$ be even, $L=\log N$, $S=\mathfrak S(N)$, and let $p=p_0$ be the least prime not dividing $N$. Assume $p\to\infty$ along the sequence under consideration. With $\gamma$ the Euler–Mascheroni constant, fix $0<c<e^\gamma$ and set

$$
 X=p(\log p)^c,\qquad
 g_N=\max\left\{\frac1{p(p-1)},\frac1{L\log L}\right\}.
$$

Keep $W\ge0$ fixed and nonzero in $C_c^1((1/2,9/16))$. Use the $M_1,Q_0$ of the [smooth bridge](spectral-signed-rectangle-smooth-bridge.md) and its [absolute-profile addendum](spectral-signed-rectangle-l1-no-jump.md). Define only the remaining profile

$$
 \mathcal R_N(X)=\int_X^{7Q_0/32}\frac{M_1(t)}t\,dt+
             \frac{L}{Q_0}\int_{7Q_0/32}^{Q_0/2}M_1(t)\,dt .
$$

For a sufficiently large fixed smooth cutoff exponent $C$, we prove

$$
 \mathcal R_N(X)=o(NSg_N)\quad\Longrightarrow\quad
 G_W\gg_{W,c} Sg_N .
 \tag{1}
$$

The guarantee is $\gg_{W,c} NSg_N/L^2$ central prime pairs, as in the earlier test. The [unconditional BV estimate](spectral-l1-profile-upper-tail.md) again allows replacing $\mathcal R_N(X)$ by $\int_X^{\sqrt N L^{C_A}}M_1(t)\,dt/t$ for fixed $A>4$ and a sufficiently large $C>C_A+1$. No growing-cutoff conclusion for bounded $p$ is claimed. For example, on primorials one has $p\sim L$ by the prime number theorem, so $c=1$ absorbs out to $X\sim L\log L$, not merely $p+1$. There are many additional prime indices in that absorbed range, because every prime above the primorial cutoff is coprime to $N$.

## 1. The signed coefficient up to the larger cutoff

Write $m=N-n$, and let $\mathbb E_N[f]$ denote the positive functional

$$
 N^{-1}\sum_{\substack{N/2<n\le9N/16\\(n,N)=1}}
     \Lambda(n)W(n/N)f(N-n).
$$

The exact Abel identity of the earlier one-sided test works with real $X$ in place of its integer $T_0$: the long multiplier is one and $\partial_t K=-1/t$ on $[1,X]$, and the integrated weight of an index $q<X$ is $\log(X/q)$. The strict convention at $q=X$ is immaterial. Indeed $p\ll L$ by Chebyshev, hence $X\ll_c L^2$, well below $7Q_0/32$ for large $N$. As $X<p^2$ for large $p$, all nontrivial contributing $q<X$ are primes. Set

$$
 \mathcal P=\{r\text{ prime}:p\le r<X,\ r\nmid N\},\qquad
 w_r=\log(X/r),\qquad w_{\max}=c\log\log p .
$$

Then the one-sided transfer is

$$
 G_W=S\int W-\mathbb E_N[\mu C_X]
         +O_{A,W}\!\left(L^{-A}+\mathcal R_N(X)/N\right),\qquad
 C_X(m)=S-\sum_{r\in\mathcal P} w_r\left(\mathbf1_{r\mid m}-\frac1{r-1}\right).
 \tag{2}
$$

The minus signs in $C_X$ come from $\mu(r)=-1$; the low-cutoff Abel part has been combined with the same $-S\mathbb E_N[\mu]$ as in the earlier test. The bound on the remainder uses the same second Abel estimate on $t\ge X$. Ordinary Siegel–Walfisz, at the reduced residues $n\equiv N\bmod r$, gives

$$
 \mathbb E_N[C_X]=S\int W+O_{A,W,c}(SL^{-A}).
 \tag{3}
$$

Here the moduli are $O_c(L^2)$, the weights and their number cost only a fixed power of $L$, and nonunit prime powers cost at most $O(L^2)$ per modulus before normalization. Request additional fixed logarithmic savings before summing. No signed progression estimate occurs in (3).

From the singular-series Euler factors and the definition of $p$,

$$
 S\ \ge\
   \prod_{r<p}\left(1-\frac1r\right)^{-1}
     \prod_{r\ge p}\left(1-\frac1{(r-1)^2}\right)
  = (e^\gamma+o(1))\log p
$$

as a lower bound (both products are over primes). The tail product tends to one by absolute convergence, and the first product uses the [Mertens prime product theorem, Theorem 3.4(c) in Koukoulopoulos](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf). In the inequality the replacement of a factor at a prime dividing $N$ by $1-1/(r-1)^2$ can only decrease it. Let $H(m)=\sum_{r\in\mathcal P}\mathbf1_{r\mid m}$. Fix $1<\kappa<e^\gamma/c$ and take $k=\lceil\kappa\log p/\log\log p\rceil$. Explicitly choose any $\delta>0$ with $2\delta<1-c\kappa/e^\gamma$. For sufficiently large $p$,

$$
 C_X(m)\ge S-w_{\max}H(m)\ge \delta S\quad\text{on }H(m)<k,\qquad
 (C_X(m))_-\le w_{\max}H(m)\quad\text{always}.
 \tag{4}
$$

Unlike the earlier fixed-cutoff test, (4) need not give positivity at every individual $m$.

## 2. Control the actual exceptional mass

Expand $\binom{H(m)}k$ over $k$ distinct primes from $\mathcal P$. For each subset its product $d$ is coprime to $N$ and satisfies

$$
 d\le X^k=\exp\left(O_c\big((\log p)^2/\log\log p\big)\right)=N^{o(1)}
$$

uniformly, since $p\ll L$. For primes $n\le N$ in the reduced residue $N\bmod d$, the [Montgomery–Vaughan Brun–Titchmarsh inequality, Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=3) bounds their total normalized $\Lambda W$ weight by $O_W(1/\varphi(d))$: use the full interval up to $N$ and $\log(N/d)\asymp L$. Deleting nonunits only decreases this upper bound. The proper prime powers in $n$ cost $O_W(N^{-1/2}L)$ per subset; there are at most $X^k$ subsets, so their total is $O_W(N^{-1/3})$ for large $N$. Consequently

$$
 \mathbb E_N\!\left[\binom Hk\right]\ll_W
          \frac{h^k}{k!}+N^{-1/3},
 \qquad h=\sum_{r\in\mathcal P}\frac1{r-1}
       \ll_c\frac{\log\log p}{\log p}.
 \tag{5}
$$

The factorial comes from retaining distinct primes and expanding the $k$th power of $h$. The upper estimate for $h$ follows by partial summation on $[p,X]$ using $\pi(u)\ll u/\log u$: the endpoint is $O(1/\log p)$ and the integral is $O(\log(\log X/\log p))$. By $k!\ge(k/e)^k$ and $\kappa>1$, the first term on the right of (5) is at most $p^{-2\kappa+o(1)}=o(p^{-2})$. Indeed $\log(eh/k)\le -2\log\log p+O_c(\log\log\log p)$ whenever $h>0$; if $h=0$ the bound is automatic. The proper-power error is also $o(p^{-2})$, as $p\ll L$.

Let $E$ be either square-divisibility event used in the earlier one-sided test: $p^2\mid m$, or $r^2\mid m$ for some prime $4L\le r\le8L$ not dividing $N$. On $H<k$, (4) gives $(1-\mu(m))C_X(m)\ge\delta S\mathbf1_E$ since $E$ implies $\mu(m)=0$. On $H\ge k$ we still have $(1-\mu(m))C_X(m)\ge-2w_{\max}H(m)$, by $0\le1-\mu(m)\le2$. Combining the cases yields

$$
 \mathbb E_N[(1-\mu)C_X]\ge
       \delta S\mathbb E_N[\mathbf1_E] -
       \mathbb E_N[\mathbf1_{H\ge k}(\delta S+2w_{\max}H)].
$$

For integer $H\ge k$, $1\le\binom Hk$ and $H\le k\binom Hk$. Thus the loss above is bounded by $(\delta S+2w_{\max} k)\mathbb E_N[\binom Hk]=o(S/p^2)$ by (5) and $w_{\max}k=O_c(S)$. This bound also accounts for the possible intersection of $E$ with $H\ge k$.

The two real square-divisibility masses have respectively the uniform lower bounds $\gg_W 1/[p(p-1)]$ and $\gg_W 1/(L\log L)$ by Siegel–Walfisz and two-term Bonferroni, as proved in the [earlier fixed-cutoff test](spectral-l1-absorb-low-cutoff.md). All intersection moduli there are $O(L^4)$; no use of Siegel–Walfisz for the products in (5) is made. Choose the stronger event and use (2)–(3). We obtain a gap $\gg_{W,c} Sg_N$, up to $o(S/p^2)+O_{A,W,c}(SL^{-A}+\mathcal R_N(X)/N)$. This proves (1), since $g_N\ge p^{-2}$ and $g_N\ge1/(L\log L)$. Removing proper prime powers and dividing by the maximum raw pair weight $O_W(L^2)$ gives the stated count. The new step is a bound at a single fixed modulus on the possible negative part of the absorbed signed coefficient, not a bound on the absolute $M_1(t)$ in the absorbed or surviving range.
