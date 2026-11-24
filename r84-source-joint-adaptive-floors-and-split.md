# Joint target-adaptive prime floors and rough split on the actual carrier

Use the same genuine below-square-root carrier as the [common-split local law](r81-source-variable-split-local-sign-law.md), the [subpower maximal law](r82-source-target-adaptive-subpower-split.md), and the [full split maximal law](r83-source-full-polynomial-adaptive-split.md). Thus $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, $\epsilon=1/64$, $\mathcal J=[X/2,(1+\Delta)X/2]$, and $\mathcal X=[X,(1+\Delta)X]$. The lower split is $Z_0=V_X^2$, $V_X=\exp(T\ell^\theta)$; the full range is $[Z_0,X^{\delta_0}]$ for the same sufficiently small fixed $\delta_0$. Keep exactly the actual prime alphabets, the two excluded neighborhoods, old prime, squarefree unit conditions, literal $W$ size and count gates, and genuine typical exceptional count on the whole product $WU$. Both Möbius parities are still retained.

Fix a compact rectangle of floor exponents

$$
 \mathcal R=[a_-,a_+]\times[b_-,b_+]\subset(0,20)^2,
      \qquad a_-+b_->20.
$$

At a target $N$ allow any $(a,b)\in\mathcal R$ and any $Z$ in the full split range, independently of all other targets. The actual prime floors are $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$, where $T_N=\log N/\log\log N$. Write $R_{N,Z}^{a,b}$ for the original signed sum on this prescribed selection, with the unchanged tests $d>D_N,e>D_N,de>Q_N$, $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$ and $Q_N=\lfloor Ne^{-20T_N}\rfloor$, and let $\mathcal C_{X,Z}$ be the exact positive normalization of the common-split theorem. In particular $\mathcal C_{X,Z}$ does not depend on $a,b$. Define the actual local term

$$
 {\cal L}_{N,Z}^{a,b}=
   \Sigma(N)B_{\mathcal J}(N)
      \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2
             \Psi(a+b-20),\qquad B_{\mathcal J}(N)=|\mathcal J\cap(N-\mathcal J)| .
$$

Here $\Psi$ is the same deterministic signed coefficient of the [short-prime sign theorem](r79-source-short-prime-euler-sign-transition.md), and $\Sigma$ is the even binary singular series.

**Theorem (unconditional).** With a constant depending on the fixed carrier and compact rectangle, one has

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
   \sup_{\substack{(a,b)\in\mathcal R\\Z_0\le Z\le X^{\delta_0}}}
             |R_{N,Z}^{a,b}-{\cal L}_{N,Z}^{a,b}|^2
                     \ll X^3\ell^{-1/20}.
 \tag{1}
$$

The choices of the two floors and the split can be independently target-dependent. On the part of the rectangle with $|\Psi(a+b-20)|\ge\kappa$ for any fixed $\kappa>0$, in each fixed interior subwindow all such choices have the sign of their own $\Psi$ and magnitude $\gg_\kappa X$ outside a common $O_\kappa(X\ell^{-1/20})$ exceptional set. On the full window the strict sign has a common $O_\kappa(X\ell^{-1/60})$ exceptional set. Restricting instead to $\Psi(a+b-20)=0$ gives genuine simultaneous mean-square cancellation, when that locus meets the rectangle. None of this proves a pointwise estimate at a prescribed exceptional target, control of a different carrier, or Hypothesis S.

## 1. Uniformity of the fixed-node theorem

The fixed-node error from the common-split law is

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
       |R_{N,Z}^{a,b}-{\cal L}_{N,Z}^{a,b}|^2
                          \ll X^3\ell^{-1/5}
 \tag{2}
$$

uniformly over this rectangle and the full split range. We check the compact floor uniformity explicitly, since the nodes will depend on $X$.

