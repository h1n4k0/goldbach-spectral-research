# Dense low-coordinate aliases can be removed from the surviving means

**Scope.** This is a modulus mean square for a genuine dense piece of the literal exterior window-mean matrix. It can keep **all** alias indices; the saving is from the raw-coordinate position and the true mean's square-root Volterra prefix, not from taking only a thin alias family. The unit-restricted von Mangoldt weights, all three signs and the exact continuous model are matched on the same cut. It leaves a fully exterior dense covariance, not a full mean–mean estimate or an individual-modulus result.

## Statement and definition of the cut

Use the reference partition and literal weighted unit means of [R60](r60-operator-localized-coarse-contrast-annulus.md) and [R63](r63-operator-signed-window-mean-modulus-average.md), with $1\le D\le H<M\le Q^\Gamma$, where $0<\Gamma<1$ is fixed. Let $\mathcal A\subset[Q,2Q]$ consist of $J\ge1$ distinct even integers, with original local Dirichlet GRH at every selected $N$. In an entry indexed by reference windows $I,I'$ lying in dyads starting at $V,U$, the raw arguments of their exact weights are denoted by $x,y$, respectively; the weights are supported in $[0,Q M]$. Fix $0<\rho\le1$, with $\rho H\ge1$, and define $C_N^{\rm either}(\rho)$ by retaining only the part of this entry with

$$
             x/Q\le\rho V\quad\text{or}\quad y/Q\le\rho U .
$$

Define $C_N^{\rm both}(\rho)$ by requiring both inequalities. These restrictions act on both the integer points and the Lebesgue model on each affine line, with the exact signs $+,+,-$ and no equality line. There may also be any further restriction of alias indices, chosen independently for each $N$, applied to the integer and model terms together.

Assume auxiliary Dirichlet GRH for every integer modulus $q\le \lceil20\sqrt{Q\rho M}\rceil$, including $q=1$. Then for every $\epsilon>0$,

$$
 \begin{split}
 \left(\operatorname{Avg}_{\mathcal A}\|C_N^{\rm either}(\rho)\|_{\rm HS}^2\right)^{1/2}
 &\ll_{\Gamma,\epsilon} Q^\epsilon\left[
      \rho^{5/4}\frac{Q^{1/4}M^{3/4}}{\sqrt J}
      +\sqrt\rho\,\frac{M}{\sqrt{JH}}
      +\sqrt\rho\,\frac{M}{\sqrt{QH}}
      +\frac{\sqrt M}{H}\right],\\
 \left(\operatorname{Avg}_{\mathcal A}\|C_N^{\rm both}(\rho)\|_{\rm HS}^2\right)^{1/2}
 &\ll_{\Gamma,\epsilon} Q^\epsilon\left[
      \rho^{11/4}\frac{Q^{1/4}M^{3/4}}{\sqrt J}
      +\rho^{5/2}\frac{M}{\sqrt{JH}}
      +\rho^{5/2}\frac{M}{\sqrt{QH}}
      +\frac{\sqrt M}{H}\right].
 \end{split}                                                     \tag{1}
$$

One may impose additional fixed raw-coordinate interval cuts in each leg, without changing these bounds. Those cuts can depend on the reference dyad pair, but are fixed in the raw coordinates as $N$ varies. The first three bounds come from raw dyads above one. The last is a pointwise origin bound. The auxiliary range for this theorem depends on the maximum allowed shorter raw coordinate, not on the entire outer radius.

For the [R60](r60-operator-localized-coarse-contrast-annulus.md) example $H=Q^{2/5},M=Q^{3/5},D=Q^{8/25},J\gg Q^{99/100}$, take the **union** of the either-low region with $\rho=Q^{-17/100}$ and the both-low region with $\rho=Q^{-2/25}$. Its deleted contribution has HS RMS $O_\epsilon(Q^{-3/400+\epsilon})$. The union uses auxiliary moduli through $\lceil20Q^{19/25}\rceil$. With no lower bound on $J$, its exceptional count at threshold $Q^{-1/400}$ is $O_\epsilon(Q^{49/50+\epsilon})$ among the selected $N$ satisfying the stated hypotheses. Neither this count nor (1) settles any prescribed sparse set or the whole literal-mean variance.

