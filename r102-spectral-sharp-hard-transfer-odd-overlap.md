# A sharper actual hard transfer and the pointwise exceptional difference with one shared odd conductor prime

The hard exceptional correction can be transferred to its literal integer test with a full reciprocal power of the original denominator cap. In the two-pole reduction an exact character zero removes the remaining rare divisibility class as soon as the target and the Page conductor share an odd prime. Combining these two facts with the [partially aligned cap lower bound](r101-spectral-pointwise-partial-alignment.md) removes its missing-product power threshold on that set of actual targets.

Use the original mixed-strip exceptional terms $\mathfrak E_\pm$, the actual even target $Y\le N\le 2Y$, $G=\log Y$, $Z=\sqrt G/\log G$, and $Q_0=e^{16Z}$. If a genuine primitive real Page character $\chi$ occurs, let $r\le Q_0$ and $\beta$ be its conductor and simple real zero in the usual Page range, and write $r_{\rm odd}$ for the odd part of $r$. Use the exact original half-open $I\subset(N/2,9N/16]$, real test $\omega$ of bounded supremum and pointwise variation, and the same fixed admissible $B>B_0>0$. No numerical cutoff or local condition defining the actual parities is changed. When there is no such zero the exceptional terms are zero.

**Raw estimates.** Uniformly for the original hard tests, let $\mathfrak H_\pm$ be the genuine hard transfer of [R88](r88-spectral-hard-exceptional-residue-transfer.md), and let $\mathcal D_0(N),\mathcal D_1(N)$ be the exact finite algebraic two-pole expressions of the [all-target contraction](r94-spectral-all-target-ramanujan-exception.md). For a fixed $C$,

$$
    \mathfrak E_\pm-\mathfrak H_\pm
             = O(Y^\beta G^C Q_0^{-1}),                              \tag{1}
$$

and with the actual response $\gamma_N=c_r(N)/\varphi(r)$,

$$
 \mathfrak E_\pm
 =\frac{\gamma_N}{2}\bigl(\mathcal D_0(N)\pm\mathcal D_1(N)\bigr)
 +O\!\left(Y^\beta G^C\left\{Q_0^{-1}
      +\mathbf1_{(N,r_{\rm odd})=1}
                  \frac{\tau(r_{\rm odd})^5}{r_{\rm odd}}\right\}\right).
 \tag{2}
$$

Here $\tau$ is the divisor function. The second error term vanishes under any odd overlap. The same literal $t\le Q_0/r$ remains inside each $\mathcal D_i$; (2) is independent of any cap-completion margin and has no near-one closeness assumption beyond the original Page range.

**Pointwise consequence.** In addition assume the hypotheses on the zero closeness, denominator margin, nonnegative $\omega$ of positive physical mass and fixed-size primorial planting from the partially aligned cap theorem. Explicitly, $(1-\beta)G\le C_*\log G$, $\log(Q_0/r)\ge(\log G)^3$, $\int_I\omega\ge c_{\rm test}Y$, and $K_z\mid N$ for $z_*\le z\le Z$ with $z_*$ sufficiently large fixed. If $\gamma_N\ne0$ and $(N,r_{\rm odd})>1$, then for all sufficiently large such targets,

$$
 -\chi(-1)\operatorname{sgn}(\gamma_N)
              (\mathfrak E_+-\mathfrak E_-)
       \gg |\gamma_N|\frac{Y^{2\beta-1}}G
                     \frac{\Sigma^{(r)}(N)}{(\log r)^4}.            \tag{3}
$$

The factor $\Sigma^{(r)}(N)\ge\Sigma(N)$ is precisely that of R101, supplying conductor primes as occupied in the completed exceptional Euler product and leaving the real target unchanged. There is no additional upper bound on the missing odd product. This is a hypothetical pointwise exceptional-only sign and size statement, not a lower bound for either full parity or the full Goldbach sum, a signed mean, a conclusion that a Page zero exists, or a result on Hypothesis S.

## 1. Pair the exact hard step error with local divisor moments

For the genuine left weight put $F(x)=\omega(x)x^{\beta-1}$ on $I$, and zero off $I$. It has compact support and exact pointwise variation $O(Y^{\beta-1})$, including its actual endpoint values. The exact discrete exceptional formula used in R88 applies the band projection $W$ of $F$ on $[-\Delta,\Delta]$ with $\Delta=2Q_0/Y$. Write $d\mu=dF$ for the distributional derivative and $F_+(x)=\mu((-\infty,x])$ for the right-continuous representative. The signed measure is compactly supported and has mass zero. Its variation is at most the pointwise variation of $F$. For the designated integer values we also have

