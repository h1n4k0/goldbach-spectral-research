# Opposite arithmetic signs of the genuine giant parity pieces

Use the genuine both-leg carrier of the [capped long-floor theorem](r85-source-capped-long-floor-orbits.md) at the exact floor choice $a=b=0$. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\rho,\Delta,\theta,\epsilon$ as in that theorem, $\mathcal J=[X/2,(1+\Delta)X/2]$, and $\mathcal X=[X,(1+\Delta)X]$. The two actual distinguished primes satisfy $F,G\ge\sqrt N$, including equality when possible. Keep the original real split $Z_0=V_X^2\le Z\le X^{\delta_0}$, the actual old prime and prime exclusions, all squarefree unit and $W,U$ gates, and the actual typical count on the entire $WU$ in each cofactor. In particular $h=sWU$ and $k=s'W'U'$ have their actual split, and $n=hF,m=kG$ lie in $\mathcal J$, $n+m=N$. Neither the actual integer cuts $d>D_N,e>D_N,de>Q_N$ nor the external minus is changed. Here $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor Ne^{-20T_N}\rfloor$ and $T_N=\log N/\log\log N$.

For each $\varepsilon_1,\varepsilon_2\in\{-1,1\}$ additionally keep only $\mu(h)=\varepsilon_1,\ \mu(k)=\varepsilon_2$. These are the two genuine cofactor parities, not the parities of any short divisor labels. Write $R_{N,Z}^{[\varepsilon_1,\varepsilon_2]}$ for this signed part of the original sum. As before retain the **unconditioned** positive normalization $\mathcal C_{X,Z}$ of the [common-split law](r81-source-variable-split-local-sign-law.md); the four parity slices will have explicit factors in their coefficients. Set

$$
 \begin{split}
 \mathcal L_{N,Z}^{[\varepsilon_1,\varepsilon_2]}
       &= -\frac{\varepsilon_1\varepsilon_2}{4}\Psi(20)\,
           \Sigma(N)B_{\mathcal J}(N)
            \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2,\\
 B_{\mathcal J}(N)&=|\mathcal J\cap(N-\mathcal J)|.
 \end{split}
 \tag{1}
$$

Here $\Sigma$ is the binary singular series and $\Psi$ is the uncapped short-prime phase. The [Dickman sign theorem](r86-source-dickman-capped-phase-chart.md) gives $\Psi(20)<0$, since its unique positive zero is less than $51/5$.

**Theorem (unconditional).** For one common $Z$ in the full allowed range and any of the four parity pairs, uniformly,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \left|R_{N,Z}^{[\varepsilon_1,\varepsilon_2]}
                          -\mathcal L_{N,Z}^{[\varepsilon_1,\varepsilon_2]}
       \right|^2\ll X^3\ell^{-1/5}.
 \tag{2}
$$

Moreover, allowing both the parity pair and the split to be chosen independently at each target, there is the simultaneous estimate

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
    \sup_{\substack{Z_0\le Z\le X^{\delta_0}\\
                    \varepsilon_1,\varepsilon_2\in\{-1,1\}}}
       \left|R_{N,Z}^{[\varepsilon_1,\varepsilon_2]}
                       -\mathcal L_{N,Z}^{[\varepsilon_1,\varepsilon_2]}
       \right|^2\ll X^3\ell^{-1/10}.
 \tag{3}
$$

Thus on each fixed interior subwindow, simultaneously for every split, each same-parity piece is strictly positive and each opposite-parity piece is strictly negative, of magnitude $\gg X$, outside a common $O(X\ell^{-1/10})$ exceptional set of even targets. On the full window the strict signs hold outside one common $O(X\ell^{-1/30})$ set. Their leading phases cancel on summing all four parity pairs, as required by the unconditioned giant cancellation. The theorem is only for this prescribed giant carrier, not a pointwise sign on every target, an assertion on other parity-conditioned carriers, or Hypothesis S.

## 1. Exact elimination at the literal giant floors

Whenever an opposite label $e$ is long, $e\ge D_N+1>\sqrt N e^{-20T_N}$. Hence the actual $F\ge\sqrt N$ gives $Fze>Q_N$ for every $z\mid h$, including $F=\sqrt N$ if that equality occurs. All $F$-containing labels are long, and their complete signed inner sum is $-\Lambda(h)=0$, since $h$ is squarefree composite. This cancellation takes place on each selected pair, so it is valid under either parity mask. The same reasoning on the other arm leaves only ordinary long labels $d=h/r$, $e=k/t$, $r\mid h$, $t\mid k$, with the genuine three strict tests and signed weight

