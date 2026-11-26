# A logarithmic shared exponent difference gives the full alias saving

In the three-factor conductor test, the translated power map on the shared factor uses the **difference** of its two exponents. When only this difference is logarithmic, a stronger square-torsion estimate is available. On actual large shared aliases it improves the inverse square-root saving to a full inverse power, while allowing the other exponent ranges to remain any fixed powers of the logarithm.

## 1. The exact incremental deletion

Use the genuine field $Z_{\rm large}$ retained by [R105 §1](r105-operator-large-shared-alias-joint-cut.md#1-exact-selected-sector-and-estimate). Keep the original complete even shell, genuine transported profiles $h,f$, common taper, $J^{-1}$ normalization, high-denominator packet $\mathcal C_+(B,R)$, all earlier selections and signs, and the true gates $z,w>A$, $k>K\ge A/Q$, $(2k,b)<G$. The same original local Dirichlet GRH at the even shell targets and the auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$, are assumed. Both earlier parity versions are permitted, including the exact R86/R87 post-parity version with $K\ge2P$. Keep the original polynomial ranges.

At an actual $q=2k,b$, use the real CRT factorization

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_bh_q,\qquad s=dh_q,\qquad q'=qb=r_bms .
 \tag{1}
$$

Here $h_q$ consists of the full powers in the original alias $q$ on the primes shared with $b$; it is not replaced by $(q,b)$ or by $\operatorname{rad}(d)$. The factors $r_b,m,s$ are pairwise coprime. Write $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$ for the two individual leg components on these three factors.

Fix $D,D_0,A_h\ge1$, a constant $C>0$, $V_Q=\lfloor(\log Q)^C\rfloor$ and $V_s=\lfloor\log Q\rfloor$. From $Z_{\rm large}$, delete, only at actual aliases with $d\ge D_0,\ h_q\ge A_h$, the remaining pairs such that

$$
\begin{gathered}
  \operatorname{cond}(\alpha^j)\,
       \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)\,
       \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D
       \quad\hbox{for some integers }1\le j,u,v,a,c\le V_Q,\\
                   u\ne v,\qquad 1\le |a-c|\le V_s .
 \end{gathered}
 \tag{2}
$$

Conductors are primitive inducing conductors, with one for the principal character. The logarithmic condition is on the shared **difference**, not independently on $a,c$, and does not shrink the alias or coprime-denominator ranges. All old equal and unequal cuts remain in force; no further containment of the new exponent ranges in R96 is needed. The deletion is made before the different numerator detunings.

Write $Z_{\log}$ for the resulting field. With $R_*=1+R$ and the original packet norm, the estimate is

