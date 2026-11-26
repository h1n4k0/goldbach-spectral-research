# The raw short-Euler rate in the matching Walsh channel

Use the seven actual signed subrows and intrinsic bit vectors $\mathbf b_j$ of the [actual Walsh theorem](r96-source-walsh-two-full-and-dominance-switch.md), with its exact carrier, physical interval, parity convention and unconditioned comparator. In particular $W_j^{\mathbf b_j}$ is unnormalized, $0\le a,b\le A_0$ for a fixed finite $A_0$, and $Z_0\le Z\le X^{\delta_0}$ is the true rough split. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, and set

$$
 \sigma=2\log 2-1>0,\qquad
 E_j(N;a,b,Z)=W_j^{\mathbf b_j}(N;a,b,Z)-\mathcal N_{N,Z}A_j(a,b).
$$

The local factor $\mathcal N_{N,Z}=\Sigma(N)B_{\mathcal J}(N)(\mathcal C_{X,Z}/|\mathcal J|)^2$ and the seven phases $A_j$ are exactly those in (5) of the Walsh theorem.

**Theorem.** Uniformly at every fixed common $(a,b,Z)$,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
          \max_j |E_j(N;a,b,Z)|^2
      \ll X^3\ell^{-2\sigma}.                                    \tag{1}
$$

With fixed common floors and arbitrary target-adaptive true split and row,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
          \sup_{Z,j}|E_j(N;a,b,Z)|^2
      \ll X^3\ell^{-\sigma}.                                     \tag{2}
$$

With arbitrary independently target-adaptive floors, true split and row,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
          \sup_{a,b,Z,j}|E_j(N;a,b,Z)|^2
      \ll X^3\ell^{-\sigma/2}.                                   \tag{3}
$$

The constants may depend on the fixed carrier and $A_0$, not on the chosen parameters at the targets. These are matching-channel error bounds only. They do not give a sharper estimate in a full-sign channel, a better exception bound for the simultaneous dominance switch, or a pointwise result for every modulus.

## 1. Keep the raw rate in the accepted scalar

On every actual squarefree pair exactly one literal parity projector is nonzero. Multiplying it by the matching Walsh character and summing the projectors multiplies the row mark by $\mu(h)^{b_{j,1}}\mu(k)^{b_{j,2}}$ before any analytic comparison. This deletes both intrinsic full-cofactor factors wherever present, since $\mu(h)^2=\mu(k)^2=1$. It does not delete the signs $\mu(r)$ or $\mu(z)$ on the short ordinary or containing labels, nor any unit, prime-floor, divisor or product test. Thus this is the actual no-full-sign arithmetic sum, not the sum of four already-bounded parity errors. The ordinary-ordinary external sign is negative, both split mixed orientations are negative, the double nonlong mark is negative, and the double retained-long forbidden mark is positive. These are the seven separate signs in $A_j$.

Fix $(a,b,Z)$ first. Use the hard log-label bins and integer boundary treatment of the [four-parity proof](r89-source-four-actual-parity-phases.md), §§2–3, in the separate shape form of the [seven-row theorem](r95-source-off-axis-right-forbidden-dominance.md), §2. Restoring the external-floor slivers and the exact $N$-unit mask costs $O(X^{3/2}\ell/L)$ plus arbitrary inverse-logarithmic target-norm error. Among $O(\ell^2)$ bin pairs there are $O(\ell)$ ambiguous ones, each retaining the literal strict or weak tests, with total positively bounded norm $O(X^{3/2}\ell^{-1})$. The accepted signed bins have no full-sign factors in either arm. Their transforms use (6) of the four-parity proof, with $O(\ell^{-2})$ bin density errors and $O(\ell^{-1})$ bin main densities. In the rational completion the reduced numerators are summed before absolute values; hence the sum of these transform errors, including the completion, costs $O(X^{3/2}\ell^{-1})$ in target norm. Passing from the accepted real bins to the area kernels also costs $O(X^{3/2}\ell^{-1})$ by the positive boundary-bin mass. This step only evaluates the accepted part: it does not drop actual equality cases at the moving integer thresholds.

For clarity, put $\tau=\log Z/L$ and let $\mathfrak m_Z$ denote the signed short-label measure in the real scalar, with atoms indexed by the labels $j'\mid sW$, $j'\le M$. Its weight before the area kernel is

