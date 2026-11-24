# Prime-divisor Fourier lines of the actual retained exterior Gram

**Scope.** On the genuine fixed macro directions of R74, the exact diagonal plus continuous benchmark has small total Fourier energy outside the R73 rational collars. The complementary variance is therefore a question about the actual odd-prime Gram, not about unknown high modes of the benchmark. Separately, on one fixed true direction retained by R74, there is an explicit nonzero Fourier line of the actual positive Gram at every reduced fraction with odd prime denominator up to $Q^{3/40}$. This gives a signed difference between the average Gram at moduli divisible and not divisible by that prime. These are statements about the actual arithmetic, with original units and continuous centering. They do not bound the unestimated prime energy outside the collars, a specified modulus, or weak S.

## 1. Statement and exact indexing

Use the common literal parent index basis and any fixed R74 macro projection $\Pi$ of [R74](r74-operator-fixed-macro-mean-all-modes.md), and the two actual raw profiles $h,f$ from [R71](r71-operator-parent-terminal-layer.md). The spatial reference dyads are in $[H,M]$, with $4\le H<M\le Q^\Gamma$ and fixed $0<\Gamma<1$; their lower endpoints are $V$. The original physical basis on each parent $I$ is the normalized true weighted mean on $I_N=(Q/N)I$. In the exact formulas of R74, write $T_N^{u,v}=P_N^{u,v}-B_N^{u,v}$, $B_N^{u,v}=D_N^{u,v}+K_N^{u,v}$, for $u,v\in\{h,f\}$. In particular, $P_N^{h,h}$ is the true positive odd-character Gram of the entire unit-restricted Mangoldt data, not a prime model; the equality term is subtracted in $D$, and $K$ uses the signed singular-series continuum. Let $\iota=1$ if at least one family is $f$ and $0$ otherwise.

Use all even moduli $N=2m\in[Q,2Q]$, indexed by $m=m_0,\ldots,m_0+J-1$, $J\asymp Q$. For any field $F$ use

$$
 \widehat F(j)=J^{-1}\sum_m e(-j(m-m_0)/J)F_{2m},\qquad e(z)=e^{2\pi iz}.
 \tag{1}
$$

For $2\le B_0\le Q$ integer and $R\ge1$, let $\mathcal C(B_0,R)$ be the union of closed collars of radius $R$ in circular index distance around $Ja/b$ for reduced fractions $a/b\bmod 1$, $1\le b\le B_0$, as in [R73](r73-operator-rational-modulus-collars.md). Set $L=\log(3Q)$. For fixed $0<\kappa<1/3$ let $E_\kappa$ and $\mathcal B_{\rm HS}$ be the exact parameters from R74 (2). Under original local Dirichlet GRH at the even moduli in the shell,