$$
       -\mu(h)\mu(k)\mu(r)\mu(t)\log(Fr)\log(Gt).
$$

In particular we apply the orbit identity before replacing any literal prime floor or using a positive bound.

On every surviving true term $h,k\ge H_-=\frac12\sqrt X e^{-20T}$, since they are at least their long labels. The corresponding upper window is $H_+=(1+\Delta)\sqrt X/2$ by the true giant floor and $\mathcal J$. All omission labels are at most $M=\exp(21T)$, using $h/D_N,k/D_N\ll e^{20T}$. This is still true on our fixed comparisons. For large $X$ the cap is below the smallest split $Z_0$, so each omission label divides the genuine $sW$ for every split and its arity is bounded. No upper label or parity is inferred from a real model.

For the remaining ordinary row replace the true lower prime floor temporarily by $\sqrt X$ and restrict the prime above by $\sqrt X e^{20T}$. The lower difference occupies a fixed log-width-$O(1)$ sliver, since $N/X$ is in a fixed compact interval. The possible upper difference, before that restriction, lies in a similarly narrow sliver because $h\ge H_-$ and $hF\le(1+\Delta)X/2$. Retain the fixed cofactor interval $[H_-,H_+]$ in these enlarged positive comparisons. On the comparison $F\ge\sqrt X$ the distinguished factor is unique, since two factors at least $\sqrt X$, including repetitions, would force the product to be at least $X>\max\mathcal J$. In the final fixed prime interval the cofactor window is automatic at each physical $x=hF\in\mathcal J$. In all comparisons only the ordinary row is used; a containing sum on the enlarged prime window has not been asserted to cancel.

The [finite-orbit positive Fourier bound](r77-source-finite-short-orbit-product-boundary.md) for an all-label arm in a fixed $O(1)$ log prime sliver is $O(X^{3/4}\ell/L)$ in fourth norm, against $O(X^{3/4})$ on the unrestricted opposite window. This bounds the restoration error by $O(X^{3/2}\ell/L)$ in target $\ell^2$, also after imposing genuine parities. Removing a unit restriction for a convolution temporarily costs individually $O_A(XL^{-A})$ for every fixed $A$: each common prime divides $N$, is at least $e^{5T/4}$ and forces the first operand to be a multiple of it; there are $O(\ell)$ such candidates. Fixed polynomial logarithmic weights and the bounded-arity label multiplicities are absorbed in this exponential saving.

For every integer operand the exact parity projector is

$$
          \mu(h)\mathbf1_{\mu(h)=\varepsilon}
                            =\tfrac12(\mu(h)+\varepsilon).
 \tag{4}
$$

It is legitimate because the genuine $h$ is squarefree. We will suppress every term in the expanded product having a **full** cofactor Möbius sign on at least one arm. The surviving bit has coefficient $-\varepsilon_1\varepsilon_2/4$ and the two short signs $\mu(r)\mu(t)$ with genuine log marks. In particular no assertion that the conditioned integer sets individually have half of the full *signed* weight is used.

## 2. The genuine ordinary label bins and the parity projection

Use the exact ordinary label coordinate $\gamma=(\log(h/r)-L/2)/T$ (and its counterpart on the right), with hard bins of width $\ell^{-1}$. On the fixed window and cap its full range is bounded. For each bin, the usual finite-orbit fourth-norm bounds are $O(X^{3/4}\ell^{-1})$ for positive or short-signed coefficients, and $O(X^{3/4}\ell^{-1-1/10})$ for the coefficient with additional $\mu(h)$. To apply the latter, one can use the neutral lower-prime band from $e^{22T}$ to $V_X/4$. It is present in $W$ at every split, above every omission choice and below the true tag interval; it does not affect the upper count set. Its reciprocal mass $\theta\log\ell+O(1)$ gives the signed gain after the same small lower-factor detachment, cutoff strip and count-moment estimates as in the [growing-rough proof](r75-source-dynamic-giant-growing-rough-residual.md). This is precisely the prior ordinary-arm estimate, now on a fixed hard prime interval of width $20T$; the hard label $h/r$ already lies in the cofactor coefficient. The minor bound uses the half-integer separation of the integer product $hF$ and does not substitute a smooth physical cutoff.