The strict margins $20-a_+$ and $20-b_+$ are positive. The derivative of $\frac12 u-c u/\log u$ with respect to $u$ is positive for sufficiently large $u$, uniformly for $c\in[a_-,a_+]\cup[b_-,b_+]$. Hence the fixed external floors $F_0(a)=\sqrt X e^{-aT}$ and $G_0(b)=\sqrt X e^{-bT}$ are no higher than their actual floors on $\mathcal X$, with log errors bounded by an absolute fixed constant uniformly in the rectangle. The literal relation $F,G>D_N$ therefore holds uniformly for all operands so selected. In the fourth short-orbit row the product test with the opposite floor even gives $F,G<\sqrt X$ in the fixed-floor comparison, because $Q_N/G_0(b)\ll\sqrt X e^{-(20-b_+)T}$ and similarly for $G$. The finite-orbit proof can use a single cap $M=\exp((22+a_++b_+)T)$ for all short and omission labels and, in the ordinary signed density, a single neutral Euler band starting at $\exp((23+a_++b_+)T)$ and ending at $V_X/4$. This is all inside every actual lower alphabet once $X$ is sufficiently large. Its reciprocal mass is $\theta\log\ell+O(1)$, exactly the required mass for the ordinary signed $\ell^{-1/10}$ factor. The existence of a distinct tagged prime if two near-square-root factors competed is uniform with these bounded exponents. It applies also if a proposed distinguished prime repeats, so no extra prime veto appears in the positive fixed comparisons.

All actual cofactor windows have logs within $O_{\mathcal R}(T)$ of $\frac12 L$. Thus the numbers of bins of width $T/\ell$ in the R81 proof are $O_{\mathcal R}(\ell)$ per axis, the seam strips have uniform $O(1)$ log thickness from the genuine floors and moving integer cutoff, and the available small labels and cofactor intervals have uniform length and multiplicity bounds. For each fixed $s,W$ the same residual count $K(W)$ and reciprocal continuum density are used as there. Its upper compact supremum and Lipschitz bound are $O(\tau^{-1})$, canceled against lower labeled mass $O(\ell\tau)$ with $\tau=\log Z/L$; neither bound uses a special floor endpoint. The actual central real area for the fourth row is $f_\delta(t)=\frac12(\delta-t)_+^2$, where $\delta=a+b-20$ and $t\ge0$ is the sum of the two short label exponents. Indeed $\min(a,b)-\delta=\min(20-a,20-b)$ has a fixed positive lower bound on $\mathcal R$, so the whole relevant triangle is inside both floor intervals. Its bounded size, bounded variation in the label exponents, and number of relevant short-product Euler orders are uniform (one may take the same cutoff $A=21$ in the sign calculation). Thus all reciprocal-PNT, peeling, and real-offset errors in that proof stay uniform, as do the common rational coefficient norm and real overlap. This makes (2), rather than just a pointwise-in-parameters version, available at the moving mesh nodes.

We will also use that $\Psi$ is uniformly Lipschitz on the range of $\delta$ in this rectangle. In the real representation of the sign theorem it is the signed average of the four mixed translates of $f_\delta$, integrated against the two fixed old-prime logarithmic laws and the convolution exponential of $-2\mathbf1_{[4,A]}(t)\,dt/t$ for $A=21$. These are finite variation measures on the used range, and $f_\delta(t)$ is Lipschitz in $\delta$ uniformly for $t\ge0$ and $0<\delta<20$. The claim follows, with no need to assume differentiability at a transition zero.

## 2. Global positive comparisons for the three moving coordinates

Use the fixed base split $Z_0$, the global external floors $F_{0}(a_+)$ and $G_{0}(b_+)$, the cap $M$ above, and the actual physical interval $\mathcal J$. In all active terms of the four-row identity each cofactor is at least $H_-=\frac12\sqrt X e^{-20T}$: an ordinary long label forces this, and an active short containing label $Fz$ with an opposite long label satisfies $Fz\le Q_N/(D_N+1)<\sqrt N$, which forces $h\gg\sqrt X$. The upper cofactor windows follow from the actual physical interval and global external floors. These fixed windows have log width $O_{\mathcal R}(T)$. The representation is unique on these comparisons by the same tagged-prime argument as above. At an active cofactor, $U_Z>1$ follows from $W_Z\le X^{\epsilon/2}$ and the old prime bound, as $sW_Z<H_-$. The operand masks as functions of split are therefore nested throughout the full range, and the true tag count is invariant under changing split.

