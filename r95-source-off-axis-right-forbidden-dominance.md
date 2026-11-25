# One retained-long forbidden subrow dominates off the zero-floor axis

Retain the exact original divisor tests, carrier, true parities and normalizer of the [actual four-parity law](r89-source-four-actual-parity-phases.md). Let $0\le a,b\le A_0$ for a fixed finite $A_0$, and $Z_0\le Z\le X^{\delta_0}$ be the true split. In particular an ordered pair $n=hF,m=kG$ is actually selected with $n,m\in\mathcal J,\ n+m=N$, the squarefree unit and tag masks, and the literal distinguished-prime floors $F\ge\sqrt N e^{-aT_N}$, $G\ge\sqrt N e^{-bT_N}$. Use the literal integer cuts $d>D_N,e>D_N,de>Q_N$, where $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor,\ Q_N=\lfloor Ne^{-20T_N}\rfloor$, $T_N=\log N/\log\log N$. The parities are $\mu(h)=\varepsilon_1,\mu(k)=\varepsilon_2$, not the signs of the short labels. Use $\mathcal N_{N,Z}=\Sigma(N)B_{\mathcal J}(N)(\mathcal C_{X,Z}/|\mathcal J|)^2$ from the [axis row law](r94-source-genuine-axis-row-dominance.md).

**Theorem.** The seven genuine signed subrows of the [capped algebra](r85-source-capped-long-floor-orbits.md), as defined below, each have their own comparator $\mathcal N_{N,Z}$ times the indicated phase. The sum over even targets in $\mathcal X$ of the maximum squared comparator error is $O(X^3\ell^{-1/20})$, with a common maximum over all seven subrows and all independently target-adaptive $a,b,Z,\varepsilon_1,\varepsilon_2$.

If $A_0>25$, there is a fixed closed rectangle with nonempty interior, lying strictly inside $0<a<5/4,\ b>24,\ a,b<A_0$, with its right floors near $25$, on which exactly five of these subrows are active. All five have actual magnitude $\gg X$ on any fixed interior target subwindow, and the single **right-containing retained-long forbidden** subrow has absolute value greater than the **sum of the other four absolute values** by $\gg X$. The winning subrow has sign $-\varepsilon_1$. Also there is a fixed positive-left rectangle with $a+b<20$, right floors near the lower axis witness, on which the genuine ordinary subrow dominates in the same sense. All these actual comparisons hold simultaneously outside one $O(X\ell^{-1/20})$ even exceptional set on an interior target subwindow, with full-window strict comparisons outside $O(X\ell^{-1/60})$ even targets. This is an unconditional mean-square consequence for fixed boxes, not a per-target theorem for every even $N$, a growing-box assertion, or Hypothesis S.

## 1. The seven exact subrows, before any analytic comparison

On each selected pair use the old ordinary marks $u_h(r)=\mu(h)\mu(r)\log(Fr)$, $u_k(t)=\mu(k)\mu(t)\log(Gt)$ for $d=h/r,e=k/t$, and containing marks $-v_h(z),-v_k(w)$ for $Fz,Gw$, where $v_h(z)=\mu(z)\log(h/z)$ and similarly for $k$. The exact algebra with the original external minus on each pair is the following.

- $O$ is the ordinary–ordinary sum with all three original tests and mark $-u_h(r)u_k(t)$.
- $R_n,R_f$ hold the left ordinary $d>D_N$ and use the common mark $-u_h(r)v_k(w)$. In $R_n$ the right containing label is nonlong, $Gw\le D_N$. In $R_f$ it is retained long and forbidden by the product, $Gw>D_N,\ dGw\le Q_N$. The reflected rows $L_n,L_f$ hold the right ordinary long label and use $-v_h(z)u_k(t)$, with the corresponding left nonlong and left retained-long forbidden conditions.
- $D_f$ is the double-containing forbidden product with both labels retained long and $(Fz)(Gw)\le Q_N$, of mark $+v_h(z)v_k(w)$. $D_n$ uses both nonlong labels $Fz,Gw\le D_N$ and mark $-v_h(z)v_k(w)$.

