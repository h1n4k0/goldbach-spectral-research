# One common shell cutoff controls a wider set of genuine modulus modes

**Scope.** This is a Hilbert–Schmidt mean-square bound for a larger set of discrete modulus Fourier modes of the actual signed exterior covariance. One common smooth cutoff handles the arithmetic on all selected rational denominators, and full Fourier Parseval restores the original sharp shell just once. This permits both a larger dense collection of rational centers and separate packets at far larger denominators. The set still does not contain all Fourier modes, and the estimate does not give weak S or control at a prescribed modulus.

## 1. Statement

Use the actual matrices $T_N^{u,v}$ of [R76](r76-operator-joint-rational-numerator-variance.md) on the common transported parent basis, the true unmasked/body/terminal profiles $u,v\in\{h,f,g\}$ of [R71](r71-operator-parent-terminal-layer.md), and the spatial dyads in $[H,M]$, $4\le H<M\le Q^\Gamma$ for fixed $0<\Gamma<1$. Thus every positive alias and all three signed orientations are present, with the actual prime-power units and exact continuous correction, and with no equality line. Use the full consecutive even shell $N=2m\in[Q,2Q]$, $m=m_0,\ldots,m_0+J-1$, $J\asymp Q$, and define

$$
 \widehat T(j)=J^{-1}\sum_m e(-j(m-m_0)/J)T_{2m}^{u,v},
 \qquad e(z)=e^{2\pi i z}.
 \tag{1}
$$


Let $\mathcal B$ be a nonempty finite set of positive integer denominators, $D=\max\mathcal B$, with $DM\le Q/100$. For each $b\in\mathcal B$ choose a radius $R_b\ge1$. The set $\mathcal C_{\mathcal B}$ consists of the modes $j\bmod J$ lying at circular distance at most $R_b$ from $Ja/b$ for at least one reduced numerator $a\bmod b$ and $b\in\mathcal B$. For $b=1$ the reduced numerator is $0$. Write $L_b=1+R_b$ and set

$$
 A=M\left(\sum_{b\in\mathcal B}b^2L_b\right)^{1/2}.
 \tag{2}
$$

Assume original local Dirichlet GRH at every even modulus of the shell and auxiliary Dirichlet GRH at all moduli $q'\le\lceil8MD\rceil+2$, including $1$, exactly the assumptions of R76 for this maximum denominator. For every $2\le S\le Q/100$,

