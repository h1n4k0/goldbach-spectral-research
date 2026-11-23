# A true second moment for sparse signed aliases of the surviving means

**Scope.** This is a modulus mean square of a genuinely occurring signed piece of the literal mesowindow-mean matrix. It allows any bounded number of nonzero alias indices, chosen separately at each modulus, and keeps the exact continuous model on those same indices. It does not control all aliases simultaneously or bound the full mean–mean block at any prescribed modulus.

## Statement

Use the reference partition of [R60](r60-operator-localized-coarse-contrast-annulus.md) with $1\le D\le H<M\le Q^\Gamma$ for a fixed $0<\Gamma<1$. In the physical realization at each even $N$, let $I_N=(Q/N)I$, and use the genuine normalised mean $e_{I,N}=r_N\mathbf1_{I_N}/\|r_N\mathbf1_{I_N}\|_2$ for every reference window $I$. Let $\mathcal A\subset[Q,2Q]$ consist of $J\ge1$ distinct even moduli. Assume original local Dirichlet GRH at all $N\in\mathcal A$, and auxiliary Dirichlet GRH for every modulus $q\le\lceil20\sqrt{QM}\rceil$, including $q=1$. No modulus-interval or density condition is imposed.

For a set $\mathcal K\subset\{1,\ldots,\lfloor4M\rfloor\}$, let $C_N(\mathcal K)$ be the actual matrix on the indexed means with only alias indices $k\in\mathcal K$ kept. On each kept $k$ take both difference lines and the reflected-sum line, with signs $+,+,-$, the real unit-restricted $\Lambda$ atom weights, and the corresponding signed continuous model with $\mathfrak S(kN)$. In particular this is not a Gram in which the equality line, proper powers, or opposite residues have been silently changed. Then for every integer $K\ge1$,

$$
 \left(\frac1J\sum_{N\in\mathcal A}
         \max_{|\mathcal K|\le K}\|C_N(\mathcal K)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon}Q^\epsilon
       \left[\sqrt{\frac KJ}(QM)^{1/4}
                    +\frac K{\sqrt{QH}}\right].
 \tag{1}
$$

For $H=Q^{2/5},\ M=Q^{3/5},\ D=Q^{8/25},\ K=\lfloor Q^{9/50}\rfloor$, and $J\gg Q^{99/100}$, this is $O_\epsilon(Q^{-1/200+\epsilon})$. Without requiring the lower bound on $J$, at most $O_\epsilon(Q^{197/200+\epsilon})$ selected moduli can satisfy $\max_{|\mathcal K|\le K}\|C_N(\mathcal K)\|_{\rm HS}>Q^{-1/400}$. Here the spatial parameters are exactly the [R60](r60-operator-localized-coarse-contrast-annulus.md) and [R62](r62-operator-full-mixed-contrast-deletion.md) example, but the auxiliary GRH range is broader. The bound includes $1\le k\le K$, or any other selection of at most $K$ indices in the full range, and is not an estimate of the untruncated matrix.

## 1. The exact moving means retain the raw prefix

For a window $I$ in the dyadic piece $[V,2V]$, its exact [R63](r63-operator-signed-window-mean-modulus-average.md) raw test profile is

$$
 h_{I,t}(x)=\frac{\sqrt{2\pi x}}{Q}
       \frac{\int_{I,\;z\ge x/Q} w_t(z)\,dz}
            {(\int_I w_t(z)\,dz)^{1/2}},
 \qquad
 w_t(z)=z^{-3}\big((Qz)^{-2/\log t}+(Qz)^{-1/4}\big),
 \quad Q\le t\le2Q .
 \tag{2}
$$

It is extended by zero at $x\le0$. At $t=N$ it is the genuine raw weight of $e_{I,N}$ by the exact $z=Nu/Q$ substitution, including the square-root prefix below $QI$. It vanishes above $2QV$. We will also need the signed scalar profile $\widetilde h_{I,t}=Q\partial_t h_{I,t}$; there is no derivative in the raw variable when taking $\partial_t$.

Write $Z=QV,\ b_V=\sqrt D/(\sqrt Q V),\ \omega_V=\sqrt{D/V}$. Both profiles $h_{I,t},\widetilde h_{I,t}$ are of the form

$$
 h(x)=\frac{\omega_V}{Z}\sqrt x\int_{QI}\mathbf1_{x\le w}\,d\mu(w),
 \qquad \|\mu\|_{\rm TV}\ll_\Gamma1 ,
 \tag{3}
$$

