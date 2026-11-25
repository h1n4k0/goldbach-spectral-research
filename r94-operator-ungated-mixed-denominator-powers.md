# Partial product Parseval removes the shared-prime excess cutoff

The mixed-power relation concerns only the part of the denominator coprime to the alias. Conditioning on that part of the product, instead of on the entire product, leaves a vector of numerators on the shared-prime part. Bounding that vector jointly eliminates the shared-prime power loss in the mixed-relation deletion, even at unrestricted prime-power denominators.

## 1. The same selected sector, with no excess cutoff

Use the exact $Z_{\rm ind}$ of R92, with its real shell parameter, original common taper, $J^{-1}$ normalization, actual parent profiles $h,f$, and separated high-denominator packet $\mathcal C_+(B,R)$. As in R93, assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH up to $\lceil8MB\rceil+2$, including modulus $1$. Keep all original parameter ranges, the actual $k>K\ge A/Q$ aliases, $(2k,b)<G$, $z,w>A$, and every earlier character selection. Either input of R92 is allowed, with or without the exact R86/R87 parity removals; the former has $K\ge2P$.

For each $q=2k,b$, set

$$
q'=qb,\qquad b=dm,\qquad
 d=\prod_{p\mid q}p^{v_p(b)},\qquad q_0=qd,\qquad q'=q_0m,\qquad (q_0,m)=1 .
 \tag{1}
$$

