# The actual largest-prime Walsh carrier without a typical-count mask

Use the seven separate signed divisor rows of the [four-parity comparison](r95-source-off-axis-right-forbidden-dominance.md) and the actual unnormalized Walsh convention of the [Walsh theorem](r96-source-walsh-two-full-and-dominance-switch.md). Keep the same fixed carrier parameters, hard physical window $\mathcal J$, targets $\mathcal X$, true prime floors, squarefree $N$-units, exact integer long/product tests and exterior sign. In particular $L=\log X$,\ell=\log L$,T=L/\ell$,\theta=1/20$,0\le a,b\le A_0$ for a fixed finite floor box, and $Z_0=V_X^2\le Z\le X^{\delta_0}$ is the real split. On each side keep $h=sWU$ with the original old prime, distinct prime alphabets, both excluded neighborhoods, the original hard lower product and count gates $W\le X^{\epsilon/2}$ and $\omega(W)\le2\log\ell$, and the original upper condition $U>1$. Make only the following change to the carrier:

* Remove the typical tagged count requirement on $WU$ altogether.
* Select the distinguished prime canonically, $F=P^+(n)$ when $n=hF$ and $G=P^+(m)$ when $m=kG$. Apply the actual prime floors to these distinguished primes.

Denote the resulting genuine seven Walsh rows by $\widetilde W_j^{\mathbf u}$. The same intrinsic bits $\mathbf b_j$ are defined by their actual marks. This carrier includes the original typically tagged one, but does not require even one tag. It does not remove the two excluded neighborhoods or either of the lower $W$ gates.

Write $\tau=\log Z/L$. Define the exact *new* positive normalization by (1) of the [variable-split law](r81-source-variable-split-local-sign-law.md) with the count selector entirely unrestricted:

$$
 \widetilde{\mathcal C}_{X,Z}
    =\frac{|\mathcal J|}{\ell}
       \sum_{\substack{s,W\\\text{original lower alphabets and gates}}}
       \frac{\varrho_{+,\mathbb Z_{\ge0}}
                  (1/2-\log(sW)/L)}{sW},\qquad
 \widetilde{\mathcal N}_{N,Z}
    =\Sigma(N)B_{\mathcal J}(N)
                    (\widetilde{\mathcal C}_{X,Z}/|\mathcal J|)^2.   \tag{1}
$$

The density here uses the same real allowed prime ranges and excluded neighborhoods as before. Let $A_j(a,b)$ denote precisely the seven phases in (5) of the Walsh theorem, without changing their signs or respective orientations.

**Theorem.** Uniformly, $\widetilde{\mathcal C}_{X,Z}\asymp X$. Put $\sigma=2\log 2-1$ and

$$
 \widetilde E_j^{\mathbf u}(N;a,b,Z)
   =\widetilde W_j^{\mathbf u}(N;a,b,Z)
         -\mathbf1_{\mathbf u=\mathbf b_j}
                         \widetilde{\mathcal N}_{N,Z}A_j(a,b).
$$

At every fixed common $a,b,Z$ the squared target error satisfies

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
             \max_{j,\mathbf u}|\widetilde E_j^{\mathbf u}|^2
                           \ll X^3\ell^{-2\sigma}.                 \tag{2}
$$

For the channel with two surviving full-cofactor signs the fixed squared error is $O(X^3\ell^{-4\sigma})$ (with its exact zero comparator). If floors, true split and row and bit indices can all be chosen independently at each target, the squared norm of the common maximum of $|\widetilde E_j^{\mathbf u}|$ is $O(X^3\ell^{-\sigma/2})$; with fixed common floors and freely moving split it is $O(X^3\ell^{-\sigma})$. Constants may depend on the fixed carrier and $A_0$. This is a signed averaged law for the specified enlarged canonical-largest carrier, not a result for an arbitrary unfiltered divisor sum, a prescribed exceptional target, or Hypothesis S.

## 1. Rooted comparison and the zero-tag bound

On the actual canonical carrier, the containing complete orbits vanish by $\Lambda(h)=\Lambda(k)=0$, since each cofactor is squarefree composite. The [capped long-orbit identities](r85-source-capped-long-floor-orbits.md), (4)–(5), apply verbatim: they use only the actual complementary labels and divisor tests, not the tagged count. Thus each of the seven rows still has the quoted signed expression with its real short labels. Every active cofactor lies in the old global windows $\log h=L/2+O_{A_0}(T)$, and all labels lie below $M=\exp((24+2A_0)T)<Z_0$, by the same geometric argument. Because these labels use only $sW$, their eligibility is independent of the location of the split. The intrinsic Walsh bits still toggle full $\mu(h),\mu(k)$ and not the short signs.

