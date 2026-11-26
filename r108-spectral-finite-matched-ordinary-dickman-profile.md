# The finite ordinary Dickman profile of missing conductor primes

**Scope.** This evaluates the ordinary finite cap in the genuine odd-conductor matched parity mean at positive primorial scale, without taking the real cutoff parameter large enough to approximate the cap by its full mass. A bounded set of missing conductor primes produces an explicit signed sum of translated Dickman correlations. A separated set of prime logs can make the regular term negative. The conditional sign statement for the genuine mixed-strip sums applies where this ordinary sign reinforces the exceptional correction. This is not a pointwise conclusion, full signed-shell control, a prime-pair result, Weak S, or existence of any Page zero. No Dirichlet GRH or external zero-gap assertion is used.

Use the exact genuine correlation and original moving-major setting of [the odd-conductor matched means](r104-spectral-genuine-odd-conductor-large-missing-mean.md). Put $G=\log Y$, $g=\log G$, $Z=\sqrt G/\log G$, and let $Y\le N\le2Y$ be even. Suppose the actual primitive real Page character $\chi$ has odd squarefree conductor $r$ with simple zero $\beta>1-4a_0/\sqrt G$. Take the genuine complete family $K=K_z=\prod_{p\le z}p$ and write

$$
 D=r/(r,K),\qquad M=[K,r]=KD\le e^{2Z},\qquad
 H=1/\varphi(D),\qquad \gamma(N)=c_r(N)/\varphi(r).
 \tag{1}
$$

The normalized mean $\langle\cdot\rangle_K$ is $(K/Y)\sum_{Y\le N\le2Y,\ K\mid N}\eta(N/Y)(\cdot)$, with all actual targets included. Keep the fixed, nonnegative bounded-BV tests $w,\eta$ of positive integrals on the same common scaled left interval $I_N=NJ$, $J\subset(1/2,9/16]$ real half-open, with left weight $w(u/N)$. Let $X_\pm=S_\pm$ or $X_\pm=S_\pm^{\rm maj}$ denote the genuine full mixed strip or its **original** moving polynomial-major integral, with the same true squarefree parity selectors and genuine fixed admissible $B>B_0>0$. No largeness condition relating $B$ to the missing primes will be used.

For fixed $\vartheta_*>0$, $J_1>0$ and $m_0\ge0$, assume
$z\le Z$, $\vartheta_*g\le\ell:=\log z$, $D\le G^{J_1}$ and $m:=\omega(D)\le m_0$. Thus $\ell/g\le1/2$ eventually and $z\ge A_0g$ for any fixed $A_0$ eventually. Use $\mathcal R>0$ from [the ordinary response formula](r105-spectral-small-missing-odd-conductor-parity-mean.md), or explicitly

$$
 \mathcal R=\frac{K}{\varphi(K)}H^2\mathcal W,\qquad
 \mathcal W=\frac1Y\int_Y^{2Y}\eta(v/Y)v
                  \int_J\frac{w(s)}{\log(v(1-s))}\,ds\,dv .
 \tag{2}
$$

This uses the same tests as $X_\pm$. Write $P_1(M)$ for the completed exceptional color-one cap of [the matched exceptional mean](r100-spectral-matched-ramanujan-exceptional-mean.md), before the sign and parity half, with its true finite physical endpoints.

Extend the ordinary Dickman function $\rho$ by zero on the negative axis, and take its usual cumulative normalization $\rho=1$ on $[0,1]$, $u\rho'(u)=-\rho(u-1)$ for $u>1$ away from integer breakpoints. Put $\kappa=\int_0^\infty\rho(u)\,du>0$ and $C_\rho(t)=\int_{\mathbb R}\rho(u)\rho(u+t)\,du$. For $t>0,\ a\in\mathbb R$ define