$$
\|Z_{\rm large}-Z_{\log}\|_{\rm pkt}
  \ll_{\Gamma,\Theta,C,\epsilon}
   Q^\epsilon\,\frac{BD}{\sqrt{D_0}\,A_h}
   \left[\frac{R_*^{3/2}+R_*^{5/2}}Q
                         +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

It holds with all denominator prime powers, for restrictions of the deletion fixed by $k,b$, and after a fixed orthogonal spatial compression or packet restriction.

Use the second R105 example as input, with $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$ and its earlier $Q^{79/100}$ unequal cutoff on $h_q\ge Q^{9/50}$. Keeping those and the earlier thresholds unchanged, take $D_0=Q^{1/5},\ A_h=Q^{9/50},\ D=Q^{22/25}$ in (2). Then (3) is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$ for this larger selected conductor ceiling. The post-parity sharp $\widehat T,\widehat P$ comparison remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$ to the new field. This does not extend the larger ceiling to all shared differences or to small $h_q$, and it does not estimate the surviving covariance, an individual even modulus, other packets, or weak S.

## 2. The true shared power map needs only its difference

For an actual full product $\nu=\nu_d\rho\bmod b$, the original incidence forces precisely

$$
\alpha'=\bar\alpha,\qquad
       \eta'=\rho\bar\eta,\qquad
       \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{4}
$$

where $\pi_s$ is the unit reduction from $s$ to $d$. The union (2) is invariant under interchanging these true partners: conjugation preserves the alias power conductor, and swapping the two exponent pairs simultaneously preserves the inequalities, including the shared difference bound. The old retained masks preserve the same involution. Thus at fixed $\nu,k,b$ the new selected support is implemented by the same genuine projected progression vector $F_\nu$ on both raw legs. The earlier parity masks remain on their original legs.

For a positive order $j_0$ denote by $T_{j_0}(n)$ the number of characters on $n$ whose $j_0$-th power is principal; put $T_{j_0}(1)=1$. Set

$$
H(n)=\sum_{j_0\le V_Q} T_{j_0}(n),\qquad
        H_s(n)=\sum_{j_0\le V_s} T_{j_0}(n).
$$

As in [R105 §2](r105-operator-large-shared-alias-joint-cut.md#2-same-vector-support-and-the-uniform-product-conditioned-estimate), the three outputs at the fixed $\nu$ are the translated power map
$(\alpha,\eta,\gamma)\mapsto
(\alpha^j,\eta^{u-v}\rho^v,\gamma^{a-c}(\nu_d\circ\pi_s)^c)$.
Its nonempty fibers at a fixed tuple have cardinality $T_j(r_b)T_{|u-v|}(m)T_{|a-c|}(s)$. Both mixed differences are nonzero. The number of possible output characters of conductor at most $D$ is at most $D\tau(q')$ by counting primitive inducing divisors of $q'$; coprimality of the three factors gives precisely the product of component conductors. Sum over the allowed tuples, with at most polylogarithmic multiplicities, divide by $\phi(q')$, and absorb the polynomial-range inverse totient and divisor factors. The resulting fraction of genuine progression characters is at most

$$
O_{\Theta,C,\epsilon}\!\left(
          Q^\epsilon\,\frac{D H(r_b)H(m)H_s(s)}{r_bms}
                              \right).
 \tag{5}
$$

Only $H_s$ has the narrower range. This is uniform in the full product, and every inherited mask can only reduce this fraction. The empty range case is immediate.

The normalized residue Parseval of [R105 §2](r105-operator-large-shared-alias-joint-cut.md#2-same-vector-support-and-the-uniform-product-conditioned-estimate) gives the same factor (5) in the squared pointwise and integrated increment estimates for the projected genuine vector. Use the fixed-full-product scalar bound of [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms) with bilinear norm $O_\epsilon(Q^\epsilon\sqrt{\mathfrak e(q,b)})$ where $\mathfrak e(q,b)=d/(q,d)$, including for the raw Fourier arguments. Its exact transpose factor on the difference orientations is $\nu(-1)$. Therefore the R105 common-test bounds for the cosine, skew translation, and signed sum carry through with (5). On the reflected sharp parity pieces keep the old derivative identities and pointwise bounds, not a marginal identity on the sharp masks. All character restrictions are fixed and commute with the auxiliary leg parity projections. Full numerator Parseval costs at most $\phi(b)\le b$ because the fixed-product bound is uniform. Thus the true per-alias common-test cost is

$$
O_\epsilon\!\left(Q^\epsilon b \sqrt{\mathfrak e(q,b)}
   \frac{D H(r_b)H(m)H_s(dh_q)}{r_b m d h_q}\,\mathcal K\right).
 \tag{6}
$$

Here $\mathcal K=K_1+QK'_2$, with the inherited extra $Q(E_\infty+E_1)$ for the parity pieces when needed, using the same $P/k\le1/2$. This step is before the different numerator detunings and does not estimate any arbitrary pair mask.

## 3. A one-radical square-torsion moment

The new arithmetic input is

$$
\sum_{d\le B}\frac{H_s(d)^2}{\operatorname{rad}(d)}
                   \ll_{\Theta,\epsilon} Q^\epsilon .
 \tag{7}
$$

Indeed $H_s(d)^2\le V_s\sum_{j_0\le V_s} T_{j_0}(d)^2$. For each fixed $j_0$ the latter coefficient is multiplicative. Insert $d^{-\delta}$ for a fixed $0<\delta<1$ at cost $B^\delta$, bounding the nonnegative sum by

$$
B^\delta \prod_{p\le B}
        \left(1+\frac1p\sum_{e\ge1}
                           \frac{T_{j_0}(p^e)^2}{p^{e\delta}}\right).
 \tag{8}
$$

For $p\nmid2j_0$, $T_{j_0}(p^e)=\gcd(j_0,p-1)$. The sum of these local increments is bounded by a constant depending on $\delta$ times
$\sum_{p\le B}\gcd(j_0,p-1)^2/p^{1+\delta}$. To see the uniform bound on this last sum, use the elementary Jordan totient identity

$$
\gcd(j_0,p-1)^2
       =\sum_{\substack{v\mid j_0\\v\mid p-1}}J_2(v),
       \qquad J_2(v)=v^2\prod_{p\mid v}(1-p^{-2}).
$$

It follows by multiplying the prime-power divisor sums
$\sum_{i=0}^aJ_2(p^i)=p^{2a}$. For each $v$ enlarge the primes with $p\equiv1\bmod v$ to the integers $nv+1,\ n\ge1$. Their $p^{-1-\delta}$ sum is $O_\delta(v^{-1-\delta})$. Consequently

$$
\sum_{p\le B}\frac{\gcd(j_0,p-1)^2}{p^{1+\delta}}
        \ll_\delta \sum_{v\mid j_0}v^{1-\delta}
        \ll_\delta j_0^{1-\delta/2}.
 \tag{9}
$$

The last step is the elementary divisor bound $\tau(j_0)\ll_\delta j_0^{\delta/2}$. Since $j_0\le\log Q$, this is $o(\log Q)$ uniformly for every fixed $\delta>0$. There is no estimate for primes in progressions in this new step.

At $p\mid2j_0$ the elementary cyclic-unit bound $T_{j_0}(p^e)\le2j_0$, also used in [R105 §3](r105-operator-large-shared-alias-joint-cut.md#3-sum-the-large-shared-alias-parts-and-restore-the-packet), gives local logarithmic cost $O_\delta(\log(2j_0))$ in (8), hence total $O_\delta(\log^2(2j_0))=o(\log Q)$. The Euler product in (8) is therefore $Q^{o(1)}$ uniformly over the stated orders. Choosing $\delta$ small enough to absorb $B^\delta$ and summing the polylogarithmic number of orders gives (7). In contrast, the bound (9) with $j_0$ allowed to be an arbitrary fixed power of $\log Q$ does not by itself prove (7); the narrower range is used only for the shared factor.

## 4. The actual weighted alias sum and detuning

At fixed $b,d$ define $L_{b,d}$ as the sum of the arithmetic factors in (6) without $Q^\epsilon b$ and $\mathcal K$, over the actual selected alias group, zero if $d<D_0$. As in [R105 §3](r105-operator-large-shared-alias-joint-cut.md#3-sum-the-large-shared-alias-parts-and-restore-the-packet), use $r_bh_q\le8M$, the uniqueness of the alias for that pair, $(q,d)\ge\operatorname{rad}(d)$, and $H_s(dh_q)\le2V_sH_s(d)$ by [R99 (9)](r99-operator-unequal-shared-leg-powers.md#3-sum-the-full-shared-part-of-each-actual-alias) on the same prime support. With $U=\max(A_h,\operatorname{rad}(d))$, the inner $r_b$ sum in [R105 (8)](r105-operator-large-shared-alias-joint-cut.md#3-sum-the-large-shared-alias-parts-and-restore-the-packet) is bounded by [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) for $H$; the $h_q$ sum starts at $U$ and is $O_\epsilon(Q^\epsilon/U)$ by [R105 (9)](r105-operator-large-shared-alias-joint-cut.md#3-sum-the-large-shared-alias-parts-and-restore-the-packet). This yields the bound

$$
L_{b,d}\ll_{\Theta,C,\epsilon}Q^\epsilon
           \frac{D H(m)H_s(d)}
                  {m\sqrt{d\operatorname{rad}(d)}\,U}.
 \tag{10}
$$

Only those positive upper sums extend beyond actual aliases, not the selected field. The split into the two torsion ranges is maintained throughout.

Now use $U\ge A_h$ alone and (7), so there is no need to trade part of $A_h$ for a second radical factor. The other moment $\sum_{m\le B}H(m)^2/m^2\ll_\epsilon Q^\epsilon$ is the square of the positive R90 harmonic bound. Cauchy over the unitary divisors at fixed $b$, $b^2\le B^2$, and the positive relaxation to $dm\le B$ give

$$
\begin{split}
 \sum_{b\le B} b^2
      \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
  &\ll_{\Theta,C,\epsilon} Q^\epsilon
        \frac{B^2D^2}{D_0A_h^2}
        \sum_{m\le B}\frac{H(m)^2}{m^2}
        \sum_{d\le B}\frac{H_s(d)^2}{\operatorname{rad}(d)}\\
  &\ll_{\Theta,C,\epsilon}Q^\epsilon B^2D^2/(D_0A_h^2).
 \end{split}
 \tag{11}
$$

We use the actual lower gate $d\ge D_0$ and may take smaller intermediate epsilons in the finite subpower budgets.

Apply [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) to restore the original distinct numerator detunings from the common Taylor tests. Retain each output coefficient, of absolute value at most $2^{-n}$ at Taylor order $n$, and each original exterior unit phase. At offset $\ell$, the common seminorms cost $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$ with the original weights, as in R105. Divide by $J\asymp Q$ and square-sum over $|\ell|\le R+1$ in (11). This proves (3), including all three offset factors. At the numerical parameters the prefactor has exponent $39/100+22/25-1/10-9/50=99/100$; it gives $-1/160,-3/800,-19/4000$ in the three terms respectively. No independent restoration or benchmark term of the earlier sharp comparison is altered.

## 5. Strict eligibility after the older large-alias cutoff

Take the second numerical construction of [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six):

$$
d=3\cdot2^e\asymp Q^{1/5},\quad
 3^\ell\asymp Q^{37/200},\quad
 r\asymp Q^{411/1000},\quad
 m\in(B/(2d),B/d)
$$

with $d$ the least such number at least $D_0$, and the distinct odd primes $r,m>3$ chosen as there. Use $k=3^\ell r,\ q=2k,\ b=dm,\ h_q=2\cdot3^\ell,\ s=2^{e+1}3^{\ell+1}$, so $k\asymp Q^{596/1000}$, $(q,b)=6$, and the original and new alias gates hold, with $\operatorname{rad}(d)=6$. Keep the conjugate generators on $r$, the generator $\eta$ and $\eta'=\eta^{2V^*}$ on $m$, and a primitive conjugate pair with trivial tame part on $3^{\ell+1}$. The integer $V^*$ bounds all finitely many relevant fixed log-power ranges. Every previously tested alias and coprime mixed conductor is $r$ or $m$, respectively, as in R105, and the full product remains high on $m$. In particular $r>Q^{51/125}$ and $rm\asymp Q^{601/1000}>Q^{3/5}$.

Change the two-adic partner only. Take primitive sign-trivial $\gamma_2$ with $5$-order $2^{e-1}$ at $2^{e+1}$, and put

$$
\gamma'_2=\gamma_2^{-3+2^{e-1-t}},
          \qquad  t=\left\lfloor\tfrac2{25}\log_2 Q\right\rfloor .
$$

This exponent is odd, so $\gamma'_2$ is primitive. The product exponent $-2+2^{e-1-t}$ has $2$-adic valuation one for large $Q$, so their product still induces the primitive conductor $2^e$ on $d$, and all its earlier small powers have conductor $Q^{1/5-o(1)}$. The local product on $3^{\ell+1}$ is principal, so this is a genuine full-product pair.

For any earlier positive unequal shared exponents $a,c$, the $2$-part exponent is $a-3c+c2^{e-1-t}$. If $a=3c$, its conductor is $2^{t+2-v_2(c)}=Q^{2/25-o(1)}$. Otherwise the valuation is $v_2(a-3c)=O(\log\log Q)$, and the conductor is $Q^{1/5-o(1)}$. The $3$-part has conductor $3^{\ell+1-v_3(a-c)}=Q^{37/200-o(1)}$ by the local law of [R104 §1](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation); the exponent difference is nonzero and polylogarithmic. Thus the earlier R99 small shared cut fails, and all previous three-factor tests with unequal shared exponents, including both R105 thresholds in (4) of that proof, have total conductor at least $Q^{866/1000-o(1)}>Q^{79/100}$. The earlier equal-shared tests have high $2$-part $Q^{1/5-o(1)}$, giving total conductor $Q^{801/1000-o(1)}$, outside their thresholds. The R98 shared-product cut is avoided by the same high $2$-part. The pair is therefore present after all prior masks.

The local primitive-numerator factors are nonzero: the congruence modulo $2$ is automatic on odd units and both two-adic Gauss sums are primitive even after the change. The unchanged $3,r,m$ factors have exactly the finite nonvanishing of [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six), in particular the unique unit frequency at the large $3$-power. Now $(j,u,v,a,c)=(1,2,1,3,1)$ has shared difference two, within (2), and its new total conductor is $rm\,3^{\ell+1}2^{t+2}\asymp Q^{866/1000}<Q^{22/25}$ for large $Q$. This is a genuine new nonzero incidence coefficient on the exact retained input before optional parity deletions, not a lower bound for any integrated packet field.