Temporarily use rooted Fourier polynomials: admit every candidate prime $F$ in the stated near-square-root window with physical integer $hF\in\mathcal J$ and the indicated lower/upper factors of $h$. Omit only the comparison condition $F\ge P^+(h)$ and the veto $F\nmid h$, besides the harmless floor/unit separations already in the original bin proof. The rooted rows here are defined by the already-expanded marks; no identity for nonsquarefree $hF$ is claimed. Every rooted term not selected by the genuine canonical-largest/prime-repetition rule has a second near-square-root prime factor in its physical integer, counting a second copy of $F$ if present. Both factors are $\ge \sqrt X\exp(-A_0T-O(1))$, and both are strictly above the whole stable tag band $(2V_X,Y_{*,X}^{1/2})$. Their remaining product is at most $\exp(O_{A_0}(T))$, strictly below $2V_X$ for large $X$. Thus each such removed root lies on an arm with **zero** tags. Similarly there are at most two candidate prime roots per physical integer, since three such factors exceed the hard range. The old root uniqueness in the tagged case follows from the same observation.

To bound the absolute correction, let $\lambda_W$ be the reciprocal prime sum of the true tag at or below $Z$, and let $\lambda_U$ be the real upper tagged reciprocal mass above $Z$. Reciprocal PNT on the lower segment and ordinary integration on the upper, with both exact prime exclusions, give uniformly

$$
 \lambda_W+\lambda_U=(1-\theta)\log\ell
                           -\log(J_X+1)+O(1),
 \qquad J_X=\left\lfloor\frac{\log\ell}{\log\log\ell}\right\rfloor .
                                                                    \tag{3}
$$

A zero-tag arm has no tagged lower prime and its upper measure is free-only. The positive labeled reciprocal mass of its lower profile is $O(\ell\tau e^{-\lambda_W})$: the tag lies above the short-label prime band, so no label multiplier applies there, and removing the exact tagged factors divides the unrestricted positive Euler mass by $\prod_{\mathrm{tag}\cap W}(1+1/p)\asymp e^{\lambda_W}$. Keep the lower caps in the arithmetic polynomial, dropping them only for this positive upper bound. On the compact upper coordinates the upper zero-tag density is $O(\tau^{-1}e^{-\lambda_U})$. Indeed the free-only positive exponential has that total mass bound, and marking one free coordinate as in §2 of the [growing-residual calculation](r75-source-dynamic-giant-growing-rough-residual.md) bounds its density away from zero by the same quantity. The atom does not interfere in the compact-range evaluation.

For the full unbinned positive arm, the cofactor log window has normalized real length $O(1/\ell)$. On the old auxiliary arcs, real major transforms with absolute variation factor $\min(X,|\beta|^{-1})$ have the above density bound times this length: the external endpoint movement is bounded from the same positive density. At fixed rooted $h$ the prime $F$ is still summed in a hard interval by Siegel–Walfisz, with unchanged reduced-numerator factor; the same half-integer Perron separations give arbitrary inverse-logarithmic minor and discrete errors. In the minors a bounded number of candidate roots and the old bounded short-label multiplicity leave coefficient energy $O(XL^C)$ for some fixed $C$; the bilinear coefficients are determined at fixed $h$ and the prime is unrestricted inside its interval. The fourth norm of the rooted positive zero-tag polynomial is therefore

$$
          O\!\left(X^{3/4}e^{-(\lambda_W+\lambda_U)}\right)
          =O\!\left(X^{3/4}(J_X+1)\ell^{-(1-\theta)}\right).        \tag{4}
$$

The full rooted comparison without a tag condition has fourth norm $O(X^{3/4})$ by the same positive calculation. Each genuine difference on the sum line is dominated after the exact row expansion by a constant times the positive convolution with one zero-tag arm and the other full arm, summed over its two orientations. This includes a possible bad root on both sides without any disjointness assumption. Hölder and Parseval make the correction $O(X^{3/2}(J_X+1)\ell^{-(1-\theta)})$ in target norm. This is smaller than $X^{3/2}\ell^{-2\sigma}$. No assumption that every untagged number has a unique candidate root was used. Removing temporary nonunits or the fixed prime-window slivers has the old arbitrary inverse-logarithmic and $O(X^{3/2}\ell/L)$ bounds; the two-root multiplicity changes only constants in those positive estimates.