for finite signed real measures depending on the interval and $t$. Indeed the measure in $z=w/Q$ for the first is a constant times $V^{3/2}D^{-1/2}w_t(z)dz/(\int_I w_t)^{1/2}$; its mass is $O(\sqrt{\ell_I/D})$ for $\ell_I=|I|\le D$, since $w_t\asymp_\Gamma V^{-3}$. For the second, differentiate this density: $Q|\partial_t w_t(z)|\ll_\Gamma w_t(z)$, so the differentiated measure has the same TV bound. Both $h$'s are absolutely continuous, but the representation (3) also makes the endpoint cutoff harmless for TV estimates. In particular $\|h\|_\infty+\mathrm{TV}(h)\ll b_V$, $\|h\|_2\ll\omega_V$, and $|h(x)|\ll b_V\sqrt{x/(QV)}$. The logarithmic constants are uniform across the short last windows and over $t$.

For either such profile define

$$
 A_h(\alpha)=\sum_{n\ge1}\Lambda(n)h(n)e(n\alpha),\qquad
 B_h(\beta)=\int_{\mathbb R}h(x)e(x\beta)\,dx,\quad e(s)=e^{2\pi i s}.
$$

The elementary estimates are

$$
 \|A_h\|_{L^2(\mathbb R/\mathbb Z)}\ll L^{1/2}\omega_V,\quad
 \|B_h\|_{L^2(\mathbb R)}\ll\omega_V,\quad
 |B_h(\beta)|\ll b_V\min(QV,|\beta|^{-1}),
 \tag{4}
$$

where $L=\log Q$. The first follows from the Chebyshev bound for $\sum_{n\le2QV}\Lambda(n)^2$ and $b_V^2 QV=D/V$; the others follow by Plancherel and bounded variation.

## 2. Weighted GRH arc bounds with the correct mean factor

For an active window pair $I,I'$ of dyadic scales $V\le U$ use $X=QU$ and $P=\lfloor\sqrt X/10\rfloor$. The major arcs around reduced $a/q$, $q\le P$, have radius $\delta_q=2P/(qX)$; they are disjoint. On the complementary symmetric set, Dirichlet approximation gives $P<q\le20\sqrt X$ and $|\beta|\le2P/(qX)$ in $\alpha=a/q+\beta$. Thus the stated auxiliary cap suffices uniformly.

For any involved $q$, let $F_r(x)=\psi(x;q,r)-x/\phi(q)$ for unit residues $r$, zero for nonunits, and zero for $x\le0$. The two [R59](r59-operator-balanced-arcs-cuberoot-prefix.md) GRH bounds are

$$
 \sum_r|F_r(x)|^2\ll xL^4,\qquad
 \int_{y}^{2y}\sum_r|F_r(x+\ell)-F_r(x)|^2dx
 \ll y\ell L^4\quad(1\le \ell\le y,\ y\ge2)
 \tag{5}
$$

in the relevant polynomial ranges. The latter is the locally justified Selberg–Prachar estimate, not a mean over $q$. For the centered signed measures $\nu_r=h\,dF_r$, the analogue of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md)'s weighted estimate is

$$
 \int_{\mathbb R}\sum_r|\nu_r((x,x+\ell])|^2dx
           \ll \omega_V^2\,\ell L^4\quad(\ell\ge2).
 \tag{6}
$$

Here is a verification for these scalar mean profiles. By (3) and Minkowski it suffices for each $w\in QI$ to bound the squared integral of the residue vector of $\int_{(x,x+\ell]\cap(0,w]}\sqrt t\,dF_r(t)$ by $O(Z^2\ell L^4)$ before multiplying by $\omega_V^2/Z^2$. Abel and (5) pointwise bound the vector of any such increment with right edge $b$ by $O(bL^2)$. If $\ell>Z$, use this with $b\le2Z$ on a set of $x$-length $O(\ell)$. Otherwise, windows with $-\ell\le x<\ell$ cost $O(\ell^3 L^4)$, and windows crossing $w$ have $x$-length at most $\ell$, costing $O(Z^2\ell L^4)$. For the remaining nonempty windows $\ell\le x,\ x+\ell\le w$, write the weighted increment as the ordinary one times $\sqrt{x+\ell}$, minus the Abel integral of $(F_r(t)-F_r(x))/(2\sqrt t)$. Integrate the leading square using (5) on dyads starting at $\ell$, which sum geometrically to $O(Z^2\ell L^4)$. The Abel integral has residue-vector norm $O(\ell L^2)$ pointwise by (5), hence squared integral $O(Z\ell^2 L^4)$, also admissible. This proves (6) for the original or differentiated profile. Convolving $\nu_r$ with the length-$\ell$ indicator and applying real-line Plancherel gives

$$
 \sum_r\int_{-\delta}^{\delta}|\widehat\nu_r(\beta)|^2\,d\beta
 \ll \omega_V^2 L^4/\ell\qquad(\delta\ell\le1/4).
 \tag{7}
$$

At a rational displacement put $A_h=M_h+E_h+Z_h$ with

