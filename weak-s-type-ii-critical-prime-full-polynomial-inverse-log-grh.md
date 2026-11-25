# Inverse-logarithmic energy on the full genuine polynomial critical shell under global GRH

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and $e(z)=e^{2\pi i z}$. Use the exact setup of the [full-width critical-shell theorem with signed unit grouping](weak-s-type-ii-critical-prime-full-polynomial-narrow-derivative-unit-signs-grh.md): $J=[N-y,N/2)$ with $N/2\le y\le9N/16$, the actual hard cofactor interval $I_k$ has $k>t\ge N^{.49999}$, and the exact hard coefficient is

$$
 D_m=\mathbf1_{m\in J}
    \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\(dk,N)=1,\ (d,k)=1}}
                          \mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
$$

The hard interval $I_d\subset[X,\infty)$ is arbitrary. On this support it may be intersected with $[X,N/(2t))$ without losing any terms; no further width restriction is imposed. Keep all actual unit primes, the true prime polynomial $P$ and its permissible bounded selector, with the original hard product and prime cutoffs. Write $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
             \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}
             |D(a/q+\beta)|^2\,d\beta .
$$

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including $\zeta(s)$. Then uniformly on the full original admissible polynomial divisor interval and all actual target-dependent cutoffs,

$$
                       \mathcal E_N(D)\ll \frac{N L_2^4}{L}.
 \tag{1}
$$

The actual signed full shell, its separately centered numerator covariance and the exact parity-preserving signed even-lattice residual of length $M=\lceil XL^2\rceil$ are consequently $O(NL_2^2/\sqrt L)$. The determinant-zero and actual constant-mode improvements below are unconditional; the original nonzero integer determinant bound still uses global GRH. In particular (1) is not an unconditional shell estimate, does not concern other moduli or shells or individual compensated offset squares, and is not Hypothesis S.

## 1. Actual transfers at the smaller smoothing width

Use the true common physical cutoff $\Omega(m/N)$ and common absolute cofactor cutoff $w(k)=W(\log k)$, supported inward in the original intervals. Now take

$$
                           \delta=L^{-2}.
$$

