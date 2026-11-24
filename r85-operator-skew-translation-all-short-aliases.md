# Removing the sine gap in the actual short-alias quotient field

The skew difference cannot be estimated by inserting the same progression increment in both legs: that skew quadratic form vanishes identically. Instead, at a fixed affine shift, the integrated skew pairing of a common interval-restricted progression vector is odd in the shift. A raw Fourier transform gives a sine multiplier, whose first-order zero is enough to exploit the conditional progression increment estimate. An interval decomposition transfers this bound back to the actual parent weights.

## 1. Setting and conclusion

Use the complete even modulus shell, normalized Fourier test $J^{-1}\sum_m$ for $N=2m$, genuine $h,f$ parent profiles, separated high packet $\mathcal C_+(B,R)$, and common taper from [R84](r84-operator-short-cosine-and-sum-aliases.md). Assume the original local Dirichlet GRH at the target even moduli and auxiliary Dirichlet GRH through $\lceil 8MB\rceil+2$, including modulus $1$. The residual $\mathcal X_{\rm res}$ is exactly that of [R82](r82-operator-low-product-character-long-quotient.md): two actual centered progression vectors on $z,w>A$, the high character selection on each leg, the high product conductor mask, and the selection $(2k,b)<G$. Let $\mathcal Z_{>K}$ retain just the aliases $k>K$ with every other mask, sign, integration restriction and Fourier weight left unchanged. Put $R_*=1+R$. For $Q\le A\le QH/100$ and $A/Q\le K\le4M$ in the R84 parent regime, the deleted field satisfies