$$
 \frac{1}{\ell}\,
 \frac{\mu(j')}{sW}\,
 \varrho_{+,K(W)}\!\left(\frac12-\frac{\log(sW)}{L}\right)
             \delta_{\log j'/T}.
                                                                    \tag{4}
$$

Sum this under the actual lower masks of (6). Section 2 of the seven-row theorem gives the separate ordinary area, the two reflected pairs of mixed areas, and the separate double nonlong and forbidden areas. Applied to any one of them the signed real scalar is an integral against $\mathfrak m_Z\otimes\mathfrak m_Z$ with the corresponding external sign. Each area kernel is bounded, uniformly Lipschitz in each short coordinate, and zero if either short coordinate exceeds $A_0+20$. The original label cap satisfies $\log M/T>A_0+20$. In particular we need not approximate either double row by subtracting independently estimated actual sums.

The short Euler peeling behind §4 of the [capped theorem](r85-source-capped-long-floor-orbits.md) and §4 of the four-parity proof has the following *unrounded* relative error at the bounded scalar scale:

$$
 \rho_\ell=\ell^{\,1-2\log 2}+\frac{\log\ell}{\ell}.
                                                                    \tag{5}
$$

Here are the two estimates giving (5). Peel the $W$ primes up to $e^{AT}$ at a fixed $A>24+2A_0$. They lie below every tag and both removed neighborhoods for all sufficiently large $X$, and in the lower level at every allowed split. The short labels only use these primes and the old prime, and the actual upper selector $K(W)$ is unchanged. Doubling the occupation weight on the fixed eligible log-ratio band covers all label choices; the total positive lower mass is $O(\ell\tau)$, and its normalized $2^{\omega(W)}$ moment is $O(\ell)$. Explicitly the normalized Euler quotient for weights $1\le \nu_p\le2$ is bounded by $\exp(\sum_p\nu_p/p)$, and the sum on the doubled band is bounded while the full lower sum is at most $\log\ell+O(1)$. Replace the actual $2\log\ell$ total count cap by the temporary $3\log\ell$ cap on the low part; later release that temporary cap. Markov on this positive law bounds both discrepancies, respectively, by $O(\ell^{1-2\log 2})$ and $O(\ell^{1-3\log 2})$ after the $O(\tau^{-1})$ density bound and factor $\ell^{-1}$ in (4).

On the temporary cap the low-product logarithm is $O(T\log\ell)$. Moving the hard size cutoff to the retained high product changes only a strip of this width at the original cutoff. Expanding the high-product logarithm into its prime log weights in that strip, where this logarithm is $\gg L$, and fixing the other factors bounds its relative mass by $O((1+T\log\ell)/L)$: in the resulting log interval the remaining weighted prime sum is $O(1+T\log\ell)$. These are positive bounds with the label weights already included. The Lipschitz norm $O(\tau^{-1})$ of the same actual upper density bounds the effect of removing the small factor from its argument, after (4), by $O(\log\ell/\ell)$ as well. This comparison does not change the tag law of the retained factors. The same estimates hold without label multiplicities for the exact unconditioned normalization.

On the detached low part the genuine signed atom has coefficient $-1/(p+1)$ under the positive reciprocal normalization; the old prime gives its two signs at zero and $\log s/T$. As in the capped and four-parity proofs, the convolution exponential comparison follows from the exponentially small repeated-prime error, and reciprocal PNT on the fixed log bands gives the signed measure $\nu=(\delta_0-\pi)*\exp_*(-\lambda_A)$ in the bounded Lipschitz tests, uniformly in the true split. There is no need for total-variation convergence from the discrete atoms to the real densities. The detached positive factors agree with $\mathcal C_{X,Z}/|\mathcal J|$ to $O(\rho_\ell)$ by the same comparison without the sign labels. The mass in absolute value on either arm is bounded, so the two-arm area test costs the sum of the two $O(\rho_\ell)$ losses, not a square-root loss. Thus the real scalar, through its individual signed kernel and external sign, is

$$
       (\mathcal C_{X,Z}/|\mathcal J|)^2 A_j(a,b)
                         +O(\rho_\ell).
                                                                    \tag{6}
$$

The two rates in (5) were rounded earlier to accommodate the full-sign channels. Here neither such channel is present. With $\|\Sigma\|_{\ell^2(N)}\ll\sqrt X$, $B_{\mathcal J}\ll X$, and $\rho_\ell\ll\ell^{-\sigma}$, the error in (6) has norm $O(X^{3/2}\ell^{-\sigma})$ after multiplication by the original local factor. The other errors listed above are smaller, proving (1) with a finite sum over the seven rows.

## 2. Use the raw initial-gap estimates before taking a maximum

Keep the native marked split threshold from the [full polynomial split proof](r83-source-full-polynomial-adaptive-split.md):

$$
                 \tau_*=\frac{\epsilon}{16}
                           \frac{\log\log\ell}{\log\ell}.
                                                                    \tag{7}
$$

For large $X$ it lies above $\log Z_0/L$. In the *single* interval from $Z_0$ to $X^{\tau_*}$ use the raw positive all-label bounds (8)–(9) in the [subpower comparison](r82-source-target-adaptive-subpower-split.md), not its final signed comparison bound. Indeed the changed side has the two actual upper-gate failure alternatives and is dominated by the unmarked positive envelope. Its size and count penalty is

$$
  \ell^{-\sigma}
       +\exp\!\left(-\frac{\epsilon}{8\tau_*}
                                      \log\frac1{\tau_*}\right)
       \ll \ell^{-\sigma}.                                         \tag{8}
$$

Here the exponential term is $O(\ell^{-1})$, since the exponent in magnitude is eventually at least $\log\ell$. The positive domination of the changed row is made with the common cofactor windows, global prime windows and fixed short-label cap of the seven-row theorem. Its mark for any pair retained at both splits is unchanged, including the Walsh multiplier. Thus raw (8) gives an $O(X^{3/2}\ell^{-\sigma})$ target-norm gap envelope *independent of both floors* and of the row. The unchanged arm uses the common bound $O(X^{3/4})$ in fourth norm.

The same raw penalty gives the initial normalization change $O(X\ell^{-\sigma})$. In detail, apply the positive calculation of (8) to the zero-frequency one-arm count in (10) of the subpower proof. Use its fixed nonzero reference prime-exponent interval, chosen in a fixed positive reference floor range as allowed in §5 of the capped theorem. This count keeps the physical interval, original tag, and lower size and count gates, without any test on the paired target. Its mass is the fixed reference interval length times $\mathcal C_{X,Z}$ up to $O(X/\ell)$; label 1 suffices to bound the loss in the count. Hence the assertion applies to the same floor-independent exact $\mathcal C_{X,Z}$ even when one of the two evaluated floors is zero. Replacing that exact calibration by a limiting constant would not justify this maximization.

For upper split gaps of exponent width $d$ above $\tau_*$ and endpoint ratio at most two, the full polynomial split proof uses the actual gap prime **and** upper-gate failure, giving independent positive gap norm $O_H(X^{3/2}(d+L^{-H}))$ for each fixed $H$, and calibration change $O(X(d+\ell^{-1}))$. A floor gap of width $d$ uses the positive enclosing true prime slab with target norm $O(X^{3/2}(d+\ell/L))$. For both kinds of upper gap use the common supersets of the seven-row proof, which do not depend on the other coordinates. On these supersets the prime log marks are bounded by the positive marks as before; the Walsh multiplier and each fixed row test cannot increase an absolute coefficient bound. Thus these are pointwise positive envelopes for a change, with the listed norms, not merely uniform bounds on a fixed-parameter change.

Choose mesh spacing at most $\eta$ along each free floor axis and the split exponent above $\tau_*$, with $O(\eta^{-1})$ nodes per free axis, and include the single initial split gap. In both applications below $\eta=o(\tau_*)$, so the upper endpoint-ratio requirement holds. Bracket any chosen tuple at its coordinate nodes. The sum of squared envelopes over each upper axis costs $O(X^3\eta)$ since the total length is bounded and $\sum d^2=O(\eta)$; the floor enlargements and inverse-logarithmic errors cost less. The initial squared gap norm is $O(X^3\ell^{-2\sigma})$. Because these envelopes are independent of the other axes, there is no product grid factor in either cost. The precisely calibrated comparator changes pointwise by at most

$$
     O\!\left(X|\Sigma(N)|
                (\eta+\ell^{-1}+\ell^{-\sigma})\right)
                                                                    \tag{9}
$$

using the bounded Lipschitz row phases and $\mathcal C_{X,Z}\ll X$. The squared norm of this comparator bound has no node factor either.

For (2) take $\eta=\ell^{-\sigma}$ with one free axis. The budget from (1) on the grid is $O(X^3\eta^{-1}\ell^{-2\sigma})=O(X^3\eta)$. For (3) take $\eta=\ell^{-\sigma/2}$ with three free axes. The node budget is $O(X^3\eta^{-3}\ell^{-2\sigma})=O(X^3\eta)$. In both cases the gap bounds and (9) complete the true target-adaptive estimate with the exact comparator, which proves (2)–(3). No other Walsh channel is part of these bounds.