$$
 \left(\sum_{j\notin\mathcal C(B_0,R)}
            \|\widehat B^{u,v}(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\kappa,\epsilon,\Theta}
 E_\kappa+\iota\mathcal B_{\rm HS}
       + L^{3/2}\big(B_0^{-1}+(1+R)^{-1/2}\big).
 \tag{2}
$$

This holds on the entire exact parent basis, hence also after applying any fixed orthogonal projection on both legs, including $\Pi$. No auxiliary GRH range is added for (2). For the R74 parameters $H=Q^{2/5},M=Q^{3/5},W_V=Q^{23/175}V^{4/7}$, with $B_0=\lfloor Q^{1/10}\rfloor,\ R=Q^{3/40}$, the bound is $O_\epsilon(Q^{-3/80+\epsilon})$ for $h,h$ and $O_\epsilon(Q^{-1/50+\epsilon})$ if one family is $f$.

For the second result fix those same spatial parameters and $B_0=\lfloor Q^{1/10}\rfloor$. There is a single real unit vector $\mathbf v_Q$ in the range of every specified R74 macro projection (independent of all frequencies and of $N$), and a positive explicit $\gamma_Q\asymp1$ defined below. Let

$$
 F_{2m}=\langle\mathbf v_Q,P_{2m}^{h,h}\mathbf v_Q\rangle,\qquad
 {\cal D}_J(\eta)=J^{-1}\sum_{r=0}^{J-1}e(-\eta r).
 \tag{3}
$$

Assume also auxiliary Dirichlet GRH through $\lceil8MB_0\rceil+2$, including $1$, as in R73. For every odd prime $p\le Q^{3/40}$, every $1\le a<p$, and the nearest index $j$ to $Ja/p$ modulo $J$,

$$
 \widehat F(j)
 =-\gamma_Q\frac{\log p}{p(p-1)}
        e(a m_0/p)\,{\cal D}_J(j/J-a/p)
   +O_\epsilon\!\left(\frac{\log p}{p(p-1)}
                     (L^{-1}+Q^{-1/80+\epsilon})\right).
 \tag{4}
$$

Take the real representative with $|j-Ja/p|\le1/2$ here. The factor $|{\cal D}_J|\ge 2/\pi$ at these indices. There is also the untapered exact rational coefficient

$$
 J^{-1}\sum_m e(-am/p)F_{2m}
 =-\gamma_Q\frac{\log p}{p(p-1)}
   +O_\epsilon\!\left(\frac{\log p}{p(p-1)}
                       (L^{-1}+Q^{-1/80+\epsilon})\right).
 \tag{5}
$$

Consequently, uniformly over the same odd primes and with averages over the actual even shell,

$$
 \operatorname{Avg}_{p\mid N}F_N-\operatorname{Avg}_{p\nmid N}F_N
 =-\gamma_Q\frac{\log p}{p-1}
   +O_\epsilon\!\left(\frac{\log p}{p-1}
                        (L^{-1}+Q^{-1/80+\epsilon})\right).
 \tag{6}
$$

In particular the sign is negative, for fixed sufficiently small $\epsilon$ and large $Q$. This compares averages of a real positive quadratic form; individual deviations are not claimed.

## 2. Stationary comparison on a common log basis

Let $z$ denote reference physical position and $x=\log z$. Transport a physical function at parameter $t\in[Q,2Q]$ by the unitary scaling $f\mapsto(Q/t)^{1/2}f((Q/t)z)$, followed by the log unitary. Define

$$
 m_t^*(x)=\big((Qe^x)^{-2/\log t}+(Qe^x)^{-1/4}\big)^{1/2},\qquad
 w_t(z)=z^{-3}m_t^*(\log z)^2 .
$$

The $I$-th transported actual parent direction in log space is

$$
 \eta_{I,t}(x)=
 \frac{\mathbf1_{\log I}(x)e^{-x}m_t^*(x)}{\big(\int_I w_t(z)\,dz\big)^{1/2}} .
 \tag{7}
$$

Indeed the physical normalizer at $t$ equals $(t/Q)(\int_Iw_t)^{1/2}$, and this factor cancels with the explicit rescaling factors in the unitary. Let $J_t$ be the isometry from the fixed parent index space with columns $\eta_{I,t}$, and $G_t=M_{m_t^*}J_t$. Both are supported in the fixed log annulus $\mathcal L=[\log H,\log M]$.

Write $C_0,C_\psi$ for the fixed convolution operators whose kernels in the conventions of [post-R15](operator-post-r15-stationary-tail.md) are the inverse integrals $\int e^{i\xi(x-y)}a(\xi)\,d\xi$, for $a(\xi)=1/(1+\xi^2)$ and $a(\xi)=\Re\psi(3/4+i\xi/2)/(1+\xi^2)$, respectively. In particular $C_0$ has kernel $\pi e^{-|x-y|}$. Define the slow matrix functions

$$
 V_t=G_t^* C_0G_t,\qquad
 A_t=(\log t-\log\pi)V_t+G_t^*C_\psi G_t,\qquad
 b_N=\sum_{p\mid N}\frac{\log p}{p-1}.
 \tag{8}
$$

By the exact post-R15 comparison and translation invariance of the convolution under $x\mapsto x+\log(Q/N)$, for each even $N$ one has

$$
 \|B_N^{h,h}-(A_N-b_NV_N)\|_{\rm HS}\ll_\kappa E_\kappa.
 \tag{9}
$$

For a compression to just a dyad beginning at $V$, (9) holds with $H$ replaced by $V$ in $E_\kappa$, since the entire corresponding physical region has lower endpoint at least $V/2$. If one of $u,v$ is $f$, R74 (8) bounds the additional HS error from replacing the exact $B_N^{u,v}$ by $B_N^{h,h}$ by $\mathcal B_{\rm HS}$. This is the actual terminal-mask comparison, not a change to the odd-prime Gram.

Uniformly on the polynomial reference annulus,
$\left|\partial_t\log m_t^*(x)\right|\ll_\Gamma (QL)^{-1}$
by differentiating the displayed formula and using $\log(Qe^x)\ll_\Gamma L$. The logarithmic derivative of each normalizer in (7) is bounded by the same order. Since the columns are disjointly supported, it follows that $\|G_t\|_{\rm op}\ll_\Gamma1$ and $\|\partial_tG_t\|_{\rm op}\ll_\Gamma(QL)^{-1}$. The symbols of both fixed convolutions are bounded and $L^2$, the second because the digamma has logarithmic growth on the displayed vertical line. Their kernels are $L^2$ by Plancherel. Each convolution restricted to $\mathcal L\times\mathcal L$ therefore has HS norm $O_\Gamma(\sqrt L)$, by integrating its squared kernel along one coordinate first. The ideal property and differentiation give

$$
 \begin{split}
 &\|V_t\|_{\rm HS}+QL\|\partial_tV_t\|_{\rm HS}\ll_\Gamma\sqrt L,\\
 &\|A_t\|_{\rm HS}\ll_\Gamma L^{3/2},\qquad
                 Q\|\partial_tA_t\|_{\rm HS}\ll_\Gamma\sqrt L.
 \end{split}
 \tag{10}
$$

In operator norm the corresponding bounds are $O_\Gamma(1)$ for $V_t$, $O_\Gamma((QL)^{-1})$ for its derivative, $O_\Gamma(L)$ for $A_t$, and $O_\Gamma(Q^{-1})$ for its derivative. This uses the bounded convolution multipliers. No factor involving the number of parents enters these bounds.

## 3. All complementary modes of the exact benchmark

For a Hilbert-valued sequence $X_m$ on the complete index interval, let $K_X=\sup_m\|X_m\|+\sum_{m<m_0+J-1}\|X_{m+1}-X_m\|$, with sums starting at $m_0$. For real $\theta$ summation by parts against the geometric progression gives

$$
 \left\|J^{-1}\sum_m X_m e(-\theta(m-m_0))\right\|
 \ll \frac{K_X}{1+J\operatorname{dist}(\theta,\mathbb Z)} .
 \tag{11}
$$

For a fixed rational center $a/b$, apply (11) with $\theta=j/J-a/b$ and sum its square over circular index distances $>R$ to get an $\ell^2$ bound $O(K_X(1+R)^{-1/2})$. This step holds for nonintegral centers without altering the endpoints of the actual modulus shell.

The even indexing makes $b_{2m}=\log2+\sum_{p>2,\ p\mid m}\log p/(p-1)$. Its part with $p>B_0$ is at most $O(L/B_0)$ pointwise, since $\sum_{p\mid 2m}\log p\le\log(2m)$. For the part with $p\le B_0$ use
$\mathbf1_{p\mid m}=p^{-1}\sum_{a=0}^{p-1}e(am/p)$.
By (10), $K_X=O(L^{3/2})$ for $X_m=A_{2m}$ and $O(\sqrt L)$ for $X_m=V_{2m}$. Apply (11) on the complement to each displayed prime mode and use the triangle inequality in $\ell^2(\mathrm{HS})$. The sum of their absolute scalar coefficients is at most $O(\log(2 B_0))=O(L)$: this is $\sum_{p\le B_0}\log p/(p-1)$ and follows from the Chebyshev bound $\sum_{p\le x}\log p\ll x$ by partial summation. The constant at $2$ and the slow field $A$ use the center $0/1$. Thus all these small-prime contributions together cost $O(L^{3/2}(1+R)^{-1/2})$. For the large-prime contribution the pointwise HS bound is $O(L^{3/2}/B_0)$, and normalized Fourier Parseval gives this bound on its entire Fourier field, as it also gives $O(E_\kappa+\iota\mathcal B_{\rm HS})$ for the exact comparison errors in (9). This proves (2) with the stated scope. The example uses $\kappa=1/4$, $E_\kappa=O_\epsilon(Q^{-1/10+\epsilon})$, $\mathcal B_{\rm HS}=O_\epsilon(Q^{-1/50+\epsilon})$ from R74, and $R^{-1/2}=Q^{-3/80}$.

## 4. The true retained test and its prime-modulus coefficients

Choose the highest full reference dyad $[V,2V]\subset[H,M]$, so $V\asymp M$ for the parameters of (4). Let $\mathbf v_Q$ have components $(\int_Iw_Q(z)\,dz)^{1/2}$ on that entire dyad and zero elsewhere, and normalize it. It is in the range of $\Pi$ because on each of its macro groups it is proportional to the exact retained vector; it is not a test chosen after selecting a frequency. At $t=Q$, the function $J_Q\mathbf v_Q$ is proportional to $\mathbf1_{[\log V,\log(2V)]}(x)e^{-x}m_Q^*(x)$, normalized in $L^2(dx)$. On this fixed log-length interval $m_Q^*\asymp_\Gamma1$, and the normalized test is pointwise bounded above and below by positive constants on the interval. Since the kernel of $C_0$ there is at least $\pi/2$, the explicit number

$$
 \gamma_Q=\langle\mathbf v_Q,V_Q\mathbf v_Q\rangle
 \tag{12}
$$

is bounded above and below by absolute positive constants for these parameters. Write $v_t=\langle\mathbf v_Q,V_t\mathbf v_Q\rangle$ and $g_t=\langle\mathbf v_Q,A_t\mathbf v_Q\rangle$. By (10) in operator norm, $v_t=\gamma_Q+O(L^{-1})$, $|v_t'|\ll(QL)^{-1}$, $|g_t|\ll L$, and $|g_t'|\ll Q^{-1}$. In (9) on this dyad use $\kappa=3/10$ and $H$ replaced by $V\asymp Q^{3/5}$; its error is $O_\epsilon(Q^{-9/50+\epsilon})$.

Fix $p\le Q^{3/40}$ and $1\le a<p$. We first compute the coefficient of the exact benchmark at a frequency $\vartheta$ with circular $|\vartheta-a/p|\le 1/(2J)$, using the phase $e(-\vartheta(m-m_0))$. In the prime sum in $b_{2m}$ retain primes $q\le Q^{1/3}$ first. Each reduced center $c/q$ other than $a/p$, including the constant center, has distance from $a/p$ at least $1/(pq)$; for $Q$ large this distance still exceeds $1/(2pq)$ after detuning. With $X_m=v_{2m}$, (11) bounds each nonmatching component by $O(pq/J)$. The coefficients for any one prime sum to $\log q/(q-1)$ in absolute value, so the bound after summing nonmatching primes is $O(pQ^{1/3}/J)$ by the Chebyshev bound. The constant term has cost $O(p/J)$. The full omitted prime tail has size $O(LQ^{-1/3})$. By (11) for $X_m=g_{2m}$, the slow part at this frequency costs $O(Lp/J)$, since $a/p$ is at least $1/p$ from zero modulo one. These additive errors, plus the exact comparison error $O_\epsilon(Q^{-9/50+\epsilon})$, are $O_\epsilon(Q^{-9/50+\epsilon})$ in total.

The matching prime term in $-b_{2m}v_{2m}$ is exactly

$$
 -\frac{\log p}{p(p-1)}\, e(a m_0/p)
       J^{-1}\sum_{r=0}^{J-1}
          v_{2(m_0+r)}e(-(\vartheta-a/p)r).
$$

In this term alone replace $v_{2(m_0+r)}$ by $\gamma_Q$; the cost is $O((\log p)/(p(p-1)L))$. Keeping this replacement inside the resonant term is what permits a uniform *relative* estimate for polynomially growing $p$. For $\vartheta=j/J$ this proves the right side of (4) first for the benchmark, with error before the prime replacement $O_\epsilon(Q^{-9/50+\epsilon})$. The main factor satisfies $|{\cal D}_J(j/J-a/p)|\ge2/\pi$ from the geometric formula $|\sin(\pi r)|/(J|\sin(\pi r/J)|)$ for $r=j-Ja/p$, with the continuous value $1$ at $0$. For $\vartheta=a/p$, using the phase $e(-am/p)$ instead removes $e(a m_0/p)$ and sets ${\cal D}_J=1$.

On the actual signed matrix $T^{h,h}$, [R73](r73-operator-rational-modulus-collars.md) (2) bounds its coefficient at the nearest integer mode by $O_\epsilon(Q^\epsilon\sqrt{pM/Q})$, since the detuning is at most $1/2$. It gives the same bound for the exact rational test: apply the smooth rational-weight estimate R73 (4) to its shell cutoff with no detuning, and restore the same $O(\sqrt{pQM})$ endpoint strip by the pointwise envelope, just as in R73 §4. In either case the bound is $O_\epsilon(Q^{-13/80+\epsilon})$. Thus $P=T+B$ has the stated coefficients. Indeed $\log p/[p(p-1)]\gg Q^{-3/20}$ on the chosen prime range, so after division the arithmetic error is $O_\epsilon(Q^{-1/80+\epsilon})$ and the stationary error is smaller. This proves (4) and (5) with all matching benchmark terms intact.

For (6), let $\alpha_p=J^{-1}\#\{m:p\mid m\}=1/p+O(J^{-1})$, and let $\mathbb E$ denote the actual complete-shell mean. Orthogonality gives

$$
 \begin{split}
 \alpha_p(1-\alpha_p)
       \big(\mathbb E[F\mid p\mid m]-\mathbb E[F\mid p\nmid m]\big)
 &=\mathbb E[\mathbf1_{p\mid m}F]-\alpha_p\mathbb E F\\
 &=p^{-1}\sum_{a=1}^{p-1}\mathbb E[e(-am/p)F]
                    +(p^{-1}-\alpha_p)\mathbb E F .
 \end{split}
 \tag{13}
$$

The pointwise positive Gram bound in R74 §3 gives $|\mathbb E F|\ll L^5$. The correction $O(L^5/J)$ on the right in (13), after division by $\alpha_p(1-\alpha_p)\asymp1/p$, is smaller than the error in (6), uniformly over the prime range. Substituting (5) and using $\alpha_p(1-\alpha_p)=(p-1)p^{-2}(1+O(p/J))$ proves (6), since $p\mid m$ and $p\mid N$ are equivalent for odd $p$.

## 5. What remains

The nonzero peak (4), for example at the integer nearest $J/3$, shows that uncentered positive prime-Gram energy at high ordinary frequencies does not tend to zero even on one fixed true retained exterior direction. The peak is accounted for by the exact deterministic arithmetic term, not an obstruction to cancellation in the signed $T$.

Conversely for every fixed $\Pi$, (2) and the triangle inequality show that the difference between the off-collar RMS of $\Pi\widehat T^{u,v}\Pi$ and that of $\Pi\widehat P^{u,v}\Pi$ is at most the right side of (2). At the indicated parameters the collar part of the former is already $O_\epsilon(Q^{-1/80+\epsilon})$ by R73 (3), and the nonretained spatial and mixed directions are estimated separately by R74. Thus after their respective proved errors, the remaining mean-square question is the off-collar energy of the actual positive odd-prime Gram on the fixed retained spatial macro directions (or the corresponding mixed Gram). Neither (2) nor the prime peaks estimate that energy. In particular ordinary-modulus mean square of the full retained signed matrix is still unproved.
