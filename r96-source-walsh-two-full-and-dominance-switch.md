# Actual Walsh cancellation and a change of the dominating subrow

Use the seven genuine signed subrows $S_j^{\boldsymbol\varepsilon}$ of the [off-axis forbidden-dominance theorem](r95-source-off-axis-right-forbidden-dominance.md), in its notation, on the same exact carrier and with the same external signs. Thus $j$ ranges over $O,R_n,R_f,L_n,L_f,D_n,D_f$; every unit, parity, prime-floor, long-divisor and product test remains the literal test for the actual squarefree pair $n=hF,\ m=kG$. The floors $a,b$ range over a fixed box $[0,A_0]^2$, and the true split $Z$ ranges over $[Z_0,X^{\delta_0}]$. Neither the subrows nor their endpoint conditions are redefined.

For bits $\mathbf u=(u_1,u_2)\in\{0,1\}^2$, define the **unnormalized actual** Walsh coefficient by

$$
 W_j^{\mathbf u}(N;a,b,Z)
      =\sum_{\varepsilon_1,\varepsilon_2=\pm1}
            \varepsilon_1^{u_1}\varepsilon_2^{u_2}
                 S_j^{\boldsymbol\varepsilon}(N;a,b,Z).
 \tag{1}
$$

The intrinsic full-cofactor sign bits $\mathbf b_j$ of the seven genuine rows are

$$
 \begin{array}{c|ccccccc}
 j & O & R_n & R_f & L_n & L_f & D_n & D_f\\ \hline
 \mathbf b_j & (1,1)&(1,0)&(1,0)&(0,1)&(0,1)&(0,0)&(0,0).
 \end{array}                                                      \tag{2}
$$

**Theorem.** The unique Walsh channel with no full-sign cancellation requirement in row $j$ is $\mathbf u=\mathbf b_j$; it has the genuine R95 comparator given below. Each channel with exactly one full sign has the former squared norm $O(X^3\ell^{-1/5})$ at fixed common $a,b,Z$ and common adaptive squared norm $O(X^3\ell^{-1/20})$, with zero comparator. In the other channel, $\mathbf u=\mathbf b_j+(1,1)\pmod2$, one can use the gain from **both** full signs. Uniformly in the row, at fixed common $a,b,Z$ the actual sum satisfies

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
     \left| W_j^{\mathbf b_j+(1,1)}(N;a,b,Z)\right|^2
                      \ll X^3\ell^{-2/5}.                       \tag{3}
$$

Allowing $a,b,Z$ and the row to be chosen independently at each target gives

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
      \sup_{\substack{a,b\in[0,A_0],\ Z_0\le Z\le X^{\delta_0}\\j}}
     \left| W_j^{\mathbf b_j+(1,1)}(N;a,b,Z)\right|^2
                       \ll X^3\ell^{-1/10}.                     \tag{4}
$$

With a single common pair $a,b$ and maximization only in $Z,j$, the bound in (4) improves to $O(X^3\ell^{-1/5})$. All constants may depend on the fixed carrier and $A_0$, not on parameter choices at the targets.

On the fixed high rectangle of the off-axis theorem, in every parity-resolved slice the actual $R_f$ dominates the other active subrows combined in absolute value, as already proved there. On the **same** targets and true splits, after summing the actual parities the winning subrow is instead $D_f$, with strictly negative sign. Both statements hold simultaneously outside one $O(X\ell^{-1/20})$ even exceptional set in each fixed interior target subwindow, and outside $O(X\ell^{-1/60})$ for the strict comparisons on the full window. On the interior both winning margins are $\gg X$. No pointwise assertion at all targets or extension to a growing box or to Hypothesis S is made.

## 1. The exact arithmetic projections

For each true physical pair (1) multiplies its original row mark by $\mu(h)^{u_1}\mu(k)^{u_2}$: just one of the four literal parity masks is selected. In particular $\mu(h)^2=\mu(k)^2=1$ since $h,k$ are squarefree, so existing full-sign factors either cancel exactly or are left unchanged. The residual full-sign bits are $\mathbf b_j+\mathbf u$ modulo two. Nothing about the short-label signs is changed. For example the right containing mark still includes $\mu(w)$ from $v_k(w)=\mu(w)\log(k/w)$, whether or not a full sign $\mu(k)$ is now present. This proves (2) and the channel classification without a continuum parity model.

