# Short sum aliases and cosine differences in the actual long quotient product

An alias-dependent smooth raw cutoff gives two exact marginal cancellations for the **symmetric** incidence on a difference orientation. Two constant subtractions turn it into a quadratic progression increment. This permits deletion of all sum orientations and all cosine difference orientations through an alias cutoff larger than the minimum physical dyad. The sine differences do not have this two-subtraction identity. A separate single-increment estimate removes them only on a smaller range.

## 1. Setting and statement

Keep the complete even modulus shell $N=2m\sim Q$, normalized modulus Fourier transform $J^{-1}\sum_m$, actual transported parent profiles $u,v\in\{h,f\}$ on dyads $H\le V,U\le M$, and the separated high rational packet $\mathcal C_+(B,R)$ of [R82](r82-operator-low-product-character-long-quotient.md) and [R83](r83-operator-small-alias-progression-increments.md). Keep their common real shell taper of endpoint length $O(S)$, $2\le S\le Q/100$, and exact numerator-dependent detunings. Assume original local Dirichlet GRH at the even target moduli and auxiliary Dirichlet GRH through $\lceil 8MB\rceil+2$, including modulus $1$. Let $R_*=1+R$. Use the R82 residual $\mathcal X_{\rm res}$ with both raw coordinates $z,w>A$, exactly the high individual character projections of [R81](r81-operator-low-conductor-long-quotient.md), high product conductor $>D_\times$, and the common-divisor cut $(2k,b)<G$.

Choose $Q\le A\le QH/100$ and $A/Q\le L\le K\le 4M$. Define $\mathcal Y_{K,L}$ from the actual residual integral as follows, applying the masks before the exact scalar detunings but retaining those detunings in the resulting Fourier field:

* Retain every term with $k>K$.
* For $L<k\le K$, retain only the skew-symmetric (sine) incidence of both difference orientations. Equivalently in the **pre-detuning** multiplicative numerator expansion, retain only product characters $\nu$ with $\nu(-1)=-1$. The sum orientation is not retained there.
* Retain no term with $k\le L$.

The raw restrictions, real parent weights, actual auxiliary progression vectors, and all inherited signs and high selections are unchanged in the retained terms. With $D_{\rm pkt} =R_*^{5/2}/Q+R_*^{1/2}/S$, the bound is

$$
\begin{split}
 \left(\sum_{j\in\mathcal C_+(B,R)}
        \|\mathcal X_{\rm res}(j)-\mathcal Y_{K,L}(j)\|_{\rm HS}^2
        \right)^{1/2}
 &\ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B^{3/2}
      \left[\frac KQ R_*^{3/2}+(K+\sqrt{ML})D_{\rm pkt}\right].
 \end{split}
 \tag{1}
$$

The whole sum-orientation deletion alone satisfies the same bound with $K+\sqrt{ML}$ replaced by $K$, and in both its terms $K$ can be replaced by $K\min(1,K/H)$ up to an absolute constant. A fixed orthogonal compression and restriction to any subset of the packet, even if selected from the sharp field, both preserve these estimates.

At the R82–R83 example parameters

$$
\begin{gathered}
 H=Q^{2/5},\quad M=Q^{3/5},\quad W_V=Q^{23/175}V^{4/7},
 \quad A=Q^{6/5},\quad B=\lfloor Q^{39/100}\rfloor,\quad
 R=\lfloor Q^{1/400}\rfloor,\quad S=Q^{249/250},\\
 D_\times=Q^{1/1000},\quad G=Q^{1/5},\qquad
 K=\lfloor Q^{81/200}\rfloor,\qquad L=\lfloor Q^{21/100}\rfloor ,
 \end{gathered}
 \tag{2}
$$

the bound in (1) is $O_\epsilon(Q^{-3/800+\epsilon})$. Thus the sharp even-shell fields $\widehat T$ and $\widehat P$ each have packet HS RMS distance $O_\epsilon(Q^{-1/500+\epsilon})$ to $\mathcal Y_{K,L}$, by the already established R82 sharp comparison. This is a deletion in the actual correlated field, not a bound for $\mathcal Y_{K,L}$. In particular the intermediate sine differences and the full large-alias residual are not estimated, and the retained packet is not the full set of modulus Fourier modes.

