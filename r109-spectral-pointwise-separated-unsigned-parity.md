# A pointwise separated-shift main term for the odd-disjoint unsigned parity component

If an actual odd Page conductor is disjoint from the even target and its nonzero signed log shifts lie beyond the physical cap on the scale of that cap, the unsigned component of the exceptional parity difference has a simple pointwise main term. Its coefficient is exactly the singular series at the true target divided by the conductor, with the exterior sign $-\chi(N)$. For example, a single prime Page conductor has the required shift separation. This does **not** give the sign of the actual signed-pole contribution, of the exceptional parity difference as a whole, or of a genuine full mixed correlation.

Use the genuine dyad, actual conductor $r$, primitive real character $\chi$, zero $\beta$, even $N$ with $(N,r)=1$, and all real hard cuts and bounded-BV tests of the [odd-disjoint two-positive reduction](r106-spectral-odd-disjoint-two-positive-unsigned-mode.md). In particular $G=\log Y$, $g=\log G$, $Q_0=\exp(16\sqrt G/g)$, and $D=\sqrt N(\log N)^{-B}$ with the original fixed admissible $B>B_0>0$. Define

$$
 \begin{split}
   F(m)&=\omega(N-m)(N-m)^{\beta-1},\qquad L_m=\log m,\\
   T_m&=\log(m/D^2),\qquad
   \mathcal I_\beta=\int_{N-I}\frac{F(m)}{L_m}\,dm,\qquad
   H=\omega(r)+\mathcal A_{N,r},\\
   \mathcal A_{N,r}&=\sum_{p\mid N,\ p\nmid r}p^{-3/4},\qquad
   C_r^{[2]}=\prod_{p\mid r}(1-1/p)(1-2/p).
 \end{split}                                                       \tag{1}
$$

Here $\omega(r)$ counts distinct conductor primes and is not the physical weight $\omega$. Write $\mathcal P_1$ for the original real color-1 remainder with its literal finite $t\le Q_0/r$. Its exact contribution, before the inherited raw error of that reduction, is

$$
                   \mathcal U=-\frac{\chi(N)C_r^{[2]}}{\varphi(r)}
                                           \mathcal P_1.           \tag{2}
$$

Thus the genuine exceptional difference is $\gamma_N\mathcal D_1+\mathcal U+O(Y^\beta G^{C_0}/Q_0)$, where $\gamma_N=\mu(r)/\varphi(r)$ and $\mathcal D_1$ is the unchanged signed pole. No signed-pole estimate is used below.

**Theorem.** Fix any $\eta>0$. Suppose the actual conductor satisfies

$$
 \left|\sum_{p\mid r}\varepsilon_p\log p\right|
      \ \ge (2B+\eta)g
 \quad\text{for every }\;
       (\varepsilon_p)_{p\mid r}\in\{-1,0,1\}^{\omega(r)}
                    \setminus\{0\}.                               \tag{3}
$$

For every fixed $A>0$, impose the original local completion margin
$\log(Q_0/r)\ge C_A(g+H)$ with a sufficiently large constant. Then for constants $c>0$ and $C>0$ independent of $Y,N,r$,

$$
 \mathcal U
 =-\frac{\chi(N)\Sigma(N)}{r}\,\mathcal I_\beta
     +O\!\left(\frac{Y^\beta}{rG}
                \exp(CH-c\sqrt g)\right)
     +O_A\!\left(\frac{Y^\beta}{rG^A}\right).                       \tag{4}
$$

Here $\Sigma$ is the binary singular series. The constants may depend on the original fixed parameters, the bounded test norm and $\eta$. Under the same margin with the constant increased, the raw $O(Y^\beta G^{C_0}/Q_0)$ above is also $O_A(Y^\beta/(rG^A))$, so (4) may be substituted into the genuine exceptional difference with only those errors and **with** its signed pole.