$$
 \mathcal H(t,a)=\int_{-t}^t C_\rho(v+a)\,dv-t C_\rho(t+a),
 \qquad
 \Phi(t;\lambda_1,\ldots,\lambda_m)=
    \frac1{\kappa^2}
     \sum_{\epsilon\in\{-1,0,1\}^m}
        (-1)^{\#\{i:\epsilon_i=0\}}
            \mathcal H\!\left(t,\sum_i\epsilon_i\lambda_i\right).
 \tag{3}
$$

For no missing primes the empty sum of shifts is zero and the single term has positive sign. Label the primes of $D$ in increasing order as $p_i$, and put $\lambda_i=\log p_i/\ell$ and $t_*=2Bg/\ell$.

**Theorem.** Uniformly in the allowed $z,D$ with the fixed declared parameters and tests, for either genuine choice of $X_\pm$ one has

$$
 \langle\gamma(X_+-X_-)\rangle_K
   =\mathcal R\,\Phi(t_*;\lambda_1,\ldots,\lambda_m)
                   -\chi(-1)H P_1(M)+o(\mathcal R).
 \tag{4}
$$

In particular if $\ell/g\to\vartheta>0$, $m$ is fixed, and the actual scaled prime logs converge to $\lambda_i^\infty$, the coefficient of $\mathcal R$ can be replaced by $\Phi(2B/\vartheta;\lambda_1^\infty,\ldots,\lambda_m^\infty)$ with the same type of error. No additional zero-closeness assumption is needed for (4).

For each fixed $t>0$ and fixed $m\ge1$ there is $L(t,m)>0$ such that if
$\left|\sum_i\epsilon_i\lambda_i\right|\ge L(t,m)$ for every nonzero $\epsilon\in\{-1,0,1\}^m$, the ordinary profile has sign $(-1)^m$ and its magnitude is bounded below by a positive constant depending on $t$. In particular it is negative for a single sufficiently far missing prime on this scaled log axis. Along the convergent sequences just described, with separated limit data, impose also $(1-\beta)G\le C_*\log G$ for fixed $C_*$ and $\chi(-1)=(-1)^{m+1}$. Then the two terms in (4) reinforce and the actual matched mean has sign $(-1)^m$ with magnitude $\gg\mathcal R+HP_1(M)$. For odd $m$ this includes the actual negative mean for an even character, without a separate Euler-tail dominance condition. These are sufficient hypotheses on the actual labels and the hypothetical Page zero, not an existence assertion about them. Other sign regimes are not inferred.

## 1. Global convergence for the actual premasked ordinary primitive

Use the exact premasked ordinary expansion of R105 Section 1. In the completely dormant slots outside $K$, the genuine base primitive is $F_z=R*\nu_K$, with $R(u)=\sum_{n\le e^u}\mu(n)/n$ for $u\ge0$ and zero below zero. The local weights of this base are the squarefree factors $-\alpha_p^\circ$ at all $p>z$, with $\alpha_p^\circ=(p-1)/(p^2-2)=1/p+O(p^{-2})$, and zero at $p\le z$. Put $f_z(v)=F_z(\ell v)$.

On every compact interval $0\le v\le A$, the comparison in [the reciprocal Dickman proof](r97-spectral-aligned-mean-dickman-lower.md), Section 1, applies directly to these all-minus weights. More explicitly, the cumulative mass of $\sum_{z<p\le z^A}\alpha_p^\circ\delta_{\log p/\ell}$ differs uniformly from that of $\mathbf1_{[1,A]}(u)\,du/u$ by $O_A(\ell^{-1}+z^{-1})$, from partial summation of the ordinary reciprocal prime estimate. For each fixed number of factors, convolution preserves this cumulative convergence by telescoping and bounded positive mass. Deleting repeated prime choices costs $O_A(\sum_{p>z}p^{-2})$, and surviving ordered tuples are divided by their factorial. There are at most $\lfloor A\rfloor$ factors, so the alternating sum gives the Dickman primitive exactly in the limit, uniformly on $[0,A]$. This is the finite simplex argument of R97, including discrete endpoints. Both scaled functions are zero below zero.

For global control use the positive $\nu_K$ and its $\theta=1/\ell$ moment $\|\nu_K\|_\theta\ll\ell$ from R105 (6). Splitting its shifts at $A\ell/2$ and using the ordinary reciprocal Möbius $L^1$ tail of [the finite ordinary bracket](r80-spectral-whole-mixed-parity-density.md), Section 2, gives

$$
  \int_A^\infty |f_z(v)|\,dv
     \ll e^{-c\sqrt{A\ell}}+e^{-A/2}\qquad(A\ge1),
 \tag{5}
$$

with fixed $c>0$ after reducing it for integration. Indeed before scaling the first term is bounded by $\|\nu_K\|_0\|R\mathbf1_{[A\ell/2,\infty)}\|_1$ and the second by $\|R\|_1\|\nu_K\|_\theta e^{-A/2}$; divide by $\ell$. Also the log-bin bound of [the local mass comparison](r107-spectral-ordinary-matched-local-mass-full-primorial-scale.md), (5), gives mass $O(1)$ on each real unit bin for $\nu_K$. The summable unit-bin suprema of $R$ from its ordinary decay imply $\|f_z\|_\infty\ll1$. This bounds the $L^2$ tail by the $L^1$ tail times a fixed constant. The compact convergence and (5) thus give $f_z\to\rho$ in $L^1$ and $L^2$. In particular $\kappa$ is finite and positive. Consequently $C_{f_z}\to C_\rho$ uniformly on the whole line by translation invariance and Cauchy--Schwarz; it also converges in $L^1$ by the convolution inequality.

The normalization need not use an independent formula for $\kappa$. Indeed $\int R=1$ as in R80, and the exact total mass of $\nu_K$ is
$(K/\varphi(K))\prod_{p>z}(1-\alpha_p^\circ)/(1-1/p)$.
The latter product is $1+O(z^{-1})$ since the local deviation is $O(p^{-2})$. Therefore the just-proved $L^1$ convergence gives

$$
                         \frac{K}{\ell\varphi(K)}\ \longrightarrow\ \kappa .
 \tag{6}
$$

## 2. The three leading occupations at a forced prime

The ordinary parity difference $\mathcal B_+-\mathcal B_-$ has the physical factor $\Sigma(N)P_N$ and the true finite correlation combination $\int_{-T}^T C_N(t)\,dt-TC_N(T)$, with $T=2B\log\log v+\log(1-s)$ at $v=N,\ s=u/v\in J$. This is the same signed coefficient of the R80 bracket as used in R105. In the premasked expansion the common scalar factor is
$B_K=\Sigma(K)P_K=(\varphi(K)/K)\prod_{p>z}(1-2/p^2)$.
The remaining scalar occupancy at $p>z$ has coefficient
$\delta(p)=(1-1/p)/(1-2/p^2)-1=-1/p+O(p^{-2})$.
Each primitive slot has its positive shifts $\rho_{d_i}$, where $\rho_p=\sum_{k\ge1}(\alpha_p^\circ)^k\delta_{k\log p}$. The $j$ weight is $\mu(j)\alpha^\circ(j)^2$, with the exclusion indicator expanded by $d_0\mid j$. The only remaining target condition is $d=[k,d_0,d_1,d_2]\mid N$, with all primes of $d$ outside $K$ and $k$ the scalar occupancy label.

Use the true BV target sampling of R104 (4) on each tuple with $d\le2Y$. Only $D\mid d$ survives in the continuum under the matched filter, with density exactly $1/d$ after normalizing by $K/Y$. The discrepancy summed before imposing density is $O(KG^C2^{\omega(D)})=Y^{o(1)}$, by the identical premasked BV and absolute weights of R105 Section 1. It is $o(\mathcal R)$ since $D\le G^{J_1}$ and the tests are fixed positive. In particular we keep all moving endpoints through this ordinary averaging.

For the continuum approximation, if the two fixed shifted primitives are $F_i=R*\lambda_i$, R107 (5) gives $\|F_i\|_\infty\ll\|\lambda_i\|_0/\ell$ by summing the unit-bin suprema of $R$. Also $\|F_i\|_1\ll\|\lambda_i\|_0$. Hence for every such pair the linear correlation cap functional has absolute value at most

$$
 \left|\int_{-T}^T C_{F_1,F_2}(t)\,dt
                         -T C_{F_1,F_2}(T)\right|
       \ll (1+T/\ell)\|\lambda_1\|_0\|\lambda_2\|_0 .
 \tag{7}
$$

Here $T/\ell=O_{B,\vartheta_*}(1)$, and the same bound holds if any factor outside the fixed smooth reciprocal factor $S_z$ in a slot is replaced by a positive submeasure. The physical integration is $\ll\mathcal W$ times the bound, since the tests are nonnegative. This estimate is what permits comparing the strength of individual occupancy terms to the true continuum scale.

At a prime $p>z$ write $a_p=\alpha_p^\circ=1/p+O(p^{-2})$. At $p\notin D$ any non-dormant choice costs $O(p^{-2})$ in absolute mass after density: $j$ alone has $a_p^2(1-a_p)^{-2}=O(p^{-2})$ for its two slot masses, and if $p$ appears in $d$ at least one of the occupancy masses costs $O(p^{-1})$, with its extra density $1/p$. Thus the sum over all choices there is $1+O(p^{-2})$ with dormant term one. At a forced $p\mid D$, the three leading choices are exactly:

1. $p$ enters $k$ alone, with scalar weight $\delta(p)/p=-1/p^2+O(p^{-3})$ and no shift.
2. $p$ enters $d_1$ alone at its first geometric shift, of weight $a_p/p=1/p^2+O(p^{-3})$ and shift $\log p$ in slot one.
3. $p$ enters $d_2$ alone at its first geometric shift, of the same weight and shift in slot two.

In each of these choices $p\nmid j$. All remaining forced local choices have absolute mass $O(p^{-3})$ after density: two simultaneous occupations each bring a reciprocal cost, an occupation through $d_0$ forces the $O(p^{-2})$ mass from $j$, and the higher powers of a shift start at $a_p^2$. A choice with $p\mid j$ and a separate occupation is bounded the same way. These estimates are absolute on product measures, so dropping inter-label coprimality for the bounds is valid. The leading terms themselves obey all the original coprimality conditions.

To sum the error, the total non-dormant mass from any unforced prime is $O(z^{-1})$ relative to the positive product of all forced bounds $C^m/D^2$, since $\sum_{p>z}p^{-2}\ll z^{-1}$. At forced primes the excluded choices, or approximation of each of the three scalar weights by its signed $p^{-2}$ value above, cost $O_{m_0}(z^{-1})D^{-2}$ altogether, by telescoping the finite products and using $p>z$. Every retained leading tuple has $d=D\le2Y$ and $j=1$, so no artificial tail outside the true $d$ bound affects it; dropping that bound in the absolute error product only enlarges the bound. Restore the two base masses $\|\nu_K\|_0^2\asymp\ell^2$ and $B_K\asymp\ell^{-1}$. By (7) the resulting continuum error is $O_{B,\vartheta_*,m_0}(\mathcal W\ell D^{-2}z^{-1})=o(\mathcal R)$.

## 3. Pass the actual finite cap to the Dickman profile

In a leading tuple, the shifts in slot one and slot two are sums of the corresponding $\log p_i$. If their difference is $a$, then the exact cross-correlation equals $C_{F_z}(t+a)$. Changing variables to the scale $\ell$ gives an $\ell^2$ factor multiplying
$\int_{-T/\ell}^{T/\ell} C_{f_z}(v+a/\ell)\,dv-(T/\ell)C_{f_z}(T/\ell+a/\ell)$.
The sign is $(-1)^{\#\{i:\epsilon_i=0\}}$ when $\epsilon_i$ records the scalar choice or one of the two shift slots above, and $a/\ell=\sum_i\epsilon_i\lambda_i$. On the whole real support $T/\ell=t_*+O(1/\ell)$. The rescaled endpoints and shifts are bounded in terms of the declared parameters, since $\ell\ge\vartheta_*g$, $\log D\le J_1g$, and $m\le m_0$. Uniform correlation convergence and continuity of $C_\rho$ therefore give the exact finite expression $\mathcal H(t_*,\sum_i\epsilon_i\lambda_i)+o(1)$, uniformly in all such tuples and physical points. We have not extended the finite cap to its full integral.

The common continuum prefactor of the leading expression is
$\mathcal W B_K\ell^2/D^2$. Relative to $\mathcal R$ it tends to $\kappa^{-2}$, since $B_K=(\varphi(K)/K)(1+O(z^{-1}))$, $\varphi(D)/D\to1$ uniformly for the bounded number of primes $p_i>z$, and (6) holds. Adding the estimates from Sections 1--2 proves that the true ordinary term is $\mathcal R\Phi+o(\mathcal R)$. Now use R104 Section 3 with its ordinary mean retained. The genuine arc transfers and R100 exceptional comparison there give the actual exceptional term $-\chi(-1)HP_1(M)$ after taking the parity difference, with all other errors $O_A(HYG^{-A})$. This is $o(\mathcal R)$ for a sufficiently large fixed $A$ because $D\le G^{J_1}$. This proves (4) for both genuine arc choices. The limits with converging scaled labels follow from the continuous kernel in (3).

Finally, for $t>0$ the centered $\mathcal H(t,0)=2\int_0^t C_\rho(v)dv-t C_\rho(t)$ is positive. In fact $\rho$ is positive and nonincreasing on $[0,\infty)$ by its delay equation and the standard positivity check of R97; hence $C_\rho$ is positive and nonincreasing for $t\ge0$, and $\mathcal H(t,0)\ge t C_\rho(t)>0$. Also $\mathcal H(t,a)\to0$ as $|a|\to\infty$ for fixed $t$, because the $L^2$ autocorrelation vanishes at infinity and is continuous. Choose $L(t,m)$ so the supremum of $|\mathcal H(t,a)|$ for $|a|\ge L(t,m)$ is less than $\mathcal H(t,0)/(2(3^m-1))$. The sum of the noncentral terms in (3) then has absolute value less than half the centered value, leaving the stated sign $(-1)^m$ and a lower bound for its magnitude. Under the additional closeness condition R100 gives $P_1(M)>0$. For the indicated character parity its sign in (4) agrees with the ordinary limit, so the $o(\mathcal R)$ error preserves that combined sign. This uses the exact separated limits and does not give pointwise or full-shell control.