For example the carrier genuinely permits zero tags on both legs. At any fixed large scale choose distinct primes $F,G$ in a small proportional interval near $2\sqrt X$. Choose distinct old primes $s,s'$ within the original band and distinct upper primes $U,U'$ so that $h=sU$ and $k=s'U'$ are near narrow windows of order $\sqrt X/4$, with $hF,kG$ strictly inside $\mathcal J$. Such choices follow by the prime number theorem on fixed proportional intervals, taking narrower intervals for the first primes if necessary. Set $W=W'=1$. The upper primes lie far above the excluded bands and every original allowed split (whose fixed top exponent is small), the true roots are largest, and all primes can be chosen distinct across the two operands. Their actual sum is an even target in $\mathcal X$. Both giant floors hold for $a=b=0$ and the ordinary pair $d=h,e=k$ passes all three literal long/product cuts. These zero-tag operands do not lie in the original typical-count carrier.

## 2. Real signed arms and the new rooted scalar

Apply the same hard-bin comparison of the [actual four-parity law](r89-source-four-actual-parity-phases.md) to the rooted rows, with upper tag set $\mathbb Z_{\ge0}$. The cofactor factorization $sWU$ for fixed $h$ is still unique; the original signed, unsigned and derivative-mark real evaluations only change this one upper selector. In a fixed bin of normalized width $1/\ell$, the full-sign signed real polynomial uses the *unrestricted-count* comparison from §3 of the [stretched full-sign theorem](r98-source-tag-full-sign-stretched-cancellation.md). No atypical subtraction or changed alphabet enters the current rooted sums. Above the split $Z_*=\exp(T\ell^{1/4})$ the detachable allowed $W$ band from above all labels to $Z_*$ has signed Euler ratio $O(\ell^{-1/2})$; the temporary arity replacement, hard lower size strip and real argument shift cost relative $O(\ell^{-\sigma}+\ell^{-3/4}\log\ell)$. Below that split the signed upper density on the compact range is $O(\ell^{-5})$ by the same full signed Dickman convolution with the excluded-band exponential. These estimates apply to either actual real log mark and to its scaled physical derivative on a common clipped interval. The symmetric differences of intervals as physical $x$ moves have the old positive negligible cost $O(\ell/L)$ in total variation. Thus a genuinely full-sign bin has fourth norm $O(X^{3/4}\ell^{-1-\sigma})$. The no-full-sign or positively enlarged bin has fourth norm $O(X^{3/4}\ell^{-1})$. None of the discrete minor estimates depends on a tag-specific factorization of $F$; the old root energy argument only used bounded multiplicity, as above.

For a fixed common $a,b,Z$, accepted bin pairs are separated convolutions after the temporary unit/floor comparisons. The original boundary lines and their movement are unchanged; the $O(\ell)$ ambiguous pairs keep the literal arithmetic tests and cost $O(X^{3/2}\ell^{-1})$ in target norm when bounded positively. Summing the products of the two bin bounds over $O(\ell^2)$ accepted pairs gives $O(X^{3/2}\ell^{-m\sigma})$ if $m=1,2$ full signs survive. Restoring the canonical-largest conditions costs (4) in target norm times the other arm bound, independent of $m$. In particular $1-\theta>2\sigma$, so both of these rates survive. These channels have zero comparator.

