# The true long-floor seam and its capped signed continuum

Retain the genuine carrier of the [variable-split local law](r81-source-variable-split-local-sign-law.md), with $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, $\epsilon=1/64$, $\mathcal J=[X/2,(1+\Delta)X/2]$, and even $N$ in $\mathcal X=[X,(1+\Delta)X]$. The split is $Z_0=V_X^2\le Z\le X^{\delta_0}$ with $V_X=\exp(T\ell^\theta)$, and each operand has its exact squarefree and $N$-unit conditions, the original old prime, both deleted neighborhoods, and the actual typical count on the entire $WU$. The original $W$ size and count gates remain unchanged. Both Möbius parities are retained.

Fix any finite $A_0>0$; now let $0\le a,b\le A_0$, with no lower bound on $a+b-20$ and no restriction that either exponent be below $20$. Keep the literal prime floors $F\ge\sqrt N e^{-aT_N}$, $G\ge\sqrt N e^{-bT_N}$, where $T_N=\log N/\log\log N$, and the exact integer tests

$$
 d>D_N,\quad e>D_N,\quad de>Q_N,\qquad
 D_N=\lfloor\sqrt N e^{-20T_N}\rfloor,\qquad
 Q_N=\lfloor Ne^{-20T_N}\rfloor .
$$

Let $R_{N,Z}^{a,b}$ be the resulting genuine signed sum with the unchanged external minus, and $\mathcal C_{X,Z}$ the exact positive normalization (1) of the variable-split law. As before $B_{\mathcal J}(N)=|\mathcal J\cap(N-\mathcal J)|$ and $\Sigma(N)$ is the even binary singular series.

To define the new coefficient, choose any fixed $A>\max(4,A_0)$, denote a Dirac mass at $x$ by $\delta_x^{\rm at}$, and set

$$
 \lambda_A(dt)=\mathbf1_{[4,A]}(t)\frac{dt}{t},\qquad
 \pi(dt)=\frac{\mathbf1_{[5/4,7/4]}(t)}{\log(7/5)}\,\frac{dt}{t},
 \qquad
 \nu_A=(\delta_0^{\rm at}-\pi)*\exp_*(-\lambda_A).
$$

Here $\exp_*(\xi)=\sum_{j\ge0}\xi^{*j}/j!$ for a finite signed measure, with the order-zero unit atom. Put

$$
 \begin{split}
 H_{a,b}(t,u)
   &=\frac12\bigl(\min(a-t,20)+\min(b-u,20)-20\bigr)_+^2\\
   &\hspace{10mm}-(a-20-t)_+(b-20-u)_+,\\
 \Phi(a,b)&=\iint H_{a,b}(t,u)\,d\nu_A(t)d\nu_A(u),\\
 \mathcal L_{N,Z}^{a,b}
   &=\Sigma(N)B_{\mathcal J}(N)
          \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2\Phi(a,b).
 \end{split}
 \tag{1}
$$

The integral is independent of the chosen $A>\max(4,A_0)$, since its kernel vanishes when either argument exceeds $A_0$. The first area in (1) is the contribution from forbidden pairs of **retained long** labels. The second is the new product of the two actual incomplete long-orbit residues, with the original external minus.

**Theorem (unconditional).** Uniformly for any one common choice of $(a,b,Z)$ as above, possibly depending on $X$, one has

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
         |R_{N,Z}^{a,b}-\mathcal L_{N,Z}^{a,b}|^2
                 \ll X^3\ell^{-1/5}.
 \tag{2}
$$

Moreover the parameters may be chosen independently at every target in the entire stated box and split range, with the common maximal estimate

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \ \sup_{\substack{0\le a,b\le A_0\\Z_0\le Z\le X^{\delta_0}}}
          |R_{N,Z}^{a,b}-\mathcal L_{N,Z}^{a,b}|^2
                  \ll X^3\ell^{-1/20}.
 \tag{3}
$$