## 1. Raw profiles and the extra ratio of masses

For $Q\le t\le2Q$, the exact normalised raw mean profile $h_{I,t}$ is the [R63](r63-operator-signed-window-mean-modulus-average.md) formula

$$
 h_{I,t}(x)=\frac{\sqrt{2\pi x}}Q
    \frac{\displaystyle\int_{I,\ z\ge x/Q}z^{-3}
                ((Qz)^{-2/\log t}+(Qz)^{-1/4})\,dz}
         {\displaystyle\left(\int_I z^{-3}
                ((Qz)^{-2/\log t}+(Qz)^{-1/4})\,dz\right)^{1/2}} .
 \tag{2}
$$

This is exactly the physical $r_N$-mean under $z=Nu/Q$ at $t=N$; [R63](r63-operator-signed-window-mean-modulus-average.md) gives the normalization and retains the raw square-root prefix. Write $\omega_V=\sqrt{D/V}$. As in [R64](r64-operator-sparse-alias-window-mean-variance.md), both $h_{I,t}$ and $Q\partial_t h_{I,t}$ admit the representation

$$
 h(x)=\frac{\omega_V}{QV}\sqrt{x}
                 \int_{QI}\mathbf1_{x\le s}\,d\mu_{I,t}(s),
 \qquad \|\mu_{I,t}\|_{\rm TV}=O_\Gamma(1)
 \tag{3}
$$

with finite signed measures. For the first one the total mass is $O(\sqrt{|I|/D})$; differentiating the normalized density in (2) preserves a bounded TV mass because $Q|\partial_t w_t(z)|\ll_\Gamma w_t(z)$, with $w_t$ the weight in its two integrals.

Partition the normalised raw coordinates $x/Q,y/Q>1$ into dyads with lower edges $v,w=1,2,4,\ldots$, clipping them at support and any cut endpoints. Use a consistent $(a,b]$ convention in each raw block. Fix one such pair and, if necessary, transpose so that $v\le w$; this does not impose $V\le U$. For a clipped leg inside $[Qv,2Qv]$, define

$$
 \lambda_v=v/V,\qquad a_v=\omega_V\lambda_v
$$

and analogously $\lambda_w,a_w=\omega_U\lambda_w$ on the other leg. The fixed raw restriction of (3) is a superposition of $\sqrt x\mathbf1_{(a,b]}$ with $Qv\le a\le b\le2Qv$. This includes the differentiated profile and any of the additional fixed interval cuts. It follows that

$$
 \|h\|_\infty+\mathrm{TV}(h)\ll \frac{a_v}{\sqrt{Qv}},\qquad
 \|A_h\|_{L^2(\mathbb T)}+\|B_h\|_{L^2(\mathbb R)}
       \ll L a_v,\qquad
 |B_h(\beta)|\ll \frac{a_v}{\sqrt{Qv}}\min(Qv,|\beta|^{-1}),
 \tag{4}
$$

where $A_h(\alpha)=\sum_n\Lambda(n)h(n)e(n\alpha)$, $B_h(\beta)=\int h(x)e(x\beta)\,dx$, and $e(s)=e^{2\pi i s}$. The $L^2$ statements follow by Parseval and the raw support length, using the trivial mark bound $O_\Gamma(L)$; the Fourier decay follows by BV integration. We only use nonempty raw intersections, so $\lambda_v,\lambda_w\le2$ and $v,w\le M$. Formula (4) improves the normalised mean mass by the raw ratio $\lambda_v$, not just its square root.

## 2. Use balanced arcs at the *shorter* raw scale

