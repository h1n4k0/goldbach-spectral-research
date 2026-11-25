# The exceptional correction in a signed mean on the complete planting

**Scope.** This averages the genuine mixed-strip exception and the genuine full and original moving polynomial-major correlations over a **complete prescribed divisibility family**, without discarding any of its targets. The left tests have one common scaled shape throughout the dyad, and the target test has bounded variation. If the actual Page conductor does not divide the planting integer, its exceptional correction has arbitrarily small signed mean. If it divides, a finite averaged two-pole term is retained, with no size claim. No Dirichlet GRH or external real-zero-gap theorem is used. This is not a mean of absolute values, an assertion for individually adapted target tests, or a result on prime pairs or Hypothesis S.

Use the notation and genuine coefficients of [the all-scale reduction](r87-spectral-all-scale-exceptional-left-reduction.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, $L=\log N$, $D_N=\sqrt N L^{-B}$ and $H_{0,N}=\sqrt N L^{-B_0}$ for fixed admissible $B>B_0>0$. The two true squarefree factor-count parity coefficients $M_{\pm,N}$, the original moving polynomial arcs of denominator bound $N^{1/1000}$, and the possible single Page zero of primitive real $\chi$ with conductor $r\le Q_0$ and $\beta>1-4a_0/\sqrt G$ are unchanged. If no such zero exists, the genuine correction $\mathfrak E_\pm$ is zero.

Fix a real half-open $J\subset(1/2,9/16]$, a bounded-BV left weight $w$ on $J$, and a bounded-BV target weight $\eta$ on $[1,2]$. Their supremum and pointwise variation are bounded by a common fixed constant. They may depend on the dyad but are common to all $N$ in it. Use the actual $I_N=NJ$ and $\omega_N(u)=w(u/N)$, with their literal point values. Write $S_\pm(N)$ for the genuine full signed correlation and $S_\pm^{\rm maj}(N)$ for the integral on its **actual original moving** majors, with these tests and the true left log-prime weights. For any even integer $2\le K\le e^{2Z}$ constant across this dyad, set

$$
       \langle F\rangle_K
       =\frac K Y\sum_{\substack{Y\le N\le2Y\\K\mid N}}
                                      \eta(N/Y)F(N).
 \tag{1}
$$

### The signed exceptional term for any fixed dyad progression

In the presence of the zero, use the finite algebraic model $\mathcal D_i(N)$ of [the all-target Ramanujan formula](r94-spectral-all-target-ramanujan-exception.md), i.e. the actual right hand side (3) of [the two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md), with color $i=0,1$. Its dyad-fixed quantities $\chi,\beta,r,t\le Q_0/r,S=Y^{1/10}$ stay fixed. Define $\overline{\mathcal D}_{i,K}(v)$ for real $v\in[Y,2Y]$ by evaluating the physical test and cutoff formulas at $N=v$, and changing only the factors at $p\mid q$ in that formula's $\mathcal L(h;q,N)$ as follows. Set $\gamma_K(p)=1$ for $p\mid K$, and $\gamma_K(p)=1/p$ otherwise. At $p\mid(q,h)$ replace $E_p^2\mathbf1_{p\mid N}$ by $E_p^2\gamma_K(p)$; at $p\mid q,\ p\nmid h$ replace the local factor by

$$
       E_p^2\left(\frac{1-\gamma_K(p)}{p-1}
                                   -2c_p\gamma_K(p)\right).
 \tag{2}
$$

Here $c_p=\chi(p)p^{-\beta}$ and $E_p=(1-c_p)^{-1}$ as there. All remaining factors of $\mathcal L$, including at $p\nmid q$, are identical. This is a finite, explicitly defined algebraic average after the actual character calculation, not a prime-divisibility probability assumption.

**Theorem 1.** With the genuine correction, in the presence of the zero,

$$
  \langle \mathfrak E_\pm\rangle_K
    = \frac{\mathbf1_{r\mid K}}{2Y}
              \int_Y^{2Y}\eta(v/Y)
                  \{\overline{\mathcal D}_{0,K}(v)
                        \ \pm\overline{\mathcal D}_{1,K}(v)\}\,dv
       + O\!\left(Y^\beta G^C r^{-1/2}\right)
 \tag{3}
$$

with a fixed $C$, uniformly in $K,J,w,\eta$. In particular it is $O_A(Y^\beta G^{-A})$ for every fixed $A$ when $r\nmid K$, by the classical conductor growth at this Page threshold. No condition measures how much of $r$ fails to divide $K$. There is no margin requirement between $r$ and $Q_0$.

### The signed genuine full and original-major means on the complete planting

Now fix the prescribed even planting integer $K=K_z=2\prod_{2<p\le z,\ p\in\mathcal P}p$ from [the all-scale planted family](r87-spectral-all-scale-exceptional-left-reduction.md). Here $\mathcal P$ is any fixed nonempty union of reduced residue classes of fixed modulus, of density $d\in(0,1]$, and $G^\epsilon\le z\le Z$ for fixed $0<\epsilon<1/2$. Write $\ell=\log z$, $\theta_z=\ell/\log G$, and $s_d=d/(2d+1)$. Let $\mathcal K_{\pm,d}$ be the actual [positive-cut Dickman constants](r83-spectral-ap-radical-major-law.md). Define $\mathcal E_{\pm,K}$ to be the integral term on the right of (3) if the zero exists, and zero otherwise.

**Theorem 2.** On every sufficiently large dyad the two actual means on this **complete** $K_z$ family satisfy, for each fixed $A>0$,

$$
 \begin{split}
 \langle S_\pm\rangle_{K_z},\ \langle S_\pm^{\rm maj}\rangle_{K_z}
    ={}&\frac{K_z}{\varphi(K_z)}
        \mathcal K_{\pm,d}
            \left(\frac{2B}{\theta_z},\frac{B-B_0}{\theta_z}\right)
        \left(\int_J w(s)\,ds\right)
        \frac1Y\int_Y^{2Y}\frac{\eta(v/Y)v}{\log v}\,dv\\
       &+\mathcal E_{\pm,K_z}
        +O_A\!\left(
           \frac{K_z}{\varphi(K_z)}\frac{Y|J|}{G}\ell^{-s_d}
                                            +YG^{-A}\right).
 \end{split}                                                       \tag{4}
$$

The error is uniform across the allowed $z$ and all the declared tests. Both means in (4) include all actual multiples of $K_z$ in the dyad. In particular the formula has no exceptional term if there is no Page zero or $r\nmid K_z$. Since $K_z$ is squarefree, every **even** primitive real Page conductor fails to divide it: its two-part is $4$ or $8$. The remaining possible correction in (4) is when the odd Page conductor is supported on the complete planting. It is not being estimated. The assertion when $r\nmid K_z$ does not say that the term is pointwise small on that family.

## 1. Exact arithmetic projection before a growing cutoff

We prove (3) with the actual R94 formula, including its $O(Y^\beta G^C r^{-1/2})$ error, which is unchanged by (1) since the number of sampled points is $O(Y/K)$. For each fixed short product $h=u_1u_2$ and $q\mid t$ in the model, the only nonconstant dependence of $\mathcal L(h;q,N)$ on the arithmetic of $N$ is through $p\mid N$ at $p\mid q$; all these primes are coprime to $r$. Write its exact expansion as

$$
                 \mathcal L(h;q,N)=
                    \sum_{a\mid q} A_{h,q}(a)\mathbf1_{a\mid N}.
 \tag{5}
$$

It is a finite expansion, since $q$ is squarefree. Each factor at $p\mid q$ has two values, and is their affine expression in $\mathbf1_{p\mid N}$. The sum of absolute coefficients of that affine factor is $O(1)$ uniformly, since $\beta\ge.99$ eventually and $E_p$ is bounded. The factors outside $q$ away from $h$ have absolute product $O(1)$ by $\sum p^{-2\beta}<\infty$ at this uniform range. Those at $p\mid h$ outside $q$ have magnitude $E_p^2$; their product is $G^{O(1)}$, using $h\le Y^{1/5}$ and $\sum_{p\mid h}p^{-\beta}\ll\log\log G+1$ by splitting at $G$, as in the actual R94 bound. Thus
$\sum_{a\mid q}|A_{h,q}(a)|\ll G^{O(1)}C_1^{\omega(q)}$ with a fixed $C_1$, and the entire sum over $t,q,a$ including the absolute weights $|\mu(t)|q|\mu(t/q)|/\varphi(t)$ is $G^{O(1)}Q_0^{O(1)}$. Here $\omega(q)$ in the exponent counts distinct primes, not the left weight. This subpower loss can be afforded because the errors below save a power of $Y$.

For the physical integral of a fixed $u_1,u_2$ and color $i$, use $x=v(1-s)$, where $s\in J$ and $N=v$ is evaluated on the real dyadic interval. Let $\mathcal W_i(v;u_1,u_2)$ be this physical integral with the factor $\eta(v/Y)$ included, but without the short weight $\chi(u_1u_2)/(u_1u_2)^\beta$ or any rational factor. It is exactly

$$
     \eta(v/Y)v^{2\beta-1}
       \int_J w(s)\{s(1-s)\}^{\beta-1}
                          \mathcal G_i(v(1-s);u_1,u_2;v)\,ds,
 \tag{6}
$$

where the final argument $v$ specifies that $D_v,H_{0,v}$ are used in $\mathcal G_i$ of the two-pole formula. For each $s$, $T=\log(1-s)+2B\log\log v$ and the second real width is the positive part of the minimum of $T/2$ and
$\tfrac12\log(1-s)+B_0\log\log v+\log\max(u_1,u_2)$. Both $T$ and the resulting width $W$ have supremum $O(\log G)$ on the actual dyad, and total variation $O(1/G)$ by the positive-part and minimum inequalities and monotonicity of $\log\log v$. Also $\rho=|\log(u_1/u_2)|\le G/10$, and the denominator $\log(v(1-s))\asymp G$. Consequently the two $\mathcal G_i$ have bounded supremum plus variation by a fixed power of $G$, uniformly in $s,u_1,u_2$. Multiplication by $v^{2\beta-1}$ and $\eta(v/Y)$, then integration in the fixed $s$ domain, shows

$$
      \|\mathcal W_i\|_\infty+\operatorname{Var}_{[Y,2Y]}(\mathcal W_i)
                       \ll Y^{2\beta-1}G^{O(1)} .
 \tag{7}
$$

This calculation is why a common scaled shape is required. It keeps all actual moving physical cutoffs, does not freeze them, and works with pointwise-BV target weights.

For each $a\mid q$ in (5) the retained targets are multiples of $K_a=[K,a]$, where $(a,r)=1$. If $r\nmid K$, then $(r,K_a)=(r,K)<r$. The normalized sequence $c_r(K_a n)/\varphi(r)$ is bounded by one and has exact zero mean over a complete period of length $r/(r,K_a)$. Indeed for each unit numerator the sum of $e(bK_a n/r)$ over that period vanishes. Therefore any partial interval in $n$ has sum $O(r)$, and partial summation with (7) bounds the corresponding sample of $\mathcal W_i$ by $O(rY^{2\beta-1}G^{O(1)})$. This is cancellation at each fixed divisor constraint, not a cancellation through a set that discards arbitrary targets.

If $r\mid K$, then the normalized Ramanujan factor is exactly one at every sampled $N$. For a pointwise-BV $\mathcal W_i$ the arithmetic sample on multiples of $K_a$ is
$K_a^{-1}\int_Y^{2Y}\mathcal W_i(v)\,dv+
O(\|\mathcal W_i\|_\infty+\operatorname{Var}(\mathcal W_i))$.
For example partition into consecutive cells of length $K_a$, compare the point to the cell average by its variation, and leave the two partial end cells as supremum errors. After multiplying by $K/Y$, the continuum multiplier is $(K,a)/(aY)$. This factor is multiplicative in squarefree $a$, with the values $\gamma_K(p)$ of (2). Applying it to (5) therefore gives **exactly** the two replacement factors (2), with no independence assumption and while retaining the true finite $t$ sum.

In either case the total discretization error after the short weights is bounded by
$Y^\beta G^{O(1)}(K/Y)rQ_0^{O(1)}$, since
$\sum_{u_1,u_2\le S}(u_1u_2)^{-\beta}\ll G^2Y^{(1-\beta)/5}$,
$2\beta-1+(1-\beta)/5\le\beta$, and the outer factor $r/(\varphi(r)L'(\beta,\chi)^2)$ is $G^{O(1)}$ by the earlier reciprocal bound. The fixed $Q_0$ and $K,r$ here are all $e^{O(Z)}=Y^{o(1)}$. Thus this error is absorbed by $Y^\beta G^C r^{-1/2}$. Combining with R94 and the true parity half-sum proves (3) and both conditional cases.

## 2. Transfer the signed mean to the two genuine arc decompositions

Use the deterministic auxiliary evaluation in [Section 3 of the folded-sampling proof](r89-spectral-exceptional-conductor-folded-sampling.md#3-consequences-for-the-genuine-full-and-original-major-sums): at **every** actual even $N$ in the dyad the real common auxiliary major integral equals $\mathcal B_\pm(N)+\mathfrak E_\pm(N)+O_A(YG^{-A})$. Here $\mathcal B_\pm$ is the exact uncolored completed finite-cut bracket defined there. Its deterministic proof uses neither a planting/moment hypothesis nor a smallness claim for $\mathfrak E_\pm$: it is the step **before** taking relative exceptional sets. We leave all profile coefficients of $\mathcal B_\pm$ intact initially.

The [true fixed auxiliary complement bound](r86-spectral-universal-good-scale-windows.md#2-common-analytic-inputs-and-disjoint-error-budgets) gives an ambient squared sum at most $Y^3G^{O(1)}Q_0^{-1/2}$, uniformly in the actual admissible tests. This bound does not use zero-freeness or the profile hypothesis. By Cauchy--Schwarz, the mean of its modulus on all $K$ multiples, with $\eta$ bounded, is

$$
                 \ll YG^{O(1)}\sqrt K\,Q_0^{-1/4}
                          \ll YG^{O(1)} e^{-3Z}.
 \tag{8}
$$

This uses the full ambient mean-square bound, so it does not omit any exceptional points on the sampled progression. Adding this genuine common complement gives the corresponding signed mean identity for the full sum.

For the [true original moving minor](r79-spectral-original-minor-power-exception.md), use its $O(Y^{1-1/40000})$ bound off $O(Y^{1-3/10000})$ ambient targets. On those remaining targets, trivial torus Cauchy--Schwarz gives $O(YG^{O(1)})$ for the actual moving integral: the left norm uses the actual log-prime weights bounded by $O(G)$ on the physical support; the right norm uses the true fixed-order divisor moment in the original minor proof. Thus its absolute mean on all $K$ multiples is at most

$$
                \ll Y^{1-1/40000}
                      + K G^{O(1)}Y^{1-3/10000},
 \tag{9}
$$

again with no points discarded. Since $K\le e^{2Z}$, both (8) and (9) are smaller than $YG^{-A}$ for every fixed $A$. Subtract the actual original moving minor from the full sum to obtain the same mean identity on the original moving majors, without identifying the two kinds of arcs.

## 3. Quantitative profile and singular-series mean on the literal $K_z$

Take $K=K_z$ now. On its complete multiples the actual divided-by-$K_z$ Euler moment of [R90, Section 2](r90-spectral-all-scale-translates-conductor-trim.md) gives
$X_N=\sum_{p\mid N,\ p\nmid K_z}(\log p)/p=O(\log(2\ell))$
off $O_A((Y/K_z)G^{-A})$ targets for every $A$. Its counting proof is valid on multiples of any fixed dyad divisor with this size; no conductor selection is required for that moment. Even on the omitted moment targets we keep the exact bracket in the mean. In fact the uniform bounds for the actual normalized primitives in [the quantitative profile proof](r91-spectral-polylogarithmic-trim-quantitative-profile.md#2-quantitative-convergence-on-the-complete-initial-ap-mask) are $\|f_{N,j}\|_1\ll1$, $\|f_{N,j}\|_2\ll\sqrt\ell$, $|v f_{N,j}(v)|\ll1$, with the uniform signed absolute half-moment of the $j$ weights. The exact formula (15) in R90 gives
$|\mathcal B_\pm(N)|\ll \Sigma(N)|I_N|(1+\ell)/L$ for all targets, without using strong profile convergence: the rescaled positive cap is $O(1)$, and the crude full $L^2$ bound controls the terminal square and the point autocorrelation even when the finite terminal threshold vanishes. Since $\Sigma(N)\ll G^{O(1)}$, the moment-exception contribution is $O_A(YG^{-A})$ by first asking for a stronger moment count.

For every other $N$ use [the quantitative mask-to-profile argument, Sections 2--4](r91-spectral-polylogarithmic-trim-quantitative-profile.md), with the removal measure **the unit mass at zero**. The base is exactly the prescribed AP mask $K_z$ and the only change is the positive Euler addition for the actual primes dividing $N$ outside $K_z$, whose mean on log scale is $O(X_N/\ell)$. Those analytic sections use that moment and $\ell\asymp\log G$, not the earlier conductor-trim estimates for the prime arithmetic. Thus, at precisely this untrimmed base, their quantitative approximation of the exact bracket gives the leading profile with error
$O(\Sigma(N)|I_N|\ell^{-s_d}/L)$, with true positive cutoffs and the cusp treatment unchanged. We have not applied R91's full-correlation theorem on an unselected target. Here $\theta_z$ is common on the dyad, the limit constants are bounded on the fixed compact positive cutoffs, and
$\int_{I_N}\omega_N(u)/\log(N-u)\,du=(N/L)\int_Jw(s)\,ds+O(N|J|/G^2)$.
The latter follows by $u=Ns$ and $\log(1-s)=O(1)$ on the fixed central range. Its error is also within the claimed natural-scale profile error.

We finish by computing a deterministic weighted singular-series mean for this progression. For any even $K$ in the stated range and integer $m$ one has
$\Sigma(Km)=\Sigma(K)\sum_{a\mid m,(a,K)=1}g(a)$, where $g$ is nonnegative squarefree and $g(p)=1/(p-2)$ at odd primes, with $g(2)=0$. This follows by the standard binary singular product, with primes already in $K$ not counted again. Since $g(a)\le\tau_3(a)/a$ on squarefree $a$, one has $\sum_{a\le U}g(a)\ll(1+\log U)^3$ and $\sum_{a>U}g(a)/a\ll U^{-1/2}$ by the ordinary divisor Euler sum at exponent $3/2$. For any dyadic BV test $F(v)$, the same cell estimate as above gives

$$
 \frac K Y \sum_{\substack{Y\le N\le2Y\\K\mid N}}\Sigma(N)F(N)
     =\Sigma(K)\prod_{p\nmid K,\ p>2}\left(1+\frac{1}{p(p-2)}\right)
                     \frac1Y\int_Y^{2Y}F(v)\,dv
       +O\!\left(\Sigma(K)(\|F\|_\infty+\operatorname{Var}F)
          \left[\frac K Y G^3+\left(\frac K Y\right)^{1/2}\right]\right).
 \tag{10}
$$

Indeed expand the divisor sum up to $2Y/K$, apply the sample formula on $Ka$ multiples, and complete the absolutely convergent remaining Euler sum. There are no statistical priors in (10). The product prefactor is exactly $K/\varphi(K)$: for primes not in $K$, the new local factor is the inverse of the usual unoccupied singular factor, and for $p\mid K$ its original local is $p/(p-1)$, including $p=2$. With $F(v)=\eta(v/Y)v/\log v$ its norm is $O(Y/G)$, so the error in (10) is negligible to every fixed log accuracy. The same calculation with the positive weight $v/\log v$ bounds the average of the natural-scale profile error, and the leading profile on the moment-exception targets is also negligible by the preceding crude estimates.

Combining (3), (8)--(10) and the actual quantitative bracket approximation gives (4). If $r$ is even, primitivity of the real character implies its two-primary conductor is $4$ or $8$, as in the long unsigned deletion; a character on a product with two-part exactly $2$ would induce from the odd modulus. Thus the indicated even-conductor vanishing criterion on the squarefree complete planting is genuine. The proof gives signed means only; no estimate of the absolute aligned term or of target-specific full coefficients follows.
