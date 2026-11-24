# The true critical-boundary count outside a narrow band around twice the reciprocal mean

Keep the genuine central fixed-target prime polynomial $P$, its arbitrary fixed selector $|E(u,v)|\le1$, and all exact hard cuts of the [signed typical-count proof](weak-s-type-ii-critical-prime-unrestricted-typical-small-part.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and the original signed coefficient is $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. We use the three exact least-prime exchange boundaries at $p=P^-(m)$, with original signs and endpoint tests, and retain $p\le W$ where $2\le W<Z_1$.

Let $Z_1=\exp(L^\delta)$ for a fixed $0<\delta<1$. Take either $Z_0=2$ or $Z_0=\exp(L^\gamma)$ with fixed $0<\gamma<\delta$, put $\lambda_i=\log Z_i$, and let $R=\lambda_1/\lambda_0$. For the true squarefree $m$, let $b_1$ be its product of primes in $[Z_0,Z_1)$. There is **no restriction** on lower small factors of $m$ and no size, arity, alphabet or assignment restriction on either leg. For fixed $c>0$, $c\ne2$, retain the genuine terms with $\omega(b_1)\le c\log R$ if $c<2$, and those with $\omega(b_1)\ge c\log R$ if $c>2$. Either selection has signed polynomial $D_c$ satisfying unconditionally

$$
\int_0^1|D_c(\alpha)|^2\,d\alpha
 \ll_{\gamma,\delta,c,J}
 N(1+\log W)(1+L_2)^2 R^{-\mathcal J(c)}+NL^{-J},
\qquad \mathcal J(c)=2-c+c\log(c/2).
\tag{1}
$$

In the constant-$Z_0$ case omit $\gamma$ from the constants. For fixed polylogarithmic $W$ and fixed $J>0$ large, the true full and double-centered signed pairings on the entire critical-prime shell are therefore $o(N)$ on every sufficiently large even target. These include **both** tails and actual nonempty middle bands, in contrast to the [earlier above-typical middle selection](weak-s-type-ii-critical-prime-unrestricted-low-and-typical-middle.md). More quantitatively, for fixed polylogarithmic $W$ one may remove all genuine terms outside the band

$$
\left|\omega(b_1)-2\log R\right|
 \le 10\sqrt{\log R\,(1+\log L_2)}
\tag{2}
$$

with total signed shell error $O(N(1+L_2)^{-8})$. The band (2), rather than the ordinary reciprocal mean $\log R$, is left uncontrolled by this proof.

## 1. All long lcms can be treated with an ordinary signed sum

Put $b=r_{Z_1}(m)$, the true product of primes below $Z_1$ dividing $m$, and $v=m/b$, $Y=N/b$. Distinct $b$ have disjoint coefficient support. As in the [previous fixed-allocation argument](weak-s-type-ii-critical-prime-unrestricted-typical-small-part.md#1-what-the-absolute-allocation-bound-gives), $b>N^{1/10}$ has squared cost $O_{\delta,J}(NL^{-J})$ by the universal $4^{\omega(b)}/b$ Rankin moment. In all other cases the exact rough partners of $v$, $d/r$ and $k/(b/r)$ for $r=r_{Z_1}(d)\mid b$, are $>N^{.39}$. Fix one branch and one of the two short orientations and write its signed coefficient, after removal of a common squarefree sign in the exchanged orientation, as

$$
 F_b(v)=\sum_{r\in\mathcal R_p(b)}\mu(r)
             \sum_{\substack{a\mid v\\a\in J_r(v)}}\mu(a).
\tag{3}
$$

Here $\mathcal R_p(b)$ is the set of divisors of $b$ having $p\mid r$ in branch 1, or $p\nmid r$ in branches 2 and 3; no other allocation is removed. All actual remaining cuts appear in $J_r(v)$. One has $7Y/16\le v<Y/2$, every allowed $a$ is $>N^{.39}$ and at most $\sqrt v$ (strict on the exchanged orientation), and all separate tests in $a,v/a$ are hard intervals. Cauchy across branches and orientations has constant cost. Only after squaring (3) may one add squares over all rough $v$ in the true physical product interval, as in the earlier proof.

Expand the square over both allocations and both rough short divisors $a,a'$. Use the [signed short-lcm density argument](weak-s-type-ii-critical-prime-unrestricted-typical-small-part.md#3-signed-main-and-signed-long-lcm-transfer) at $Z=Z_1$, with $Q=Z_1^{O_D(1+L_2)}=Y^{o(1)}$ and fixed large $D$. This introduces the continuous main density $V_1=\prod_{\ell<Z_1}(1-1/\ell)\asymp1/\lambda_1$, with error $O_{\delta,D}(Y L^{3-D})$ per allocation pair for $[a,a']\le Y/Q$. In the long part set $a=gx$, $a'=gz'$ with $(x,z')=1$, and write $v=gxz' u$, so $1\le u<Q$ even in the continuous comparison. Both short inequalities imply

$$
xu=v/a'\ge\sqrt v,\qquad z'u=v/a\ge\sqrt v .
$$

In particular **both** $x$ and $z'$ are polynomially large, regardless of which lcm variable is largest. For fixed $g,z',u$, every exact test on $x$ is an interval: the four arguments are $gx,gz',z'u,xu$, the short inequalities are $gx\le z'u$ and $gz'\le xu$, and the product and lcm conditions are linear inequalities. The signed weight is $\mu^2(g)\mu(z')\mu(x)$ with $(x,gz')=1$ and $(g,z')=1$ on nonzero support. The ordinary rough masked Mertens bound (equation (6) of the cited signed argument) therefore gives $O_{\delta,D}(Y L^{-D}/(gz'u))$ for the sum over this whole $x$ interval, since $x\ge\sqrt{7Y/16}/Q>N^{.4}$ for all large $N$. Open and closed endpoint differences are absorbed in that bound. The estimate also holds at each fixed real $u$ in the main comparison, where the exact identity $dv/[a,a']=du$ leaves no extra $x$-weight. Summing unrestricted harmonics of $g,z',u$, or integrating $du/u$ in the comparison, gives $O_{\delta,D}(Y L^{3-D})$ per allocation pair. Thus **all** long-lcm corrections are negligible after keeping a signed large variable, including the former gcd-largest piece.

## 2. Keep the whole signed allocation in log-space

The full signed continuous lcm form is the [positive gcd form](weak-s-type-ii-critical-prime-unrestricted-typical-small-part.md#4-the-positive-form-and-its-one-common-divisor-atom), with the true signed sum across $r$ retained inside the norm in $g$. Use the uniform **reciprocal** signed rough Mertens prefix from its proof to truncate the inner variable $x\in J_r(v)/g$ at $\Xi=Z_1^{C_{\delta,D}(1+L_2)}=N^{o(1)}$. Take its constant large enough so both endpoint prefixes of a remaining tail interval lie in the uniform range, including the extra $(x,g)=1$ condition. The tail contribution in the squared $g$ norm is $O_{\delta,D}(\tau(b)^2 L^{-D})$ on enlarging the prefix's saving exponent. Indeed each tail for fixed $g,r$ is power-log small and the total $g$ harmonic weight is $O(L)$; then \(\left|A+B\right|^2\le2|A|^2+2|B|^2\). This argument estimates the tail as a norm error, without altering any actual signed coefficient.

Minkowski in $x\le\Xi$ now costs $\sum_{x\le\Xi,\ x\ {\rm rough}}1/x=O_\delta(1+L_2)$ **in norm**, with each signed sum over $r$ untouched. For each fixed such $x$ and real $v$, discard $(g,x)=1$ and majorize $\varphi(g)\mu^2(g)/g^2$ by $1/g$ in its nonnegative squared norm. The needed bound is for

$$
\sum_{g\ {\rm rough}}\frac1g
      \left|\sum_{r\in\mathcal R_p(b)}
           \mu(r)\mathbf1_{gx\in J_r(v)}\right|^2 .
\tag{4}
$$

Every nonempty $g$ interval in its square expansion lies above $N^{.39}/\Xi>N^{.38}$. For all hard intervals in this range the ordinary rough reciprocal measure is $V_1\,dg/g$ with additive error $O_{\delta,D}(L^{-D})$, by the earlier even/odd Bonferroni interval estimate and partial summation; its floor error is $Z_1^{O_D(1+L_2)}/N^{.38}$ and its relative density error can be chosen $L^{-D-2}$. For each $r,r'$ the intersection of their two actual $g$ intervals is an interval. Hence (4) equals the corresponding continuous squared integral with density $V_1$, up to $O_{\delta,D}(\tau(b)^2 L^{-D})$. In this positive continuous square, drop the short upper cut on $gx$; it is common to all $r$ at fixed $x,v$ and can only restrict the integral.

For fixed $m=bv$ in a single exact branch there is one **common hard interval** for $d$ (all physical tests on $d,m/d$), with log length $O(1+\log p)$. The only non-common test, whether $p$ lies in $d$ or $k$, is already encoded by $\mathcal R_p(b)$. In the direct orientation $d=r g x$; in the exchanged orientation $d=r v/(g x)$. Consequently on the log-$g$ axis the remaining interval is translated by $\pm\log r$ for each $r$, up to a translation or reflection common to all $r$. Fourier Plancherel in this log coordinate bounds the integral in (4) by

$$
 V_1\int_{\mathbb R}\min(C(1+\log p),2/|\tau|)^2
       \prod_{\substack{\ell\mid b\\\ell\ne p}}
          |1-\ell^{i\tau}|^2\,d\tau
  +O_{\delta,D}(\tau(b)^2 L^{-D}),
\tag{5}
$$

with an absolute Fourier normalization absorbed. To see the prime product, in branch 1 put $r=p r_*$, $r_*\mid b/p$, and in branches 2 and 3 put $r=r_*\mid b/p$. The signed polynomial of translations is, up to a unit phase and sign, $\prod_{\ell\mid b,\ell\ne p}(1-\ell^{\pm i\tau})$. The hard log interval has Fourier modulus bounded by its length and by $2/|\tau|$; no smoothing assumption is made. The bound is uniform in $x,v$ and the fixed orientation.

Squaring the Minkowski loss and integrating in $v$ introduces its earlier factor $V_1$ and the physical length $O(Y)$. Including all negligible corrections, the sum of the true squared coefficients at this $b$ is at most

$$
O_\delta\!\left(
   \frac{Y(1+L_2)^2}{\lambda_1^2}
   \int_{\mathbb R}\min(C(1+\log p),2/|\tau|)^2
          \prod_{\ell\mid b,\ell\ne p}|1-\ell^{i\tau}|^2\,d\tau
         \right)
 +O_{\delta,D}(Y\tau(b)^2 L^{-D}).
\tag{6}
$$

This estimate is before any count selection. Because the reciprocal $\tau(b)^2$ sum is $O(\lambda_1^4)$, summing its error still beats any fixed power of $L$.

## 3. The signed Euler tilt in the actual middle band

Put $u=c/2$. For $c<2$, respectively $c>2$, the exact upper, respectively lower count indicator is at most $u^{\omega(b_1)-c\log R}$. Factor $b=p b'$ with $p=P^-(b)\le W$; the factor for $p$ in $u^{\omega(b_1)}$ is $1$ or $u$, both bounded on any fixed compact range of tilts. Drop actual unit and finite $b$ constraints only in the resulting positive reciprocal bound. For each fixed $p,\tau$, the Euler sum over $b'$ in (6), including the tilt factor, is thus bounded by $O_u(R^{-c\log u})$ times

$$
\mathcal E(\tau)=
\prod_{\ell<Z_0}\left(1+\frac{|1-\ell^{i\tau}|^2}{\ell}\right)
\prod_{Z_0\le\ell<Z_1}
     \left(1+\frac{u|1-\ell^{i\tau}|^2}{\ell}\right).
\tag{7}
$$

The actual restriction $\ell>p$ in $b'$ has only been relaxed here, and the remaining reciprocal factor for $p$ is $1/p$.

For a cutoff $Z$ with $\lambda=\log Z$ one has uniformly for real $\tau$

$$
\sum_{\ell<Z}\frac{\cos(\tau\log\ell)}\ell
 =\log|\zeta(1+\lambda^{-1}+i\tau)|+O(1).
\tag{8}
$$

From the absolutely convergent logarithmic Euler expansion, higher powers cost $O(1)$. Below $Z$ changing $\ell^{-1-\lambda^{-1}}$ to $1/\ell$ costs $O(1)$ by the Chebyshev harmonic logarithmic bound; the tail beyond $Z$ costs $O(1)$ by the prime upper bound and $\int_1^\infty e^{-s}\,ds/s$. The statement also holds at $Z=2$, with bounded left and right sides. Prime Mertens, $\log(1+x)\le x$ in (7), and (8) give

$$
\mathcal E(\tau)\ll_u
 \lambda_0^2 R^{2u}
 |\zeta(1+\lambda_1^{-1}+i\tau)|^{-2u}
 |\zeta(1+\lambda_0^{-1}+i\tau)|^{2(u-1)} .
\tag{9}
$$

The expression after $\lambda_0^2 R^{2u}$ is at most $O_u(\log(2+|\tau|)^{C_u})$. For $u\le1$ both factors are reciprocals; use [Lee–Leong, Theorem 2.1 (14)](https://arxiv.org/pdf/2208.06141v5#page=4) on real parts at least one, together with continuity and the classical zero-free line at bounded ordinates (the reciprocal is zero at the simple pole). For $u>1$, away from $\tau=0$ combine that reciprocal estimate with $|\zeta(\sigma+i\tau)|\ll\log(2+|\tau|)$ for $1\le\sigma\le3$ away from the pole. The latter follows from the truncated defining series with one integral remainder, at cutoff comparable to $2+|\tau|$. For bounded small $|\tau|$ and growing $\lambda_0$, use $\zeta(s)=1/(s-1)+O(1)$ on a fixed small disk about one. Since $\lambda_1\ge\lambda_0$, the ratio from the pole factors is bounded:

$$
 \frac{(\lambda_1^{-2}+\tau^2)^u}
      {(\lambda_0^{-2}+\tau^2)^{u-1}}
 \le \lambda_1^{-2}+\tau^2 .
$$

When $Z_0=2$ its zeta factor is already bounded at small ordinates. These bounds are uniform for $u$ in compact subintervals of $(0,\infty)$.

Integrate (9) against the hard-window factor in (6); the integral with $\min(C(1+\log p),2/|\tau|)^2\log(2+|\tau|)^{C_u}$ is $O_u(1+\log p)$ by splitting at $(1+\log p)^{-1}$ and $1$. Sum $(1+\log p)/p$ over $p\le W$ to obtain $O(1+\log W)$. Since $Y=N/b$ and $\lambda_0^2/\lambda_1^2=R^{-2}$, (6) now yields (1), including the earlier cumulative errors. Restriction to the disjoint critical arcs and separate numerator centering are ordinary $L^2$ contractions. The true fixed prime box has squared norm $O(N)$ by unique oriented products, and Cauchy with the exact phase $e(-N\alpha)$ gives both stated genuine signed pairings.

For (2) take moving $c=2\pm10\sqrt{(1+\log L_2)/\log R}$; eventually both belong to $[3/2,5/2]$ and the above constants are uniform. Since $\mathcal J''(c)=1/c$ and $\mathcal J(2)=\mathcal J'(2)=0$, $\mathcal J(c)\ge(c-2)^2/5$ in this range. The exponential power of $R$ in (1) is at most $O((1+L_2)^{-20})$. The polylogarithmic $W$ and the Minkowski factors cost at most $O((1+L_2)^3)$ in squared energy. This gives the claimed signed remainder outside the band. No bound inside the band follows.

## 4. Genuine high-count terms, not a lower bound

As a strict occupied example, let $N=2^j$, put $K_0=\lfloor 3L_2\rfloor$, $\varepsilon_N=L_2^{-1/2}$, and take two different primes in each disjoint factor-$4$ cell whose lower endpoint is $\exp(L^{(1-\varepsilon_N)i/(K_0+1)})$, with $i$ from a sufficiently large fixed initial index to $K_0$. The cells are disjoint for large $N$: successive lower-endpoint logarithms have ratio tending to $e^{1/3}$, and skipping a fixed initial part makes consecutive endpoints differ by a factor exceeding four. Bertrand twice supplies the primes. Put one prime from every cell on each leg, and append $3$ on the $d$ side. Both products have logarithm $O(L_2 L e^{-\sqrt{L_2}})=o(L)$. Additional distinct primes of size $N^{1/2-o(1)}$ place $d\in[1.05X,1.06X]$, $k\in[.43X,.44X]$ by the prime number theorem. With $W=3$, $I_0=[X,2X]$, $t=N^{.49999}$, $y=9N/16$, this gives a genuine squarefree unit branch-1 term with $p=3$ and $d/3<X$. In every fixed band of exponents $(\gamma,\delta)$ in $(0,1)$ the number of these small factors is $(6(\delta-\gamma)+o(1))L_2$; the same formula holds from a fixed constant cutoff with $\gamma=0$. It is on the true high tail of (1) for $c=3$, outside the preceding respective low-count selections. This witnesses actual new support, not a signed lower bound.

The exact critical covariance of the narrowing band (2), the broader operator problem, and weak S remain open.