In the matching channel both full-cofactor signs disappear by the actual Walsh projection, leaving only the signed short labels. The genuine rooted bins have the real scalar (6) of the four-parity law with $\varrho_{+,\mathbb Z_{\ge0}}$; the upper set is now fixed. Its real shift, prime-mark and variation errors are still $O(\ell^{-2})$ in a bin. Completing the same reduced rational numerators before absolute values produces $\Sigma(N)B_{\mathcal J}(N)$, with aggregate target error $O(X^{3/2}\ell^{-1})$ including replacement of accepted boxes by their real shapes. All row inequalities giving these shapes are identical to those of the seven-row proof. The raw signed-Euler calculation of the [matching theorem](r97-source-matching-walsh-raw-euler-rate.md) uses the identical measure of short factors, extracted below the tag and split. The upper count selector may be replaced by all counts in the same proof: it is unchanged by the peel, and its unsigned density and Lipschitz norm obey the same compact bounds. Thus each of the seven separate real signed scalars has its original phase $A_j(a,b)$ times $(\widetilde{\mathcal C}_{X,Z}/|\mathcal J|)^2$, with error $O(\ell^{-\sigma}+\log\ell/\ell)$. The unsigned peeled mass is compared to the *new* exact sum in (1), not to the typically tagged mass. The new normalization is uniformly $O(X)$ by the positive density bound and $\gg X$ by inclusion of the old typically tagged real density, whose positive lower bound was proved in the variable-split law. The density comparison on the compact uses the same continuous representatives. Multiplying by $\Sigma(N)B_{\mathcal J}(N)$, then restoring the true largest and squarefree conditions using (4), proves (2). This comparison does not assume that the unconditioned answer equals the old typically tagged one at this precision.

## 3. Truly adaptive floors and split on the enlarged carrier

The true largest prime is intrinsic to a fixed physical integer. On a pair retained at both coordinates the short mark and Walsh parity do not depend on how the split is reallocated. The lower size and arity caps are nested, and $U>1$ holds automatically on the active cofactor windows when the lower size gate holds. Thus the exact positive loss criterion of the [marked split proof](r83-source-full-polynomial-adaptive-split.md) is unchanged: a changed operand needs both a literal gap prime and failure at the upper endpoint of a true lower cap. The positive comparisons now use the global rooted base window with no tag condition. The tilted reciprocal calculation has the same density and moment bounds with its genuine allowed upper set equal to all counts; when marking a tagged coordinate the translated all-count set is again all counts. The comparison at fixed $h$ in prime $F$ and its minor error are still valid with bounded root multiplicity. All these comparisons are positive envelopes independent of the other floor or split coordinates, as for the old seven rows, not regularity assumptions on a selected targetwise parameter path.

In particular above the old threshold $\tau_*=(\epsilon/16)(\log\log\ell)/\log\ell$, split gaps of exponent width $d$ with endpoint ratio at most two have target norm $O_A(X^{3/2}(d+L^{-A}))$. The initial interval below it has positive norm $O(X^{3/2}\ell^{-\sigma})$ by the raw Rankin bound of the matching theorem; this uses no old signed comparator. Floor gaps of width $d$ cost $O(X^{3/2}(d+\ell/L))$ using the genuine enclosing prime slab in the rooted base window. The signed rows themselves need not be monotone.

For the new normalization use the same fixed positive reference prime exponent interval as in the matching theorem, counting ordered rooted $(h,F)$ with weight $\log F$, omitting the greatest-prime and squared-prime vetoes in this calibration only. The positive major evaluation at zero frequency is the length of the reference exponent interval times $\widetilde{\mathcal C}_{X,Z}$, up to $O(X/\ell)$ uniformly, by the unconditioned density and its compact Lipschitz bound. The set of rooted terms in this calibration is nested and any loss meets the same genuine gate criteria. Label $1$ is enough for the positive bound. Thus normalization changes are $O(X(d+\ell^{-1}))$ above $\tau_*$ and $O(X\ell^{-\sigma})$ in the initial interval. This compares the same new quantity (1) independently of the actual two floors, including a floor equal to zero.

Mesh the free floors and the split exponent above $\tau_*$ at spacing at most $\eta$ and use the one initial interval separately. The pointwise maximum of each coordinate change is bounded by its independent positive envelopes, so their squared sum per axis is $O(X^3\eta+X^3\ell^{-2\sigma})$, without a product grid factor. The pointwise comparator change is $O(X|\Sigma(N)|(\eta+\ell^{-\sigma}+\ell^{-1}))$ by the actual normalization and the bounded Lipschitz phases. Its squared norm has no grid factor. At a node (2) costs $O(X^3\ell^{-2\sigma})$. With all three axes moving, choose $\eta=\ell^{-\sigma/2}$ to balance the $O(\eta^{-3})$ nodal budget and the gaps; with one axis moving choose $\eta=\ell^{-\sigma}$. Both widths are $o(\tau_*)$. This proves the common estimates for the genuine largest-prime rows rather than the temporary rooted surrogate.
