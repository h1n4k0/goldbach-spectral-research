# Log-bin mass controls the ordinary matched mean at the full primorial scale

**Scope.** For the genuine odd-conductor matched parity mean, this removes the narrow upper condition on the primorial scale in the ordinary-cap comparison, at the cost of a sufficiently large **fixed** cutoff parameter. At the top primorial scale the conclusion is a small fixed relative error, not an asymptotic with vanishing relative error. In the subrange $\log z=o(\log\log Y)$ the same estimate does give a vanishing relative error. The genuine full and original moving-major mixed-strip means still have their own exceptional term. Sign implications below are conditional on the stated hypothetical character and zero conditions and do not settle pointwise control, the full signed shell, prime pairs, Weak S, or Page-zero existence. No Dirichlet GRH or external zero-gap assertion is used.

Use the setting of [the small-missing matched parity calculation](r105-spectral-small-missing-odd-conductor-parity-mean.md). Put $G=\log Y$, $g=\log G$, $Z=\sqrt G/\log G$, $Y\le N\le2Y$ even. The actual Page character $\chi$, if under consideration, is primitive real with **odd** squarefree conductor $r$ and a simple zero $\beta>1-4a_0/\sqrt G$. Write $b=1-\beta$. Let $K=K_z=\prod_{p\le z}p$, $D=r/(r,K)$, $M=KD=[K,r]\le e^{2Z}$, $\ell=\log z$, $H=1/\varphi(D)$ and $\gamma(N)=c_r(N)/\varphi(r)$. For fixed $J_1>0$ and fixed $m_0$ retain $D\le G^{J_1}$ and $\omega(D)\le m_0$. Retain $A_0g\le z\le Z$, with $A_0$ sufficiently large as in the inherited exceptional-cap lower bound when that lower bound is used. In particular $\ell\le g/2$ for large $Y$, but we do **not** assume $\ell\le g/(\log g)^2$.

The genuine fixed admissible $B>B_0>0$ determine the same cuts as in R105 (larger fixed $B$ will be allowed). The common half-open scaled left interval $I_N=NJ$, $J\subset(1/2,9/16]$, the left weight $w(u/N)$ and dyad weight $\eta(N/Y)$ are unchanged. The weights are fixed, nonnegative, bounded-BV and have positive integrals; put $\mathfrak w=(\int_Jw)(\int_1^2\eta)$. The normalized mean $\langle\cdot\rangle_K$ is the original $(K/Y)\sum_{Y\le N\le2Y,\ K\mid N}\eta(N/Y)(\cdot)$ on all true sampled targets. For either actual full or original moving-major choice $X_\pm$ define $\mathcal R$ as in R105:

$$
 \mathcal R=\frac{K}{\varphi(K)} H^2\,\mathcal W,\qquad
 \mathcal W=\frac1Y\int_Y^{2Y}\eta(v/Y)v
                 \int_J\frac{w(s)}{\log(v(1-s))}\,ds\,dv .
 \tag{1}
$$

It is positive and satisfies $\mathcal R\asymp \mathfrak w(Y/G)\ell H^2$. Write $P_1(M)$ for the genuine exceptional completed color-one integral, with its original cutoffs and without the exceptional parity sign or half, as in [the matched cap proof](r100-spectral-matched-ramanujan-exceptional-mean.md).

**Theorem.** There are absolute $C,c>0$ such that, for any fixed $B>2J_1+1$ that is admissible with $B_0$, the ordinary cap in the matched mean satisfies

$$
 \left|\langle\gamma(\mathcal B_+-\mathcal B_-)\rangle_K
                                  -\mathcal R\right|
 \ \ll\ C^{\omega(D)}\mathcal R
  \left\{(1+Bg)e^{-c\sqrt{Bg}}+
           (1+Bg/\ell)
                  \exp\!\left(-\frac{(B/2-J_1)g-O(1)}{\ell}\right)
  \right\}+o(\mathcal R).
 \tag{2}
$$

