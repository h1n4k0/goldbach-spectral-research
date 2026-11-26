# Finite-cap autocorrelation for the odd-disjoint two-positive parity mode

On the genuine odd-disjoint targets of the [two-positive reduction](r106-spectral-odd-disjoint-two-positive-unsigned-mode.md), the color-1 signed short-log kernel admits a finite-cap autocorrelation formula. This removes the short-log summation endpoints in that color at a stretched-exponential cost, while keeping the actual physical cap and its endpoint term. The ordinary masked autocorrelation has a nonnegative Fourier transform before the finite signed conductor shifts. Neither that property nor a whole-line normalization supplies the sign of the actual parity difference.

Retain the notation and all hypotheses of the [short-log kernel theorem](r107-spectral-odd-disjoint-short-log-kernels.md). Thus an actual odd squarefree primitive Page conductor $r\le Q_0$ is coprime to the even $Y\le N\le2Y$; $G=\log Y$, $Q_0=\exp(16\sqrt G/\log G)$, $S=Y^{1/10}$, $\gamma_N=\mu(r)/\varphi(r)$. In the true physical integral $m\in N-I$, put $L_m=\log m$, $T_m=2\Delta_m=\log(m/D^2)>0$, and $F(m)=\omega(N-m)(N-m)^{\beta-1}$. In particular $L_m\asymp G$ and $T_m\ll\log G$. The raw errors and both original signed-pole pieces are unchanged.

For $(j,Nr)=1$ with $j$ squarefree, let the ordinary masked primitive and its autocorrelation be

$$
 R_j(t)=\sum_{\substack{n\le e^t\\(n,jNr)=1}}\mu(n)\alpha^\circ(n),
 \qquad C_j(t)=\int_{\mathbb R}R_j(x)R_j(x+t)\,dx,\qquad
 C(t)=\sum_{\substack{j\ {\rm sf}\\(j,Nr)=1}}
           \mu(j)\alpha^\circ(j)^2 C_j(t).
                                                               \tag{1}
$$

Here $R_j(t)=0$ for $t<0$, $\alpha^\circ$ is multiplicative on squarefree integers with $\alpha_p^\circ=(p-1)/(p^2-2)$ at the allowed primes, and the $n$ sum is squarefree by $\mu$. Define $T_h C(t)=C(t+h)$ for the one-dimensional shifts, and

$$
 \mathscr L_r=\prod_{p\mid r}
   \bigl({\rm Id}-\kappa_p T_{\log p}-\kappa_p T_{-\log p}\bigr),
 \qquad \kappa_p=(p-1)/(p-2).
                                                               \tag{2}
$$

In terms of $\mathcal V_{N,r}$ from the short-log theorem, set

$$
 \mathcal P_1^{\rm ac}=
   \mathcal V_{N,r}\int_{N-I}\frac{F(m)}{L_m}
    \left[
      \int_{-T_m}^{T_m}(\mathscr L_r C)(t)\,dt
       -T_m(\mathscr L_r C)(T_m)
    \right]\,dm.
                                                               \tag{3}
$$

There is a fixed $c>0$ such that the completed short-log color 1 satisfies

$$
       \widehat{\mathcal P}_1=\mathcal P_1^{\rm ac}
                   +O(Y^\beta e^{-c\sqrt G}).
                                                               \tag{4}
$$

This comparison uses no new rational-cap margin. In particular under the existing local margin
$\log(Q_0/r)\ge C_A(\log G+\omega(r)+\mathcal A_{N,r})$,
$\mathcal A_{N,r}=\sum_{p\mid N,\ p\nmid r}p^{-3/4}$,
one may use (3) in the **actual** exceptional parity difference with error $O_A(|\gamma_N|Y^\beta G^{-A})$, in addition to the existing raw error. More explicitly the two-positive reduction then reads

