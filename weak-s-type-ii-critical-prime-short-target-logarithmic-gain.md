# A logarithmic gain on short target windows for the dense critical shell

Let $Y$ be large and $L=\log Y$. Use exactly the moving physical cuts, true $N$-unit masks, arbitrary target-dependent bounded prime-pair selector $E_N$, and optional fixed common complementary product multiplier of [the dense critical-shell mean-square theorem](weak-s-type-ii-critical-prime-arbitrary-selector-mean-square.md). In particular both signed pairings use all prime $q$ in $[.8\sqrt N,.9\sqrt N]$, all nonzero numerators, and the exact arc width $|\beta|\le1/(10N)$. Fix $\kappa>0$ and suppose that $Y^{1/3+\kappa}\le H\le .01Y$. Then unconditionally,

$$
 \sum_{\substack{Y\le N\le Y+H\\ N\ {\rm even}}}
 \sup_{\substack{E_N,\ {\rm all\ permitted}\\{\rm hard\ cuts}}}
       \big(|\mathcal I_N|^2+|\mathcal C_N|^2\big)
 \ll_\kappa H Y^2 L^{-1}(1+\log L)^{14}.
 \tag{1}
$$

The signed sums and integrals are taken before the absolute values. Thus for any fixed $0<\nu<1/2$ the two actual dense-shell values are at most $Y/L^\nu$ except for $O_\kappa(H L^{-1+2\nu}(1+\log L)^{14})$ targets, uniformly over the same choices. This localizes the actual almost-all estimate below the square-root length; it is not a pointwise statement at a prescribed target. A complementary product multiplier is still common across this ambient target interval, not independently chosen at each $N$.

## 1. A short hyperbolic-strip prime-pair bound in a residue

Put $X=\sqrt Y$ and $\sigma=\min(.01,\kappa/40,1/100)$. Let $U,V$ be the two fixed proportional ambient prime intervals covering all the actual $u,v$ supports for $Y\le N\le1.01Y$. They are disjoint, each has endpoints $\asymp X$, and both are bounded above by a fixed multiple of $X$. Uniformly in a real $B$, $1\le h\le Y^\sigma$, and a residue $c\bmod h$, the number of actual prime pairs in $U,V$ with

$$
 B<uv\le B+H,\qquad uv\equiv c\pmod h
$$

is $O_\kappa(H/(\varphi(h)L^2))$. The nonunit case has no pairs because the primes exceed $h$. We can allow $H\le.03Y$ in this lemma for harmless endpoint enlargements. If the product interval does not meet the ambient product support the assertion is immediate; otherwise $B,B+H\asymp Y$ uniformly for these fixed boxes.

First, count arbitrary integers in the strip with given progressions $u\equiv a\bmod d$, $v\equiv b\bmod e_0$, where $1\le d,e_0\le Y^{3\sigma}$. The count is

$$
 \frac{\operatorname{area}\{(u,v)\in U\times V:B<uv\le B+H\}}
          {d e_0}
 +O\big(Y^{1/3}+H/X+1\big).
 \tag{2}
$$

One may use enclosing intervals of the form $(U_-,U_+]$ and $(V_-,V_+]$, without changing any included integers. Write

$$
 g_C(u)=\min(V_+,\max(V_-,C/u)).
$$

The exact summand over each allowed integer $u$ is the difference of the two floors of $(g_C(u)-b)/e_0$ at $C=B+H,B$. The linear part in the difference sums to the area main term with error $O(H/(e_0X))$: $g_{B+H}-g_B$ has amplitude $O(H/X)$ and total variation $O(H/X)$, being piecewise monotone on at most a fixed number of intervals. Approximate its $u$-progression sum by its integral divided by $d$ using the uniform $O(1)$ discrepancy of a single arithmetic progression and partial summation.