All the parity projectors and exact original pair gates are applied to each subrow. The signs are not a new postulated decomposition. In a mixed orbit, the total containing sum is zero by $\sum_{z\mid h}\mu(z)\log(h/z)=\Lambda(h)=0$, and likewise for $k$, since the actual cofactors are composite. Thus the accepted $v$ sum is the negative of the two excluded sums. For a double orbit the uncurved long–long total is the product of the two nonlong residues by the same identity; subtracting the actual forbidden long product and including the external minus gives exactly $D_f+D_n$. This is the pairwise capped algebra, before any enlargement of prime windows. In particular $R_f,L_f,D_f$ use a weak forbidden product condition and a **strict** long condition; the literal integer equalities are not moved.

## 2. Separate phases and the common adaptive estimate

Write $P,Q,\Phi$ and $M$ for the exact signed Euler scalars and the primitive in the [Dickman theorem](r86-source-dickman-capped-phase-chart.md) and the four-parity law. In $Q(a,b)$ the containing arm is the *first* input. The split of that model into its two areas and the analogous double split will be denoted

$$
 \begin{split}
 q_n(a,b)&=M(a-20)M(b+20), &q_f(a,b)&=Q(a,b)-q_n(a,b),\\
 d_n(a,b)&=M(a-20)M(b-20), &d_f(a,b)&=\Phi(a,b)+d_n(a,b).
 \end{split}                                                      \tag{1}
$$

Here $M(x)=0$ for $x\le0$. More explicitly, if $t,u$ are the two nonnegative short coordinates integrated against the local signed Euler measure $\nu$, the $q_n$ kernel is $(a-20-t)_+(b+20-u)_+$, and the $q_f$ kernel is $\tfrac12(c^2-(c+w_0-20)_+^2)$, where $c=(\min(a-t,20))_+$, $w_0=\min(20,(u-b)_+)$. These are the two separate real regions of §4 of the four-parity law: for the forbidden wedge the containing variable $g$ and the reflected ordinary variable $y$ lie in the capped intervals $0\le g\le c,\ w_0\le y\le20$, with $g+y\ge20$. Similarly the double kernels are the nonlong rectangle $(a-20-t)_+(b-20-u)_+$ and the retained-long forbidden triangle $\tfrac12(\min(a-t,20)+\min(b-u,20)-20)_+^2$. The products in (1) follow from $\int(x-t)_+\,d\nu(t)=M(x)$. Each individual kernel is bounded and Lipschitz on the relevant fixed range, and vanishes when either short coordinate exceeds $A_0+20$. Thus the signed Euler peeling applies separately to these five types of real shape, not by subtraction of independently estimated arithmetic sums.

The phases of the seven original subrows are

$$
 \begin{array}{c|ccccccc}
  \mathrm{row}& O&R_n&R_f&L_n&L_f&D_n&D_f\\ \hline
  4\mathrm{\ phase}&
 -\varepsilon_1\varepsilon_2P(a,b)&-\varepsilon_1 q_n(b,a)&-\varepsilon_1 q_f(b,a)&
 -\varepsilon_2 q_n(a,b)&-\varepsilon_2 q_f(a,b)&-d_n(a,b)&d_f(a,b).
 \end{array}                                                       \tag{2}
$$

Indeed on an ordinary arm $\mu(h)\mathbf1_{\mu(h)=\varepsilon_1}=(\mu(h)+\varepsilon_1)/2$; on a containing arm the projector is $(1+\varepsilon_1\mu(h))/2$, with the corresponding right identities. After the full-sign bits are bounded, these identities give the exact coefficients in (2), including the negative double nonlong residue. The finite sum of (2) recovers the already-known full parity phase, but it is the separate subrows that are estimated here.