Both $\log D_N=L/2-20T+O(1)$ and $\log Q_N=L-20T+O(1)$ on the window. Thus in this label grid the true coordinate tests and product test have only $O(\ell)$ ambiguous bin pairs, and there are $O(\ell^2)$ possible bin pairs. The tests, including equality where relevant for rejecting a strict test, are applied literally within the ambiguous blocks and dominated by positive bin convolutions. Their norm is $O(X^{3/2}\ell^{-1})$ by Hölder and Parseval. Each fully accepted pair is valid for every target in the window, so provides the exact separated convolution after the preceding fixed floor and unit comparisons. In the expansion (4), any term with at least one full parity factor has fourth-norm gain $\ell^{-1/10}$ on that arm; summing the norm over at most $O(\ell^2)$ pairs bounds all such terms by $O(X^{3/2}\ell^{-1/10})$ in target $\ell^2$. They do not contribute to the leading term. Only the bit with two short signs, multiplied by $-\varepsilon_1\varepsilon_2/4$, remains to be evaluated.

Let $I$ be an ordinary label bin, and let $A_I$ be its actual short-signed no-full-parity polynomial, with marks $\mu(r)\log(Fr)$. Define its real scalar

$$
 c_I=\frac1\ell
       \sum_{\substack{s,W\\\text{actual lower masks}}}
         \sum_{\substack{r\mid sW\\r\le M}}
           \frac{\mu(r)}{sW}\,
            \varrho_{+,K(W)}\!\left(\frac12-\frac{\log(sW)}L\right)
             \left|\bigl(I+\log r/T\bigr)\cap[-20,0]\right|,
 \tag{5}
$$

where $\varrho_{+,K(W)}$ is the exact count-restricted upper reciprocal density at the chosen split. On the auxiliary polylogarithmic major arc at a reduced numerator of denominator $q$, the actual polynomial is the real transform of $c_I\mathbf1_{\mathcal J}$, with an absolute error of size $O(\ell^{-2}\min(X,|\beta|^{-1}))$ in the real transform, times $\mu(q)/\varphi(q)$, and the same arbitrary inverse-logarithmic discrete errors as in the common-split law. We check this new ordinary scalar, because the label $h/r$ differs from a short containing choice.

At fixed $h,r$ use Siegel–Walfisz on the hard prime interval and the real mark $1+\log r/\log F$ after extracting the prime log. All prime factors of $h$ are above the polylogarithmic denominators. Keep the exact label condition in selecting $h,r$ in this step. At physical $x=hF$, write $\alpha=(L/2-\log F)/T\in[-20,0]$. Then the **actual** real label coordinate is

$$
       \gamma=\alpha-\log r/T+(\log x-L)/T .
$$

Consequently the interval of integration in $\alpha$ is exactly
$\bigl(I+\log r/T-(\log x-L)/T\bigr)\cap[-20,0]$.
Also $d\log h/L=d\alpha/\ell$ at fixed $x$. The density argument is $\frac12+\alpha/\ell+(\log x-L)/L-\log(sW)/L$, lying in the same compact $[.4,.6]$ as before. The Lipschitz bound $O(\tau^{-1})$ of the density at $\tau=\log Z/L$ combines with the positive lower labeled reciprocal mass $O(\ell\tau)$. On the bin's normalized width at most $\ell^{-1}$, replacing the argument by that in (5) and the mark by one has absolute cost $O(\ell^{-2})$ after the prefactor $\ell^{-1}$. Dropping the physical shift in the interval endpoints costs $O(1/T)$, smaller than this. This is an absolute positive error bound regardless of cancellation in $c_I$.

For variation of the real error in physical $x$, shifting $x$ to $y$ changes the moving integration endpoints by at most $O(|x-y|/(XT))$, even after clipping. On the common part the mark depends on $\alpha,r$ but no longer on $x$, and the density variation there is $O(\tau^{-1}|x-y|/(XL))$. The resulting variation error is $O(1/T)$ on $\mathcal J$; the jumps from restricting to $\mathcal J$ are at most the preceding supremum bound. This gives the claimed transform estimate using the usual bounded-variation integration by parts. The discrete-to-real reciprocal count approximation and Siegel–Walfisz retain arbitrary inverse-logarithmic precision uniformly in the real split, as their proofs handle the hard cofactor interval and its piecewise smooth mark uniformly; the physical shifted endpoints remain literal until this step. The auxiliary minor estimates are unchanged by removing the full parity, because its modulus was at most one. The coefficients in (5) satisfy $|c_I|\ll\ell^{-1}$ and bounded sum of absolute values, by the positive labeled bound.

