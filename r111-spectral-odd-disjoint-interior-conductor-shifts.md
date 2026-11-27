# The odd-disjoint unsigned correction counts interior conductor shifts away from the cap wall

The ordinary part of the unsigned exceptional correction is tested on a finite logarithmic cap. When conductor shifts avoid a narrow collar of that wall, **interior** shifts contribute the whole ordinary autocorrelation mass, while exterior shifts contribute no main term. The resulting signed coefficient is a finite rational sum over the true interior shifts. It is neither the zero-shift term alone nor the coefficient obtained by sending the physical cap to infinity.

## 1. Exact scope and statement

Use the genuine even dyad $Y\le N\le2Y$ and the actual $I,\omega$ of the [odd-disjoint two-positive formula](r106-spectral-odd-disjoint-two-positive-unsigned-mode.md), with its bounded pointwise-BV test $\omega$ on the real half-open $I\subset(N/2,9N/16]$. Keep the fixed allowed $B>B_0>0$ and $D=\sqrt N(\log N)^{-B}$. Let $G=\log Y$, $g=\log G$, $Q_0=\exp(16\sqrt G/g)$, with an actual odd squarefree primitive Page conductor $r\le Q_0$, real character $\chi$, and simple real zero $\beta$ in the original strip. Assume $(N,r)=1$. Define

$$
 \begin{split}
 F(m)&=\omega(N-m)(N-m)^{\beta-1},\qquad L_m=\log m,\qquad
 T_m=\log(m/D^2),\\
 \mathcal I_\beta&=\int_{N-I}\frac{F(m)}{L_m}\,dm,\qquad
 H=\omega(r)+\sum_{p\mid N}p^{-3/4},\qquad
 C_r^{[2]}=\prod_{p\mid r}(1-1/p)(1-2/p).
 \end{split}                                                       \tag{1}
$$

Here $\omega(r)$ counts distinct conductor primes. As in the [separated unsigned proof](r109-spectral-pointwise-separated-unsigned-parity.md), the notation $\mathcal U=-\chi(N)C_r^{[2]}\mathcal P_1/\varphi(r)$ means exactly the unsigned component of the genuine exceptional parity difference. The $\mathcal P_1$ uses the literal original finite $t\le Q_0/r$, not a formally extended rational definition.

For each $\varepsilon=(\varepsilon_p)_{p\mid r}$ with $\varepsilon_p\in\{-1,0,1\}$, put

$$
 \begin{split}
 s_\varepsilon&=\sum_{p\mid r}\varepsilon_p\log p,\qquad
 c_\varepsilon=\prod_{\substack{p\mid r\\ \varepsilon_p\ne0}}(-\kappa_p),
      \qquad \kappa_p=\frac{p-1}{p-2},\\
 \mathcal J_r
    &=\sum_{\substack{\varepsilon\\ |s_\varepsilon|<2Bg}} c_\varepsilon .
 \end{split}                                                       \tag{2}
$$

The operator coefficients are exactly those of the [shifted autocorrelation](r108-spectral-odd-disjoint-shifted-autocorrelation.md); the absence, positive shift, and negative shift are the three allowed terms at each prime. Suppose the actual scale and conductor satisfy

$$
 H\le g^{1/3},\qquad \log(Q_0/r)\ge g^3,\qquad
       \bigl||s_\varepsilon|-2Bg\bigr|\ge g^{3/4}
                       \quad\text{for every }\varepsilon .       \tag{3}
$$

**Theorem.** For a fixed $c>0$ the true unsigned component then satisfies

$$
      \mathcal U
       =-\chi(N)\mathcal J_r\frac{\Sigma(N)}r\,\mathcal I_\beta
           +O\!\left(\frac{Y^\beta}{rG}e^{-c g^{3/8}}\right),     \tag{4}
$$

where $\Sigma(N)$ is the binary singular series at the original target. The anchor $2Bg$ in (2) determines membership exactly on the moving physical cap under (3); nothing in (4) changes the denominator cap, the hard interval, or that physical cap.