Set $X=Qv$, $P=\lfloor\sqrt X/10\rfloor$, and use the disjoint [R59](r59-operator-balanced-arcs-cuberoot-prefix.md) major arcs of radius $\delta_q=2P/(qX)$ at reduced $a/q$, $q\le P$. Off these arcs Dirichlet approximation gives $P<q\le20\sqrt X$, $|\beta|\le2P/(qX)$. We will use a supremum only on the shorter raw leg on the minors and for double errors, while the longer leg uses its integrated error. For the low regions in the statement, $v\le\rho M$ (if the cut is imposed on the longer leg, then $v\le w\le\rho M$ as well). This verifies the auxiliary cap.

Let $F_r(t)=\psi(t;q,r)-t/\phi(q)$ on reduced residues and zero otherwise. Use the pointwise residue vector bound $\sum_r|F_r(t)|^2\ll tL^4$ and the local short-interval bound of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md), $\int_z^{2z}\sum_r|F_r(t+\ell)-F_r(t)|^2dt\ll z\ell L^4$ for $1\le\ell\le z,\ z\ge2$ in these polynomial ranges. For $\nu_r=h\,dF_r$ on either leg, the corresponding weighted estimate is

$$
 \int_{\mathbb R}\sum_r|\nu_r((t,t+\ell])|^2dt
       \ll a_v^2\,\ell L^4 \qquad(\ell\ge2)
 \tag{5}
$$

on the $v$-leg, and the same with $w$ on its leg. To prove (5), use Minkowski and the superposition in (3). For one clipped elementary $\sqrt x$ weight in $[Qv,2Qv]$, the pointwise residue norm of an arbitrary interval integral of $\sqrt x\,dF_r$ is $O(QvL^2)$ by Abel and the pointwise bound. If $\ell>Qv$, nonempty windows occupy $O(\ell)$ total slide measure, giving the required squared bound $O((Qv)^2\ell L^4)$ before its coefficient in (3). If $\ell\le Qv$, windows crossing either interval endpoint have slide measure at most $2\ell$ and the same bound. In the interior, Abel expresses the increment as the ordinary residue increment times $\sqrt{t+\ell}$ minus the integral of $(F_r(x)-F_r(t))/(2\sqrt x)$. The first contribution is $O((Qv)^2\ell L^4)$ by the short-interval estimate on dyads at scale $Qv$; the second has pointwise norm $O(\ell L^2)$ and integration length $O(Qv)$. Multiply by the square of $\omega_V/(QV)$, sum the TV mass in (3), and obtain (5). No assumption comparing $\ell$ to the long leg is needed; its own two cases apply. Convolution by a length-$\ell$ indicator gives by Plancherel

$$
 \sum_r\int_{-\delta}^{\delta}|\widehat{\nu}_r(\beta)|^2d\beta
 \ll a_v^2 L^4/\ell,\qquad \delta\ell\le1/4 .
 \tag{6}
$$

At $a/q+\beta$, decompose $A_h=M_h+E_h+Z_h$ with $M_h=\mu(q)B_h(\beta)/\phi(q)$, $E_h=\sum_r e(ar/q)\widehat\nu_r(\beta)$, and $Z_h$ the nonunit prime-power term. It has supremum $O_\Gamma(L^2a_v/\sqrt{Qv})$. Abel summation using the pointwise vector GRH bound gives

$$
 |E_h(a,\beta)|\ll a_v\sqrt q\,(1+|\beta|Qv)L^2 .
 \tag{7}
$$

More precisely, the constant and $2\pi i\beta$ parts in $\widehat\nu_r$ have residue-vector Fourier supremum $O(a_vL^2)$ and $O(a_v Qv L^2)$, respectively; the $2\pi i\beta$ part before multiplication by $\beta$ also has squared $L^2(\mathbb R)$ norm $O(a_v^2 Qv L^4)$ by Plancherel. For the constant part, the raw cutoff endpoints simply give the two terms $\sqrt b F_r(b)$ and $\sqrt a F_r(a)$ for an elementary weight on $(a,b]$; the square-root derivative has the same integrated bound, by $\|F_r(x)\|_{\ell^2(r)}\ll\sqrt x L^2$. For the $\beta$-part, the bounds follow by integrating or squaring $|h(x)|\sqrt x$ over its support. This explicit endpoint convention justifies the use of BV cuts at genuine prime powers.