$$
 \mathfrak E_+-\mathfrak E_-
    =\gamma_N\mathcal D_1-
       \frac{\chi(N)C_r^{[2]}}{\varphi(r)}\mathcal P_1^{\rm ac}
      +O_A\bigl(|\gamma_N|Y^\beta G^{-A}+Y^\beta G^C Q_0^{-1}\bigr),
 \qquad C_r^{[2]}=\prod_{p\mid r}(1-1/p)(1-2/p).
                                                               \tag{5}
$$

Equation (5) is only an exceptional correction formula. In particular it asserts no existence of an exceptional zero, no sign or relative size for the remaining signed pole $\mathcal D_1$, and no conclusion on a full correlation.

## 1. Ordinary primitives with the true deleted primes

Use the ordinary reciprocal Möbius primitive $R_*(u)=\sum_{n\le e^u}\mu(n)/n$, zero below zero, with $R_*(u)\ll e^{-c_0\sqrt u}$ on $u\ge1$ and $\int R_*=1$, as in Section 2 of the [ordinary cap proof](r80-spectral-whole-mixed-parity-density.md). The first estimate is the classical unconditional input already used there. For the unmasked $\alpha^\circ$ model take $\alpha_2^\circ=0$; deleting primes of $jNr$ then gives exactly (1), since $2\mid N$. For a prime $p$, the ratio of the two local Euler factors, from $1-X/p$ to $1-\alpha_p^\circ X$, is a series with nonnegative coefficients: if $p>2$, $0<\alpha_p^\circ<1/p$, and the difference in the numerator is nonnegative after division. If the prime is deleted, insert additionally $(1-\alpha_p^\circ X)^{-1}$. With $X$ acting by the shift in the cumulative primitive $u\mapsto u-\log p$, this represents $R_j$ as the convolution of $R_*$ with a positive measure supported in $[0,\infty)$. The identity may first be read at the finitely many possible shifts $\le u$; the following absolute moment then also makes the global convolution legitimate.

For $\delta=1/4$, the unmasked ratio has uniformly bounded $\delta$-exponential moment, since its nonconstant local contribution for odd $p$ is $O(p^{-2+\delta})$, and the factor at 2 is finite. Put

$$
 A(v)=\prod_{\substack{p\mid v\\p>2}}
         (1-\alpha_p^\circ p^{1/4})^{-1}.
\quad
 \|R_j\|_1+\|R_j\|_2+\|R_j\|_\infty\ll A(Nr)A(j).
                                                               \tag{6}
$$

Indeed the shifted kernel has exponential moment $\ll A(Nr)A(j)$, and each unshifted norm of $R_*$ is bounded. For large $a$, the same bound multiplied by $e^{-c_1\sqrt a}$ holds for the three corresponding tail norms on $[a,\infty)$. To see this, split the shifts at $a/2$: the first part only sees the ordinary primitive on $[a/2,\infty)$, while Minkowski and the exponential moment bound the second part by $O(e^{-a/8}A(Nr)A(j))$. Reduce $c_1>0$ to absorb the polynomial prefactors from integrating the ordinary tail. Thus the tail bound applies to the exact right-continuous value $R_j(a)$ as well. It is uniform in all the masks.

For $v\ge2$, $\log A(v)\ll(\log(2v))^{1/4}$: split the sum of $O(p^{-3/4})$ at $\log(2v)$, bounding the small prime sum by the corresponding integer sum and the number of larger divisors by $\log v/\log\log(2v)$ when the latter denominator is at least 1. The finite smaller cases are absorbed into the constant. Also

$$
 \sum_{j\ {\rm sf}} j^{1/2}\alpha^\circ(j)^2 A(j)^2\ll1.
                                                               \tag{7}
$$

Here the majorant uses $\alpha^\circ_2=0$ and a convergent Euler product with odd-prime increments $O(p^{-3/2})$. In particular (1) converges absolutely in $L^1$ and uniformly, because $\|C_j\|_1\le\|R_j\|_1^2$ and $\|C_j\|_\infty\le\|R_j\|_2^2$. Each $C_j$ is even and continuous by $L^2$ translation; so is $C$.

## 2. Genuine short endpoints and the boundary term

