# A near-linear exterior Type-I cutoff for the high-conductor Gram

**Scope.** An unsmoothed replacement in the actual exterior covariance. It extends the cutoff of the [previous exterior Type-I estimate](r34-operator-exterior-type-i.md) on early and intermediate exterior dyads for the retained high conductors. It is not a bound on the remaining signed covariance.

Let $N$ be sufficiently large and even, $L=\log N$, $\alpha=L^{-1}$, $\beta=1/8$, and

$$
 m(x)^2=(Ne^x)^{-2\alpha}+(Ne^x)^{-2\beta},\qquad
 r_N(u)=u^{-3/2}m(\log u).
$$

In physical $L^2(du)$ write the [exact atom](weak-s-exterior-fine.md) for odd $\chi\bmod N$ as

$$
 p_\chi(u)=-\frac{\sqrt{2\pi}}{N}r_N(u)
      \sum_{n\le Nu}\sqrt n\,\Lambda(n)\chi(n).
$$

Write $p_{\chi,\le D}$ for its replacement using
$\Lambda_{\le D}(n)=\sum_{d\mid n,\ d\le D}\mu(d)\log(n/d)$.
Fix $K>0$, $\mathsf A>2K+5$, $\mathsf B>K+4$, and choose a real threshold $1\le q_0\le N$. For $Y\ge1$ and dyads $V=2^jY$, $j\ge0$, choose any common integer cutoffs

$$
 0\le D_V\le \min\{VL^{-\mathsf A},\sqrt{q_0}L^{-\mathsf B}\}.
 \tag{1}
$$

Let $s_\chi=p_{\chi,\le D_V}$ on each dyad, $t_\chi=Q_Yp_\chi-s_\chi$ on the exterior, and $Q_Y={\bf1}_{u\ge Y}$. The squared $L^2$ budget of $s_\chi$ over the high-conductor subset satisfies

$$
 \left(\operatorname{Avg}_{\chi\ {\rm odd}}
       {\bf1}_{q_\chi\ge q_0}\|s_\chi\|_2^2\right)^{1/2}
 \ll L^{3/2+o(1)}\big(L^{-\mathsf A/2}+L^{3/2-\mathsf B}\big)
 =o(L^{-K-1})
 \tag{2}
$$

unconditionally, uniformly in $Y,q_0$ and the cutoffs. Under the original local Dirichlet GRH the actual covariance therefore satisfies

$$
 \left\|\operatorname{Avg}_{\chi\ {\rm odd}}{\bf1}_{\chi\in\mathcal F}
 [ (Q_Yp_\chi)\otimes(Q_Yp_\chi)-t_\chi\otimes t_\chi]\right\|_{\rm HS}
 =o(L^{-K})
 \tag{3}
$$

for every subfamily $\mathcal F$ of the odd characters with primitive conductor at least $q_0$. The average is always normalized by the total number of odd characters modulo $N$. Subtracting the same-copy benchmark for the chosen family and applying the [logarithmic separation mask](r31-operator-zero-diagonal.md) and then any orthogonal compression preserve the estimate. To compare with the finite zero residual in that estimate, take physical $Y=e^H$ with its stated logarithmic threshold $H$, and add its separately proved residue error.

For the high-conductor family left by the [conductor-defect cutoff](r33-operator-conductor-defect.md) one can take $q_0=N\exp[-C(\log L)^2/\log\log L]$ with fixed $C>K+3$. At the largest allowed cutoffs in (1), the first branch is essentially linear in $V$ until $V$ reaches $\sqrt{q_0}L^{\mathsf A-\mathsf B}$. More generally, for every fixed $0<\eta<3/4$, whenever

$$
 \exp((K+3)(\log L)^2/\log\log L)\le V\le N^{3/4-\eta},
$$

the cutoff in (1) exceeds the earlier exterior $V^{2/3}L^{-\mathsf A_0}$ cutoff by a factor tending to infinity, for any fixed admissible $\mathsf A_0>(2K+5)/3$. In the unsaturated branch the ratio is $V^{1/3}L^{\mathsf A_0-\mathsf A}$; in the saturated branch it is $\sqrt{q_0}V^{-2/3}L^{\mathsf A_0-\mathsf B}$, which grows by a fixed power of $N$ in the displayed range. Floors are immaterial there. For arbitrarily larger $V$, the capped cutoff need not improve the previous theorem.

## 1. Conductorwise orthogonality below the rational alias threshold