$$
 M_h=\frac{\mu(q)}{\phi(q)}B_h(\beta),\qquad
 E_h=\sum_r e(ar/q)\widehat\nu_r(\beta).
$$

The nonunit term $Z_h$ has supremum $O(b_V L^2)$ because the total $\Lambda$ mass of powers of primes dividing $q$ is $O(L^2)$. Abel gives $\widehat\nu_r=-\widehat{h'F_r}-2\pi i\beta\widehat{hF_r}$. From (3), (5) and Plancherel, uniformly in $t$,

$$
 \begin{split}
 \sup_\beta\sum_r|\widehat{h'F_r}(\beta)|^2&\ll \omega_V^2 L^4,\\
 \sup_\beta\sum_r|\widehat{hF_r}(\beta)|^2&\ll \omega_V^2 (QV)^2 L^4,\\
 \sum_r\int_{\mathbb R}|\widehat{hF_r}(\beta)|^2d\beta&\ll\omega_V^2(QV)L^4 .
 \end{split}
 \tag{8}
$$

For the first, interchange the scalar cutoff superposition (3) and the integral: the weight derivative consists of $1/(2\sqrt x)$ times a bounded cumulative plus cutoff contributions of mass at most a constant against $\sqrt x$. Multiplying by the residue norm $O(\sqrt x L^2)$ bounds the integrated vector by $O(\omega_V L^2)$. The second follows by integrating $|h(x)|\sqrt x\ll\omega_V x/(QV)$ over its support; the third follows by squaring this pointwise integrand and integrating. These arguments apply with the signed differentiated measure as well. In particular

$$
 |E_h(a,\beta)|\ll \omega_V\sqrt q\,(1+|\beta|QV)L^2 .
 \tag{9}
$$

On the minor arcs, $QV\le X$, $|\beta|X\le2$, and $q\asymp\sqrt X$. The main and nonunit terms are smaller than $Q^\epsilon\omega_V X^{1/4}$ by (4), so this bounds the minor supremum of $A_h$. On the majors, (7) with $\ell=qX/(8P)$ and finite additive Parseval over $a$ show that the integrated squared $E_h$ mass on the reduced $q$-arcs is $O(\omega_V^2 L^4 P/X)$. Use (9) on the other leg and $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$ for the double-error product. Combining with the minor bound and (4) yields for both the minor product and the double major error

$$
 \|\text{product}\|_{L^2(\mathbb T)}
     \ll_\epsilon Q^\epsilon X^{1/4}\omega_V\omega_U .
 \tag{10}
$$

For the single major errors, use the [R54](r54-operator-asymmetric-crossing.md) and [R59](r59-operator-balanced-arcs-cuberoot-prefix.md) weighted argument: apply Parseval in $a$, take the first of (8) with $\|B_h\|_2$ from the other leg, and the last of (8) with $\sup_\beta|\beta B_h(\beta)|\ll b_V$ or $b_U$ from the other leg. Summing $q/\phi(q)^2\ll_\epsilon Q^\epsilon$ gives total $L^2$ norm

$$
 \ll_\epsilon Q^\epsilon\omega_V\omega_U \sqrt{1+U/V}.
 \tag{11}
$$

The symmetric arc set makes the same bounds valid with either Fourier argument negative. Equations (10) and (11) continue to hold with either one of the profiles replaced by $Q\partial_t$ of that original profile. Since $1\le V\le U\le M\le Q^\Gamma$, the factor $\sqrt{1+U/V}$ in (11) is $O(X^{1/4})$.

## 3. Sampling the exact moving profiles and restoring the model

For one pair and one alias orientation $(\varepsilon_1,\varepsilon_2)=(-,+),(+,-),(+,+)$, let $c_s(t)$ be the Fourier coefficients of one of the products just estimated, using the exact $h_{I,t},h_{I',t}$ on their fixed pair-specific arcs. The product is continuously differentiable as an $L^2$ function of $t$ (for fixed $Q$ the prime sums are finite, continuum weights have bounded support, and all restrictions here are fixed in $t$). Differentiation either differentiates one profile or the other, including principal-density and error profiles; these operations commute with the fixed arc masks. Thus (10) and (11), with Parseval, give uniformly

$$
 \|c(t)\|_{\ell^2}+Q\|\partial_t c(t)\|_{\ell^2}
     \ll_\epsilon Q^\epsilon X^{1/4}\omega_V\omega_U .
 \tag{12}
$$

The t-norm bound on derivatives is why the literal $N$-dependent mean directions can be used without an absolute-value cost from approximating their operators.

For fixed coefficients $c_s$, put $N=2n$, and allow an arbitrary chosen set $\mathcal K_N$ for each selected $N$, of size at most $K$. At each window pair restrict it further to $k\le4U$; both the full arithmetic and continuous line weights are exactly zero beyond that support threshold for **every** $t$ and actual $N$. Cauchy in $k$ and the divisor bound for the number of representations of $s=2kn\le8QU\cdot2$ give

$$
 \sum_{N\in\mathcal A}\left|
       \sum_{k\in\mathcal K_N,\ k\le4U}c_{kN}\right|^2
 \ll_\epsilon KQ^\epsilon\sum_s|c_s|^2 .
 \tag{13}
$$

The estimate applies to any further subset of the selected $N$, with no loss of normalisation. For $c_{kN}(N)$ use the exact fundamental theorem of calculus

$$
 c_{kN}(N)=c_{kN}(Q)+\int_Q^{2Q}\mathbf1_{t\le N}\partial_t c_{kN}(t)\,dt.
$$

Apply (13) to the first term and to the selected $N\ge t$ for each integrand, then use Minkowski and (12) (the derivative's $1/Q$ is canceled by the integration length). After dividing the square sum by $J$, the RMS per pair from all sampled products is

$$
 \ll_\epsilon Q^\epsilon\sqrt{K/J}\,X^{1/4}\omega_V\omega_U .
 \tag{14}
$$

This works for arbitrary N-dependent selections of the aliases, even when the subset of moduli changes under the integral. It does not use a frozen weight approximation or an ordinary interval of moduli.

We next bound the unsampled errors. Original nonunits at $N$ can be removed and restored at per-pair cost $O(L^{O(1)}K b_Vb_U)$: each leg has $O(L^2)$ total $\Lambda$ mass on powers of bases dividing $N$, and each of its integers has at most one corresponding partner per orientation and each kept $k$, of mark $O(L)$. No proper powers of admissible bases are omitted. The major-arc nonunits $Z_h$ at $q$ cost $O(L^{O(1)}K (b_V\omega_U+b_U\omega_V))$ per pair by Cauchy against (4); the double $Z_h$ term is no larger. These are uniform in the actual $t=N$.

In the principal-density product on the major arcs at $s=kN$, replace the $\beta$-integrals by the full line and extend the Ramanujan series from $q\le P$ to $q\ge1$. The tail beyond $\delta_q$ in the two Fourier factors has integral $O(b_Vb_U/\delta_q)=O(qD/(PV))$ by (4). The full integral equals the continuous tensor on the exact affine line and is $O(D/U)$ by support and the sup weights. The [R59](r59-operator-balanced-arcs-cuberoot-prefix.md) absolute bounds $\sum_{q\le P}q|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon$, and $\sum_{q>P}\mu(q)^2|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon/P$, apply uniformly to these polynomial $s$; $c_q$ in this sentence is the Ramanujan sum. The extended series equals $\mathfrak S(kN)$ since $N$ is even. Fourier inversion matches the exact three line parametrisations, with the original signs. Thus the total model error per pair is

$$
 \ll_\epsilon Q^\epsilon \frac{KD}{P}(1/V+1/U).
$$

No equality line is inserted, and all $t$-dependence in these pointwise bounds is evaluated at the actual $N$.

## 4. Aggregate and take the genuine maximum

There are $O(V/D)$ and $O(U/D)$ window means in the two dyads, respectively, with disjoint physical supports at each $N$. Aggregate the squared HS entries and then the modulus mean, so the uniform per-pair estimates are multiplied by $O(\sqrt{VU}/D)=O((\omega_V\omega_U)^{-1})$. This cancels the geometric factor in (14) and leaves $O_\epsilon(Q^\epsilon\sqrt{K/J}(QU)^{1/4})$. The pointwise unit and model terms after aggregation are at most $O_\epsilon(Q^\epsilon K/\sqrt{QH})$, since $P\asymp\sqrt{QU}$, $V,U\ge H$, $b_V=\omega_V/\sqrt{QV}$, and similarly for $U$. Sum over the $O(L^2)$ dyad pairs and three orientations to prove (1) for any fixed choice of the family $(\mathcal K_N)_{N\in\mathcal A}$, with constant independent of that family. Choosing a maximizing set of size at most $K$ at each $N$ proves the actual maximum assertion.

In the printed example the sampled exponent is $9/100+2/5-99/200=-1/200$; the pointwise term is smaller. With no lower bound on $J$, (13) without division gives the unnormalised squared mass of the sampled errors $\ll_\epsilon Q^\epsilon K(QM)^{1/2}$. The pointwise errors are uniformly $o(Q^{-1/400})$, hence Chebyshev gives the stated $197/200$ exception exponent before $\epsilon$. This genuine second moment is only for the sparse-alias contribution. At $U\asymp M$, replacing $K$ by the complete alias count $O(M)$ returns the same cube-root sampling constraint as [R59](r59-operator-balanced-arcs-cuberoot-prefix.md); no cancellation between all the remaining shifts is established. This leaves the full mean–mean variance, prescribed-modulus control, and weak S open.
