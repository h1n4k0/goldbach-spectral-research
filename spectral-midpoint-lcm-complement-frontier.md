# Exact cancellation and two endpoint bounds for the true midpoint LCM block

**Scope.** This extends the [midpoint parity tests](spectral-midpoint-parity-signed-transport.md) on the actual prime sequence. The total part of their mixed product above the divisor midpoint vanishes pointwise on even squarefree composites; every individual high coefficient vanishes if the shifted partner has a prime factor above the midpoint. A complement formula then isolates a genuinely signed Möbius coefficient in a polynomial band above the midpoint, with a quadratic bound for its deterministic bias. A divisor switch bounds the top endpoint. The remaining true signed moment is not estimated; this is neither a positivity result nor a proof of Hypothesis S.

Use the earlier notation: $N$ is sufficiently large and even, $L=\log N$, $S=\mathfrak S(N)$, $I$ is a central half-open cell of length $H=N/(16\lceil L^J\rceil)$ in $(N/2,9N/16]$ with fixed $J\ge1$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Write $m=N-n$, $t=\sqrt m$, and fix $0<\beta<1/1000$, $z=N^\beta$. Unless stated otherwise the partner $m$ is squarefree and $z$-rough, meaning it has no prime factor $<z$. Denote this gate by $\mathcal G$. On the genuine prime positions in $I$, $(m,N)=1$. All weighted sums are raw $\lambda$-mass, not divided by $H$ or $N$.

Put $w(m,e)=1-2\log e/\log m$, and retain the earlier midpoint sums $F_0(m)=\sum_{d\mid m,\ d<t}\mu(d)$ and $F_1(m)=\sum_{e\mid m,\ e<t}\mu(e)w(m,e)$. Their truncations at $d,e\le D=\sqrt N L^{-B}$ are denoted by $F_{0,D}$ and $F_{1,D}$; here $B>0$ is fixed. On $h\mid m$ define

$$
 C_m(h)=
 \sum_{\substack{d,e\mid h,\ d,e<t\\\operatorname{lcm}(d,e)=h}}
       \mu(d)\mu(e)w(m,e).
$$

## 1. What the true high-LCM sum can see

For $h<t$, neither restriction cuts any divisors of $h$. For each $e\mid h$ the sum of $\mu(d)$ over $\operatorname{lcm}(d,e)=h$ is

$$
 \mu(h/e)\sum_{a\mid e}\mu(a),
$$

since $h$ is squarefree. Only $e=1$ survives, with $w(m,1)=1$. Hence $C_m(h)=\mu(h)$ in the entire low range. The high sum therefore satisfies the exact formula

$$
 \sum_{\substack{h\mid m\\ h>t}} C_m(h)=F_0(m)F_1(m)-F_0(m).       \tag{1}
$$

There is no equality endpoint at $t$ because $m>1$ is squarefree. By the midpoint complement identities, this is zero when $m$ is prime or an even-parity composite ($\mu(m)=+1$). For odd-parity squarefree composites ($\mu(m)=-1$) it equals $-F_0(m)$. If $m$ has a prime factor $p>t$, each $d,e<t$ avoids $p$, and their lcm divides $m/p<t$. Thus every individual high coefficient is then zero, for either parity. Also every nonzero coefficient satisfies $h\le de<m$ for at least one contributing pair; on $\mathcal G$ this implies $m/h\ge z$ and $h\le m/z$.

Let $C_{m,D}$ be the analogous coefficient with $d,e\le D$. For large $N$, $D<t$ throughout $I$, and again $C_{m,D}(h)=\mu(h)$ for $h\le D$. Thus $\sum_{h>D}C_{m,D}(h)=F_{0,D}F_{1,D}-F_{0,D}$. On $\mathcal G$ all four divisor sums are bounded by $2^{\lfloor1/\beta\rfloor}$. The [critical-band estimate (3)–(4)](spectral-midpoint-parity-signed-transport.md) therefore gives