The exact coefficient $\mathcal J_r$ is nonzero on these separated walls. A quantitative consequence for the **sign of this one component** needs a lower bound relative to the error in (4). Two such regimes are given below. No sign of the separate signed pole, the full exceptional difference, or the full mixed sum is claimed here.

## 2. The finite cap sees the ordinary whole mass only from interior shifts

Let $C$ be the ordinary masked autocorrelation of the shifted theorem. It is even. In the finite color-one bracket of that theorem, keep its actual paired endpoint form when expanding individual shifts. In fact by $c_{-\varepsilon}=c_\varepsilon$, one has the exact identity

$$
 \begin{split}
 \int_{-T_m}^{T_m}(\mathscr L_r C)(v)\,dv
                    -T_m(\mathscr L_r C)(T_m)
  = \sum_\varepsilon c_\varepsilon\bigg[
        \int_{s_\varepsilon-T_m}^{s_\varepsilon+T_m}C(t)\,dt
        -\frac{T_m}{2}
                  \big(C(s_\varepsilon-T_m)+C(s_\varepsilon+T_m)\big)
                                  \bigg].
 \end{split}                                                       \tag{5}
$$

Thus neither endpoint is discarded merely because the sum is even. On the genuine $m$-interval, $T_m=2B\log\log N+\log(m/N)=2Bg+O(1)$ uniformly. Put $a=g^{3/4}/2$. If a shift in (2) is interior, (3) implies $[s_\varepsilon-T_m,s_\varepsilon+T_m]\supset[-a,a]$ and both endpoints have absolute value at least $a$, for large $Y$. For an exterior shift its full interval lies outside $(-a,a)$ and again the endpoints have absolute value at least $a$.

The ordinary tail bound (5) of the separated proof, applied at $a$, is

$$
 \sup_{|t|\ge a}|C(t)|+\int_{|t|\ge a}|C(t)|\,dt
                        \ll \exp(C H-c_1\sqrt a).                 \tag{6}
$$

It holds uniformly on this same original masked $C$; it does not use the older all-shifts-exterior separation. Each individual shifted bracket in (5) is therefore $\mathbf1_{|s_\varepsilon|<2Bg}\int_{\mathbb R}C$, with absolute error at most $O((1+T_m)\exp(CH-c_1\sqrt a))$. The full finite sum of absolute shift coefficients is $\prod_{p\mid r}(1+2\kappa_p)\le5^{\omega(r)}$. Since $\sqrt a\asymp g^{3/8}$, $\omega(r)\le H\le g^{1/3}$ and $T_m\ll g$, summing gives

$$
      \int_{-T_m}^{T_m}(\mathscr L_r C)(v)\,dv
        -T_m(\mathscr L_r C)(T_m)
        =\mathcal J_r\int_{\mathbb R} C(t)\,dt
                                  +O(e^{-c_2 g^{3/8}}).          \tag{7}
$$

Restore the shifted proof's factor $\mathcal V_{N,r}$, the original $F(m)/L_m$ integration, and the exterior of $\mathcal U$. The unshifted mass is exactly $\mathcal V_{N,r}\int C=(r/\varphi(r))\Sigma(Nr)$. At each $p\mid r$, disjointness multiplies the singular factor from $N$ to $Nr$ by $(p-1)/(p-2)$; hence as in (7) of the separated proof,

$$
   \frac{C_r^{[2]}}{\varphi(r)}\,\frac{r}{\varphi(r)}\Sigma(Nr)
                             =\frac{\Sigma(N)}{r}.                \tag{8}
$$