With $C>0,D_{\rm mix}\ge1$, put $V_Q=\lfloor(\log Q)^C\rfloor$. Remove exactly the pairs in [R93 (2)](r93-operator-unequal-mixed-denominator-powers.md#1-exact-sector-and-bound),

$$
\operatorname{cond}(\eta^u(\eta')^v)\le D_{\rm mix}
       \quad\hbox{for some integers }1\le u,v\le V_Q,\quad u\ne v ,
 \tag{2}
$$

where $\eta,\eta'\bmod m$ are the two individual components on $m$. The cut now applies at **all** original eligible $k,b$, without a condition on $d/(q,d)$. Write $Z_{\rm all}$ for the field after the deletion, keeping the original three signs, raw constraints and earlier product and leg selections. With $R_*=1+R$ and the [packet norm of R92](r92-operator-individual-denominator-power-conductors.md#1-exact-input-and-conclusion),

$$
\|Z_{\rm ind}-Z_{\rm all}\|_{\rm pkt}
       \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B\sqrt{D_{\rm mix}}M
        \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The same estimate applies when the deletion is restricted to any subset of aliases that depends only on $k,b$, in particular to the high-excess complement of the R93 gate. It also holds after fixed orthogonal spatial compression or restriction to a subset of the packet.

For $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250},\ D_{\rm mix}=Q^{3/1000}$, and the other R93 scales, (3) is $O_{\epsilon,C}(Q^{-9/4000+\epsilon})$. For the input with both earlier parity removals the sharp $\widehat T,\widehat P$ comparison stays $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm all}$. This estimates a deletion on this packet. It does not bound the remaining covariance, an individual even modulus, other packets, or weak S.

## 2. Joint control at one partial product

Fix $q,b$ as in (1), one of the original orientations $\sigma=(\sigma_1,\sigma_2)$, and a common test before all numerator-specific detunings. Use the negative rational incidence of [R82 (4)](r82-operator-low-product-character-long-quotient.md#2-exact-dependence-on-the-product-of-the-two-characters):

$$
A_a(r,s)=\mathbf 1_{q\mid\sigma_1r+\sigma_2s}
              e(-a(\sigma_1r+\sigma_2s)/q'),\qquad e(x)=e^{2\pi i x},
 \tag{4}
$$

on units $r,s\bmod q'$ and reduced $a\bmod b$. The reduced numerator is indexed by the pair of units $a_d\bmod d,\ a_m\bmod m$. The $q_0$ and $m$ phases in CRT have local numerators $a\bar m$ and $a\bar q_0$, with each inverse taken on the respective coprime factor. The congruence in (4) lives entirely in $q_0$. On its support, the integer quotient $(\sigma_1r_0+\sigma_2s_0)/q$ is defined modulo $d$, so the $q_0$ phase uses $a_d\bar m\bmod d$. The $q_0$ incidence $A^{(0)}_{a_d}$ is therefore the exact R76 incidence at denominator $d$, with a fixed unit permutation of the reduced numerators, and the negative phase convention. The $m$ phase has no relation between the two residue variables besides their separate unit masks. For either trivial factor use the singleton numerator/character and phase one on that factor.

For arbitrary complex unit residue vectors $X,Y$ on $q'$, expand multiplicatively only on $m$:

$$
X(r_0,r_m)=\phi(m)^{-1}\sum_{\eta\bmod m}
                     \mathsf X_\eta(r_0)\bar\eta(r_m),
 \qquad \sum_\eta\|\mathsf X_\eta\|_2^2=\phi(m)\|X\|_2^2,
 \tag{5}
$$

and similarly for $Y$. All norms on unit residue arrays here use counting measure. The $m$-factor of the bilinear incidence for $\eta,\eta'$ is the product of two additive Gauss factors. The additive frequencies are primitive because $a_m,\bar q_0,\sigma_i$ are units. Substituting $r_m\mapsto a_m^{-1}r_m$ and $s_m\mapsto a_m^{-1}s_m$ separates out $(\eta\eta')(a_m)$. The remaining coefficient $c_{\eta,\eta'}$, including the fixed CRT factors, has absolute value at most $m$, by the primitive-additive bound for arbitrary characters in [R81 §2](r81-operator-low-conductor-long-quotient.md#2-exact-local-power-vanishing-and-the-low-conductor-fourth-moment). In particular no wild part on $q_0$ has been assessed by an individual full-product Gauss bound.

Let $\mathscr B_\rho(X,Y)$ denote the vector indexed by the reduced $a_d$'s which is the coefficient of $\rho(a_m)$, with $\rho\bmod m$, in the full numerator output $(X^{\mathsf T}A_aY)_a$. The exact formula is

$$
\big(\mathscr B_\rho(X,Y)\big)_{a_d}
   =\phi(m)^{-2}\sum_{\eta\bmod m} c_{\eta,\rho\bar\eta}\,
              \mathsf X_\eta^{\mathsf T}
                  A^{(0)}_{a_d}\mathsf Y_{\rho\bar\eta}.
 \tag{6}
$$

For arbitrary $q_0$-vectors $U,V$, the joint additive numerator bound [R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) here is $d\|U\|_2\|V\|_2$. Indeed the incidence splits into $d$ congruence matrices on $q_0=qd$, one for each possible affine quotient residue modulo $d$. Each is a partial permutation, and additive Parseval over all $d$ numerators, then restriction to the units, gives that bound. Apply it to (6), use $|c_{\eta,\rho\bar\eta}|\le m$, and then Cauchy over the bijective partner map $\eta\mapsto\rho\bar\eta$. From (5),

$$
\|\mathscr B_\rho(X,Y)\|_{\ell^2(a_d)}
        \le \frac{dm}{\phi(m)}\|X\|_2\|Y\|_2
        \ll_\epsilon Q^\epsilon d\|X\|_2\|Y\|_2 .
 \tag{7}
$$

This holds for non-squarefree $d,m$ with no other restriction on their exponents. In particular (7) is valid on arbitrary raw partial Fourier-transformed vectors when they occur later; it is not just a bound at two particular progression values.

## 3. Exact selections and the conditional raw estimates

The fixed partial product $\rho$ forces $\eta'=\rho\bar\eta$. In its coefficient the mixed selection (2) is equivalent to the R93 subset $\mathcal L_m(\rho)$ defined by $\operatorname{cond}(\eta^{u-v}\rho^v)\le D_{\rm mix}$ for at least one allowed $(u,v)$. This subset is invariant under $\eta\mapsto\rho\bar\eta$, since both exponent orders occur. Put $F_\rho(z)$ for the true centered progression vector after all R92 leg selections, restricted further to this subset on $m$. Using $F_\rho$ on both legs of (6) implements the deletion exactly within the component $\rho$; there is no arbitrary matrix mask in (7). In the true ranges, R93 (8)–(9) give

$$
\begin{split}
 \|F_\rho(z)\|_2^2&\ll_\epsilon Q^\epsilon f(m)\,z,\\
 \int_X^{2X}\|F_\rho(z+h)-F_\rho(z)\|_2^2\,dz
       &\ll_\epsilon Q^\epsilon f(m)\,X|h|,\qquad 1\le |h|\le X/4,\\
 0\le f(m)&\le1,\qquad
     \sum_{m\le B} f(m)\ll_{\Theta,C,\epsilon}Q^\epsilon D_{\rm mix}.
 \end{split}
 \tag{8}
$$

These are true per-character GRH pointwise and integrated increment bounds summed over the subset. The underlying fiber count uses only $\rho$ and the translated power on $m$, not the rest of the full product. Earlier individual cuts still act on the actual complete character of $q'$; they may depend on other CRT factors and can only reduce the count. The projected progression functions and their coefficients may be complex.

It remains essential to keep the **full** product masks of R82/R91. The full product character on $b$ is uniquely a pair $(\nu_d,\rho)$ by CRT. Thus for each fixed $\rho$ those masks are precisely an orthogonal projection $\Pi_\rho$ of the $a_d$-vector onto the multiplicative characters $\nu_d(a_d)$ with the permitted full product $\nu_d\rho$. This follows by coefficient extraction in the exact tensor product of the two finite multiplicative bases, or by applying R82 (5)–(6) to the $q_0$ incidence at denominator $d$. The fixed unit permutation in §2 changes coefficient phases, not the projector. The projector may vary with $\rho$ but is fixed in the raw variables and shell parameter; it costs no loss in (7). In particular we have not replaced the full product cut by a restriction only on $\rho$.

On either difference orientation, the full residue transpose is $A_a^{\mathsf T}=A_{-a}$. In the two numerator coordinates the reflection sends $(a_d,a_m)$ to $(-a_d,-a_m)$. Extracting the coefficient of $\rho(a_m)$ gives the exact identity

$$
\mathscr B_\rho(Y,X)=\mathcal J_\rho\mathscr B_\rho(X,Y),
 \qquad (\mathcal J_\rho L)(a_d)=\rho(-1)L(-a_d).
 \tag{9}
$$

The linear map $\mathcal J_\rho$ is a unitary involution and commutes with $\Pi_\rho$, since reflection is diagonal in the $a_d$ character basis. Therefore $(I+\mathcal J_\rho)\Pi_\rho\mathscr B_\rho/2$ and $(I-\mathcal J_\rho)\Pi_\rho\mathscr B_\rho/2$ are, respectively, symmetric and skew complex bilinear forms with values in the same finite numerator space. Their joint bound is (7); transposition here does not take a complex conjugate. The form for the signed sum orientation only needs $\Pi_\rho$ and (7).

## 4. Common tests, the sharp masks, and exact packet transfer

For the unmodified raw larger-alias field, apply the fixed-alias proof of [R89 §3](r89-operator-prime-to-denominator-alias-conductors.md#3-per-alias-weighted-estimates-and-the-exact-masks) in the finite $\ell^2(a_d)$ space at each $\rho$. Let $K_1=\|\omega\|_\infty+\|\omega'\|_1,\ K'_2=\|\omega''\|_1+K_1/Q$ for its common test $\omega\in C_c^2((Q,2Q))$. In the two differences, the true sharp-to-smooth comparison on good pairs, and the direct bound on other pairs, use the R84 scale $\rho_k=A+8kQ\le9kQ$ and two pointwise bounds of (8). The smoothly cut symmetric form uses the two zero raw marginals in [R84 (8)](r84-operator-short-cosine-and-sum-aliases.md#3-two-exact-marginal-cancellations-on-the-symmetric-difference) with the same $F_\rho$ on both legs. On the skew form of (9), restrict $F_\rho$ to the same raw interval on both legs. The pointwise endpoint and interior increment estimates in [R85 (3)](r85-operator-skew-translation-all-short-aliases.md#3-a-weighted-raw-translation-estimate-for-the-skew-incidence) both scale by $f(m)$ in squared norm, using (8). Oddness under raw translation comes from skew transposition; bilinear Plancherel applies componentwise in the finite space, and (7) at opposite raw frequencies controls its joint norm. Thus the R85 first moment and weighted raw pairing have the same factor $f(m)$. For either form the fourth chain term still changes $w$ to the actual $t$ before estimating the raw translation $h=\pm kt$; $1/k$ remains and $|h|/k\le2Q$. The other derivative terms and the sum orientation use the same pointwise norms as in R89. All parent square sums are unchanged. This gives joint cost $O_\epsilon(Q^\epsilon d f(m)[K_1+QK'_2])$ at each $\rho,k,b$.

For the post-R86/R87 input, subtract the deleted parts of the two exact parity pieces, with the original [overlap convention](r87-operator-adaptive-raw-minimum-even.md#2-exact-reflection-on-the-raw-order). Both reflected raw orientations still have the same incidence on the relevant auxiliary-even leg after extracting $\rho(a_m)$ and applying $\Pi_\rho$: the original identity holds for each full numerator, and all auxiliary residue reflections act diagonally on the leg characters, preserving the fixed projections. This justifies using the true combined derivative kernels of [R86](r86-operator-long-alias-short-leg-even.md#3-bound-the-integrated-difference-at-a-fixed-alias) and R87, with no marginal identity on their sharp raw masks. On either leg the parity projections contract the pointwise bounds (8). Therefore the optional cost per $\rho,k,b$ from the exact R92 (8) pointwise argument is bounded by

$$
O_\epsilon\!\left(Q^\epsilon d f(m)\frac{QP}{k}
                                      (E_\infty+E_1)\right),
 \quad
 E_\infty=\|\omega'\|_\infty+\|\omega\|_\infty/Q,\qquad
 E_1=\|\omega''\|_1+\|\omega'\|_1/Q+\|\omega\|_1/Q^2 .
 \tag{10}
$$

The sum orientation keeps its original negative sign, and neither boundary nor unit contributions have been newly approximated.

Restore the $a_m$ dimension by multiplicative Parseval after the common tests. Since the bound is uniform in $\rho$, the resulting joint numerator HS norm is at most $\phi(m)$ times the preceding bound. This factor is $\sqrt{\phi(m)}$ from character orthogonality times $\sqrt{\phi(m)}$ for all possible partial products. As $d\phi(m)\le b$, the total per-alias numerator cost is bounded by $Q^\epsilon b f(m)$ times the same test seminorms, with $P/k\le1/2$ in (10). In particular there is no factor $d/(q,d)$. All steps before this point have the common test; no numerator projection is moved across the distinct fractional detunings.

Group each actual $k\le4M$ by its unitary divisor $d\mid b$, for which $\operatorname{rad}(d)\mid2k$ and the count is $O(M/\operatorname{rad}(d))$ as in [R91 (8)](r91-operator-denominator-product-power-conductors.md#3-sum-the-shared-factor-cost-in-the-actual-raw-estimates). A subset fixed by $k,b$ can only decrease this count. Thus the per-$b$ total factor, apart from the common seminorms, is $O_\epsilon(Q^\epsilon bM L_b)$ with

$$
L_b=\sum_{\substack{d\mid b\\(d,b/d)=1}}
                       \frac{f(b/d)}{\operatorname{rad}(d)},
   \qquad
   \sum_{b\le B}b^2L_b^2\ll_{\Theta,C,\epsilon}Q^\epsilon B^2D_{\rm mix}.
 \tag{11}
$$

The sum is R93 (13): apply Cauchy over $d$, enlarge to all $dm\le B$ in the positive majorant, and use $f^2\le f$, (8), and the subpower $\sum_{d\le B}\operatorname{rad}(d)^{-2}$ from R92 (9). This covers arbitrary $b$.

Finally use the exact [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) Taylor tests with the original $a$-dependent coefficients bounded by $2^{-n}$ at index $n$, the original unit-modulus phases and $J^{-1}$. At offset $\ell$, the weighted $K_1$ is $O(1+|\ell|)$ and the other weighted seminorms are $O(S^{-1}+(1+|\ell|)^2/Q)$, as in R93. After division by $J\asymp Q$, the factors in brackets are consequently $(1+|\ell|)/Q,\ (1+|\ell|)^2/Q,\ 1/S$. Square-sum over $|\ell|\le R+1$ and use (11) on the denominators. This proves (3) with all true masks, weights and detunings. None of the deterministic model or sharp-shell errors from prior rounds changes.

## 5. A nonzero incidence above the former excess gate

At the numerical scales, fix $1/2500<\theta<1/20$ and take $d=2^e\asymp Q^\theta$, $k=r\asymp Q^{11/20}$ an odd prime, and $m$ an odd prime with $b=dm$ in the high denominator band. Such prime choices exist for large $Q$ by Bertrand's postulate. Then $(q,b)=2<G$ and $d/(q,d)=2^{e-1}$, exceeding the numerical R93 gate for large $Q$. On the $r$ factor pair a generator-order character with its conjugate, and on $m$ pair a generator $\eta$ with $\eta'=\eta^{-2}$. As in R93 §5 the latter two individual characters and their product retain conductor $m$ under all earlier allowed powers, while $\eta^2\eta'=1$. The alias powers on $r$ also keep the required conductor. In both legs at $2^{e+1}$ take conjugate primitive characters $\xi_2,\xi'_2$, so the $d$-component of the product is principal and both top local powers survive the earlier exact vanishing criterion.

The actual local coefficient at $2^{e+1}$ is nonzero. In R93 (4) with $p=2,a=1$, the $r$-sum at fixed $x$ (here $r$ is the local unit residue) is the Ramanujan sum $2^e\mathbf 1_{2^e\mid x}-2^{e-1}\mathbf 1_{2^{e-1}\mid x}$. The first term contributes $2^e$; the second totals zero because $\xi'_2$ is nontrivial on the top subgroup $1+2^e j,\ j\bmod2$. Multiplying by the ratio of the totients in R93 (4) gives magnitude $2^{e+1}$. The factors at $r,m$ are nonzero by conjugacy and the primitive coprime Gauss evaluations, respectively. This is a genuine coefficient allowed into the deletion above the former gate in the unmodified input. It does not assert any lower bound on the integrated field.