Write $J_m(w)=-|w|\min(\Delta_m,|w|/2)$, so the original color-1 kernel is $J_m(x-y)/L_m$. In the exact completed short sum choose one term of the conductor shift product, with shifts $s_1,s_2\ge0$, $s_1+s_2\le\log r$. Expand the coprime constraint of the other labels as $\sum_{j\mid(u,v)}\mu(j)$. Upon writing $u=ju'$, $v=jv'$, squarefreeness imposes the additional deletion $p\mid j$ in both primes of the reduced labels, and the two signed weights of $j$ multiply to $\alpha^\circ(j)^2$. Write $s=s_1-s_2$. The common $\log j$ drops from the difference inside $J_m$, not from the two upper bounds. The resulting term before the outer coefficient $\mu(j)\alpha^\circ(j)^2$ and $L_m^{-1}$ is exactly

$$
 \iint_{\substack{x\le a_1\\y\le a_2}}
       J_m(x-y+s)\,dR_j(x)dR_j(y),
 \qquad  a_i=\log S-\log j-s_i.
                                                               \tag{8}
$$

The right-continuous hard tests include an atom at $a_i$ if present. For $j>Y^{1/50}$, the whole original weighted sum of (8) is $O(G^C Y^{-1/100})$ per conductor choice: wherever nonzero, its $J_m$ is bounded by $G^C$, each finite unsigned reciprocal sum is $\ll G^C$ by $\alpha^\circ(p)\le1/p$ and the prime harmonic bound, and (7) handles the reciprocal square. For $j\le Y^{1/50}$, $\log r=o(\sqrt G)$ gives $a_i\ge .07G$ at sufficiently large $Y$. Replace the two measures in (8) individually by

$$
       {\bf1}_{x\le a_i}\,dR_j(x)-R_j(a_i)\delta_{a_i}.
                                                               \tag{9}
$$

This is an exact zero-total-mass compactly supported signed measure with cumulative ${\bf1}_{x<a_i}R_j(x)$. The difference in (8) is bounded by the small endpoint masses times a fixed $G$-power, using the genuine finite unsigned weights for the other leg; the term with both endpoints obeys the same bound. Equations (6)–(7) make the weighted total $e^{-c_2\sqrt G+O(G^{1/4})}$ per conductor choice. In particular, no endpoint continuity of the discrete primitive is used.

As a distribution on the real line,

$$
 -J_m''(w)
   ={\bf1}_{(-T_m,T_m)}(w)-\tfrac{T_m}{2}
                              (\delta_{T_m}+\delta_{-T_m})(w).
                                                               \tag{10}
$$

Indeed $J_m=-w^2/2$ in the central interval and $J_m=-(T_m/2)|w|$ outside it. Its derivative has upward jump $T_m/2$ at each boundary. With the compact cumulatives in (9), two Stieltjes integrations by parts therefore pair the two cumulatives with $\partial_x\partial_y J_m(x-y+s)=-J_m''(x-y+s)$. For example smooth $J_m$ by a symmetric compact approximate identity: the smoothed $J_m$ converges uniformly on the finite integration box, and the correlation of the two compact cumulatives is continuous by $L^2$ translation, so (10) follows with its endpoint point masses. This also proves the formula when either $a_i$ or an endpoint in (10) corresponds to a discrete short log.

We may now replace each compact cumulative by full $R_j$. Its $L^2$ tail controls each point evaluation of the correlation error, and its $L^1$ tail controls the integrated error over any real interval, both with the corresponding full norm of the other slot. These estimates are uniform in the translate $s$. The multiplier on the two point evaluations is $O(T_m)$, hence harmless. For $j>Y^{1/50}$ the full-correlation contribution of (10), bounded by (6) with no tails, is $O((1+T_m)A(Nr)^2Y^{-1/100})$ by (7). This justifies restoring all $j$ in (1). Finally the absolute sum of the conductor choice coefficients is at most $5^{\omega(r)}$, and already $5^{\omega(r)}\le \exp(O(\log r))=\exp(o(\sqrt G))$ here. It preserves the claimed stretched-exponential saving.