Fix a conductor $q\mid N$ with $q\ge q_0$ and a dyad $[V,2V)$ with $D=D_V\ge1$. Write $X=Nu$, $L_V=\log(2NV)$, and $r=\prod_{p\mid N,\ p\nmid q}p$, so $qr\mid N$. As in the exterior Type-I estimate, inclusion–exclusion yields the arithmetic expression

$$
 \sum_{d\le D}\mu(d)\chi(d)\sum_{a\mid r}\mu(a)\chi_*(a)\sqrt{da}
                 \sum_{b\le X/(da)}\chi_*(b)w_a(b),\qquad
 w_a(v)=\sqrt v\log(av),\quad w_a(0)=0,
 \tag{4}
$$

where $\chi_*$ is the primitive inducing character. Replace $\chi(d)$ in (4) by $\chi_*(d){\bf1}_{(d,r)=1}$. The prefix $S(t)=\sum_{b\le t}\chi_*(b)$ is periodic modulo $q$ on $t\ge0$. Write $S_0$ for its mean-zero periodic version. Abel summation in (4) splits into endpoint $w_a(t)S_0(t)$ and integral $-\int_0^t w_a'(v)S_0(v)\,dv$ with $t=X/(da)$. The mean cancels since $w_a(0)=0$.

For $h\ne0$ the exact Fourier coefficient of $S_0$ is $\tau(\chi_*)\overline{\chi_*}(-h)/(2\pi i h)$, with $\tau(\chi_*)=\sum_{b\bmod q}\chi_*(b)e^{2\pi i b/q}$ and $|\tau(\chi_*)|=\sqrt q$. This follows by differentiating the periodic step function and using the primitive Gauss identity. Let

$$
 M=\left\lfloor q/(4D)\right\rfloor.
$$

By (1), $M\ge D$ and $M\asymp q/D$ for large $N$. For the harmonics $0<|h|\le M$, remove from the norm the common unimodular factor $\tau(\chi_*)/\sqrt q$, and $\overline{\chi_*}(-1)$; for fixed $a$ the factor $\chi_*(a)$ is unimodular as well. Then extend the sum of nonnegative squares over primitive odd characters to the full character family modulo $q$, normalized throughout by $\phi(q)$. All test coefficients now depend only on $d,h,u,a,q,N$ and not on the character. Exact character orthogonality on units imposes

$$
  d h'\equiv d' h\pmod q.
$$

Since $|dh'-d'h|\le2DM<q$, the congruence requires $h/d=h'/d'$, including when the harmonics are negative. Thus different reduced rational groups are orthogonal in this enlarged finite mean. The coefficients at nonunit pairs are simply zero. The additive Fourier phases can be kept at their actual sample values: no spatial averaging is used for these low harmonics.

For the endpoint, the identity $\sqrt{da}\,w_a(X/(da))=\sqrt X(\log X-\log d)$ lets us factor out $\sqrt X$. In a rational group $d=jd_0,\ h=jh_0$ with $(d_0,h_0)=1$, the remaining coefficient of the whole group is bounded by

$$
 O\!\left(\sqrt q L_V |h_0|^{-1}(1+\log(D/d_0))\right).
$$

The squared sum is $O(qD L_V^2)$ as in the periodic endpoint lemma. Restoring the physical weight after the factor $\sqrt X$ and integrating $u$ over its dyad shows that the low-harmonic endpoint costs at most

$$
 O\big((NV)^{-\alpha}L_V\sqrt{D/V}\,\sqrt{q/N}\tau(r)\big)
$$

in the dyadic spatial and conductorwise square-mean norm, where $\tau(r)$ is the divisor count of $r$ (not a Gauss sum). For the integral in (4), the previously proved rescaling bound is

$$
 \sup_{t\ge0}\left|\int_0^t w_a'(v)e^{2\pi i hv/q}\,dv\right|
 \ll\sqrt{q/|h|}\big(1+|\log(aq/|h|)|\big).
$$

For $|h|\le M\le q$ and $aq\mid N$, the logarithmic factor is $O(L)$. Consequently the coefficient in a reduced group, including $\sqrt{da}$ from (4), is

$$
 O\!\left(q\sqrt a L\,\sqrt{d_0}|h_0|^{-3/2}(1+\log(D/d_0))\right).
$$