## 3. The ordinary triangle and its exact signed phase

For the surviving short-signed bit, the accepted bin pairs have scalar $c_Ic_{I'}$. The common-split rational completion applies without change: sum reduced numerators before absolute values, use $\|c_q(N)\|_{\ell^2}/\varphi(q)^2\ll_\xi\sqrt X\,q^{-3/2+\xi}$ for squarefree $q$, and obtain $\Sigma(N)B_{\mathcal J}(N)$ times the real scalar. The $O(\ell^2)$ products of the bin error from §2 cost $O(X^{3/2}\ell^{-1})$ in the target norm, by the pointwise $O(\ell^{-2})$ bin error and $O(\ell^{-1})$ bin main scale. The arbitrary inverse-logarithmic discrete errors and the auxiliary minor estimates are negligible. When passing to the fixed real cut region its disagreement with completely accepted bin pairs is at most $O(\ell)$ boundary pairs, costing $O(\ell^{-1})$ in the real scalar. This replacement is only in the absolute-controlled boundary error.

In the resulting scalar use $u=\log r/T$, $v=\log t/T$, and $\gamma=\alpha-u,\ \gamma'=\alpha'-v$ with $\alpha,\alpha'\in[-20,0]$. The two long cuts are $\gamma,\gamma'\ge-20$ and the product region is $\gamma+\gamma'\ge-20$. Both coordinates are at most zero, so the diagonal already implies the two long conditions. The available upper endpoints are $-u$ and $-v$. The lower endpoints from $\alpha,\alpha'\ge-20$ remove no positive area: in distances $s,s'\ge0$ below the upper endpoints the diagonal requires $s+s'\le20-u-v$, always with both distances at most $20$ if there is area. Thus the actual limiting area as a function of its two short labels is

$$
                          \tfrac12(20-u-v)_+^2.
 \tag{6}
$$

The sign of this area is the one from (4), not the sign of the containing-branch triangle on two below-square-root floors. All actual integer coordinate boundaries and the physical shifts were retained or bounded in the stated positive errors before reaching (6).

The signed Euler average in (6) is exactly the $\Psi(20)$ average per unit positive normalization. To justify the quantitative error here, use the [signed low-factor peeling](r85-source-capped-long-floor-orbits.md) on the real scalar (5). All short labels have exponent at most $21$ and the test (6) is uniformly bounded and Lipschitz, with support in each coordinate at most $20$. Separate the old prime and the lower factors up to $e^{21T}$, lying below the genuine tag range and every split. Short-label choices in absolute value at most double the lower reciprocal occupation in this fixed log-ratio band, so the $O(\ell\tau)$ positive bound and the normalized $2^{\omega(W)}$ moment $O(\ell)$ hold. Temporarily relaxing the actual lower count and restoring it in the high normalization costs $O(\ell^{1-2\log 2})$. The log size of the temporarily capped low part is $O(T\log\ell)$; peeling it shifts the hard size strip and the same upper density by normalized $O(\log\ell/\ell)$, using the original positive marked strip bound and the Lipschitz bound for the same $K(W)$. The low part is untagged, so $K(W)$ is not changed in the residual upper density.

Each included low divisor prime contributes exactly $-1/(p+1)$ under its positive reciprocal occupation; the old prime contributes its exact signed difference at zero and its actual log size. Reciprocal PNT and the convolution exponential then give the same signed measure $\nu$ in each arm as in the Dickman theorem, including the cutoff-independence on the active label support. The error of the elementary prime-factor product against its signed convolution exponential is exponentially small by the square-prime reciprocal sum; the passage to the continuous fixed log-ratio intervals has arbitrary inverse-log error for this bounded-variation area. The positive high normalization, after comparison with the original unconditioned lower masks, is exactly $\mathcal C_{X,Z}/|\mathcal J|$ up to the same absolute $O(\ell^{1-2\log 2}+\log\ell/\ell)$ error. No parity-conditioned normalization is inserted at this step. Consequently the surviving bit has real scalar

$$
        \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2
              \iint \tfrac12(20-u-v)_+^2\,d\nu(u)d\nu(v)
                           +O(\ell^{-1/10})
          =\left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2
                    \Psi(20)+O(\ell^{-1/10}).
$$

Multiplying by its coefficient $-\varepsilon_1\varepsilon_2/4$ gives exactly (1), with the same $\Sigma(N)B_{\mathcal J}(N)$ multiplier. The arithmetic floor, unit, seam and signed-bit errors already have target norm $O(X^{3/2}\ell^{-1/10})$, and the scalar error has that norm because $B_{\mathcal J}\ll X$ and $\|\Sigma\|_{\ell^2(N)}\ll\sqrt X$. This proves (2) for the true parity slices.

## 4. Actual targetwise split and parity choices

Use the [full split gap comparison](r83-source-full-polynomial-adaptive-split.md), now with the fixed giant windows and the ordinary row of §1. The applicability is direct: on the active cofactor window the $W$ size and arity gates nest as $Z$ increases, and $U>1$ is automatic once the size gate holds. The total true tag count and $\mu(h),\mu(k)$ are invariant when factors move between $W$ and $U$ at fixed $h,k$. All label caps are below $Z_0$, so their enumeration and signed marks are also unaffected for a pair that survives the change. Thus a difference inside a split gap still requires simultaneously a genuine prime in that gap and failure of a genuine lower gate at the top of the gap. The same positive comparison bounds every parity slice, even after dropping the two sign masks on its positive right; it does not drop either mask in the true coefficient.

Use exponent mesh $\tau=\log Z/L$ of width $\eta=\ell^{-1/10}$, starting its linear part at $\tau_*=(\epsilon/16)\log\log\ell/\log\ell$ as in that proof. The marked Rankin calculation gives each upper-gap target norm $O_A(X^{3/2}(\Delta\tau+L^{-A}))$, and applies to arbitrary inverse-log precision for the last gap as well. It uses fixed prime/cofactor windows of log width $O(T)$, the exact marked count decrement and the genuine positive gate failure. These hypotheses all hold here, with ordinary short labels cap $M$ and the positive prime mark $\log F$. The part below $\tau_*$ is bounded against the base split by the unmarked positive Rankin comparison of the [subpower split theorem](r82-source-target-adaptive-subpower-split.md), with target norm $O(X^{3/2}\ell^{-1/10})$, again one bound for all parity choices. These comparison arguments act on the actual ordinary row, after the exact containing cancellation, and thus are unchanged by the parity selection.

For the change in the exact comparator across split gaps the original calibration of $\mathcal C_{X,Z}$ applies unchanged: that normalization is independent of the prime floor and of the parity slice. One may use the earlier fixed positive reference prime interval to calibrate the same unconditioned normalization. Equivalently here choose a fixed normalized prime interval strictly inside $(-1,0)$ in $\alpha$ and use the prime mark $\log F$; all its primes exceed the actual giant floor for large $X$, and the standard count-sensitive reciprocal density gives its physical mass as the interval length times $\mathcal C_{X,Z}$ up to $O(X/\ell)$. The marked gap and initial subpower estimates at frequency zero then bound the comparator variation as in the full split proof. No calibration of a prescribed parity support is required, since the factor in (1) is an exact outcome of the projector (4).

At the $O(\eta^{-1})$ mesh nodes apply (2), uniformly in all four sign choices. Taking the square of the maximum over nodes costs at most their sum of squares, $O(X^3\eta^{-1}\ell^{-1/5})$. The split-gap estimates give $O(X^3\{\sum (\Delta\tau)^2+\eta^{-1}\ell^{-2}\})=O(X^3\eta)$, including normalization errors, and the lower subpower piece has smaller cost. This proves (3); no common sign or split is imposed between different targets. Finally $\mathcal C_{X,Z}\asymp X$ uniformly, the singular series is absolutely bounded below on even targets, and $\Psi(20)<0$. Thus the local term in (1) has the asserted sign and interior order-$X$ size. For the full window discard endpoint strips of width $X\ell^{-1/30}$ and apply (3) to any remaining target with a wrong sign for any split or parity choice, where the local magnitude is $\gg X\ell^{-1/30}$. This gives the stated common exceptions. The cancellation of the four leading terms is the exact sum of the four factors $-\varepsilon_1\varepsilon_2/4$; it does not give a sign or a pointwise theorem for the parity-unconditioned remainder.