The weights are $[0,1]$-valued, of bounded variation $O(1)$, and can be zero on a hard interval too short to contain a nontrivial inward mollification. As in [the common endpoint proof](weak-s-type-ii-critical-prime-cross-dyad-subpolynomial-grh.md#1-common-endpoint-transfer-before-splitting-into-dyads), the ordinary squared physical-edge error is $O(N\delta+N^{.99}+NL^3e^{-c\Phi})=O(NL^{-2})$, with $\Phi=L^{3/5}(\log L)^{-1/5}$. That argument uses the true free signed short label at scale $N/(guz)$, with its uniform ordinary Mertens input for polynomial arguments, and does not depend on $\delta$ beyond the interval length $O(N\delta)$ of the continuous term.

Either cofactor endpoint still meets only $O(1)$ original divisor dyads, from $m\in[7N/16,N/2)$. For a divisor dyad write $A_i=\lambda_i X$, $K_i=X/\lambda_i$, with $\lambda_i\le N^{1/100000}$. The [actual narrow cofactor edge bound](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#1-literal-endpoint-and-arithmetic-transfers-on-the-polynomial-dyad) at this width uses its unchanged signed continuous form $O_B(\delta+K_i^{-1}+\delta^2L_2^3+L^{-B})$, with $B>2$. For the actual small-gcd counts take $G=\lfloor L^4\rfloor$. The upper bound there is

$$
 N\delta^2(1+\log(2G))+\delta A_iG+\lambda_i^2G^2,
$$

and the larger-gcd floor is $O(K_i^2/G)$. Each term is $O(N\delta)$ because $\lambda_i\le N^{1/100000}$. The hard-prefix BV transfer is unchanged. This verifies the extension of both genuine smoothing costs to $\delta=L^{-2}$ and yields ordinary squared error $O(NL^{-2})$ on the **whole** original interval.

Keep the same exact long unit $(d,N)=1$, squarefree cutoff $l\le T=L^{16}$ with $(l,N)=1$, and short inclusion cutoff $h\mid\operatorname{rad}N$, $h\le H_0=\exp(C_0L_2^2)$ where the fixed constant $C_0$ is sufficiently large. Their precise smoothed coefficients are as in [the full polynomial proof, §1](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#1-keep-the-genuine-common-smoothing-and-the-original-units); their ordinary squared approximation error $O(NL^{-8})$ and approximate norm $O(\sqrt N)$ are unchanged because the forced-divisibility estimates use only bounded sup norm and variation for the short and physical weights. The auxiliary bump in the normalized short variable on each dyad equals one on the actual $\Omega$ support. The exact split retains $s=(l,d)\mid l$, $d=su$, $(u,lN)=1$, $k$ a multiple of $l^2h/s$.

The [full polynomial determinant construction](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#2-integrate-in-the-complete-square-and-dispatch-its-off-diagonal) still cuts $|\tau|\le L^4$ and $0<|j|\le\lambda_iN^{1/1000}$ in the actual sampled vector. For the high $\tau$ tail the derivatives of $G_\beta(v)=\Omega(e^v)e(\beta Ne^v)$ give
$|\widehat G_\beta(\tau)|\ll_r\delta^{1-r}|\tau|^{-r}=O_r(L^{2r-2}|\tau|^{-r})$. With $|\tau|>L^4$, choose fixed enough $r$ to give any needed inverse-log saving against the full ordinary sampled norm, or the corresponding bound with a fixed polynomial in $(1+|\tau|)$ in the analytical exact rational norm. For the dual tail the usual mesh is $\gg(\lambda_i T^2H_0)^{-1}$ and all cutoff derivatives cost fixed powers of $L$ at retained $\tau$, so the power cutoff in $j$ still beats all logarithmic losses. The exact-rational-only restoration of $j,\tau$ in [§3 of that proof](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#3-restore-the-exact-physical-integral-on-the-rational-diagonal-only) uses $Y_\tau=1+\delta^{-1/2}+|\tau|$ in its norm and high-sample bounds; changing $\delta^{-1/2}$ here to $L$ preserves those savings. Finally $\|\widehat G_\beta\|_1=O(L_2)$ remains true. Consequently the original global-GRH nonzero-determinant estimate stays $O(N^{1.91})$ per pair of dyads before the two $\tau$ integrals, and all such contributions and the two restorations are harmless after the final label and shell sums. No larger modular label set is introduced below.

## 2. A direct signed reciprocal norm at polynomial scale

We need the following uniform extension of the [sharp masked signed lcm argument](weak-s-type-ii-critical-prime-unconditional-all-targets.md#1-the-signed-lcm-form-with-the-full-unit-mask). Let $0<\alpha<\gamma$ and $C>0$ be fixed, let $I$ be any real hard interval in $[N^\alpha,N^\gamma]$, and let $B_0\le N^C$ be a positive integer. Put $V(B_0)=\varphi(B_0)/B_0$. Then

$$
 \sum_{c\ge1}\frac1c
       \left|\sum_{\substack{cv\in I\\(cv,B_0)=1}}\frac{\mu(cv)}v\right|^2
                   \ll_{\alpha,\gamma,C}\frac1{V(B_0)}.
 \tag{2}
$$

All integer variables in the sums are positive. The weight here is directly $1/c$, without comparing it to $\varphi(c)/c^2$ with an additional log factor.

Write $Z=\exp(C_1L_2^2)$ with sufficiently large fixed $C_1$, and $K=N^\alpha/Z$. Nonzero terms have squarefree $c$ and $(c,B_0)=1$. If $c<K$, factoring $\mu(c)$ leaves the signed reciprocal prefix difference in $v$ with true coprimality mask $cB_0$, at both endpoints $\gg Z$. It is $O_A(L^{-A})$ for, say, fixed $A=10$ upon choosing $C_1$ large enough, by the same coprime reciprocal Mertens proof as in the cited argument: convolve with reciprocal weights of the mask-smooth integers, split at the square root of the endpoint, and use reciprocal Rankin exponent $1/L_2$ on the tail. The Euler costs there remain $O(L_2)$ and $L_2^{O(1)}$ for every fixed polynomial mask bound, by splitting its primes at $L^2$. Thus $c<K$ is negligible after summing the harmonic $c$ weights.

For $c\ge K$ first remove only the **inner** extra $B_0$ exclusion by exact Dirichlet convolution. The identity for $\mu(v)\mathbf1_{(v,B_0)=1}$ is the convolution of $\mu$ with the indicator of integers all of whose prime factors divide $B_0$. Since the retained $c$ is coprime to $B_0$, this preserves the mask $(v,c)=1$ after rescaling. Minkowski thus gives a norm cost $\sum_{r\ B_0\text{-smooth}}1/r=1/V(B_0)$. It remains to show, for every resulting interval $I'=I/r$,

$$
 \sum_{\substack{c\ge K\\(c,B_0)=1}}\frac{\mathscr C(c)}c
       \left|\sum_{\substack{cv\in I'\\(v,c)=1}}\frac{\mu(v)}v\right|^2
                         \ll V(B_0),\qquad \mathscr C(c)=\mu^2(c).
 \tag{3}
$$

The upper bound for $v$ is still at most $N^\gamma$. For each fixed $v,v'$ the $c$ conditions are the single actual interval $I'/v\cap I'/v'\cap[K,\infty)$, and the coprimality mask is $B_0vv'$. We compare its harmonic count for $\mathscr C(c)/c$ to one with $\mathscr B(c)/c$, where $\mathscr B(c)=\mu^2(c)\varphi(c)/c$ is the original DIT weight in gcd coordinates.

Here are the needed complete local factors and the error. Both multiplicative functions restricted by a polynomial-size coprime mask $Q$ are $1*g_Q$; at allowed primes the local $g$ coefficients are $0,-1$ at $p,p^2$ for $\mathscr C$, and $-1/p,-(1-1/p)$ at $p,p^2$ for $\mathscr B$, with higher coefficients zero in both. At a forbidden prime the value at $p$ is $-1$ and higher are zero. Thus $\sum_d |g_Q(d)|/d^{3/4}=N^{o(1)}$, by absolute convergence of the allowed part and splitting masked primes at $L^2$. The resulting count is density times the endpoint plus $O(x^{3/4}N^{o(1)})$ at endpoint $x$, by the elementary count of multiples. Abel gives for a hard interval in $[K,\infty)$ the harmonic integral times that density plus $O(N^{-\alpha/4+o(1)})$. This error also bounds isolated included endpoints, uniformly in all masks in use.

Let $d_{\mathscr C}(Q),d_{\mathscr B}(Q)$ denote the two densities. At an allowed prime their respective local factors are $(1-1/p)(1+1/p)$ and $(1-1/p)(1+1/p-1/p^2)$; at an excluded prime each factor is $1-1/p$. Thus, with $a_p=1/p-1/p^2$,

$$
 \frac{d_{\mathscr C}(B_0vv')}{d_{\mathscr B}(vv')} =
 K_{B_0}\prod_{p\mid(B_0,vv')}(1+a_p)
        \prod_{\substack{p\mid vv'\\p\nmid B_0}}
              \left(1-\frac{1}{p^2(1+1/p)}\right),
 \qquad K_{B_0}=\frac{d_{\mathscr C}(B_0)}{d_{\mathscr B}(1)}
                     \asymp V(B_0).
 \tag{4}
$$

The last comparison uses $\prod_{p\mid B_0}(1+1/p)^{-1}\asymp V(B_0)$ by an absolutely convergent product.

First transfer the actual harmonic $\mathscr C$ sum in (3) to the corresponding integral on the exact interval. Write the correcting product in (4) as $\prod_{p\mid vv'}(1+\eta_p)$, with $\eta_p=a_p$ for $p\mid B_0$ and $\eta_p=-1/(p^2(1+1/p))$ otherwise. Expand each indicator $\mathbf1_{p\mid vv'}$ as $\mathbf1_{p\mid v}+\mathbf1_{p\mid v'}-\mathbf1_{p\mid v}\mathbf1_{p\mid v'}$. Each resulting term imposes two squarefree divisibilities $d_1\mid v,d_2\mid v'$ with its signed coefficient. For each term transfer back from the same harmonic integral with density $d_{\mathscr B}(vv')$ to the discrete $\mathscr B(c)/c$ sum with mask $(c,vv')=1$. The aggregate errors are negligible: the signed $v,v'$ terms have the absolute reciprocal weights $1/(vv')$, with total $\ll L^2$, and the sum of absolute allocation coefficients is at most
$\prod_p(1+3|\eta_p|)\ll L_2^3$ (only finitely many primes in $vv'$ occur, the unrestricted product outside $B_0$ converges). Thus these comparisons cost $O(N^{-\alpha/4+o(1)})$ after all labels, not a polynomial-size count of $v,v'$.

A transferred discrete term is a scalar product in the positive $\mathscr B(c)/c$ norm over $c\ge K$. For the factor with $d_i\mid v$, substitute $v=d_i z$, so the inherited $(v,c)=1$ forces $(d_i,c)=1$, and for its nonzero squarefree signs the exact remaining mask is $(z,cd_i)=1$. This gives an exterior $1/d_i$ and a reciprocal smooth-integer convolution over the primes of $d_i$, with norm cost $d_i/\varphi(d_i)$. The remaining unmasked norm is bounded by the uniform signed DIT interval form using $\mathscr B(c)/c=\mu^2(c)\varphi(c)/c^2$; dropping the outer $c\ge K$ and $(c,d_i)=1$ in a positive norm is a contraction bound. Each factor therefore has norm $O(1/\varphi(d_i))$. Cauchy on the scalar product and absolute summation in the finite allocation expansion now cost at most

$$
 \prod_p\left(1+|\eta_p|
        \left(\frac{2}{p-1}+\frac1{(p-1)^2}\right)\right)=O(1),
$$

uniformly in the mask, by convergence of $\sum_p p^{-2}$. With $K_{B_0}\asymp V(B_0)$ and the negligible errors this proves (3), since $V(B_0)\gg_C 1/L_2$. Finally use the squared external convolution cost $1/V(B_0)^2$ and the small-$c$ part to obtain (2). The proof also gives uniformity for bounded-BV weights on $I$: partial summation in the original divisor variable expresses such a weight as a signed combination of hard subinterval prefixes; apply Minkowski in the positive norm of (2). No part of this reciprocal norm comparison uses GRH.

## 3. Keep the stronger sparse sampling bound and integrate the actual derivative

Use the exactly inverted physical rational vector of [the preceding signed unit proof](weak-s-type-ii-critical-prime-full-polynomial-narrow-derivative-unit-signs-grh.md#1-the-inherited-physical-rational-diagonal-and-literal-approximation), after the inherited time and dual tails but with $h\le H_0$ initially. At fixed $l,s,\beta$ define

$$
 R_c(x)=\sum_{\substack{scv\in I_d\\(cv,lN)=1}}
                \frac{\mu(cv)}v\,w(Nx/(scv)),
 \qquad F_c(x)=\Omega(x)e(\beta Nx)R_c(x).
$$

For each $h_1,h_2$ pair the exact same rational equality with $(u u',N)=1$ gives $g=(h_1,h_2)$ and the same transform $\widehat F_c(a\Lambda_c)$ on both arms, with $\Lambda_c=N/(q l^2g c)$. As in that proof, the precise signed pair contribution is

$$
 \frac{q(q-1)N^2\,\mu(h_1)\mu(h_2)}{q^2l^4h_1h_2}
       \sum_{c\ge1}\frac1{c^2}\sum_{\substack{a\ne0\\(a,c)=1}}
                                      |\widehat F_c(a\Lambda_c)|^2 .
 \tag{5}
$$

All restoration and sampling below takes place in this exact **rational** determinant diagonal, not in the finite modular expansion.

Fix $q,l,g$, and write $C_* = N/(q l^2g)$ so $\Lambda_c=C_*/c$. In the dense range $c\ge C_*$ use positive periodization at period $1/\Lambda_c\ge1$, since the physical support has length less than one. Its weighted cost is at most

$$
       \frac1{C_*}\sum_{c\ge C_*}\frac{\|F_c\|_2^2}{c}.
 \tag{6}
$$

In the sparse range $1\le c<C_*$, do **not** weaken the $a\ne0$ integration-by-parts bound to $\Lambda_c^{-1}$. Keep the stronger $\Lambda_c^{-2}\|F_c'\|_1^2$ after summing $1/a^2$. Write

$$
 A_c=(\Omega(x)e(\beta Nx))'R_c(x),\qquad
 B_c=\Omega(x)e(\beta Nx)R_c'(x).
$$

The weighted sparse cost is at most

$$
              \frac{O(1)}{C_*^2}
                  \sum_{1\le c<C_*}(\|A_c\|_1^2+\|B_c\|_1^2).
 \tag{7}
$$

In (6)–(7) the additional coprimality of $a,c$ is dropped only by positivity.

The dense cost (6), and the $A_c$ part of (7), are at most $O(1/(C_*V(lN)))$. In fact apply (2) at the **whole** actual interval $I_d/s$, with mask $B_0=lN$, using bounded-BV weight $w(Nx/(su))$ in $u$ for each fixed physical $x$. Its sup and variation are $O(1)$ by monotone composition. This is in the location required by (2): $s\le L^{16}$ and $d$ lies between $X$ and $N^{.50001}$, say $u\in[N^{.48},N^{.51}]$ for large $N$. It follows that $\|R_c(x)\|_{\ell^2(1/c)}^2\ll1/V(lN)$ uniformly in real physical $x$. For $A_c$ now use Minkowski in $x$ and $\|(\Omega(x)e(\beta Nx))'\|_1=O(1)$, and use $C_*^{-2}\le C_*^{-1}/c$ on the sparse range. This derivative bound is for the physical phase only.

The genuine cofactor derivative $B_c$ instead satisfies the **per-coordinate** estimate $\|B_c\|_1\ll1$, uniformly in $c$ and in $\delta$. To see this, expand the finite $v$ sum for each fixed $c$ and take absolute values only for this derivative. Write $w(k)=W(\log k)$, so the derivative with respect to $x$ in each term is $x^{-1}W'(\log(Nx/(scv)))$. The two translates of the log-coordinate mollifier making up $W'$ have $L^1$ norm at most a fixed constant. The change of variable $z=\log(Nx/(scv))$ thus bounds the integral of each summand's derivative factor on $x\in[7/16,1/2]$ by a constant. Moreover it can be nonzero for either endpoint $k_{\mathrm e}$ only when

$$
                   v\asymp \frac{N}{s c k_{\mathrm e}},
$$

with fixed positive proportional constants: $x$ is in that fixed physical interval and $W'$ is only within $O(\delta)$ of the two actual log endpoints. The unsigned reciprocal sum $1/v$ in each such proportional interval is $O(1)$, including when its scale is below one. The two possible endpoints give $\|B_c\|_1=O(1)$. This uses the exact physical integration domain, and does not bound the pointwise derivative by its possibly large $\delta^{-1}$ sup norm. Thus its part of (7) is $O(1/C_*)$ by counting $c<C_*$, or is empty if $C_*\le1$. Combined, the dense and sparse bounds give

$$
 \sum_c\frac1{c^2}\sum_{\substack{a\ne0\\(a,c)=1}}
              |\widehat F_c(a C_*/c)|^2
                  \ll \frac{1}{C_* V(lN)} .
 \tag{8}
$$

The crucial savings are the true sparse $\Lambda_c^{-2}$ and the per-$c$ integrated derivative, rather than a pointwise derivative cost in a reciprocal norm.

Now restore all $h\mid\operatorname{rad}N$ **only in the analytical rational vector** as in [the exact exterior unit argument](weak-s-type-ii-critical-prime-full-polynomial-narrow-derivative-unit-signs-grh.md#3-exact-exterior-unit-signs-in-the-physically-inverted-norm). Formula (5) is valid for any set of rational $h$ labels, including labels not coprime to $q$, because exact equality of the rationals uses only true $(uu',N)=1$. For the vector of omitted labels $h>H_0$ use (8) and absolute values of the two exterior signs. Its squared norm is at most

$$
 O\left(\frac{N^2}{L l^2 V(lN)}\right)
 \sum_{\substack{h_1,h_2\mid\operatorname{rad}N\\h_1,h_2>H_0}}
                                      \frac1{[h_1,h_2]} .
$$

The same pair Rankin bound from the cited proof makes the last sum $O(e^{-C_0L_2}L_2^{O(1)})$. Even $1/V(lN)\ll L_2$ is harmless. This bounds the rational tail vector before any further norm sums. It has not added an $h$ term into the modular coefficient or its off-diagonal.

For the full rational vector, group the signs in (5) at each gcd $g$ first; the common $F_c$ and step $\Lambda_c$ are identical within the group. Their exact coefficient is $g^{-2}\prod_{p\mid N,p\nmid g}(1-2/p)\ge0$, with the same exact zero at $p=2$ if $2\nmid g$. The factor $1/C_*$ in (8) supplies one $g$, and the signed Euler mass remaining is

$$
       \sum_{g\mid\operatorname{rad}N}\frac1g
                  \prod_{\substack{p\mid N\\p\nmid g}}(1-2/p)
                            =V(N).
$$

Thus (8), (5) and $\sum_q(q-1)\ll N/L$ give a full squared rational bound at fixed $l,s,\beta$ of

$$
                O\left(\frac{N^2}{L l^2}\frac{V(N)}{V(lN)}\right).
 \tag{9}
$$

The omitted $h$ norm just bounded and the inherited exact-rational $j,\tau$ restoration errors can be transferred back with negligible costs. Since $(l,N)=1$, the ratio in (9) is exactly $l/\varphi(l)$; it no longer costs logarithms in $N$. Combine with the original off-diagonal determinant bound, then take Minkowski over $l,s$. In norm the genuine label factor is

$$
       \sum_{\substack{l\le T\\ l\text{ squarefree}}}
            \frac{\tau_{\rm d}(l)}{l}\sqrt{\frac{l}{\varphi(l)}}
        \le \prod_{p\le T}
                  \left(1+\frac2{p\sqrt{1-1/p}}\right)
        \ll (\log T)^2\ll L_2^2 ,
$$

where $\tau_{\rm d}$ is the divisor function and the last bound is Mertens with absolutely summable $O(p^{-2})$ local deviations. In the true additive nonprincipal expansion the extra squared factor $q/(q-1)$ is bounded, and the $\beta$ interval has length $1/(5N)$. Thus the inherited true nonprincipal contribution is $O(NL_2^4/L)$, plus errors smaller than $O(NL^{-2})$.

## 4. A signed real sum–integral for the actual $q$-nonunits

We return to the **original truncated** smoothed coefficient of §1, with all $\Omega$ and $\beta$ weights, not the analytical extension to all $h$. Its nonunit value is independent of the actual numerator $a$. If $q\mid N$ it is zero by the true long unit and $k<X/2<q$. Otherwise $q\mid dk$ forces $q\mid d$ and $d=q s u$ in the actual split, with $s=(l,d)=(l,d/q)$ because $l\le T<q$. Here $(u,lNq)=1$ and $\mu(d)=-\mu(s)\mu(u)$ on its nonzero support. The genuine short condition from the approximation is $k$ a positive multiple of $b=l^2h/s$. The true cofactor weight is the common $w(k)$ across the whole interval because the auxiliary bumps were one on the actual physical support.

For fixed $l,s,u,h$, the exact $k$ test is $w(k)\Omega(qsu k/N)e(\beta qsu k)$, continuous and compactly supported for positive $k$, with total variation $O(1)$ independent of $\delta$ and of the four labels. This uses the support $qsu k\asymp N$ and $|\beta|N\ll1$ for the phase, and the bounded variation of both real cutoffs. Sampling at positive multiples of $b$ therefore equals $b^{-1}$ times the real integral with $O(1)$ error: compare the integral on each progression cell to its sampled endpoint and sum the variation. After $x=qsu k/N$, the main term is exactly

$$
        \frac{N}{q l^2 h u}
                     \int\Omega(x)e(\beta Nx)w(Nx/(qsu))\,dx.
 \tag{10}
$$

The total absolute cost of the $O(1)$ errors over the labels is $O(N^{1/100000+o(1)})=o(X)$, since $qsu\in I_d\subset[X,N/(2t))$ implies $u\ll N^{1/100000}/s$, and $l,s,h$ have only subpower total counts. This is uniform in $q,\beta$.

In the main term (10) the actual truncated $h$ signs give the single factor

$$
 \sum_{\substack{h\mid\operatorname{rad}N\\h\le H_0}}\frac{\mu(h)}h
      =V(N)+O_A(L^{-A})
$$

for every specified fixed $A$ by sufficiently large fixed $C_0$, using the same reciprocal Rankin bound for the omitted $h$ labels. In particular this is $O(V(N))$. For each fixed physical $x$ the remaining actual $u$ weight $w(Nx/(qsu))$ has sup and variation $O(1)$. The signed harmonic sum of $\mu(u)/u$ on any prefix with mask $(u,lNq)=1$ is $O((lNq)/\varphi(lNq))$: convolve the bounded ordinary reciprocal Möbius prefix with the positive reciprocal weights of the mask-smooth integers. This also applies on the actual hard interval $qsu\in I_d$ with the bounded-BV multiplier by Abel. Since $q\nmid lN$, the cost is $O((l/\varphi(l))/V(N))$. The exterior true $h$ factor cancels the last $1/V(N)$. Finally

$$
           \sum_{\substack{l\le T\\l\text{ squarefree}}}
                   \frac{\tau_{\rm d}(l)}{l^2}\frac{l}{\varphi(l)}
                    \ll1
$$

by its convergent prime product. Thus (10), after keeping the genuine $\mu(u)$ and $h$ signs, gives $O(N/q)=O(X)$ for the actual $q$-nonunit value, including the negligible floors. This is uniform in the entire polynomial interval and all cuts.

Its shell energy is $O(N/L)$ by the original number of critical primes, $\sum_q(q-1)\ll N/L$, and the $\beta$ length $1/(5N)$. The actual principal unit coefficient has numerator-zero value equal to the ordinary full approximated polynomial minus these true nonunits. Its constant value on $a\ne0$ comes with the factor $-1/(q-1)$. Since the ordinary squared norm is $O(N)$ by §1 and $\sum_q1/(q-1)\ll1/L$, the ordinary part contributes $O(N/L)$ in energy as well; the subtracted nonunits satisfy the same or smaller bound. No artificial constant from the rational construction has replaced either actual term.

## 5. Return to the exact signed shell

The original arcs are disjoint. Use ordinary Parseval for the global genuine smoothing error $O(NL^{-2})$ and the smaller squarefree and short-unit truncation errors, together with the original shell estimates in §§3–4. This proves (1) for the exact hard coefficient. The true $P$ and $D$ have ordinary norm $O(\sqrt N)$, so Cauchy and separate numerator centering give the first two signed bounds. The original parity-preserving identity for the genuine odd supports and physical geometry, with error $O(N/L+N(X/M)^2)$, gives the third signed bound at $M=\lceil XL^2\rceil$. The sharper diagonal and actual nonunit estimates are unconditional, but the nonzero-determinant argument remains conditional as stated.
