# The unsmoothed exterior covariance admits a moving Type-I divisor cutoff

**Scope.** This is an estimate on the true Hardy atom covariance, with no averaging of the modulus or of the location. It removes a short-divisor summand of the exact identity $\Lambda=\mu*\log$. It is not the [central Type-I rectangle estimate](spectral-vaughan-central-type-i.md): both spatial arguments here may range on the whole unbounded exterior, and the argument uses a periodic character prefix on each physical dyad. The remaining long-divisor Gram and its signed comparison with the benchmark are not estimated.

Let $N$ be sufficiently large and even, $L=\log N$, $\alpha=1/L$, $\beta=1/8$, and put

$$
 m(x)^2=(Ne^x)^{-2\alpha}+(Ne^x)^{-2\beta},\qquad
 r_N(u)=u^{-3/2}m(\log u).
$$

In the unitary physical space $L^2(du)$ the true atom for odd $\chi\bmod N$ is given by the [physical Hardy realization](r20-operator.md)

$$
 p_\chi(u)=-\frac{\sqrt{2\pi}}{N}\,r_N(u)
          \sum_{n\le Nu}\sqrt n\,\Lambda(n)\chi(n).
$$

For $D\ge0$, replace $\Lambda(n)$ in this formula by

$$
 \Lambda_{\le D}(n)=\sum_{\substack{d\mid n\\ d\le D}}\mu(d)\log(n/d)
$$

to define $p_{\chi,\le D}$. For every physical dyad $V\le u<2V$ with $V\ge1$ and integer $0\le D\le V$, one has

$$
 \|{\bf1}_{[V,2V)}p_{\chi,\le D}\|_2
 \ll (NV)^{-\alpha}\log(2NV)
       \left(\sqrt{D/V}+D^{3/2}/V\right).
 \tag{1}
$$

The proof of (1) is unconditional; it is a bound for the physical arithmetic functions, uniform over all odd characters, including primitive characters of conductor comparable to $N$.

For fixed $K>0$, take $Y\ge\exp((K+3)(\log L)^2/\log\log L)$, $\mathsf A>(2K+5)/3$, and $D_V=\lfloor V^{2/3}L^{-\mathsf A}\rfloor$ for $V=2^jY$. Define $s_\chi=p_{\chi,\le D_V}$ on each such dyad, and $t_\chi=p_\chi-s_\chi$ there. With the original local Dirichlet GRH, for every subset $\mathcal F$ of the odd family,

$$
 \left\|\operatorname{Avg}_{\chi\ {\rm odd}}
      {\bf1}_{\chi\in\mathcal F}
      \big[(Q_Yp_\chi)\otimes(Q_Yp_\chi)-t_\chi\otimes t_\chi\big]\right\|_{\rm HS}
       =o(L^{-K}),
 \qquad Q_Y={\bf1}_{u\ge Y}.
 \tag{2}
$$

Here $t_\chi$ is taken on the exterior, and the normalization uses all odd characters even if $\mathcal F$ is a proper subset. In particular the family retained after the [conductor cutoff](r33-operator-conductor-defect.md) can be used. Either the model $D_N+K_N$ (for the full family) or the genuine same-copy diagonal for the chosen family can be subtracted from both sides of the replacement without change to the error. After the unitary log change, the [exterior separation mask](r31-operator-zero-diagonal.md) can be applied, and subsequent orthogonal compression also preserves the bound. In the latter use the R31 residue-vs-actual atom error (or its finite cutoff) separately, at the stated R31 precision.

## 1. Periodic endpoints

Put $X=Nu$, let $\chi_*$ have primitive conductor $q\mid N$, and let $r=\prod_{p\mid N,\ p\nmid q}p$, so $qr\mid N$. Inclusion–exclusion for the missing Euler factors gives $\chi(m)=\chi_*(m)\sum_{a\mid r,\,a\mid m}\mu(a)$. Thus the arithmetic sum in $p_{\chi,\le D}$ is exactly

$$
 \sum_{d\le D}\mu(d)\chi(d)\sum_{a\mid r}\mu(a)\chi_*(a)\sqrt{da}
      \sum_{b\le X/(da)}\chi_*(b)w_a(b),\qquad
 w_a(v)=\sqrt v\log(av),\quad w_a(0)=0 .
 \tag{3}
$$

In particular the modulus $N$ character on $d$ keeps precisely the original unit restriction. An odd inducing character is nonprincipal. Its prefix $S(t)=\sum_{1\le b\le t}\chi_*(b)$ is $q$-periodic. Subtract its mean over one period and write the result as $S_0(t)$. For $h\ne0$ the Fourier coefficient at $e^{2\pi iht/q}$ has modulus at most $\sqrt q/(2\pi|h|)$: distributional differentiation gives the corresponding finite Gauss sum, and primitivity gives the Gauss sum bound (it is zero at nonunits). There is no constant coefficient. Abel summation, with $w_a'$ integrable at zero, gives

$$
 \sum_{b\le t}\chi_*(b)w_a(b)
     =w_a(t)S_0(t)-\int_0^t w_a'(v)S_0(v)\,dv .
 \tag{4}
$$

The subtracted mean cancels exactly because $w_a(0)=0$.

For any coefficients $c_d$ with $|c_d|\le1$, fix $a\mid r$ and consider $\sum_{d\le D}c_d S_0(Nu/(da))$. Its frequencies are $Nh/(qad)$ for $h\ne0$. Distinct such rational frequencies have spacing at least $\Delta=N/(qaD^2)$. In a class $h/d=h_0/d_0$ in lowest terms, the combined coefficient has modulus at most

