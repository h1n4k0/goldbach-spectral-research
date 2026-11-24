# Actual progression increments remove the small aliases of the long quotient product

**Scope.** This removes a range of whole aliases from the genuine residual of R82, not just a further set of conductor components. The sum orientation is absent on this long range. In each difference orientation an exact subtraction of a constant progression vector makes the second raw leg a short progression increment. A conditional Selberg estimate gives the power saving for those actual increments. The larger aliases, the full modulus-frequency variance, and weak S are not estimated.

## 1. Setting and bound

Use the original complete even shell, common transported parent basis, physical scales, the actual raw profiles $h,f$, and the high packet $\mathcal C_+(B,R)$ from [R79](r79-operator-exceptional-centered-product.md) and [R82](r82-operator-low-product-character-long-quotient.md). In each selected frequency its center is the unique reduced $a/b$ with $\lceil B/2\rceil\le b\le B$, with the same exact detuning and normalized Fourier test as there. Retain original local Dirichlet GRH at the even moduli and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including $1$. Use the same common real shell taper $\omega_S$, of endpoint-strip length $O(S)$, $2\le S\le Q/100$, and write $R_*=1+R$.

Let $\mathcal X_{\rm res}(j)$ be the true long high–high product of R82 with its high product and small common-divisor selections, on the exact raw domain $z,w>A$ in its mixed derivative integral. For one alias put $q=2k,\ q'=qb$, as in R79. The high character projection in each leg is fixed at $q,b$ as in [R81](r81-operator-low-conductor-long-quotient.md). Let $K_0\ge1$ satisfy

$$
4QK_0\le A,\qquad 2A\le QH/2 .
 \tag{1}
$$

Define $\mathcal X_{>K_0}(j)$ by retaining exactly the aliases $k>K_0$ in $\mathcal X_{\rm res}(j)$, with every other restriction and weight unchanged. Set $\Delta_A=2A/(QH)$. Then, in the entire common parent space,

$$
\begin{split}
 \mathfrak E_{\le K_0}
  &:=
  \left(\sum_{j\in\mathcal C_+(B,R)}
       \|\mathcal X_{\rm res}(j)-\mathcal X_{>K_0}(j)\|_{\rm HS}^2
        \right)^{1/2}\\
 &\ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B^{3/2}
     \bigg[
        \Delta_A\,\frac M Q R_*^{3/2}
      + \Delta_A^2\left(\frac M Q R_*^{5/2}
                         +\frac M S R_*^{1/2}\right)
      +\frac{K_0}{Q} R_*^{3/2}
      +\sqrt{M K_0}\left(\frac{R_*^{5/2}}{Q}
                         +\frac{R_*^{1/2}}{S}\right)
     \bigg].
 \end{split}
 \tag{2}
$$

The same bound holds after a fixed orthogonal compression or restriction to any subset of Fourier indices, even if selected from the sharp field. The first two terms are for an extra near-edge integration strip, and the last two are for the remaining small-alias difference product.

In particular take the actual R82 parameters

$$
\begin{gathered}
 H=Q^{2/5},\quad M=Q^{3/5},\quad W_V=Q^{23/175}V^{4/7},
 \quad A=Q^{6/5},\\
 B=\lfloor Q^{39/100}\rfloor,\quad R=\lfloor Q^{1/400}\rfloor,\quad
 S=Q^{249/250},\quad
 D_\times=Q^{1/1000},\quad G=Q^{1/5},\quad K_0=Q^{19/100}.
 \end{gathered}
 \tag{3}
$$

Then $\mathfrak E_{\le K_0}\ll_\epsilon Q^{-9/800+\epsilon}$. Combining with R82 (2)–(3) and its sharp-shell comparison inherited from R81 yields

$$
\left(\sum_{j\in\mathcal C_+(B,R)}
       \|\widehat T(j)-\mathcal X_{>K_0}(j)\|_{\rm HS}^2\right)^{1/2}
               \ll_\epsilon Q^{-1/500+\epsilon},
 \tag{4}
$$