For example, if $H\le g^{1/3}$ and the fixed nonnegative weight has $\int_I\omega(u)\,du\ge c_IY$ for a constant $c_I>0$, then $\mathcal U$ has sign $-\chi(N)$ and magnitude $(1+o(1))\Sigma(N)\mathcal I_\beta/r$ on the targets meeting (3) and the margin. The hypothetical whole-line replacement from the shifted autocorrelation has the **opposite** sign whenever $\omega(r)$ is odd. This comparison is not a replacement of the finite cap.

## 1. Ordinary correlation tails at the physical scale

Use $R_j,C_j,C,\mathscr L_r,\mathcal V_{N,r}$ from the [shifted autocorrelation](r108-spectral-odd-disjoint-shifted-autocorrelation.md), in particular its exact color-1 comparison with the physical bracket
$\int_{-T_m}^{T_m}(\mathscr L_r C)(t)dt-T_m(\mathscr L_r C)(T_m)$.
The only small-scale estimate needed in that bracket is the ordinary masked tail. Explicitly, put
$M(v)=\prod_{p\mid v,\ p>2}(1-\alpha_p^\circ p^{1/4})^{-1}$
with its same $\alpha_p^\circ=(p-1)/(p^2-2)$. Section 1 there gives, for every $a\ge1$, the $L^1,L^2$ norms of $R_j$ bounded by $O(M(Nr)M(j))$, and the corresponding tail norms on $[a,\infty)$ bounded by this factor times $e^{-c_1\sqrt a}$. The proof splits a positive shift convolution at $a/2$; the implied constants do not require $a$ comparable to $G$. Here use the unrelaxed bound
$\log M(Nr)\ll\sum_{p\mid Nr}p^{-3/4}\ll H$.

For each $C_j(t)=\int R_j(x)R_j(x+t)\,dx$, supported primitives $R_j(x)=0$ for $x<0$ give
$|C_j(t)|\le\|R_j\|_2\|R_j{\bf1}_{[a,\infty)}\|_2$ for $t\ge a$. For the integrated tail at $t\ge a$, Tonelli on the absolute weights gives $\|R_j\|_1\|R_j{\bf1}_{[a,\infty)}\|_1$. Evenness handles $t\le-a$. Multiplying by the absolute reciprocal-square weights in the $j$ sum is legitimate: the shifted proof's Euler moment (7) in particular gives $\sum_j\alpha^\circ(j)^2 M(j)^2\ll1$. This proves

$$
    \sup_{|t|\ge a}|C(t)|+\int_{|t|\ge a}|C(t)|\,dt
                        \ \ll\ \exp(CH-c_1\sqrt a),\qquad a\ge1.  \tag{5}
$$

The bound is absolute, not a sign argument on the ordinary kernel.

## 2. Keep the unshifted term; discard only separated translations

Write $T=T_m$. On the actual support $T=2Bg+O(1)$ uniformly, since $m\asymp Y$ and $T=2B\log\log N+\log(m/N)$. In particular $T\ge Bg$ for large $Y$. The zero-shift coefficient in $\mathscr L_r$ is exactly one under (3). Its bracket contribution is $\int_{\mathbb R} C+O(\exp(CH-c\sqrt g))$ by (5) at $a=T$, including the retained endpoint term $TC(T)$. Factors $1+T\ll1+g$ can be absorbed by reducing $c$.

For every other shift $s=\sum_{p\mid r}\varepsilon_p\log p$, the interval $[s-T,s+T]$ and its endpoints are outside $(-\eta g/2,\eta g/2)$ for large $Y$ by (3). Equation (5) bounds the absolute shifted contribution, including the endpoint, also by $\exp(CH-c\sqrt g)$. The sum of the absolute coefficients of all placements of the conductor primes is $\prod_{p\mid r}(1+2\kappa_p)\le5^{\omega(r)}$, where $\kappa_p=(p-1)/(p-2)$. This loss is absorbed in the fixed constant multiplying $H$. Hence, at the **original** cap $T_m$,

$$
 \int_{-T_m}^{T_m}(\mathscr L_r C)(t)\,dt
       -T_m(\mathscr L_r C)(T_m)
       =\int_{\mathbb R} C(t)\,dt+O(\exp(CH-c\sqrt g)).             \tag{6}
$$

