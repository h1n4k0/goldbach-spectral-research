# A matched Ramanujan mean detects missing odd conductor factors

**Scope.** This extends the actual exceptional signed-mean calculation to full-primorial samples that can miss arbitrarily many odd factors of the actual Page conductor, subject to the combined modulus bound below. The signed test is the normalized Ramanujan sum of that conductor, bounded by one. It is selected after specifying the actual conductor, not a fixed family of tests independent of it. There is a quantitative conditional lower bound even when the response factor is smaller than every fixed inverse power of the logarithm. No Page-zero existence, individual-target bound, full signed-shell or mixed-strip positivity, prime-pair conclusion, or Weak S follows. No Dirichlet GRH or imported zero-gap assertion is used.

Use the dyad, cutoffs and genuine exceptional corrections $\mathfrak E_\pm$ as in the [complete signed mean](r95-spectral-complete-planting-signed-mean.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, and the actual Page character $\chi$ is primitive real with conductor $r\le Q_0$ and simple zero $\beta>1-4a_0/\sqrt G$. If no such zero exists the correction is zero and no filter is needed. Write $r=2^e r_{\rm odd}$, with $e\in\{0,2,3\}$ and $r_{\rm odd}$ squarefree, as in [the three 2-adic channels](r99-spectral-two-adic-exceptional-mean-channels.md). Keep the same fixed admissible $B>B_0>0$, bounded-BV common scaled left test $I_N=NJ$, $\omega_N(u)=w(u/N)$ with $J\subset(1/2,9/16]$ half-open, and bounded-BV target weight $\eta(N/Y)$.

Take the original complete planting $K_z=\prod_{p\le z}p$ with $2\le z\le Z$, and set $M=[K_z,r]$. Assume $M\le e^{2Z}$ and that $z$ and $M$ are constant within the dyad. Put $D=r_{\rm odd}/(r_{\rm odd},K_z)$, $P=M/K_z$, and $\tau_e=1$ for $e=0,2$, $\tau_3=1/2$. Define the original normalized mean and the real matched factor by

$$
   \langle F\rangle_{K_z}=\frac {K_z}Y
      \sum_{\substack{Y\le N\le2Y\\K_z\mid N}}\eta(N/Y)F(N),
   \qquad
    \gamma(N)=c_r(N)/\varphi(r),
 \tag{1}
$$

where $c_r$ is the ordinary Ramanujan sum. In particular $|\gamma(N)|\le1$. For $i=0,1$ let $P_i(M)$ be the integral (2) of the three-channel proof, using the exact completed cap $\mathcal A_i(v,x)$ of [the aligned formula](r96-spectral-aligned-mean-euler-collapse.md) with sampling modulus $M$. Explicitly,

$$
 P_i(M)=\frac1Y\int_Y^{2Y}\eta(v/Y)
      \int_{v-x\in vJ}\frac{w((v-x)/v)(v-x)^{\beta-1}x^{\beta-1}}
                            {\log x}\,\mathcal A_i(v,x)\,dx\,dv .
$$

All original hard cuts and the original finite denominator range are retained.

**Theorem.** For any function $\psi$ on the $P$ residue classes of the integer $m=N/K_z$ (the values can depend on the fixed dyad), let $\mathbb E_P$ denote the exact uniform finite average over $m\bmod P$. With a fixed exponent $C$ one has

$$
 \left\langle \psi(N/K_z)\mathfrak E_\pm(N)\right\rangle_{K_z}
   = -\frac{\chi(-1)}2(P_0(M)\pm P_1(M))\,
                  \mathbb E_P[\psi(m)\gamma(K_zm)]
     +O\!\left(Y^\beta G^C r^{-1/2}\mathbb E_P|\psi|\right).
 \tag{2}
$$

In particular for $\psi(m)=\gamma(K_zm)$ the exact response factor is $\tau_e/\varphi(D)$, and the error in (2) is at most
$O(Y^\beta G^C r^{-1/2}(\tau_e/\varphi(D))\,2^{\omega(D)})$.
No lower size restriction on this response factor is needed.

For the following lower bound assume in addition $(1-\beta)G\le C_*\log G$, with fixed $C_*$, and $z\ge A_0\log G$ for a sufficiently large fixed $A_0$ depending only on the fixed cutoffs and threshold. Take fixed nonnegative $w,\eta$ with positive integrals. For sufficiently large such dyads,

$$
 -\chi(-1)\,\left\langle
       \gamma(N)\bigl(\mathfrak E_+(N)-\mathfrak E_-(N)\bigr)
                         \right\rangle_{K_z}
 \ \gg\
      \frac{\tau_e}{\varphi(D)}
      \left(\int_J w\right)\left(\int_1^2\eta\right)
      \frac{Y^{2\beta-1}}G\,\frac{M}{\varphi(M)(\log r)^4}.
 \tag{3}
$$

Constants may depend on the fixed tests and parameters. This allows $D>1$ even when $\varphi(D)$ exceeds every fixed power of $G$; it does not require $D$ to be small relative to $r$. Neither (2) nor (3) asserts this bound for conductors outside the stated $M$ range.

## 1. Retain the explicit error on each translated residue

For each $a=K_zm\bmod M$ use the normalized residue mean $(M/Y)\sum_{N\equiv a\ (M)}\eta(N/Y)(\cdot)$ over the dyad. The [all-target formula](r94-spectral-all-target-ramanujan-exception.md) retains the explicit error $O(Y^\beta G^C r^{-1/2})$ on each such mean, since $M\le e^{2Z}$ and there are $O(Y/M)$ terms. For each finite $q\mid t$ in that two-pole model, the only termwise arithmetic constraints in the R95 affine expansion are $d\mid N$ with $d\mid q$, $q$ squarefree and $(q,r)=1$. Every prime dividing both $d$ and $M$ divides $K_z$, since all primes of $M$ outside $K_z$ divide $r$. Thus every constraint is compatible with $N\equiv a\bmod M$, and the intersection is one translate modulo $[M,d]$. Its normalized BV sampling multiplier is $(M,d)/(dY)$, exactly as in R99, independent of $a$. Since $r\mid M$, the Ramanujan factor is $\gamma(a)$ on that whole class. The physical weight and arithmetic divisor expansion are exactly those of R95 (5)--(7), and both translated sampling errors and the true all-target error remain $O(Y^\beta G^C r^{-1/2})$ with a fixed $C$. In detail the sampling error has the power factor $(M/Y)rQ_0^{O(1)}=Y^{-1+o(1)}$ after the $Y^\beta G^{O(1)}$ absolute weights; it is absorbed by the displayed conductor error.

Therefore the underlying finite algebraic mean on each class is the same complete $M$ model, times $\gamma(a)$. The exact R96 Euler collapse applies because the remaining labels satisfy $rt\mid M\le Q_0$, so there is no further denominator truncation error. In converting to the R96 geometric caps, keep the **fixed power saving** on the artificial cutoff $S=Y^{1/10}$ from R96 Section 3. That argument uses the primitive tail $Y^{-c_2}$ uniformly through $j\le S^{1/2}$, and the positive moment saving $S^{-1/8}$ off that range. All other factors there are $Y^{o(1)}$, and $Y^{2\beta-1}\le Y^\beta$. Hence its error is $O(Y^\beta Y^{-c_3})$ with fixed $c_3>0$, also absorbed by $O(Y^\beta G^C r^{-1/2})$. In this way the per-class formula (5) of R99 retains the explicit conductor error, before any conversion to arbitrary inverse logarithms. Averaging with the literal $\psi$ gives (2); indeed the factor $1/P=K_z/M$ exactly combines the normalized residues, and the absolute weighted error is bounded by the finite mean of $|\psi|$.

The allowed conductor exponents imply $P=2^{\max(e-1,0)}D$. At a missing odd prime $p\mid D$, as $m$ runs modulo $p$, the local $\gamma_p(K_zm)$ is $1$ when $p\mid m$ and $-1/(p-1)$ otherwise. Its mean square is $1/(p-1)$ and its mean modulus is $2/p$. At odd conductor primes dividing $K_z$ the factor is identically one; at the $2$-part the mean square and mean modulus both equal $\tau_e$ by the exact rows in R99. Independence here is just the Chinese remainder theorem on the finite classes modulo $P$. Thus

$$
  \mathbb E_P\gamma(K_zm)^2=\frac{\tau_e}{\varphi(D)},\qquad
  \mathbb E_P|\gamma(K_zm)|=\tau_e\prod_{p\mid D}\frac2p,\qquad
  \frac{\mathbb E_P|\gamma(K_zm)|}{\mathbb E_P\gamma(K_zm)^2}
           =\prod_{p\mid D}2(1-1/p)\le 2^{\omega(D)}.
 \tag{4}
$$

This is why the conductor error must be retained in (2), rather than simply using a uniform $O_A(Y^\beta G^{-A})$ without regard to the mean modulus of the filter.

## 2. Extra conductor primes are positive shifts on the integrated primitive

We check exactly the extra prime factors in applying [the all-primorial integrated proof](r98-spectral-all-primorial-aligned-mean.md) to $M$ for the lower bound. Let $\ell=\log z$, $b=1-\beta$, and choose $U_*=C_0\log G$ for a fixed constant large enough to exceed $\ell$ and all genuine $U_v$. The R96 coefficient $\alpha_p^M$ vanishes on all $p\le z$ and also on the extra set $\{p\mid r:p>z\}$. Outside $M$ put $a_p=|\alpha_p^M|$, so $a_p\ll p^{-\beta}$ and $|a_p-p^{-\beta}|\ll p^{-2\beta}$. Start with the exact rough reciprocal Möbius primitive of R98 Section 1, rough at $z$ only. In the all-minus intermediate primitive keep weight $-1/p$ at the extra $r$ primes; replace the weights by $-a_p$ only at $p>z,\ p\nmid r$. With these choices the perturbing finite signed ratio product at relevant $p\le e^{U_*}$ is a **subproduct** of the same type of ratios in R98 (4), with total-variation error $O(z^{1-2\beta}+bU_* e^{bU_*})=o(1)$ by the same bound on their absolute local errors. Its shifts start after $\ell$. The resulting intermediate integrated primitive is nonnegative on $[0,U_*]$, equals $u$ for $0\le u\le\ell$, is $\gg\ell$ for $u\ge\ell$ there, and it and its unsmoothed primitive are $O(\ell)$ in absolute value, by the R98 comparison with ordinary rough reciprocal Möbius.

Use the positive ratios $(1+\alpha_p^M X)/(1-a_pX)$ at the primes outside $M$, as in R98 Section 2. At an extra conductor prime $p>z$ the actual coefficient is zero, so its ratio to the intermediate primitive is instead $(1-X/p)^{-1}$. Both are genuine nonnegative shift measures with unit atom at zero. Both have total mass $1+O(1/p)$ and normalized first log moment $O(\log p/p)$ for all relevant $p\le e^{U_*}$, uniformly, since $bU_*=o(1)$. For the additional geometric one the mean is exactly $\log p/(p-1)$. Consequently the same Markov argument in R98 (5) applies to their combined positive product: restricting primes to $p\le e^{U/C_1}$ for fixed sufficiently large $C_1$ puts at least half that restricted mass at shifts $\le U/2$, and the mass of the full product with $p\le e^U$ is only a bounded multiple of the restricted mass. For $\ell\le U\le2\ell$ its cumulative mass is bounded by the reciprocal mass of primes in $(z,z^2]$. If $D_+(U)$ is that combined positive cumulative shift mass, the actual primitive $R_1$ and its integral $A$ satisfy

$$
 \sup_{0\le u\le U}(|R_1(u)|+|A(u)|)\ll\ell D_+(U),
 \qquad A(U)\gg\ell D_+(U)\qquad(\ell\le U\le U_*).
 \tag{5}
$$

For $U\le\ell$ they remain exactly $1$ and $U$ at the endpoint. This uses no hypothesis on the number or size distribution of the extra conductor primes.

For the negative signed part of the finite cap, the R98 inverse-removal sums (6)--(8) run only over $p>z$ with nonzero actual coefficient. Removing the additional conductor primes leaves their bounds unchanged: both the aggregate mass and its first log moment are $\ll z^{1-2\beta}$, the latter by $\sum_{p\le t}\log p\ll t$ as before. Hence $(C_M(0)-Q_M(U))/M_M\ge-O(z^{1-2\beta}S(U)^2)$ with $S(U)=\sup_{[0,U]}|R_1|$ and $M_M$ denoting the prefactor (2) of R96 with $K=M$. Likewise for $\ell\le U\le U_*$ the finite $J_M(U)/M_M$ is $\gg\ell^2D_+(U)^2$ by (5) and the inverse-removal mass, and for $U\le\ell$ it is exactly $U^2$. The true $T_{v,x}$ is positive and $O(\log G)$. Because $z^{1-2\beta}=z^{-1}e^{2b\ell}$ with $b\ell=o(1)$, the hypothesis $z\ge A_0\log G$ with $A_0$ large makes the negative shifted-tail error at most half the $J_M$ lower in the first range. In the second range $U_v^2\gg\ell^2$ since $U_v=(B-B_0)\log\log v$ and $\ell\le\log G$, whereas the negative error is $O(1)$ and $\ell\to\infty$. Thus on the actual support the genuine color-one cap is $\mathcal A_1(v,x)\gg M_M\ell^2$.

The normalizing product now has $M/\varphi(M)$ exactly, because the conductor factor $r/\varphi(r)$ restores **all** the conductor primes. The remaining interior Euler factors are only at primes $p\le z$, since every extra prime of $M$ belongs to $r$. Their product is at least $\exp(-2\sum_{p\le z}p^{-\beta})\gg\ell^{-2}$. The exterior factor is $1+O(z^{1-2\beta})$, and $|L'(\beta,\chi)|\ll(\log r)^2$ as in R96 and R98. Consequently the positive physical integral satisfies

$$
 P_1(M)\gg
      \left(\int_J w\right)\left(\int_1^2\eta\right)
      \frac{Y^{2\beta-1}}{G}\frac{M}{\varphi(M)(\log r)^4}.
 \tag{6}
$$

This is a lower bound for the exact cap in a signed mean, not a pointwise estimate on the arithmetic correction.

## 3. The finite detector still works at a subpower-small response

Subtract the two parity formulas (2) and match with $\psi=\gamma$. The color-zero term cancels, leaving the real sign $-\chi(-1)$, times $\tau_e/\varphi(D)$ and $P_1(M)$. The error divided by that response is $O(Y^\beta G^C r^{-1/2}2^{\omega(D)})$ by (4). For any fixed $\delta>0$, $2^{\omega(D)}\ll_\delta D^\delta\le r^\delta$: the local ratio $2/p^\delta$ is at most one above a fixed threshold and there are only finitely many smaller primes. Taking for example $\delta=1/4$ and using the classical Page conductor bound $r>G^A$ for each fixed $A$ makes this normalized error $O_A(Y^\beta G^{-A})$ for every fixed $A$. Under the stated zero closeness $Y^{2\beta-1}\ge YG^{-2C_*}$ and $\log r\le2Z$, so (6) dominates that error on the fixed tests. This proves (3) with the exact small response factor even when the ordinary unweighted mean is annihilated. The argument works entirely with the original untrimmed divisibility family; the stronger conclusion is confined to a bounded signed test of its genuine exceptional correction.