Here $\mathcal B_\pm$ are the true regular brackets, the bounded $O(1)$ in the exponent is absolute for large enough $Y$ relative to fixed $B$, and the implied coefficient on the displayed two terms can be chosen absolute. The $o(\mathcal R)$ can depend on the declared fixed parameters and weights and is uniform over the allowed $z,D$.

In particular if $\ell/g\to0$ the right side is $o(\mathcal R)$ for fixed $B>2J_1+1$. On the whole range $A_0g\le z\le Z$, given fixed $0<\varepsilon<1/4$, one can instead take $B$ sufficiently large and fixed, depending on $J_1,m_0,\varepsilon$, to obtain for either genuine $X$,

$$
       \langle\gamma(X_+-X_-)\rangle_K
          =\mathcal R-\chi(-1) HP_1(M)+E,\qquad
            |E|\le \varepsilon\mathcal R+o(\mathcal R).
 \tag{3}
$$

No closer zero assumption is needed for (2)--(3). To infer a sign, suppose in addition $bG\le C_*\log G$ with fixed $C_*$. If $\chi(-1)=-1$, then (3) gives a positive matched mean, $\gg\mathcal R+HP_1(M)$, on the entire stated range. If $\chi(-1)=1$, take the fixed gap $B-B_0$ sufficiently large as well. Then the sufficient criterion of [the competing Euler-tail bound](r106-spectral-competing-odd-mean-euler-tail-dominance.md) applies here with $y=G^{3/4}>z$: $De^{-2bG}\ge C_{\rm dom}\mathcal F_\chi(y)^2$ for sufficiently large fixed $C_{\rm dom}$ implies a negative matched mean, of magnitude at least $\tfrac12 HP_1(M)$. No sign is asserted in the competing case without a dominance condition. Here and throughout, statements for sufficiently large dyads inherit the possible ineffectivity of the Page conductor bound.

## 1. A unit log-bin bound for each genuine primitive shift measure

Use the exact premasked expansion from R105 Section 1, with all primes of $K$ occupied before expanding the remaining arithmetic constraints. Recall its positive base measure $\nu_K$ on the log variable: at $p\mid K$ the local generating factor is $(1-X/p)^{-1}$, with $X$ denoting a shift by $\log p$, while at $p\nmid K$ it is the positive ratio $(1-\alpha_p^\circ X)/(1-X/p)$ for $\alpha_p^\circ=(p-1)/(p^2-2)$. In the two primitive slots the exact functions are $F_i=R*\lambda_i$ with $\lambda_i=\nu_{K,j}*\rho_{d_i}$, where $R(u)=\sum_{n\le e^u}\mu(n)/n$ for $u\ge0$, zero below zero. The two measures are nonnegative and supported on $[0,\infty)$, including their shifts from $j$ and the outer occupancy labels $d_i$. No signed coefficient is put inside them.

Factor out the same smooth reciprocal measure from each slot:

$$
        S_z=\sum_{\substack{a\ge1\\P^+(a)\le z}}\frac1a\,\delta_{\log a},
        \qquad \lambda_i=S_z*\kappa_i .
 \tag{4}
$$

The $a=1$ atom is included; $\kappa_i$ is the remaining finite positive measure. The full mass of $S_z$ is $\asymp\ell$ by the reciprocal prime bounds. On every real log interval $I$ of length at most one, $S_z(I)\ll1$: discard smoothness and bound the sum of $1/a$ on an interval of ratio at most $e$ (and include the possible $a=1$ atom). Convolution with $\kappa_i$ and the exact multiplicativity of total masses for positive measures now give

$$
          \sup_{|I|\le1}\lambda_i(I)
                    \ll\frac{\|\lambda_i\|_0}{\ell},
       \qquad \|\lambda_i\|_0=\lambda_i(\mathbb R).
 \tag{5}
$$

A zero measure causes no difficulty. This argument involves neither equidistribution of smooth logs nor an estimate for individual shifted prime residues.

Let $C_R(t)=\int R(u)R(u+t)\,du$. Its supremum and $L^1$ norm are finite, and $|C_R(t)|+\int_{|x|\ge |t|}|C_R(x)|\,dx\ll e^{-c_0\sqrt{|t|}}$ for $|t|\ge1$, as in R105, by the ordinary reciprocal Möbius tails; the constants are absolute. In particular $\sum_{n\in\mathbb Z}\sup_{[n,n+1]}|C_R|$ converges. Partition the argument of the shifted correlation into unit intervals, and use (5). Uniformly for every real $q$,