$$
 \begin{split}
 &\sum_{\substack{n\in I\\m\in\mathcal G}}\lambda(n)
 \left|\sum_{\substack{h\mid m\\h>D}} C_{m,D}(h)
       -\sum_{\substack{h\mid m\\h>t}} C_m(h)\right|\\
 &\hspace{35mm}\ll_{\beta,B,J}\frac{SH(1+\log L)}{L^2}.            \tag{2}
 \end{split}
$$

In particular the genuinely above-BV part, after this small loss, is a signed $-F_0$ moment on actual rough squarefree odd composites whose largest prime is below $t$. Formula (1) does **not** give cancellation for a subset of high moduli on the even class; it concerns the whole high block.

## 2. Double-complement formula and first polynomial band

Fix $h\mid m$ with $h>t$. If $h$ has a prime factor $>t$, then $C_m(h)=0$, since neither short divisor can contain it. Suppose all primes dividing $h$ are below $t$. Drop both cutoff conditions and then use inclusion–exclusion. The full coefficient is $\mu(h)$ by the same inner sum as above. The arm $e>t$ cancels because $e>1$. The arm $d>t$ cancels too: write $e=(h/d)a$, $a\mid d$. The inner weighted sum is a combination of $\sum_{a\mid d}\mu(a)$ and $\sum_{a\mid d}\mu(a)\log a$, both zero since every such $d$ has at least two prime factors. To see the log cancellation, for each prime in $\log a$ sum over the subsets of the other primes.

The both-outside term remains with a plus sign. Set $u=h/d$, $v=h/e$, so $\operatorname{lcm}(d,e)=h$ is equivalent to $(u,v)=1$ and $d,e>t$ becomes $u,v<h/t$. No divisor is exactly $t$. Squarefreeness gives $\mu(d)\mu(e)=\mu(uv)$, and hence

$$
 C_m(h)=\mu(h)+
   \sum_{\substack{u,v\mid h,\ (u,v)=1\\u,v<h/t}}
       \mu(uv)\left(1-\frac{2\log(h/v)}{\log m}\right),
 \qquad P^+(h)<t.                                             \tag{3}
$$

For the contributing $h\le m/z$, the two new indices $u,v$ are strictly less than $t/z$. Equivalently, with $q=m/h$, they satisfy $qu<t$ and $qv<t$ separately. This does not imply $quv<t$, and the roughness and largest-factor restrictions remain.

If $t<h\le tz$ and $h$ is composite, each prime dividing $h$ is $\le h/z\le t$, hence $<t$, and each nonunit divisor of $h$ is $\ge z\ge h/t$. Only $u=v=1$ remains in (3). Thus throughout this first polynomial band,

$$
 C_m(h)=
 \begin{cases}
 0,&h\text{ prime},\\
 \mu(h)-\dfrac{2\log(h/t)}{\log m},&h\text{ composite}.
 \end{cases}                                                  \tag{4}
$$

This formula does not replace $\mu(h)$ by its sign average.

## 3. A uniform rough-cofactor sieve budget

For a fixed squarefree rough $r\in[z,N^{3/5}]$ with $(r,N)=1$, let $M_I(r)$ be the total true $\lambda$-mass over $n\in I$ with $r\mid m$ and $m/r$ rough. Set $U=H/r$, $Y=U^{1/100}>z$ for large $N$. Sieve the integer cofactor in the interval of length $U$ so that $n=N-r(m/r)$ has no prime divisor $<Y$ and the cofactor has none $<z$. At primes dividing $r$ the primality form has no root; these primes are not below $z$. At a prime below $z$ that divides $N$, the two candidate roots coincide, including at $2$; at each remaining prime below $z$ they are distinct. The local product is therefore exactly

$$
 \prod_{\substack{p<Y\\p\nmid r}}(1-1/p)\,
 V_z,\qquad V_z=\prod_{\substack{p<z\\p\nmid N}}(1-1/(p-1))
              \asymp \frac{S}{\beta L}.
$$

The product comparison is as in the midpoint proof. The [dimension-two fundamental upper sieve](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) with level $U^{1/2}$, CRT errors $O(2^{\omega(a)})$ per squarefree sieve modulus $a$, and $\log U\asymp L$ gives, after multiplying the count by $L$,

$$
 M_I(r)\ll \frac{H V_z}{\varphi(r)}+
                L U^{1/2}\log(2U).                           \tag{5}