For the floor discrepancies, where the two clipped endpoints coincide the difference vanishes. Where an endpoint is a constant and the difference does not vanish, $u$ belongs to the sweep between $B/V_\pm$ and $(B+H)/V_\pm$, of length $O(H/X)$, so the constant part costs $O(1+H/(dX))$. On the reciprocal parts write $u=a+d\ell$; the relevant sums are of the sawtooth $\psi(z)=\{z\}-1/2$ at $z=C/(e_0(a+d\ell))-b/e_0$ on at most a fixed number of intervals. The sawtooth at integers has its actual value $-1/2$ here. For any positive integer frequency $j$, van der Corput's second derivative estimate gives

$$
 \left|\sum_{\ell\ {\rm in\ a\ reciprocal\ part}}
 e\!\left(\frac{jC}{e_0(a+d\ell)}\right)\right|
 \ll Y^{1/4}\left(\sqrt{j/e_0}+\frac{\sqrt{e_0}}{d\sqrt j}\right),
 \tag{3}
$$

where $e(z)=\exp(2\pi i z)$. Indeed the interval of $\ell$ has length $O(X/d)$ and the absolute second derivative is $\asymp j d^2/(e_0 X)$. The usual estimate $O(M_0\sqrt{\lambda}+\lambda^{-1/2})$ for length $M_0$ and same-sign second derivative between $\lambda$ and a constant multiple of $\lambda$ follows by cutting away derivative distances $<\min(1/4,\sqrt\lambda)$ from integers. For $\lambda\ll1$ those cut pieces contain altogether $O(M_0\sqrt{\lambda}+\lambda^{-1/2})$ integers by monotonicity. The remaining $O(M_0\lambda+1)$ pieces each have exponential sum $O(\lambda^{-1/2})$: for adjacent lattice points telescope through $1/(e(f(\ell+1)-f(\ell))-1)$, whose variation is $O(\lambda^{-1/2})$ while the monotone derivative remains between the same two consecutive integers at distance $\gg\sqrt\lambda$. Allowing one endpoint per piece costs the same bound. The case $\lambda\gg1$ is trivial.

For completeness, the elementary sawtooth discrepancy bound used with (3) is