For full $R_j$, the correlation before (10) is $C_j$, so the result is $\int_{-T_m}^{T_m}C_j(t+s)\,dt-(T_m/2)[C_j(T_m+s)+C_j(-T_m+s)]$. Each conductor prime can be assigned to neither slot or to exactly one; this produces exactly (2) on $C_j$. Since (2) preserves evenness, the endpoint evaluations combine into $-T_m(\mathscr L_r C)(T_m)$. Divide by $L_m$, restore the factor $\mathcal V_{N,r}\le1$ and integrate against the genuine $F(m)$ on $N-I$, whose absolute mass is $O(Y^\beta)$. This proves (4). The existing controlled completion of the finite $t$ sum in the short-log theorem and $C_r^{[2]}/\varphi(r)\le|\gamma_N|$ then give (5).

## 3. Fourier sign before conductor shifts and the whole-line check

Use $\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-i\xi t}\,dt$. Let $R_1$ be (1) with $j=1$, not an unmasked function. Because the additional deletion of a prime divides by $1-\alpha_p^\circ e^{-i\xi\log p}$, a nonzero factor, we have

$$
 \widehat C(\xi)=|\widehat R_1(\xi)|^2
       \prod_{p\nmid Nr}
          \left(1-\frac{(\alpha_p^\circ)^2}
                            {|1-\alpha_p^\circ e^{-i\xi\log p}|^2}\right)
       \ge0 .
                                                               \tag{11}
$$

This follows by Fourier transforming each $C_j$, summing its squarefree $j$ weights, and using (6)–(7). The product converges uniformly on the real axis; all local factors are strictly positive since $\alpha_p^\circ<1/2$. The same norm bounds and Plancherel give $\widehat C\in L^1$, so Fourier inversion applies at every $t$. In (3) the Fourier multiplier on (11) consists of the two real factors

$$
 \left(\frac{2\sin(T_m\xi)}{\xi}-T_m\cos(T_m\xi)\right)
       \prod_{p\mid r}\bigl(1-2\kappa_p\cos(\xi\log p)\bigr),
                                                               \tag{12}
$$

with the value $T_m$ for the first bracket at $\xi=0$; the inverse integral has its usual $1/(2\pi)$. In particular (11) does not allow positivity reasoning on the finite cap after (12), which has signed factors.

As a separate normalization check only, denote by $\Sigma(n)$ the usual binary singular series on an even argument $n$, with factors $(1-1/p)^{-1}$ when $p\mid n$ and $p(p-2)/(p-1)^2$ otherwise. In (11) at $\xi=0$, the primitive mass is the unmasked mass 1 times the positive ratios in Section 1. Consequently the local product for $\int C$ is $(1-2\alpha_p)/(1-1/p)^2$, where $\alpha_p=0$ for $p\mid Nr$. Multiplying this by the local default in $\mathcal V_{N,r}$ from the short-log theorem gives $\Sigma(Nr)$ at all $p\nmid r$, and at $p\mid r$ one obtains $(1-1/p)^{-2}$ instead of $(1-1/p)^{-1}$. Therefore $\mathcal V_{N,r}\int C=(r/\varphi(r))\Sigma(Nr)$. Since $\mathscr L_r$ has total signed shift mass $\prod_{p\mid r}(1-2\kappa_p)=\mu(r)\prod_{p\mid r}p/(p-2)$, the exact whole-line identity is

$$
 -\frac{\chi(N)C_r^{[2]}}{\varphi(r)}\,
         \mathcal V_{N,r}\int_{\mathbb R}\mathscr L_r C(t)\,dt
       =-\chi(N)\gamma_N\Sigma(Nr).
                                                               \tag{13}
$$

The argument $Nr$ in (13) is only an Euler normalization; neither the physical target nor its hard cutoff is changed. The full line integral in (13) is not the bracket in (3). In particular the allowed conductor shift range is $[-\log r,\log r]$, not a range proved smaller than $T_m$, and the endpoint term does not disappear from the actual formula.