In particular for $a+b\le20$ the local term vanishes. For $0\le a,b\le20$ and $a+b>20$, $\Phi(a,b)$ agrees with the earlier $\Psi(a+b-20)$, also at the allowed edges. Past the individual floor line it need not agree: for $a=20.5,b=0.5$ (when included in the box), $\Phi(a,b)=1/8$, whereas the earlier scalar at excess one is $1/2$. On a part of the box with $|\Phi|\ge\kappa>0$, (3) gives the sign of its own local term simultaneously for all choices in each fixed interior subwindow outside $O_\kappa(X\ell^{-1/20})$ even targets, with magnitudes $\gg_\kappa X$ there. Over the full window the strict sign has a common $O_\kappa(X\ell^{-1/60})$ exceptional set. On the exact zero locus (3) gives simultaneous cancellation in mean square. Constants may depend on the fixed carrier and $A_0$. These are results for this prescribed carrier only, not on a fixed exceptional modulus or Hypothesis S.

## 1. Exact incomplete long orbits and support

On a true pair write $n=hF$, $m=kG$ as before. For an ordinary omitted divisor $r\mid h$ put $d=h/r$ and $u_h(r)=\mu(h)\mu(r)\log(Fr)$. Similarly write $e=k/t$ and $u_k(t)$ for an ordinary right label. For a containing label $Fz$, $z\mid h$, put $v_h(z)=\mu(z)\log(h/z)$ so the actual containing-label mark is $-v_h(z)$. Let $v_k(w)$ be the right analogue. As $h,k$ are squarefree composite on the true carrier, the complete signed containing sums vanish, by $\sum_{z\mid h}\mu(z)\log(h/z)=\Lambda(h)=0$. Consequently the exact uncurved sum of just the **long** containing labels is

$$
 L_h:=\sum_{\substack{z\mid h\\Fz>D_N}}(-v_h(z))
       =\sum_{\substack{z\mid h\\Fz\le D_N}}v_h(z),
 \qquad
 L_k=\sum_{\substack{w\mid k\\Gw\le D_N}}v_k(w).
 \tag{4}
$$

This includes equality at the literal integer $D_N$, including a distinguished prime equal to it. It applies even when more than one divisor label is nonlong.

The original sum has the ordinary-ordinary part
$-\sum_{d,e>D_N,\,de>Q_N}u_h(r)u_k(t)$.
The containing-left mixed part is exactly

$$
 -\sum_{e>D_N}u_k(t)
   \left\{L_h+\sum_{\substack{z\mid h\\Fz>D_N,\ Fz e\le Q_N}}v_h(z)\right\},
$$

with the reflected expression for the other mixed part. The last part, with both labels containing, is

$$
 \begin{split}
  &\sum_{\substack{z\mid h,\ w\mid k\\
             Fz>D_N,\ Gw>D_N,\ (Fz)(Gw)\le Q_N}}v_h(z)v_k(w)\\
  &\hspace{12mm}-
    \sum_{\substack{z\mid h,\ w\mid k\\Fz\le D_N,\ Gw\le D_N}}
                                               v_h(z)v_k(w).
 \end{split}
 \tag{5}
$$

These formulas follow by taking full long sums before subtracting forbidden products, not by canceling across a forbidden long boundary. They are literal algebra on each genuine pair. In particular the last negative row is not an artificial subtraction or a parity projection.

For every active term of these expanded rows both cofactors have lower bound $H_-=\frac12\sqrt X e^{-20T}$. An ordinary long label forces $h>D_N$, hence this bound. A containing label in a forbidden product with a long mate is at most $Q_N/(D_N+1)<\sqrt N$ and thus has $h\gg\sqrt X$; and (4) requires $F\le D_N$, giving the same stronger bound. The upper cofactor windows follow from $hF\in\mathcal J$ and $F_0(A_0)=\sqrt X e^{-A_0 T}$, and analogously on the right. These log windows have fixed width $O_{A_0}(T)$.

