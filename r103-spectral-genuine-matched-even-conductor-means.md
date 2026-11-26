# Matched even-conductor channels of the genuine mixed strip

**Scope.** This extends the matched calculation from the isolated exceptional correction to the **genuine full mixed-strip correlation and its original moving-major integral**. It applies on the complete full-primorial divisibility family, even when that primorial misses odd primes of the actual even Page conductor. The errors are controlled relative to the small exact Ramanujan response, not merely to the unmodulated scale. The sign and lower bound are conditional on a sufficiently close Page zero. No existence claim, individual-target sign or size, unweighted positivity, full signed shell beyond this mixed strip, prime-pair result, or Weak S is asserted. No Dirichlet GRH or external zero-gap theorem is used.

Use the original dyad, common scaled tests, and actual sums of [the complete signed mean](r95-spectral-complete-planting-signed-mean.md) and [the genuine two-adic mixed means](r102-spectral-genuine-two-adic-mixed-means.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, $I_N=NJ$ for a real half-open $J\subset(1/2,9/16]$, and $\omega_N(u)=w(u/N)$, with uniformly bounded-BV $w,\eta$ common across the dyad. The real cuts are the original fixed admissible $B>B_0>0$. Write $X_\pm=S_\pm$ for the genuine full correlation or $X_\pm=S_\pm^{\rm maj}$ for its **original moving** polynomial-major integral. The superscript thus uses denominator bound $N^{1/1000}$ and radius $2N^{1/1000}/N$, not the common auxiliary arcs. Symbols $\mathcal B_\pm,\mathfrak E_\pm$ denote the exact regular bracket and actual exceptional correction in [the all-scale decomposition](r89-spectral-exceptional-conductor-folded-sampling.md).

Suppose the actual Page character $\chi$ in that decomposition exists, with primitive real conductor $r=2^e r_{\rm odd}$, $e=2$ or $3$, and simple real zero $\beta>1-4a_0/\sqrt G$. The odd part $r_{\rm odd}$ is squarefree. Fix the full primorial $K=K_z=\prod_{p\le z}p$ with $2\le z\le Z$, and let $M=[K,r]\le e^{2Z}$. Neither $r_{\rm odd}\mid K$ nor any upper bound on the number of missing odd factors is required. Adopt the notation of [the matched exceptional mean](r100-spectral-matched-ramanujan-exceptional-mean.md):

$$
 D=\frac{r_{\rm odd}}{(r_{\rm odd},K)},\qquad
 P=\frac M K=2^{e-1}D,\qquad
 \gamma(N)=\frac{c_r(N)}{\varphi(r)},\qquad
 H=\mathbb E_{m\bmod P}\gamma(Km)^2
       =\frac{\tau_e}{\varphi(D)},\quad \tau_2=1,\quad\tau_3=\tfrac12 .
 \tag{1}
$$

Write $L_\gamma=\mathbb E_{m\bmod P}|\gamma(Km)|$, so $L_\gamma/H\le 2^{\omega(D)}$ exactly as in that proof. Here $\mathbb E$ is the uniform finite-class average, unrelated to the physical sampling at the dyad edges. The normalized physical mean still uses $(K/Y)\sum_{K\mid N}\eta(N/Y)(\cdot)$. Let $P_i(M)$, $i=0,1$, be the completed cap integrals of R100 at modulus $M$, with all original $U_v,T_{v,x}$ retained and without the parity half or $-\chi(-1)$ sign.

**Theorem.** Uniformly for the stated tests and for each fixed $A>0$, for either genuine choice of $X_\pm$,

$$
   \left\langle\gamma(N)X_\pm(N)\right\rangle_K
       =-\frac{\chi(-1)}{2}H\bigl(P_0(M)\pm P_1(M)\bigr)
                                   +O_A(H\,YG^{-A}).
 \tag{2}
$$

The error is relative to the exact factor $H$, even when it is smaller than every fixed inverse power of $G$. No additional zero-closeness or lower $z$ bound is needed for (2).

For the quantitative sign assume in addition that $(1-\beta)G\le C_*\log G$, $z\ge A_0\log G$ for the sufficiently large fixed $A_0$ of R100, and that $w,\eta$ are fixed nonnegative with positive integrals. Then for all sufficiently large such dyads,

$$
 -\chi(-1)\left\langle\gamma(N)
                  \bigl(X_+(N)-X_-(N)\bigr)\right\rangle_K
 \gg H\left(\int_Jw\right)\left(\int_1^2\eta\right)
       \frac{Y^{2\beta-1}}G\,\frac M{\varphi(M)(\log r)^4}.
 \tag{3}
$$

The large-scale comparison is ineffective as in R100. The same weights and progression are used for the two actual sums and both parities. No targets are discarded.

## 1. Quantitative ordinary errors on the original auxiliary arcs

Let $\mathcal U_\pm(N)$ be the actual auxiliary major integral with the common cutoff $Q_0$ and radius $2Q_0/Y$. Before any averaging we claim, uniformly on the actual dyad and hard tests,

$$
 \mathcal U_\pm(N)
   =\mathcal B_\pm(N)+\mathfrak E_\pm(N)
      +O\!\left(YG^C\exp(-4Z+C G^{1/4})\right)
 \tag{4}
$$

for a fixed $C$. This requires keeping rates in the deterministic R89 step, and using the non-squarefree even conductor; its previously displayed arbitrary fixed inverse-log error alone would not suffice here.

Partition the actual auxiliary arcs into $r\nmid q$ and $r\mid q$. On the first part use [R87 Section 1](r87-spectral-all-scale-exceptional-left-reduction.md), which excludes the actual Page pole from every progression conductor there, including genuine nonunit reductions and masks. The analytic budget in [the uniform auxiliary-major calculation](r86-spectral-universal-good-scale-windows.md) (Section 2) is $Y G^{O(1)}Q_0^5 e^{-c\sqrt G}$, plus a fixed power saving from the positive-variable counts after fixed powers of $Q_0$. These come from the polynomial range prime and signed Möbius estimates and the positive squarefree floors described in [R85 Section 2](r85-spectral-unconditional-planted-ap-good-dyads.md). They are pointwise, before any target restrictions, and $\log Q_0=16Z=o(\sqrt G)$.

On $r\mid q$ use R87 Section 2 against the **actual** right Fourier polynomial, not its formal model. The ordinary principal term is exactly zero: it carries $\mu(q)$, and $4\mid r$ implies $4\mid q$. The exceptional term is exactly $\mathfrak E_\pm$ by definition. The residual in the left progression (R87 (6)) integrates to the same $Y G^{O(1)}Q_0^5 e^{-c\sqrt G}$ budget. In completing the formal ordinary rational sum on all denominators, **no formal term with $r\mid q$ is missing**, again because $\mu(q)=0$. This is precisely where the even-conductor hypothesis matters; the generic ineffective inverse-log saving for the omitted ordinary $r$-multiples is not used.

The slow Fourier completion in R85 Section 2 has error $YQ_0^{-1}G^{O(1)}$. The ordinary rational tail is $Y G^{O(1)}Q_0^{-1/4}\mathcal A(N)^{C_1}$, by R85 (6), where
$\mathcal A(N)=\prod_{p\mid N,\ p>2}(1-\alpha_p^\circ p^{1/4})^{-1}$ and $\alpha_p^\circ=(p-1)/(p^2-2)$. The elementary uniform bound in R89 (10) gives $\log\mathcal A(N)=O(G^{1/4})$: split $\sum_{p\mid N}p^{-3/4}$ at $G$ and use $\log N=O(G)$. With the actual cap this tail is $Y G^{O(1)}\exp(-4Z+O(G^{1/4}))$ without a radical exception.

We give the rate check for the remaining real cap conversion in R85, which does not extend the finite positive cuts. In the [ordinary squarefree CRT calculation](r63-spectral-full-squarefree-crt-strip.md), (12)--(13), and the [ordinary signed cap calculation](r67-spectral-high-mixed-parity-major.md), Section 2, the artificial cutoff logs are comparable to $G$. At $j$ below the half-log cutoff the real primitive endpoint is still at least $c_0G$ for a fixed $c_0>0$; the other $j$ have the reciprocal square weight and the positive half-moment of [the ordinary finite-bracket proof](r80-spectral-whole-mixed-parity-density.md), Section 2. For clarity, a reciprocal primitive involved in these steps has prime array $\beta_p=1/p+O(p^{-2})$ outside a mask $w_0$ of polynomial size in $Y$, and zero on the mask primes. For the unmasked ordinary reciprocal Möbius primitive the rate is $O(e^{-c\sqrt u})$ in the log variable (Montgomery--Vaughan, [Chapter 6](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287), (6.18), also used in R63). Its convolution with the Euler ratio $(1-\beta_p X)/(1-X/p)$ at shift $\log p$ has a $1/4$-exponential absolute moment bounded by

$$
 \exp\!\left(O\left(1+\sum_{p\mid w_0}p^{-3/4}\right)\right)
               =\exp(O(G^{1/4})).
 \tag{5}
$$

Indeed the nonconstant weighted local deviations off the mask sum like $O(p^{-7/4})$, while on it the ratio is geometric. Splitting shifts at $u/2$ gives the pointwise and $L^1,L^2$ tail rates $\exp(-c_2\sqrt G+O(G^{1/4}))$ at the artificial endpoints, with $c_2>0$ after reducing it for the integrals. This applies uniformly to $Nj$ for the small $j$ and to the analogous low reciprocal cutoff in R63. In the complementary large-$j$ range, the $j^{1/2}$ moment of $\alpha(j)^2\mathcal A(j)^2$ costs a fixed power of $Y^{-1}$ and the $N$ moments cost only $\exp(O(G^{1/4}))$ as above; the finite short arrays also have at most fixed polylogarithmic unsigned mass by their reciprocal weights. Thus endpoint mass subtraction, clipping and restoration in the untwisted moment and autocorrelation calculations save this same stretched exponential, with only fixed polynomial factors in $G$. The actual finite $U_v$ and $T_{v,x}$ in the bracket are retained, not sent to infinity.

In particular the ordinary low intersection term is the same finite quadratic and squared-integral expression as before, obtained by finite signed integration (R67 Section 2 and [the low-strip formula](r65-spectral-bv-visible-strip-minor.md), Section 3). The separate prime marginal is not part of this genuine mixed coefficient. The estimates for its ordinary derivation, if retained before removing that marginal, are the ordinary prime number theorem with de la Vallée Poussin error on polynomially large prime intervals (Montgomery--Vaughan, Chapter 6, Theorem 6.9), and the fixed-power squarefree convolution there. Neither an inverse-log Bombieri--Vinogradov error from the full visible-strip sum nor a Dickman-profile approximation has been used in (4). With the prefactors and real integration length, all these real conversion errors are bounded by $Y G^{O(1)}\exp(-c_3\sqrt G+O(G^{1/4}))$ or a fixed power saving. This is smaller than the rational-tail term in (4), and proves the claimed quantitative deterministic budget.

## 2. A zero ordinary channel despite missing odd primes

By R102 Sections 1--3 the exact regular bracket on even $N$ expands into real dyadic BV profiles times constraints $d\mid N$ with $d$ **odd squarefree**, with no 2-adic occupancy beyond knowing $N$ is even. More explicitly, for each fixed tuple of short labels its real profile (including the common $\eta$) has sup plus variation at most $Y G^C$ times the two primitive shift masses, and the sums of the absolute scalar coefficients times those shift masses cost only $G^C$ after imposing $d\le2Y$ at the true sampled targets. These are R102 (5)--(8), which preserve the moving real integrals.

For a fixed such $d$, impose both $K\mid N$ and $d\mid N$. The progression is $N=[K,d]n$ and $v_2([K,d])=1$. On its even targets the 2-part of $\gamma(N)$ is $f_e(N)$ exactly as in R99, and on this progression its period in $n$ is $2^{e-1}$, with mean zero. The odd conductor factor is periodic in $n$ modulo a divisor of $D$: each prime of $r_{\rm odd}$ that divides $K$ already contributes the constant one, as does any missing prime supplied by $d$. The remaining odd period is coprime to $2^{e-1}$. By the exact CRT the product $\gamma([K,d]n)$ has zero complete-period mean and absolute value at most one, so every partial interval sum is $O(D)$. This does not require dropping the targets for which $\gamma$ vanishes or choosing a particular odd class. Partial summation against each genuine BV profile, followed by the same absolute scalar sum as R102, gives

$$
                      \langle\gamma\mathcal B_\pm\rangle_K
                              =O(KD G^C).
 \tag{6}
$$

This cancellation is at the expanded odd divisor constraints; $\gamma_{\rm odd}$ is not assumed to have mean zero after such a constraint.

## 3. Quantitative transfer on all the actual sampled targets

For either $s=1,2$, for the literal $\gamma$, the discrete count on each $M$-class is at most $Y/M+O(1)$, so

$$
 \frac K Y\sum_{\substack{Y\le N\le2Y\\ K\mid N}}|\gamma(N)|^s
           \le (1+O(M/Y))\,\mathbb E_{m\bmod P}|\gamma(Km)|^s .
 \tag{7}
$$

The implied upper constant is uniform at the dyad edges and the identity of the period classes is exact. The first moment of $\gamma$ bounds the contribution of (4) to the weighted comparison by $YG^C e^{-4Z+C G^{1/4}}L_\gamma$.

For the true common auxiliary complement use the ambient squared bound $\ll Y^3G^C Q_0^{-1/2}$ of [the fixed-arc complement proof](r86-spectral-universal-good-scale-windows.md) as in R95. Keeping the second moment of $\gamma$ from (7), Cauchy--Schwarz gives a contribution $\ll YG^C Q_0^{-1/4}\sqrt{KH}$. The bounded factor $\eta$ changes only the constant. For the [actual original moving minor](r79-spectral-original-minor-power-exception.md), use its bound $O(Y^{1-1/40000})$ off $O(Y^{1-3/10000})$ ambient targets. On the good part (7) gives $\ll Y^{1-1/40000}L_\gamma$; on the rest the true torus Cauchy--Schwarz bound $YG^C$ and $|\gamma|\le1$ give $\ll KG^C Y^{1-3/10000}$. This bounds the whole sampled minor, rather than removing the exceptional targets. Add the true common complement to the auxiliary integral to get the full sum; subtract the actual original moving minor from that full sum for the genuine original major. These are distinct arc operations.

Divide all these errors and (6) by $H$. The relations $L_\gamma/H\le2^{\omega(D)}\ll r^{1/4}$ from R100 and $r\le M\le e^{2Z}$ give, respectively, a deterministic error $\ll YG^C e^{-(7/2)Z+C G^{1/4}}$ and arbitrary fixed inverse-log saving against each fixed power saving in $Y$. Also $K/H=K\varphi(D)/\tau_e\le2KD\le 2M$, so the common complement divided by $H$ is $\ll YG^Ce^{-3Z}$. For (6) and the exceptional-count term of the minor use $H^{-1}\le2D$ and $KD\le M$; their factors $KD/H$ or $K/H$ are $Y^{o(1)}$. As $G^{1/4}=o(Z)$, every ordinary and actual complement error is consequently $O_A(HYG^{-A})$ **before** applying any lower-bound assumption on $\beta$ or $z$.

Finally (2) of R100 applied to $\psi=\gamma$ evaluates $\langle\gamma\mathfrak E_\pm\rangle_K$ by the leading expression in (2) here, with error $O(Y^\beta G^C r^{-1/2}L_\gamma)$. Divide this by $H$ and use $2^{\omega(D)}\ll r^{1/4}$ and the classical Page conductor growth $r>G^C$ for every fixed $C$ eventually. The remaining error is $O_A(YG^{-A})$ after that division. Combining the estimates proves (2).

To obtain (3), subtract the two actual parity formulas; only the exact color-one cap remains. R100's sign argument gives
$P_1(M)\gg (\int_Jw)(\int_1^2\eta)Y^{2\beta-1}M/(G\varphi(M)(\log r)^4)$ under the stated hypotheses. In particular this scale is at least $Y$ times a fixed inverse power of $G$, since $(1-\beta)G\le C_*\log G$ and $\log r\le2Z$. Thus (2) has error smaller than half the asserted lower bound by choosing $A$ large **after** factoring out $H$. This proves the conditional sign for genuine modulated means. It is not a claim that the ordinary full shell can be replaced by just its exceptional part on any individual target.