$$

The constant is absolute for the stated exponent ranges and all sufficiently large $N$ (threshold may depend on $\beta,J$). The true primes exceed $Y$, so none are lost in this upper count.

If $[X_1,X_2]\subset[z,N]$ has ratio $X_2/X_1$, then

$$
 \sum_{\substack{X_1\le r\le X_2\\r\ z\text{-rough}}}
       \frac1{\varphi(r)}
 \ll \frac{1+\log(X_2/X_1)}{\beta L}                           \tag{6}
$$

for large $N$. Indeed $r/\varphi(r)\le2$ uniformly, since there are at most $1/\beta$ distinct primes all $\ge z$. Apply a dimension-one upper sieve to $(X,2X]$ only up to $z^{1/3}\le X^{1/3}$, with level $X^{1/2}$. Every $z$-rough integer passes. The parameter is at least $3/2$, and Mertens and the CRT give the main bound $O(X/(\beta L))$ and remainder $O(X^{1/2})$. Cover $[X_1,X_2]$ by $O(1+\log(X_2/X_1))$ such intervals with $X\asymp X_1$ or larger; count an initial real endpoint by at most one. The power error after dividing by $X$ is negligible since $X_1\ge z$.

## 4. Quadratic bias at the first edge; an upper edge by switching

Let $0\le\theta\le1/4$, and let $\mathcal B_\theta(m)$ be the set of composite divisors $h$ of $m$ with $t<h\le tN^{\beta\theta}$. Write

$$
 J_\theta(I)=
 \sum_{\substack{n\in I\\m\in\mathcal G}}\lambda(n)
              \sum_{h\in\mathcal B_\theta(m)}\mu(h).
$$

By (4) the $\lambda$-mean of the true high coefficient on this band is $J_\theta(I)-R_\theta(I)$, where $R_\theta$ is nonnegative and uses $2\log(h/t)/\log m$ instead of $\mu(h)$. Its weighted correction satisfies

$$
 0\le R_\theta(I)\ll
       \frac{SH}{L}\left(\theta+\frac1{\beta L}\right)^2.        \tag{7}
$$

To verify this, all possible $h$ lie between $\sqrt{7N/16}$ and $N^{1/2+\beta\theta}$, so (6) bounds their reciprocal sum by $O(\theta+1/(\beta L))$. Use (5) with $r=h$ and drop the moving inequalities for this upper bound. Its aggregate remainder is $O(N^{3/4+\beta/8}L^2)$ by summing $r^{-1/2}$ to $N^{1/2+\beta\theta}$. The coefficient $2\log(h/t)/\log m$ is at most $O(\beta\theta)$ uniformly. Multiplication of the main budget $O((SH/(\beta L))(\theta+1/(\beta L)))$ by that coefficient, and absorption of the power error, prove (7). In contrast the same estimate without this coefficient is only $O((SH/(\beta L))(\theta+1/(\beta L)))$; it is not a signed estimate on $J_\theta$.

At the opposite end, take $h\ge N^{1-\beta-\beta\theta}$ with a possibly nonzero coefficient. Since $q=m/h\in[z,N^{\beta+\beta\theta}]$ is rough and $1+\theta<2$, $q$ is prime. Switching from $h$ to this complementary $q$ is injective for each $m$. Use $|C_m(h)|\le3^{\lfloor1/\beta\rfloor}$: each prime of $h$ belongs only to $d$, only to $e$, or to both, and $|w(m,e)|\le1$ in the original sum. By (5) on the switched modulus $r=q$, and (6) on the new short interval, the **absolute** true high-end contribution is at most

$$
 \ll_{\beta,J}\frac{SH}{L}\left(\theta+\frac1{\beta L}\right).    \tag{8}
$$

The combined additive errors here are $O(N^{(1+5\beta/4)/2}L^2)$. For either edge $\theta$ can be chosen after fixed $\beta$ to make the proved error an arbitrarily small fraction of $SH/L$, or can tend to zero for an $o(SH/L)$ error. The remaining $J_\theta(I)$ and the interior of the high block, with the signs in (3), still require new genuine arithmetic information.