Also $\mathcal V_{N,r}\le1$, $C_r^{[2]}/\varphi(r)\le1/r$, and $\int_{N-I}|F(m)|/L_m\,dm\ll Y^\beta/G$. This restores the scale of the error in (7). The original short endpoint approximation of the shifted proof has error $O(Y^\beta e^{-c_3\sqrt G}/r)$ after the exterior. The controlled finite rational comparison in the [short-log formula](r107-spectral-odd-disjoint-short-log-kernels.md), before the exterior, costs at most $O(Y^\beta G^C e^{CH}(Q_0/r)^{-1/4})$, and after the exterior this is smaller than the error in (4) under (3). Thus both comparisons are absorbed without changing the actual finite $\mathcal P_1$. This proves (4) for the genuine unsigned component. The raw error of the two-positive decomposition of the genuine difference, $O(Y^\beta G^C/Q_0)$, would also be smaller under (3); its distinct signed pole would still remain.

## 3. Exact nonvanishing and robust sign cases

The only zero shift is $\varepsilon=0$, since the $\log p$ are linearly independent over integer coefficients by unique factorization. It contributes $1$ to (2). The nonzero selected shifts occur in distinct pairs $\varepsilon,-\varepsilon$ with equal rational coefficients. Let $D_r=\prod_{p\mid r}(p-2)$, an odd positive integer. Then $D_r\mathcal J_r$ equals $D_r$ plus an even integer, because for every shift $D_rc_\varepsilon$ is integral. In particular

$$
           D_r\mathcal J_r \equiv D_r\pmod{2},
                  \qquad |\mathcal J_r|\ge D_r^{-1}.             \tag{9}
$$

The latter lower bound by itself can be too small to deduce the sign of $\mathcal U$ at the scale of (4).

**Large conductor primes.** If all $p\mid r$ satisfy $p\ge e^{g^{1/2}}$, replace every $\kappa_p$ by $1$ in the coefficients of (2), without changing which shifts are selected. For any finite subset of assignments the absolute coefficient error is bounded by the error sum over all assignments, which is at most $O(5^{\omega(r)}\omega(r)/p_{\min})=o(1)$: telescope the product, at each prime $p$ use $|\kappa_p-1|=(p-2)^{-1}$ and the absolute row sums at most $5$. The new coefficient is the signed count

$$
           J_{\mathrm{int}}
              =\sum_{\substack{\varepsilon\\ |s_\varepsilon|<2Bg}}
                      (-1)^{\#\{p:\,\varepsilon_p\ne0\}}.        \tag{10}
$$

It is an odd integer by the same pairing. Hence $\mathcal J_r=J_{\mathrm{int}}+o(1)$, its absolute value is at least $1-o(1)$, and its sign is that of $J_{\mathrm{int}}$. For a nonnegative test with $\int_I\omega(u)\,du\ge c_{\mathrm{test}}Y$, $\mathcal I_\beta\gg Y^\beta/G$ and the even-target $\Sigma(N)\gg1$; the true unsigned contribution consequently has sign $-\chi(N)\operatorname{sgn}(J_{\mathrm{int}})$.

**One short prime in a two-prime conductor.** Suppose instead the actual conductor is $r=pq$, with distinct odd primes and $p\le G^B$, and assume the same mask and original rational margin of (3). The Page conductor grows faster than every fixed power of $G$ as in the [all-scale exceptional reduction](r87-spectral-all-scale-exceptional-left-reduction.md), by the classical Siegel bound. Thus $q$ also grows faster than every fixed power of $G$, uniformly along such actual conductors. The only interior shifts are $0,\pm\log p$, while the intervals centered at $\pm\log q$ or $\pm\log q\pm\log p$ lie well outside the cap; the wall condition of (3) is automatic eventually since the interior gaps are at least $Bg$. Therefore

$$
             \mathcal J_r=1-2\kappa_p=-\frac{p}{p-2}\le -1.        \tag{11}
$$

With the same positive macroscopic test, the unsigned contribution in (4) has sign $+\chi(N)$. The hypothetical whole-line substitute for (5) would instead use $\prod_{v\mid r,\ v\ {\rm prime}}(1-2\kappa_v)>0$, not (11), and would give sign $-\chi(N)$ after the common exterior. This is an opposite-sign comparison with the formal whole-line calculation, not with the separate physical signed-pole term. Neither existence of such Page conductors nor the required rational-cap margin for them is asserted.