For the comparator let $\mathcal N_{N,Z}=\Sigma(N)B_{\mathcal J}(N)(\mathcal C_{X,Z}/|\mathcal J|)^2$ be the genuine unconditioned normalizer. Write $A_j(a,b)$ for the phase vector after multiplying the R95 row coefficient by four and removing its displayed full-parity factor:

$$
 \bigl(A_O,A_{R_n},A_{R_f},A_{L_n},A_{L_f},A_{D_n},A_{D_f}\bigr)
  =\bigl(-P(a,b),-q_n(b,a),-q_f(b,a),-q_n(a,b),-q_f(a,b),
                       -d_n(a,b),d_f(a,b)\bigr).                \tag{5}
$$

Thus $S_j^{\boldsymbol\varepsilon}$ has comparator $\mathcal N_{N,Z} A_j(a,b)\,\varepsilon_1^{b_{j,1}}\varepsilon_2^{b_{j,2}}/4$. Finite Walsh orthogonality gives comparator $\mathcal N_{N,Z} A_j(a,b)$ for $W_j^{\mathbf b_j}$, zero in all other channels. This establishes the fixed and adaptive old error bounds for the matching and one-full-sign channels just by summing the four R95 errors; it imposes no lower bound on a matching phase that happens to vanish. The faster bounds below do **not** come by summing these old errors.

## 2. Both arm estimates before summing target errors

For the two-full-sign channel the separate arm polynomials for the accepted hard bins each carry a full $\mu(h)$ or $\mu(k)$ along with their own true short sign and mark. Use §2 of the [four actual parity laws](r89-source-four-actual-parity-phases.md), which gives fourth norm $O(X^{3/4}\ell^{-1-1/10})$ for **one arm** with that full sign, both for an ordinary label $h/r$ and for a containing label $Fz$ and their right counterparts. In particular its containing estimate uses the actual $Fz$ integer Perron cutoff with full cofactor sign, not a sign on a real proxy label. The neutral band of the cofactor is separate from the bounded short-label cap, which is why the additional true short sign does not obstruct that arm estimate.

For one common $a,b,Z$, the same finite log bin grid as in R95 has $O(\ell^2)$ accepted pairs per row. A fully accepted pair is an actual convolution after the ordinary unit comparison; Hölder and Parseval therefore bound its target norm by the **product of the two** improved fourth norms,

$$
                     O(X^{3/2}\ell^{-2-1/5}).
$$

Summing over the accepted pairs gives $O(X^{3/2}\ell^{-1/5})$. The $O(\ell)$ ambiguous boundary pairs retain their exact strict or weak integer tests and are bounded positively by the former $O(X^{3/2}\ell^{-1})$ total norm; no full-sign gain on these pairs is claimed. The enlarged external floor slivers and the temporary unit comparison cost no more than the old $O(X^{3/2}\ell/L)$ and arbitrary inverse-logarithmic corrections, which are smaller here. These estimates act on each actual subrow, including the two separate excluded portions of a mixed orbit and both double portions. Thus the two-full-sign channel is bounded in target norm by $O(X^{3/2}\ell^{-1/5})$, giving (3). This argument does not approximate it by a signed Euler scalar.

## 3. A finer common maximum for the zero-comparator channels

Use the actual positive subrow gap envelopes of §2 of the off-axis theorem (and the underlying [axis envelope proof](r94-source-genuine-axis-row-dominance.md)). Multiplication by the Walsh factor on an actual retained pair does not alter the tests, prime factorization, short labels or magnitude of any row mark. The same envelopes bound row changes directly after taking absolute values. For a single floor gap, enlarge the split to the common $Z_0$ supersets and keep the enclosing prime slab on the affected leg; for a split gap take global prime windows on both arms and use the genuine changed-side condition of a gap prime together with failure of an upper $W$-gate. On either axis this provides a pointwise positive comparison **independent of the choices on the other axes**, including all finite row and parity indices. No false regularity of a targetwise parameter path is assumed.