The factor $1/j$ in the grouped bound follows from $\sqrt d\,|h|^{-3/2}=\sqrt{d_0}|h_0|^{-3/2}/j$. The sum of squares is $O(q^2 a L^2 D^2)$, using $\sum_{d_0\le D}d_0(1+\log(D/d_0))^2\ll D^2$. After restoring the physical atom weight and summing over $a\mid r$, the low-harmonic integral costs

$$
 O\big((NV)^{-\alpha}L(D/V)(q/N)\sum_{a\mid r}\sqrt a\big).
$$

The factors $\sqrt{q/N}\tau(r)$ and $(q/N)\sum_{a\mid r}\sqrt a$ are bounded absolutely, as in the published estimate, by $qr\mid N$ and the bounded products $\prod_{p\mid r}2/\sqrt p$ and $\prod_{p\mid r}(p^{-1}+p^{-1/2})$.

## 2. High harmonics and the unbounded Gram bound

The high-harmonic integral tail is absolutely bounded using the rescaled integral above. The sum over $|h|>M$ of $|h|^{-3/2}(1+|\log(aq/|h|)|)$ is $O(L/\sqrt M)$ by a dyadic sum, since $M\le q\le N$ and $aq\mid N$. Summing $\sqrt d$ and using the bounded $a$-product gives dyadic norm

$$
 O\big((NV)^{-\alpha}L(D/V)\sqrt{D/M}\big).
$$

For the high endpoint tail, at a fixed character and $a\mid r$ a reduced group with $\lvert h\rvert>M$ must have $|h_0|>Md_0/D$. Apart from its endpoint log factor $O(L_V)$, the square sum of grouped Fourier coefficients is therefore at most

$$
 O\left(q\sum_{d_0\le D}(1+\log(D/d_0))^2
                         \sum_{|h_0|>Md_0/D}|h_0|^{-2}\right)
 \ll q(D/M)\log^3(2D).
 \tag{5}
$$

The last bound sums $O(D/(Md_0))$ inside because $M\ge D$. The distinct frequencies $Nh/(qad)$ are $N/(qaD^2)$-separated. Applying the proven smooth-majorant separated-frequency inequality on the dyad, splitting the endpoint log as $\log X-\log d$, restoring the physical atom weight, and summing over $a\mid r$ gives the tail norm

$$
 O\left((NV)^{-\alpha}L_V\sqrt{D/M}\log^{3/2}(2D)
                  (V^{-1/2}+D/V)\right).
$$

For this step one may use finite Fejér sums with the harmonics $|h|>M$; the bound on merged absolute coefficients is unchanged. They converge in periodic $L^2$ after subtracting the low harmonics, and then in dyadic spatial $L^2$ for the finitely many dilations. For the integral, dominated convergence against the integrable $w_a'$ gives its absolutely convergent integrated series, just as in the original exterior proof.

Combining these four bounds and using $D\le V$, $\sqrt{D/M}\ll D/\sqrt q\le L^{-\mathsf B}$, and $\log(2D)\ll L$, the squared norm on each dyad, averaged over primitive odd characters mod $q$ with denominator $\phi(q)$, is bounded by the square of

$$
 O\big((NV)^{-\alpha}L_V(L^{-\mathsf A/2}+L^{3/2-\mathsf B})\big).
$$

Every such primitive character induces exactly one odd character modulo $N$, and every odd character occurs at its unique conductor. Transforming to the total odd-family mean costs in the squared estimate at most
$2\sum_{q\mid N}\phi(q)/\phi(N)=2N/\phi(N)=L^{o(1)}$.
The last bound follows, for instance, by splitting $\sum_{p\mid N}1/p$ at $L$ and using Chebyshev and partial summation. The infinite sum $\sum_{j\ge0}(N2^jY)^{-2/L}\log^2(2N2^jY)\ll L^3$ is uniform in $Y\ge1$ by the original exterior dyadic weight estimate. This proves (2). Finally the original local GRH gives the exact Hardy interpretation and $\operatorname{Avg}_{\rm odd}\|p_\chi\|_2^2\ll L^2$ by Li–Liu Prop. 6.5. Rank-one HS triangle and Cauchy–Schwarz with (2) prove (3).

The remaining Gram with the coefficient $\Lambda-\Lambda_{\le D_V}$ is a signed arithmetic convolution target. Nothing here estimates its cancellation against the same-copy diagonal or the stationary model. The gain used same-modulus character orthogonality below the rational alias threshold, not translation smoothing, random phases, or an assumption on the independence of zeros.