$$
 \left|\sum_{\ell}\psi(z_\ell)\right|
 \ll \frac{\#\{\ell\}}T+
       \sum_{j=1}^{2T}\frac1j
            \left|\sum_\ell e(jz_\ell)\right|
 \tag{4}
$$

for positive integer $T$. To see this, convolve $\psi$ on the circle with the normalized nonnegative kernel proportional to $(\sin(\pi T z)/\sin(\pi z))^4$. This kernel has integral one, degree at most $2T-2$, and is $O(T(1+T\|z\|)^{-4})$, with $\|z\|$ distance to the nearest integer. The normalization follows by bounding the integral above and below by constants times $T^3$ before normalization (use $|z|\ll1/T$ for the lower bound). The error in the convolution is bounded by $O(1/T)+O((1+T\|z\|)^{-3})$: off the jump the sawtooth has slope one, and away from $|w|\ge\|z\|$ the increment through the convolution variable $w$ never crosses the jump. This bound includes exact integer arguments. For a trigonometric polynomial majorant of the second error, take a large constant times

$$
 [F_T(z)+F_T(z+1/(2T))]/T,\qquad
 F_T(z)=T^{-1}(\sin(\pi Tz)/\sin(\pi z))^2.
$$

The sum of the squared numerators at the two shifts is one and both denominators are $O((\|z\|+1/T)^2)$, with continuous definitions at the removable zeros. This expression majorizes a constant times $(1+T\|z\|)^{-2}$ and its Fourier coefficients, including the constant coefficient, are all $O(1/T)$. The convolved sawtooth has zero constant term and coefficients $O(1/j)$, since its Fourier coefficients before convolution are $-1/(2\pi i j)$ for $j\ne0$. Summing these pointwise bounds proves (4).

Take $T=\lfloor Y^{1/6}\rfloor$. Inserting (3) into (4) bounds all reciprocal floor errors by $O(Y^{1/3}+Y^{1/4}\sqrt{e_0}/d)=O(Y^{1/3})$, because $e_0\le Y^{3\sigma}$ and $3\sigma<1/6$. This proves (2), with its exact clipping and endpoint conventions.

To sieve, let $R=Y^\sigma$ and use the square weights supported on squarefree $\ell\le R$ coprime to $h$ given by finite inversion of

$$
 \sum_{\ell:\ r\mid\ell}\frac{\lambda_\ell}{\ell}
 =\frac{\mu(r)}{G_h(R)\varphi(r)}
 \quad (r\le R,\ (r,h)=1),\qquad
 G_h(R)=\sum_{\substack{r\le R\\(r,h)=1}}\frac{\mu^2(r)}{\varphi(r)}.
$$

The weights outside the displayed support are zero. Inversion gives $\lambda_1=1$ and $|\lambda_\ell|\le\ell/\varphi(\ell)$ by factoring $\varphi(\ell j)$ on the nonzero squarefree terms, hence $\sum|\lambda_\ell|\ll R\log(2R)$. Also

$$
 \sum_{\ell,\ell'}\frac{\lambda_\ell\lambda_{\ell'}}{[\ell,\ell']}
 =G_h(R)^{-1}
 \ll \frac{h}{\varphi(h)\log R}.
 \tag{5}
$$

The equality is the identity $(\ell,\ell')=\sum_{r\mid(\ell,\ell')}\varphi(r)$ followed by the defining equations. For the upper bound note that $G_1(R)\gg\log R$ by the harmonic squarefree count, and decomposing a squarefree $r$ into factors supported in and coprime to $h$ gives $G_1(R)\le(h/\varphi(h))G_h(R)$. The nonnegative sieve weight $(\sum_{\ell\mid u}\lambda_\ell)^2$ is exactly one on the actual primes $u>R$, and likewise for $v$.

For a unit $c\bmod h$, split over the $\varphi(h)$ unit classes of $u$; then $v\equiv c\bar u\bmod h$. After expanding the two square weights the additional divisor constraints are on $[\ell_1,\ell_2]\mid u$ and $[\ell_3,\ell_4]\mid v$. They are coprime to $h$, so CRT gives two progressions of moduli $d=h[\ell_1,\ell_2]$ and $e_0=h[\ell_3,\ell_4]$, both $\le Y^{3\sigma}$. Apply (2). The area is $O(H)$ since the vertical thickness is $O(H/X)$ and $|U|\ll X$. The two main densities in (5) and the number of unit classes give

$$
 O\!\left(H\frac{\varphi(h)}{h^2}G_h(R)^{-2}\right)
 =O_\kappa\!\left(\frac{H}{\varphi(h)L^2}\right).
$$

The absolute accumulated error is $O(h (R\log(2R))^4 (Y^{1/3}+H/X+1))$. Dividing it by $H/(hL^2)$ gives $O(Y^{6\sigma}L^6(Y^{1/3}/H+Y^{-1/2}+1/H))=o(1)$ by $6\sigma<\kappa$, $6\sigma<1/2$. Thus the stated semiprime multiplicity holds with all its residue and sharp product restrictions. This supplies the logarithmic saving for intervals shorter than those obtained by applying a one-variable Brun–Titchmarsh bound after fixing $u$.

## 2. Improve the signed cell energy to one logarithm

Write $Q(J)=\sum_{u,v\in J}\mu(u)\mu(v)/[u,v]$ for a hard interval of positive integers. For any family of pairwise disjoint integer intervals $J$ in $[1,U_0]$, we claim

$$
 \sum_J Q(J)\ll 1+\log U_0.
 \tag{6}
$$

First, the ordinary reciprocal sum $M_1(x)=\sum_{n\le x}\mu(n)/n$ is $O(\exp(-c\sqrt{\log(x+2)}))$ for some fixed $c>0$ and all $x\ge1$. This follows from the classical Mertens bound (for example [Lee–Leong, Theorem 2.2, (17)](https://arxiv.org/pdf/2208.06141v5#page=5)), by partial summation and $\sum_{n\ge1}\mu(n)/n=0$. For the last equality the Mertens bound gives convergence and continuity at $s=1$ in the partially summed Dirichlet series, while $1/\zeta(s)\to0$ along $s>1$.

For any disjoint family of integer intervals, the squared sum of their individual $\sum_{n\in J}\mu(n)/n$ is $O(1)$. Indeed write each nonempty $J=[A,B]\cap\mathbb Z$ using integer endpoints. Among intervals with $B/A\ge e$ their starting logarithms are at least unit-separated, so the bounds for $M_1(B)-M_1(A-1)$ are square-summable, with $M_1(0)=0$. For the others group by $j=\lfloor\log A\rfloor$. Such intervals lie in $[e^j,e^{j+2}]$, so the sum of their absolute increments is $O(1)$ by disjointness and the unsigned harmonic sum on that range. Their maximum increment is $O(e^{-c'\sqrt j})$ by the same Mertens endpoints; the finitely small endpoints can be bounded directly. The squared sum in the group is thus summable over $j$. This argument applies after any common real rescaling of the intervals and passage to integer points, since disjointness is preserved.

Expand $\gcd(u,v)=\sum_{d\mid u,v}\varphi(d)$ in $Q$ and put the two variables equal to $d$ times new variables. As $\mu(dn)=\mu(d)\mu(n)\mathbf1_{(n,d)=1}$ on squarefree $d$, this gives

$$
 \sum_J Q(J)
 =\sum_{d\le U_0}\frac{\varphi(d)\mu^2(d)}{d^2}
         \sum_J\left|\sum_{\substack{dn\in J\\(n,d)=1}}\frac{\mu(n)}n\right|^2 .
 \tag{7}
$$

For a fixed $d$, the function $\mu(n)\mathbf1_{(n,d)=1}$ is the convolution of $\mu$ with the indicator of integers supported entirely on primes dividing $d$. This identity follows prime by prime, since multiplying the $\mu$ Euler factor by $(1-p^{-s})^{-1}$ deletes it for $p\mid d$. Use this convolution in the inner sums and apply Minkowski in the interval index. For each supported factor $r$, the intervals for the remaining variable given by $drn\in J$ are disjoint, so the preceding square-sum bound applies uniformly. The sum of convolution weights is $\sum_{r:\,p\mid r\Rightarrow p\mid d}1/r=d/\varphi(d)$. Thus the inner squared sum in (7) is $O((d/\varphi(d))^2)$. Finally $\sum_{d\le U_0}1/\varphi(d)\ll1+\log U_0$: use $d/\varphi(d)=\sum_{a\mid d}\mu^2(a)/\varphi(a)$ and the convergent positive series $\sum_a\mu^2(a)/(a\varphi(a))$. This proves (6).

At each fixed complementary partition level, the physical $m$-cells have disjoint coefficients and the short-divisor intervals at each real $v=m/h$, each allocation $r\mid h$ and each orientation are disjoint, as proved in the base mean-square result. The gain (6) replaces its $O(L^{3/2})$ main bound by $O(L)$. The accumulated floor errors in that proof were already $O((Y/h)L)$: the direct orientation keeps the $k$-cell fixed per short divisor while the $d$-cell runs, and the reflected orientation reverses the roles. As before the positive Cauchy cost over allocations and orientations is $O(4^{\omega(h)})$. We obtain, for all the fixed physical partition levels and $h\le Y^{.01}$,

$$
 \sum_{\mathbf c}\|D_{h,\mathbf c}\|_2^2
   \ll 4^{\omega(h)}(Y/h)L .
 \tag{8}
$$

The initial per-interval signed bound $\|D_h\|_2^2\ll4^{\omega(h)}Y/h$ and every physical gate remain unchanged.

## 3. Localize the actual mean-square proof

Retain the physical-cell estimates and notation of the cited dense-shell theorem, including $\|D_h\|_2^2\ll4^{\omega(h)}Y/h$ and $M\asymp L^{12}$; use the improved fixed-level cell bound (8) above. The arbitrary physical rounding errors are uniform per target and thus contribute $O(HY^2 L^3/M)$ on this window. Use $Z=L^4$ for the target unit condition. The large-prime error in the summed square is now

$$
 \ll Y^2\sum_{Z<p\le 2Y}\frac{H/p+1}{p}
 \ll HY^2/Z+Y^2(1+\log L),
$$

which is smaller than (1). This uses the same divisor-supported signed energy at $h=p$, before applying the union bound to the squared differences.

For each target let $H_N=\prod_{p\mid N,p\le Z}p$. If $H_N>Y^\sigma$, one can multiply its distinct prime factors successively and find a squarefree divisor $h\mid N$ with $Y^\sigma<h\le ZY^\sigma$. Here $h\ll H$. Consequently the number of these exceptional targets is at most a constant times $H$ times the reciprocal sum of squarefree $h>Y^\sigma$ supported on primes $\le Z$. With $\theta=1/\log Z$, the latter is bounded by

$$
 Y^{-\sigma\theta}\prod_{p\le Z}(1+p^{\theta-1})
 \ll e^{-\sigma L/\log Z}(1+\log Z)^e ,
$$

where the exponent $e$ is Euler's number. This decays faster than any fixed reciprocal log power. Their contribution is negligible by the ordinary $O(Y^2)$ squared bound per target. For all remaining $N$ the small-prime unit expansion is exactly over $h\mid H_N$ with $h\le Y^\sigma$, as required by §1.

For $q$ and $\beta$, build the coarse cells on the respective endpoint sweeps over $[Y,Y+H]$. Each of the two endpoints in each coordinate is monotone over this interval. Split each swept range into $M$ equal cells and retain the middle interval between the two sweeps as one cell. The sweeps are disjoint for $H\le .01Y$. There are $O(M)$ cells per coordinate; pad with empty cells to form dyadic trees as before. Width of a $q$ sweep cell is $O(H/(M\sqrt Y))$ and of a $\beta$ sweep cell $O(H/(MY^2))$. The respective derivative lower bounds $\gg Y^{-1/2},Y^{-2}$ show that each type of omitted wall strip occurs for targets in an interval of length $O(H/M)$. A wall at the common middle-cell endpoint affects at most one target there (assign half-open cells and allow bounded adjacent-cell overlap for the estimate). Thus among targets with $h\mid N$ the multiplicity is $O(H/(Mh))$, still much larger than the endpoint $O(1)$. The proof of the earlier arc-wall error uses the supremum over physical cell rectangles before summing disjoint strips. It is unchanged except that its squared bound for each $h$ is now

$$
 \ll \frac{YH}{Mh}(1+\log M)^6\,4^{\omega(h)}(Y/h)L.
$$

The five-coordinate maximal Fourier sum remains the same. At a fixed Fourier index $b=N-uv$ and for a fixed $h\mid N$, we now count only $uv$ in a translated interval of length $H$ and with $uv\equiv-b\bmod h$. The bound in §1 gives multiplicity $O_\kappa(H/(\varphi(h)L^2))$ for every such index; add an endpoint by enlarging the interval by one if necessary. Cauchy on the prime products at each target costs $O(Y)$, uniformly over the arbitrary selectors; thus the main squared sum for fixed $h$ is

$$
 \ll_\kappa \frac{HY^2}{L}(1+\log M)^{10}
              \frac{4^{\omega(h)}}{h\varphi(h)}.
$$

Use the same exact inclusion-exclusion and Minkowski after taking square roots, with the Euler factor $\sum_h 2^{\omega(h)}/\sqrt{h\varphi(h)}\ll(1+\log Z)^2$. Squaring yields the first assertion in (1); all the wall, unit-tail and physical errors above are smaller. The earlier uniform full-vs-centered comparison costs $O(HY^2/L^3)$ in squared sum at these actual targets, proving the centered part. Thus the short hyperbolic-strip sieve handles the two genuine prime legs, and the signed cell improvement uses the actual complementary coefficients. Neither changes the statistic.