$$
                  \sum_{n\in\mathbb Z}|F(n)-F_+(n)|
                                  \le \operatorname{Var}(F).       \tag{4}
$$

Indeed for any finite selection of integers choose points just to their right, within disjoint short cells, converging to the right limits. The absolute increments sum to at most the full variation by joining the partitions in their natural order. Passing to the finite right limits and then to all integers yields (4).

In the standard transform convention $\widehat F(\eta)=\int F(x)e(-\eta x)\,dx$, where $e(t)=e^{2\pi it}$, integration by parts gives $\widehat F(\eta)=\widehat\mu(\eta)/(2\pi i\eta)$ for $\eta\ne0$. In particular the band projection, in the equivalent convention of R88, is exactly

$$
         W(x)=\int\left\{\frac12+
              \frac1\pi\operatorname{Si}(2\pi\Delta(x-u))\right\}d\mu(u),
 \qquad \operatorname{Si}(v)=\int_0^v\frac{\sin t}{t}\,dt.            \tag{5}
$$

To see the identity, first exclude a symmetric interval of radius $\varepsilon$ at zero from the frequency integral and interchange the finite integrals. The resulting sine-integral expression is bounded and tends to the displayed one, using zero total mass for the constant. Dominated convergence for fixed $x$ follows from the bounded sine integral and the finite measure. The small omitted Fourier integral also tends to zero because $\widehat F$ is bounded. The step error of the bracket in (5) against $\mathbf1_{x\ge u}$ is bounded by $C\min(1,(\Delta|x-u|)^{-1})$ with value bound $C$ at equality. This follows from the usual sine-tail bound by integration by parts and $\int_0^\infty\sin t/t\,dt=\pi/2$. Thus the error at any integer $n$ uses the integral of this local majorant against $|d\mu|$, plus the actual discrepancy in (4).

For clarity the local divisor estimate needed here is elementary. Let $\tau_j$ count ordered products of $j$ positive integers. For a fixed integer $j\ge2$, any interval of length $H$, intersected with $[1,C_0Y]$ for fixed $C_0$, has

$$
   \sum_{m\ {\rm in\ interval}}\tau_j(m)
              \ll_j H(1+G)^{j-1}
                     +Y^{1-1/j}(1+G)^{j-2}.                       \tag{6}
$$

For each ordered product choose one maximal component and sum over the other $j-1$ factors. Their product $s$ is at most $(C_0Y)^{1-1/j}$. The last factor has at most $H/s+1$ choices, giving (6) by harmonic sums and the elementary count of ordered products. If the target residue class modulo $d$ is a unit, the same argument gives $H/d$ in place of $H$ in the first term: all possible $s$ are coprime to $d$, and the last factor satisfies one residue class modulo $d$. The floor term is unchanged. These counts are valid with arbitrary half-open or closed endpoint conventions, by the same floor bound.

For $n\ne0$ the actual right sequence in the exact R88 transfer is bounded by $G^C\tau(|n|)\tau_4(N-n)$ on its support $|n|\ll Y$, $N-n\in[N/3,2N]$, using the actual Ramanujan cutoff bound. At $n=0$ the true $\chi(0)=0$ removes the sequence value. By (6), $\tau^2\le\tau_4$, $\tau_4^2\le\tau_{16}$, and Cauchy–Schwarz on the two shifted arguments, the sum of the absolute right weights on any interval of length $H\ge\Delta^{-1}$ is $O(HG^C)$ uniformly in its center. Indeed $\Delta^{-1}=Y/(2Q_0)=Y^{1-o(1)}$ dominates the floor term of (6) for every fixed index. For the negative part of $n$ apply (6) to $|n|$ on its reflected interval. The elementary divisor inequalities follow prime by prime by sending two ordered exponent-compositions to a table of their joint marginals.

For each shift $u$ in (5), use the central interval $|n-u|\le\Delta^{-1}$, then dyadic shells of lengths comparable to $2^k/\Delta$ on the actual support. Each shell costs at most $O(\Delta^{-1}G^C)$ after the factor $2^{-k}$ from the step error, and there are $O(1+G)$ shells. Integrating against $|d\mu|$ gives $O(Y^{\beta-1}\Delta^{-1}G^C)$. The discrepancy (4) costs only $Y^{\beta-1+o(1)}$ after the pointwise divisor bound on the actual finite support. This is negligible since $Q_0=Y^{o(1)}$. Include the factor $r/\varphi(r)\le G^C$ in the original correction and substitute $\Delta=2Q_0/Y$. This proves (1) on the true integers, with no new smoothing of the weight or change to the frequency band.

