# A geometric split mesh for the actual subpower Walsh maximum

Use the [tag-retained subpower theorem](r99-source-tag-retained-subpower-full-sign.md) with precisely the same genuine seven rows, hard physical interval, prime floors, unit conditions, exact long/product tests and ordinary/containing signs. Write $L=\log X$, $\ell=\log L$, $H=\log\ell$, $J=\lfloor H/\log H\rfloor$, and use the original $\theta=1/20$ and small fixed $\epsilon>0$ of the carrier. As before, $0\le a,b\le A_0$ for a fixed finite $A_0$, and the true split exponent $\tau=(\log Z)/L$ ranges over

$$
        \tau_0=2\ell^{\theta-1}\le\tau\le\tau_{\max}=\frac1{8(J+1)}.
                                                                    \tag{1}
$$

In particular the initial split is literally $Z_0=X^{\tau_0}$. For each true Walsh row and bit index use the original number $m_j(\mathbf u)$ of surviving full-cofactor sign factors. This note only concerns $m=m_j(\mathbf u)\in\{1,2\}$, whose comparator is zero. It extends the common maximum, not the fixed-node estimate or the range of splits.

**Theorem.** With both floors allowed to depend independently on the target along with the split, the genuine maximal squared norm satisfies

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
    \sup_{\substack{0\le a,b\le A_0,\ \tau_0\le\tau\le\tau_{\max}\\
                   j,\mathbf u,\ m_j(\mathbf u)=m}}
           |W_j^{\mathbf u}(N;a,b,X^\tau)|^2
                 \ll X^3\ell^{-3m/2}\qquad(m=1,2).                 \tag{2}
$$

When both floors are fixed in common and the split is genuinely target-adaptive, the bound is $O(X^3\ell^{-3m})$ on the same range, uniformly in those floors. If just one of the two floors is fixed in common the bound is $O(X^3\ell^{-2m})$. Constants are allowed to depend on fixed carrier parameters and $A_0$. There is no improvement asserted for the matching channel, the dominance exception count, the full polynomial split range or Hypothesis S.

## 1. A marked positive loss through the initial part as well

The [seven-row gap argument](r95-source-off-axis-right-forbidden-dominance.md), §2, shows that split changes of actual rows are dominated by a positive convolution envelope independent of both floors. Use its global prime/cofactor windows and fixed cap $M<Z_0$ on every short label. On a fixed retained pair every true label, its mark, the parity factor and the pointwise divisor/product tests are unchanged by reallocating the split factors. The same is true of the exactly applied Walsh multiplier of modulus one. The actual distinguished prime is unique throughout the global window. Because the two lower size and arity gates are nested and the true total tagged count is split-invariant, every at-risk operand belongs to the actual fixed base carrier at $Z_0$. The nonempty upper requirement is automatic once the lower size gate holds on this physical support.

For a split gap $[\tau^-,\tau^+]$ within (1), put $v=\tau^+$ and $\xi=\log(\tau^+/\tau^-)$. A genuinely lost operand must have both a prime in $(X^{\tau^-},X^{\tau^+}]$ and a failure at the upper endpoint of either the exact lower-product size cap or the lower arity cap. The strict bottom and weak top are literal, and no prime excluded from the original alphabets can supply the mark. Use a positive polynomial for this changed side at the fixed base split, with all short labels and weight $\log F$, multiplied by the number of occurrences in this gap and the indicator of the upper failure union. The other operand has the original global positive base envelope, with fourth norm $O(X^{3/4})$. This yields a single pair of positive convolutions controlling both orientations of actual loss, uniformly in the other parameters, rather than estimates for individually chosen parameter paths.

We claim that the changed-side polynomial satisfies

$$
 \|\mathcal A_{\mathrm{gap}}\|_4\ll_A
       X^{3/4}\left[
          \xi\left\{\ell^{1-2\log 2}
                 +\exp\!\left(-\frac{\epsilon}{8v}\log\frac1v\right)\right\}
                   +L^{-A}\right]                                  \tag{3}
$$

for every fixed $A>0$, including below the old linear-mesh threshold. This is the **raw** marked bound (7) of the [full polynomial split proof](r83-source-full-polynomial-adaptive-split.md), before dividing its gain by the upper split exponent. We spell out why the proof of that bound applies on the entire present exponential range; its later conversion to an additive linear mesh does not.

In the fixed base polynomial all marked primes are above $Z_0$ and therefore genuinely in the upper product. In the real reciprocal replacement at fixed actual base lower part, the marked measure is exactly one coordinate in the marked hard interval convolved with the old positive upper measure, with the integer count set decreased by one if and only if the marked coordinate is tagged. This is (5) of the full polynomial split proof. Its bounded-variation reciprocal replacement works at arbitrary real interval ends, using only $v\ge\tau_0$: the mark/arity telescoping costs at most a polynomial in total tilted reciprocal mass times its exponential, and that mass is $O(\log\ell+\lambda e^\lambda)$ for the size tilt with $\lambda=\tfrac12\log(1/v)$. Since $v^{-1}\ll\ell^{1-\theta}$, this is $o(\ell)$. The extra weight and its variation cost only a fixed power of $\ell$ per marked coordinate in those telescoping errors. The PNT errors, including deletion of repeat primes, are therefore arbitrary inverse logarithmic without division by the gap width. The hard product interval, original lower masks and exact upper tag selector remain in the comparison. For positive real density bounds the marked coordinate is at most $v\le\tau_{\max}=o(1)$; removing it from the old cofactor argument in $[.4,.6]$ keeps the latter in a fixed compact positive range, separated from the upper measure's atom. Its mass contributes the reciprocal width $\xi$, not an additive floor on the mesh.