$$
 \frac{O(\sqrt q)}{|h_0|}
 \sum_{j\le D/d_0}\frac1j
 \ll \frac{\sqrt q}{|h_0|}\big(1+\log(D/d_0)\big).
$$

The sum of the squares over the distinct rationals is $O(qD)$ because $\sum_{h_0\ne0}|h_0|^{-2}<\infty$ and $\sum_{d_0\le D}(1+\log(D/d_0))^2\ll D$.

For clarity, the usual separated-frequency mean-square bound here follows by majorizing the indicator of $[V,2V]$ by a scaled smooth bump whose Fourier transform is $O(V(1+V|t|)^{-2})$. On a $\Delta$-separated set the absolute row sum is $O(V+\Delta^{-1})$, which bounds the quadratic form by this constant times the squared coefficient sum. Apply first to finite Fourier sums, or periodic Fejér sums, then pass to $L^2([V,2V])$ using periodic $L^2$ convergence and the finite number of $d$. This proves

$$
 \left\|\sum_{d\le D}c_d S_0(Nu/(da))\right\|_{L^2([V,2V])}
 \ll \sqrt{qD}\sqrt{V+qaD^2/N}.
 \tag{5}
$$

In the endpoint of (3)–(4), $\sqrt{da}\,w_a(X/(da))=\sqrt X(\log X-\log d)$. Apply (5) separately for the $\log X$ and $\log d$ coefficients, costing $\log(2NV)$ as $D\le V$. The physical atom's remaining weight after the factor $\sqrt X$ is bounded on the dyad by $O((NV)^{-\alpha}/(\sqrt N V))$. Summing over $a\mid r$ therefore bounds the endpoint norm by

$$
 \frac{O((NV)^{-\alpha}\log(2NV))}{V}
 \left(\sqrt{DV}\sqrt{q/N}\,\tau(r)
             + D^{3/2}\frac qN\sum_{a\mid r}\sqrt a\right).
$$

Both factors multiplying $\sqrt{DV}$ and $D^{3/2}$ are bounded absolutely: $q/N\le1/r$, $\tau(r)/\sqrt r=\prod_{p\mid r}2/\sqrt p$, and $r^{-1}\sum_{a\mid r}\sqrt a=\prod_{p\mid r}(p^{-1}+p^{-1/2})$; only finitely many small primes can increase those products. This gives (1) for the endpoint.

## 2. The weighted Abel integral and true Gram

For $\lambda=h/q\ne0$, rescale $v=|\lambda|^{-1}z$ in the integral of $w_a'(v)e^{2\pi i\lambda v}$. The integrals of $z^{-1/2}$ and $z^{-1/2}\log z$ against the corresponding unit-frequency oscillations over $[0,R]$ are bounded uniformly in $R$: they are absolutely integrable on $(0,1)$, and one integration by parts bounds the tail. Therefore

$$
 \sup_{t\ge0}\left|\int_0^t w_a'(v)e^{2\pi i h v/q}\,dv\right|
 \ll \sqrt{q/|h|}\,\big(1+|\log(aq/|h|)|\big).
$$

Multiplication by the coefficient bound for $S_0$ gives an absolutely summable series over $h\ne0$, bounded by $O(q(1+\log(aq)))$. To justify this expansion at the integrable singularity of $w_a'$ at zero, apply it first to Fejér sums. They are uniformly bounded by $\|S_0\|_\infty$ and converge almost everywhere; dominated convergence applies for every fixed $t$. Thus the weighted integral in (4) is $O(q\log(2aq))$ uniformly in $t$. By (3) and $aq\mid N$ its total arithmetic contribution is

$$
 O\!\left(D^{3/2}qL\sum_{a\mid r}\sqrt a\right)=O(NLD^{3/2}).
$$

After multiplying by the original physical atom weight $O((NV)^{-\alpha} V^{-3/2}/N)$ and taking the dyadic $L^2$ norm, this gives the second term in (1). This proves the full bound, with no smoothing of the real endpoint.

Now insert $D_V$. For all $Y\ge1$, the infinite geometric sum is

$$
 \sum_{j\ge0}(N2^jY)^{-2/L}\log^2(2N2^jY)\ll L^3.
$$

Indeed, for $z=\log(N2^jY)$ the summand is $O(L^2 e^{-z/L})$, and the sum of the last factor is $O(L)$. Here the other factors in (1) are bounded by $Y^{-1/6}L^{-\mathsf A/2}+L^{-3\mathsf A/2}$. Consequently uniformly by character

$$
 \|s_\chi\|_2\ll L^{3/2}
       (Y^{-1/6}L^{-\mathsf A/2}+L^{-3\mathsf A/2})
       =o(L^{-K-1})
$$

at the stated $Y$ and $\mathsf A$. Under the original local GRH, Li–Liu Proposition 6.5 as in the [fine-side exterior estimate](weak-s-exterior-fine.md) gives $\operatorname{Avg}_{\chi\ {\rm odd}}\|p_\chi\|_2^2\ll L^2$. The rank-one HS norm, Cauchy–Schwarz over the same family, and $t_\chi=Q_Yp_\chi-s_\chi$ now prove (2).

No sign or small-norm assertion is made for the Gram from $\Lambda_{>D_V}=\Lambda-\Lambda_{\le D_V}$. Those are convolution summands, not a classification of the genuine prime supports: the replacement leaves an exact long-divisor signed arithmetic target, not a prime-only truncation and not an estimate of the whole distinct-copy sector.