## 2. The genuine rare class and the two-pole error

Apply the [long unsigned deletion](r91-spectral-exceptional-long-unsigned-deletion.md) to the literal hard correction. Its square-label tail at $b_0>Y^{1/30}$ costs $O(Y^{\beta-1/30+o(1)})$. For all terms with a complete affine period of mean zero, its incomplete-period and BV argument costs $O(Y^{\beta-1/10+1/30+o(1)})$. We use both of these bounds unchanged. In the remaining terms the other three factors have product $h$, the positive variable is a multiple of $s=[a_0,b_0^2]$, and every odd conductor prime divides $hs$. Therefore $r_{\rm odd}$ divides the actual product $m$ on each surviving expansion term, even before squarefreeness is restored. These terms retain the literal factor $\chi(N-m)$. If a prime divides $(N,r_{\rm odd})$, that factor is zero on **every** such term. This exact vanishing does not rely on a density estimate or on extending a true cutoff.

For general targets we can also sharpen the absolute bound on the rare class. Take $d=r_{\rm odd}$ and assume $(N,d)=1$. The positive weighted estimate immediately before the final Cauchy step of R91 (4) bounds this cluster by

$$
          Y^{\beta-1}G^C
       \sum_{\substack{n\in I\cap\mathbb Z\\n\equiv N\ ({\rm mod}\ d)}}
                   \tau(n)^2\,\tau(N-n)^5 .                         \tag{7}
$$

Here $m=N-n>0$ and both sides are of size at most a constant times $Y$. For $\sum\tau(n)^4$ over this progression use $\tau^4\le\tau_{16}$ and the unit-residue version of (6). The floor $Y^{1-1/16}G^{O(1)}$ is absorbed into $(Y/d)G^C$, since $d\le Q_0=Y^{o(1)}$. The sum of $\tau(N-n)^{10}$ over the same progression is at most

$$
   \tau(d)^{10}\sum_{k\ll Y/d}\tau(k)^{10}
                    \ll \tau(d)^{10}(Y/d)G^C ,
$$

because $N-n=dk$ and $\tau(dk)\le\tau(d)\tau(k)$. Cauchy–Schwarz inside the actual progression now bounds (7) by $O(Y^\beta G^C\tau(d)^5/d)$. This estimate is only needed without odd overlap; with overlap the cluster was exactly zero before taking the absolute bound.

The remaining two-pole steps of the all-target proof leave their own fixed-power or stretched-exponential errors unchanged. In particular its short-truncated mutual-coprimality tail is $O(Y^{\beta-1/100+o(1)})$, the two genuine masked long-pole estimates cost $Y^\beta G^{O(1)}Q_0^{O(1)}e^{-c\sqrt G}$, and its subsequent positive tail extensions have fixed power savings. All are smaller than $Y^\beta G^C Q_0^{-1}$ because $\log Q_0=o(\sqrt G)$. One can therefore replace exactly the two inherited hard-transfer and unsigned-deletion errors in that proof by (1) and the estimates just proved. The same finite algebraic expressions and exact conductor contraction $\gamma_N$ are left intact, giving (2).

## 3. Divide by the genuine response only after using the exact zero

Under the pointwise assumptions, the exact algebraic completion and lower bound of R101 (5)–(7) apply to the actual cut $N-x\in I$. Neither calculation used the size of the missing odd product: that old condition was used only to absorb the error in its all-target arithmetic formula. In particular the completed color-one physical integral is $\gg Y^{2\beta-1}\Sigma^{(r)}(N)/[G(\log r)^4]$ with the outside sign $-\chi(-1)$, and every algebraic completion error is multiplied by $\gamma_N$ when inserted in (2).

If $\gamma_N\ne0$, its actual magnitude is $1/\varphi(r_{\rm odd}/(r_{\rm odd},N))\ge1/r$, by the primitive real local factors, including the nonzero normalized $2$-part of modulus one. Under $(N,r_{\rm odd})>1$ the second raw error of (2) is absent. Hence the raw error divided by $|\gamma_N|$ is $O(Y^\beta G^C r/Q_0)$, which is $O_A(Y^\beta G^{-A})$ for every fixed $A$ under the unchanged denominator margin. The same is true of the algebraic completion error after division. By the zero closeness, $\log r\ll\sqrt G$, and the absolute lower bound on the singular factor at even targets, these relative errors are smaller than half the physical lower for sufficiently large fixed $A$. Subtracting the actual parities cancels color zero, keeps the exact sign $-\chi(-1)\gamma_N$, and proves (3). No sign claim is made when the exact response vanishes or under the error in (2) without the stated overlap.