A single cap $M=\exp((24+2A_0)T)$ covers all omission and short labels in these rows, including in the fixed external floor comparisons. In fact $h,k\ll\sqrt X e^{A_0T}$ and $D_N\asymp\sqrt X e^{-20T}$. Thus ordinary omissions are at most $h/D_N$ or $k/D_N$; a forbidden containing label has $z\le Q_N/(F(D_N+1))\ll e^{A_0T}$; and one in (4) has $z\le D_N/F\ll e^{(A_0-20)T}$, or its reflection. For large $X$ this global cap is below $Z_0$ and all these labels lie in $sW_{Z_0}$, or its right counterpart, whenever the operand passes the exact split. Moreover the short labels of (5) alone can all be cut off by $\exp(AT)$ for the fixed $A$ in (1). Active cofactor logarithms and distinguished-prime logarithms are comparable to $L$ uniformly. In the fixed external comparison two factors at or above $\sqrt X e^{-A_0T}$, even two copies of one factor, would leave a product of size $e^{O_{A_0}(T)}$ and are both above the tag range. This is impossible with the required distinct prime exceeding $2V_X$ in the stabilized total typical count. Thus the distinguished representation remains unique without an extra prime veto in the auxiliary polynomials.

## 2. Hard bin comparison and the saving ordinary legs

We record which parts of the previous Fourier estimates are used without an assumption $F,G>D_N$. In every arm split into hard log bins of width $T/\ell$ in its actual label, either $h/r$ for an ordinary arm or $Fz$ for a short arm. Cofactor windows, real floor windows and label supports have width $O_{A_0}(T)$ in log, by §1. Every label polynomial has its genuine base count at its chosen split, physical hard interval $hF\in\mathcal J$, and the log mark specified above. The [finite-orbit Fourier bounds](r77-source-finite-short-orbit-product-boundary.md) give fourth norm $O(X^{3/4}\ell^{-1})$ in a bin for the positive all-label or short signed marks, and $O(X^{3/4}\ell^{-1-1/10})$ for the signed ordinary marks. Here these are estimates for the individual polynomials and do not use the lower long test on which bin pair is ultimately selected. Their ingredients are the fixed cofactor width, short label cap, true count-restricted reciprocal density, and the neutral Euler band for the ordinary sign. With the cap from §1 one can take this band to start at $\exp((25+2A_0)T)$ and end at $V_X/4$; it remains wholly in $W$ for every split, above all labels and below every tagged prime. Its reciprocal mass is $\theta\log\ell+O_{A_0}(1)$ and the signed ratio gives the same $\ell^{-1/10}$. The upper count set is not relaxed. The two hard half-integer Perron separations when necessary are still exactly on the products $hF$ and $Fz$, and no additional real gate is substituted for those products. The cutoff extension of the windows therefore only changes constants.

Use fixed lower external prime floors $F_0(a)=\sqrt X e^{-aT}$ and $G_0(b)=\sqrt X e^{-bT}$. The genuine floors dominate them, with $O_{A_0}(1)$ log difference, since $\frac12 y-cy/\log y$ is increasing in $y$ for sufficiently large $y$ uniformly for $0\le c\le A_0$. Changing a floor excludes only a fixed prime sliver of log width $O_{A_0}(1)$. The same positive Fourier bound, in one full label arm with only that prime sliver and on the other full arm, has fourth norms $O(X^{3/4}\ell/L)$ and $O(X^{3/4})$ respectively. Thus Hölder and Parseval make this an $O(X^{3/2}\ell/L)$ error in target $\ell^2$. The unit restriction can also be restored at arbitrary inverse-logarithmic precision: if an overlap prime divides both operands then it divides $N$ and is at least $e^{5T/4}$; there are $O(\ell)$ such candidates, each permits $O(X/p)$ first operands, with the two log marks and all bounded-arity labels costing only fixed powers of $L$. These give $O_H(XL^{-H})$ per target for any fixed $H$. Both comparisons use the actual signed expansion before absolute domination; they do not assume a full untreated divisor sum is absolutely small.

