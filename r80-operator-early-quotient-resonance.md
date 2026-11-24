# A genuine early quotient resonance and its removal from the centered product

**Scope.** The pointwise quotient fourth-moment estimate suggested by the preceding reduction is false on the actual early raw range, even for true Mangoldt data and the smallest switched alias. This is not a synthetic residue vector. Nevertheless, the portion of the literal twice-centered product where either raw coordinate is early can be removed on the entire R78 high-denominator packet with a power-small Hilbert–Schmidt error. The surviving estimate is a long–long prime-progression problem; no bound on that residual or on weak S is asserted.

## 1. The actual quotient fourth estimate fails near the beginning

Write $q=2k,\ q'=qb$ for the auxiliary switched modulus in [R79](r79-operator-exceptional-centered-product.md), with $q=2$ for $k=1$. For units $r\bmod q'$ let $F_{q',r}(z)=\psi(z;q',r)-z/\phi(q')$ be the true progression discrepancy defined there. On a fiber $r_0\bmod q$, extend its values by zero at nonunit lifts and use the normalized additive transform

$$
E_{q,b,a}(z;r_0)
   =b^{-1/2}\sum_{\substack{v\bmod b\\r_0+qv\ {\rm unit}\bmod qb}}
                      e(av/b)F_{qb,r_0+qv}(z),\qquad
 A_{q,b,a}(z)=\sum_{r_0\bmod q}|E_{q,b,a}(z;r_0)|^2 ,
 \tag{1}
$$

where $e(x)=\exp(2\pi i x)$. A pointwise bound $\sum_{a\bmod b}^{*}A_{q,b,a}(z)^2\ll_\epsilon Q^\epsilon z^2/b$ would be sufficient for a square-root gain in the joint two-error estimate, by Cauchy in the two quotient channels. It is not a valid bound over *all* raw coordinates of R79.

Indeed let $b=p$ be a sufficiently large odd prime, take $q=2$, and consider $p/100\le z\le p/50$. The only unit fiber is $r_0=1$. Using $a=1$, its exact numerator before division by $\sqrt p$ is

$$
\sum_{\substack{n\le z\\n\ {\rm odd}}}
                  \Lambda(n)e((n-1)/(2p))
       -\frac{z}{p-1}
           \sum_{\substack{v\bmod p\\1+2v\not\equiv0\bmod p}} e(v/p).
 \tag{2}
$$

For the first equality we used $z<p$ and the literal occurrence of each odd integer in its residue $1+2v\bmod 2p$. The last sum is the negative of one unit complex number, because it omits one element of a complete geometric sum. The phases of the first sum have real parts bounded below by a positive absolute constant; the Chebyshev lower bound for the Mangoldt sum gives mass $\gg z$, still after removing powers of $2$, whose mass is $O(\log(2z))$. Thus $|E_{2,p,1}(z;1)|\gg z/\sqrt p$, uniformly on this raw interval, unconditionally. In particular

$$
\sum_{a\bmod p}^{*}A_{2,p,a}(z)^2
                         \gg z^4/p^2\asymp p^2 .
 \tag{3}
$$

The proposed upper scale $z^2/p$ is only of order $p$. This is an obstruction also in the $p\asymp Q^{39/100}$ range of [R78](r78-operator-flat-numerator-most-modes.md), for sufficiently small $\epsilon$, and concerns actual prime powers rather than a model satisfying only GRH-wise bounds. It does not say anything negative about long raw prefixes, or about the actual signed combination of all aliases after integration. We now remove this region and much more in the true integrated problem.

## 2. Exact long–long reduction on the full high packet

Use the true $h,f$ raw families, the common transported parent basis and the complete shell of even moduli from R79. Thus $4\le H<M\le Q^\Gamma$ with fixed $0<\Gamma<1$, the reference dyads start at $V$, and each parent width is at most $W_V\le V/20$. Let $\mathcal C_+(B,R)$ be the high-denominator collars of R79 §1, with their same uniqueness/spacing hypothesis, original local Dirichlet GRH on the shell, and auxiliary Dirichlet GRH for $q'\le\lceil8MB\rceil+2$, including $1$. Keep the same exact detuning, normalization of $\widehat T$, original $\widehat P$, and one common cutoff $\omega_S$ supported in the shell with edge length $O(S)$, $2\le S\le Q/100$. Use R79's matrix $\mathcal X(j)$ (2), in which each orientation contributes the actual twice-integrated residue product.

Let $1\le A\le QH/2$, set $\delta_A=A/(QH)$ and $R_*=1+R$, and define $\mathcal X_{\rm long}(j)$ by replacing the raw integration domain in exactly that formula by $\{z>A,\ w>A\}$ in every entry and at every alias and orientation. This is a restriction of the integral **after** the mixed derivative has been taken. The restriction does not differentiate a raw indicator, reinterpret a prime-power atom, or create a sharp cutoff boundary term. Then

$$
\begin{split}
 &\left(\sum_{j\in\mathcal C_+(B,R)}
        \|\mathcal X(j)-\mathcal X_{\rm long}(j)\|_{\rm HS}^2\right)^{1/2}\\
 &\qquad\ll_{\Gamma,\Theta,\epsilon}
 Q^\epsilon B^{3/2}
   \left[
       \delta_A\,\frac M Q R_*^{3/2}
       +\delta_A^2\left(\frac M Q R_*^{5/2}
                              +\frac M S R_*^{1/2}\right)
   \right].
 \end{split}
 \tag{4}
$$

This is an estimate on the entire common parent basis, hence after any fixed orthogonal compression, and over any subset of these Fourier modes.

For the original R78 spatial and frequency parameters $H=Q^{2/5},M=Q^{3/5},W_V=Q^{23/175}V^{4/7},B=\lfloor Q^{39/100}\rfloor,R=\lfloor Q^{1/400}\rfloor$, choose $A=Q^{6/5}, S=Q^{4/5}$. The bound (4) is $O_\epsilon(Q^{-9/800+\epsilon})$. Apply R79 (3) with this $S$, its $B_0=\lfloor Q^{1/5}\rfloor$, $R_0=\lfloor Q^{1/4}\rfloor$, and $\kappa=3/10$. Its comparison error is $O_\epsilon(Q^{-1/10+\epsilon})$ for $h,h$ and $O_\epsilon(Q^{-1/50+\epsilon})$ with a body leg, both smaller than (4). Thus for either $\widehat T$ or $\widehat P$,

$$
\left(\sum_{j\in\mathcal C_+(B,R)}
        \|\widehat T(j)-\mathcal X_{\rm long}(j)\|_{\rm HS}^2\right)^{1/2}
                    \ll_\epsilon Q^{-9/800+\epsilon}
 \tag{5}
$$

with the analogous left side for $\widehat P$. In particular (5) applies on **every** actual exceptional mode of R78, not only its good set. On the new integral the raw coordinates both exceed $Q^{6/5}$, whereas every $q'=2kb$ is $O(Q^{99/100})$. The precise long–long product is still to be estimated.

## 3. Common weighted derivative on the two early strips

Work first on two parent entries on dyads $V\le U$. Put $X=QV,\ Y=QU$, and use their envelopes $b_I=\sqrt{|I|}/(\sqrt Q V)$, $b_{I'}=\sqrt{|I'|}/(\sqrt Q U)$ as in [R72](r72-operator-principal-modulus-low-modes.md) (4)–(5). Write $U_t(z)=u_{I,t}(z)$, $V_t(w)=v_{I',t}(w)$, where the symbol $V_t$ here denotes the profile on the second leg, not a dyad start. The proof is symmetric under reversal of the two physical dyads. The profiles have supports in $[0,2X]$, $[0,2Y]$, and the spatial derivatives of their first two normalized parameter derivatives have fixed $L^1$ envelopes of masses $O(b_I)$, $O(b_{I'})$.