$$
       \int |C_R(q-s)|\,d\lambda_i(s)
                    \ll \frac{\|\lambda_i\|_0}{\ell}.
 \tag{6}
$$

The same estimate holds with $q+s$ or the reflected correlation. This is the needed comparison for the actual cap's endpoint term.

## 2. The finite correlation tail pays $T/\ell$, not $T$

Take a fixed genuine ordered tuple of R105 (5), with weights $\lambda_1,\lambda_2$ as above. For $T=2B\log\log v+\log(1-s)$ on the actual support, its cap replacement error is
$\int_{|t|>T} C_{F_1,F_2}(t)\,dt+TC_{F_1,F_2}(T)$.
The slot representation is the double integral of $C_R(t+s_1-s_2)$ against the two positive shift measures, justified by Fubini using the absolute correlation norm. On the part with $s_1+s_2\le T/2$, the correlation arguments at $T$ and outside the interval $[-T,T]$ have absolute value at least $T/2$. Both errors there are therefore bounded by
$O((1+T)e^{-c_1\sqrt T}\|\lambda_1\|_0\|\lambda_2\|_0)$.

For the remaining pairs, at least one shift is at least $T/4$. For the integrated tail use the global $L^1$ norm of $C_R$ for each fixed pair, and Markov on the measure of that large slot. For the endpoint term, if $s_1\ge T/4$, first fix $s_1$ and integrate $s_2$ using (6), allowing the entire second slot in this absolute bound. Then Markov in $s_1$ bounds its mass by $e^{-\theta T/4}\|\lambda_1\|_\theta$, where $\|\lambda\|_\theta=\int e^{\theta s}\,d\lambda(s)$ and $\theta=1/\ell$. The other ordering is identical with the roles of the two slot indices exchanged; (6) applies to both orientations of the shift. Since $\|\lambda_i\|_0\le\|\lambda_i\|_\theta$, the whole error of this tuple is bounded by

$$
 \ll (1+T)e^{-c_1\sqrt T}\|\lambda_1\|_0\|\lambda_2\|_0
       +(1+T/\ell)e^{-\theta T/4}
                       \|\lambda_1\|_\theta\|\lambda_2\|_\theta .
 \tag{7}
$$

In particular the boundary factor $T$ has gained the missing $1/\ell$ from an **unweighted** local bound on the other slot; no tilted local bound is required.

Now use the same actual sampling as R105. For a fixed tuple its genuine target condition is $d\mid N$ with $(d,K)=1$, and the exact mean in the odd Ramanujan channel forces $D\mid d$. Before imposing that condition the remaining discrete discrepancies are $O(KG^C2^{\omega(D)})=Y^{o(1)}$, by the original BV profiles and absolute sums in R105 Section 1; this applies to their finite-minus-complete difference in (7) as well. We do not bound the variation of the artificial split into large and small shifts. Apply the positive forced-density sum of R105 (7), with the scalar factor already premasked on $K$: for the moments of order 0 or $\theta$ it is $\ll C^{\omega(D)}\ell D^{-2+\theta}$ with $\theta=0$ or $1/\ell$ respectively. Its implied constants are absolute because the moment estimates depend only on the prime sums, and a prime that appears in multiple slots still incurs one density factor $1/p$.

On the physical support $T=2Bg+O(1)$ uniformly for large $Y$, and $\log D\le J_1g$. Insert (7) and the physical integration factors into this forced-density sum. The resulting continuum error is at most a constant times

$$
 C^{\omega(D)}\mathfrak w\frac{Y\ell}{GD^2}
 \left\{(1+Bg)e^{-c_2\sqrt{Bg}}+
      (1+Bg/\ell)\exp\!\left(-\frac{(B/2-J_1)g-O(1)}{\ell}\right)\right\}.
 \tag{8}
$$