The literal cuts move by $O(1)$ in log over $\mathcal X$: $\log D_N=L/2-20T+O(1)$, $\log Q_N=L-20T+O(1)$. In any row all its cut boundaries, in log-label coordinates, are horizontal or vertical lines or the fixed-slope product diagonal, each in a band of log width $O(1)$. Uniformly in $(a,b)$ there are $O(\ell^2)$ possible pairs of bins for each row and only $O(\ell)$ ambiguous pairs near these boundaries. On completely accepted pairs of bins the actual conditions are exact for every target, and the coefficient is the convolution of the two corresponding signed polynomials after the harmless unit comparison. On ambiguous pairs, retain the strict or weak arithmetic tests when defining their terms, but dominate each by the positive coefficient. Thus the ambiguous-bin error in each row has norm $O(X^{3/2}\ell^{-1})$. This covers equality at $D_N$ or $Q_N$ without changing what a label means.

Each of the ordinary-ordinary row and the four mixed subrows has at least one signed ordinary arm. Hölder and Parseval give a total target $\ell^2$ norm $O(X^{3/2}\ell^{-1/10})$ by summing the norm over at most $O(\ell^2)$ accepted pairs with two bin factors and at least one signed gain, plus the preceding seam and restoration errors. This includes the new unrestricted residue (4) against an ordinary arm: its one-sided short test is $Fz\le D_N$, not a product condition, and the opposite ordinary long test is unchanged. No cancellation of the new double-residue product (5) has been attributed to this step.

## 3. Real shapes of the two genuine double rows

For either double row the genuine support has $F,G\ll\sqrt X$ with a fixed constant: in the first row of (5) each of $Fz,Gw$ is at most $Q_N/(D_N+1)<\sqrt N$, and in the second they are at most $D_N$. After fixing the external prime floors as above, restricting $F,G\le\sqrt X$ thus changes only positive prime slivers of log width $O(1)$, with the same negligible \(\ell^2\) error. This applies uniformly even at $a=0$ or $b=0$, when there may be no interval left or a single exact endpoint. Put

$$
 \alpha=(L/2-\log F)/T,\quad
 \alpha'=(L/2-\log G)/T,\quad
 t=\log z/T,\quad u=\log w/T,\quad
 \gamma=\alpha-t,\quad\gamma'=\alpha'-u .
$$

The fixed comparisons have $\alpha\in[0,a]$, $\alpha'\in[0,b]$. Because $h=x/F$ in the real density, on this support the active cofactor interval from §1 places no extra restriction on $\alpha$ or $\alpha'$ when $x\in\mathcal J$. For example the lower bound on $h$ is automatic at $F\le\sqrt X$, and the upper bound is automatic at the global external floor. The exact long cuts are $\gamma<d_N^*$, $\gamma'<d_N^*$, and the exact forbidden product cut is $\gamma+\gamma'\ge q_N^*$, where $d_N^*=(L/2-\log D_N)/T$ and $q_N^*=(L-\log Q_N)/T$ are both $20+O(1/T)$. The second row requires $\gamma,\gamma'\ge d_N^*$. These are the actual sets for the bin classification just described.

In the real comparison the first region has $\gamma,\gamma'\le20$ and $\gamma+\gamma'\ge20$, so both $\gamma,\gamma'$ are nonnegative, and the lower endpoints $\gamma\ge-t,\gamma'\ge-u$ never remove area. Its two possible upper endpoints are $\min(a-t,20)$ and $\min(b-u,20)$. The upper-corner area is therefore the first term of $H_{a,b}(t,u)$ in (1). This remains true if an upper endpoint is negative, since the other is at most $20$ and the area and the positive part are then both zero. In the second region $\alpha\ge20+t$, $\alpha'\ge20+u$, so its area is the product in the second term of (1). Equality of continuous boundaries has zero area; exact arithmetic equalities have already been covered in the hard-bin comparison.

We next compute the actual common local term from these areas. For clarity, in a short-arm bin $I$ in $\gamma$, the real scalar coefficient has exactly the form of the variable-split proof:

$$
 c_{a,I}
  =\frac1\ell\sum_{\substack{s,W\\\text{true lower masks}}}
     \sum_{\substack{z\mid sW\\z\le e^{AT}}}
       \frac{\mu(z)}{sW}\,
       \varrho_{+,K(W)}\!\left(\frac12-\frac{\log(sW)}L\right)
          \left|\bigl(I+\log z/T\bigr)\cap[0,a]\right|.
 \tag{6}