The shorter leg has $\sup_{\mathfrak m}|A_h|\ll Q^\epsilon a_v X^{1/4}$ by (4), (7) and $|\beta|Qv\le2$. Use the longer leg's ordinary $L^2$ norm in its product. For the double error on the majors take $\ell=qX/(8P)$ in (6) on the **longer** leg. Additive Parseval over $a\bmod q$ then bounds its integrated squared error on the $q$-arcs by $O(a_w^2 L^4 P/X)$. On the shorter leg use the pointwise square of (7), $O(a_v^2 q(1+P/q)^2L^4)$. Sum $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$. Hence both the minor product and major double-error product have $L^2(\mathbb T)$ norm

$$
                 \ll_\epsilon Q^\epsilon a_v a_w X^{1/4}.
 \tag{8}
$$

For single errors use the [R54](r54-operator-asymmetric-crossing.md) weighted argument: after additive Parseval over $a$, use the constant part's supremum with $\|B\|_2$, and the $\beta$-part's Plancherel bound with $\sup|\beta B_h|\ll a_v/\sqrt{Qv}$ on the $v$-leg (or the reversed estimate). Summing $q/\phi(q)^2$ gives $O_\epsilon(Q^\epsilon a_v a_w \sqrt{1+w/v})$. The estimates hold for both signs of either Fourier argument and for $Q\partial_t$ applied on one leg. In particular, choosing the shorter scale for the arcs does not introduce a larger minor or double-error loss from the longer raw support.

## 3. Sample all aliases; restore the original continuous model

For a fixed orientation, the raw sample indices are $s=kN$, $k\ge1$, with $O(w)$ possible aliases per modulus from $x,y\le2Qw$. As in [R64](r64-operator-sparse-alias-window-mean-variance.md), Cauchy in $k$ and divisor multiplicity imply $\sum_N|\sum_k c_{kN}|^2\ll_\epsilon wQ^\epsilon\|c\|_{\ell^2}^2$ for any fixed coefficient function, even with the additional modulus-dependent alias restriction in the statement. For the genuine moving profiles use $c_{kN}(N)=c_{kN}(Q)+\int_Q^{2Q}\mathbf1_{t\le N}\partial_t c_{kN}(t)\,dt$. The raw masks and arcs are fixed in $t$, and all the product estimates just proved hold with one normalized differentiated weight. Minkowski and sampling the subset $N\ge t$ give the same bounds as for fixed $t$. This explicitly uses the exact moving mean, not an approximate fixed raw mean.

Pointwise, one can remove the $N$-nonunit raw atoms at cost $O(L^{O(1)}w\,a_va_w/(Q\sqrt{vw}))$ per entry, counting $O(w)$ partners on the exact lines for each fixed nonunit prime power and bounding their total marks by logs. For the major nonunit terms $Z_h$, ordinary $L^2$ Cauchy in (4) gives cost $O(L^{O(1)}w\,a_va_w/\sqrt{Qv})$ after counting aliases. No admissible proper powers are removed. On the main major-arc contribution, the omitted $\beta$-integral per $q$ is at most $O(q\,a_va_w\sqrt{v/w}/P)$, by the two Fourier decays of (4) and $\delta_q=2P/(qQv)$; the full integral is at most $O(a_va_w\sqrt{v/w})$ by the shorter support length and the two sup weights. The absolute Ramanujan bounds of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md) now extend the integrals and the series at cost $O_\epsilon(Q^\epsilon w\,a_va_w\sqrt{v/w}/P)$. Fourier inversion restores the exact clipped continuous affine integral at that alias, and the full Ramanujan series is $\mathfrak S(kN)$; all signs are unchanged. Since $P\asymp\sqrt{Qv}$, this last error is also bounded by $O_\epsilon(Q^\epsilon w\,a_va_w/\sqrt{Qv})$.