The exact four-row expansion is done before using positivity. Its signed marks on a given pair and genuine long/curved tests are independent of the floors and of the split, once that pair is selected. In all rows, absolute marks are bounded by a fixed multiple of the positive all-label mark assigning a weight $\log F$ to every $z\mid sW_{Z_0}$ with $z\le M$ (and the analogue on the right). Let $A,B$ be those two positive polynomials with the global windows and genuine lower-split carrier, including the exact total tag event. The base construction is the same as in the subpower maximal law. The unweighted fourth norms are $O(X^{3/4})$ by the [finite-orbit positive estimate](r77-source-finite-short-orbit-product-boundary.md). In the following positive comparisons only, target-unit and cut tests can be discarded to dominate literal changed terms.

**Floor gaps.** For a closed interval $[\alpha,\alpha+d]\subset[a_-,a_+]$, changing $a$ from $\alpha$ to anywhere in this interval, leaving $b,Z$ arbitrary, affects only operands whose prime log is between the two actual floors at its endpoints. With a fixed sufficiently large $C_0$, this true slab lies in the fixed hard interval

$$
     [\,\tfrac12 L-(\alpha+d)T-C_0,\ 
                  \tfrac12 L-\alpha T+C_0\,]
 \tag{3}
$$

for every $N\in\mathcal X$. This includes all integer endpoint possibilities. Use the polynomial $A_\alpha^{\rm slab}$ obtained by inserting (3) into $A$. The change in the actual signed coefficient is dominated by a fixed multiple of $(A_\alpha^{\rm slab}*B)(N)$, uniformly in the other parameters. This follows because increasing $a$ only relaxes its literal floor; every changed actual pair then has precisely the required prime in (3), and the four signed mark formulas themselves are unchanged. The corresponding $b$ comparison uses $(A*B_\beta^{\rm slab})(N)$, uniformly in $a,Z$.

In these comparisons the positive one-arm fourth norm is at most

$$
          \|A_\alpha^{\rm slab}\|_4
                 \ll X^{3/4}(d+\ell/L),
 \tag{4}
$$

and similarly on the other arm. This is the full positive arbitrary-width prime slab estimate with width $dT+2C_0$. One can check it directly from the earlier auxiliary arc calculation. At fixed cofactor, Siegel–Walfisz with the $\log F$ mark retains the hard intersections of the prime slab with its floor and the physical interval and supplies the usual reduced factor $\mu(q)/\varphi(q)$. In the real term in physical $x=hF$ the log mark cancels the prime log denominator. At each $x$ the permitted interval in normalized $\log h/L$ has length at most $(dT+2C_0)/L$; its two moving endpoints shift by at most $|\log x-\log y|/L$, even after clipping by the global cofactor windows. Use the count-restricted reciprocal upper density with exact $K(W)$ and its uniform bound $O(\tau_0^{-1})$, where $\tau_0=\log Z_0/L$, against lower labeled reciprocal mass $O(\ell\tau_0)$. This proves a supremum $O(d+\ell/L)$ on real density and total variation $O(\ell/L)$ as $x$ runs over $\mathcal J$. The Fourier transform then has this scale times $\min(X,|\beta|^{-1})$, with arbitrary inverse-logarithmic arithmetic error. The auxiliary major fourth norm gives (4); the auxiliary minor uses the same hard half-integer separation of $hF$ as in the finite orbit, with (3) merely a fixed prime-coefficient interval, so is negligible. In particular there is no small slab length assumption beyond the displayed bound and no division by $d$. Hölder and Parseval consequently give a positive $\ell^2(N)$ envelope of size $O(X^{3/2}(d+\ell/L))$ for each floor gap, valid for all the other coordinates without a mesh count in them.