and the same for the true prime Gram $\widehat P$. Thus all the relevant $k\le Q^{19/100}$ can be discarded even on the actual exceptional indices of [R78](r78-operator-flat-numerator-most-modes.md). The conclusion concerns this selected Fourier packet, not all moduli or all Fourier indices, and gives no estimate for the remaining $\mathcal X_{>K_0}$.

## 2. The common test and exact constant subtraction

For a fixed $b$ start with a common scalar test $\omega\in C_c^2((Q,2Q))$, before the numerator-specific fractional detunings. Let $K_1=\|\omega\|_\infty+\|\omega'\|_1$ and $K_2=\|\omega''\|_1$. On one entry of a dyad pair $V\le U$, denote the corresponding raw profiles by $U_t(z)=u_{I,t}(z)$, $V_t(w)=v_{I',t}(w)$. The letters $U_t,V_t$ here are functions, with dyad starts $V,U$ as indicated. They are supported in $[0,2QV]$, $[0,2QU]$, and have the actual parameter and spatial envelopes of [R72 (4)–(5)](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes). For an orientation $\sigma$, write

$$
t=(\sigma_1z+\sigma_2w)/k,\qquad
    \mathcal H(z,w)=\omega(t)U_t(z)V_t(w).
 \tag{5}
$$

All expressions involving $t$ are extended by zero outside the support of the test.

The R82 high product-conductor cut, for this common test and a fixed $k,b$, can be applied pointwise to the vector of raw incidences on the full reduced numerator set $(\mathbb Z/b\mathbb Z)^\times$. In fact the finite product-character identity R82 (4)–(6) expresses the dependence on the primitive numerator as a multiplicative character for each surviving pair. Thus imposing $\operatorname{cond}(\nu)>D_\times$ is an orthogonal projection of that vector. It is an $\ell^2$ contraction for arbitrary vectors in the two raw legs, before Taylor factors for detuning. The high individual character projections are fixed orthogonal projections on the actual progression residue vectors; denote their output by $\mathbf F^{\rm hi}(z)$. The condition $(2k,b)<G$ is independent of the numerator. This order is used throughout and does not assert that these restrictions commute with the final differing detunings.