To justify the bound, first fix one common $a,b,Z$. The fixed-node proof of the four-parity law §§1–4 works subrow by subrow. The same global cofactor window and fixed short-label cap below $Z_0$ apply, and replacing external-floor slivers and units costs the same absolute bounds on an individual row. At most $O(\ell^2)$ pairs of true hard label bins occur in each subrow, with $O(\ell)$ ambiguous pairs along the literal moving boundaries. For each full-sign bit, one bin arm has fourth norm $O(X^{3/4}\ell^{-1-1/10})$ and the other has $O(X^{3/4}\ell^{-1})$; this uses the true $Fz$ or $Gw$ Perron separator also on a containing full-sign arm. Hölder and Parseval across the finite bin sum give the same $O(X^{3/2}\ell^{-1/10})$ norm on each subrow. The ambiguous bins are bounded positively at $O(X^{3/2}\ell^{-1})$, keeping exact tests inside those bins. The accepted no-full-sign bits use the shared scalar (6) and the reduced-numerator completion of that proof. For each subrow, convert its hard-bin scalar to the indicated bounded Lipschitz area separately. Its positive boundary-bin cost is $O(\ell^{-1})$ in the scalar and its signed Euler peeling error is $O(\ell^{-1/10})$, as in that proof; the same unconditioned normalization applies. This proves squared target error $O(X^3\ell^{-1/5})$ for each entry of (2), not an estimate found by subtracting two full-slice formulas.

For adaptation, the positive all-label gap estimate of the capped law §5 applies to every row change. It is a pointwise envelope independent of the other coordinates, as in the axis row law: for a floor gap keep its enclosing prime log slab on the changed side and use the common $Z_0$ supersets and global prime windows elsewhere; for a split gap put both floors in their global prime windows and use a full $Z_0$ envelope on the unchanged side. The genuine lost side is bounded only after the actual two-event split condition (gap prime **and** upper $W$-gate failure) is applied. The parity, labels and cuts of each pair that is retained do not change; the true distinguished prime is unique in the global comparison and the label cap is below $Z_0$. Thus the same positive estimates apply after taking the maximum over row or parity and over the other coordinates. Two floor gaps of exponent length $d$ each have the old bound $O(X^{3/2}(d+\ell/L))$; for split gaps above the [marked split threshold](r83-source-full-polynomial-adaptive-split.md) $\tau_*=(\epsilon/16)\log\log\ell/\log\ell$ use $O_H(X^{3/2}(d+L^{-H}))$ when the exponent endpoints have ratio at most two. The single initial interval is handled by the [subpower bound](r82-source-target-adaptive-subpower-split.md) at norm $O(X^{3/2}\ell^{-1/10})$. Exact calibration of $\mathcal C_{X,Z}$ is unchanged, since it is unconditioned and floor independent: a split gap changes it by $O(X(d+\ell^{-1}))$ above $\tau_*$, or $O(X\ell^{-1/10})$ in the initial gap, by the same fixed one-arm calibration of the axis row law.

Mesh the two floor axes and the split exponent above $\tau_*$ with spacing at most $\eta=\ell^{-1/20}=o(\tau_*)$, and bracket below. Positive gap envelopes are independent of the other axes, so on each axis sum their squared norms, not the squares times a product grid count. The total across all axes is $O(X^3\eta)$, because $\sum d^2=O(\eta)$ on each axis and the initial squared gap norm is $O(X^3\ell^{-1/5})$. The calibration and Lipschitz bounds for all comparators give $O(X\eta|\Sigma(N)|)$ comparator change pointwise, hence $O(X^3\eta^2)$ squared norm. Finally the $O(\eta^{-3})$ joint nodes have total squared budget $O(X^3\eta^{-3}\ell^{-1/5})=O(X^3\eta)$, with only a constant cost to include all seven subrows and four parities. This proves the stated common adaptive bound while keeping the separate comparisons.

## 3. A strict margin for the single right-forbidden row

At $(a,b)=(0,25)$ put $p=-P(0,25)>0$ by the [global ordinary sign](r91-source-monotone-parity-kink-positive-two-parity.md), and $q_n=q_n(25,0)=M(5)M(20)$. The left and double phases vanish at $a=0$, exactly as in the axis law. We will show

$$
                  Q(25,0)-p-2q_n>\frac{577}{26880}.              \tag{3}
$$

This is stronger than the grouped containing-row inequality: it makes $q_f(25,0)=Q(25,0)-q_n$ exceed $p+q_n$.