**Split gaps.** For any two mesh values $Z_j=X^{\tau_j}$, $Z_{j+1}=X^\sigma$ with $\sigma/\tau_j\le2$ and $\sigma>\tau_0$, changing the split from $Z_j$ to within this gap can lose an actual operand only if its cofactor has a prime in $(Z_j,Z_{j+1}]$ and fails at least one true lower gate at $Z_{j+1}$. This is the two-event argument of the full split proof, with strict lower and weak upper prime endpoints. It still applies at any $a,b$ in the rectangle. The positive gap polynomials of that proof are formed at the base split, here with the same global windows and cap defining $A,B$. Those replacements do not change the marked count-restricted reciprocal measure, the original occupation factor bound, or the actual split gates. Their only effects are to enlarge the hard cofactor windows to fixed log width $O_{\mathcal R}(T)$, and to admit the uniformly bounded-arity label cap $M$ above. As in that proof, the marked reciprocal mass is at most a multiple of the reciprocal gap length $\int_{\tau_j}^{\sigma}dt/t$ times the genuine top-failure loss, with the exact upper tag decrement for a marked tagged prime. More explicitly, for either arm the fourth norms of the positive gap comparison are

$$
 \ll_A X^{3/4}\left[
   \left(\int_{\tau_j}^{\sigma}\frac{dt}{t}\right)
       \left\{\ell^{\,1-2\log2}
                +\exp\!\left(-\frac{\epsilon}{8\sigma}
                                     \log\frac1{\sigma}\right)\right\}
                     + L^{-A}\right] .
 \tag{5}
$$

The same result with $X$ in place of $X^{3/4}$ holds for their sums at zero. This is precisely the marked Rankin calculation before choosing a mesh: one extra $\|\nu\|_\infty$ is absorbed in the size bound, positive fourth norms respect coefficientwise domination, and the zero-frequency version uses the identical real density. In particular, for $\sigma\ge\eta=\ell^{-1/20}$ the braces divided by $\sigma$ are uniformly bounded, and $\int_{\tau_j}^{\sigma}dt/t\le2(\sigma-\tau_j)/\sigma$. The split-gap $\ell^2(N)$ envelope is then $O_A(X^{3/2}(\sigma-\tau_j+L^{-A}))$, uniformly in both floors, by convolution against the other full positive arm and Hölder.

The first split gap is handled without a mark, from $Z_0$ to $X^\eta$. Apply the actual missing-arm domination and Rankin bound of the subpower maximal law with cap $\tau_1=\eta$, but with the global floor windows and cap. Those fixed windows satisfy that proof's width, cofactor and label bounds uniformly, so a single positive envelope works for every $a,b$ in the rectangle. Its $\ell^2(N)$ norm is $O(X^{3/2}\ell^{-1/10})$ because $\exp(-(\epsilon/8)\eta^{-1}\log(1/\eta))\ll\ell^{-1/10}$. This compares true signed coefficients throughout the first gap to their coefficients at $Z_0$, with neither floor frozen in the comparison.

**Calibration.** The one-arm calibration of the subpower proof uses a fixed nonzero exponent interval in $(0,\min(a_-,b_-,1))$, the actual $\mathcal J$ and the $\log F$ mark, and maintains all genuine factor gates. Its mass is $|J_*|\mathcal C_{X,Z}+O(X/\ell)$, with $J_*$ this fixed exponent interval; this follows from the upper-density comparison and is independent of the chosen floor exponents. A calibration operand lost over a split gap obeys the same two events as above, and in its positive envelope the label $1$ suffices. Applying the frequency-zero version of (5) therefore gives

$$
 \sup_{Z_j\le Z\le Z_{j+1}}
       |\mathcal C_{X,Z}-\mathcal C_{X,Z_j}|
            \ll X(\sigma-\tau_j+\ell^{-1})
       \qquad (\sigma\ge\eta,\ \sigma/\tau_j\le2).
 \tag{6}