Use the original [marked split threshold](r83-source-full-polynomial-adaptive-split.md) $\tau_*=(\epsilon/16)\log\log\ell/\log\ell$ in $\tau=\log Z/L$. The single initial gap has norm $O(X^{3/2}\ell^{-1/10})$ by the [subpower comparison](r82-source-target-adaptive-subpower-split.md), and the other split gaps of exponent length $d$ have norm $O_H(X^{3/2}(d+L^{-H}))$ at endpoint ratio at most two. A floor gap of length $d$ has norm $O(X^{3/2}(d+\ell/L))$. These are unchanged exact-gate estimates rather than new comparisons made after a parity approximation.

Take a linear mesh on the two floor axes and on the split exponent above $\tau_*$, of spacing at most $\eta=\ell^{-1/10}$. Its split endpoint ratios are at most two since $\eta=o(\tau_*)$. Include $Z_0$ for the initial gap and bracket below on the two floor axes and on the split axis. On each axis the squared maximal error from changing from the bracketed node is bounded by the sum of its squared one-axis envelopes, using the pointwise independence noted above. These sums cost $O(X^3\eta)$ across all axes because $\sum d^2=O(\eta)$ on each, and the initial squared gap budget $O(X^3\ell^{-1/5})$ is smaller. The negligible floor and split terms times the number of gaps still have smaller norm. No normalization calibration is needed here: the comparator is identically zero in every channel being estimated.

There are $O(\eta^{-3})$ nodes, with summed squared cost $O(X^3\eta^{-3}\ell^{-2/5})=O(X^3\eta)$ by (3), and only seven row choices. This proves (4). If $a,b$ are fixed, take instead split spacing $\eta=\ell^{-1/5}$; the gap budget including the initial interval and one-dimensional node budget $X^3\eta^{-1}\ell^{-2/5}$ are both $O(X^3\ell^{-1/5})$. This derives the sharper statement on the exact same split range, not a restricted family of splits.

## 4. The actual change of dominant subrow

Write $U_j=W_j^{(0,0)}=\sum_{\boldsymbol\varepsilon}S_j^{\boldsymbol\varepsilon}$ for the parity-summed arithmetic subrow. On the fixed high rectangle from R95 the rows $L_n,D_n$ are identically absent by the literal left floor. The other five rows are active, and the conditioned winner $R_f$ has sign $-\varepsilon_1$ for every parity. At $\mathbf u=(0,0)$, (2) makes the actual $O$ a two-full-sign cancellation and makes $R_n,R_f,L_f$ one-full-sign cancellations. In particular all four have zero comparator. The remaining row $D_f$ is in its matching channel: its comparator is

$$
                         \mathcal N_{N,Z} d_f(a,b)
                         =\mathcal N_{N,Z}\Phi(a,b).
$$

This is strictly negative with $|\Phi|$ bounded away from zero on the fixed high rectangle, as proved there. It cannot be inferred just from the separate signs of the $R_f$ rows.

Choose the same high rectangle and let the threshold for the R95 maximal row errors be smaller than a fixed fraction of the minimum of $|\Phi|$ and its positive conditioned dominance margins there. On an interior target subwindow $\mathcal N_{N,Z}\gg X$ uniformly in the split. After possibly enlarging the *one* exceptional set by a constant factor, the R95 error applies to all rows, parities and choices at that threshold. Then the four parity-summed zero-comparator rows are individually small against the negative $D_f$, and

$$
             U_{D_f}<0,\qquad
             |U_{D_f}|-\bigl(|U_O|+|U_{R_n}|+|U_{R_f}|+|U_{L_f}|\bigr)
                             \gg X .
$$

At the same targets and true splits, the conditioned $R_f$ comparison still holds. Both are comparisons among genuine actual arithmetic sums, not lists of limiting coefficients. On the whole window the same conclusion of strict dominance and signs follows by trimming endpoint strips of width $X\ell^{-1/60}$ and using the remaining positive overlap in Markov's inequality for the R95 common squared bound. The improved cancellation of individual two-full channels does not improve the required exception scale for this joint dominance comparison.