$$

Here $\varrho_{+,K(W)}$ is the real upper reciprocal density with the exact remaining count condition. There is no full cofactor-parity sign in the double rows. On each reduced auxiliary major arc the actual short polynomial is the continuous transform of $c_{a,I}\mathbf1_{\mathcal J}$ plus an error of size $O(\ell^{-2}\min(X,|\beta|^{-1}))$, multiplied by the standard $\mu(q)/\varphi(q)$, and with arbitrary inverse-logarithmic discrete error as in the variable-split proof. Indeed the true mark divided by $\log F$ is $1+O_{A_0}(\ell^{-1})$ here. On changing variables to $\alpha$ at fixed physical $x$, the interval in (6) is fixed and the real density argument changes from the one shown by $O_{A_0}(\ell^{-1})$ and is in $[.4,.6]$. Its Lipschitz bound $O(\tau^{-1})$ multiplies the genuine lower labeled reciprocal mass $O(\ell\tau)$, $\tau=\log Z/L$; the variation in $x$ has the same or smaller error. The right arm has the corresponding coefficient $c_{b,I'}$. The two hard product separations give the same arbitrary inverse-logarithmic auxiliary minor bounds. Thus this bin calculation is uniform in the extended floor range, with $|c_{a,I}|\ll\ell^{-1}$ and a bounded sum of absolute coefficients over all bins.

For each of the two regions, take the fixed sum of $c_{a,I}c_{b,I'}$ over its completely accepted bin pairs. The local arithmetical coefficient, after summing the reduced numerators before taking absolute values, is $\Sigma(N)B_{\mathcal J}(N)$ times this scalar, as in the common-split law. The error has target norm $O(X^{3/2}\ell^{-1})$: the product transform errors, summed over $O(\ell^2)$ pairs, have continuous density scale $O(\ell^{-1})$; the literal radii and numerator errors are accounted by $\|c_q(N)\|_2/\varphi(q)^2\ll_\xi\sqrt X\,q^{-3/2+\xi}$ on squarefree $q$, for any fixed $\xi>0$, with the same completing tails. The ambiguous positive coefficients have already been bounded. Passing in the two scalars from accepted real bins to their limiting regions costs $O(\ell^{-1})$ since only $O(\ell)$ boundary-bin pairs are altered. Taking their signed difference gives exactly the sum of (6) against the area kernel $H_{a,b}$ with the two short label variables. In particular the residue sign in (5) persists into the scalar; its product has not been replaced by a positivity bound.

## 4. Signed Euler limit with the same exact normalization

The preceding real scalar is the two-arm short-label sum of (6) integrated against $H_{a,b}$. This kernel is uniformly bounded and Lipschitz in $t,u,a,b$ on the relevant fixed ranges, and is zero if either label variable exceeds $A_0$. Thus the quantitative low-factor peeling of the variable-split law applies to this scalar as well. Here are the points needed to check its use for the new nonseparable difference of areas.

In the real scalar only, peel $W_{\rm l}$ with primes up to $e^{AT}$ from $W_{\rm h}$. These primes are below the two deleted neighborhoods and every tag for large $X$, and are in $W$ for every allowed split. The genuine residual set $K(W)=K(W_{\rm h})$ is therefore unchanged before and after peeling. The true short labels in (6) divide $sW_{\rm l}$. In the absolute comparison, counting their choices doubles the occupation weight only in the fixed log-ratio band $[e^{4T},e^{AT}]$ and permits two choices for $s$. The positive Euler mass for the lower part is $O(\ell\tau)$ and its normalized $2^{\omega(W)}$ moment is $O(\ell)$. With the real density bound $O(\tau^{-1})$ and the factor $\ell^{-1}$ per arm, replacing the old $2\log\ell$ total count by a temporary $3\log\ell$ low count and then releasing the temporary gate costs $O(\ell^{1-2\log 2})$. The log of the temporarily capped lower factor is $O(T\log\ell)$, so the genuine hard size strip and the shift of the same count-restricted density from $sW$ to $W_{\rm h}$ give $O(\log\ell/\ell)$ after normalization. The strip bound is obtained by marking a high factor with its $\log p$ weight on the strip where the high product is of log size $\gg L$, exactly as in the common-split law; this is a positive bound, not a change to the tag law. These estimates use only a bounded test area and genuine bounded-arity label choices, so apply to both terms of (1) and to the unlabelled normalization.

After factoring the low part, the law of whether its prime occurs in the short signed divisor contributes exactly $-1/(p+1)$ under the positive weight $1+1/p$; the old prime contributes the two signs at $0$ and $\log s/T$. On each arm, the finite product of the corresponding signed atoms at log position $\log p/T$ differs from its convolution exponential by exponentially small total variation, by marking one repeated-prime error and using $\sum_{p\ge e^{4T}}p^{-2}$. Reciprocal PNT on the fixed normalized log band gives $\lambda_A$ in the resulting real limit, and on the old prime interval gives exactly the reference law $\pi$ after division by its reciprocal mass. For the bounded-variation test $H_{a,b}$ the reciprocal-PNT errors can be made arbitrary inverse-logarithmic uniformly. Only finitely many convolution orders matter, depending on $A_0$. No prime of $U$ contributes to the detached short measure; the density of the retained higher factors still uses its actual $K(W_{\rm h})$. Comparing the two same positive normalizations with their original $\mathcal C_{X,Z}$, their error after division by $|\mathcal J|$ is also $O(\ell^{1-2\log2}+\log\ell/\ell)$. Consequently the signed real bin scalar is

$$
 \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2\Phi(a,b)
          + O(\ell^{-1/10})
$$

uniformly, which suffices at the scale of the saving ordinary legs. This is the same normalization as before, not a factor defined by the capped region itself. Together with §§2–3, $B_{\mathcal J}\ll X$ and $\|\Sigma\|_{\ell^2(N)}\ll\sqrt X$, it proves (2).

For $a,b\le20$ the capped term is $\frac12(a+b-20-t-u)_+^2$ and the residue term is zero. The equivalence with the earlier $\Psi$ for positive excess follows by applying the two old-prime differences to this kernel and using $\exp_*(-\lambda_A)*\exp_*(-\lambda_A)=\exp_*(-2\lambda_A)$, as in the [short-prime sign theorem](r79-source-short-prime-euler-sign-transition.md). Since $a,b\ge0$, if $a+b\le20$ they are automatically both at most $20$ and the kernel vanishes. For the past-floor example $a=20.5,b=0.5$, every nonzero short coordinate is at least $5/4$ in the support of $\nu_A$. Either such coordinate makes the capped area zero, and the residue product is zero because $b<20$. The atom at $(0,0)$ has weight one and area $\frac12(.5)^2=1/8$, whereas in the old scalar at excess one the atom has area $1/2$ and is again the only support. There is also a negative-sign region with $a>20$: $\Phi(20,11)=\Psi(11)<0$ by the earlier theorem, and the explicit kernel is continuous, so this continues into an open region across that floor line. No sign is asserted on the whole box.

## 5. Actual targetwise adaptation across all seams

We check that the joint maximum proof did not require an individual $a<20$ margin except in the old fixed-node law. In the current seven-subrow decomposition the signed mark on a fixed pair does not depend on $a,b$ or the split. Its tests involve only the original long/curved cuts and its actual labels, any of which is below the one fixed cap $M<Z_0$. The true total tag event is split-invariant and if the $W$ size gate passes then $U>1$ automatically in the active cofactor windows. Consequently moving an actual floor within a mesh gap changes only primes in the genuine gap at that target, and moving a split changes only operands lost under the nested real $W$ gates. The same global positive all-label envelope with external floor $F_0(A_0)$, cofactor windows from §1 and the cap $M$ dominates every affected row. The short mark $\log(h/z)$ and the ordinary log mark are both $O(\log F)$ there. It is important that this domination is after the exact algebra (4)–(5), including a long prime exactly at its threshold.

The [joint adaptive mesh bounds](r84-source-joint-adaptive-floors-and-split.md) thus apply to changes of the genuine coefficients using these global windows. For a floor gap of exponent length $d$, the true moving threshold lies in the fixed enclosing log slab of length $dT+O(1)$, including all its endpoint primes. Its one-arm positive fourth norm is $O(X^{3/4}(d+\ell/L))$, clipped by the same other hard cuts; the opposite global full norm is $O(X^{3/4})$. This follows from the count-sensitive density bound and exact prime hard slab as in that proof: the real upper coordinate interval has normalized length $O((dT+1)/L)$ and its endpoints move by at most $|\log x-\log y|/L$ at fixed physical $x,y$. Hence the resulting $\ell^2(N)$ error for a floor gap is $O(X^{3/2}(d+\ell/L))$ uniformly in the other two axes. For an upper split gap, a changed pair requires a gap prime **and** failure at the upper $W$ gate. The [full split marked calculation](r83-source-full-polynomial-adaptive-split.md), using the same global windows, yields an $O_A(X^{3/2}(\Delta\tau+L^{-A}))$ gap error for upper exponent $\sigma\ge\eta=\ell^{-1/20}$ and endpoint ratio at most two. Its counting loss divided by $\sigma$ is bounded even from $\sigma=\eta$, since $\ell^{1-2\log2}/\eta=o(1)$, and the exponential size loss divided by $\sigma$ is bounded. For the first split gap $[Z_0,X^\eta]$ the [unmarked subpower comparison](r82-source-target-adaptive-subpower-split.md) gives $O(X^{3/2}\ell^{-1/10})$, since $\eta^{-1}\log(1/\eta)$ dominates $\log\ell$. These bounds use only the global cofactor windows and label cap, not particular values of the two floors.

The normalization difference at a split gap is the same as in the earlier marked calibration: at the upper gaps it is $O(X(\Delta\tau+\ell^{-1}))$ and in the first gap $O(X\ell^{-1/10})$. The normalization $\mathcal C_{X,Z}$ does not involve either floor. Its one-arm calibration can be taken at a fixed positive prime exponent interval inside $(0,1)$, independent of any floor endpoints here, and retains the same literal $W$ and upper count gates. Equivalently use the earlier calibration at a fixed reference positive pair to compare the exact same $\mathcal C_{X,Z}$. This avoids relying on a nonexistent interior prime exponent interval for a floor equal to zero.

Now mesh the two floor axes at length at most $\eta$ in $[0,A_0]$, and mesh the split exponent linearly at length at most $\eta$ above its first gap. There are $O(\eta^{-3})$ combined nodes, where (2) has uniform squared error $O(X^3\ell^{-1/5})$. Bracket a target's chosen triple below and change one axis at a time. Because the positive comparisons are uniform in the other two coordinates, for each axis the square of the maximum gap envelope is bounded by the sum of squares over that axis alone. Thus the total gap cost is $O(X^3\eta)$: the sum of squared mesh lengths per axis is $O(\eta)$, the thin logarithmic floor enlargements and negligible reciprocal-PNT errors contribute less, and the first split gap costs $O(X^3\ell^{-1/5})$. In the comparator, the calibration and the uniform Lipschitz continuity of $\Phi$ from its compact kernel give a pointwise change $O(X\eta|\Sigma(N)|)$ relative to the bracket node. Its squared norm is $O(X^3\eta^2)$ with no grid factor. The node budget $O(X^3\eta^{-3}\ell^{-1/5})$ is $O(X^3\eta)$ at this chosen mesh scale, proving (3) with no regularity assumption on the targetwise choices.

The claimed sign and zero-locus consequences follow with the exact same local overlap and uniform positive normalization. On the interior the overlap is order $X$ and $\Sigma(N)$ has an absolute positive lower bound for even $N$. On the whole interval remove endpoint strips of width $X\ell^{-1/60}$ and apply (3) to any target with a wrong or zero sign for an allowed triple with $|\Phi|\ge\kappa$ outside the strips. At an exact zero the entire comparator vanishes. No statement for a prescribed exceptional target follows from these mean-square estimates.
