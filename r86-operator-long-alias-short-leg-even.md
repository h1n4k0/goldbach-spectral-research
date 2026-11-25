# The even short-leg sector of the actual larger aliases

For a sufficiently large alias on a dyad pair with a short physical leg, only one positive difference orientation can occur. Reflecting the short residue identifies its even-character part with the negative sum incidence. The two actual signed kernels then differ only by a shift in the real modulus parameter. This deletes the auxiliary-even short leg on low physical annuli, even when the alias and the other physical annulus are much larger than the short-alias cutoff. The odd short leg does not have this cancellation.

## 1. Setting and assertion

Keep the complete even shell, genuine $h,f$ profiles in the transported parent basis, separated high-denominator packet $\mathcal C_+(B,R)$, and common smooth shell taper $\omega_S$ of [R85](r85-operator-skew-translation-all-short-aliases.md). Use its exact normalized modulus transform $J^{-1}\sum_m$ for $N=2m$. Assume the original local Dirichlet GRH at the even targets and auxiliary Dirichlet GRH through $\lceil 8MB\rceil+2$, including modulus $1$. The long field $\mathcal X_{\rm res}$ is exactly the [R82](r82-operator-low-product-character-long-quotient.md) residual: the raw integration restriction $z,w>A$, both of the actual high individual character selections, the high product conductor selection, and $(2k,b)<G$. Its two difference signs are positive and its sum sign negative. Write $R_*=1+R$ and $\mathcal Z_{>K}$ for the same field restricted to $k>K$, as in R85.

Take a threshold $H\le P\le M$ on the shorter physical dyad and a cutoff $K$ with $K\ge 2P$ in the R85 regime. On pairs of **distinct** physical dyads, call their starts $V<U$ in increasing order, independent of which matrix index is first. Define $\mathcal E_{P,K}$ to be the exact part of $\mathcal Z_{>K}$ in those pairs with $V\le P$ in which the true high progression vector on the shorter leg is projected to its **even characters of the auxiliary modulus $q'=2kb$**. Use both matrix orders, and use the original orientations and signs, phases, product projection and the sharp raw integration restriction. This deletes no even part on equal dyads, no odd part on any dyad, and nothing on pairs whose shorter dyad starts above $P$.

Then

