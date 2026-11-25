# Adaptive raw-minimum deletion in the actual larger-alias field

The signed sum–difference reflection applies to the **smaller raw coordinate** even when that coordinate belongs to the larger physical dyad. For a physical dyad well above the short-alias cutoff, the true parent profile is proportional to the square root near zero. Keeping this factor through the signed derivative estimate permits a square-root adaptive raw cutoff. This removes a genuine sector of larger aliases inside high–high and equal physical dyads.

## 1. Actual masks and the packet estimate

Use the complete even shell, transported parent families $h,f$, Fourier convention $J^{-1}\sum_m$ with $N=2m$, common taper $\omega_S$, and uniquely centered high-denominator packet $\mathcal C_+(B,R)$ of [R85](r85-operator-skew-translation-all-short-aliases.md) and [R86](r86-operator-long-alias-short-leg-even.md). Retain original local Dirichlet GRH at the even targets and auxiliary Dirichlet GRH through $\lceil 8MB\rceil+2$, including modulus $1$. Let $\mathcal Z_{>K}$ be the exact R85 larger-alias field: it retains $k>K$, both raw coordinates $>A$, both true high individual projections, high product conductors $>D_\times$, the mask $(2k,b)<G$, and all original signed orientations. Write $R_*=1+R$.

Fix $H\le P\le M$. For each matrix entry split the actual raw integral into its two orders by size, after the mixed derivative has been taken. On a branch call the smaller raw coordinate $z$, and the larger $w$; ties can be assigned to either branch since their line has zero area. Let $V$ be the physical dyad start associated with $z$, and $U$ that associated with $w$. They are not ordered and may be equal. Use the cutoff

$$
Z_V=
 \begin{cases}
     2QV,&V<4P,\\
     Q\sqrt{PV},&V\ge4P .
 \end{cases}
 \tag{1}
$$

Define $\mathcal R_{P,K}$ as the contribution in the two branches with $z\le Z_V$, in which the genuine high progression vector at $z$ is additionally projected to its **even characters of the auxiliary modulus $q'=2kb$**. The other leg is unchanged. These are integration masks on the actual derivative, not differentiated cutoffs or masks on a new coefficient. In this definition all original signs, the sharp bounds $z,w>A$, and the exact detunings and other selections in $\mathcal Z_{>K}$ are kept. There is no requirement $K\ge2P$ for this raw-minimum deletion. Additional alias masks independent of the primitive numerator and common to the paired orientations are allowed.

Then

$$
\left(\sum_{j\in\mathcal C_+(B,R)}
              \|\mathcal R_{P,K}(j)\|_{\rm HS}^2\right)^{1/2}
   \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B^{3/2}P
         \left[\frac{R_*^{5/2}}{Q}+\frac{R_*^{1/2}}S\right].
 \tag{2}
$$

After removing the R86 field $\mathcal E_{P,K}$, if $K\ge2P$, the same estimate holds for the raw deletion applied to the **remaining** field; denote that second deletion by $\mathcal R^{\rm rem}_{P,K}$. This formulation never subtracts the overlap twice. A fixed orthogonal spatial compression or restriction to any subset of the packet contracts the bounds.

At the R85–R86 parameters

$$
\begin{gathered}
 H=Q^{2/5},\quad M=Q^{3/5},\quad W_V=Q^{23/175}V^{4/7},
 \quad A=Q^{6/5},\quad B=\lfloor Q^{39/100}\rfloor,\quad
 R=\lfloor Q^{1/400}\rfloor,\quad S=Q^{249/250},\\
 D_\times=Q^{1/1000},\quad G=Q^{1/5},\quad
 K=\lfloor Q^{81/200}\rfloor,\qquad P=K/2 ,
 \end{gathered}
$$

the rate in (2) is $O_\epsilon(Q^{-3/800+\epsilon})$. If $V\asymp M$, the cutoff $Z_V$ is of order $Q^{1+201/400}$. This covers raw coordinates well above $QK$ at such $V$ and can occur even on equal or maximal physical dyads; R86 does not remove anything on those pairs. The exact sharp $\widehat T$ and $\widehat P$ each differ from $\mathcal Z_{>K}-\mathcal E_{P,K}-\mathcal R^{\rm rem}_{P,K}$ by $O_\epsilon(Q^{-1/500+\epsilon})$ in this packet norm, using the inherited R86 comparison. No bound for that remaining field is asserted. The argument does not delete smaller-raw odd characters in these strips, estimate both-raw-large terms, bound all Fourier modes or give a pointwise modulus or weak-S result.

## 2. Exact reflection on the raw order