This does not assert that the translated profiles have small total mass on the full real line; they are small on this one bounded test interval only.

Restore the original exterior factors in (2). In the shifted proof, $\mathcal V_{N,r}\le1$ and
$\mathcal V_{N,r}\int_{\mathbb R}C=(r/\varphi(r))\Sigma(Nr)$.
The latter identity is unshifted, so there is no total signed translation mass in (6). Also $C_r^{[2]}/\varphi(r)=r^{-1}\prod_{p\mid r}(1-2/p)\le r^{-1}$. Formula (6) costs at most the first error in (4) on integrating, as $\int_{N-I}|F(m)|\,dm\ll Y^\beta$ and $L_m\asymp G$. The actual physical endpoint removal error of the shifted proof is $O(Y^\beta e^{-c_2\sqrt G}/r)$ with this same exterior, dominated by the displayed bounds. For the rational approximation use the explicit [short-log comparison](r107-spectral-odd-disjoint-short-log-kernels.md) (5) **before** its exterior factor. With $C_r^{[2]}/\varphi(r)\le1/r$ this costs
$O(Y^\beta G^C e^{CH}(Q_0/r)^{-1/4}/r)$, $O_A(Y^\beta/(rG^A))$ under the declared margin. Likewise $G^{C_0}r/Q_0\ll_A G^{-A}$ under a sufficiently large $C_A$, proving the claim about the raw error. No unconditional completion at a near endpoint $r\approx Q_0$ is made.

Since $(r,N)=1$, at an odd prime $p\mid r$ the ratio of the binary singular series local factors at $Nr$ and $N$ is $(p-1)/(p-2)$. Accordingly

$$
     \frac{C_r^{[2]}}{\varphi(r)}\,
       \frac r{\varphi(r)}\,\Sigma(Nr)
        =\frac{\Sigma(N)}r,                                      \tag{7}
$$

prime by prime: the remaining product
$\prod_{p\mid r}(1-2/p)(1-1/p)^{-1}(p-1)/(p-2)$ is one. This proves (4) without changing $N$ in the physical test. With the stated nonnegative test, $\mathcal I_\beta\gg Y^\beta/G$ on the original fixed dyadic window, and $\Sigma(N)\gg1$ for even $N$. Thus $H\le g^{1/3}$ and, say, $A>2$ suffice for the sign. The whole-line substitute instead carries $-\chi(N)\gamma_N\Sigma(Nr)$ times that same positive physical test, by (13) of the shifted proof. Its sign is therefore opposite when $\mu(r)=-1$.

## 3. Automatic separation for a hypothetical prime conductor

If the actual odd Page conductor $r$ is prime, (3) asks solely for $\log r\ge(2B+\eta)g$. For the original Page strip, the [all-scale exceptional proof](r87-spectral-all-scale-exceptional-left-reduction.md), Section 1, checks via the classical Siegel bound that $r>G^K$ eventually for every fixed $K$: $1-\beta\ll G^{-1/2}$ and $1-\beta\gg_\epsilon r^{-\epsilon}$ force this after choosing $\epsilon<1/(2K)$. Thus separation is automatic in this conditional prime case. The inequality is ineffective and does not assert such a zero exists or that the rational margin automatically holds.

The small target-mask hypothesis excludes only a vanishing ambient fraction in this prime case. Indeed for $A_N=\sum_{p\mid N}p^{-3/4}$, expand $e^{A_N}$ as a positive squarefree divisor sum. The count of multiples of $d$ in $[Y,2Y]$ is at most $2Y/d$ if $d\le2Y$ and zero otherwise. Thus $Y^{-1}\sum_{Y\le N\le2Y}e^{A_N}\le2\prod_p(1+(e^{p^{-3/4}}-1)/p)\ll1$. Outside $O(Y e^{-g^{1/3}/2})$ ambient targets one has $A_N\le g^{1/3}/2$, and for a prime conductor this implies $H\le g^{1/3}$ eventually. Odd-disjointness remains a literal hypothesis, and the statement is about the unsigned exceptional component only, with no inference for the signed pole or Hypothesis S.