For $k\le K_0$, the sum orientation has no contribution: in that case $z+w=kt\le2QK_0<2A$, whereas both raw coordinates exceed $A$. For each difference orientation first remove the strip $A<z\le2A,\ w>A$ on this dyad pair. This is allowed within the actual mixed derivative integral, without differentiating the strip indicator. The [R80 (4)](r80-operator-early-quotient-resonance.md#2-exact-longlong-reduction-on-the-full-high-packet) estimate with $2A$ in place of $A$ bounds its contribution by the first two terms of (2). Here is why that estimate applies to this restricted product: in the proof of R80 (8)–(10), the removed strip is contained in the raw region with either coordinate at most $2A$; its indicator is common to all numerator coefficients and all Taylor tests. Before detuning the actual high projections are residue norm contractions, as is the additional product projection on the numerator vector. The incidence therefore has the same joint bound as used in that proof. The restriction to $k\le K_0$ and the common-divisor cut are also independent of the test variable and can only decrease the positive upper sums there. In the reversed dyad order make the analogous strip removal in the smaller-support leg, calling that leg $z$ for the rest of the argument.

Now consider $z>2A,\ w>A$ in either difference orientation. Where the common test is supported, $w=z+h$ with $h=\pm kt$, so $|h|\le2QK_0\le A/2$. In particular the lower boundary $w=A$ is outside the support of $\mathcal H$ and of its $z$-derivative. At each fixed such $z$, except possibly the finitely many parent breakpoints on an entry, $\partial_z\mathcal H$ is absolutely continuous as a function of $w$: the raw profiles and the spatial primitives defining them are absolutely continuous, and the mixed derivative has the integrable envelopes of R72. It is zero at $w=A$ and at all sufficiently large $w$. Consequently

$$
\int_A^\infty \partial_{zw}^2\mathcal H(z,w)\,dw=0 .
 \tag{6}
$$

In the exact incidence at fixed $q,b,\sigma,a$, the coefficient of each residue pair or each character pair is independent of $w$. Equation (6) permits replacing the second vector by
$\mathbf F^{\rm hi}(w)-\mathbf F^{\rm hi}(z)$
inside the integral, with no changed term on the boundary or in the benchmark. Equivalently it subtracts $W_{\xi'}(z)$ from $W_{\xi'}(w)$ in the exact selected product of two actual coefficients. This identity holds for each selected character pair and before any bound. Swapping the two raw legs when $U<V$ interchanges the positive difference orientations and preserves the product selection, as well as the negative sum's already empty domain.

## 3. A conditional short progression increment on the actual affine difference

Write $\mathbf F_{q'}(x)=(\psi(x;q',r)-x/\phi(q'))_{r\bmod q'}^*$ for the actual progression discrepancy, with its usual zero extension on nonunit entries. For $X$ in the present polynomial raw ranges and $1\le |h|\le X/4$, we use

$$
\int_X^{2X}
         \|\mathbf F_{q'}(z+h)-\mathbf F_{q'}(z)\|_2^2\,dz
              \ll_\epsilon Q^\epsilon X|h| .
 \tag{7}
$$

This is the explicit-formula estimate of [R59 (4)](r59-operator-balanced-arcs-cuberoot-prefix.md#1-exact-raw-transference-and-a-local-short-interval-input). Its proof applies with the present $q'$: one takes a truncated formula at height comparable with $X$ for the two ends, and uses GRH for the relevant primitive inducing characters. The count of zeros in unit ordinate bins is $O(\log(2q'(|\gamma|+2)))$; the omitted imprimitive prime powers and the explicit-formula errors cost $O((\log(3Q))^2)$ in each increment before averaging. More explicitly, the ordinate split at $X/|h|$, with the local log-coordinate square bound (R59 (5)), gives $O(|h|^2(X/|h|+1)(\log(3Q))^2)$ for the low zero integral and $O(X^2(\log(3Q))^2/(X/|h|))$ for the separate high endpoint sums. Both are $O(X|h|(\log(3Q))^2)$, and the squared pointwise remainder also fits (7) since $|h|\ge1$. Finite character Parseval proves (7). The argument needs only a polynomial bound on $q'$ and the stated auxiliary GRH; no additional upper restriction on $q'$ relative to $X$ is used in the increment estimate. For negative $h$, translate the integration interval by $h$, and cover it by boundedly many comparable dyads; the positive increment proof applies there. The same bound holds for the increment of $\mathbf F^{\rm hi}$ because its character projection is fixed in $z,w,t$.

At a fixed $t\in[Q,2Q]$, use $h=\pm kt$ from the actual difference geometry. Its magnitude is at least $1$ and at most $A/2$. Cover $z\in[2A,2QV]$ by dyadic intervals starting at $2A$, clipping the last one. On each such interval (7) applies. Cauchy–Schwarz with the other leg's pointwise $\sqrt z$ size and the geometric dyad sum give

$$
\int_{2A}^{2QV}\sqrt z\,
      \|\mathbf F^{\rm hi}(z+h)-\mathbf F^{\rm hi}(z)\|_2\,dz
          \ll_\epsilon Q^\epsilon (QV)^{3/2}\sqrt{|h|}.
 \tag{8}
$$

Indeed on a dyad of size $X$ the two squared integrals are $O(X^2)$ for the factor $\sqrt z$ and $O_\epsilon(Q^\epsilon X|h|)$ for the increment. This is an average in the actual lower raw variable with $t$ fixed, not an asserted uniform pointwise saving in every progression.

## 4. Estimate the integrals and restore the exact Fourier indices

For the difference product after (6), the [joint numerator incidence bound R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) is

$$
b\|\mathbf F^{\rm hi}(z)\|_2
        \|\mathbf F^{\rm hi}(w)-\mathbf F^{\rm hi}(z)\|_2 .
 \tag{9}
$$

The high product projection can be applied before taking this norm, by the contraction in §2. The estimates here do not require cancellation between the two positive difference orientations.

We spell out the derivative estimates. The chain rule for (5) is the four-term one of [R80 (7)](r80-operator-early-quotient-resonance.md#3-common-weighted-derivative-on-the-two-early-strips). The terms have respectively zero, one, one, and two parameter derivatives; in the last one the scalar multiplier is $\sigma_1\sigma_2/k^2$, and the derivative is $\partial_t^2(\omega U_tV_t)$. For the first three terms of the bound on (9), the pointwise GRH estimate gives
$\|\mathbf F^{\rm hi}(z)\|_2\ll_\epsilon Q^\epsilon\sqrt{QV}$ and
$\|\mathbf F^{\rm hi}(w)-\mathbf F^{\rm hi}(z)\|_2\ll_\epsilon Q^\epsilon\sqrt{QU}$
on the relevant support when $V\le U$. The common derivative bounds for those three terms are $O(b_Ib_{I'}K_1)$ in $L^1$, as in R76 (5): raw derivatives have fixed $L^1$ envelopes, and a single $t$-derivative is integrated by changing the corresponding free affine variable, canceling its $1/k$. Taking HS and using $\sum_I b_I^2\ll(QV)^{-1}$, $\sum_{I'}b_{I'}^2\ll(QU)^{-1}$ makes $Q\sqrt{VU}\,b_Ib_{I'}$ cost $O(1)$. Summing these terms over at most $K_0$ aliases gives $O_\epsilon(Q^\epsilon b K_0 K_1)$ before shell normalization, also after summing dyad pairs with logarithms absorbed.

For the last derivative term use the stronger increment bound. With $z$ fixed the affine change $w\mapsto t$ gives $|dw|=k\,|dt|$, leaving a factor $1/k$. The bound on $\partial_t^2(\omega U_tV_t)$ is

$$
O_{\Gamma,\Theta}(b_Ib_{I'})
           (|\omega''(t)|+|\omega'(t)|/Q+|\omega(t)|/Q^2)
$$

by the actual parameter envelopes, keeping the supports in the raw variables. At fixed $t$ use $\|\mathbf F^{\rm hi}(z)\|_2\ll Q^\epsilon\sqrt z$ and (8), with $|h|\le2kQ$. Minkowski gives the per-entry contribution in joint numerator norm at most

$$
Q^\epsilon b\,b_Ib_{I'}\,
       \frac{(QV)^{3/2}\sqrt{kQ}}{k}\,(K_2+K_1/Q).
 \tag{10}
$$

The two parent square sums show that the scalar factor other than $b$ and the $K_i$ costs

$$
\frac{(QV)^{3/2}\sqrt{kQ}}{kQ\sqrt{VU}}
                    =\frac{QV}{\sqrt{Uk}}
                          \le Q\sqrt{V/k}
$$

in HS. Thus summing $k\le K_0$ and the dyad pairs yields
$O_\epsilon(Q^\epsilon b\,Q\sqrt{M K_0}(K_2+K_1/Q))$.
Any restrictions on the $k$'s in (1) of R82 only reduce the positive upper estimates at this step. All bounds were for the genuine increment after the exact signed subtraction, without disregarding phases in the definition of the resulting field.

Finally restore the original numerator-dependent detuning by the common Taylor weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field), for each denominator $b$ and fixed integer shift $\ell$ from the nearest center. The effective $K_1$ is $O(1+|\ell|)$, and the effective $K_2+K_1/Q$ is $O(S^{-1}+(1+|\ell|)^2/Q)$. These replacements take place in the just proved **common test** bounds. The Taylor coefficients retain their $2^{-n}$ sup bounds after the character projection, and no projection of an already-detuned field is claimed. Divide by $J\asymp Q$, preserving the outer unit phases exactly. Square-sum over $b$ and $|\ell|\le R+1$, using $\sum b^2\ll B^3$ and shift sums of orders $R_*^3,\ R_*^5,\ R_*$. This gives the last two terms of (2); adding the already estimated strip gives the full result.

At (3) the strip's three component powers are $-9/800,-167/800,-839/4000$. The other three powers are $-177/800,-11/800,-59/4000$. The largest is $-9/800$. R82's original sharp comparison has larger $Q^{-1/500+\epsilon}$ error, so (4) follows without enlarging its GRH range, changing its exact benchmark, or imposing any condition on the omitted exceptional indices.