On $0<z\le A\le QH/2$ both $h_{I,t}$ and $f_{I,t}$ are the **same exact** constant multiple of $\sqrt z$, with coefficient $(\sqrt{2\pi}/Q)(\int_Iw_t)^{1/2}$ in the notation of [R71 (1)–(2)](r71-operator-parent-terminal-layer.md#statement-and-the-exact-profile-split). The terminal mask vanishes there because the left end of its support is at least $Q(V-W_V)>QH/2$. The coefficient and each of its $Q^j\partial_t^j$ derivatives for $0\le j\le2$ are $O_\Gamma(b_I/\sqrt X)$, by the same weight derivatives as R72 (4). In particular on the early strip the following bounds hold uniformly in $t$, with the spatial derivative interpreted classically inside the positive interval:

$$
\big|Q^j\partial_t^j U_t(z)\big|
             \ll b_I\sqrt{z/X},\qquad
 \big|Q^j\partial_t^j\partial_z U_t(z)\big|
             \ll \frac{b_I}{\sqrt{Xz}}\qquad(0\le j\le2).
 \tag{6}
$$

Use the analogous bounds with $Y,b_{I'}$ on $0<w\le A$.

For a common scalar test $\omega\in C_c^2((Q,2Q))$ before any numerator-specific detuning, let $K_1=\|\omega\|_\infty+\|\omega'\|_1$ and $K_2=\|\omega''\|_1$, and set $t=(\sigma_1z+\sigma_2w)/k$. At fixed $t$ differentiate raw functions in their own raw coordinates. The chain rule gives the four terms of the derivative of $\mathcal H=\omega(t)U_t(z)V_t(w)$:

$$
\begin{split}
 \partial_{zw}^2\mathcal H={}&
      \omega(\partial_zU)(\partial_wV)
   +\frac{\sigma_2}{k}\partial_t[\omega(\partial_zU)V]
   +\frac{\sigma_1}{k}\partial_t[\omega U(\partial_wV)]
   +\frac{\sigma_1\sigma_2}{k^2}\partial_t^2[\omega U V].
 \end{split}
 \tag{7}
$$

The R72 profile bounds make all terms integrable, and the mixed derivative has no atom at a physical parent edge; the spatial primitives themselves are absolutely continuous. At all $0\le z\le2X$, $0\le w\le2Y$, auxiliary GRH gives the residue $\ell^2$ bounds
$\|\mathbf F_{q'}(z)\|_2\ll_\epsilon Q^\epsilon\sqrt z$ and
$\|\mathbf F_{q'}(w)\|_2\ll_\epsilon Q^\epsilon\sqrt w$.
These follow by the character prime-sum bound and finite Parseval as in R76; below $z=1$ the deterministic density term satisfies it directly. The pointwise $\sqrt z\sqrt w$ factors, not their maximum on the dyads, matter inside the early strips.

Let $D_A=\{(z,w):z,w>0,\ z\le A\text{ or }w\le A\}$. We claim the weighted derivative bound

$$
\iint_{D_A}\sqrt z\sqrt w\,|\partial_{zw}^2\mathcal H(z,w)|\,dz\,dw
       \ll b_Ib_{I'}\sqrt{XY}
            \left[\delta_A K_1
                  +\delta_A^2\frac X k(K_2+K_1/Q)\right].
 \tag{8}
$$

For detail, on $z\le A$ a raw derivative on the first profile satisfies
$\int_0^A\sqrt z\,|Q^j\partial_t^j\partial_z U_t(z)|\,dz
 \ll b_I A/\sqrt X$ by a common pointwise envelope from (6). Without that derivative its weighted supremum is at most $O(b_I A/\sqrt X)$, and the integral of that envelope over the strip is $O(b_I A^2/\sqrt X)$. On the unrestricted second leg, the corresponding weighted supremum of a profile is $O(b_{I'}\sqrt Y)$, and the integral of its weighted raw derivative envelope is $O(b_{I'}\sqrt Y)$. The first term of (7) has ratio $A/X$ against $b_Ib_{I'}\sqrt{XY}K_1$. In the second term of (7) integrate the unrestricted $w$ at fixed $z$ using $|dw|=k\,|dt|$, then the weighted raw derivative on the early leg. In the third term integrate $z$ at fixed $w$ by that affine change, using instead the weighted early supremum. The total scalar parameter derivative in each case is integrated against $|\omega'|+|\omega|/Q$, of $L^1$ norm $O(K_1)$. Both terms again gain $A/X$. In the fourth term fix the early $z$ and integrate $w$ by the same affine change; this leaves $1/k$ times the $L^1$ norm of $|\omega''|+|\omega'|/Q+|\omega|/Q^2$, which is $O(K_2+K_1/Q)$. The early weighted profile integral contributes $b_I A^2/\sqrt X$ in place of $b_I X\sqrt X$. This gives the quantity $A^2/(Xk)$ in place of $X/k$.

On the strip $w\le A$ the same first three estimates give the factor $A/Y$. For the last term fix the early $w$ this time and integrate $z$ by the affine change: the coefficient is then $A^2/(Yk)\le A^2/(Xk)$, not a larger coefficient from the unrestricted long leg. Since $A/X,A/Y\le\delta_A$ and $A^2/X\le\delta_A^2 X$, (8) follows by bounding the union with the two strips. The estimate uses absolute values after the derivative, so either strip or a disjoint splitting of their union is allowed; no cutoff has been differentiated.

## 4. Joint quotient norms and summing the real Fourier packet

For this fixed $b,k$ and common test, at each raw $(z,w)$ use the two-error residue incidence bound [R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term), namely the joint numerator $\ell^2$ bound $b\|\mathbf F_{q'}(z)\|_2\|\mathbf F_{q'}(w)\|_2$. The derivative and the early integration region are common to the numerators. Minkowski and (8) give the per-entry per-$k$ cost

$$
Q^\epsilon b\,b_Ib_{I'}\sqrt{XY}
        \left[\delta_A K_1+\delta_A^2\frac X k(K_2+K_1/Q)\right].
 \tag{9}
$$

This treats the exact centered product without comparing positive and negative prime counts or replacing the singular series. The remaining model, principal, and one-error terms were already removed in R79; only its exact $\mathcal X$ is split here.

Sum (9) over actual positive $k\le4U$, the three orientations and the parent dyad pairs. With $\sum_I b_I^2\ll X^{-1}$, $\sum_{I'} b_{I'}^2\ll Y^{-1}$, the $\sqrt{XY}b_Ib_{I'}$ factor costs $O(1)$ in the joint HS norm. Using $\sum_{k\le4U}1/k\ll \log(3Q)$ and $X\le QM$, the result **before** Fourier shell normalization is at most

$$
Q^\epsilon b M\left[\delta_A K_1
                +\delta_A^2 Q(K_2+K_1/Q)\right].
 \tag{10}
$$

All signed orientations are included with their original signs, although triangle suffices for this excision estimate.

For each denominator $b$ and integer shift $\ell$, restore the actual numerator-dependent fractional rounding by applying the common Taylor test weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) to (10). The effective $K_1$ is $O(1+|\ell|)$ and $K_2$ is $O(S^{-1}+(1+|\ell|)^2/Q)$. This is valid after the integration restriction because $D_A$ is fixed for all test terms and denominators. Divide by $J\asymp Q$, and keep the exact phase of absolute value one from R79 in each numerator. The joint numerator $\ell^2$ bound now is

$$
Q^\epsilon b\left[
       \delta_A\frac M Q(1+|\ell|)
       +\delta_A^2\left(\frac M Q(1+|\ell|)^2+\frac M S\right)
   \right].
$$

Sum its three terms by the $\ell^2$ triangle inequality over $|\ell|\le R+1$ and $B/2\le b\le B$, with $\sum b^2=O(B^3)$. Counting extra representations can only increase the squared norm. This proves (4) for the actual R79 matrix, which uses the same one common real cutoff. The resulting difference is not a Fourier transform of separately cut positive prime sums, but controls the exact restriction of the signed integrated field appearing in (5).

Finally $\delta_A=Q^{-1/5}$ at the example parameters. The three exponents in (4) are $-9/800$, $-167/800$, and $-11/800$, respectively. R79's larger comparison remainder for a body profile is $-1/50$, and the new common edge exponent there is $-1/10$. This proves (5) with both exact benchmark choices and the original sharp complete even shell. Equations (3) and (5) together leave a well-delimited task: estimate the genuine long–long quotient covariance or its weighted integral, and do not impose a false fourth-moment bound on all earlier raw coordinates.