$$
\left(\sum_{j\in\mathcal C_+(B,R)}
         \|\mathcal E_{P,K}(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B^{3/2}P
          \left[\frac{R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{1}
$$

The same estimate holds after compression by fixed orthogonal projections or restriction to any subset of the packet. In the proof, the selected $k$'s may be further restricted by any mask independent of the primitive numerator and common to the paired sum and difference orientations.

In particular, at the exact R85 parameters, take $K=\lfloor Q^{81/200}\rfloor$ and $P=K/2$. The right side of (1) is $O_\epsilon(Q^{-3/800+\epsilon})$, even for pairs with $U$ near $M=Q^{3/5}$ and aliases up to their actual support limit $4U$. In consequence the sharp $\widehat T$ and $\widehat P$ each differ from $\mathcal Z_{>K}-\mathcal E_{P,K}$ by $O_\epsilon(Q^{-1/500+\epsilon})$ in this packet norm, by the R85 comparison. This adds a deletion **among** the larger aliases, not a range of whole larger aliases. The remaining field, in particular the odd short leg and the large–large dyad pairs, is not estimated. The theorem gives neither a bound on all Fourier modes nor a pointwise modulus or weak-S conclusion.

## 2. Reflection in the exact switched incidence

Fix $b,k$, a pair $V<U$ as in §1, and one matrix entry. Relabel the two raw coordinate names if necessary so $z$ is the coordinate on the shorter dyad; the $+,-$ and $-,+$ orientations interchange under this relabeling. Put $X=QV,\ Y=QU$, and let $U_t(z)$, $V_t(w)$ denote the two actual profiles for this pair of parent entries. Write $q=2k,\ q'=qb$, and $F(z)=F^{\rm hi}_{q'}(z)$ for the true centered residue vector with its high selection from [R81](r81-operator-low-conductor-long-quotient.md). Let $\mathcal R F(r)=F(-r)$ on the unit residues modulo $q'$, and set $F^{\rm ev}=(F+\mathcal R F)/2$. This projection is an $\ell^2$ contraction. It commutes with the high individual projection because both are diagonal in the Dirichlet character basis; the even condition is $\xi(-1)=1$ on the short character, not $\nu(-1)=1$ on the product.

For the two relevant orientations denote the exact negative rational incidence from R82 (4) by $A_a^{-+}$ and $A_a^{++}$. Their matrix entries are the unit-residue indicator of $q\mid\sigma_1 r+\sigma_2 s$ times $e(-a(\sigma_1 r+\sigma_2 s)/(qb))$, with the same two unit sets. Therefore

$$
A_a^{++}(r,s)=A_a^{-+}(-r,s),\qquad
 (F^{\rm ev}(z))^{\mathsf T} A_a^{++} F(w)
       =(F^{\rm ev}(z))^{\mathsf T} A_a^{-+} F(w).
 \tag{2}
$$

Both statements are exact modulo $q'$, including all non-coprime $q,b$ covered by R82. The equality in (2) holds for the whole reduced numerator vector, so applying the high product conductor projector $\Pi_\times$ preserves it. Equivalently reflecting the short leg multiplies each short character coefficient by $\xi(-1)=1$ and does not change the product character. Likewise it does not alter $(2k,b)<G$. This reasoning is before the distinct fractional detunings.

The $+,-$ orientation cannot appear in this ordering, since $z\le2QV$ and $k>K\ge2V$, so $(z-w)/k<Q$. This assertion is also true of its mixed derivative on the support, since the common parameter test and its derivatives are supported strictly within $(Q,2Q)$. For a common scalar test $\omega\in C_c^2((Q,2Q))$, set

$$
t_-=(w-z)/k,\qquad t_+=(w+z)/k,\qquad
 \mathcal H_\pm(z,w)=\omega(t_\pm)U_{t_\pm}(z)V_{t_\pm}(w).
$$

Products containing $\omega$ and their derivatives are extended by zero in the parameter outside its support. By the original $+,-$ signs on the two surviving terms and (2), the even short-leg contribution is the integral on $z,w>A$ of the same numerator vector against

$$
\partial_{zw}^2\mathcal H_- -
                                  \partial_{zw}^2\mathcal H_+ .
 \tag{3}
$$

The first sign here is from the $-,+$ difference orientation and the second from $+,+$. No raw cutoff has been differentiated or changed. If instead the short leg were odd, the reflection in (2) would introduce $-1$, and (3) would be a sum rather than a difference.

## 3. Bound the integrated difference at a fixed alias

We first prove a common-test bound. Use the exact [R72 (4)–(5) envelopes](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes). Thus the sup of $Q^j\partial_t^j U_t$ for $0\le j\le2$ is $O(b_I)$, its spatial-derivative envelope $G_I(z)$ is independent of $t$ and of $L^1$ norm $O(b_I)$, and the support is contained in $[0,2X]$. For the other profile use $b_{I'},G_{I'}(w),[0,2Y]$. We will use

$$
\begin{split}
    E_\infty(\omega)&=\|\omega'\|_\infty+\|\omega\|_\infty/Q,\\
    E_1(\omega)&=\|\omega''\|_1+\|\omega'\|_1/Q+\|\omega\|_1/Q^2.
 \end{split}
$$

An upper envelope for any one parameter derivative of the common test times the profiles is the corresponding product of profile envelopes times $O(|\omega'|+|\omega|/Q)$. For two parameter derivatives use $O(|\omega''|+|\omega'|/Q+|\omega|/Q^2)$. These envelopes apply also to profiles differentiated in their own raw coordinate, using $G_I,G_{I'}$ there. They hold with extension by zero for the products, and are independent of the values of raw variables except for the fixed spatial envelopes.

Let, at fixed $z,w$,

$$
B_0(t)=\omega U_zV_w,\qquad B_1(t)=\omega U_zV,\qquad
 B_2(t)=\omega U V_w,\qquad B_3(t)=\omega UV ,
$$

where $U_z,V_w$ denote raw derivatives at fixed $t$, and all right-hand profiles are at $t,z,w$ as appropriate. The mixed chain rule of R80 (7), with $\partial_z t_\pm=\pm1/k$, $\partial_w t_\pm=1/k$, gives (3) as

$$
[B_0(t_-)-B_0(t_+)]
 +\frac{B_1'(t_-)-B_1'(t_+)}k
 -\frac{B_2'(t_-)+B_2'(t_+)}k
 -\frac{B_3''(t_-)+B_3''(t_+)}{k^2}.
 \tag{4}
$$

Primes on $B_i$ are $t$-derivatives at fixed raw coordinates, not derivatives after the two parameter maps. The usual R72 absolutely continuous primitives justify the rule almost everywhere with no atom at a fixed parent endpoint.

The absolute raw integral of the first term is $O(b_I b_{I'}(X/k)E_\infty)$. In fact $0\le t_+-t_-=2z/k\le4X/k$ on the first support, and the $B_0$ time derivative is bounded by $O(G_I(z)G_{I'}(w)E_\infty)$. Integrate the two fixed derivative envelopes.

For the second term fix $z$ and estimate the difference by integrating the second derivative $B_1''$ between $t_-$ and $t_+$. Bound it by $O(G_I(z)b_{I'})$ times the common integrable scalar second-derivative envelope. For each fixed $z$ the shift length $\delta=2z/k$ is independent of $w$. Change $w$ to $s=t_-$ and use Fubini in $\int_\mathbb R\int_s^{s+\delta}(\cdots)(t)\,dt\,ds$, which is exactly $\delta$ times the scalar $L^1$ norm. The change of variable cancels the $1/k$. Integrate $G_I$; the cost is $O(b_I b_{I'}(X/k)E_1)$. The supports or raw lower cuts can only decrease this absolute upper estimate, and using the common scalar envelope has avoided treating the longer raw profile as constant.

For the third term do not subtract its two terms. Bound them using $b_I G_{I'}(w) E_\infty$ and integrate $z$ over length $2X$. Its $1/k$ gives $O(b_I b_{I'}(X/k)E_\infty)$. For the fourth use the sup profile envelopes and, at fixed $z$, change $w$ separately in each term to $t_\pm$. The Jacobian cancels one of its two $1/k$'s and allows the scalar $L^1$ estimate $E_1$; the other integral is over length $2X$. Thus its cost is $O(b_I b_{I'}(X/k)E_1)$. Combining the four estimates proves

$$
\iint_{z,w>A}
       |\partial_{zw}^2\mathcal H_-
                  -\partial_{zw}^2\mathcal H_+|\,dz\,dw
 \ll_{\Gamma,\Theta} b_I b_{I'}\frac Xk
                         \big(E_\infty(\omega)+E_1(\omega)\big).
 \tag{5}
$$

The $X/k$ gain in the first two terms depends on the actual signed pairing; an estimate of separate sum and difference fields does not give (5).

## 4. Numerator, parent, and exact packet aggregation

Use the [R76 joint numerator bound](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) on the common contracted vector in (2). Auxiliary GRH and residue Parseval give $\|F^{\rm ev}(z)\|_2\ll_\epsilon Q^\epsilon\sqrt z$ and $\|F(w)\|_2\ll_\epsilon Q^\epsilon\sqrt w$, even with the actual high selections. The numerator vector after $\Pi_\times$ is therefore at most $O_\epsilon(Q^\epsilon b\sqrt{XY})$ in joint $\ell^2$ throughout the relevant supports. Multiplying by (5), and using $\sum_I b_I^2\ll X^{-1}$, $\sum_{I'} b_{I'}^2\ll Y^{-1}$, makes the factor $\sqrt{XY}b_Ib_{I'}$ cost $O(1)$ in HS on the pair. The common-test bound there is $O_\epsilon(Q^\epsilon b(X/k)(E_\infty+E_1))$ per alias. Both orientations of the matrix pair are covered by relabeling as in §2. Summing $K<k\le4U$ harmonically on each pair, and then summing the logarithmically many eligible dyad pairs with $X=QV\le QP$, gives the combined cost

$$
O_\epsilon\!\left(
                  Q^\epsilon b\, QP\,
                          [E_\infty(\omega)+E_1(\omega)]\right).
 \tag{6}
$$

No $\ell^2$ orthogonality across aliases is asserted. The product and small common-divisor selections have been kept throughout.

For the common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field), the effective $E_1$ is $O(S^{-1}+(1+|\ell|)^2/Q)$ on integer shift $\ell$. The same bound holds for the effective $E_\infty$: the common taper has $\|\omega_S'\|_\infty\ll1/S$, and a derivative on the Taylor-modulated bulk multiplier costs $O((1+|\ell|+n)/Q)$ for its $n$-th term, with the same factorial summability and $2^{-n}$ fractional coefficient as in R77. The weights depending on $a$ multiply the finished common-test vectors; the unit-modulus exterior phase is unchanged. Divide (6) by $J\asymp Q$; then square-sum the resulting $O_\epsilon(Q^\epsilon bP[S^{-1}+(1+|\ell|)^2/Q])$ over the packet denominators $B/2\le b\le B$ and the true detuned indices $|\ell|\le R+1$. The sums $\sum b^2=O(B^3)$ and $\sum_\ell (1+|\ell|)^4=O(R_*^5)$ yield (1), with the $S^{-1}$ term contributing $R_*^{1/2}$. At the chosen parameters the two powers are $-3/800$ and $-19/4000$, respectively.

Finally, on the affected larger-alias dyad pairs the exact field left after deletion has a short auxiliary character $\xi(-1)=-1$. Its long-leg parity is determined by $\xi(-1)\xi'(-1)=\nu(-1)$ for the actual surviving product $\nu$. No cancellation for this odd short leg or for the excluded dyad pairs follows from the estimate.