To check the constants, set $m_\pi=\int\kappa=\mathbb E_\pi U=M(7/4)$, where $\kappa$ is the old-prime survival function and $\pi$ has density proportional to $1/u$ on $[5/4,7/4]$. The equality with $M(7/4)$ follows from $M=\rho_4*\kappa$ and $\rho_4=1$ in its initial segment. The paired integrands $t/(3/2+t)-t/(3/2-t)$ are strictly negative for $0<t\le1/4$, so $m_\pi<3/2$. The positive and negative masses of $A$ each equal $m_\pi$, and $M\le m_\pi$. By the [explicit delay bound](r92-source-individual-opposite-parity-reversals.md) $\rho_4(u)\le16/945$ for $u\ge18$, so $M(20)\le(16/945)m_\pi$ and $q_n\le(16/945)m_\pi^2\le4/105$.

Now repeat the actual fixed-axis integrals of the [axis flip proof](r93-source-zero-left-axis-parity-flips.md), keeping the sharper negative mass $m_\pi$: the positive interval $0<s<1$ contributes at least $M(6)$ to $Q(25,0)$, its negative part costs at most $m_\pi M(9)$, and $p\le2m_\pi M(25)$. Its shift bound gives $M(9)\le e^{-3/4}M(6)$, $M(25)\le e^{-19/4}M(6)$. With $e^{3/4}>2,\ e^{19/4}>32$, this yields $Q(25,0)>M(6)/4$ and $p<3M(6)/32$. Since $M(6)>5/8$, we get $Q(25,0)-p>(5/32)M(6)>25/256$. Subtract $2q_n\le8/105$ to obtain (3). In particular its positive phase margin after division by four is $577/107520$; no numerical computation or growing floor is required.

By continuity of every phase, keep a strictly smaller positive margin on a fixed rectangle with strictly positive left floor sufficiently close to zero and right floor sufficiently close to $25$. Choose it inside $0<a<5/4,\ b>24,\ a,b<A_0$. On it the genuine left nonlong subrows $L_n,D_n$ vanish exactly: $a<20$ makes every $Fz>D_N$, independent of $b$. All five other phases are strictly nonzero. In order $O,R_n,R_f,L_f,D_f$, their signs are respectively

$$
       \varepsilon_1\varepsilon_2,\quad
       -\varepsilon_1,\quad -\varepsilon_1,\quad
       \varepsilon_2,\quad -1.                                   \tag{4}
$$

Here $q_n(b,a)>0$ since $b>24$, and $q_f(b,a)>0$ by the continued strict margin (3). The small positive left floor gives $q_f(a,b)=Q(a,b)<0$ by §5 of the four-parity law. The double phase is $d_f=\Phi(a,b)<0$ by the Dickman capped sign for $b\ge24$, $a>0$, using symmetry. Nonvanishing is uniform on a sufficiently small closed rectangle, and its right-forbidden absolute phase still exceeds the sum of the other absolute phases by a fixed positive constant.

For the low rectangle let $b_0=a_Q(0)<20$ from the [unique mixed reversal](r90-source-unique-parity-floor-reversal.md). At $(0,b_0)$, the ordinary phase is nonzero and every other phase is zero. Hence its strict dominance persists in a fixed small neighborhood; within this neighborhood choose $b$ slightly below $b_0$ and then a sufficiently small positive $a$, with $a+b<20$. There both nonlong mixed rows and the nonlong double are exactly absent, since each containing label is long on either side. The double-forbidden row is also exactly absent: $FG\ge N e^{-(a+b)T_N}>Q_N$. Shrink the rectangle so that all three remaining models are nonzero: $Q(b,0)<0$ just below $b_0$ and this persists at small positive $a$, while $Q(a,b)<0$ at the indicated left floors. The ordinary phase dominates the sum of the two mixed absolute phases.

Finally $\mathcal N_{N,Z}\gg X$ uniformly on an interior target subwindow, for every true split. The common squared bound gives, by Markov, one exceptional set of size $O(X\ell^{-1/20})$ outside which the actual subrow errors are smaller than a fixed fraction of both the continued positive margins and all specified nonzero magnitudes times $\mathcal N_{N,Z}$. Thus the comparisons are between the *individual actual rows* at the same targets and chosen splits, not between signed models only. Over the full target window remove endpoint strips of width $X\ell^{-1/60}$ and apply the same estimate to the remaining overlap scale, giving the asserted full-window count. The statement does not decide the other parts of the original sum or its signs on exceptional targets.