For the arity or size loss use respectively the genuine Rankin weights $2^{\omega(W_{X^v})}$ and $W_{X^v}^{\lambda/\log X^v}$, on both true base alphabets; they include eligible upper primes between $Z_0$ and $X^v$. As in the [subpower tilted proof](r82-source-target-adaptive-subpower-split.md), the lower labels cost only a bounded reciprocal-band doubling, and the relative count-tilted major density is $O(\xi\ell)$; the size-tilted bound is $O(\xi\exp(2\lambda+2\lambda e^\lambda+O(1)))$. The fourth norms acquire the factor $X^{3/4}$ from the real major transforms. The hard physical prime/cofactor rectangles, their Perron separation and the auxiliary minor proof are unchanged. In particular the actual integer mark is at most $O(\ell)$, and the pointwise size multiplier is at most $\exp(O(\lambda/v))=L^{o(1)}$, even at $v=\tau_0$. Thus the minor errors remain arbitrary inverse logarithmic, as do the discrete major errors. These are the ingredients of (6)–(7) of the full polynomial split proof, with the original exact tag and all endpoint conditions.

Finally the two possible actual failures contribute the Rankin factors $\ell^{-2\log2}$ and $\exp(-\epsilon\lambda/(2v))$. For the latter the tilt overhead $2\lambda+2\lambda e^\lambda+O(1)$ is at most $\epsilon\lambda/(4v)$ once $v$ is sufficiently small, uniformly here, since $e^\lambda=v^{-1/2}$. This gives (3). Neither a lower bound by the old linear-mesh threshold nor a fixed positive bottom floor has been used. The old auxiliary threshold was introduced only afterwards to replace the factor $\xi$ by a linear-size quantity in the full polynomial interval. Here, as in the seven-row comparison, the proof uses the global base windows and positive all-label polynomial with no target-dependent choices of floor; enlarging to that window does not change the marked reciprocal calculation.

## 2. Spend the reciprocal widths only once

Put $\sigma=2\log2-1$. By $J\log J=(1+o(1))H$, the size exponent in (3) is minimized at $v=\tau_{\max}$, where

$$
 \frac{\epsilon}{8\tau_{\max}}\log\frac1{\tau_{\max}}
                 =\epsilon(J+1)\log(8(J+1))
                 =(\epsilon+o(1))H .
$$

Thus the factor in braces in (3) is $O(\ell^{-c_\epsilon})$ with $c_\epsilon=\min(\epsilon/2,\sigma)>0$. Hölder and Parseval in the genuine positive convolution give one pointwise envelope for each split gap, independent of both floors and of the row and bit indices, whose target norm is

$$
              O_A\bigl(X^{3/2}(\xi\ell^{-c_\epsilon}+L^{-A})\bigr).
                                                                    \tag{4}
$$

The estimate does not assert monotonicity of a signed Walsh row; only the lost supports were nested.

Let $r\in\{0,1,2\}$ be the number of free floor axes. Mesh each free floor axis linearly with spacing at most $\eta$. On the split axis mesh the variable $\log\tau$ with spacing at most $H\eta$, starting exactly at $\tau_0$ and ending exactly at $\tau_{\max}$; the final shortened gap, if any, is kept. The total reciprocal log length is $\log(\tau_{\max}/\tau_0)=O(H)$, so the split also has $O(\eta^{-1})$ nodes, while $\sum_{\rm gaps}\xi^2=O(H^2\eta)$. With the choices below the gap endpoint ratio is at most two. Every split gap, even the first, uses (4); there is no separate untreated initial interval.

Bracket any targetwise chosen tuple at its lower coordinate nodes and change one coordinate at a time. The positive bound on each gap is independent of the other choices. The squared maximum of the changes along an axis is therefore bounded by the sum of the squared envelopes on that axis alone. By (4) the split contribution costs

$$
 O_A\!\left(X^3\{H^2\eta\ell^{-2c_\epsilon}+\eta^{-1}L^{-2A}\}\right)
                  \ll X^3\eta.                                     \tag{5}
$$

The floor changes have the independent genuine prime-slab bounds of the seven-row proof, of norm $O(X^{3/2}(d+\ell/L))$ for a floor gap of length $d$. Their squared sum also costs $O(X^3\eta)$, since $\sum d^2=O(\eta)$ along each axis. The floor and split negligibles in these comparisons are smaller for the fixed powers of $\ell^{-1}$ used below. No product-grid count multiplies either gap budget. The comparator for these channels is identically zero, so no adaptation of a continuum coefficient is needed.

At every node, the fixed common-parameter estimate (2) of the tag-retained subpower theorem costs $O(X^3\ell^{-6m})$, uniformly including all seven true row and bit choices with the given $m$. There are $O(\eta^{-(r+1)})$ nodes. Choosing $\eta=\ell^{-6m/(r+2)}$ makes the total node budget $O(X^3\eta^{-(r+1)}\ell^{-6m})=O(X^3\eta)$, which, with (5) and the genuine floor envelopes, proves all the claims. The supremum can select arbitrary allowed coordinates at each target without a measurability or regularity condition on that selection.