Work first before numerator-specific detuning, with a common scalar test $\omega\in C_c^2((Q,2Q))$ at a fixed $k,b$. In a raw branch relabel coordinates as needed so $z\le w$; when relabeling, exchange the two difference orientations. At fixed dyads $V,U$ put $X=QV,\ Y=QU$, and write $U_t(z)$, $V_t(w)$ for their actual profiles (the notation $V_t$ is the second profile, not a dyad start). Use the high vectors from [R81](r81-operator-low-conductor-long-quotient.md) and the high product projector $\Pi_\times$ on the complete reduced numerator family from [R82](r82-operator-low-product-character-long-quotient.md). As in [R86 (2)](r86-operator-long-alias-short-leg-even.md#2-reflection-in-the-exact-switched-incidence), the sum incidence on the actual auxiliary unit set satisfies

$$
A_a^{++}(r,s)=A_a^{-+}(-r,s).
 \tag{3}
$$

This statement is true modulo $q'=2kb$, without a coprimality assumption between $2k$ and $b$. The even projector on the vector at $z$ makes the two finite bilinears equal. The identity survives $\Pi_\times$ by linearity on the numerator family; equivalently reflection acts on a corresponding short coefficient by $\xi(-1)=1$, leaving its product character unchanged. The common-divisor mask is the same in both. In the $+,-$ orientation the parameter $(z-w)/k\le0$, so that orientation and its derivative give zero on the branch under the support of the common test.

Set $t_\pm=(w\pm z)/k$ and $\mathcal H_\pm(z,w)=\omega(t_\pm)U_{t_\pm}(z)V_{t_\pm}(w)$. Including the original positive difference and negative sum signs, (3) gives the **same** numerator vector against

$$
\partial_{zw}^2\mathcal H_- -\partial_{zw}^2\mathcal H_+
 \tag{4}
$$

on $z,w>A,\ z\le w,\ z\le Z_V$. In particular the two derivative kernels are combined before putting absolute values on integrals. The two raw masks are common to the compared orientations and there is no boundary measure at $z=w$ or $z=Z_V$. If the roles of the original two coordinates were exchanged, the surviving positive orientation is the other one; the calculation is the same in the relabeled variables. All these identities concern the integrated centered product already identified in R82, not a reflection of the original sharp Fourier coefficients after their distinct detunings.

The R86 physical-short removal is compatible with this argument. On an entry selected by R86 its remaining progression vector on that physical leg is the auxiliary-odd projection of its high vector at all raw points. On a raw branch where this is the smaller raw leg, the new raw-even component is zero, since the projections are orthogonal. On the other branch the added odd projection is on the **other** leg. The reflection only acts on the even restricted leg, so (3)–(4) still apply; the longer-raw leg projection is an $\ell^2$ contraction. On entries not selected by R86 the definitions coincide. This proves the exact overlap rule for $\mathcal R^{\rm rem}_{P,K}$, with all projections taken before the original fractional multipliers.

## 3. Weighted derivative bounds

Let

$$
E_\infty=\|\omega'\|_\infty+\|\omega\|_\infty/Q,\qquad
 E_1=\|\omega''\|_1+\|\omega'\|_1/Q+\|\omega\|_1/Q^2 .
$$

Use the exact [R72 profile envelopes](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes): $Q^j\partial_t^j U_t$ is bounded by $O(b_I)$, its first raw derivative has fixed $L^1$ envelope of mass $O(b_I)$, and the support is $[0,2X]$, for $0\le j\le2$. The second leg has the corresponding $b_{I'}$ bounds and raw support $[0,2Y]$. Products with $\omega$ are extended by zero outside its compact parameter support. Since the profile primitives are absolutely continuous with the stated envelopes, all mixed derivatives below are ordinary integrable functions almost everywhere, as in R86.

If $V<4P$, apply the unweighted derivative calculation [R86 (4)–(5)](r86-operator-long-alias-short-leg-even.md#3-bound-the-integrated-difference-at-a-fixed-alias). It uses only the first raw support length $2X$, the bound $2z/k\le4X/k$ on the parameter shift, and the fixed envelopes on the other leg, so does not require $V\le U$. It gives absolute derivative integral $O(b_Ib_{I'}(X/k)(E_\infty+E_1))$ on the branch, even if $X>Y$. With pointwise GRH bounds on the vector norms of $O_\epsilon(Q^\epsilon\sqrt X)$ and $O_\epsilon(Q^\epsilon\sqrt Y)$, this case has effective scalar cost $X/k\le4QP/k$ after the parent square sums.

If $V\ge4P$, use the written cutoff $Z_V\le X/2$. On this interval both genuine $h$ and $f$ are the **same** multiple $c_t\sqrt z$, whose normalized parameter derivatives are $O(b_I/\sqrt X)$; this is the early analytic part of [R84 §2](r84-operator-short-cosine-and-sum-aliases.md#2-common-test-and-an-adaptive-raw-cutoff). In particular

$$
\sqrt z\,|Q^j\partial_t^j(\partial_z U_t)(z)|\ll b_I/\sqrt X,\qquad
 \sqrt z\,|Q^j\partial_t^j U_t(z)|\ll b_I z/\sqrt X
                     \quad(0\le j\le2).
 \tag{5}
$$

On the second leg, both the weighted raw derivative integral and the weighted supremum of the profile are $O(b_{I'}\sqrt Y)$, using the fixed support and envelopes with $\sqrt w$. These two weights in (5) and on the other leg will account for the genuine GRH progression vector $\sqrt z\sqrt w$ factors.

For clarity, at fixed $z,w$ write $B_0=\omega U_zV_w,\ B_1=\omega U_zV,\ B_2=\omega UV_w,\ B_3=\omega UV$ as functions of $t$; the raw derivatives here are at fixed $t$. The four terms of (4) are

$$
B_0(t_-)-B_0(t_+),\quad
 k^{-1}(B_1'(t_-)-B_1'(t_+)),\quad
 -k^{-1}(B_2'(t_-)+B_2'(t_+)),\quad
 -k^{-2}(B_3''(t_-)+B_3''(t_+)).
 \tag{6}
$$

For the first term use a parameter derivative supremum and the shift $2z/k$. With (5) its weighted short raw cost is $b_I/\sqrt X$ times $\int_0^{Z_V}2z\,dz/k$; on the other leg use the weighted derivative integral. For the second use the parameter derivative integral in the interval $[t_-,t_+]$. After taking the weighted supremum of the other profile (which has no raw derivative in this term), the scalar second-derivative envelope has $L^1$ norm $O(E_1)$ and is independent of $w$. With $z$ fixed, the change $w\mapsto t_-$ cancels $1/k$; Fubini counts each scalar $t$ over an interval of length $2z/k$ in $t_-$. The weighted early raw derivative envelope thus again integrates against $2z/k$.

For the third term the weighted first profile contributes $b_I z/\sqrt X$; use the weighted derivative integral on the other profile, a parameter derivative supremum, and the displayed $1/k$. In the fourth term use that same weighted first profile and the weighted second profile supremum. At fixed $z$, changing $w\mapsto t_\pm$ gives a scalar second-derivative $L^1$ bound, leaving one factor of $1/k$. These third and fourth terms integrate $z$ up to $Z_V$ with no further shift factor. In all four upper bounds one may enlarge the $w$ integration after taking the absolute value of each term in the paired derivative calculation; this does not move a raw mask into the derivative. Both shift terms have used the actual affine length $2z/k$, not $O(Z_V/k)$ evaluated at an unrelated physical support. Consequently the weighted integral of (4) on the branch is

$$
\ll_{\Gamma,\Theta} b_I b_{I'}\sqrt{XY}\,
          \frac{Z_V^2}{Xk}(E_\infty+E_1),\qquad
                         \frac{Z_V^2}{X}= QP .
 \tag{7}
$$

## 4. Aggregate the actual numerator family and exact Fourier tests

At each raw point use [R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) on the common numerator vector in (3). The original high vectors, the auxiliary-even or auxiliary-odd projections on a leg, and $\Pi_\times$ all obey the same joint bound $b\|F(z)\|_2\|F(w)\|_2$, using the corresponding contractions before detuning. Auxiliary GRH and residue Parseval give the weighted bound $O_\epsilon(Q^\epsilon b\sqrt z\sqrt w)$. Applying (7), or the first case of §3, yields a parent entry bound with factor $b_I b_{I'}\sqrt{XY}$, whose joint HS cost on the dyad pair is $O(1)$ by $\sum_I b_I^2\ll X^{-1}$, $\sum_{I'}b_{I'}^2\ll Y^{-1}$. Thus after summing both disjoint branches, the logarithmically many dyad pairs, and aliases $k>K$ up to their genuine support $4\max(V,U)$, the common-test cost is at most

$$
O_\epsilon\!\left(
                     Q^\epsilon b\, QP(E_\infty+E_1)\right).
 \tag{8}
$$

Here the $1/k$ is summed harmonically; no independence or orthogonality of aliases is assumed. The arithmetic and spatial factor bounds are the same for the unmodified raw-even part and for the R86-complement raw-even part by §2.

Finally use the common Taylor detunings from [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) and their $E_\infty,E_1$ bounds as in R86 §4. The effective common-test cost for the two seminorms together is $O(S^{-1}+(1+|\ell|)^2/Q)$ on the integer offset $\ell$. The exact fractional coefficients multiply the output of each common test, and the outer unit-modulus phase and $J^{-1}$ normalization are retained. Sum in $\ell^2$ over $B/2\le b\le B,\ |\ell|\le R+1$, with $\sum b^2=O(B^3)$, $\sum_\ell (1+|\ell|)^4=O(R_*^5)$ and $O(R_*)$ offsets for the taper term. This proves (2) with the original phases and sharp masks. The two exponents at the stated parameters are $-3/800$ and $-19/4000$. Only the exact integrated high product is reduced; the previously subtracted benchmark and sharp-shell comparison are unchanged.