In deriving the second exponential we used $D^\theta e^{-\theta T/4}$. Neither the cap geometry nor the literal density factors have been extended in this comparison. The prefactor $\mathfrak w Y\ell/(GD^2)$ is $O(\mathcal R)$ since $\varphi(D)\le D$ and the test is nonnegative on the physical support. The complete integral of the ordinary correlation yields exactly the singular-series mean $\mathcal R+o(\mathcal R)$ by R105 Section 3, including its small absolute BV sampling error and the Rankin tail from its continuum Euler factors. Those estimates use only $D\le G^{J_1}$ and the declared scales, not the narrower upper bound on $\ell$. The subpower discrepancy above is $o(\mathcal R)$ as well, since $\mathcal R\gg \mathfrak w Y\ell/(GD^2)$ and $D\le G^{J_1}$. This proves (2).

## 3. Fixed margins for the two actual mixed means

For fixed $B>2J_1+1$ and $\ell/g\to0$, the second bracketed term of (2) tends to zero because $g/\ell\to\infty$ and the coefficient $B/2-J_1$ is positive. At the full range $\ell\le g/2$, put $x=g/\ell\ge2$. If $B\ge4J_1+4$, then $B/2-J_1\ge B/4$, and the second term in (2) is at most an absolute constant times
$\sup_{x\ge2}(1+Bx)e^{-Bx/4}\le (1+2B)e^{-B/2}$,
for sufficiently large $B$. Here the absolute $O(1)/\ell$ error in the exponent is harmless since $\ell\to\infty$. Now $C^{\omega(D)}\le C^{m_0}$, so choosing large fixed $B$ makes this error as small a fraction of $\mathcal R$ as desired; the first bracketed term still vanishes. This does not give an $o(1)$ fraction at fixed $B$ along all $\ell\asymp g$.

Use [the genuine odd-conductor comparison](r104-spectral-genuine-odd-conductor-large-missing-mean.md), Section 3, keeping the ordinary matched mean instead of upper-bounding it. The actual auxiliary, common-complement and original moving-minor comparisons there have error $O_A(HYG^{-A})$ after the exact response, and on the parity difference the exceptional term is exactly $-\chi(-1)HP_1(M)$ up to that error. These comparisons did not use R105's narrow upper bound on $\ell$. Since $D\le G^{J_1}$, any fixed $A>J_1+2$ makes this error $o(\mathcal R)$ by (1); the tests are fixed and positive. This proves (3) for the genuine full correlation and, separately, for its original moving polynomial-major integral, with no sampled targets discarded.

Under $bG\le C_*\log G$, R100 supplies $P_1(M)>0$ with its lower bound in the stated $z$ range. If $\chi(-1)=-1$ it reinforces the positive ordinary term in (3). To check the competing case without importing an extra cutoff assumption, take $B-B_0$ larger than a sufficiently large absolute constant and set $y=G^{3/4}$. Then $y>z$ throughout this range. In R106 Sections 1--2 the real derivative comparison and small-prime product estimates require only $b\log r=o(1)$ and $\log y,\ell=o(\log r)$, which continue to follow from the same Page threshold, $r\le e^{2Z}$ and the Page conductor growth. The normalized log shift of the positive Euler factors up to $y$ is $O(\log y)=O(g)$ with an absolute constant, as in R106 (8). The large fixed gap gives $U_v=(B-B_0)\log\log v\ge\ell$ and makes that mean at most $U_v/2$. The identical finite Markov step thus gives the R106 bound for $P_1(M)$ with this $y$, once again without replacing the actual finite cap. The exact response ratio $HP_1(M)/\mathcal R\gg D e^{-2bG}/\mathcal F_\chi(y)^2$ follows as in R106 (11).

A sufficiently large fixed dominance constant makes $HP_1(M)\ge4\mathcal R$. Insert this into (3) with $\chi(-1)=1$ and $\varepsilon<1/4$; for large $Y$ the error is smaller than $\mathcal R$, yielding $-\langle\gamma(X_+-X_-)\rangle_K\ge\frac12 HP_1(M)$. Outside this comparison the expansion (3) still has a controlled ordinary term, but we do not infer the sign of the competition.