$$
\left(\sum_{j\in\mathcal C_+(B,R)}
       \|\mathcal X_{\rm res}(j)-\mathcal Z_{>K}(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B^{3/2}K
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{1}
$$

The new part of (1) is the skew difference, where it holds even with the summation restricted to any set of eligible aliases in $[1,K]$ chosen independently of the numerator. Orthogonal spatial compression and restriction to any subset of the specified Fourier indices contract the resulting bound.

In particular keep the R84 example

$$
\begin{gathered}
 H=Q^{2/5},\quad M=Q^{3/5},\quad W_V=Q^{23/175}V^{4/7},\quad
 A=Q^{6/5},\quad B=\lfloor Q^{39/100}\rfloor,\quad
 R=\lfloor Q^{1/400}\rfloor,\quad S=Q^{249/250},\\
 D_\times=Q^{1/1000},\quad G=Q^{1/5},\qquad
 K=\lfloor Q^{81/200}\rfloor .
 \end{gathered}
$$

Then (1) is $O_\epsilon(Q^{-3/800+\epsilon})$. Thus **all orientations**, including the skew differences, can be discarded through $Q^{81/200}$ in this actual packet. By the inherited sharp comparison, the true $\widehat T$ and $\widehat P$ each differ from $\mathcal Z_{>K}$ by $O_\epsilon(Q^{-1/500+\epsilon})$ in the same packet norm, including the [R78 exceptional indices](r78-operator-flat-numerator-most-modes.md#5-exponents-mode-count-and-the-remaining-variance). The larger-alias field $\mathcal Z_{>K}$ is not estimated. This is not a bound for the full set of Fourier modes, a different modulus averaging family, an individual modulus, or weak S.

## 2. Exact skew incidence

At fixed $q'=2kb$, the true high residue vector is $F(z)=F^{\rm hi}_{q'}(z)$. Write $A_a$ for the R82 fixed orientation incidence on the full reduced numerator set and $\mathcal A_a=(A_a-A_{-a})/2$ for its skew difference. Since $A_a^\mathsf T=A_{-a}$, $\mathcal A_a^\mathsf T=-\mathcal A_a$. It corresponds to the odd product $\nu(-1)=-1$ part, as in [R84 §3](r84-operator-short-cosine-and-sum-aliases.md#3-two-exact-marginal-cancellations-on-the-symmetric-difference). The high product conductor projector $\Pi_\times$ is an $\ell^2_a$ contraction on the full reduced numerator vector, so for arbitrary complex residue vectors $X,Y$

$$
\|\Pi_\times(X^\mathsf T\mathcal A_aY)_{a\bmod b}^*\|_{\ell^2_a}
       \le b\|X\|_2\|Y\|_2 .
 \tag{2}
$$

This is the [R76 (7) incidence inequality](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) plus reflection; it holds for Fourier-transformed residue vectors too. No projection is moved past differing detunings. Real or complex weights may appear in a common test.

## 3. A weighted raw translation estimate for the skew incidence

Fix a raw dyad $[D,2D]$ in the polynomial raw range of R84, a real shift $h$ with $8\le|h|\le D/4$, and an interval $C\subset[D,2D]$. Write $G(z)=\mathbf1_C(z)F(z)$, extended by zero. Auxiliary GRH gives the pointwise $O_\epsilon(Q^\epsilon\sqrt D)$ on $[3D/4,9D/4]$. [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) gives for $1\le |u|\le D/4$

$$
\|G\|_{L^2(\mathbb R;\ell^2)}^2\ll_\epsilon Q^\epsilon D^2,\qquad
 \|G(\cdot+u)-G\|_{L^2(\mathbb R;\ell^2)}^2
                      \ll_\epsilon Q^\epsilon D|u|.
 \tag{3}
$$

Indeed on the overlap of the interval with its translate, the increment integral is bounded by the unrestricted actual progression Selberg integral over $[D,2D]$. On the symmetric difference at the two ends there is total raw length at most $2|u|$, with the same pointwise squared bound. Either sign of $u$ is allowed and the high individual character projection is fixed.

Let $I_a(h)=\int_\mathbb R G(z)^\mathsf T\mathcal A_aG(z+h)\,dz$. By translation and skew transposition, $I_a(-h)=-I_a(h)$. Bilinear Plancherel with transform $e(-z\xi)$ and the odd relation give, in the joint numerator vector,

$$
(I_a(h))_a=\frac12\int_{\mathbb R}
          (e(h\xi)-e(-h\xi))
          (\widehat G(-\xi)^\mathsf T\mathcal A_a\widehat G(\xi))_a\,d\xi .
 \tag{4}
$$

No Fourier transform in the modulus is taken in (4); this is a separate raw-line transform at a fixed $t$. The products are integrable by Cauchy–Schwarz and the formula holds for finitely many $a$. Apply (2) inside the integral, use AM–GM on $\|\widehat G(-\xi)\|_2\|\widehat G(\xi)\|_2$, and use the evenness of the absolute sine bound. This yields

$$
\|\Pi_\times(I_a(h))_a\|_2
 \ll b\int_{\mathbb R}\min(1,|h\xi|)\|\widehat G(\xi)\|_2^2\,d\xi
 \ll_\epsilon Q^\epsilon bD|h|.
 \tag{5}
$$

For the last estimate, on $|\xi|<1/D$ use the first part of (3) times $|h|/D$. On any dyadic band $\tau\le|\xi|\le2\tau$ with $1/D\le\tau\le1/|h|$, choose $u=1/(8\tau)$ so $1\le u\le D/8$ and $|e(u\xi)-1|\gg1$ throughout the band. By translation Plancherel and (3), its spectral mass is $O_\epsilon(Q^\epsilon D/\tau)$, and its weighted contribution $O_\epsilon(Q^\epsilon D|h|)$. The $O(\log(3Q))$ bands are absorbed. For the full tail $|\xi|\ge1/|h|$, average the translation norm in (3) over $u\in[|h|/8,|h|/4]$. The normalized average of $|e(u\xi)-1|^2$ is bounded below there: it is a positive continuous function of $|h\xi|$ on $[1,\infty)$, approaching $2$ at infinity by the explicit cosine integral. This bounds the entire tail by $O_\epsilon(Q^\epsilon D|h|)$, including frequencies above all polynomial scales.

Replacing $I_a(h)$ by the interval-weighted untruncated pairing $\int_C F(z)^\mathsf T\mathcal A_a F(z+h)\,dz$ costs $O_\epsilon(Q^\epsilon bD|h|)$ by (2): the missing raw set $C\setminus(C-h)$ is contained in an interval of length at most $|h|$ adjacent to one endpoint, and both arguments are $\asymp D$. Thus (5) holds for this actual pairing over every $C$; it does not require endpoint phases or unit-restoration estimates. A complex $p$ of bounded variation on $[D,2D]$ is a constant plus a Stieltjes integral of indicators of intervals $[D,s]$, with total coefficient variation at most $|p(2D)|+\operatorname{Var}(p)$, taking a representative up to null sets. Therefore Minkowski yields

$$
\left\|\Pi_\times\left(\int_D^{2D}
        p(z)F(z)^\mathsf T\mathcal A_a F(z+h)\,dz\right)_a\right\|_2
 \ll_\epsilon Q^\epsilon bD|h|\,(\|p\|_\infty+\operatorname{Var}(p)).
 \tag{6}
$$

Clipping the terminal dyad is allowed by extending the weight with an indicator and paying one jump of size at most $\|p\|_\infty$.

## 4. The exact sharp masks and the four chain terms

At dyad pair $V\le U$, set $X=QV,Y=QU$. As in [R84 §2](r84-operator-short-cosine-and-sum-aliases.md#2-common-test-and-an-adaptive-raw-cutoff), $\rho_k=A+8kQ$; on pairs $4\rho_k\le X$ use the smooth profiles $\chi_k U_t,\chi_k V_t$, and the original field on other pairs. For a common test $\omega$, put $K_1=\|\omega\|_\infty+\|\omega'\|_1$ and $K'_2=\|\omega''\|_1+K_1/Q$. The weighted raw boundary difference and the total bound on other pairs are R84 (7), $O_\epsilon(Q^\epsilon b K[K_1+QK'_2])$. That bound applies to the skew incidence by (2), since R84 (4)–(7) use only the pointwise progression norm and the joint incidence bound, not symmetry or an estimate for increments. The cutoff was introduced only in the proof; no cutoff or boundary term is changed in the statement. The first three chain terms on smoothly cut pairs cost $O_\epsilon(Q^\epsilon bK K_1)$ by the pointwise GRH bound and the fixed spatial derivative envelope, without any subtraction. In the fourth, change $w$ to $t$ at fixed $z$, leaving $1/k$, then $w=z+h$ with the actual $h=\pm kt$. Integrate at fixed $t$ over dyads starting at $\rho_k$ and capped at $2X$; $|h|\le2kQ\le\rho_k/4$ and $|h|\ge Q$.

Leibniz in $\partial_t^2(\omega\,\chi U\,\chi V)$, at **fixed raw variables before the change**, gives finitely many scalar $t$-factors with total $L^1$ mass $O(K'_2)$. For a term with $r$ and $s$ parameter derivatives on the first and second profiles, absorb $Q^{-r-s}$ in that scalar and take the common fixed-$t,h$ spatial weight

$$
p(z)= Q^r\partial_t^r(\chi_k U_t)(z)\,
        Q^s\partial_t^s(\chi_k V_t)(z+h),\qquad r+s\le2 .
 \tag{7}
$$

Do not differentiate $h$ in this definition. By the [R72 fixed spatial envelopes](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes) and R84 cutoff envelope, the sup and TV of $p$ on every raw dyad are $O_{\Gamma,\Theta}(b_Ib_{I'})$; the fixed translation of the second profile does not change its variation. These hold uniformly in the possibly clipped intervals, real $t$, k and orientations. This is why it is essential to integrate in $z$ at each fixed $t$, rather than take the absolute value of the skew integrand before the raw-line Fourier step. The good pair's product really vanishes when either coordinate is below $\rho_k$, but (6) needs only the supremum and variation, not positivity.

Sum (6) geometrically over $D\le2X$ at fixed $t$. This gives $O_\epsilon(Q^\epsilon b\,b_Ib_{I'}X|h|)$ in the full numerator vector norm; the entries have true normalized profile factors. Integrate $t$ absolutely against the scalar $L^1$ bound $K'_2$. Since $|h|/k=t\le2Q$, the parent's per-dyad HS cost is $O_\epsilon(Q^\epsilon b Q K'_2 X/\sqrt{XY})\le O_\epsilon(Q^\epsilon b Q K'_2)$ per alias. This uses $\sum_I b_I^2\ll X^{-1}$, $\sum_{I'}b_{I'}^2\ll Y^{-1}$ and the same R84 logarithmic dyad summation. Both difference orientations follow; no mutual cancellation is claimed.

Therefore the actual skew differences through $K$ have common-test cost $O_\epsilon(Q^\epsilon b K[K_1+QK'_2])$, the same as the separate R84 cosine estimate. This bound used a raw translation pairing, not the R84 symmetric quadratic increment or an assumption about a uniform prime-pair correlation.

## 5. Restore the exact Fourier weights and combine the orientations

Apply the original Taylor detuning expansion [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) to the common-test skew bound just proved. On denominator $b$ and integer shift $\ell$, the effective common-test derivative costs are $O(1+|\ell|)$ for $K_1$, and $O(S^{-1}+(1+|\ell|)^2/Q)$ for $K'_2$. The true $a$-dependent Taylor multipliers act on the output of each pre-detuning projected vector, and the original exterior phase of absolute value one is kept. Thus division by $J\asymp Q$ gives the joint skew estimate

$$
O_\epsilon\!\left(Q^\epsilon bK\left[
       \frac{1+|\ell|}{Q}+\frac{(1+|\ell|)^2}{Q}+\frac1S\right]\right).
 \tag{8}
$$

No fractional detunings were dropped and no new reflection identity is assumed for an already detuned Fourier field. Square-sum over $B/2\le b\le B,\ |\ell|\le R+1$ with $\sum b^2\ll B^3$, exactly as in R84 §5. The full sum bound R84 (12) and the symmetric difference bound R84 (10), both through $K$, also have the cost in (8). Adding the three actual pieces with their inherited signs proves (1). Because the sharp-shell comparison is unchanged, no separate endpoint restoration or modification of the original benchmark is needed. The three powers in (1) at the stated parameters are $-1/160,\ -3/800,\ -19/4000$, respectively.