$$

For the first split gap the unmarked Rankin comparison at zero in the subpower proof gives instead $O(X\ell^{-1/10})$, including its $O(X/\ell)$ calibration error. Floor changes do not alter this exact $\mathcal C_{X,Z}$ at all.

## 3. One positive error maximum per coordinate

Put $\eta=\ell^{-1/20}$. Mesh each floor interval by increasing nodes with gap at most $\eta$ (all except possibly a last one of length exactly $\eta$), including both endpoints. A degenerate floor interval has just one node. In the split coordinate use the first gap $[\tau_0,\eta]$ and then a linear mesh from $\eta$ to $\delta_0$, again with gap at most $\eta$, where $\tau=\log Z/L$. For sufficiently large $X$, $\tau_0<\eta<\delta_0$ and every gap beyond the first has ratio of upper to lower endpoint at most two. There are $O(\eta^{-1})$ nodes on each axis, hence $O(\eta^{-3})$ combined nodes.

For each target and any allowed triple, bracket all three coordinates below by mesh nodes (or use the final endpoint at an exact final node). Change the three coordinates one at a time between the triple and its bracket, keeping the other two coordinates arbitrary at each step. The genuine coefficient difference is bounded by the sum of the three positive envelopes above. These bounds are global in the unaltered coordinates, so for the targetwise supremum there are only $O(\eta^{-1})$ candidate envelopes along **each** axis, not ordered triples of envelopes. For example for the $a$ coordinate each gap has one sequence $(A_\alpha^{\rm slab}*B)(N)$, regardless of the chosen $b,Z$. The square of the maximum of these nonnegative sequences is at most the sum of their squares. Thus along either floor axis the total squared envelope cost is

$$
   \ll X^3\left\{\sum_{\text{floor gaps}}d^2
                         +\eta^{-1}(\ell/L)^2\right\}
     \ll X^3\eta ,
$$

since $\sum d^2\le\eta\sum d=O_{\mathcal R}(\eta)$. The split axis analogously costs $O(X^3(\eta+\ell^{-1/5}))$, using (5) above the first gap with any fixed $A>0$ and the separate first-gap envelope. All strict and weak arithmetic tests were applied to the original sums before these positive comparisons.

For the comparator difference, (6) and the first-gap calibration give a uniform normalization change $O(X\eta)$ anywhere relative to the bracket node. $\Psi(a+b-20)$ changes by $O(\eta)$ by the Lipschitz bound in §1. Since $\mathcal C_{X,Z}\ll X$ and $B_{\mathcal J}\ll X$, the pointwise comparator error relative to the chosen node is $O(X\eta|\Sigma(N)|)$, simultaneously on the entire box. There is no grid multiplicity here. The \(\ell^2(N)\) norm of $\Sigma(N)$ is $O(\sqrt X)$ on the window as in the common-split law, so this cost is $O(X^3\eta^2)$ in the sum of squares.

Finally apply (2) to the combined nodes and square-sum their individual errors, bounding the square of their maximum. This costs $O(X^3\eta^{-3}\ell^{-1/5})=O(X^3\eta)$. Adding all the error terms and including the exact mesh endpoints proves (1). The argument needs no regularity of the targetwise parameter choices.

For the sign statement on $|\Psi|\ge\kappa$, use the uniform $\mathcal C_{X,Z}\asymp X$ and positive absolute lower bound for the even singular series. On a fixed interior subwindow the local term then has the stated sign and magnitude uniformly; (1) bounds the targets where any allowed triple fails. On the full window discard endpoint strips of width $X\ell^{-1/60}$ and use (1) outside them, where the magnitude of the comparator is at least a fixed positive multiple of $X\ell^{-1/60}$ for these triples. At an exact zero the local term vanishes without approximation, giving the simultaneous cancellation bound stated above.