$$
 \begin{split}
 \left(\sum_{j\in\mathcal C_{\mathcal B}}
                   \|\widehat T(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon\bigg[
   &\sqrt{\frac M Q}
           \left(\sum_{b\in\mathcal B}\frac{L_b^3}{b}\right)^{1/2}
    +\frac M Q\left(\sum_{b\in\mathcal B} b^2L_b^5\right)^{1/2}\\
   &+\frac{A}{S}+\sqrt{\frac S Q}\bigg].
 \end{split}
 \tag{3}
$$

The identical bound holds after applying any fixed orthogonal projection on both parent legs, including the fixed true macro projection of [R74](r74-operator-fixed-macro-mean-all-modes.md). If $A/Q$ is sufficiently small, choose $S=A^{2/3}Q^{1/3}$; the last two terms then total $O((A/Q)^{1/3})$. The lower endpoint constraint for $S$ is automatic for large $Q$, since $A\ge M\ge4$, and the sufficiently small upper ratio ensures $S\le Q/100$.

In particular, for the full denominator interval $\mathcal B=\{1,\ldots,B\}$ and a common radius $R$, (3) is

$$
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon\left[
   \sqrt{\frac M Q}(1+R)^{3/2}
   +\frac M Q B^{3/2}(1+R)^{5/2}
   +\frac M S B^{3/2}(1+R)^{1/2}
   +\sqrt{\frac S Q}\right].
 \tag{4}
$$

Here a factor $O(\sqrt{\log(2B)})$ in the first term is absorbed by $Q^\epsilon$. The largest previously treated uniform denominator collection with the R76 estimates had a separate boundary term for each denominator. The benefit in (3) is to restore a single boundary error on the entire frequency set, rather than to improve the per-denominator arithmetic.

## 2. Common taper and the exact sharp edge

Choose a **single** $\omega\in C_c^2((Q,2Q))$ equal to one except in two endpoint strips of total length $O(S)$, with

$$
 \|\omega\|_\infty+\|\omega'\|_1\ll1,\qquad
                         \|\omega''\|_1\ll S^{-1}.
 \tag{5}
$$

For instance use a fixed compact transition on each strip scaled to length $S$. This is chosen independently of $b$, the numerators, and the radii. Write the exact original field on the full shell as $T_{2m}=Z_{2m}+W_{2m}$, where

$$
 Z_{2m}=\omega(2m)T_{2m},\qquad
                  W_{2m}=(1-\omega(2m))T_{2m}.
$$

The support of $W$ has $O(S)$ elements, including the original endpoints if present. The pointwise bound $\|T_N^{u,v}\|_{\rm HS}\ll_\epsilon Q^\epsilon$ from [R72 §1](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes) applies with the exact actual masks. The normalized finite Fourier Parseval identity in the complexified Hilbert–Schmidt space gives

$$
 \left(\sum_{j\bmod J}\|\widehat W(j)\|_{\rm HS}^2\right)^{1/2}
 =\left(J^{-1}\sum_m\|W_{2m}\|_{\rm HS}^2\right)^{1/2}
 \ll_\epsilon Q^\epsilon\sqrt{S/Q}.
 \tag{6}
$$

This estimates the error on the *whole* Fourier field before any restriction, independently of how many denominator vectors cover one mode. In particular the same edge cost is valid for their entire union. Applying (6) to distinct tapered fields for different denominators would not justify this reuse.

## 3. The true central tapered field

Fix $b\in\mathcal B$ and an integer $\ell$, and for every reduced $a\bmod b$ let $j_0(a)$ be a nearest integer to $Ja/b$. Write $s_a=j_0(a)-Ja/b$, so $|s_a|\le1/2$, and $x(t)=(t/2-m_0)/J$. On the shell $|x(t)|\le2$ and $|x'(t)|=O(Q^{-1})$. As in R76 (11)–(12), the phase at $j=j_0(a)+\ell$, up to the constant of absolute value one $e(a m_0/b)$, is
$e(-am/b)e(-\ell x(2m))e(-s_a x(2m))$.
Expand the last factor by its power series. The $a$-dependent coefficient of each term is $s_a^n$, of absolute value at most $2^{-n}$, and the common smooth test is

$$
 \omega_{\ell,n}(t)=\omega(t)e(-\ell x(t))
                          \frac{(-2\pi i x(t))^n}{n!}.
$$

This test is the same for all reduced numerators $a$; no derivative bound is being asserted for an $a$-specific smooth test after taking a joint numerator norm. With $K_1(f)=\|f\|_\infty+\|f'\|_1$ and $K_2(f)=\|f''\|_1$, the derivative bounds and the factorial summability give

$$
 \sum_{n\ge0}2^{-n}K_1(\omega_{\ell,n})\ll1+|\ell|,\qquad
 \sum_{n\ge0}2^{-n}K_2(\omega_{\ell,n})
                   \ll S^{-1}+(1+|\ell|)^2/Q .
 \tag{7}
$$

Indeed a derivative on the bulk multiplier costs $O((1+|\ell|+n)/Q)$ per derivative after the same $O(C^n/n!)$ majorant, with an absolute $C$ and at most two derivatives. The term hitting $\omega$ twice costs $S^{-1}$, and the cross term uses $\|\omega'\|_1=O(1)$. The bulk terms integrate over length $O(Q)$. This is the fixed-$b$ power series argument of R76 with the common cutoff (5) in place of the $b$-dependent cutoff there.

Insert (7) in the joint reduced-numerator smooth estimate R76 (4), permuting the numerators by $a\mapsto-a$. That estimate already has the true unit-restoration terms, singular series, and two-centered error before taking the numerator norm. The normalization by $J\asymp Q$ gives for the present tapered field

$$
 \left(\sum_{a\bmod b}^{*}
         \|\widehat Z(j_0(a)+\ell)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\Theta,\epsilon}Q^\epsilon
 \left[b^{-1/2}\sqrt{M/Q}(1+|\ell|)
         +\frac{bM}{Q}(1+|\ell|)^2+\frac{bM}{S}\right].
 \tag{8}
$$

No boundary approximation has been made in (8); it estimates $\widehat Z$ exactly.

Every mode in $\mathcal C_{\mathcal B}$ has a representation of the above form modulo $J$ with $|\ell|\le R_b+1$. Counting repetitions only overestimates its nonnegative squared Hilbert–Schmidt norm. Apply the $\ell^2$ triangle inequality to the three right-hand terms of (8) and sum their squares over the selected denominators and shifts. The three shift sums are at most $O(L_b^3)$, $O(L_b^5)$, and $O(L_b)$, respectively. This gives the first three terms of (3) for $\widehat Z$. Add (6), which estimates the same original Fourier field's remaining part $\widehat W$ once. This proves (3) for the genuine sharp shell. A fixed compression commutes with (1) and contracts HS norm. The optimized $S$ balances $A/S$ and $\sqrt{S/Q}$; no optimization or hypothesis on the true Fourier values is used elsewhere.

## 4. Dense denominators and a separated high-denominator packet

First take $H=Q^{2/5}$, $M=Q^{3/5}$, $B=\lfloor Q^{6/25}\rfloor$, and $R=\lfloor Q^{1/100}\rfloor$ with full denominator interval as in (4). Then $A/Q\ll Q^{-7/200}$, and the first two terms of (4) have exponents $-37/200$ and $-3/200$. With the optimized edge, the RMS is $O_\epsilon(Q^{-7/600+\epsilon})$, and the auxiliary cap is $O(Q^{21/25})$. Distinct reduced rational centers with denominators at most $B$ are separated in circular index distance by at least $J/B^2$, larger than any collar width here. The denominators $B/2\le b\le B$ give $\asymp Q^{49/100}$ distinct modes by the elementary sum $\sum_{n\le X}\phi(n)=3X^2/\pi^2+O(X\log(2X))$. These modes lie outside the examples in R76 and the prior R73/R75 collars: the union of denominator sets has maximum $B$, and all their radii are $o(J/B^2)$, while the selected denominators are strictly larger.

More generally for $M=Q^\gamma$, $B\asymp Q^\beta$, $R\asymp Q^\rho$, power savings and separated distinct cardinality follow whenever

$$
 \tfrac32\rho<\tfrac{1-\gamma}{2},\qquad
 \tfrac32\beta+\tfrac52\rho<1-\gamma,\qquad
                            2\beta+\rho<1 .
$$

The cardinality exponent in that range is $2\beta+\rho$. For $\gamma=3/5$, this permits cardinality exponents approaching $8/15$ from below by taking $\rho>0$ small. This is a limit of the bounds administered here, not a claimed lower bound on the unknown true variance beyond that range.

For a separate extension, take the same $H,M$ and define

$$
 d=2^{\lfloor(8/25)\log_2 Q\rfloor},\qquad
 X=\lfloor Q^{1/25}\rfloor,\qquad
 \mathcal B_+=\{d n:X\le n\le2X,\ n\ {\rm odd}\},
       \qquad R_b=\lfloor Q^{1/200}\rfloor .
 \tag{9}
$$

Here $b\asymp Q^{9/25}$ on $\mathcal B_+$, with $\asymp Q^{1/25}$ denominators. The auxiliary cap is $O(Q^{24/25})$, and $DM\le Q/100$ holds for large $Q$. The sums in (3) give first term $O(Q^{-141/400})$, second term $O(Q^{-3/400})$, and $A/Q\ll Q^{-7/400}$. For example the second term exponent is $3/5-1+9/25+(1/25)/2+5/400=-3/400$; optimization of the edge then gives the bound

$$
     O_\epsilon(Q^{-7/1200+\epsilon})
 \quad\hbox{on the Fourier modes of }\ \mathcal C_{\mathcal B_+}.
 \tag{10}
$$

There are $\asymp Q^{81/200}$ distinct such modes. To check the count without any prime-distribution assumption, $d$ is a power of $2$ and $n$ is odd, so $\phi(dn)=\phi(d)\phi(n)$. The identity $\phi(n)=n\sum_{c\mid n}\mu(c)/c$ and the sum of odd integers up to $Y$, which is $Y^2/4+O(Y+1)$, give

$$
 \sum_{\substack{n\le Y\\n\ {\rm odd}}}\phi(n)
     =\frac{Y^2}{4}\sum_{c\ {\rm odd}}\frac{\mu(c)}{c^2}
         +O(Y\log(2Y)).
$$

The Euler product for the absolutely convergent sum is positive. Hence the number of centers is $\asymp dX^2$, multiplied by $\asymp 1+R_b$ modes per center. Distinct reduced denominators in the union of the high packet and the previous sets have spacing $\gg Q^{7/25}$ in circular index distance, since $D\asymp Q^{9/25}$. This exceeds both the widths here and the lower-denominator examples' widths. Thus the high packet is disjoint both from the dense collection just proved and from the R76/R75 example collars. The high packet changes the accessible denominator scale, not the overall cardinality exponent of the union.

At the actual R74 parent sizes $W_V=Q^{23/175}V^{4/7}$, apply the fixed macro projection there. On each of the two new subsets just specified, lying outside the R75 collars, the exact $D+K$ has HS RMS $O_\epsilon(Q^{-3/80+\epsilon})$ for $h,h$, or $O_\epsilon(Q^{-1/50+\epsilon})$ with a body leg, by [R75 (2)](r75-operator-prime-divisor-fourier-signature.md#1-statement-and-exact-indexing). Since the true $P=T+(D+K)$, the stronger signed bounds above transfer, by the triangle inequality, to the same power rates for the actual prime Gram on these new sets for $u,v\in\{h,f\}$. The full remaining modulus-frequency variance is still unestimated.