## 2. Common test and an adaptive raw cutoff

Fix $b,k$, and a common scalar $\omega\in C_c^2((Q,2Q))$, before each primitive numerator's own fractional detuning. Put

$$
K_1=\|\omega\|_\infty+\|\omega'\|_1,\qquad K_2=\|\omega''\|_1,\qquad
 K_2'=K_2+K_1/Q.
$$

On two dyads $V\le U$, set $X=QV,\ Y=QU$, and for one entry write $U_t(z)=u_{I,t}(z)$, $V_t(w)=v_{I',t}(w)$. Thus $V_t$ is the second profile, not a dyad start. If necessary interchange the raw coordinate names and difference orientations to put the shorter physical dyad first. Let

$$
t=(\sigma_1z+\sigma_2w)/k,\qquad
 \mathcal H(z,w)=\omega(t)U_t(z)V_t(w).
 \tag{3}
$$

The three orientations $+-, -+, ++$ have their inherited coefficients $+,+,-$. Write $b_I=\sqrt{|I|}/(\sqrt Q V)$ and similarly $b_{I'}$ on $U$. The fixed supports are $[0,2X]$, $[0,2Y]$; the sup and fixed spatial $L^1$ envelopes for $Q^j\partial_t^j$ at $0\le j\le2$ are those of [R72 (4)–(5)](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes). In particular $\sum_I b_I^2\ll X^{-1}$ and $\sum_{I'}b_{I'}^2\ll Y^{-1}$. On $z\le X/2$, either actual $h$ or $f$ is the same $t$-dependent multiple of $\sqrt z$, with $j$-th normalized parameter derivative of the coefficient $O(b_I/\sqrt X)$; on $w\le Y/2$ use the analogous fact. This is the profile identity used in [R80 (6)](r80-operator-early-quotient-resonance.md#3-common-weighted-derivative-on-the-two-early-strips), now with the true parent lower support at $Q(V-W_V)>X/2$, and $Q(U-W_U)>Y/2$. These parent inequalities hold throughout (2) and in the R82 standing parent regime.

Let $\mathbf F(z)=\mathbf F^{\rm hi}_{q'}(z)$ denote the R81 high projection of the real centered progression vector at $q'=2kb$. The two individual filters are identical for these progression vectors; the $h,f$ choices appear only in the scalar profiles. Auxiliary GRH and character Parseval give $\|\mathbf F(z)\|_2\ll_\epsilon Q^\epsilon\sqrt z$; for $z<1$ the unprojected discrepancy is just the deterministic density and satisfies this directly. The high product projection $\Pi_\times$ acts on the full reduced numerator vector for **each common test** (R82 (4)–(6)). [R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) bounds the joint norm of the true difference or sum incidence by $b$ times the product of the two progression vector norms. Each split or projection used below is a contraction of that joint bound. The cut $(2k,b)<G$ is independent of the numerator and all raw variables.

For a difference alias put $\rho_k=A+8kQ$. Choose a fixed smooth function $\chi:[0,\infty)\to[0,1]$ zero on $[0,1]$, one on $[2,\infty)$, and let $\chi_k(z)=\chi(z/\rho_k)$. Call a dyad pair good for this alias when $4\rho_k\le X$; otherwise keep the original sharp raw restriction and simply bound this pair. On a good dyad pair we will replace the derivative kernel $\mathbf1_{z,w>A}\partial_{zw}^2\mathcal H$ by $\partial_{zw}^2\mathcal H_\chi$, where $\mathcal H_\chi=\chi_k(z)\chi_k(w)\mathcal H(z,w)$. This changes the field only on the union of the early strips $z\le2\rho_k$ or $w\le2\rho_k$. The weighted integral of the absolute difference is at most

$$
\ll b_Ib_{I'}\sqrt{XY}
   \left[\frac{\rho_k}{X}K_1+\frac{\rho_k^2}{X k}K_2'\right].
 \tag{4}
$$

Here and below the weighted integral uses $\sqrt z\sqrt w\,dz\,dw$. To verify (4), apply the R80 four-term chain rule separately to $\mathcal H$ and $\mathcal H_\chi$ on each strip, since both kernels agree off the union. For a short leg treated as early, $0<z\le2\rho_k$, the fixed upper bounds for the $j$-th normalized parameter derivatives of the weighted profile and weighted raw derivative are respectively

$$
O(b_I z/\sqrt X),\qquad O(b_I/\sqrt X).
 \tag{5}
$$

The extra derivative $\sqrt z\,\chi_k'(z)Q^j\partial_t^j U_t(z)$ has the second size in (5), because $z\le2\rho_k$ on its support. Globally the cutoff profiles still have the R72 fixed $L^1$ derivative bounds: the new term has integral $O(b_I)$ using merely $\sup_t|Q^j\partial_t^j U_t|\ll b_I$ and $\|\chi_k'\|_1\ll1$. All cutoffs are independent of $t$. The analogous bounds hold for $w$ with $Y,b_{I'}$.

For the term with two spatial derivatives the early weighted integral contributes $O(b_I\rho_k/\sqrt X)$, and the other weighted derivative integral $O(b_{I'}\sqrt Y)$. With one $t$-derivative, change the coordinate lacking a fixed spatial derivative envelope to $t$ at fixed other coordinate, giving $dz=k\,dt$ or $dw=k\,dt$ in absolute value. Use either the early weighted derivative integral or the early weighted profile supremum $O(b_I\rho_k/\sqrt X)$, depending on which coordinate is integrated. These yield the first term of (4). With two $t$-derivatives fix the early coordinate and integrate the other in $t$, leaving $1/k$ from $1/k^2$. The early weighted profile integral is $O(b_I\rho_k^2/\sqrt X)$; the large weighted profile supremum is $O(b_{I'}\sqrt Y)$. The same estimates on the other strip produce $\rho_k/Y$ and $\rho_k^2/(Yk)$, both no larger than the asserted factors. This proves (4) with the sharp original indicator undifferentiated and no boundary term assumed small.

After the joint numerator bound and the parent HS norm, $\sqrt{XY}b_Ib_{I'}$ costs $O(1)$, so the contribution of (4) is

$$
O_\epsilon\!\left(Q^\epsilon b\left[
       \frac{\rho_k}{X}K_1+\frac{\rho_k^2}{X k}K_2'\right]\right).
 \tag{6}
$$

If $k\ge A/Q$, then $\rho_k\le 9kQ$, and on a good pair the bracket is $O(K_1+QK_2')$. If $k<A/Q$, then $\rho_k\le9A$, every pair is good by $A\le QH/100$, and summing their second term costs $O_\epsilon(Q^\epsilon A^2/(QH))$, since $X\ge QH$ and $\sum 1/k\ll\log(3Q)$. This is $O_\epsilon(Q^\epsilon QK)$, or $O_\epsilon(Q^\epsilon QL)$ if only $k\le L$ is being summed, since $K,L\ge A/Q$ and $A\le QH$. Their first terms cost $O(KK_1)$ (or $O(LK_1)$) using $\rho_k/X\le1/4$.

If a pair is not good, necessarily $k\ge A/Q$, so $X<4\rho_k\le36kQ$. The unmodified R76 (5) derivative bound with the pointwise GRH weights bounded by $\sqrt X,\sqrt Y$, and the same parent aggregation, gives
$O_\epsilon(Q^\epsilon b[K_1+(X/k)K_2'])=O_\epsilon(Q^\epsilon b[K_1+QK_2'])$.
Any sharp mask or numerator symmetry used there contracts the positive upper estimate. Thus for all dyad pairs, after logarithmic dyad summation, the cost of the cutoff replacement on good pairs and the entire estimate on other pairs is

$$
O_\epsilon(Q^\epsilon bK[K_1+QK_2'])
 \tag{7}
$$

for aliases through $K$, and the same with $L$ through $L$. In particular this step does **not** require $K\ll H$.

## 3. Two exact marginal cancellations on the symmetric difference

Use the negative rational incidence convention of R82 (4), denoting its residue matrix by $A_a$. On either difference orientation interchanging residues negates $\sigma_1r+\sigma_2s$, hence $A_a^{\mathsf T}=A_{-a}$ on the exact unit set. Thus $\mathcal S_a=(A_a+A_{-a})/2$ is the symmetric cosine incidence and $\mathcal A_a=(A_a-A_{-a})/2$ the skew incidence. These each contract the common-test numerator bound by reflection, an isometry. Reflection multiplies the product-character coefficient $\nu(a)$ by $\nu(-1)$, so commutes with $\Pi_\times$. This both proves the description of the retained sine terms by odd product characters and shows why the split is made before any different fractional detunings. It gives no such claim about an orthogonal parity projection of the finished Fourier packet.

For a good pair with the smooth cutoff, both marginal integrals of $\partial_{zw}^2\mathcal H_\chi$ vanish: fixing $z$, integrate the $w$-derivative of $\partial_z\mathcal H_\chi$; fixing $w$, do the reverse. The profile primitives are absolutely continuous (R72), with fixed integrable envelopes of their parameter derivatives, and the product with the smooth cutoff obeys these same regularity bounds. Thus the indicated functions are absolutely continuous in the variable integrated for almost every fixed other variable. They are zero at both ends because of the cutoff and compact support. There is no restriction remaining on the raw quadrant for this modified kernel. It follows for *each* numerator before projection that

$$
\iint \partial_{zw}^2\mathcal H_\chi\,
             \mathbf F(z)^{\mathsf T}\mathcal S_a\mathbf F(w)
 =-\tfrac12\iint \partial_{zw}^2\mathcal H_\chi\,
       [\mathbf F(w)-\mathbf F(z)]^{\mathsf T}
             \mathcal S_a[\mathbf F(w)-\mathbf F(z)] .
 \tag{8}
$$

Indeed the two diagonal quadratic terms independently integrate to zero, and the symmetric cross terms are equal. Applying $\Pi_\times$ preserves this finite-vector identity. For a skew matrix the diagonal scalar is already zero, and replacing both vectors by the same increment would give zero rather than the original integrand: (8) is not the full difference field.

On the cut support the difference relation gives $w=z+h,\ h=\pm kt$, with $|h|\le2kQ\le z/4$ since $z\ge\rho_k$; also $w\asymp z$. For the first three chain-rule terms, just bound the squared increment norm in (8) by $O_\epsilon(Q^\epsilon X)$ on this support, since $z\le2X$. Their unweighted $L^1$ derivative integral is $O(b_Ib_{I'}K_1)$ by the R76 proof, with the cutoff profiles now satisfying the same fixed envelopes. After multiplying by $b$ and aggregating, $X/\sqrt{XY}\le1$, so each alias costs $O_\epsilon(Q^\epsilon b K_1)$ for these three terms.

For the fourth term fix $z$, and change $w$ to $t$, leaving $1/k$ from $1/k^2$. The common parameter derivative factor integrated in $t$ has $L^1$ norm $O(b_Ib_{I'}K_2')$ after taking suprema for the cutoff profiles and their normalized derivatives. At fixed $t$ use the actual shift $h$ and [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference), whose hypothesis is auxiliary Dirichlet GRH on $q'$ with polynomial parameters:

$$
\int_{\rho_k}^{2X}
        \|\mathbf F(z+h)-\mathbf F(z)\|_2^2\,dz
     \ll_\epsilon Q^\epsilon X |h| .
 \tag{9}
$$

Dyadic intervals starting at $\rho_k$, clipped at the top, are sufficient, with the same estimate for negative $h$ as in R83. The high character projection is fixed in $z,t$ and contracts that estimate. As $|h|\le2kQ$, the per-alias cost after HS is $O_\epsilon(Q^\epsilon b Q K_2')$, using $X/(XY)^{1/2}\le1$. Summed through $K$, together with (7), the full symmetric difference bound is

$$
O_\epsilon(Q^\epsilon b K[K_1+QK_2']) .
 \tag{10}
$$

## 4. Single increments and the sum orientation

For the full difference incidence on $k\le L$, retain both matrices or act on $A_a$ directly. With the same cutoff, the zero marginal in $w$ allows replacement of $\mathbf F(w)$ by $\mathbf F(w)-\mathbf F(z)$ while leaving the first vector unchanged; no symmetry is needed. The first three derivative terms cost $O_\epsilon(Q^\epsilon bK_1)$ per alias exactly as in §3 since $w\asymp z$ throughout the cut support. For the fourth, use the same affine change and (9), and use Cauchy–Schwarz at each fixed $t$ to estimate the raw integral of $\sqrt z\,\|\mathbf F(z+h)-\mathbf F(z)\|_2$ by $O_\epsilon(Q^\epsilon X^{3/2}\sqrt{kQ})$. Dividing by $k\sqrt{XY}$ in the derivative change and parent HS normalization gives

$$
\frac{X^{3/2}\sqrt{kQ}}{k\sqrt{XY}}
        =\frac{QV}{\sqrt{Uk}}\le Q\sqrt{V/k}.
$$

Summation through $L$ on each dyad pair, with the $L$-version of (7) and the logarithmic dyad summation, gives

$$
O_\epsilon\!\left(Q^\epsilon b
       [L K_1+Q\sqrt{ML}\,K_2']\right).
 \tag{11}
$$

Here $L\le4M$ allows absorbing the $QLK_2'$ part of (7). This argument removes both difference channels for $k\le L$, even when $kQ$ is larger than $A$. For the deleted sine portion alone one can simply use the contraction $a\mapsto -a$ in this same proof, so overlapping the bounds (10) and (11) creates no double counting in the exact mask.

For $++$, the relation $z+w=kt\le2kQ$ puts both coordinates in $[0,2kQ]$. If $4kQ\le X$, this is a true early region, and use the estimate (4) on the sharp derivative restricted to the support, with early threshold of order $kQ$ and **no** replacement or differentiation of the long mask. It gives $O_\epsilon(Q^\epsilon b\, (k/V)[K_1+QK_2'])$ per $k$ and dyad pair. If $4kQ>X$, use the unsmoothed estimate in §2, yielding $O_\epsilon(Q^\epsilon b[K_1+QK_2'])$. The result in either case is $O_\epsilon(Q^\epsilon b\min(1,k/V)[K_1+QK_2'])$, up to an absolute constant also in the second case where $k/V>1/4$. Hence the full sum orientation, with its original negative sign, costs

$$
O_\epsilon\!\left(
       Q^\epsilon b K\min(1,K/H)[K_1+QK_2']\right)
 \tag{12}
$$

through $K$, using $V\ge H$ and summing dyad pairs. No short-increment estimate is required for (12); the pointwise progression bound under auxiliary GRH still enters.

## 5. Exact Fourier restoration

Apply (10) for the symmetric part through $K$, the sine-only version of (11) through $L$, and (12) for the sum part through $K$. These complementary deleted pieces recreate exactly $\mathcal X_{\rm res}-\mathcal Y_{K,L}$ with the original signs, at each common test. The temporary cutoff was used only in the proofs of (10) and (11); the definition of the residual in §1 keeps the original sharp $z,w>A$ integration.

For fixed $b,\ell$ apply the Taylor detuning weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field). The effective $K_1$ is $O(1+|\ell|)$ and $K_2'$ is $O(S^{-1}+(1+|\ell|)^2/Q)$; the bounded fractional factors multiply the output of each common test **after** the projections and their joint estimates. Keep the actual outer unit phase, divide by $J\asymp Q$, then square-sum $b,\ell$ using $\sum_{B/2\le b\le B}b^2\ll B^3$ and the shift power sums $O(R_*^3), O(R_*^5), O(R_*)$. This proves (1) and the separate bound for the sum deletion, with exact taper and detuning at every affected index.

At (2), $K$ and $\sqrt{ML}$ both have exponent $81/200$. The three powers in (1) are $-1/160,\ -3/800,\ -19/4000$ respectively. The R82 comparison with sharp $\widehat T,\widehat P$ has larger error $Q^{-1/500+\epsilon}$ and is unchanged, proving the stated inherited comparison while leaving the intermediate odd-product and full larger-alias covariance unestimated.