There are $O(V/D)$ and $O(U/D)$ windows of the respective physical dyads. Summing squared HS entries over these windows multiplies the uniform entry bounds by $O(\sqrt{VU}/D)$, exactly canceling $\omega_V\omega_U$. Thus the RMS for this fixed raw dyad pair and physical dyad pair is bounded by

$$
 Q^\epsilon\lambda_v\lambda_w\left[
       \sqrt{\frac wJ}(Qv)^{1/4}
           +\frac w{\sqrt{Jv}}+\frac w{\sqrt{Qv}}\right].
 \tag{9}
$$

The last term is pointwise, while the first two use sampled square sums. Powers of $L$ and all $O(L^4)$ choices of physical and raw dyads can be absorbed in a fresh $Q^\epsilon$.

## 4. Origin, the two low regions, and the remaining core

For an origin part $x\le Q$ on one leg, use $|h_{I,N}(x)|\ll b_V \sqrt{x/(QV)}$, $b_V=\sqrt D/(\sqrt Q V)$, and $|h_{I',N}|\ll b_U$. On any affine line the actual partner at fixed $x$ is unique, and there are $O(U)$ possible integer shifts $k$ for this origin crossing since $U\ge1$. The absolute weighted atom-plus-model mass is at most $O_\epsilon(Q^\epsilon D/V^{3/2})$ per entry: bound the von Mangoldt marks by logarithms, each $x$-support by length $O(Q)$, the other leg by $b_U$, and the singular factors by $Q^\epsilon$. After HS aggregation this is $O_\epsilon(Q^\epsilon\sqrt U/V)$, uniformly in $N$, hence $O_\epsilon(Q^\epsilon\sqrt M/H)$; the other origin part is symmetric. This elementary edge step places no arithmetic hypothesis beyond identifying the operator. It also bounds additional restrictions of this edge.

On the either-low region above the edge, $\lambda_v\lambda_w\ll\rho$, $v\le\rho M$, and $w\le M$. Also $w\lambda_v\lambda_w/\sqrt v\ll M\sqrt\rho/\sqrt H$: if the shorter leg is truncated then $\lambda_v/\sqrt v=\sqrt{\lambda_v}/\sqrt V\le\sqrt\rho/\sqrt H$, while if the longer is truncated then $\lambda_w\le\rho$ and $\lambda_v/\sqrt v\ll H^{-1/2}$. In the both-low region one instead has $\lambda_v\lambda_w\le\rho^2$, $v,w\le\rho M$, and $w\lambda_v\lambda_w/\sqrt v\le M\rho^{5/2}/\sqrt H$. Split each relevant raw dyad at the exact cut endpoint and write the either-low union as two disjoint cut rectangles. Apply these bounds in (9), sum dyads, and add the edge to prove (1). The same proof applies to an additional fixed lower cut in a low rectangle; therefore form the example union by taking either-low first and then the part of both-low with both operands above the first cut.

In the example the leading powers are $1/4+3(3/5)/4-(99/100)/2-(5/4)(17/100)=-3/400$ and $1/4+3(3/5)/4-(99/100)/2-(11/4)(2/25)=-3/200$, respectively. The other terms are smaller. Without the lower bound on $J$, the unnormalised squared sample masses are bounded by $Q^\epsilon[\rho^{5/2}Q^{1/2}M^{3/2}+\rho M^2/H]$ for the first cut, and $Q^\epsilon[\rho^{11/2}Q^{1/2}M^{3/2}+\rho^5M^2/H]$ for the second. Their maximum exponent is $39/40$; all pointwise errors are $o(Q^{-1/400})$, so Chebyshev gives $49/50$ as stated.

With the separate [R64](r64-operator-sparse-alias-window-mean-variance.md) auxiliary range, one can also remove the $k\le Q^{9/50}$ part of this example, by applying the present proof with $k$ above that threshold and adding [R64](r64-operator-sparse-alias-window-mean-variance.md). What is left then has both raw legs above their either-low thresholds, at least one above its both-low threshold, and the full remaining dense range of high shift indices. The covariance there is not estimated here.
